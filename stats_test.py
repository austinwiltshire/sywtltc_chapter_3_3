"""Tests the functions of the stats.py file"""

import stats

A = [2, 4, 6]
B = [10, 20]
C = [50, 100, 180, 70]
D = [1, 2, 3, 4, 5]
E = [10, 20, 50, 80, 100]
F = [1, 1, 1]
G = [1, 2, 3, 4, 5, 6]


def test_mean():
    """Tests the mean function"""
    assert stats.mean(A) == 4.0
    assert stats.mean(B) == 15.0
    assert stats.mean(C) == 100.0
    assert stats.mean(F) == 1.0

def test_median():
    """Tests the median function"""
    assert stats.median(A) == 4.0
    assert stats.median(D) == 3.0
    assert stats.median(E) == 50
    assert stats.median(F) == 1.0
    assert stats.median(G) == 3.5

def test_range_():
    """Tests the range function"""
    assert stats.range_(A) == 4.0
    assert stats.range_(B) == 10.0
    assert stats.range_(C) == 130.0

def test_standard_deviation():
    """Tests the SD function"""
    assert stats.standard_deviation(A) == 2.0
    assert stats.standard_deviation(B) == 7.07107
    assert stats.standard_deviation(E) == 38.34058
