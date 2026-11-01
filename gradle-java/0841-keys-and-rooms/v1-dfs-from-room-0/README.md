# 841. Keys and Rooms — v1: DFS from room 0

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/keys-and-rooms/)

## Problem

There are `n` locked rooms except room 0. `rooms[i]` lists the keys found in room `i`. Return `true` if you can visit every room.

**Example**
```
[[1],[2],[3],[]]        → true
[[1,3],[3,0,1],[2],[0]] → false
```

**Constraints**
* `2 <= n <= 1000`

## Approach: DFS from room 0

> Rooms are nodes and keys are edges; DFS from room 0 and check that every room was reached.

**Graph reachability.** DFS with a stack from room 0, marking rooms as visited; count visits.

* Time: **O(n + k)** — k is the total number of keys.
* Space: **O(n)** — visited flags and the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0841/v1/KeysAndRooms.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0841/v1/KeysAndRoomsTest.java` | JUnit 6 tests |
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
