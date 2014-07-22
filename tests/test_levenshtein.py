#!/usr/local/bin/python3.4
# encoding: utf-8

'''
to run tests: python3 runtests.py;

'runtests.py' auto-generated via: py.test --genscript=runtests.py

'''

import warnings
import levenshtein as LV
import pytest


pytest_plugins = "pytest-cov"


warnings.filterwarnings('ignore')




def fnx1(w1, w2):
	return LV.p_levenshtein(w1, w2)



def test_fnx():
	assert fnx1('cat', 'hat') == 1
