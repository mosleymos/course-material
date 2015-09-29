#! /usr/env python
# -*- coding: utf-8 -*-

"""

Print a inverse alphabet with uppercase vowels  

"""


def run():
	result=""
	for lettre in map(chr,range(97,123))[::-1]:
		if((lettre=='a'or lettre == 'e') or ( lettre =='i' or lettre=='o') ):
			result+=(lettre.upper())
		else:
			result+=(lettre)
	print(result)
if(__name__=='__main__'):
	run()

