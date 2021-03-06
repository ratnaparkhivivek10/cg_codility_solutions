#!/usr/bin/python
# -*- coding: utf-8 -*-
# python 3.5.2


def solution(a, b):
    return str(bin(a * b))[2:].count('1')


print(solution(3, 7))

# Answer -> 3
"""
Write a function:
Class solution{public int solution(int A,int B);}
That,given two non-negative integers A and B, returns the number of bits set to 1 in the binary representation of the number A*B.
e.g., given A=3 and B=7 the function should return 3, because the binary representation of A*B=3*7=21 is 10101 and it contains three bits set to 1.
Assume that :
A and B are integers within the range[0..100000000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""
