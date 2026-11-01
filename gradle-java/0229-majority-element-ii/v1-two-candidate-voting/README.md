# 229. Majority Element II — v1: Two-candidate voting

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/majority-element-ii/)

## Problem

Return all values that appear **more than ⌊n/3⌋ times** in `nums`, in any order.

**Example**
```
[3,2,3] → [3],   [1] → [1],   [1,2] → [1,2]
```

**Constraints**
* `1 <= nums.length <= 5 * 10^4`

**Follow-up:** O(n) time and O(1) space.

## Approach: Two-candidate voting

> At most two values can exceed n/3; extended Boyer–Moore keeps two candidates, then a second pass verifies them.

**Boyer–Moore with two slots.** A matching value adds a vote to its slot; an empty slot adopts the value; otherwise both slots lose a vote
(three distinct values cancel). Survivors are only candidates, so count them in a second pass.

* Time: **O(n)** — two passes.
* Space: **O(1)** — two candidates and two counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0229/v1/MajorityElementII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0229/v1/MajorityElementIITest.java` | JUnit 6 tests |
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
