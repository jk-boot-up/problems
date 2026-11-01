# 217. Contains Duplicate — v2: Hash set

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/contains-duplicate/)

## Problem

Return `true` if any value appears **at least twice** in `nums`, and `false` if every element is distinct.

**Example**
```
[1,2,3,1] → true,   [1,2,3,4] → false,   [1,1,1,3,3,4,3,2,4,2] → true
```

**Constraints**
* `1 <= nums.length <= 10^5`; `-10^9 <= nums[i] <= 10^9`

## Approach: Hash set

> Add values to a hash set; the first value that is already there is a duplicate.

**Seen set.** `MyHashSet.add` returns `false` when the value is already present: that is a duplicate.

* Time: **O(n)** — one pass with O(1) average set operations.
* Space: **O(n)** — the set.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0217/v2/ContainsDuplicate.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0217/v2/ContainsDuplicateTest.java` | JUnit 6 tests |
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

* [v1-sort-and-compare-neighbours](../v1-sort-and-compare-neighbours/README.md): Sort and compare neighbours (`O(n log n)` time, `O(n)` space)
