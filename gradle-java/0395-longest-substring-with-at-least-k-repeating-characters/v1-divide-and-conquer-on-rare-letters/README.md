# 395. Longest Substring with At Least K Repeating Characters — v1: Divide and conquer on rare letters

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)

## Problem

Return the length of the longest substring of `s` in which **every** character appears at least `k` times.

**Example**
```
s = "aaabb",  k = 3 → 3   ("aaa")
s = "ababbc", k = 2 → 5   ("ababb")
```

**Constraints**
* `1 <= s.length <= 10^4`, lower-case letters, `1 <= k <= 10^5`

## Approach: Divide and conquer on rare letters

> A letter that appears fewer than k times can never be inside the answer, so split around it.

**Split.** Count the letters of the current range. If every letter appears at least `k` times, the whole range is valid. Otherwise any
letter with a count below `k` is a wall: solve each piece between walls recursively and keep the best.

* Time: **O(26 · n)** — each level of recursion removes at least one distinct letter, so there are at most 26 levels of linear work.
* Space: **O(26)** — the recursion depth (plus a counter array per level).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0395/v1/LongestSubstringKRepeating.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0395/v1/LongestSubstringKRepeatingTest.java` | JUnit 6 tests |
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

* [v2-sliding-window-per-distinct-count](../v2-sliding-window-per-distinct-count/README.md): Sliding window per distinct count (`O(26 · n)` time, `O(1)` space)
