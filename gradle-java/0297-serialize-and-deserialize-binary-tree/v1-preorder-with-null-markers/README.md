# 297. Serialize and Deserialize Binary Tree — v1: Preorder with null markers

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

## Problem

Design `serialize(TreeNode)` → `String` and `deserialize(String)` → `TreeNode` so that deserializing a serialized tree reproduces it
exactly. Any format is allowed.

**Example**
```
[1,2,3,null,null,4,5] → "1,2,#,#,3,4,#,#,5,#,#" → [1,2,3,null,null,4,5]
```

**Constraints**
* `0 <= n <= 10^4`; `-1000 <= Node.val <= 1000`

## Approach: Preorder with null markers

> Write the tree in preorder with a marker for every null child; reading it back in the same order rebuilds it uniquely.

**Preorder + `#`.** Serialize: value, then left subtree, then right subtree, with `#` for null. Deserialize: read tokens in the same order;
`#` returns null, otherwise create the node and build its left then right subtree. An explicit stack avoids deep recursion.

* Time: **O(n)** — each node is written and read once.
* Space: **O(n)** — the string and the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0297/v1/Codec.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0297/v1/CodecTest.java` | JUnit 6 tests |
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
