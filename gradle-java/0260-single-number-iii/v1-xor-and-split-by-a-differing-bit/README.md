# 260. Single Number III — v1: XOR and split by a differing bit

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/single-number-iii/)

## Problem

In `nums`, exactly two elements appear once and every other element appears exactly twice. Return the two single elements, in any order,
using O(1) extra space.

**Example**
```
[1,2,1,3,2,5] → [3,5]
[-1,0]        → [-1,0]
```

**Constraints**
* `2 <= nums.length <= 3 * 10^4`

## Approach: XOR and split by a differing bit

> XOR of everything is a ^ b; any set bit of it splits the numbers into two groups, one holding each answer.

**Two-group XOR.** XOR-ing everything cancels the pairs and leaves `x = a ^ b`, which is non-zero. Its lowest set bit `x & -x` is a bit
where `a` and `b` differ. XOR the numbers that have that bit into one value and the rest into another: pairs still cancel inside each
group, leaving `a` and `b`.

* Time: **O(n)** — two passes.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0260/v1/SingleNumberIII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0260/v1/SingleNumberIIITest.java` | JUnit 6 tests |
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
