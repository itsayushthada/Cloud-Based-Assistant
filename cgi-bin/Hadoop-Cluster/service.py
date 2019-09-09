#! /usr/bin/python36

print("content-type: text/html")
print("\n")

print("""
	<form method="post" action="hadoopSetup.py">
		Enter the Network Address: <input type="text" name="net_address"/><br>
		Enter the Subnet Mask: <input type="text" name="subnet"/><br>
		Enter the Master's Host Address: <input type="text" name="master"/><br>
		Enter the Master's Host Password: <input type="text" name="master_passwd"/><br>
		Enter the Slaves' Host Address: <input type="text" name="slave"/><br>
		Enter the Slaves' Host Password(Each password in [...]): <input type="text" name="slave_passwd"/><br>
		Enter the Clients' Host Address: <input type="text" name="client"/><br>
		Enter the Clients' Host Password(Each password in [...]): <input type="text" name="client_passwd"/><br>
		Enter the Job Tracker's Host Address: <input type="text" name="jobtracker"/><br>
		Enter the Job Tracker's Host Password: <input type="text" name="jobtracker_passwd"/><br>
		<input type="reset"/>
		<input type="submit"/>
	</form>
""")

