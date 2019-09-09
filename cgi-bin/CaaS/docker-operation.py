#! /usr/bin/python36

print("content-type: text/html")
print("\n")

import cgi
import subprocess as sp

form = cgi.FieldStorage()
docker_name = form.getvalue("dockerName")
docker_action = form.getvalue("dockerOperation")
docker_state = form.getvalue("dockerState")
docker_os = form.getvalue("dockerOs")
docker_port = form.getvalue("dockerPort")

if docker_action.lower() == "start" and docker_state.lower() == "down":
	res = sp.getstatusoutput("sudo docker start {}".format(docker_name))
	if res[0] == 0:
		print("""
			<form name="myform" method="post" action=docker-image-list.py>
			<input type='hidden' name='status' value='{}'>
		""".format(2))
		
	else:
		print("""
			<form name="myform" method="post" action=docker-image-list.py>
			<input type='hidden' name='status' value='{}'>
		""".format(3))

elif docker_action.lower() == "stop" and docker_state.lower() == "up":
	res = sp.getstatusoutput("sudo docker stop {}".format(docker_name))
	if res[0] == 0:
		print("""
			<form name="myform" method="post" action=docker-image-list.py>
			<input type='hidden' name='status' value='{}'>
		""".format(4))
		
	else:
		print("""
			<form name="myform" method="post" action=docker-image-list.py>
			<input type='hidden' name='status' value='{}'>
		""".format(5))

elif docker_action.lower() == "delete":
	res = sp.getstatusoutput("sudo docker rm -f {}".format(docker_name))
	if res[0] == 0:
		print("""
			<form name="myform" method="post" action=docker-image-list.py>
			<input type='hidden' name='status' value='{}'>
		""".format(7))
		
	else:
		print("""
			<form name="myform" method="post" action=docker-image-list.py>
			<input type='hidden' name='status' value='{}'>
		""".format(8))
		
elif docker_action.lower() == "display":
	if "shell" not in docker_os:
		print("""
			<form name="myform" method="post" action=docker-image-list.py>
			<input type='hidden' name='status' value='{}'>
		""".format(6))
	
	else:
		serverip = "192.168.43.47"
		print("""
			<script>
				var win = window.open("http://{0}:{1}", '_blank');
				win.focus();
			</script>
			<form name="myform" method="post" action=docker-image-list.py>
			<input type='hidden' name='status' value='{2}'>
		""".format(serverip, docker_port, 9))

	
else:
	print("""
			<form name="myform" method="post" action=docker-image-list.py>
			<input type='hidden' name='status' value='{}'>
		""".format(-1))


		
print("""
<script>
	document.myform.submit()
</script>
""")

