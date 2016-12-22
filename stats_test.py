"""Tests the functions of the stats.py file"""

import stats

A = [2, 4, 6]
B = [10, 20]
C = [50, 100, 180, 70]
D = [1, 2, 3, 4, 5]
E = [10, 20, 50, 80, 100]


def test_mean():
    """Tests the mean function"""
    assert stats.mean(A) == 4.0
    assert stats.mean(B) == 15.0
    assert stats.mean(C) == 100.0

def test_median():
    """Tests the median function"""
    assert stats.median(A) == 4.0
    assert stats.median(D) == 3.0
    assert stats.median(E) == 50
