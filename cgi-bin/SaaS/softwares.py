#! /usr/bin/python36

print("content-type: text/html")
print("\n")

import cgi
import subprocess as sp
from random import randint
from time import sleep

form = cgi.FieldStorage()
software = form.getvalue("software")
username = form.getvalue("username")


print("""
<html>
	<head>
		<title>SaaS</title>
	</head>
	
	<body>	
""")

portno = randint(14000, 65000)

if software == "firefox":
	res1 = sp.getstatusoutput("sudo docker run -dit -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -p {}:22 --name {} firefox:v1&".format(portno, username))
	if res1[0] == 0:
		res2 = sp.getstatusoutput("sudo docker exec {} firefox&".format(username))
		res3 = sp.getstatusoutput("sudo docker exec {0} dbus-uuidgen > /etc/machine-id &".format(username))
		if res3[0] == 0:
			res4 = sp.getstatusoutput("sudo docker ps -a")
			if res4[0] == 0:
				data = (res4[1].split())[1:]
				portno = (data[-2].split("->"))[0].split(":")[1]
				command = """sudo sshpass -p aryan ssh 192.168.43.47 -p {} -o StrictHostKeyChecking=false -X 'dbus-uuidgen > /etc/machine-id; firefox &'""".format(portno)
				
				temp = open("/var/www/cgi-bin/SaaS/ClientFiles/{}.sh".format(portno) , "w+")
				temp.write("#! /usr/bin/sh\n{}".format(command))
				temp.close()
				res5 = sp.getstatusoutput("sudo chmod 0755 /var/www/cgi-bin/SaaS/ClientFiles/{0}.sh".format(portno))
				res5 = sp.getstatusoutput("sudo zip -r /var/www/cgi-bin/SaaS/ClientFiles/{0}.zip /var/www/cgi-bin/SaaS/ClientFiles/{0}.sh".format(portno))
				print(res5)
				if res5[0] == 0:
					url = "http://192.168.43.47/cgi-bin/SaaS/ClientFiles/{0}.zip".format(portno)
					print("""
					<form name="homecoming" action="service.py" method="post">
						<input type="hidden" name="flag" value="1">
						<input type="hidden" name="instruction" value="{0}">
					</form>
					<script>document.forms["homecoming"].submit();</script>
					""".format(url))
			
print("""
	</body>
</html>
""")
