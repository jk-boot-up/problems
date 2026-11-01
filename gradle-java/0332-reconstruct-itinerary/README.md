# 332. Reconstruct Itinerary

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reconstruct-itinerary/)

## Problem

Given airline `tickets[i] = [from, to]`, use **all** tickets exactly once to build an itinerary starting at `"JFK"`. If several are valid,
return the lexicographically smallest. At least one valid itinerary exists.

**Example**
```
[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]] → ["JFK","MUC","LHR","SFO","SJC"]
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]] → ["JFK","ATL","JFK","SFO","ATL","SFO"]
```

**Constraints**
* `1 <= tickets.length <= 300`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-hierholzer-with-sorted-destinations](v1-hierholzer-with-sorted-destinations/README.md) | Hierholzer with sorted destinations | `O(E log E)` | `O(E)` | [▶ animation](v1-hierholzer-with-sorted-destinations/animation/index.html) |
