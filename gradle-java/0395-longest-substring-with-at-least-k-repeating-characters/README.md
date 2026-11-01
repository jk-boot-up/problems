# 395. Longest Substring with At Least K Repeating Characters

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)

## Problem

Return the length of the longest substring of `s` in which **every** character appears at least `k` times.

**Example**
```
s = "aaabb",  k = 3 → 3   ("aaa")
s = "ababbc", k = 2 → 5   ("ababb")
```

**Constraints**
* `1 <= s.length <= 10^4`, lower-case letters, `1 <= k <= 10^5`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-divide-and-conquer-on-rare-letters](v1-divide-and-conquer-on-rare-letters/README.md) | Divide and conquer on rare letters | `O(26 · n)` | `O(26)` | [▶ animation](v1-divide-and-conquer-on-rare-letters/animation/index.html) |
| [v2-sliding-window-per-distinct-count](v2-sliding-window-per-distinct-count/README.md) | Sliding window per distinct count | `O(26 · n)` | `O(1)` | [▶ animation](v2-sliding-window-per-distinct-count/animation/index.html) |
