# 395. Longest Substring with At Least K Repeating Characters — v2: Sliding window per distinct count

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

## Approach: Sliding window per distinct count

> Fix how many distinct letters the window may hold (1..26); for each, a plain sliding window works.

**Add a constraint.** A plain window fails because adding a letter can make things worse or better. Fixing `target` = the number of
distinct letters allowed makes it monotone: grow the right end; shrink from the left while more than `target` distinct letters are in
the window. When the window has exactly `target` distinct letters and all of them reach `k`, it is a candidate. Try `target = 1..26`.

* Time: **O(26 · n)** — 26 linear sweeps.
* Space: **O(1)** — 26 counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0395/v2/LongestSubstringKRepeating.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0395/v2/LongestSubstringKRepeatingTest.java` | JUnit 6 tests |
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

* [v1-divide-and-conquer-on-rare-letters](../v1-divide-and-conquer-on-rare-letters/README.md): Divide and conquer on rare letters (`O(26 · n)` time, `O(26)` space)
