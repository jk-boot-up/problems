# 93. Restore IP Addresses

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

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-backtracking-over-four-parts](v1-backtracking-over-four-parts/README.md) | Backtracking over four parts | `O(1)` | `O(1)` | [▶ animation](v1-backtracking-over-four-parts/animation/index.html) |
