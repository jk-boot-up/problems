# 220. Contains Duplicate III

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/contains-duplicate-iii/)

## Problem

Given `nums`, `indexDiff` and `valueDiff`, return `true` if there are two indices `i != j` with `|i - j| <= indexDiff` and
`|nums[i] - nums[j]| <= valueDiff`.

**Example**
```
nums = [1,2,3,1],     indexDiff = 3, valueDiff = 0 → true
nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3 → false
```

**Constraints**
* `2 <= nums.length <= 10^5`, `-10^9 <= nums[i] <= 10^9`, `1 <= indexDiff <= nums.length`, `0 <= valueDiff <= 10^9`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-check-every-nearby-pair](v1-check-every-nearby-pair/README.md) | Check every nearby pair | `O(n · k)` | `O(1)` | [▶ animation](v1-check-every-nearby-pair/animation/index.html) |
| [v2-ordered-window-with-treeset](v2-ordered-window-with-treeset/README.md) | Ordered window with TreeSet | `O(n log k)` | `O(k)` | [▶ animation](v2-ordered-window-with-treeset/animation/index.html) |
| [v3-buckets-over-a-sliding-window](v3-buckets-over-a-sliding-window/README.md) | Buckets over a sliding window | `O(n)` | `O(min(n, k))` | [▶ animation](v3-buckets-over-a-sliding-window/animation/index.html) |
