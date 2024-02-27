from ldap3 import Server, ServerPool, Connection, Tls, SASL, GSSAPI
import ssl

class MyLDAP:
    def __init__(self,
                 ldap_servers: list,
                 base_dn: str,
                 user_attributes: list = ['whencreated','serviceprincipalname','samaccountname',
                                  'pwdlastset','primarygroupid','objectguid','lastlogontimestamp',
                                  'givenname','sn'],
                 paged_size: int = 100
                 ) -> None:
        """Create a new MyLDAP class object

        Args:
            ldap_servers (list): A list of ldap server DNS names
            base_dn (str): The base of the search distinguished name e.g. 'DC=tailspin,DC=com'
            user_attributes (list, optional): A list of LDAP user attributes. Defaults to ['whencreated','serviceprincipalname','samaccountname', 'pwdlastset','primarygroupid','objectguid','lastlogontimestamp', 'givenname','sn'].
            paged_size (int, optional): The page size for LDAP searches. Defaults to 100.
        """
        self.base_dn: str = base_dn
        self.user_attributes: list = user_attributes
        self.paged_size = paged_size
        self.svr_pool = ServerPool(ldap_servers,
                      pool_strategy='ROUND_ROBIN',
                      exhaust=True,
                      active=True)
        self.tls_conf = Tls(validate=ssl.CERT_REQUIRED, version=ssl.PROTOCOL_TLSv1_2)
        # use the currently signed in Windows user name on this read-only connection
        self.ldap_con = Connection(self.svr_pool, authentication=SASL, sasl_mechanism=GSSAPI, 
                                   auto_bind=True, read_only=True, lazy=True)
    
    def is_valid_str(self, s: str) -> bool:
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

    def get_user_by_id(self, user_id: str) -> str:
        """Pass in an AD sAMAccountName (or pattern) and get the attributes back.

        Args:
            user_id (str): AD sAMAccountName (or pattern)

        Returns:
            str: The requested AD user(s) as a string in json format
        """
        ret_val: str = ''
        if self.is_valid_str(user_id):
            search_filter: str = f"(&(objectclass=user)(objectcategory=user)(samaccountname={user_id}))"
            cnt: int = 0
            if (self.ldap_con.search(search_base=self.base_dn,
                            search_scope='SUBTREE', 
                            search_filter=search_filter,
                            attributes=self.user_attributes,
                            paged_size=self.paged_size)):
                ret_val = '{ "users": ['
                ret_val += "\n"
                for entry in self.ldap_con.entries:
                    if cnt > 0:
                        ret_val += ", \n"
                    ret_val += entry.entry_to_json()
                    cnt += 1
                
                ret_val += ']}'
                ret_val = ret_val
        else:
            ret_val = '{"error": "invalid user_id search string"}'

        return ret_val

    def get_users_query(self, first_name: str | None = None, last_name: str | None = None):
        """Pass in a first name and/or a last name to match against.
        e.g. /users/?first_name=Ray*&last_name=Sto*

        Args:
            None

        Returns:
            str: The requested AD user(s) as a str formatted as json data
        """
        ret_val: str = ''
        search_filter: str = '(&(objectclass=user)(objectcategory=user)'
        if first_name:
            if self.is_valid_str(first_name):
                search_filter += f"(givenname={first_name})"
            else:
                ret_val = '{"error": "first_name has invalid characters in it.'
        if last_name:
            if self.is_valid_str(last_name):
                search_filter += f"(sn={last_name})"
            else:
                if len(ret_val) > 3:
                    ret_val += ' last_name also has invalid character in it."}'
                else:
                    ret_val = '{"error": "last_name has invalid characters in it.'

        if len(ret_val) == 0:
            search_filter += ')'
            cnt: int = 0
            if (self.ldap_con.search(search_base=self.base_dn,
                            search_scope='SUBTREE', 
                            search_filter=search_filter,
                            attributes=self.user_attributes,
                            paged_size=self.paged_size)):
                ret_val = '{ "users": ['
                ret_val += "\n"
                for entry in self.ldap_con.entries:
                    if cnt > 0:
                        ret_val += ", \n"
                    ret_val += entry.entry_to_json()
                    cnt += 1

            ret_val += '] }'
            
        return ret_val
