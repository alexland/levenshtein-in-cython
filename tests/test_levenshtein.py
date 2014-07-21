#!/usr/local/bin/python3.4
# encoding: utf-8

'''
to run tests: python3 runtests.py;

'runtests.py' auto-generated via: py.test --genscript=runtests.py

'''


import levenshtein as LV
import pytest






def fnx1(w1, w2):
	return LV.levenshtein(w1, w2)



def test_fnx():
	assert fnx1('cat', 'hat') == 1
