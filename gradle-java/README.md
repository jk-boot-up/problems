# LeetCode Top Interview 150 — Java 25 + Gradle 9.8.2

The problems of LeetCode's **Top Interview 150** study plan. Each problem is a standalone Gradle build:

```
0088-merge-sorted-array/
├── README.md              problem statement (in our own words), examples, constraints, versions table
├── settings.gradle.kts    includes one subproject per solution version
├── gradlew                Gradle 9.8.2 wrapper
├── v1/                    simplest approach
│   ├── src/main/java      Java 25 solution
│   ├── src/test/java      JUnit 6 tests
│   └── animation/         narrated, animated walkthrough (index.html)
└── v2/ … v5/              further approaches, up to the most efficient one
```

Each `animation/index.html` is self-contained and works offline:

* **Problem** tab: statement, examples, key idea and approach.
* **Walkthrough** tab: several scenarios (examples and edge cases) animated step by step; each step is read aloud
  with the browser's Web Speech API (no audio files needed).
* **Complexity** tab: time and space complexity with a growth chart, compared across the problem's versions.
* Light / Medium / Dark themes (remembered between visits), keyboard shortcuts, and links between versions.

## Build

```bash
cd 0088-merge-sorted-array && ./gradlew test   # every version of one problem
./gradlew testAll                               # everything (composite build, run from gradle-java/)
```

The Gradle toolchain asks for JDK 25; the foojay resolver plugin downloads it if it is not installed.

## Regenerating

All projects are generated from `tools/problems/batch_*.py` by `python3 tools/generate.py`.
The shared animation player lives in `tools/engine/`.

## Problems

