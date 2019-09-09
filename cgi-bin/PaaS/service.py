#! /usr/bin/python36

print("content-type: text/html")
print("\n")

print("""
	<form method="post" action="plattforms.py">
		Enter the UserName: <input type="text" name="username"/><br>
		Select the Plattform:<br>
		<select name="plattform">
			<option value="jupyter">Jupyter Notebook</option>
			<option value="rstudio">RStudio</option>
			<option value="codeblocks">CodeBlocks</option>
		</select>
		<input type="submit"/>
	</form>
""")

