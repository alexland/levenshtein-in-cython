#!/usr/local/bin/python3.4
# encoding: utf-8

'''
to run tests: python3 runtests.py;

'runtests.py' auto-generated via: py.test --genscript=runtests.py

'''

import warnings
import os
import pytest

warnings.filterwarnings('ignore')

def import_pkg_modules ():
    import sys
    this_file = __file__
    x = os.path.dirname(this_file)
    x = os.path.dirname(x)
    mod_lib = os.path.join(x, 'levpy')
    sys.path.append(mod_lib)

import_pkg_modules()
import hamming as HM


def fnx1(s1, s2):
	return HM.hamming(s1, s2)



def test_fnx():
	assert fnx1('maid', 'make') == 1
