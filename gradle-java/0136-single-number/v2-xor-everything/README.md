# 136. Single Number — v2: XOR everything

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/single-number/)

## Problem

Every element of a non-empty array appears **twice** except one. Find that one, in linear time and constant extra space.

**Example**
```
[2,2,1] → 1,   [4,1,2,1,2] → 4,   [1] → 1
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`

## Approach: XOR everything

> x ^ x = 0 and x ^ 0 = x, so XOR-ing everything cancels the pairs and leaves the single value.

**XOR.** XOR is commutative and associative, `x ^ x = 0` and `x ^ 0 = x`; XOR all values and the pairs vanish.

* Time: **O(n)** — one pass.
* Space: **O(1)** — one accumulator.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0136/v2/SingleNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0136/v2/SingleNumberTest.java` | JUnit 6 tests |
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

* [v1-hash-set-toggling](../v1-hash-set-toggling/README.md): Hash set toggling (`O(n)` time, `O(n)` space)
