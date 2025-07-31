 Problem: Bitwise ORs of Subarrays
LeetCode Problem: 898. Bitwise ORs of Subarrays

Problem Statement
Given an array of integers arr, the task is to compute the number of distinct results we can get by taking the bitwise OR of every possible non-empty subarray.

A subarray is a contiguous part of the array.
The bitwise OR of a subarray is calculated by applying the | operator between all elements of that subarray.

 Approach & Explanation
This solution uses a straightforward brute-force method, optimized slightly by reusing the OR value across a subarray rather than recalculating from scratch.

 Key Steps:
We loop through each possible starting index i of a subarray.

For each i, we maintain a running or_value and keep extending the subarray till the end of the array.

At every extension, we update the or_value using the current element:
or_value |= arr[j]

Every OR result is added to a set to ensure uniqueness.

In the end, we return the number of unique OR values collected in the set.

 Why This Works
Using a set automatically removes duplicate OR results across different subarrays.
By updating the OR progressively instead of recalculating for each subarray from scratch, we avoid redundant work, making this faster than a fully naive triple-loop approach.

Example
For arr = [1, 2, 4], the distinct OR values of subarrays are:
1, 3, 7, 2, 6, 4 → total 6 unique values.

 Time and Space Complexity
Time Complexity: O(n²) in the worst case (when all subarrays yield different ORs).

Space Complexity: O(n) for storing the set of unique OR values.


