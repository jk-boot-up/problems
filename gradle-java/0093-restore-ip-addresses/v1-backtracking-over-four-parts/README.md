# 93. Restore IP Addresses — v1: Backtracking over four parts

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/restore-ip-addresses/)

## Problem

Return every valid IPv4 address that can be formed by inserting three dots into the digit string `s` (no reordering or removal). A valid part
is 0–255 with no leading zeros.

**Example**
```
"25525511135" → ["255.255.11.135","255.255.111.35"]
"0000"        → ["0.0.0.0"]
"101023"      → ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

**Constraints**
* `1 <= s.length <= 20`

## Approach: Backtracking over four parts

> Choose 1–3 digits for each of the four parts, rejecting parts above 255 or with leading zeros.

**Backtracking.** At part `p` from index `i`, try lengths 1–3; skip if not enough digits remain for the other parts, if the part has a
leading zero, or if it exceeds 255. After four parts, accept if all digits were used.

* Time: **O(1)** — at most 3⁴ = 81 combinations.
* Space: **O(1)** — four parts of recursion.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0093/v1/RestoreIPAddresses.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0093/v1/RestoreIPAddressesTest.java` | JUnit 6 tests |
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
