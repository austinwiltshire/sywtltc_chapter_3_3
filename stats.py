"""Some simple statistical functions."""

import numbers
import collections
import math

def mean(number_list):
    """Takes the mean/average of a list of numbers, a simple measure of 'middle'.
    See: https://en.wikipedia.org/wiki/Arithmetic_mean"""
    #preconditions
    assert isinstance(number_list, collections.Iterable), "Must be iterable."
    assert all(isinstance(x, numbers.Number) for x in number_list), "Must be numbers."
    assert len(number_list) > 0, "Cannot take mean of empty list."
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
    assert all(isinstance(x, numbers.Number) for x in number_list), "Must be numbers."
    assert sorted(number_list) == number_list, "Numbers must be in order smallest to largest."
    assert len(number_list) > 0, "Cannot take median of empty list."
    #function
    mid = len(number_list)//2
    if len(number_list) % 2 == 0:
        answer = (number_list[mid-1] + number_list[mid]) / 2.0
    else:
        answer = number_list[mid]
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
    assert all(isinstance(x, numbers.Number) for x in number_list), "Must be numbers."
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
    assert all(isinstance(x, numbers.Number) for x in number_list), "Must be numbers."
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
