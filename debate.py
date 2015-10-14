#!/usr/bin/env python

def gini(list):
    numerator = 0
    denominator = 0
    N = len(list)
    for i in range(N):
        for j in range(N):
            numerator += abs(list[i] - list[j])
            denominator += 2 * list[i]
    return float(numerator) / denominator

debate = [31+5/60.0, 28+5/60.0, 17+56/60.0, 15+35/60.0, 9+11/60.0]
# source https://twitter.com/nytimes/status/654131249234247682
perfect_eq = [42] * 7
perfect_in = [99999] + ([0] * 999)
print "debate              ", round(gini(debate), 3)
print "perfect equality    ", gini(perfect_eq)
print "perfect inequality  ", gini(perfect_in)
