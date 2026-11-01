# 3. Longest Substring Without Repeating Characters — v2: Window with last-seen index

[← Problem statement](../README.md)

> Keep a window with no repeats; when a character repeats, jump the left edge just past its previous position.

## Approach

**Sliding window with last positions.** Store the last index of every character. Move `right` across the string; if `s[right]`
was last seen at or after `left`, jump `left` to one past that position. The window `left..right` never contains a repeat.

* Time: **O(n)** — each character is processed once; left only jumps forward.
* Space: **O(k)** — k is the alphabet size (here a fixed array of 128 entries).

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0003/v2/LongestSubstring.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0003/v2/LongestSubstringTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
