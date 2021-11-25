import math

def get_statistics(input_list):
    # Write your code here.
    return {
        "mean": mean(input_list),
        "median": median(input_list),
        "mode": mode(input_list),
        "sample_variance": sample_variance(input_list),
        "sample_standard_deviation": sample_standard_deviation(input_list),
        "mean_confidence_interval": mean_confidence_interval(input_list),
    }
def mean(input_list):
    res = 0
    ct = 0
    for i in input_list:
        res += i
        ct += 1
    return res/ct

def median(input_list):
    input_list.sort()
    length = len(input_list)
    mid = length//2
    if length % 2 != 0:
        return input_list[mid]
    else:
        return (input_list[mid] + input_list[mid-1]) / 2

def mode(input_list):
    freq = dict()
    for i in input_list:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    max_freq = 0
    res = None
    for key in freq:
        if freq[key] > max_freq:
            res = key
            max_freq = freq[key]
    return res

def sample_variance(input_list):
    res = 0
    avg = mean(input_list)
    for i in input_list:
        res += (i - avg) ** 2
    return res / (len(input_list)-1)

def sample_standard_deviation(input_list):
    return math.sqrt(sample_variance(input_list))

def mean_confidence_interval(input_list):
    avg = mean(input_list)
    std = sample_standard_deviation(input_list) / math.sqrt(len(input_list))
    return [avg - std*1.96, avg + std*1.96]