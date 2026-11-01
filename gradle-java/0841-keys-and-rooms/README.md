# 841. Keys and Rooms

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

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-from-room-0](v1-dfs-from-room-0/README.md) | DFS from room 0 | `O(n + k)` | `O(n)` | [▶ animation](v1-dfs-from-room-0/animation/index.html) |
