# 217. Contains Duplicate — v1: Sort and compare neighbours

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/contains-duplicate/)

## Problem

Return `true` if any value appears **at least twice** in `nums`, and `false` if every element is distinct.

**Example**
```
[1,2,3,1] → true,   [1,2,3,4] → false,   [1,1,1,3,3,4,3,2,4,2] → true
```

**Constraints**
* `1 <= nums.length <= 10^5`; `-10^9 <= nums[i] <= 10^9`

## Approach: Sort and compare neighbours

> After sorting, equal values are adjacent.

**Sort.** Sort a copy and check whether any two neighbours are equal.

* Time: **O(n log n)** — sorting.
* Space: **O(n)** — the sorted copy.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0217/v1/ContainsDuplicate.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0217/v1/ContainsDuplicateTest.java` | JUnit 6 tests |
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

* [v2-hash-set](../v2-hash-set/README.md): Hash set (`O(n)` time, `O(n)` space)
