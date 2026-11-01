# 151. Reverse Words in a String — v1: Split, reverse, join

[← Problem statement](../README.md)

> Let the library split on runs of spaces, reverse the list, and join with single spaces.

## Approach

**Library calls.** `s.trim().split("\\s+")` gives the words; reverse the list; `String.join(" ", words)`.
Short and clear, though it allocates an intermediate array.

* Time: **O(n)** — splitting, reversing and joining are linear.
* Space: **O(n)** — the array of words.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0151/v1/ReverseWords.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0151/v1/ReverseWordsTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
