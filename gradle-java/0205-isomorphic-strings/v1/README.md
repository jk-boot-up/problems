# 205. Isomorphic Strings — v1: Two-way mapping

[← Problem statement](../README.md)

> Map characters both ways (s→t and t→s); any conflicting mapping means not isomorphic.

## Approach

**Two maps.** Walk both strings together. If `s[i]` already maps to something other than `t[i]`, or `t[i]` is already the image
of a different character, return `false`. Otherwise record both directions.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two arrays of 256 entries.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0205/v1/IsomorphicStrings.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0205/v1/IsomorphicStringsTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
