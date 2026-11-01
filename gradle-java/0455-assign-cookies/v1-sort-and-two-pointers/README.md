# 455. Assign Cookies — v1: Sort and two pointers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/assign-cookies/)

## Problem

Child `i` is content with a cookie of size at least `g[i]`. Cookie `j` has size `s[j]`. Each child gets at most one cookie. Return the
maximum number of content children.

**Example**
```
g = [1,2,3], s = [1,1]   → 1
g = [1,2],   s = [1,2,3] → 2
```

**Constraints**
* `1 <= g.length <= 3 * 10^4`, `0 <= s.length <= 3 * 10^4`

## Approach: Sort and two pointers

> Sort both; give each cookie, smallest first, to the least greedy child it can satisfy.

**Greedy.** Sort both arrays. Walk the cookies from smallest; if the current cookie satisfies the least greedy unsatisfied child, give it
and move to the next child. A cookie too small for that child is too small for everyone left, so skip it.

* Time: **O(n log n + m log m)** — sorting.
* Space: **O(1)** — besides sorting.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0455/v1/AssignCookies.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0455/v1/AssignCookiesTest.java` | JUnit 6 tests |
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
