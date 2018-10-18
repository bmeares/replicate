import os
l = []
l.append("rep")
i = 0
l.append(str(i))
l.append(".py")
s = "".join(l)

out = open(s, "w+")
print("weee!")
code = """import os
l = []
l.append(\"rep\")
i = 1
l.append(str(i))
l.append(\".py\")
s = \"\".join(l)
out = open(s, "w+")

code = \"\"\"
import os
os.system(\"python3 replicate.py\")
\"\"\"

out.write(code)
out.close()
command = \"python3 \"
command += s
os.system(command)
"""

out.write(code)
out.close()
command = "python3 "
command += s
os.system(command)
