# 68. Text Justification — v1: Optimal

[← Problem statement](../README.md)

> Greedily pack words per line, then spread the spare spaces across gaps, giving the extra ones to the leftmost gaps.

## Approach

**Greedy lines + space distribution.** Starting at word `i`, extend `j` while `lettersLength + (j - i) <= maxWidth`.
For a normal line with `gaps = j - i - 1`, total spaces = `maxWidth - letters`; each gap gets `spaces / gaps` and the first
`spaces % gaps` gaps get one more. The last line and single-word lines are joined with one space and right-padded.

* Time: **O(L)** — L is the total number of output characters (lines × maxWidth); each is written once.
* Space: **O(maxWidth)** — the builder for the current line, apart from the output.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0068/v1/TextJustification.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0068/v1/TextJustificationTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
