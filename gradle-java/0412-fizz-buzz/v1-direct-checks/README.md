# 412. Fizz Buzz — v1: Direct checks

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/fizz-buzz/)

## Problem

Return a list of `1..n` as strings where multiples of 3 are `"Fizz"`, multiples of 5 `"Buzz"`, multiples of both `"FizzBuzz"`.

**Example**
```
n = 5 → ["1","2","Fizz","4","Buzz"]
```

**Constraints**
* `1 <= n <= 10^4`

## Approach: Direct checks

> Check divisibility by 15 first, then by 3 and by 5.

**Build the label.** Append `"Fizz"` if divisible by 3 and `"Buzz"` if divisible by 5; if nothing was appended, use the number.

* Time: **O(n)** — one pass.
* Space: **O(1)** — apart from the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0412/v1/FizzBuzz.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0412/v1/FizzBuzzTest.java` | JUnit 6 tests |
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
