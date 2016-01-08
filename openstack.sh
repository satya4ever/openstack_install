#
#
#This script will download RDO latest repo 
#and install it.
#
#Make sure NetworkManager is stop and disabled before running the script
#For e.g.
#systemctl stop NetworkManager;systemctl disable NetworkManager
#
#After that the script will install the openstack using packstack installer
#
#This script is created by Satyajit Bulage.
#
#!/bin/bash
sudo yum install -y  https://www.rdoproject.org/repos/rdo-release.rpm

sudo yum install -y openstack-packstack

sudo packstack --allinone

sudo packstack --answer-file ~/packstack*.txt
