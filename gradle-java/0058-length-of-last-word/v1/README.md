# 58. Length of Last Word — v1: Optimal

[← Problem statement](../README.md)

> Scan from the end: skip trailing spaces, then count letters until the next space.

## Approach

**Backward scan.** Start at the end, skip spaces, then count characters until a space or the start of the string.

* Time: **O(n)** — at worst we scan the whole string once.
* Space: **O(1)** — an index and a counter.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0058/v1/LengthOfLastWord.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0058/v1/LengthOfLastWordTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
