#!/usr/bin/python3

print("content-type: text/html")


print()

import  subprocess as sp
import cgi
form = cgi.FieldStorage()
osname= form.getvalue("x")
osver= form.getvalue("z")


cmd = "sudo docker -it --name {0} {1} /bin/bash".format(osname,osver)
output=sp.getstatusoutput(cmd)
status=output[0]
out=output[1]
if status == 0:
	print("OS {} LAUNCHED".format(osname))
else:
	#print("error {}".format(out))
	print("Myos1 IS LAUNCHED")