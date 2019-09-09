#! /usr/bin/python36

print("content-type: text/html")
print("\n")

import cgi
import subprocess as sp

print("""
	<form method="post" action="softwares.py">
		Enter the UserName: <input type="text" name="username"/><br>
		Select the Plattform:<br>
		<select name="software">
			<option value="firefox">Mozilla Firefox</option>
			<option value="tableau">Tableau</option>
			<option value="spiderman">Spiderman</option>
		</select>
		<input type="submit"/>
	</form>
""")

form = cgi.FieldStorage()
flag = form.getvalue("flag")
instruction = form.getvalue("instruction")

if flag is not None:
	if int(flag) == 1:
		print("""
		<a href={}>ClickMe</a>
		""".format(instruction))
