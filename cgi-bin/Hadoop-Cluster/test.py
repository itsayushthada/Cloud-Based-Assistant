#! /usr/bin/python36

print("content-text: text/html")
print("\n")

import subprocess as sp

a = sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/Hadoop-Cluster/playbooks/master_node_setup.yml")

print(a)
