#!/usr/local/bin/python3.4
# encoding: utf-8

import os
import sys
import string
import warnings
import numpy as NP
from functools import partial

import sys
sys.path.append("./")

warnings.filterwarnings('ignore')


def determine_path ():
    """
	modified from https://wiki.python.org/moin/Distutils/Tutorial

	"""
	try:
		root = __file__
        if os.path.islink (root):
            root = os.path.realpath (root)
        return os.path.dirname (os.path.abspath (root))
    except:
        print "something is wrong"
        print "no __file__ variable. please contact package author"
        sys.exit ()


def start ():
    print "module is running"
    print determine_path ()
    files = [f for f in os.listdir(determine_path () + "/assets")]
    print files


def levenshtein(w1, w2, LuT):
	'''
	returns: levenshtein distance as int
	pass in: two words as python strings;
	this fn for the easy case in which word lengths are equal;
	'''
	lw1, lw2 = len(w1), len(w2)
	if lw1 != lw2:
		return 'the two words do not have equal length'

	w1, w2 = w1.lower(), w2.lower()
	t1 = NP.array([LuT[chr] for chr in w1])
	t2 = NP.array([LuT[chr] for chr in w2])
	tdiff = t2 - t1
	return NP.where(tdiff==0, 0, 1).sum()


p_levenshtein = partial(levenshtein,
	LuT = {k:v for v, k in enumerate(string.ascii_lowercase)})



if __name__ == "__main__":
	print "now what?"
