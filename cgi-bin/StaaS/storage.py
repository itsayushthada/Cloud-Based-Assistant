#! /usr/bin/python36

print("content-type: text/html")
print("\n")

import cgi
import subprocess as sp
from random import randint
from time import sleep

form = cgi.FieldStorage()
username = form.getvalue("username")
size_value = form.getvalue("size_value")
size_order = form.getvalue("size_order")
operation = form.getvalue("operation")
clientIP = "192.168.43.146"

if operation == "create":
	res1 = sp.getstatusoutput("sudo lvcreate --name {} --size {} myVG".format(username, size_value+size_order))
	if res1[0] == 0:
		res2 = sp.getstatusoutput("sudo mkfs.ext4 /dev/myVG/{}".format(username))
		if res2[0] == 0:
			res3 = sp.getstatusoutput("sudo mkdir /cloud/{};sudo chown -R apache /cloud;".format(username))
			if res3[0] == 0:
				res4 = sp.getstatusoutput("""sudo ansible localhost -m mount -a "src=/dev/myVG/{0} path=/cloud/{0} fstype=ext4  state=mounted" """.format(username))
				if res4[0] == 0:
					res5 = sp.getstatusoutput(""" sudo echo "/cloud/{} 192.146.43.73(rw,no_root_squash)" | sudo tee /etc/exports""".format("himani"))
					res5 = sp.getstatusoutput("sudo systemctl restart nfs")
					command = """
					mkdir /media/mydrive-{0}
					mount 192.168.43.47:/cloud/{0} /media/mydrive-{0}
					""".format(username)
					temp = open("/var/www/cgi-bin/StaaS/ClientFiles/{}.sh".format(username) , "w+")
					temp.write("#! /usr/bin/sh\n{}".format(command))
					temp.close()
					res5 = sp.getstatusoutput("sudo chmod 0755 /var/www/cgi-bin/StaaS/ClientFiles/{0}.sh".format(username))
					res5 = sp.getstatusoutput("sudo zip -r /var/www/cgi-bin/StaaS/ClientFiles/{0}.zip /var/www/cgi-bin/StaaS/ClientFiles/{0}.sh".format(username))
					if res5[0] == 0:
						url = "http://192.168.43.47/cgi-bin/StaaS/ClientFiles/{0}.zip".format(username)
						print("""
		<form name="homecoming" action="service.py" method="post">
			<input type="hidden" name="flag" value="1">
			<input type="hidden" name="instruction" value="{0}">
		</form>
		<script>document.forms["homecoming"].submit();</script>""".format(url))	

if operation == "extend":
	res1 = sp.getstatusoutput("sudo lvextend --size +{0}{1} /dev/myVG/{2}".format(size_value,size_order, username))
	if res1[0] == 0:
		res2 = sp.getstatusoutput("sudo resize2fs /dev/myVG/{}".format(username))
		print("""
		<form name="homecoming" action="service.py" method="post"></form>
		<script>document.forms["homecoming"].submit();</script>""")	
								
elif operation == "reduce":
	res1 = sp.getstatusoutput("""sudo ansible localhost -m mount -a "src=/dev/myVG/{0} path=/cloud/{0} fstype=ext4  state=unmounted" """.format(username))
	if res1[0] == 0:
		res2 = sp.getstatusoutput(""" sudo ansible localhost -m lvol -a "vg=myVG lv={} size=400m force=yes resizefs=yes"  """.format(username))
		if res2[0] == 0:
			res3 = sp.getstatusoutput("""sudo ansible localhost -m mount -a "src=/dev/myVG/{0} path=/cloud/{0} fstype=ext4  state=mounted" """.format(username))
			print("""
		<form name="homecoming" action="service.py" method="post"></form>
		<script>document.forms["homecoming"].submit();</script>""")	
									
print("""
<html>
	<head>
		<title>StaaS</title>
	</head>
	
	<body>	
""")



print("""
	</body>
</html>
""")
