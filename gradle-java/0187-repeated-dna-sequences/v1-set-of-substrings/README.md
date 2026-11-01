# 187. Repeated DNA Sequences — v1: Set of substrings

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

## Approach: Set of substrings

> Slice every 10-letter window and remember it in a set of strings.

**Substring set.** For each start, take the 10-letter substring. Adding it to `seen` fails for a repeat; report it the first time that
happens.

* Time: **O(n · L)** — `L = 10` characters copied and hashed per window.
* Space: **O(n · L)** — the stored substrings.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0187/v1/RepeatedDNA.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0187/v1/RepeatedDNATest.java` | JUnit 6 tests |
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

* [v2-rolling-2-bit-encoding](../v2-rolling-2-bit-encoding/README.md): Rolling 2-bit encoding (`O(n)` time, `O(n)` space)
