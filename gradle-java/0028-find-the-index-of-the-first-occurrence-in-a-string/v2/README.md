# 28. Find the Index of the First Occurrence in a String — v2: KMP

[← Problem statement](../README.md)

> KMP: precompute how far the needle can fall back on a mismatch, so the haystack pointer never moves backwards.

## Approach

**Knuth–Morris–Pratt.** Build `lps[i]`: the length of the longest proper prefix of `needle[0..i]` that is also its suffix.
Then scan the haystack with `j` matched characters. On a mismatch, fall back to `j = lps[j-1]` instead of restarting,
so the haystack index only moves forward.

* Time: **O(n + m)** — building lps is O(m), and the scan is O(n).
* Space: **O(m)** — the lps table.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0028/v2/StrStr.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0028/v2/StrStrTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
