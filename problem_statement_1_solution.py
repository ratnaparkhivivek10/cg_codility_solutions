from itertools import combinations
def solution(data):
    pit_depth = []
    for p, q, r in combinations(range(len(data)), 3):
        is_pq_decreasing = all([data[i] > data[i+1] for i in range(p, q)])
        is_qr_increasing = all([data[i] < data[i+1] for i in range(q, r)])
        
        if is_pq_decreasing and is_qr_increasing:
            pit = min(data[p] - data[q], data[r] - data[q])
            pit_depth.append(pit)
    
    return max(pit_depth)
            
#print(solution([0,1,3,-2,0,1,0,-3,2,3]))
#Ans -> 4
"""
A non-empty zero-indexed array A consisting of N integers is given. A pit in this array is any triplet of integers (P, Q, R) such that:
1. 0 ≤ P &lt; Q &lt; R &lt; N;
2. sequence [A[P], A[P+1], ..., A[Q]] is strictly decreasing, 
 i.e. A[P] &gt; A[P+1] &gt; ... &gt; A[Q];
3. sequence A[Q], A[Q+1], ..., A[R] is strictly increasing, 
 i.e. A[Q] &lt; A[Q+1] &lt; ... &lt; A[R].
 
 The depth  of a pit (P, Q, R) is the number min {A[P] − A[Q], A[R] − A[Q]}.
 For example, consider array A consisting of 10 elements such that:
  A[0] =  0
  A[1] =  1
  A[2] =  3
  A[3] = -2
  A[4] =  0
  A[5] =  1
  A[6] =  0
  A[7] = -3
  A[8] =  2
  A[9] =  3

Triplet (2, 3, 4) is one of pits in this array, because sequence [A[2], A[3]] is strictly decreasing (3 &gt; −2) and sequence [A[3], A[4]] is strictly increasing (−2 &lt; 0). Its depth is min {A[2] − A[3], A[4] − A[3]} = 2. Triplet (2, 3, 5) is another pit with depth 3. Triplet (5,6, 7, 8) is yet another pit with depth 4. There is no pit in this array deeper (i.e. having depth greater) than 4.

Write a function:
int solution(int A[]);

that, given a non-empty zero-indexed array A consisting of N integers, returns the depth of the deepest pit in array A. The function should return −1 if there are no pits in array A.

For example, consider array A consisting of 10 elements such that:
  A[0] =  0
  A[1] =  1
  A[2] =  3
  A[3] = -2
  A[4] =  0
  A[5] =  1
  A[6] =  0
  A[7] = -3
  A[8] =  2
  A[9] =  3
the function should return 4, as explained above.

Assume that:
1. N is an integer within the range [1..1,000,000]
2. each element of array A is an integer within the range [−100,000,000..100,000,000]

Complexity

1. expected worst-case time complexity is O(N);
2. expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
"""
