# 208. Implement Trie (Prefix Tree) — v1: Array-of-children trie

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Trie &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/)

## Problem

Implement a **trie** (prefix tree) of lowercase words:
* `insert(word)`
* `search(word)`: `true` if `word` was inserted
* `startsWith(prefix)`: `true` if some inserted word starts with `prefix`

**Example**
```
insert("apple"); search("apple") → true; search("app") → false;
startsWith("app") → true; insert("app"); search("app") → true
```

**Constraints**
* `1 <= word.length, prefix.length <= 2000`; at most `3 * 10^4` calls.

## Approach: Array-of-children trie

> Each node has 26 child slots; a word is a path from the root, with an end-of-word flag on its last node.

**Fixed child arrays.** Each node holds `Node[26] children` and a boolean `end`. `insert` walks the letters, creating missing nodes,
and marks the last node. `search` and `startsWith` walk the same path; `search` also needs `end`.

* Time: **O(L)** — per operation, L being the word length.
* Space: **O(total letters)** — at most one node per inserted letter.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0208/v1/Trie.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0208/v1/TrieTest.java` | JUnit 6 tests |
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
