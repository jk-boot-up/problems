# 189. Rotate Array — v1: Extra array

[← Problem statement](../README.md)

> Write each value straight to its final index (i + k) % n in a copy, then copy back.

## Approach

**Copy to the target positions.** Value at `i` belongs at `(i + k) % n`. Fill a new array, then copy it back into `nums`.

* Time: **O(n)** — two linear passes.
* Space: **O(n)** — the temporary array.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0189/v1/RotateArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0189/v1/RotateArrayTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
