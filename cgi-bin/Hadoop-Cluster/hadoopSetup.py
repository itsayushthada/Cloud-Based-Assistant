#! /usr/bin/python36

print("content-type: text/html")
print("\n")

import cgi
import subprocess as sp

form = cgi.FieldStorage()

net_address = form.getvalue("net_address")
subnet = form.getvalue("subnet")
master = form.getvalue("master")
master_passwd = form.getvalue("master_passwd")
slave = form.getvalue("slave")
slave_passwd = form.getvalue("slave_passwd")
client = form.getvalue("client")
client_passwd = form.getvalue("client_passwd")
jobtracker = form.getvalue("jobtracker")
jobtracker_passwd = form.getvalue("jobtracker_passwd")

passwords = {}

if subnet == "255.255.255.0":
	master_ip = net_address[:-1]+master
	passwords[master_ip] = master_passwd
	
	temp = open("/etc/ansible/host/host1", "w")
	temp.write("[master_node]\n{} ansible_ssh_user=root ansible_ssh_pass={}\n\n".format(master_ip, passwords[master_ip]))
	
	############################	
	slave_passwd_list = []
	i = 0
	while i < len(slave_passwd):
		x = slave_passwd.find("[")
		y = slave_passwd.find("]")
		slave_passwd_list.append(slave_passwd[x+1:y])
		slave_passwd = slave_passwd[y+1:]
		
	slave = slave.split(",")
	slave_ip = []
	for ip_addr in slave:
		slave_ip.append(net_address[:-1]+ip_addr)
		
	temp.write("[slave_nodes]\n")
	for i in range(0,len(slave_ip)):
		passwords[slave_ip[i]] = slave_passwd_list[i]
		temp.write("{} ansible_ssh_user=root ansible_ssh_pass={}\n".format(slave_ip[i], passwords[slave_ip[i]]))
		
	##############################
	
	client_passwd_list = []
	i = 0
	while i < len(client_passwd):
		x = client_passwd.find("[")
		y = client_passwd.find("]")
		client_passwd_list.append(client_passwd[x+1:y])
		client_passwd = client_passwd[y+1:]
		
	client = client.split(",")
	client_ip = []
	for ip_addr in client:
		client_ip.append(net_address[:-1]+ip_addr)
	
	temp.write("\n[client_nodes]\n")	
	for i in range(0,len(client_ip)):
		passwords[client_ip[i]] = client_passwd_list[i]
		temp.write("{} ansible_ssh_user=root ansible_ssh_pass={}\n".format(client_ip[i], passwords[client_ip[i]]))
		
	################################
	
	jobtracker_ip = net_address[:-1]+jobtracker
	passwords[jobtracker_ip] = jobtracker_passwd
	temp.write("\n[jobtracker_node]\n{} ansible_ssh_user=root ansible_ssh_pass={}\n\n".format(jobtracker_ip, passwords[jobtracker_ip]))
	
def master_setup():
	res1 = sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/Hadoop-Cluster/playbooks/master_node_setup.yml --extra-vars='MASTER_IP={}' &".format(master_ip))
		
def client_setup():
	res1 = sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/Hadoop-Cluster/playbooks/client_node_setup.yml --extra-vars='MASTER_IP={}' &".format(master_ip))
	
def slave_setup():
	res1 = sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/Hadoop-Cluster/playbooks/slave_node_setup.yml --extra-vars='MASTER_IP={}  JOB_IP={}' &".format(master_ip, jobtracker_ip))
	
def jobtracker_setup():
	res1 = sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/Hadoop-Cluster/playbooks/jobtracker_node_setup.yml --extra-vars='MASTER_IP={} JOB_IP={}' &".format(master_ip, jobtracker_ip))
	
a = sp.getstatusoutput("sudo systemctl start hadoopclustersetup.service &")
	
print("""form name="homecoming" action="service.py" method="post"></form>""")
	
