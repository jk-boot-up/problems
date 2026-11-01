# 650. 2 Keys Keyboard — v2: Sum of prime factors

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/2-keys-keyboard/)

## Problem

The screen starts with one `'A'`. Each step is either **Copy All** (copy everything on screen) or **Paste** (append the last copy). Return
the minimum number of steps to get exactly `n` letters.

**Example**
```
n = 3 → 3   (copy, paste, paste)
n = 1 → 0
n = 6 → 5   (copy, paste → 2; copy, paste, paste → 6)
```

**Constraints**
* `1 <= n <= 1000`

## Approach: Sum of prime factors

> Copying d letters and pasting them d − 1 more times multiplies the count by d at a cost of d, so the answer is the sum of the prime factors.

**Factorisation.** A copy followed by `d - 1` pastes multiplies the length by `d` and costs `d` steps. So any plan is a factorisation
`n = d₁ · d₂ · …` with cost `d₁ + d₂ + …`. Splitting a composite `d = a · b` never costs more (`a + b <= a · b`), so the minimum is the
sum of the prime factors (with multiplicity).

* Time: **O(√n)** — trial division.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0650/v2/TwoKeysKeyboard.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0650/v2/TwoKeysKeyboardTest.java` | JUnit 6 tests |
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

* [v1-dynamic-programming-over-divisors](../v1-dynamic-programming-over-divisors/README.md): Dynamic programming over divisors (`O(n²)` time, `O(n)` space)
