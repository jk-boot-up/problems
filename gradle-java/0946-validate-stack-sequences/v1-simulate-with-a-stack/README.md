# 946. Validate Stack Sequences — v1: Simulate with a stack

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/validate-stack-sequences/)

## Problem

Given two arrays `pushed` and `popped` with distinct values, return `true` if they could be the result of a sequence of push and pop
operations on an initially empty stack.

**Example**
```
pushed = [1,2,3,4,5], popped = [4,5,3,2,1] → true
pushed = [1,2,3,4,5], popped = [4,3,5,1,2] → false
```

**Constraints**
* `1 <= n <= 1000`; `popped` is a permutation of `pushed`

## Approach: Simulate with a stack

> Replay the pushes on a real stack and pop greedily whenever the top is the next value to pop.

**Greedy replay.** Push values in order. After each push, pop while the top equals the next expected popped value. Popping as early as
possible never hurts, because a value on top can only leave by being popped now or later, and later only buries it. The sequence is valid
iff the stack ends empty.

* Time: **O(n)** — each value is pushed and popped once.
* Space: **O(n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0946/v1/ValidateStackSequences.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0946/v1/ValidateStackSequencesTest.java` | JUnit 6 tests |
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
