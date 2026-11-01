# 238. Product of Array Except Self — v2: Output array + running suffix

[← Problem statement](../README.md)

> answer[i] = (product of everything left of i) × (product of everything right of i), built in two passes.

## Approach

**Prefix and suffix products.** First pass, left to right: `answer[i]` = product of all values before `i`.
Second pass, right to left: keep a running `suffix` product and multiply it into `answer[i]`.

* Time: **O(n)** — two linear passes.
* Space: **O(1)** — besides the output, only the running suffix product.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0238/v2/ProductExceptSelf.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0238/v2/ProductExceptSelfTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
