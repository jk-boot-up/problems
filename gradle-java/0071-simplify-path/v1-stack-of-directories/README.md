# 71. Simplify Path — v1: Stack of directories

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/simplify-path/)

## Problem

Convert an absolute Unix-style `path` to its **canonical** form:
* `.` means the current directory and `..` the parent directory (staying at `/` if already there);
* multiple slashes count as one; other names, including `...`, are directory names;
* the result starts with one `/`, separates directories with single slashes and has no trailing slash.

**Example 1**
```
Input:  path = "/home//foo/"
Output: "/home/foo"
```

**Example 2**
```
Input:  path = "/a/./b/../../c/"
Output: "/c"
```

**Example 3**
```
Input:  path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
```

**Constraints**
* `1 <= path.length <= 3000`; letters, digits, `.`, `/`, `_`; starts with `/`.

## Approach: Stack of directories

> Split on '/', push real directory names, pop on '..', ignore '.' and empty parts.

**Stack.** Split on `/`. Skip empty parts and `.`; for `..` pop if possible; otherwise push the name. Join the stack from bottom
to top with `/`.

* Time: **O(n)** — splitting and joining are linear.
* Space: **O(n)** — the parts and the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0071/v1/SimplifyPath.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0071/v1/SimplifyPathTest.java` | JUnit 6 tests |
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
