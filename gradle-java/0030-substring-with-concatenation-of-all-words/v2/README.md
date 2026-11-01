# 30. Substring with Concatenation of All Words — v2: Word-step sliding window

[← Problem statement](../README.md)

> All words share one length L, so slide a word-sized window for each of the L starting offsets, counting words in the window.

## Approach

**Sliding window in word-sized steps.** Let `L` be the word length and `k` the number of words. For each offset `0..L-1`, slide
a window over `s` one word at a time, keeping a count of the words inside. If a word is not in `words`, reset the window. If a word
appears too often, drop words from the left until it doesn't. When the window holds `k` words, record its start.

* Time: **O(n·L)** — L offsets, each scanning about n / L words, and each word costs O(L) to cut out and hash.
* Space: **O(k)** — the two word-count maps.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0030/v2/SubstringConcatenation.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0030/v2/SubstringConcatenationTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
