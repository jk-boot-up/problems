# 212. Word Search II — v2: Trie + backtracking

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Trie &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/word-search-ii/)

## Problem

Given an `m × n` board of letters and a list of `words`, return all words that can be formed by a path of **adjacent** cells
(horizontally or vertically). A cell may be used at most once per word. Return the words in any order.

**Example**
```
Input:  board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

**Constraints**
* `1 <= m, n <= 12`; `1 <= words.length <= 3 * 10^4`; `1 <= words[i].length <= 10`

## Approach: Trie + backtracking

> Put all words in a trie and DFS the board once; the trie prunes any path that is not a prefix of some word.

**Shared trie.** Build a trie of all words, storing the full word at its end node. DFS from every cell, following the trie child for
the cell's letter; mark cells as used (`'#'`) during the path. When a node holds a word, record it and clear it (no duplicates).
Prune leaf nodes once they are exhausted.

* Time: **O(m·n·3^L)** — from each cell, a path of length up to L branches into at most 3 new directions per step.
* Space: **O(total letters)** — the trie (plus O(L) recursion).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0212/v2/WordSearchII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0212/v2/WordSearchIITest.java` | JUnit 6 tests |
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

* [v1-separate-dfs-for-every-word](../v1-separate-dfs-for-every-word/README.md): Separate DFS for every word (`O(W·m·n·3^L)` time, `O(L)` space)
