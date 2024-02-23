from ldap3 import Server, ServerPool, Connection, Tls, SASL, GSSAPI
from os import environ
import ssl
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

"""
Summary:
    A quick and dirty FastAPI and ldap3 web API for AD objects.
    It is a work in progress.

    I used the convention of "g_" and "G_" pre-pended to variable names to indicate global variables.

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
"""

def is_valid_str(s: str) -> bool:
    """determine if we have a valid search string

    Args:
        s (str): the string of characters

    Returns:
        bool: True if valid
    """
    ALLOWED_CHARS: str = "abcdefghijklmnopqrstuvwxyz0123456789*'"
    ret_val: bool = True
    for c in s.lower():
        if c not in ALLOWED_CHARS:
            ret_val = False
            break
    
    return ret_val


API_VERSION: str = '1.0'
myad = FastAPI()

# automatically bind to port 636 on an AD server using TLS v1.2 encryption
try:
    g_ldap_servers: list = environ['LDAP_SERVERS'].split(',')
except KeyError:
    print('Please define the "LDAP_SERVERS" environment variable to a comma-separated list of server names.')
    raise

g_svr_pool = ServerPool(g_ldap_servers,
                      pool_strategy='ROUND_ROBIN',
                      exhaust=True,
                      active=True)
g_tls_conf = Tls(validate=ssl.CERT_REQUIRED, version=ssl.PROTOCOL_TLSv1_2)

# use the currently signed in Windows user name on this read-only connection
g_ldap_con = Connection(g_svr_pool, authentication=SASL, sasl_mechanism=GSSAPI, 
                auto_bind=True, read_only=True, lazy=True)

# Set the default page size for searches so we don't overwhelm the AD servers
G_DEFAULT_PAGED_SIZE: int = 100
g_paged_size: int = G_DEFAULT_PAGED_SIZE
try:
    g_paged_size = int(environ['LDAP_PAGED_SIZE'])
except KeyError:
    print('WARNING: "LDAP_PAGED_SIZE" environment variable missing.', f"Using {G_DEFAULT_PAGED_SIZE} instead.")
    g_paged_size = G_DEFAULT_PAGED_SIZE
except ValueError:
    print('WARNING: "LDAP_PAGED_SIZE" environment variable had an invalid integer value.', f"Using {G_DEFAULT_PAGED_SIZE} instead.")
    g_paged_size = G_DEFAULT_PAGED_SIZE

G_DEFAULT_USER_ATTRIBUTES: tuple = ('whencreated','serviceprincipalname','samaccountname',
                                  'pwdlastset','primarygroupid','objectguid','lastlogontimestamp','givenname','sn')
g_user_attributes: list = ()
try:
    g_user_attributes = environ['LDAP_USER_ATTRIBUTES'].split(',')
except KeyError:
    print('WARNING: "LDAP_USER_ATTRIBUTES" environment variable missing.', f"Using {G_DEFAULT_USER_ATTRIBUTES} instead")
    g_user_attributes = list(G_DEFAULT_USER_ATTRIBUTES)

base_dn: str = ''
try:
    base_dn = environ['LDAP_BASE_DN']
except KeyError:
    print('ERROR - Please define the "BASE_DN" environment variable to a valid DN. e.g. DC=tailspin,DC=com')
    raise


@myad.get("/")
def read_root():
    return {'version': API_VERSION}

# I'm manually formatting the json strings; so, I don't want FastAPI to do it for me
@myad.get("/users/{user_id}", response_class=PlainTextResponse)
def get_user(user_id: str):
    """Pass in an AD sAMAccountName (or pattern) and get the attributes back.

    Args:
        user_id (str): AD sAMAccountName (or pattern)

    Returns:
        json: The requested AD user(s) in json data
    """
    ret_val: str = ''
    if is_valid_str(user_id):
        search_filter: str = f"(&(objectclass=user)(objectcategory=user)(samaccountname={user_id}))"
        cnt: int = 0
        if (g_ldap_con.search(search_base=base_dn,
                        search_scope='SUBTREE', 
                        search_filter=search_filter,
                        attributes=g_user_attributes,
                        paged_size=g_paged_size)):
            ret_val = '{ "users": ['
            ret_val += "\n"
            for entry in g_ldap_con.entries:
                if cnt > 0:
                    ret_val += ", \n"
                ret_val += entry.entry_to_json()
                cnt += 1
            
            ret_val += ']}'
            ret_val = ret_val
    else:
        ret_val = '{"error": "invalid user_id search string"}'

    return ret_val

# I'm manually formatting the json strings; so, I don't want FastAPI to do it for me
@myad.get("/users/", response_class=PlainTextResponse)
def get_users_query(first_name: str | None = None, last_name: str | None = None):
    """Pass in a first name and/or a last name to match against.
       e.g. /users/?first_name=Ray*&last_name=Sto*

    Args:
        None

    Returns:
        json: The requested AD user(s) in json data
    """
    ret_val: str = ''
    search_filter: str = '(&(objectclass=user)(objectcategory=user)'
    if first_name:
        if is_valid_str(first_name):
            search_filter += f"(givenname={first_name})"
        else:
            ret_val = '{"error": "first_name has invalid characters in it.'
    if last_name:
        if is_valid_str(last_name):
            search_filter += f"(sn={last_name})"
        else:
            if len(ret_val) > 3:
                ret_val += ' last_name also has invalid character in it."}'
            else:
                ret_val = '{"error": "last_name has invalid characters in it.'

    if len(ret_val) == 0:
        search_filter += ')'
        cnt: int = 0
        if (g_ldap_con.search(search_base=base_dn,
                        search_scope='SUBTREE', 
                        search_filter=search_filter,
                        attributes=g_user_attributes,
                        paged_size=g_paged_size)):
            ret_val = '{ "users": ['
            ret_val += "\n"
            for entry in g_ldap_con.entries:
                if cnt > 0:
                    ret_val += ", \n"
                ret_val += entry.entry_to_json()
                cnt += 1

        ret_val += '] }'
        
    return ret_val
