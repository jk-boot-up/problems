# 202. Happy Number — v2: Floyd cycle detection

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

## Approach: Floyd cycle detection

> The digit-square sequence either reaches 1 or falls into a cycle; detect the cycle with fast and slow pointers.

**Fast and slow pointers.** Treat `next(x)` = sum of squared digits as a linked list. `slow` moves one step, `fast` two. If they meet
at 1 the number is happy; if they meet elsewhere, there is a cycle without 1.

* Time: **O(log n)** — the values quickly drop below a few hundred, and each step costs O(number of digits).
* Space: **O(1)** — two numbers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0202/v2/HappyNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0202/v2/HappyNumberTest.java` | JUnit 6 tests |
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

* [v1-seen-set](../v1-seen-set/README.md): Seen set (`O(log n)` time, `O(log n)` space)
