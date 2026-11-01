# 151. Reverse Words in a String — v2: Manual right-to-left scan

[← Problem statement](../README.md)

> Scan from the right, cut out each word, and append it; spaces collapse naturally.

## Approach

**Right-to-left scan.** Walk `i` from the end. Skip spaces; mark `end`; move `i` left while it points at a non-space;
the word is `s[i+1 .. end]`. Append it to a `StringBuilder`, with a space before every word but the first.

* Time: **O(n)** — every character is visited once and copied once.
* Space: **O(n)** — the output builder.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0151/v2/ReverseWords.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0151/v2/ReverseWordsTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
