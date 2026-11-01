# 383. Ransom Note — v1: Letter counts

[← Problem statement](../README.md)

> Count the magazine's letters, then spend one count per letter of the note.

## Approach

**Counting array.** Count each letter of `magazine` in an `int[26]`. For each letter of the note, decrement its count; if it
goes negative, the magazine lacks that letter.

* Time: **O(m + n)** — one pass over each string.
* Space: **O(1)** — 26 counters.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0383/v1/RansomNote.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0383/v1/RansomNoteTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
