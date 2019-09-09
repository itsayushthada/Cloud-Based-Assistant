#! /usr/bin/python36

print("content-type: text/html")
print("\n")

import subprocess as sp
import cgi

status = cgi.FieldStorage()
c = status.getvalue("status")
if c is not None:
	c = int(c)
	if c == 0:
		print("""<script>window.alert("Container Launched Successfully.")</script>""")
	elif c==1:
		print("""<script>window.alert("Container couldn't be Launched.")</script>""")
	elif c==2:
		print("""<script>window.alert("Container Started Successfully.")</script>""")
	elif c==3:
		print("""<script>window.alert("Container couldn't be Started.")</script>""")
	elif c==4:
		print("""<script>window.alert("Container Stopped Successfully.")</script>""")
	elif c==5:
		print("""<script>window.alert("Container couldn't be Stopped.")</script>""")
	elif c==6:
		print("""<script>window.alert("Container doesn't Support this Operation.")</script>""")
	elif c==7:
		print("""<script>window.alert("Container Deleted Successfully.")</script>""")
	elif c==8:
		print("""<script>window.alert("Container couldn't be Deleted.")</script>""")
	elif c==9:
		print("""<script>window.alert("Container started in a New Tab.")</script>""")

print("""
<script>
	function dockerAction(id, action, state,os)
	{
		document.forms["myform"]["dockerName"].value = id; 
		document.forms["myform"]["dockerOperation"].value = action
		document.forms["myform"]["dockerState"].value = state
		document.forms["myform"]["dockerOs"].value = os
		document.forms["myform"]["dockerPort"].value = document.getElementById(id).value
		document.forms["myform"].submit();
	}
</script>
""")

print("""

<form action="CaaS.py">
        Container Name: <input type="text" name="username"/>
        <br>
        Image: 
        <select  name="image">
""")

img_list = sp.getoutput("sudo docker images")
img_list = img_list.split("\n")
img_list = img_list[1:]

for i in img_list:
	x = i.split()
	print("<option>")
	print(x[0] + ":" + x[1])
	print("</option>")

print("""
        </select>
        <br>
        <input type="submit"/>
        <input type="reset" />
</form>
<br>
""")

print("Tables <br>")
dstatus = sp.getoutput("sudo docker ps -a")
dstatus = dstatus.split("\n")
dstatus = dstatus[1:]

print("""<table border=1 align='center' width='80%' style='border-collapse: collapse'>
<tr>
	<td>Operating System</td>
	<td>Container Name</td>
	<td>Status</td>
	<td>Start</td>
	<td>Stop</td>
	<td>Console</td>
	<td>Delete</td>
	<td>Port</td>
</tr>""")

print("""
	<form name="myform" method="post" action="docker-operation.py">
		<input type=hidden name="dockerName">
		<input type=hidden name="dockerOperation">
		<input type=hidden name="dockerState">
		<input type=hidden name="dockerOs">
		<input type=hidden name="dockerPort">
	</form>
""")

for i in dstatus:
	if "Created" not in i:
		print("<tr>")
		temp = i.split()
		print("<td>" + temp[1] + " </td>")
		print("<td>" + temp[-1] + "</td>")
		print("<td>")
		if "Exited" in i:
			print("Down")
			portno = 0
			
		elif "Up" in i:
			print("Up")
			portno = (temp[-2].split("->")[0]).split(":")[1]

		print("</td>")
		if "Exited" in i:
			print("""<td><a href = '#' onclick='dockerAction("{0}","start","Down","{1}")'> Start </a></td>""".format(temp[0],temp[1]))
			print("""<td><a href = '#' onclick='dockerAction("{0}","stop","Down","{1}")'> Stop </a></td>""".format(temp[0],temp[1]))
			print("""<td><a href = '#' onclick='dockerAction("{0}","display","Down","{1}")'> Console </a></td>""".format(temp[0],temp[1]))
			print("""<td><a href = '#' onclick='dockerAction("{0}","delete","Down","{1}")'> Delete </a></td>""".format(temp[0],temp[1]))
		elif "Up" in i:
			print("""<td><a href = '#' onclick='dockerAction("{0}","start","Up","{1}")'> Start </a></td>""".format(temp[0],temp[1]))
			print("""<td><a href = '#' onclick='dockerAction("{0}", "stop","Up","{1}")'> Stop </a></td>""".format(temp[0],temp[1]))
			print("""<td><a href = '#' onclick='dockerAction("{0}", "display","Up","{1}")'> Console </a></td>""".format(temp[0],temp[1],))
			print("""<td><a href = '#' onclick='dockerAction("{0}", "delete","Up","{1}")'> Delete </a></td>""".format(temp[0],temp[1]))
		print("""<td>{}</td>""".format(portno))
		print("""<input type="hidden" id="{0}" value="{1}">""".format(temp[0], portno))
		print("</tr>")

print("</table>")
