# 383. Ransom Note — v1: Letter counts

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/ransom-note/)

## Problem

Return `true` if `ransomNote` can be built from the letters of `magazine`, using each magazine letter at most once.

**Example 1**
```
Input:  ransomNote = "a", magazine = "b"
Output: false
```

**Example 2**
```
Input:  ransomNote = "aa", magazine = "aab"
Output: true
```

**Constraints**
* `1 <= ransomNote.length, magazine.length <= 10^5`; lowercase letters.

## Approach: Letter counts

> Count the magazine's letters, then spend one count per letter of the note.

**Counting array.** Count each letter of `magazine` in an `int[26]`. For each letter of the note, decrement its count; if it
goes negative, the magazine lacks that letter.

* Time: **O(m + n)** — one pass over each string.
* Space: **O(1)** — 26 counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0383/v1/RansomNote.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0383/v1/RansomNoteTest.java` | JUnit 6 tests |
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
