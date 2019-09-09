#! /usr/bin/python36

print("content-type: text/html")
print("\n")

print("""
	<form method="post" action="servers.py">
		Enter the Ip Address(es): <input type="text" name="net_address"/><br><br>
		Enter the Respective Passwords(Each password in [...]): <input type="text" name="passwords"/><br><br>
		Select the Server(s) to be installed:<br>
		<input type="checkbox" name="server" value="httpd"/>Web-Server
		<input type="checkbox" name="server" value="ftp"/>FTP-Server
		<input type="checkbox" name="server" value="ldap"/>LDAP-Server
		<br><br>
		<input type="reset"/>
		<input type="submit"/>
	</form>
""")

