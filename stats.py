"""Some simple statistical functions."""

import numbers
import collections

def mean(numbers):
    """Takes the mean/average of a list of numbers, a simple measure of 'middle'.
    See: https://en.wikipedia.org/wiki/Arithmetic_mean"""
    #preconditions
    assert isinstance(numbers, collections.Iterable), "Must be iterable"
    assert isinstance(numbers, numbers.Number), "Please enter numbers"
    assert len(numbers) > 1, "Please enter at least 2 numbers to be averaged"
    #function
    #postconditions
    assert isinstance(numbers, numbers.Number), "Mean will return a number"
    pass

def median(numbers):
    """Finds the median or middle of a list of sorted numbers, a simple measure of 'middle'.
    See: https://en.wikipedia.org/wiki/Median"""
    pass

def range(numbers):
    """Finds ths range of a list of numbers, a simple measure of variance.
    See: https://www.mathsisfun.com/definitions/range-statistics-.html"""
    pass

def standard_deviation(numbers):
    """Finds the standard deviation of a list of numbers, a measure of variance.
    See: https://www.mathsisfun.com/data/standard-deviation-formulas.html"""
    pass
