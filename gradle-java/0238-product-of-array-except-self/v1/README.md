# 238. Product of Array Except Self — v1: Prefix and suffix arrays

[← Problem statement](../README.md)

> Precompute products to the left and to the right of every index, then multiply them.

## Approach

**Two helper arrays.** `left[i]` = product of `nums[0..i-1]`, `right[i]` = product of `nums[i+1..n-1]`;
`answer[i] = left[i] * right[i]`.

* Time: **O(n)** — three linear passes.
* Space: **O(n)** — two extra arrays besides the output.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0238/v1/ProductExceptSelf.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0238/v1/ProductExceptSelfTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
