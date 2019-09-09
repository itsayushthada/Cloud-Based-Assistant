#! /usr/bin/python36

print("content-type: text/html")
print("\n")

import cgi
import subprocess as sp
from random import randint
from time import sleep

form = cgi.FieldStorage()
plattform = form.getvalue("plattform")
username = form.getvalue("username")

print("""
<html>
	<head>
		<title>PaaS</title>
	</head>
	
	<body>
		You are on the Service page.	
""")

portno = randint(10000, 65000)

if plattform == "jupyter":
	res1 = sp.getstatusoutput("sudo docker run -dit --name {0} -p {1}:8888 deeplearning:v1&".format(username, portno))
	if res1[0] == 0:
		res2 = sp.call("sudo docker exec {} jupyter notebook --allow-root --ip=0.0.0.0&".format(username), shell=True)
		if res2 == 0:
			res3 = sp.getstatusoutput("sudo docker ps -a")
			if res3[0] == 0:
				data = (res3[1].split())[1:]
				portno = (data[-2].split("->"))[0].split(":")[1]
				while True:
					res4 = sp.getstatusoutput("sudo docker exec {} jupyter notebook list".format(username))
					if ":8888/" in res4[1]:
						break
				url = "http://0.0.0.0:" + str(portno) + "/?" + (res4[1].split("http://0.0.0.0:8888/?")[1]).split(" ::")[0]
				
				print("""
				<form name="homecoming" action="service.py">
				</form>
								
				<script>
					var win = window.open("{}", "_blank");
					win.focus();
					document.forms["homecoming"].submit();
				</script>
				""".format(url))
				
elif plattform == "rstudio":
	res1 = sp.getstatusoutput("sudo docker run -dit -p {1}:8787 --name {0} rstudio:v1".format(username, portno))
	if res1[0] == 0:
		url = "http://192.168.43.47:{}/auth-sign-in".format(portno)

		print("""
		<form name="homecoming" action="service.py">
		</form>
				
		<script>
			var win = window.open("{}", "_blank");
			win.focus();
			document.forms["homecoming"].submit();
		</script>
		""".format(url))
								
print("""
	</body>
</html>
""")
