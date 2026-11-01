# 169. Majority Element — v3: Boyer–Moore voting

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/majority-element/)

## Problem

Given an array `nums` of size `n`, return the **majority element**: the value that appears more than `⌊n / 2⌋` times.
You may assume a majority element always exists.

**Example 1**
```
Input:  nums = [3,2,3]
Output: 3
```

**Example 2**
```
Input:  nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints**
* `1 <= n <= 5 * 10^4`
* `-10^9 <= nums[i] <= 10^9`

**Follow-up:** solve it in linear time and O(1) space.

## Approach: Boyer–Moore voting

> Boyer–Moore voting: the majority value survives when every vote is cancelled by a different value.

**Boyer–Moore voting.** Keep a `candidate` and a `count`. When `count` is 0, adopt the current value as the candidate.
A matching value adds a vote, a different value removes one. Each different value cancels one copy of the majority,
but the majority has more copies than all other values together, so it is the candidate left at the end.

* Time: **O(n)** — one pass over the votes.
* Space: **O(1)** — just a candidate and a counter, no hash map.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0169/v3/MajorityElement.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0169/v3/MajorityElementTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

## Build and test

This folder is a standalone Gradle 9.8.2 project. Only a JDK is needed to start Gradle; JDK 25 is downloaded
automatically if it is missing.

```bash
./gradlew test
```

## Animation

Open [`animation/index.html`](animation/index.html) in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech
  engine (use the 🔊 *Narration* button to turn the voice on or off; a female voice, Amy when installed, is preferred). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-hash-map-counting](../v1-hash-map-counting/README.md): Hash map counting (`O(n)` time, `O(n)` space)
* [v2-sort-and-take-the-middle](../v2-sort-and-take-the-middle/README.md): Sort and take the middle (`O(n log n)` time, `O(log n)` space)
