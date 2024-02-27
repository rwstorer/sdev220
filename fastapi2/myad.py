from os import environ
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from myldap import MyLDAP

"""
Summary:
    A quick and dirty FastAPI and ldap3 web API for AD objects.
    It is a work in progress.

Environment Variables Required:
    LDAP_SERVERS
    LDAP_BASE_DN

Environment Variables Optional:
    LDAP_USER_ATTRIBUTES
    LDAP_PAGED_SIZE

Run:
    uvicorn adnd_ldap:myad

History:
    When                Who         What
    ----                ---         ----
    2024-02-22T17:00    Ray         Initial
    2024-02-27T11:00    Ray         Moved LDAP to a class
"""

API_VERSION: str = '1.0'
myad = FastAPI()

# automatically bind to port 636 on an AD server using TLS v1.2 encryption
try:
    myldap = MyLDAP(environ['LDAP_SERVERS'].split(','), environ['LDAP_BASE_DN'],
                    environ['LDAP_USER_ATTRIBUTES'].split(','), int(environ['LDAP_PAGED_SIZE']))
except KeyError:
    print("Optional environment variables:\n",
          "'LDAP_USER_ATTRIBUTES'--comma separated list of LDAP user attributes\n"
          "'LDAP_PAGED_SIZE'--an integer for the LDAP search page size")
    try:
        myldap = MyLDAP(environ['LDAP_SERVERS'].split(','), environ['LDAP_BASE_DN'])
    except KeyError:
        print("Required environment variables:\n",
            "'LDAP_SERVERS'--comma separated list\n",
            "'LDAP_BASE_DN'--e.g. DC=tailspin,DC=com")
        raise

@myad.get("/")
def read_root():
    return {'version': API_VERSION}

# I'm manually formatting the json strings; so, I don't want FastAPI to do it for me
@myad.get("/users/{user_id}", response_class=PlainTextResponse)
def get_user(user_id: str) -> str:
    """Search for the user_id

    Args:
        user_id (str): The LDAP attribute samaccountname

    Returns:
        str: The user(s) that match the samaccountname query string
    """
    return myldap.get_user_by_id(user_id)

# I'm manually formatting the json strings; so, I don't want FastAPI to do it for me
@myad.get("/users/", response_class=PlainTextResponse)
def get_users_query(first_name: str | None = None, last_name: str | None = None) -> str:
    """Pass the first_name, the last_name, or both.

    Args:
        first_name (str | None, optional): The LDAP first name. Defaults to None.
        last_name (str | None, optional): The LDAP last name. Defaults to None.

    Returns:
        str: The users and attributes as a JSON formatted str
    """
    return myldap.get_users_query(first_name, last_name)
