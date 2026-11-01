# 692. Top K Frequent Words

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/top-k-frequent-words/)

## Problem

Return the `k` most frequent words, sorted by frequency (highest first); equal frequencies are sorted alphabetically.

**Example**
```
["i","love","leetcode","i","love","coding"], k = 2 → ["i","love"]
["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4 → ["the","is","sunny","day"]
```

**Constraints**
* `1 <= words.length <= 500`; `k` is valid.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-counting-bounded-heap](v1-counting-bounded-heap/README.md) | Counting + bounded heap | `O(n log k)` | `O(n)` | [▶ animation](v1-counting-bounded-heap/animation/index.html) |
