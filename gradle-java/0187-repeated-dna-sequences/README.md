# 187. Repeated DNA Sequences

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hash Map &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/repeated-dna-sequences/)

## Problem

A DNA string uses the letters `A`, `C`, `G`, `T`. Return every 10-letter substring that occurs **more than once**, each reported once.

**Example**
```
"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" → ["AAAAACCCCC","CCCCCAAAAA"]
"AAAAAAAAAAAAA"                    → ["AAAAAAAAAA"]
```

**Constraints**
* `1 <= s.length <= 10^5`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-set-of-substrings](v1-set-of-substrings/README.md) | Set of substrings | `O(n · L)` | `O(n · L)` | [▶ animation](v1-set-of-substrings/animation/index.html) |
| [v2-rolling-2-bit-encoding](v2-rolling-2-bit-encoding/README.md) | Rolling 2-bit encoding | `O(n)` | `O(n)` | [▶ animation](v2-rolling-2-bit-encoding/animation/index.html) |
