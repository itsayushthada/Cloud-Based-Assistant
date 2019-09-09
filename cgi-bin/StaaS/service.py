#! /usr/bin/python36

print("content-type: text/html")
print("\n")

import cgi
import subprocess as sp

print("""
	<form method="post" action="storage.py">
		Enter the UserName: <input type="text" name="username"/><br><br>
		Enter the Size: <input type="text" name="size_value"/><br><br>
		Select the magnitude:
		<select name="size_order">
			<option value="K">KB</option>
			<option value="M">MB</option>
			<option value="G">GB</option>
		</select><br><br>
		Operation:
		Create<input type="radio" name="operation" value="create">
		Extend<input type="radio" name="operation" value="extend">
		Reduce<input type="radio" name="operation" value="reduce">
		<br><br>
		<input type="submit"/>
		<br>
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
