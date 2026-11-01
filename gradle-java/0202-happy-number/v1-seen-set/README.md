# 202. Happy Number — v1: Seen set

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/happy-number/)

## Problem

A number is **happy** if repeatedly replacing it with the sum of the squares of its digits eventually reaches `1`. Numbers that
never reach 1 loop forever in a cycle. Return `true` if `n` is happy.

**Example 1**
```
Input:  n = 19
Output: true   (1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1)
```

**Example 2**
```
Input:  n = 2
Output: false
```

**Constraints**
* `1 <= n <= 2^31 - 1`

## Approach: Seen set

> Remember every value; seeing one again means we are in a cycle.

**Hash set.** Keep applying `next` until reaching 1 or a value already in the set.

* Time: **O(log n)** — same number of steps as Floyd.
* Space: **O(log n)** — the set holds the values visited before the cycle closes.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0202/v1/HappyNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0202/v1/HappyNumberTest.java` | JUnit 6 tests |
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

* [v2-floyd-cycle-detection](../v2-floyd-cycle-detection/README.md): Floyd cycle detection (`O(log n)` time, `O(1)` space)
