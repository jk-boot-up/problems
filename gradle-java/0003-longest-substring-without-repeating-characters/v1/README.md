# 3. Longest Substring Without Repeating Characters — v1: Window with a hash set

[← Problem statement](../README.md)

> Grow the window on the right; while the new character is already inside, shrink from the left.

## Approach

**Sliding window with a set.** The set holds the window's characters. Before adding `s[right]`, remove `s[left]` and advance
`left` until `s[right]` is no longer in the set.

* Time: **O(n)** — each character is added once and removed at most once.
* Space: **O(k)** — the set holds at most k distinct characters.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0003/v1/LongestSubstring.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0003/v1/LongestSubstringTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
