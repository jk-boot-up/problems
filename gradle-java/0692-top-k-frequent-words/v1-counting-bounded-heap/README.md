# 692. Top K Frequent Words — v1: Counting + bounded heap

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/top-k-frequent-words/)

## Problem

Return the `k` most frequent words, sorted by frequency (highest first); equal frequencies are sorted alphabetically.

**Example**
```
["i","love","leetcode","i","love","coding"], k = 2 → ["i","love"]
["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4 → ["the","is","sunny","day"]
```

**Constraints**
* `1 <= words.length <= 500`; `k` is valid.

## Approach: Counting + bounded heap

> Count words, then keep a size-k heap ordered so the 'worst' word (lowest count, then largest alphabetically) is on top.

**Bounded heap.** Count with `MyHashMap`. Push each word into a heap whose top is the least desirable word (lower count first, then
alphabetically later); pop when the size exceeds `k`. Pop all and reverse.

* Time: **O(n log k)** — heap operations of size k.
* Space: **O(n)** — the counts.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0692/v1/TopKFrequentWords.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0692/v1/TopKFrequentWordsTest.java` | JUnit 6 tests |
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
