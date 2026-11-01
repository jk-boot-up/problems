# 190. Reverse Bits

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-bits/)

## Problem

Reverse the bits of a 32-bit **unsigned** integer (in Java it arrives in an `int`, so the top bit may be the sign bit).

**Example**
```
Input:  00000010100101000001111010011100   (43261596)
Output: 00111001011110000010100101000000   (964176192)
```

**Constraints**
* The input is a 32-bit binary value.

**Follow-up:** if called many times, how would you optimize it?

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-swap-halves-divide-and-conquer](v1-swap-halves-divide-and-conquer/README.md) | Swap halves (divide and conquer) | `O(1)` | `O(1)` | [▶ animation](v1-swap-halves-divide-and-conquer/animation/index.html) |
| [v2-bit-by-bit-shifting](v2-bit-by-bit-shifting/README.md) | Bit-by-bit shifting | `O(1)` | `O(1)` | [▶ animation](v2-bit-by-bit-shifting/animation/index.html) |
