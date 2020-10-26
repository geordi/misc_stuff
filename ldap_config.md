## Local LDAP Auth Config


### Packages

```
libldap-common
libpam-ldap
ldap-auth-config
ldap-auth-client
libnss-ldap
```

- Configure `/etc/ldap.conf` to point to your LDAP server
- Configure `/etc/nsswitch.conf` - to use `ldap` for auth


### Homedir

- `/etc/pam.d/common-session` add `session	optional			pam_mkhomedir.so` to the end of file
- `/usr/share/pam-config/mkhomedir` must exist with the proper content
