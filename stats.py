"""Some simple statistical functions."""

import numbers
import collections
import statistics

def mean(data):
    """Takes the mean/average of a list of numbers, a simple measure of 'middle'.
    See: https://en.wikipedia.org/wiki/Arithmetic_mean"""
    #preconditions
    assert isinstance(data, collections.Iterable), "Must be iterable."
    for num in data:
        assert isinstance(num, numbers.Number), "We need numbers yo."
    assert len(data) > 1, "Please enter at least 2 numbers to be averaged."
    #function
    answer = (sum(data) / len(data))
    #postconditions
    assert isinstance(answer, numbers.Number), "Mean will return a number."
    return answer

def median(data):
    """Finds the median or middle of a list of sorted numbers, a simple measure of 'middle'.
    See: https://en.wikipedia.org/wiki/Median"""
    #preconditions
    assert isinstance(data, collections.Iterable), "Must be iterable."
    for num in data:
        assert isinstance(num, numbers.Number), "We need numbers yo."
    assert len(data) > 2, "Please enter at least 3 numbers to calculate median."
    assert sorted(data) == data, "Numbers must be in order smallest to largest."
    #function
    answer = statistics.median(data)
    #postconditions
    assert isinstance(answer, numbers.Number), "Median will return a number."
    return answer

def range(data):
    """Finds ths range of a list of numbers, a simple measure of variance.
    See: https://www.mathsisfun.com/definitions/range-statistics-.html"""
    pass

def standard_deviation(data):
    """Finds the standard deviation of a list of numbers, a measure of variance.
    See: https://www.mathsisfun.com/data/standard-deviation-formulas.html"""
    pass
