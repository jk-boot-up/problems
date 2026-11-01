# 1588. Sum of All Odd Length Subarrays — v2: Contribution counting

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)

## Problem

Return the sum of all elements of all **odd-length** subarrays of `arr`.

**Example**
```
[1,4,2,5,3] → 58
[1,2]       → 3
[10,11,12]  → 66
```

**Constraints**
* `1 <= arr.length <= 100`

## Approach: Contribution counting

> Count how many odd-length subarrays contain each element and add value × count.

**Contribution.** Element `i` is in `(i + 1) · (n - i)` subarrays (choose a start at or before it and an end at or after it). Of these,
`((i + 1) · (n - i) + 1) / 2` have odd length. Add `arr[i]` times that count.

* Time: **O(n)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1588/v2/SumOddLengthSubarrays.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1588/v2/SumOddLengthSubarraysTest.java` | JUnit 6 tests |
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

* [v1-prefix-sums-over-every-odd-length](../v1-prefix-sums-over-every-odd-length/README.md): Prefix sums over every odd length (`O(n²)` time, `O(n)` space)
