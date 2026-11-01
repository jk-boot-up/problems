# 169. Majority Element — v3: Boyer–Moore voting

[← Problem statement](../README.md)

> Boyer–Moore voting: the majority value survives when every vote is cancelled by a different value.

## Approach

**Boyer–Moore voting.** Keep a `candidate` and a `count`. When `count` is 0, adopt the current value as the candidate.
A matching value adds a vote, a different value removes one. Each different value cancels one copy of the majority,
but the majority has more copies than all other values together, so it is the candidate left at the end.

* Time: **O(n)** — one pass over the votes.
* Space: **O(1)** — just a candidate and a counter, no hash map.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0169/v3/MajorityElement.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0169/v3/MajorityElementTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v3:test`.
