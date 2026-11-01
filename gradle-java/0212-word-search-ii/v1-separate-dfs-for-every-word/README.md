# 212. Word Search II — v1: Separate DFS for every word

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

## Approach: Separate DFS for every word

> Run the single-word search (Word Search I) for each word independently.

**One search per word.** For each word, try every cell as a start and backtrack along matching letters.

* Time: **O(W·m·n·3^L)** — the board is searched again for every one of the W words.
* Space: **O(L)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0212/v1/WordSearchII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0212/v1/WordSearchIITest.java` | JUnit 6 tests |
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

* [v2-trie-backtracking](../v2-trie-backtracking/README.md): Trie + backtracking (`O(m·n·3^L)` time, `O(total letters)` space)
