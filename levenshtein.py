#!/usr/local/bin/python3.4
# encoding: utf-8

import string
import numpy as NP
from functools import partial



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


p_levenshtein = partial(w1, w2,
	LuT = {k:v for v, k in enumerate(string.ascii_lowercase)})
