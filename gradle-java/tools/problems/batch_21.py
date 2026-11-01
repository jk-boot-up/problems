PROBLEMS = [
P(num=337, slug="house-robber-iii", title="House Robber III", diff="Medium", topic="Binary Tree General", cls="HouseRobberIII",
idea="Each node returns two numbers: the best total if it is robbed, and if it is not.",
vname="Post-order pair DP", helpers=["TreeNode"],
spec=r'''
Houses form a binary tree; robbing two directly-linked houses (parent and child) triggers the alarm. Return the maximum amount you can rob.

**Example**
```
[3,2,3,null,3,null,1] → 7   (3 + 3 + 1)
[3,4,5,1,3,null,1]    → 9   (4 + 5)
```

**Constraints**
* `1 <= n <= 10^4`
''',
approach=r'''
**Pair per node.** `rob(n)` returns `[take, skip]`: `take = n.val + left.skip + right.skip`, `skip = max(left) + max(right)`.
The answer is `max(rob(root))`.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class HouseRobberIII {

    public int rob(TreeNode root) {
        int[] r = dfs(root);
        return Math.max(r[0], r[1]);
    }

    /** Returns {best if this node is robbed, best if it is not}. */
    private int[] dfs(TreeNode n) {
        if (n == null) return new int[]{0, 0};
        int[] l = dfs(n.left), r = dfs(n.right);
        int take = n.val + l[1] + r[1];
        int skip = Math.max(l[0], l[1]) + Math.max(r[0], r[1]);
        return new int[]{take, skip};
    }
}
''',
test=r'''
class HouseRobberIIITest {

    private final HouseRobberIII solution = new HouseRobberIII();

    @Test
    void examples() {
        assertEquals(7, solution.rob(TreeNode.of(3, 2, 3, null, 3, null, 1)));
        assertEquals(9, solution.rob(TreeNode.of(3, 4, 5, 1, 3, null, 1)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {};
  (function dfs(n) {
    if (!n) return [0, 0];
    const l = dfs(n.left), r = dfs(n.right), take = n.val + l[1] + r[1], skip = Math.max(...l) + Math.max(...r);
    hl[n.id] = take >= skip ? 'ok' : 'sel';
    A.step(`${n.val}: rob it → ${n.val} + children skipped (${l[1]} + ${r[1]}) = ${take}; skip it → best of each child = ${skip}.`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'cur' } }), A.vars({ node: n.val, take, skip }));
    return [take, skip];
  })(root);
  A.step('Green nodes prefer being robbed; blue nodes prefer being skipped. The root takes the better of its two numbers.', A.tree('tree', root, { hl }));
}
A.scenario('Classic', '[3,4,5,1,3,null,1]', () => run([3, 4, 5, 1, 3, null, 1]));
'''),

P(num=338, slug="counting-bits", title="Counting Bits", diff="Easy", topic="Bit Manipulation", cls="CountingBits",
idea="bits(i) = bits(i >> 1) + (i & 1): drop the last bit, which you already counted, then add it back.",
vname="DP on i >> 1",
spec=r'''
For every `i` in `0..n`, return the number of `1` bits in its binary representation.

**Example**
```
n = 5 → [0,1,1,2,1,2]
```

**Constraints**
* `0 <= n <= 10^5`

**Follow-up:** O(n) without a built-in bit count.
''',
approach=r'''
**Reuse smaller answers.** `i >> 1` is `i` without its last bit and is smaller than `i`, so `ans[i] = ans[i >> 1] + (i & 1)`.

* Time: **O(n)** — O(1) per number.
* Space: **O(1)** — apart from the output.
''',
sc="1",
java=r'''
public class CountingBits {

    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        for (int i = 1; i <= n; i++) ans[i] = ans[i >> 1] + (i & 1);
        return ans;
    }
}
''',
test=r'''
class CountingBitsTest {

    private final CountingBits solution = new CountingBits();

    @Test
    void examples() {
        assertArrayEquals(new int[]{0, 1, 1}, solution.countBits(2));
        assertArrayEquals(new int[]{0, 1, 1, 2, 1, 2}, solution.countBits(5));
        assertArrayEquals(new int[]{0}, solution.countBits(0));
    }
}
''',
trace=r'''
function run(n) {
  const ans = [0];
  A.step('ans[0] = 0. Every larger number reuses the answer for itself shifted right by one.', A.arr('ans', ans));
  for (let i = 1; i <= n; i++) { ans.push(ans[i >> 1] + (i & 1)); A.step(`${i} = ${i.toString(2)}: ans[${i >> 1}] (${(i >> 1).toString(2) || 0}) + last bit ${i & 1} = ${ans[i]}.`, A.arr('ans', ans, { hl: { [i]: 'ok', [i >> 1]: 'sel' } })); }
}
A.scenario('n = 8', '0..8', () => run(8));
'''),

P(num=371, slug="sum-of-two-integers", title="Sum of Two Integers", diff="Medium", topic="Bit Manipulation", cls="SumOfTwoIntegers",
idea="XOR adds without carries, AND shifted left gives the carries; repeat until no carry remains.",
vname="XOR and carry",
spec=r'''
Return `a + b` without using the `+` or `-` operators.

**Example**
```
1 + 2 = 3,   2 + 3 = 5,   -1 + 1 = 0
```

**Constraints**
* `-1000 <= a, b <= 1000`
''',
approach=r'''
**Binary addition.** `a ^ b` is the sum ignoring carries; `(a & b) << 1` is the carry. Replace `a` with the partial sum and `b` with the
carry until the carry is 0. Two's complement makes negative numbers work too (Java ints wrap).

* Time: **O(1)** — at most 32 iterations.
* Space: **O(1)** — two ints.
''',
java=r'''
public class SumOfTwoIntegers {

    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a ^= b;
            b = carry;
        }
        return a;
    }
}
''',
test=r'''
class SumOfTwoIntegersTest {

    private final SumOfTwoIntegers solution = new SumOfTwoIntegers();

    @ParameterizedTest
    @CsvSource({"1,2,3", "2,3,5", "-1,1,0", "-12,-8,-20", "1000,-999,1"})
    void sums(int a, int b, int expected) {
        assertEquals(expected, solution.getSum(a, b));
    }
}
''',
trace=r'''
function run(a, b) {
  const bits = v => ((v >>> 0) & 0xff).toString(2).padStart(8, '0').split('');
  A.step(`Add ${a} and ${b} using only bit operations (low 8 bits shown).`, A.arr('a', bits(a), { noIdx: true }), A.arr('b', bits(b), { noIdx: true }));
  while (b !== 0) {
    const carry = (a & b) << 1; a ^= b; b = carry;
    A.step(`XOR gives the sum without carries: ${a}. AND shifted left gives the carries: ${b}.`, A.arr('partial sum', bits(a), { noIdx: true, hl: Object.fromEntries(bits(a).map((c, i) => [i, c === '1' ? 'sel' : ''])) }), A.arr('carry', bits(b), { noIdx: true, hl: Object.fromEntries(bits(b).map((c, i) => [i, c === '1' ? 'alt' : ''])) }));
  }
  A.step(`No carries remain. The sum is ${a}.`, A.text('Result', a, 'ok'));
}
A.scenario('2 + 3', 'a = 2, b = 3', () => run(2, 3));
A.scenario('7 + 9', 'a = 7, b = 9', () => run(7, 9));
'''),

P(num=416, slug="partition-equal-subset-sum", title="Partition Equal Subset Sum", diff="Medium", topic="1D DP", cls="PartitionEqualSubsetSum",
idea="Can some subset reach half of the total? A boolean knapsack over sums answers that.",
vname="0/1 knapsack on sums",
spec=r'''
Return `true` if `nums` can be split into two subsets with equal sums.

**Example**
```
[1,5,11,5] → true ([1,5,5] and [11]),   [1,2,3,5] → false
```

**Constraints**
* `1 <= nums.length <= 200`; `1 <= nums[i] <= 100`
''',
approach=r'''
**Subset sum.** If the total is odd, it is impossible. Otherwise `can[s]` says whether some subset sums to `s`; for each number `x`, update
`s` from `target` down to `x`: `can[s] |= can[s - x]` (going down uses each number once).

* Time: **O(n · S)** — S is half the total.
* Space: **O(S)** — one boolean array.
''',
tc="n2", sc="n",
java=r'''
public class PartitionEqualSubsetSum {

    public boolean canPartition(int[] nums) {
        int total = 0;
        for (int x : nums) total += x;
        if (total % 2 == 1) return false;
        int target = total / 2;
        boolean[] can = new boolean[target + 1];
        can[0] = true;
        for (int x : nums) {
            for (int s = target; s >= x; s--) can[s] |= can[s - x];
        }
        return can[target];
    }
}
''',
test=r'''
class PartitionEqualSubsetSumTest {

    private final PartitionEqualSubsetSum solution = new PartitionEqualSubsetSum();

    @Test
    void examples() {
        assertTrue(solution.canPartition(new int[]{1, 5, 11, 5}));
        assertFalse(solution.canPartition(new int[]{1, 2, 3, 5}));
        assertFalse(solution.canPartition(new int[]{1}));
    }
}
''',
trace=r'''
function run(nums) {
  const total = nums.reduce((s, x) => s + x, 0);
  A.step(`Add up all the numbers: ${total}. Two equal halves need an even total.`, A.arr('nums', nums), A.vars({ total }));
  if (total % 2) { A.step(`The total ${total} is odd, so it cannot be split evenly.`, A.arr('nums', nums), A.text('Result', 'false', 'bad')); return; }
  const target = total / 2, can = [true, ...new Array(target).fill(false)];
  A.step(`The total is ${total}, so each half must sum to ${target}. can[s] marks sums some subset can reach.`, A.arr('nums', nums), A.arr('can', can.map(v => (v ? 'T' : ''))));
  nums.forEach((x, i) => {
    const added = {}; for (let s = target; s >= x; s--) if (!can[s] && can[s - x]) { can[s] = true; added[s] = 'ok'; }
    A.step(`With ${x}: every reachable sum s also reaches s + ${x}.`, A.arr('nums', nums, { hl: { [i]: 'cur' } }), A.arr('can', can.map(v => (v ? 'T' : '')), { hl: { ...Object.fromEntries(can.map((v, k) => [k, v ? 'sel' : ''])), ...added, [target]: can[target] ? 'ok' : 'alt' } }));
  });
  A.step(can[target] ? `${target} is reachable, so an equal split exists.` : `${target} is not reachable.`, A.text('Result', String(can[target]), can[target] ? 'ok' : 'bad'));
}
A.scenario('Possible', 'nums = [1,5,11,5]', () => run([1, 5, 11, 5]));
A.scenario('Impossible', 'nums = [1,2,3,5]', () => run([1, 2, 3, 5]));
'''),

P(num=494, slug="target-sum", title="Target Sum", diff="Medium", topic="1D DP", cls="TargetSum",
idea="Choosing a plus-set P: sum(P) = (total + target) / 2, so count subsets with that sum.",
vname="Subset-count DP",
spec=r'''
Put `+` or `-` in front of every number of `nums` so the expression evaluates to `target`. Return the number of ways.

**Example**
```
nums = [1,1,1,1,1], target = 3 → 5
nums = [1], target = 1          → 1
```

**Constraints**
* `1 <= nums.length <= 20`; `0 <= nums[i] <= 1000`; `-1000 <= target <= 1000`
''',
approach=r'''
**Reduce to subset counting.** With `P` the numbers given `+`: `sum(P) - (total - sum(P)) = target`, so `sum(P) = (total + target) / 2`.
If that is negative or not an integer, there are 0 ways. Otherwise `ways[s] += ways[s - x]` for each `x`, iterating `s` downward.

* Time: **O(n · S)** — S = (total + target) / 2.
* Space: **O(S)** — one array.
''',
tc="n2", sc="n",
java=r'''
public class TargetSum {

    public int findTargetSumWays(int[] nums, int target) {
        int total = 0;
        for (int x : nums) total += x;
        if (Math.abs(target) > total || (total + target) % 2 != 0) return 0;
        int goal = (total + target) / 2;
        int[] ways = new int[goal + 1];
        ways[0] = 1;
        for (int x : nums) {
            for (int s = goal; s >= x; s--) ways[s] += ways[s - x];
        }
        return ways[goal];
    }
}
''',
test=r'''
class TargetSumTest {

    private final TargetSum solution = new TargetSum();

    @Test
    void examples() {
        assertEquals(5, solution.findTargetSumWays(new int[]{1, 1, 1, 1, 1}, 3));
        assertEquals(1, solution.findTargetSumWays(new int[]{1}, 1));
    }

    @Test
    void zeros() {
        assertEquals(4, solution.findTargetSumWays(new int[]{0, 0, 1}, 1));
        assertEquals(0, solution.findTargetSumWays(new int[]{1}, 2));
    }
}
''',
trace=r'''
function run(nums, target) {
  const total = nums.reduce((s, x) => s + x, 0), goal = (total + target) / 2;
  A.step(`Let P be the numbers given a plus sign. Then sum(P) − (${total} − sum(P)) = ${target}, so sum(P) = (${total} + ${target}) / 2 = ${goal}.`, A.arr('nums', nums));
  const ways = [1, ...new Array(goal).fill(0)];
  nums.forEach((x, i) => { for (let s = goal; s >= x; s--) ways[s] += ways[s - x]; A.step(`Include ${x}: ways[s] += ways[s − ${x}].`, A.arr('nums', nums, { hl: { [i]: 'cur' } }), A.arr('ways (subsets per sum)', ways, { hl: { [goal]: 'alt' } })); });
  A.step(`${ways[goal]} subsets sum to ${goal}, so ${ways[goal]} sign assignments reach ${target}.`, A.text('Result', ways[goal], 'ok'));
}
A.scenario('Five ones', 'nums = [1,1,1,1,1], target = 3', () => run([1, 1, 1, 1, 1], 3));
'''),

P(num=518, slug="coin-change-ii", title="Coin Change II", diff="Medium", topic="1D DP", cls="CoinChangeII",
idea="Loop coins on the outside so each combination is counted once, in a fixed coin order.",
vname="Unbounded knapsack counting",
spec=r'''
Return the number of **combinations** of coins (unlimited supply) that make up `amount`. Order does not matter.

**Example**
```
amount = 5, coins = [1,2,5] → 4,   amount = 3, coins = [2] → 0,   amount = 10, coins = [10] → 1
```

**Constraints**
* `0 <= amount <= 5000`; `1 <= coins.length <= 300`
''',
approach=r'''
**Coins outer, amounts inner.** `ways[0] = 1`. For each coin `c`, for `a` from `c` up to `amount`: `ways[a] += ways[a - c]`. Because
coins are processed one at a time, `1+2` and `2+1` are not both counted.

* Time: **O(coins · amount)** — every pair.
* Space: **O(amount)** — one array.
''',
tc="n2", sc="n",
java=r'''
public class CoinChangeII {

    public int change(int amount, int[] coins) {
        int[] ways = new int[amount + 1];
        ways[0] = 1;
        for (int c : coins) {
            for (int a = c; a <= amount; a++) ways[a] += ways[a - c];
        }
        return ways[amount];
    }
}
''',
test=r'''
class CoinChangeIITest {

    private final CoinChangeII solution = new CoinChangeII();

    @Test
    void examples() {
        assertEquals(4, solution.change(5, new int[]{1, 2, 5}));
        assertEquals(0, solution.change(3, new int[]{2}));
        assertEquals(1, solution.change(10, new int[]{10}));
        assertEquals(1, solution.change(0, new int[]{7}));
    }
}
''',
trace=r'''
function run(amount, coins) {
  const ways = [1, ...new Array(amount).fill(0)];
  A.step('ways[a] counts coin combinations making a. Process one coin type at a time so order does not matter.', A.arr('ways', ways));
  coins.forEach(c => { for (let a = c; a <= amount; a++) ways[a] += ways[a - c]; A.step(`Allow coin ${c}: ways[a] += ways[a − ${c}].`, A.arr('ways', ways, { hl: Object.fromEntries([...Array(amount - c + 1)].map((_, t) => [c + t, 'sel'])) })); });
  A.step(`${ways[amount]} combinations make ${amount}.`, A.arr('ways', ways, { hl: { [amount]: 'ok' } }), A.text('Result', ways[amount], 'ok'));
}
A.scenario('amount = 5', 'coins = [1,2,5]', () => run(5, [1, 2, 5]));
'''),

P(num=1143, slug="longest-common-subsequence", title="Longest Common Subsequence", diff="Medium", topic="Multidimensional DP", cls="LongestCommonSubsequence",
idea="If the last letters match they extend the LCS of the shorter prefixes; otherwise drop one letter from either string.",
vname="2D DP table",
spec=r'''
Return the length of the longest **common subsequence** of `text1` and `text2` (0 if none).

**Example**
```
"abcde", "ace" → 3,   "abc", "abc" → 3,   "abc", "def" → 0
```

**Constraints**
* `1 <= text1.length, text2.length <= 1000`
''',
approach=r'''
**Prefix DP.** `dp[i][j]` is the LCS of `text1[..i)` and `text2[..j)`. Equal last letters: `dp[i-1][j-1] + 1`; otherwise
`max(dp[i-1][j], dp[i][j-1])`.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the table.
''',
tc="n2", sc="n2",
java=r'''
public class LongestCommonSubsequence {

    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = text1.charAt(i - 1) == text2.charAt(j - 1)
                        ? dp[i - 1][j - 1] + 1
                        : Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[m][n];
    }
}
''',
test=r'''
class LongestCommonSubsequenceTest {

    private final LongestCommonSubsequence solution = new LongestCommonSubsequence();

    @ParameterizedTest
    @CsvSource({"abcde,ace,3", "abc,abc,3", "abc,def,0", "bsbininm,jmjkbkjkv,1"})
    void lengths(String a, String b, int expected) {
        assertEquals(expected, solution.longestCommonSubsequence(a, b));
    }
}
''',
trace=r'''
function run(a, b) {
  const m = a.length, n = b.length, dp = [...Array(m + 1)].map(() => new Array(n + 1).fill(0));
  const g = () => [[''].concat(['∅', ...b])].concat(dp.map((r, i) => [i ? a[i - 1] : '∅'].concat(r)));
  for (let i = 1; i <= m; i++) for (let j = 1; j <= n; j++) {
    const eq = a[i - 1] === b[j - 1];
    dp[i][j] = eq ? dp[i - 1][j - 1] + 1 : Math.max(dp[i - 1][j], dp[i][j - 1]);
    A.step(eq ? `'${a[i - 1]}' = '${b[j - 1]}': extend the diagonal, ${dp[i][j]}.` : `'${a[i - 1]}' ≠ '${b[j - 1]}': take the better of above and left, ${dp[i][j]}.`, A.grid('dp', g(), { hl: { [`${i + 1},${j + 1}`]: eq ? 'ok' : 'cur', ...(eq ? { [`${i},${j}`]: 'sel' } : { [`${i},${j + 1}`]: 'sel', [`${i + 1},${j}`]: 'sel' }) } }));
  }
  A.step(`The LCS has length ${dp[m][n]}.`, A.text('Result', dp[m][n], 'ok'));
}
A.scenario('abcde vs ace', 'text1 = "abcde", text2 = "ace"', () => run('abcde', 'ace'));
'''),

P(num=516, slug="longest-palindromic-subsequence", title="Longest Palindromic Subsequence", diff="Medium", topic="Multidimensional DP", cls="LongestPalindromicSubsequence",
idea="Matching ends add 2 to the inner answer; otherwise drop one end.",
vname="Interval DP",
spec=r'''
Return the length of the longest **palindromic subsequence** of `s`.

**Example**
```
"bbbab" → 4 ("bbbb"),   "cbbd" → 2 ("bb")
```

**Constraints**
* `1 <= s.length <= 1000`
''',
approach=r'''
**Interval DP.** `dp[i][j]` for `s[i..j]`: `dp[i][i] = 1`; equal ends give `dp[i+1][j-1] + 2`; otherwise `max(dp[i+1][j], dp[i][j-1])`.
Fill `i` from right to left.

* Time: **O(n²)** — each interval once.
* Space: **O(n²)** — the table.
''',
tc="n2", sc="n2",
java=r'''
public class LongestPalindromicSubsequence {

    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        int[][] dp = new int[n][n];
        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                dp[i][j] = s.charAt(i) == s.charAt(j) ? dp[i + 1][j - 1] + 2 : Math.max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
        return dp[0][n - 1];
    }
}
''',
test=r'''
class LongestPalindromicSubsequenceTest {

    private final LongestPalindromicSubsequence solution = new LongestPalindromicSubsequence();

    @ParameterizedTest
    @CsvSource({"bbbab,4", "cbbd,2", "a,1", "character,5"})
    void lengths(String s, int expected) {
        assertEquals(expected, solution.longestPalindromeSubseq(s));
    }
}
''',
trace=r'''
function run(s) {
  const n = s.length, dp = [...Array(n)].map(() => new Array(n).fill(''));
  const g = () => [[''].concat([...s])].concat(dp.map((r, i) => [s[i]].concat(r)));
  for (let i = n - 1; i >= 0; i--) {
    dp[i][i] = 1;
    for (let j = i + 1; j < n; j++) dp[i][j] = s[i] === s[j] ? (dp[i + 1][j - 1] || 0) + 2 : Math.max(dp[i + 1][j], dp[i][j - 1]);
    A.step(`Row ${i}: intervals starting at '${s[i]}'. Equal ends add 2 to the inside; otherwise drop one end.`, A.grid('dp[i][j]', g(), { hl: Object.fromEntries(dp[i].map((v, j) => [`${i + 1},${j + 1}`, v === '' ? '' : j === i ? 'sel' : s[i] === s[j] ? 'ok' : 'cur'])) }));
  }
  A.step(`The longest palindromic subsequence has length ${dp[0][n - 1]}.`, A.text('Result', dp[0][n - 1], 'ok'));
}
A.scenario('bbbab', 's = "bbbab"', () => run('bbbab'));
'''),

P(num=647, slug="palindromic-substrings", title="Palindromic Substrings", diff="Medium", topic="Two Pointers", cls="PalindromicSubstrings",
idea="Expand around each of the 2n − 1 centres and count every successful expansion.",
vname="Expand around centres",
spec=r'''
Return how many substrings of `s` are palindromes (substrings at different positions count separately).

**Example**
```
"abc" → 3,   "aaa" → 6
```

**Constraints**
* `1 <= s.length <= 1000`
''',
approach=r'''
**Centres.** For each centre (a character or the gap between two), expand while the ends match; every step of the expansion is one more
palindrome.

* Time: **O(n²)** — each centre expands at most n/2 times.
* Space: **O(1)** — a few indices.
''',
tc="n2",
java=r'''
public class PalindromicSubstrings {

    public int countSubstrings(String s) {
        int count = 0;
        for (int c = 0; c < 2 * s.length() - 1; c++) {
            int l = c / 2, r = l + c % 2;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                count++;
                l--;
                r++;
            }
        }
        return count;
    }
}
''',
test=r'''
class PalindromicSubstringsTest {

    private final PalindromicSubstrings solution = new PalindromicSubstrings();

    @ParameterizedTest
    @CsvSource({"abc,3", "aaa,6", "a,1", "abba,6"})
    void counts(String s, int expected) {
        assertEquals(expected, solution.countSubstrings(s));
    }
}
''',
trace=r'''
function run(s) {
  let count = 0;
  for (let c = 0; c < 2 * s.length - 1; c++) {
    let l = c >> 1, r = l + (c & 1); const found = [];
    while (l >= 0 && r < s.length && s[l] === s[r]) { count++; found.push(s.slice(l, r + 1)); l--; r++; }
    A.step(`Centre ${c & 1 ? `between ${c >> 1} and ${(c >> 1) + 1}` : `at ${c >> 1}`}: ${found.length ? found.map(x => `"${x}"`).join(', ') : 'no palindrome'}. Total ${count}.`, A.chars('s', s, { range: found.length ? [l + 1, r - 1] : undefined, hl: { [c >> 1]: 'cur', ...(c & 1 ? { [(c >> 1) + 1]: 'cur' } : {}) } }), A.vars({ count }));
  }
  A.step(`${count} palindromic substrings.`, A.text('Result', count, 'ok'));
}
A.scenario('abba', 's = "abba"', () => run('abba'));
'''),

P(num=438, slug="find-all-anagrams-in-a-string", title="Find All Anagrams in a String", diff="Medium", topic="Sliding Window", cls="FindAllAnagrams",
idea="Slide a window of length |p| and keep letter counts; a window is an anagram when every count matches.",
vname="Fixed sliding window with counts",
spec=r'''
Return the start indices of all substrings of `s` that are anagrams of `p`, in any order.

**Example**
```
s = "cbaebabacd", p = "abc" → [0,6]
s = "abab", p = "ab"        → [0,1,2]
```

**Constraints**
* `1 <= s.length, p.length <= 3 * 10^4`; lowercase letters.
''',
approach=r'''
**Counts + mismatch counter.** `need[c]` is `count_p(c) - count_window(c)`; `diff` is the number of letters with `need != 0`. Adding or
removing a letter changes one count and updates `diff` in O(1). A window with `diff == 0` is an anagram.

* Time: **O(n)** — each letter enters and leaves the window once.
* Space: **O(1)** — 26 counters.
''',
java=r'''
public class FindAllAnagrams {

    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> out = new ArrayList<>();
        if (p.length() > s.length()) return out;
        int[] need = new int[26];
        for (char c : p.toCharArray()) need[c - 'a']++;
        int diff = 0;
        for (int x : need) if (x != 0) diff++;
        for (int i = 0; i < s.length(); i++) {
            diff += change(need, s.charAt(i) - 'a', -1);
            if (i >= p.length()) diff += change(need, s.charAt(i - p.length()) - 'a', +1);
            if (i >= p.length() - 1 && diff == 0) out.add(i - p.length() + 1);
        }
        return out;
    }

    /** Applies delta to need[c] and returns how the number of non-zero entries changed. */
    private static int change(int[] need, int c, int delta) {
        int before = need[c] != 0 ? 1 : 0;
        need[c] += delta;
        return (need[c] != 0 ? 1 : 0) - before;
    }
}
''',
test=r'''
class FindAllAnagramsTest {

    private final FindAllAnagrams solution = new FindAllAnagrams();

    @Test
    void examples() {
        assertEquals(List.of(0, 6), solution.findAnagrams("cbaebabacd", "abc"));
        assertEquals(List.of(0, 1, 2), solution.findAnagrams("abab", "ab"));
        assertEquals(List.of(), solution.findAnagrams("a", "ab"));
    }
}
''',
trace=r'''
function run(s, p) {
  const k = p.length, out = [], cnt = {}, need = {}; [...p].forEach(c => (need[c] = (need[c] || 0) + 1));
  A.step(`Slide a window of ${k} letters over s, comparing its letter counts with those of "${p}".`, A.chars('s', s), A.map('counts in p', need));
  for (let i = 0; i < s.length; i++) {
    cnt[s[i]] = (cnt[s[i]] || 0) + 1;
    if (i >= k) { cnt[s[i - k]]--; if (!cnt[s[i - k]]) delete cnt[s[i - k]]; }
    if (i >= k - 1) {
      const ok = Object.keys(need).every(c => need[c] === cnt[c]) && Object.keys(cnt).every(c => cnt[c] === need[c]);
      if (ok) out.push(i - k + 1);
      A.step(`Window "${s.slice(i - k + 1, i + 1)}" ${ok ? 'has the same counts: an anagram' : 'does not match'}.`, A.chars('s', s, { range: [i - k + 1, i], hl: ok ? Object.fromEntries([...Array(k)].map((_, t) => [i - k + 1 + t, 'ok'])) : {} }), A.map('window counts', cnt), A.arr('starts', out));
    }
  }
}
A.scenario('abc', 's = "cbaebabacd", p = "abc"', () => run('cbaebabacd', 'abc'));
'''),
]
