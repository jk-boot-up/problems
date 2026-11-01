# 1679. Max Number of K-Sum Pairs — v1: Hash map of waiting numbers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/max-number-of-k-sum-pairs/)

## Problem

In one operation, remove two numbers whose sum is `k`. Return the maximum number of operations.

**Example**
```
nums = [1,2,3,4], k = 5   → 2
nums = [3,1,3,4,3], k = 6 → 1
```

**Constraints**
* `1 <= nums.length <= 10^5`

## Approach: Hash map of waiting numbers

> For each number, if its partner k − x is waiting in the hash map, pair them; otherwise wait.

**Waiting counts.** Keep counts of unpaired numbers in a `MyHashMap`. For each `x`, if `k - x` is waiting, pair them (decrement); otherwise
add `x` to the waiting counts.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the map.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1679/v1/MaxKSumPairs.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1679/v1/MaxKSumPairsTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
