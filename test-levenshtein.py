

import levenshtein as LV
import pytest



def fnx1(w1, w2):
	return LV.levenshtein(w1, w2)



def test_fnx():
	assert fnx1('cat', 'hat') == 1
