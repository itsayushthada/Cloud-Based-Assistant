#! /usr/bin/python36

print("content-type: text/html")
print("\n")

print("""
	<script>
		var data= sessionStorage.getItem("key");
		document.write("<img src='" + data + "'/>")
	</script>
""")

