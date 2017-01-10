"""Some simple statistical functions."""

import numbers
import collections
import math

def mean(number_list):
    """Takes the mean/average of a list of numbers, a simple measure of 'middle'.
    See: https://en.wikipedia.org/wiki/Arithmetic_mean"""
    #preconditions
    assert isinstance(number_list, collections.Iterable), "Must be iterable."
    for num in number_list:
        assert isinstance(num, numbers.Number), "We need numbers yo."
    #function
    answer = (sum(number_list) / len(number_list))
    #postconditions
    assert isinstance(answer, numbers.Number), "Mean will return a number."
    assert answer >= min(number_list), "Mean should be higher or equal lowest number in list."
    assert answer <= max(number_list), "Mean should be lower or equal highest number in list."
    return answer

def median(number_list):
    """Finds the median or middle of a list of sorted numbers, a simple measure of 'middle'.
    See: https://en.wikipedia.org/wiki/Median"""
    #preconditions
    assert isinstance(number_list, collections.Iterable), "Must be iterable."
    for num in number_list:
        assert isinstance(num, numbers.Number), "We need numbers yo."
    assert sorted(number_list) == number_list, "Numbers must be in order smallest to largest."
    #function
    srtd = sorted(number_list)
    mid = len(number_list)//2
    if len(number_list) % 2 == 0:
        answer = (srtd[mid-1] + srtd[mid]) / 2.0
    else:
        answer = srtd[mid]
    #postconditions
    assert isinstance(answer, numbers.Number), "Median will return a number."
    assert answer >= min(number_list), "Median should be >= lowest number in list."
    assert answer <= max(number_list), "Median should be <= highest number in list."
    return answer

def range_(number_list):
    """Finds ths range of a list of numbers, a simple measure of variance.
    See: https://www.mathsisfun.com/definitions/range-statistics-.html"""
    #preconditions
    assert isinstance(number_list, collections.Iterable), "Must be iterable."
    for num in number_list:
        assert isinstance(num, numbers.Number), "We need numbers yo."
    assert len(number_list) > 1, "Please enter at least 2 numbers to calculate range."
    #function
    answer = max(number_list) - min(number_list)
    #postcondition
    assert isinstance(answer, numbers.Number), "Range will return a number."
    assert max(number_list) - answer == min(number_list), "The max - answer should = lowest number"
    return answer

def standard_deviation(number_list):
    """Finds the standard deviation of a list of numbers, a measure of variance.
    See: https://www.mathsisfun.com/number_list/standard-deviation-formulas.html"""
    #preconditions
    assert isinstance(number_list, collections.Iterable), "Must be iterable."
    for num in number_list:
        assert isinstance(num, numbers.Number), "We need numbers yo."
    assert len(number_list) > 1, "Please enter at least 2 numbers to calculate standard deviation."
    #function
    mean_ = mean(number_list)
    variance = sum([(e-mean_) ** 2 for e in number_list]) / (len(number_list) - 1)
    answer = math.sqrt(variance)
    rounded_answer = round(answer, 5)
    #postconditions
    assert isinstance(rounded_answer, numbers.Number), "Standard Deviation will return number."
    assert (max(number_list) - min(number_list)) > rounded_answer, "Range should be larger than SD."
    return rounded_answer
