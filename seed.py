import os
out = open("replicate.py", "w+")
out.close()
cm0 = "echo \'import os\' > replicate.py"
cm1 = "echo \'l = []\' >> replicate.py"
cm2 = "echo \'l.append(\"rep\")\' >> replicate.py"
cm3 = "echo \'i = 0\' >> replicate.py"
cm4 = "echo \'l.append(str(i))\' >> replicate.py"
cm5 = "echo \'l.append(\".py\")\' >> replicate.py"
cm6 = "echo \'s = \"\".join(l)\' >> replicate.py"
cm7 = "echo \'out = open(s, \"w+\")\' >> replicate.py"
cm8 = "echo \'print(\"wee!\")\' >> replicate.py"
cm9 = "echo \'code = \"\"\"import os\' >> replicate.py"
cm10 = "echo \'l = []\' >> replicate.py"
cm11 = "echo \'l.append(\\\"rep\\\")\' >> replicate.py"
cm12 = "echo \'i = 1\' >> replicate.py"
cm13 = "echo \'l.append(str(i))\' >> replicate.py"
cm14 = "echo \'l.append(\\\".py\\\")\' >> replicate.py"
cm15 = "echo \'s = \\\"\\\".join(l)\' >> replicate.py"
cm16 = "echo \'out = open(s, \"w+\")\' >> replicate.py"
cm17 = "echo \'code = \\\"\\\"\\\"\' >> replicate.py"
cm18 = "echo \'import os\' >> replicate.py"
cm19 = "echo \'os.system(\\\"python3 replicate.py\\\")\' >> replicate.py"
cm20 = "echo \'\\\"\\\"\\\"\' >> replicate.py"
cm21 = "echo \'out.write(code)\' >> replicate.py"
cm22 = "echo \'out.close()\' >> replicate.py"
cm23 = "echo \'command = \\\"python3 \\\"\' >> replicate.py"
cm24 = "echo \'command += s\' >> replicate.py"
cm25 = "echo \'os.system(command)\' >> replicate.py"
cm26 = "echo \'\"\"\"\' >> replicate.py"
cm27 = "echo \'out.write(code)\' >> replicate.py"
cm28 = "echo \'out.close()\' >> replicate.py"
cm29 = "echo \'command = \"python3 \"\' >> replicate.py"
cm30 = "echo \'command += s\' >> replicate.py"
cm31 = "echo \'os.system(command)\' >> replicate.py"
for i in range(32):
    name = "cm"
    name += str(i)
    w = "os.system(" + name + ")"
    exec(w)

os.system("python3 replicate.py")
