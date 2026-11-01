# 28. Find the Index of the First Occurrence in a String — v1: Brute force

[← Problem statement](../README.md)

> Try every start position and compare the needle character by character.

## Approach

**Check every alignment.** For each start `i` from 0 to `n - m`, compare `needle` with `haystack[i..i+m-1]`.

* Time: **O(n·m)** — each of about n alignments may compare up to m characters.
* Space: **O(1)** — a couple of indices.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0028/v1/StrStr.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0028/v1/StrStrTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
