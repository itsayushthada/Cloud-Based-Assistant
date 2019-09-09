#! /usr/bin/python36
print("content-type: text/html")

import cgi
import subprocess as sp
from random import randint

form = cgi.FieldStorage()
username = form.getvalue("username")
image = form.getvalue("image")
portno = randint(49152,65535)
res = sp.getstatusoutput("date")

while True:
	res = sp.getstatusoutput("sudo docker run -dit -p {}:4200 --name {} {}".format(portno, username, image))
	if "Error response" in res[1]:
		rm = sp.getstatusoutput("sudo docker rm -f {}".format(username))
	else:
		break

if res[0] == 0:
	print("""
		<form name="myform" method="post" action=docker-image-list.py>
		<input type='hidden' name='status' value='{}'>
	""".format(0))

else:
	print("""
		<form name="myform" method="post" action=docker-image-list.py>
		<input type='hidden' name='status' value='{}'>
	""".format(1))
	
print("""
<script>
	document.myform.submit()
</script>
""")
