#
#
#This is a python script which will authenticate the 'admin' tenant.
#
#This script also list all existing network of OpenStack environment.
#
#This script is created by Satyajit Bulage.
#
#!/usr/bin/env python

from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_values
from keystoneclient.v2_0 import client as keystone_client

def get_keystone_client(user, password, tenant):
    params = {
        "username": user,
        "password": password,
        "tenant_name": tenant,
        "auth_url": "http://localhost:35357/v2.0"
    }
    return keystone_client.Client(**params)

tests = [
    {"user": "admin", "password": "password", "tenant": "admin"},
]

for test in tests:
    print "Attempting authentication for tenant %s by user %s" % (
        test['tenant'], test['user']
    ),
    try:
        ks = get_keystone_client(**test)
        print "Authorized"
    except:
        print "Denied"
#
#
#
#Listing All the networks from OpenStack environment.
#
#
print "Listing All Networks."

credentials = get_credentials()
neutron = client.Client(**credentials)
list_network = neutron.list_networks()

print_values(list_network, 'networks')

