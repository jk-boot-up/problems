# 76. Minimum Window Substring — v1: Sliding window with counts

[← Problem statement](../README.md)

> Expand right until the window covers t, then shrink left as far as it stays covering; remember the smallest.

## Approach

**Sliding window.** `need[c]` counts what `t` still needs; `missing` is how many characters are still missing.
Move `right`: if `need[s[right]] > 0`, it fills a gap (`missing--`); decrement `need` either way. When `missing == 0`, shrink from
the left while `need[s[left]] < 0` (that character is in surplus), record the window, then give up `s[left]` to keep searching.

* Time: **O(m + n)** — each pointer passes over s once, plus one pass over t.
* Space: **O(1)** — a fixed 128-entry count array.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0076/v1/MinimumWindowSubstring.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0076/v1/MinimumWindowSubstringTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
