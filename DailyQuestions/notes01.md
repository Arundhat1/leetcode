# Problem-Solving Notes (24/11 → Today)

This document tracks my daily problem-solving journey, grouped into phases based on themes and skills.

---

## Phase 1 – Bitwise Thinking Bootcamp

### 2411. Smallest Subarrays With Maximum Bitwise OR
**Approach:**  
- Traverse from right to left, maintaining bit positions of the last occurrence.
- For each index, determine the farthest reach needed to achieve max OR.

**Takeaway:** Learned how OR accumulates bits and how to track bit positions efficiently.

---

### 2419. Longest Subarray With Maximum Bitwise AND
**Approach:**  
- Iterate through array while checking where AND drops below max value.
- Reset count when the AND result changes.

**Takeaway:** Unlike OR, AND loses bits quickly; forces segment resetting logic.

---

### 898. Bitwise ORs of Subarrays
**Approach:**  
- Maintain a set of possible OR values ending at each position.
- Merge with previous values to avoid recomputing all subarrays.

**Takeaway:** Optimizing subarray enumeration by reusing state across steps.

---

### 118. Pascal’s Triangle
**Approach:**  
- Use combinatorics definition: `C(n, k) = C(n-1, k-1) + C(n-1, k)`.

**Takeaway:** Refresher on combinatorics, binomial coefficients.

---

## Phase 2 – Fruits & Sliding Windows Marathon

### 2561. Rearranging Fruits
**Approach:**  
- Use frequency counts and greedy pairing to minimize swaps.

**Takeaway:** Identifying imbalance and fixing it with minimal moves.

---

### 2106. Maximum Fruits Harvested After At Most K Steps
**Approach:**  
- Combine prefix sums with sliding windows over fruit positions.
- Account for both left-first and right-first movement patterns.

**Takeaway:** Movement planning within constraints — merging prefix sums and sliding window logic.

---

### 904. Fruits Into Baskets
**Approach:**  
- Sliding window maintaining at most two fruit types.

**Takeaway:** Core template for “at most k distinct” problems.

---

### 3477. Fruits Into Baskets II
**Approach:**  
- Extend basic two-basket logic with custom rules per problem statement.

**Takeaway:** Adapting a known template to variant constraints.

---

### 3479. Fruits Into Baskets III
**Approach:**  
- Modified constraints — still maintains the two-type window but with extra edge cases.

**Takeaway:** Reinforces how flexible the sliding window pattern can be.

---

### 3363. Find the Maximum Number of Fruits Collected
**Approach:**  
- More general variant with extra movement/collection rules.

**Takeaway:** Merging multiple patterns — sliding window + movement tracking.

---

### 808. Soup Serving
**Approach:**  
- Recursive DP with memoization to compute probability outcomes.

**Takeaway:** First taste of probability DP in the streak.

---

## Phase 3 – Powers, Math, and Combinatorics

### 231. Power of Two
**Approach:**  
- Check if `n` is a power of 2 using bit tricks or modulo.

**Takeaway:** Recognizing powers with O(1) bit operations.

---

### 869. Reordered Power of Two
**Approach:**  
- Precompute digit patterns of all powers of two and compare with input.

**Takeaway:** Turning permutation problems into hashable patterns for O(1) checks.

---

### 2438. Range Product Queries of Powers
**Approach:**  
- Precompute prefix products of powers, use modular arithmetic for queries.

**Takeaway:** Segment-like querying over number properties.

---

### 2787. Ways of Expressing an Integer as Sum of Powers
**Approach:**  
- DP over powers list — similar to coin change problem.

**Takeaway:** Applying classic DP structures to mathematical expressions.

---

### 326. Power of Three
**Approach:**  
- Check divisibility from the largest power down, or use logarithmic check.

**Takeaway:** Modular arithmetic and logarithm tricks.

---

## Summary of Learning Progression
1. **Bitwise mastery:** Understanding OR/AND bitmask behavior.
2. **Sliding window flexibility:** From fixed to dynamic constraints.
3. **Mathematical reasoning:** Powers, combinatorics, and modular arithmetic.
4. **Pattern adaptation:** Using known templates in problem variants.

---
