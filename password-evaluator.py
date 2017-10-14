#!/usr/bin/env python
import sys
'''
	Password evaluator -- checks validity of passwords against following requirements:
		1. Minimum 8 characters
		2. Maximum 64 characters
		3. Only allows ASCII characters
		4. Does not match list of common passwords passed to program
		
'''
# Construct list of common passwords to avoid
common_passwords = {}

for line in sys.stdin:
	if line in common_passwords:
		continue
	common_passwords[line] = 1



# Must only follow ascii characters
def isAscii(text):
	try:
		text.decode('ascii')
	except UnicodeDecodeError:
		return False
	else:
		return True

file = open(sys.argv[1], 'r')
lines = file.read().split('\n')

for line in lines:
	# Must be maximum 64 characters
	if len(line) > 64:
		print "%s -> Error: too long" % (line)
		continue
	# Must be mininum 8 characters
	if len(line) < 8:
		print "%s -> Error: too short" % (line)
		continue
	# Must not match common passwords
	if line in common_passwords:
		print "%s -> Error: Too common" % (line)
	if isAscii(line) == False:
		print "%s -> Error: invalid characters" % (line)

file.close()


# print common_passwords