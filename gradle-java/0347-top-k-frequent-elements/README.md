# 347. Top K Frequent Elements

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)

## Problem

Return the `k` most frequent elements of `nums`, in any order. The answer is guaranteed to be unique.

**Example**
```
nums = [1,1,1,2,2,3], k = 2 → [1,2]
nums = [1], k = 1            → [1]
```

**Constraints**
* `1 <= nums.length <= 10^5`; `1 <= k <=` number of distinct values

**Follow-up:** better than O(n log n).

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-counting-min-heap-of-size-k](v1-counting-min-heap-of-size-k/README.md) | Counting + min-heap of size k | `O(n log k)` | `O(n)` | [▶ animation](v1-counting-min-heap-of-size-k/animation/index.html) |
| [v2-counting-bucket-sort](v2-counting-bucket-sort/README.md) | Counting + bucket sort | `O(n)` | `O(n)` | [▶ animation](v2-counting-bucket-sort/animation/index.html) |
