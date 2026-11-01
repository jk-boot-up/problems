# 187. Repeated DNA Sequences — v2: Rolling 2-bit encoding

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hash Map &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/repeated-dna-sequences/)

## Problem

A DNA string uses the letters `A`, `C`, `G`, `T`. Return every 10-letter substring that occurs **more than once**, each reported once.

**Example**
```
"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" → ["AAAAACCCCC","CCCCCAAAAA"]
"AAAAAAAAAAAAA"                    → ["AAAAAAAAAA"]
```

**Constraints**
* `1 <= s.length <= 10^5`

## Approach: Rolling 2-bit encoding

> Encode each 10-letter window as a 20-bit integer and roll it forward one letter at a time.

**Two bits per letter.** Map `A,C,G,T` to `0..3`. A window of 10 letters fits in 20 bits. Sliding right, shift the code left by 2, add the
new letter, and mask to 20 bits, all in O(1). Keep a set of codes seen once and a set of codes already reported.

* Time: **O(n)** — constant work per position.
* Space: **O(n)** — the two integer sets.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0187/v2/RepeatedDNA.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0187/v2/RepeatedDNATest.java` | JUnit 6 tests |
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

* [v1-set-of-substrings](../v1-set-of-substrings/README.md): Set of substrings (`O(n · L)` time, `O(n · L)` space)
