# 134. Gas Station — v2: Greedy single pass

[← Problem statement](../README.md)

> If total gas ≥ total cost a solution exists; whenever the tank goes negative, the start must be after this station.

## Approach

**Greedy single pass.** Track `total = Σ(gas - cost)`; if it is negative, no start works. Also track the current `tank`
from a candidate `start`. If `tank` drops below 0 at station `i`, no station between `start` and `i` can be the start
(each would arrive at `i` with even less fuel), so set `start = i + 1` and reset the tank.

* Time: **O(n)** — one pass around the stations.
* Space: **O(1)** — three running numbers.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0134/v2/GasStation.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0134/v2/GasStationTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
