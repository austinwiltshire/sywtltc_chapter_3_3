"""Tests the functions of the stats.py file"""

import stats

def test_mean():
    """Tests the mean function"""
    assert stats.mean([5, 5, 5]) == 5
    assert stats.mean([100, 50]) == 75
    assert stats.mean([10, 20, 30, 40, 50]) == 30
