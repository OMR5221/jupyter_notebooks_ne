import ldap3 as ldap

connect = ldap.initialize('ldap://imoasp2.fpl.com')

connect.set_option(ldap.OPT_REFERRALS, 0)


connect.simple_bind_s('OXR0MQY', 'CYB35punk2077!')

result = connect.search_s('cn=OracleContext,dc=somedomain,dc=com',ldap.SCOPE_SUBTREE,'userPrincipalName=user@somedomain.com',['memberOf'])

print(result)
