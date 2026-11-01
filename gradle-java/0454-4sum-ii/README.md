# 454. 4Sum II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hash Map &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/4sum-ii/)

## Problem

Given four arrays of length `n`, count tuples `(i, j, k, l)` with `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`.

**Example**
```
nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2] → 2
nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0] → 1
```

**Constraints**
* `1 <= n <= 200`, `-2^28 <= values <= 2^28`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-try-every-tuple](v1-try-every-tuple/README.md) | Try every tuple | `O(n⁴)` | `O(1)` | [▶ animation](v1-try-every-tuple/animation/index.html) |
| [v2-pair-sums-in-a-hash-map](v2-pair-sums-in-a-hash-map/README.md) | Pair sums in a hash map | `O(n²)` | `O(n²)` | [▶ animation](v2-pair-sums-in-a-hash-map/animation/index.html) |
