############# version: v0.11 ##################
############# Author: Kerim ##################
#!/usr/bin/env python

import string
import os
from random import *

#creating a random password with letters,digits and punctiatons
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(choice(characters) for x in range (randint(8,12)))

#input for a comment
name = raw_input("Comment for what this password is for: ")


print "This password is for: %s." % name
print password

# copy password to clipboard
os.system("echo '%s' | pbcopy" % password)
