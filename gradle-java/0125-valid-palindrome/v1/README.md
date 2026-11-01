# 125. Valid Palindrome — v1: Optimal

[← Problem statement](../README.md)

> Two pointers move inward, skipping non-alphanumerics and comparing letters case-insensitively.

## Approach

**Two pointers.** `l` starts at 0 and `r` at the end. Skip characters that are not letters or digits. Compare
`toLowerCase(s[l])` with `toLowerCase(s[r])`; on mismatch return `false`; otherwise move both inward.

* Time: **O(n)** — each character is visited at most once.
* Space: **O(1)** — no cleaned copy of the string.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0125/v1/ValidPalindrome.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0125/v1/ValidPalindromeTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
