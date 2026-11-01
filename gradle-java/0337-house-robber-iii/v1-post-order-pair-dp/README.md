# 337. House Robber III — v1: Post-order pair DP

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/house-robber-iii/)

## Problem

Houses form a binary tree; robbing two directly-linked houses (parent and child) triggers the alarm. Return the maximum amount you can rob.

**Example**
```
[3,2,3,null,3,null,1] → 7   (3 + 3 + 1)
[3,4,5,1,3,null,1]    → 9   (4 + 5)
```

**Constraints**
* `1 <= n <= 10^4`

## Approach: Post-order pair DP

> Each node returns two numbers: the best total if it is robbed, and if it is not.

**Pair per node.** `rob(n)` returns `[take, skip]`: `take = n.val + left.skip + right.skip`, `skip = max(left) + max(right)`.
The answer is `max(rob(root))`.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0337/v1/HouseRobberIII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0337/v1/HouseRobberIIITest.java` | JUnit 6 tests |
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
