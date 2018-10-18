import os
# create replicate.py via bash
code = "import os\nimport sys\nl = []\nl.append(\"rep\")\ni = 0\nl.append(str(i))\nl.append(\".py\")\ns = \"\".join(l)\n"
code += "out = open(s, \"w+\")\nprint(\"instance \" + str(int(sys.argv[1])))\ncode = \"\"\"import os\nimport sys\nl = []\n"
code += "l.append(\\\"rep\\\")\ni = 1\nl.append(str(i))\nl.append(\\\".py\\\")\ns = \\\"\\\".join(l)\nout = open(s, \"w+\")\n"
code += "code = \\\"\\\"\\\"import os\nimport sys\ncommand = \\\"python3 replicate.py \\\" + str(int(sys.argv[1]))\nos.system(command)\n"
code += "\\\"\\\"\\\"\nout.write(code)\nout.close()\ncommand = \\\"python3 \\\" + s + \\\" \\\" + str(int(sys.argv[1]) + 1)\nos.system(command)\n"
code += "\"\"\"\nout.write(code)\nout.close()\ncommand = \"python3 \" + s + \" \" + sys.argv[1]\nos.system(command)"
echo = "echo \'"
end = "\' > replicate.py"
os.system(echo + code + end)
os.system("python3 replicate.py 1")
