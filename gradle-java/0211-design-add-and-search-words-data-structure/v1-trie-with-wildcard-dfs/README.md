# 211. Design Add and Search Words Data Structure — v1: Trie with wildcard DFS

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Trie &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

## Problem

Design `WordDictionary`:
* `addWord(word)`: add a lowercase word;
* `search(word)`: `true` if any added word matches, where `.` matches **any one letter**.

**Example**
```
addWord("bad"); addWord("dad"); addWord("mad");
search("pad") → false; search("bad") → true; search(".ad") → true; search("b..") → true
```

**Constraints**
* `1 <= word.length <= 25`; at most 2 dots per search; at most `10^4` calls.

## Approach: Trie with wildcard DFS

> A trie handles exact letters directly; a '.' wildcard branches into every existing child.

**Trie + DFS.** Insert as in a normal trie. `search(i, node)`: for a letter follow that child; for `.` try every non-null child
recursively. Succeed at the end only if the node marks a word end.

* Time: **O(L)** — per add; search is O(26^d · L) with d dots (here at most 2).
* Space: **O(total letters)** — the trie nodes.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0211/v1/WordDictionary.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0211/v1/WordDictionaryTest.java` | JUnit 6 tests |
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
