#! /usr/env python
# -*- coding: utf-8 -*-

"""

Print number of characters in paragraph 

"""
phantom_menace = """Turmoil has engulfed the Galactic Republic. The\
		 taxation of trade routes to outlying star systems is in\
		  dispute. Hoping to resolve the matter with a blockade of deadly\
		   battleships, the greedy Trade Federation has stopped all shipping to\
		    the small planet of Naboo. While the congress of the Republic\
		     endlessly debates this alarming chain of events, the Supreme\
		      Chancellor has secretly dispatched two Jedi Knights, the guardians of\
		       peace and justice in the galaxy, to settle the conflict"""

def run():
	# Utiliser une regexp pour le split
	print(len(phantom_menace.split(" ")))
	print(phantom_menace.split(" "))
if(__name__=='__main__'):
	run()
