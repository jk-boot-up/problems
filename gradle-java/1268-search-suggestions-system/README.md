# 1268. Search Suggestions System

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-suggestions-system/)

## Problem

As each character of `searchWord` is typed, suggest up to three products that start with the typed prefix, in lexicographic order.
Return the list of suggestions after each character.

**Example**
```
products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
→ [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
```

**Constraints**
* `1 <= products.length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-binary-search-per-prefix](v1-sort-binary-search-per-prefix/README.md) | Sort + binary search per prefix | `O(n log n + L·(log n + 3))` | `O(n)` | [▶ animation](v1-sort-binary-search-per-prefix/animation/index.html) |
