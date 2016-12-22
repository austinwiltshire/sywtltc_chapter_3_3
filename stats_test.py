"""Tests the functions of the stats.py file"""

import stats

A = [2, 4, 6]
B = [10, 20]
C = [50, 100, 180, 70]


def test_mean():
    """Tests the mean function"""
    assert stats.mean(A) == 4.0
    assert stats.mean(B) == 15.0
    assert stats.mean(C) == 100.0
