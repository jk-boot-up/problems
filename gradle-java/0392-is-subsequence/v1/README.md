# 392. Is Subsequence — v1: Optimal

[← Problem statement](../README.md)

> Walk through t once; advance the pointer in s each time its current character appears.

## Approach

**Two pointers.** `i` walks `s`, `j` walks `t`. Whenever `s[i] == t[j]`, advance `i`. Always advance `j`.
`s` is a subsequence if `i` reaches `s.length()`.

* Time: **O(n)** — n is the length of t; each character of t is checked once.
* Space: **O(1)** — two indices.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0392/v1/IsSubsequence.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0392/v1/IsSubsequenceTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
