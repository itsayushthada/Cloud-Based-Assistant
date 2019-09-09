#! /usr/bin/python36

print("content-type: text/html")
print("\n")

import cgi
import subprocess as sp

form = cgi.FieldStorage()
ips = form.getvalue("net_address")
passwords = form.getvalue("passwords")
server = form.getvalue("server")

ips = ips.split(",")
password_list = []
while 0 < len(passwords):
	x = passwords.find("[")
	y = passwords.find("]")
	password_list.append(passwords[x+1:y])
	passwords = passwords[y+1:]
	
password_dict = {}

for i in range(0,len(password_list)):
	password_dict[ips[i]] = password_list[i]
	
filep = open("/etc/ansible/host/host1", "w")
filep.write("[new_users_list_for_x_session]\n")
for key in password_dict:
	filep.write("{0} ansible_ssh_user=root ansible_ssh_pass={1}\n".format(key, password_dict[key]))
filep.close()
	
if "httpd" in server:
	sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/Servers/playbooks/webserver.yml")
	
if "ftp" in server:
	sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/Servers/playbooks/ftpserver.yml")

if "ldap" in server:
	sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/Servers/playbooks/ldapserver.yml")
	
	