| # | LeetCode | Problem | Difficulty | Topic | Versions | Best time | Animations |
|---|----------|---------|------------|-------|----------|-----------|------------|
| 1 | 88 | [Merge Sorted Array](0088-merge-sorted-array/README.md) | Easy | Array / String | 2 | `O(m + n)` | [v1](0088-merge-sorted-array/v1/animation/index.html) [v2](0088-merge-sorted-array/v2/animation/index.html) |
| 2 | 27 | [Remove Element](0027-remove-element/README.md) | Easy | Array / String | 1 | `O(n)` | [v1](0027-remove-element/v1/animation/index.html) |
| 3 | 26 | [Remove Duplicates from Sorted Array](0026-remove-duplicates-from-sorted-array/README.md) | Easy | Array / String | 1 | `O(n)` | [v1](0026-remove-duplicates-from-sorted-array/v1/animation/index.html) |
| 4 | 80 | [Remove Duplicates from Sorted Array II](0080-remove-duplicates-from-sorted-array-ii/README.md) | Medium | Array / String | 1 | `O(n)` | [v1](0080-remove-duplicates-from-sorted-array-ii/v1/animation/index.html) |
| 5 | 169 | [Majority Element](0169-majority-element/README.md) | Easy | Array / String | 3 | `O(n)` | [v1](0169-majority-element/v1/animation/index.html) [v2](0169-majority-element/v2/animation/index.html) [v3](0169-majority-element/v3/animation/index.html) |
| 6 | 189 | [Rotate Array](0189-rotate-array/README.md) | Medium | Array / String | 2 | `O(n)` | [v1](0189-rotate-array/v1/animation/index.html) [v2](0189-rotate-array/v2/animation/index.html) |
| 7 | 121 | [Best Time to Buy and Sell Stock](0121-best-time-to-buy-and-sell-stock/README.md) | Easy | Array / String | 2 | `O(n)` | [v1](0121-best-time-to-buy-and-sell-stock/v1/animation/index.html) [v2](0121-best-time-to-buy-and-sell-stock/v2/animation/index.html) |
| 8 | 122 | [Best Time to Buy and Sell Stock II](0122-best-time-to-buy-and-sell-stock-ii/README.md) | Medium | Array / String | 1 | `O(n)` | [v1](0122-best-time-to-buy-and-sell-stock-ii/v1/animation/index.html) |
| 9 | 55 | [Jump Game](0055-jump-game/README.md) | Medium | Array / String | 1 | `O(n)` | [v1](0055-jump-game/v1/animation/index.html) |
| 10 | 45 | [Jump Game II](0045-jump-game-ii/README.md) | Medium | Array / String | 2 | `O(n)` | [v1](0045-jump-game-ii/v1/animation/index.html) [v2](0045-jump-game-ii/v2/animation/index.html) |
| 11 | 274 | [H-Index](0274-h-index/README.md) | Medium | Array / String | 2 | `O(n)` | [v1](0274-h-index/v1/animation/index.html) [v2](0274-h-index/v2/animation/index.html) |
| 12 | 380 | [Insert Delete GetRandom O(1)](0380-insert-delete-getrandom-o1/README.md) | Medium | Array / String | 1 | `O(1)` | [v1](0380-insert-delete-getrandom-o1/v1/animation/index.html) |
| 13 | 238 | [Product of Array Except Self](0238-product-of-array-except-self/README.md) | Medium | Array / String | 2 | `O(n)` | [v1](0238-product-of-array-except-self/v1/animation/index.html) [v2](0238-product-of-array-except-self/v2/animation/index.html) |
| 14 | 134 | [Gas Station](0134-gas-station/README.md) | Medium | Array / String | 2 | `O(n)` | [v1](0134-gas-station/v1/animation/index.html) [v2](0134-gas-station/v2/animation/index.html) |
| 15 | 135 | [Candy](0135-candy/README.md) | Hard | Array / String | 1 | `O(n)` | [v1](0135-candy/v1/animation/index.html) |
| 16 | 42 | [Trapping Rain Water](0042-trapping-rain-water/README.md) | Hard | Array / String | 2 | `O(n)` | [v1](0042-trapping-rain-water/v1/animation/index.html) [v2](0042-trapping-rain-water/v2/animation/index.html) |
| 17 | 13 | [Roman to Integer](0013-roman-to-integer/README.md) | Easy | Array / String | 1 | `O(n)` | [v1](0013-roman-to-integer/v1/animation/index.html) |
| 18 | 12 | [Integer to Roman](0012-integer-to-roman/README.md) | Medium | Array / String | 1 | `O(1)` | [v1](0012-integer-to-roman/v1/animation/index.html) |
| 19 | 58 | [Length of Last Word](0058-length-of-last-word/README.md) | Easy | Array / String | 1 | `O(n)` | [v1](0058-length-of-last-word/v1/animation/index.html) |
| 20 | 14 | [Longest Common Prefix](0014-longest-common-prefix/README.md) | Easy | Array / String | 1 | `O(S)` | [v1](0014-longest-common-prefix/v1/animation/index.html) |
| 21 | 151 | [Reverse Words in a String](0151-reverse-words-in-a-string/README.md) | Medium | Array / String | 2 | `O(n)` | [v1](0151-reverse-words-in-a-string/v1/animation/index.html) [v2](0151-reverse-words-in-a-string/v2/animation/index.html) |
| 22 | 6 | [Zigzag Conversion](0006-zigzag-conversion/README.md) | Medium | Array / String | 1 | `O(n)` | [v1](0006-zigzag-conversion/v1/animation/index.html) |
| 23 | 28 | [Find the Index of the First Occurrence in a String](0028-find-the-index-of-the-first-occurrence-in-a-string/README.md) | Easy | Array / String | 2 | `O(n + m)` | [v1](0028-find-the-index-of-the-first-occurrence-in-a-string/v1/animation/index.html) [v2](0028-find-the-index-of-the-first-occurrence-in-a-string/v2/animation/index.html) |
| 24 | 68 | [Text Justification](0068-text-justification/README.md) | Hard | Array / String | 1 | `O(L)` | [v1](0068-text-justification/v1/animation/index.html) |
| 25 | 125 | [Valid Palindrome](0125-valid-palindrome/README.md) | Easy | Two Pointers | 1 | `O(n)` | [v1](0125-valid-palindrome/v1/animation/index.html) |
| 26 | 392 | [Is Subsequence](0392-is-subsequence/README.md) | Easy | Two Pointers | 1 | `O(n)` | [v1](0392-is-subsequence/v1/animation/index.html) |
| 27 | 167 | [Two Sum II - Input Array Is Sorted](0167-two-sum-ii-input-array-is-sorted/README.md) | Medium | Two Pointers | 2 | `O(n)` | [v1](0167-two-sum-ii-input-array-is-sorted/v1/animation/index.html) [v2](0167-two-sum-ii-input-array-is-sorted/v2/animation/index.html) |
| 28 | 11 | [Container With Most Water](0011-container-with-most-water/README.md) | Medium | Two Pointers | 2 | `O(n)` | [v1](0011-container-with-most-water/v1/animation/index.html) [v2](0011-container-with-most-water/v2/animation/index.html) |
| 29 | 15 | [3Sum](0015-3sum/README.md) | Medium | Two Pointers | 2 | `O(n²)` | [v1](0015-3sum/v1/animation/index.html) [v2](0015-3sum/v2/animation/index.html) |
| 30 | 209 | [Minimum Size Subarray Sum](0209-minimum-size-subarray-sum/README.md) | Medium | Sliding Window | 2 | `O(n)` | [v1](0209-minimum-size-subarray-sum/v1/animation/index.html) [v2](0209-minimum-size-subarray-sum/v2/animation/index.html) |
| 31 | 3 | [Longest Substring Without Repeating Characters](0003-longest-substring-without-repeating-characters/README.md) | Medium | Sliding Window | 2 | `O(n)` | [v1](0003-longest-substring-without-repeating-characters/v1/animation/index.html) [v2](0003-longest-substring-without-repeating-characters/v2/animation/index.html) |
| 32 | 30 | [Substring with Concatenation of All Words](0030-substring-with-concatenation-of-all-words/README.md) | Hard | Sliding Window | 2 | `O(n·L)` | [v1](0030-substring-with-concatenation-of-all-words/v1/animation/index.html) [v2](0030-substring-with-concatenation-of-all-words/v2/animation/index.html) |
| 33 | 76 | [Minimum Window Substring](0076-minimum-window-substring/README.md) | Hard | Sliding Window | 1 | `O(m + n)` | [v1](0076-minimum-window-substring/v1/animation/index.html) |
| 34 | 36 | [Valid Sudoku](0036-valid-sudoku/README.md) | Medium | Matrix | 1 | `O(1)` | [v1](0036-valid-sudoku/v1/animation/index.html) |
| 35 | 54 | [Spiral Matrix](0054-spiral-matrix/README.md) | Medium | Matrix | 1 | `O(m·n)` | [v1](0054-spiral-matrix/v1/animation/index.html) |
| 36 | 48 | [Rotate Image](0048-rotate-image/README.md) | Medium | Matrix | 2 | `O(n²)` | [v1](0048-rotate-image/v1/animation/index.html) [v2](0048-rotate-image/v2/animation/index.html) |
| 37 | 73 | [Set Matrix Zeroes](0073-set-matrix-zeroes/README.md) | Medium | Matrix | 2 | `O(m·n)` | [v1](0073-set-matrix-zeroes/v1/animation/index.html) [v2](0073-set-matrix-zeroes/v2/animation/index.html) |
| 38 | 289 | [Game of Life](0289-game-of-life/README.md) | Medium | Matrix | 2 | `O(m·n)` | [v1](0289-game-of-life/v1/animation/index.html) [v2](0289-game-of-life/v2/animation/index.html) |
| 39 | 383 | [Ransom Note](0383-ransom-note/README.md) | Easy | Hashmap | 1 | `O(m + n)` | [v1](0383-ransom-note/v1/animation/index.html) |
| 40 | 205 | [Isomorphic Strings](0205-isomorphic-strings/README.md) | Easy | Hashmap | 1 | `O(n)` | [v1](0205-isomorphic-strings/v1/animation/index.html) |
| 41 | 290 | [Word Pattern](0290-word-pattern/README.md) | Easy | Hashmap | 1 | `O(n)` | [v1](0290-word-pattern/v1/animation/index.html) |
| 42 | 242 | [Valid Anagram](0242-valid-anagram/README.md) | Easy | Hashmap | 2 | `O(n)` | [v1](0242-valid-anagram/v1/animation/index.html) [v2](0242-valid-anagram/v2/animation/index.html) |
| 43 | 49 | [Group Anagrams](0049-group-anagrams/README.md) | Medium | Hashmap | 2 | `O(n·k)` | [v1](0049-group-anagrams/v1/animation/index.html) [v2](0049-group-anagrams/v2/animation/index.html) |
| 44 | 1 | [Two Sum](0001-two-sum/README.md) | Easy | Hashmap | 2 | `O(n)` | [v1](0001-two-sum/v1/animation/index.html) [v2](0001-two-sum/v2/animation/index.html) |
| 45 | 202 | [Happy Number](0202-happy-number/README.md) | Easy | Hashmap | 2 | `O(log n)` | [v1](0202-happy-number/v1/animation/index.html) [v2](0202-happy-number/v2/animation/index.html) |
| 46 | 219 | [Contains Duplicate II](0219-contains-duplicate-ii/README.md) | Easy | Hashmap | 2 | `O(n)` | [v1](0219-contains-duplicate-ii/v1/animation/index.html) [v2](0219-contains-duplicate-ii/v2/animation/index.html) |
| 47 | 128 | [Longest Consecutive Sequence](0128-longest-consecutive-sequence/README.md) | Medium | Hashmap | 2 | `O(n)` | [v1](0128-longest-consecutive-sequence/v1/animation/index.html) [v2](0128-longest-consecutive-sequence/v2/animation/index.html) |
| 48 | 228 | [Summary Ranges](0228-summary-ranges/README.md) | Easy | Intervals | 1 | `O(n)` | [v1](0228-summary-ranges/v1/animation/index.html) |
| 49 | 56 | [Merge Intervals](0056-merge-intervals/README.md) | Medium | Intervals | 1 | `O(n log n)` | [v1](0056-merge-intervals/v1/animation/index.html) |
| 50 | 57 | [Insert Interval](0057-insert-interval/README.md) | Medium | Intervals | 1 | `O(n)` | [v1](0057-insert-interval/v1/animation/index.html) |
