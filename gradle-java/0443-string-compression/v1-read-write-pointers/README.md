# 443. String Compression — v1: Read/write pointers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/string-compression/)

## Problem

Compress `chars` in place: each run of a repeated character becomes the character followed by the run length (if the length is more than
1, written digit by digit). Return the new length.

**Example**
```
["a","a","b","b","c","c","c"] → 6, chars = ["a","2","b","2","c","3"]
["a"]                          → 1
["a","b","b","b","b","b","b","b","b","b","b","b","b"] → 4 ("a","b","1","2")
```

**Constraints**
* `1 <= chars.length <= 2000`

## Approach: Read/write pointers

> Read each run of equal characters and write the character plus its count (if > 1) back into the same array.

**Two pointers.** `read` finds the end of each run; `write` writes the character and, if the run is longer than 1, its digits. Writing
never overtakes reading, because a run's encoding is never longer than the run.

* Time: **O(n)** — each character is read once.
* Space: **O(1)** — in place.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0443/v1/StringCompression.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0443/v1/StringCompressionTest.java` | JUnit 6 tests |
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
