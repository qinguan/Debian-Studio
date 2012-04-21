#!/usr/bin/python

import os
from random import Random

virtual_image_info_dic = {
	"arch":None,
	"bootappend":None,
	"config":"/etc/debootstrap/config",
	"chroot-scripts":None,
	"confdir":"/etc/debootstrap",
	"debconf":None,
	"debopt":None,
	"filesystem":None,
	"hostname":"xuguojun_test",
	"iso":None,
	"mirror":"http://mirrors.163.com/debian",
	"packages":"/etc/debootstrap/debian.packages",
	"password":"123",
	"release":None,#sequeeze
	"vmsize":"1G",
	"pre-scripts":None,
	"scripts":None,
	"target":"/mnt/test/test.img"
#	verbose
#	insecure
#	keep_src_list
#	nodebootstrap
#	nopackages
#	nopassword
}


def random_str(randomlength=8):
	"""generate a random string for file name"""

	str = ''
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	length = len(chars)-1
	random = Random()

	return "".join(random.sample(chars,randomlength))

#	for i in range(randomlength):
#		str += chars[random.randint(0,length)]
#	return str

#test:
#t = random_str()
#os.system( "echo 'hello' > /tmp/" + t)
#if(os.path.exists("/tmp/"+t)):
#	print "OK"

def generate_script(param):
	"""generate a script for generating virtual image."""
	""" param:Command line arguments"""

	if(os.path.exists("/etc/debootstrap/packages")):
		temp_packages = "/tmp/" + random_str()
		os.system("cat /etc/debootstrap/packages > " + temp_packages)
		param["packages"] = temp_packages

	for root,dirs,files in os.walk("/etc/debootstrap/extrapackages"):
		if(len(files) != 0 ):
			for file in files:
				os.system("cat " + file + " >> " + temp_packages)

	#generate the script name
	scriptname = random_str()

	os.system("echo '#!/bin/bash'> " + scriptname)

	try:
		cmd = ""
		if(os.path.exists("/usr/sbin/grml-debootstrap")):
			cmd += "/usr/sbin/grml-debootstrap --vmfile"

		for k in param.keys():
			if(param[k] != None):
				cmd += " --" + k + " " + param[k]

		os.system("echo " + cmd + " >> " + scriptname)
		os.system("chmod 755 " + scriptname)
		return scriptname,temp_packages

	except:
		os.system("rm " + scriptname)
		os.system("rm " + temp_packages)
		print "something wrong occures in command generation."


#test:
generate_script(virtual_image_info_dic)
	
	
