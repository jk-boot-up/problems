# 134. Gas Station — v1: Simulate every start

[← Problem statement](../README.md)

> Try each station as the start and drive around until the tank runs dry.

## Approach

**Brute force.** For every start `s`, drive `n` legs, adding `gas` and subtracting `cost`. If the tank never drops below zero,
`s` works.

* Time: **O(n²)** — n starts × up to n legs.
* Space: **O(1)** — a tank counter.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0134/v1/GasStation.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0134/v1/GasStationTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
