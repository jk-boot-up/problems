# 11. Container With Most Water — v2: Two pointers

[← Problem statement](../README.md)

> Start with the widest container and always move the shorter wall inward: that is the only move that might help.

## Approach

**Two pointers.** Start with `l = 0` and `r = n - 1` (maximum width). The area is limited by the shorter wall.
Moving the taller wall inward can only shrink the width without raising the limit, so always move the **shorter** one.

* Time: **O(n)** — each step moves one pointer inward.
* Space: **O(1)** — two pointers and the best area.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0011/v2/ContainerWithMostWater.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0011/v2/ContainerWithMostWaterTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
