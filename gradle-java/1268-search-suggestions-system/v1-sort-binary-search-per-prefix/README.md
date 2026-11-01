# 1268. Search Suggestions System — v1: Sort + binary search per prefix

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-suggestions-system/)

## Problem

As each character of `searchWord` is typed, suggest up to three products that start with the typed prefix, in lexicographic order.
Return the list of suggestions after each character.

**Example**
```
products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
→ [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
```

**Constraints**
* `1 <= products.length <= 1000`

## Approach: Sort + binary search per prefix

> Sort the products; for each typed prefix, binary-search where it would start and take up to three matches from there.

**Lower bound.** Sort products. Products sharing a prefix are contiguous, so binary-search the first product `>= prefix` and take up to three
that start with the prefix.

* Time: **O(n log n + L·(log n + 3))** — sorting plus a search per prefix (string comparisons cost O(L)).
* Space: **O(n)** — the sorted copy.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1268/v1/SearchSuggestions.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1268/v1/SearchSuggestionsTest.java` | JUnit 6 tests |
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
