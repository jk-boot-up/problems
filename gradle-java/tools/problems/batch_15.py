DP_GRID = r'''
const dpGrid = (label, dp, hl, rowHead, colHead) => {
  const g = [[''].concat(colHead)].concat(dp.map((r, i) => [rowHead[i]].concat(r.map(v => (v === Infinity ? '∞' : v === null || v === undefined ? '' : v === true ? 'T' : v === false ? 'F' : v)))));
  const o = []; Object.entries(hl || {}).forEach(([k, c]) => { const [i, j] = k.split(',').map(Number); o.push([`${i + 1},${j + 1}`, c]); });
  for (let j = 0; j <= colHead.length; j++) o.push([`0,${j}`, 'dim']); for (let i = 1; i <= rowHead.length; i++) o.push([`${i},0`, 'dim']);
  return A.grid(label, g, { hl: o });
};
'''

PROBLEMS = [
P(num=300, slug="longest-increasing-subsequence", title="Longest Increasing Subsequence", diff="Medium", topic="1D DP", cls="LongestIncreasingSubsequence",
idea="Patience sorting: tails[k] is the smallest possible tail of an increasing subsequence of length k + 1.",
vname="Tails array + binary search",
spec=r'''
Return the length of the longest **strictly increasing subsequence** of `nums` (elements in order, not necessarily contiguous).

**Example**
```
[10,9,2,5,3,7,101,18] → 4   ([2,3,7,101])
[0,1,0,3,2,3]         → 4
[7,7,7,7]             → 1
```

**Constraints**
* `1 <= nums.length <= 2500`

**Follow-up:** O(n log n).
''',
approach=r'''
**Smallest tails.** Keep `tails` sorted: `tails[k]` is the smallest tail value of any increasing subsequence of length `k + 1`. For each
`x`, binary-search the first tail `>= x` and replace it with `x` (or append `x` if all tails are smaller). The length of `tails` is the
answer (its contents are not necessarily a real subsequence).

* Time: **O(n log n)** — one binary search per element.
* Space: **O(n)** — the tails array.
''',
tc="nlogn", sc="n",
java=r'''
public class LongestIncreasingSubsequence {

    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        for (int x : nums) {
            int lo = 0, hi = size;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (tails[mid] < x) lo = mid + 1; else hi = mid;
            }
            tails[lo] = x;
            if (lo == size) size++;
        }
        return size;
    }
}
''',
test=r'''
class LongestIncreasingSubsequenceTest {

    private final LongestIncreasingSubsequence solution = new LongestIncreasingSubsequence();

    @Test
    void examples() {
        assertEquals(4, solution.lengthOfLIS(new int[]{10, 9, 2, 5, 3, 7, 101, 18}));
        assertEquals(4, solution.lengthOfLIS(new int[]{0, 1, 0, 3, 2, 3}));
        assertEquals(1, solution.lengthOfLIS(new int[]{7, 7, 7, 7}));
    }

    @Test
    void decreasing() {
        assertEquals(1, solution.lengthOfLIS(new int[]{5, 4, 3, 2, 1}));
    }
}
''',
trace=r'''
function run(a) {
  const tails = [];
  A.step('tails[k] is the smallest value that can end an increasing subsequence of length k + 1. Smaller tails leave more room to grow.', A.arr('nums', a), A.arr('tails', tails));
  a.forEach((x, i) => {
    let lo = 0, hi = tails.length; while (lo < hi) { const mid = (lo + hi) >> 1; if (tails[mid] < x) lo = mid + 1; else hi = mid; }
    const append = lo === tails.length, old = tails[lo]; tails[lo] = x;
    A.step(append ? `${x} is larger than every tail, so it extends the longest subsequence to length ${tails.length}.` : `${x} replaces ${old} as the smallest tail for length ${lo + 1}.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.arr('tails', tails, { hl: { [lo]: append ? 'ok' : 'alt' } }));
  });
  A.step(`The tails array has length ${tails.length}, so the LIS has length ${tails.length}.`, A.text('Result', tails.length, 'ok'));
}
A.scenario('Classic', 'nums = [10,9,2,5,3,7,101,18]', () => run([10, 9, 2, 5, 3, 7, 101, 18]));
A.scenario('Replacements matter', 'nums = [0,8,4,12,2,10,6,14]', () => run([0, 8, 4, 12, 2, 10, 6, 14]));
''',
variants=[dict(
name="Quadratic DP",
idea="len[i] = 1 + the longest len[j] over earlier j with nums[j] < nums[i].",
approach=r'''
**O(n²) DP.** `len[i]` is the LIS ending at `i`: `1 + max(len[j])` for `j < i` with `nums[j] < nums[i]`.

* Time: **O(n²)** — every pair (j, i) is compared.
* Space: **O(n)** — the len array.
''',
tc="n2", sc="n",
java=r'''
public class LongestIncreasingSubsequence {

    public int lengthOfLIS(int[] nums) {
        int n = nums.length, best = 0;
        int[] len = new int[n];
        for (int i = 0; i < n; i++) {
            len[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) len[i] = Math.max(len[i], len[j] + 1);
            }
            best = Math.max(best, len[i]);
        }
        return best;
    }
}
''',
trace=r'''
function run(a) {
  const len = [];
  a.forEach((x, i) => {
    let b = 1, from = -1; for (let j = 0; j < i; j++) if (a[j] < x && len[j] + 1 > b) { b = len[j] + 1; from = j; }
    len.push(b);
    A.step(from >= 0 ? `len[${i}]: the best earlier smaller value is ${a[from]} (len ${len[from]}), so ${b}.` : `len[${i}]: no earlier value is smaller, so 1.`, A.arr('nums', a, { hl: { [i]: 'cur', ...(from >= 0 ? { [from]: 'sel' } : {}) } }), A.arr('len', len, { hl: { [i]: 'ok' } }));
  });
  A.step(`The answer is ${Math.max(...len)}.`, A.text('Result', Math.max(...len), 'ok'));
}
A.scenario('Classic', 'nums = [10,9,2,5,3,7,101,18]', () => run([10, 9, 2, 5, 3, 7, 101, 18]));
''')]),

P(num=120, slug="triangle", title="Triangle", diff="Medium", topic="Multidimensional DP", cls="Triangle",
idea="Work from the bottom row up: each cell adds the cheaper of the two cells below it.",
vname="Bottom-up with one row",
spec=r'''
Given a `triangle` of numbers, return the minimum path sum from top to bottom. From row `i`, index `j`, you may move to index `j` or
`j + 1` of the next row.

**Example**
```
   2
  3 4
 6 5 7
4 1 8 3
Output: 11   (2 + 3 + 5 + 1)
```

**Constraints**
* `1 <= triangle.length <= 200`

**Follow-up:** O(n) extra space, n = number of rows.
''',
approach=r'''
**Bottom-up.** Copy the last row into `best`. For each row going up, `best[j] = row[j] + min(best[j], best[j + 1])`. Then `best[0]` is the answer.

* Time: **O(n²)** — every cell is processed once.
* Space: **O(n)** — one row of partial sums.
''',
tc="n2", sc="n",
java=r'''
public class Triangle {

    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[] best = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            List<Integer> row = triangle.get(i);
            for (int j = 0; j <= i; j++) {
                best[j] = row.get(j) + Math.min(best[j], best[j + 1]);
            }
        }
        return best[0];
    }
}
''',
test=r'''
class TriangleTest {

    private final Triangle solution = new Triangle();

    @Test
    void example() {
        assertEquals(11, solution.minimumTotal(List.of(List.of(2), List.of(3, 4), List.of(6, 5, 7), List.of(4, 1, 8, 3))));
    }

    @Test
    void single() {
        assertEquals(-10, solution.minimumTotal(List.of(List.of(-10))));
    }
}
''',
trace=r'''
function run(tri) {
  const n = tri.length, W = n, g = tri.map(r => r.concat(new Array(W - r.length).fill(''))), best = new Array(n + 1).fill(0);
  const view = (msg, i, j) => A.step(msg, A.grid('triangle', g, { hl: { ...(i >= 0 ? { [`${i},${j}`]: 'cur' } : {}), ...(i >= 0 && i + 1 < n ? { [`${i + 1},${j}`]: 'sel', [`${i + 1},${j + 1}`]: 'sel' } : {}) } }), A.arr('best (from below)', best.slice(0, n)));
  view('Work upward. Below the last row, every path costs 0.', -1, 0);
  for (let i = n - 1; i >= 0; i--) for (let j = 0; j <= i; j++) {
    const m = Math.min(best[j], best[j + 1]); best[j] = tri[i][j] + m; g[i][j] = `${tri[i][j]}→${best[j]}`;
    view(`Row ${i}, position ${j}: ${tri[i][j]} plus the cheaper of the two below (${m}) = ${best[j]}.`, i, j);
  }
  A.step(`The minimum path sum is ${best[0]}.`, A.text('Result', best[0], 'ok'));
}
A.scenario('Four rows', '[[2],[3,4],[6,5,7],[4,1,8,3]]', () => run([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]));
'''),

P(num=64, slug="minimum-path-sum", title="Minimum Path Sum", diff="Medium", topic="Multidimensional DP", cls="MinimumPathSum",
idea="Each cell's cheapest path comes from the cheaper of its top and left neighbours.",
vname="One rolling row",
spec=r'''
Given an `m × n` grid of non-negative numbers, find a path from the top-left to the bottom-right, moving only **right** or **down**,
that minimizes the sum of the numbers along it. Return that sum.

**Example**
```
[[1,3,1],
 [1,5,1],
 [4,2,1]]  → 7   (1 → 3 → 1 → 1 → 1)
```

**Constraints**
* `1 <= m, n <= 200`; `0 <= grid[i][j] <= 200`
''',
approach=r'''
**Row DP.** `dp[j]` holds the best sum to the current row's column `j`. Going left to right, `dp[j] = grid[i][j] + min(dp[j] (from above),
dp[j-1] (from the left))`, with edge cells having only one choice.

* Time: **O(m·n)** — each cell once.
* Space: **O(n)** — one row.
''',
tc="n2", sc="n",
java=r'''
public class MinimumPathSum {

    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] dp = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) dp[j] = grid[0][0];
                else if (i == 0) dp[j] = dp[j - 1] + grid[i][j];
                else if (j == 0) dp[j] = dp[j] + grid[i][j];
                else dp[j] = Math.min(dp[j], dp[j - 1]) + grid[i][j];
            }
        }
        return dp[n - 1];
    }
}
''',
test=r'''
class MinimumPathSumTest {

    private final MinimumPathSum solution = new MinimumPathSum();

    @Test
    void square() {
        assertEquals(7, solution.minPathSum(new int[][]{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}}));
    }

    @Test
    void wide() {
        assertEquals(12, solution.minPathSum(new int[][]{{1, 2, 3}, {4, 5, 6}}));
    }

    @Test
    void single() {
        assertEquals(5, solution.minPathSum(new int[][]{{5}}));
    }
}
''',
trace=r'''
function run(g) {
  const m = g.length, n = g[0].length, dp = new Array(n).fill('');
  A.step('Fill row by row. Each cell adds the cheaper of the path arriving from above and the path arriving from the left.', A.grid('grid', g), A.arr('dp (current row)', dp));
  for (let i = 0; i < m; i++) for (let j = 0; j < n; j++) {
    const up = i ? dp[j] : Infinity, left = j ? dp[j - 1] : Infinity;
    dp[j] = (i || j ? Math.min(up, left) : 0) + g[i][j];
    A.step(i || j ? `(${i},${j}): min(from above ${up === Infinity ? '—' : up}, from left ${left === Infinity ? '—' : left}) + ${g[i][j]} = ${dp[j]}.` : `Start at (0,0): ${dp[0]}.`, A.grid('grid', g, { hl: { [`${i},${j}`]: 'cur', ...(i ? { [`${i - 1},${j}`]: up <= left ? 'ok' : 'sel' } : {}), ...(j ? { [`${i},${j - 1}`]: left < up ? 'ok' : 'sel' } : {}) } }), A.arr('dp (current row)', dp, { hl: { [j]: 'ok' } }));
  }
  A.step(`The minimum path sum is ${dp[n - 1]}.`, A.text('Result', dp[n - 1], 'ok'));
}
A.scenario('3 × 3', '[[1,3,1],[1,5,1],[4,2,1]]', () => run([[1, 3, 1], [1, 5, 1], [4, 2, 1]]));
''',
variants=[dict(
name="Full DP table",
idea="dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) in a full m × n table.",
approach=r'''
**2D table.** Same recurrence, storing every cell's best sum (also lets you rebuild the path).

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the table.
''',
tc="n2", sc="n2",
java=r'''
public class MinimumPathSum {

    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int best = (i == 0 && j == 0) ? 0 : Integer.MAX_VALUE;
                if (i > 0) best = Math.min(best, dp[i - 1][j]);
                if (j > 0) best = Math.min(best, dp[i][j - 1]);
                dp[i][j] = best + grid[i][j];
            }
        }
        return dp[m - 1][n - 1];
    }
}
''',
trace=DP_GRID + r'''
function run(g) {
  const m = g.length, n = g[0].length, dp = g.map(r => r.map(() => null));
  for (let i = 0; i < m; i++) for (let j = 0; j < n; j++) {
    const best = Math.min(i ? dp[i - 1][j] : Infinity, j ? dp[i][j - 1] : Infinity);
    dp[i][j] = (i || j ? best : 0) + g[i][j];
    A.step(`dp[${i}][${j}] = ${dp[i][j]}.`, dpGrid('dp', dp, { [`${i},${j}`]: 'cur' }, g.map((_, r) => `r${r}`), g[0].map((_, c) => `c${c}`)));
  }
  A.step(`Answer: ${dp[m - 1][n - 1]}. The full table costs O(m·n) space.`, A.text('Result', dp[m - 1][n - 1], 'ok'));
}
A.scenario('3 × 3', '[[1,3,1],[1,5,1],[4,2,1]]', () => run([[1, 3, 1], [1, 5, 1], [4, 2, 1]]));
''')]),

P(num=63, slug="unique-paths-ii", title="Unique Paths II", diff="Medium", topic="Multidimensional DP", cls="UniquePathsII",
idea="Paths into a cell = paths from above + paths from the left, and an obstacle cell has zero paths.",
vname="One rolling row",
spec=r'''
A robot starts at the top-left of an `m × n` grid and moves only **right** or **down** to the bottom-right. Cells with `1` are
obstacles. Return the number of unique paths (it fits in 32 bits).

**Example**
```
[[0,0,0],
 [0,1,0],
 [0,0,0]] → 2
```

**Constraints**
* `1 <= m, n <= 100`
''',
approach=r'''
**Counting DP.** `dp[j]` is the number of ways into column `j` of the current row: `dp[j] = 0` on an obstacle, otherwise
`dp[j] += dp[j - 1]` (above is what is already in `dp[j]`, plus the left neighbour).

* Time: **O(m·n)** — each cell once.
* Space: **O(n)** — one row.
''',
tc="n2", sc="n",
java=r'''
public class UniquePathsII {

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int n = obstacleGrid[0].length;
        int[] dp = new int[n];
        dp[0] = 1;
        for (int[] row : obstacleGrid) {
            for (int j = 0; j < n; j++) {
                if (row[j] == 1) dp[j] = 0;
                else if (j > 0) dp[j] += dp[j - 1];
            }
        }
        return dp[n - 1];
    }
}
''',
test=r'''
class UniquePathsIITest {

    private final UniquePathsII solution = new UniquePathsII();

    @Test
    void centreObstacle() {
        assertEquals(2, solution.uniquePathsWithObstacles(new int[][]{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}));
    }

    @Test
    void blockedStart() {
        assertEquals(0, solution.uniquePathsWithObstacles(new int[][]{{1}}));
    }

    @Test
    void column() {
        assertEquals(1, solution.uniquePathsWithObstacles(new int[][]{{0, 1}, {0, 0}}));
    }
}
''',
trace=r'''
function run(g) {
  const m = g.length, n = g[0].length, ways = g.map(r => r.map(() => '')), dp = new Array(n).fill(0); dp[0] = 1;
  const view = (msg, i, j) => A.step(msg, A.grid('paths into each cell', ways, { hl: g.flatMap((r, x) => r.map((v, y) => [`${x},${y}`, v ? 'bad' : x === i && y === j ? 'cur' : ways[x][y] !== '' ? 'ok' : ''])) }));
  view('Red cells are obstacles. Each free cell counts the paths from above plus the paths from the left.', -1, -1);
  for (let i = 0; i < m; i++) for (let j = 0; j < n; j++) {
    if (g[i][j]) { dp[j] = 0; ways[i][j] = '✕'; view(`(${i},${j}) is an obstacle: 0 paths.`, i, j); continue; }
    if (j) dp[j] += dp[j - 1];
    ways[i][j] = dp[j];
    view(`(${i},${j}): ${dp[j]} path${dp[j] === 1 ? '' : 's'}.`, i, j);
  }
  A.step(`${dp[n - 1]} unique path${dp[n - 1] === 1 ? '' : 's'}.`, A.text('Result', dp[n - 1], 'ok'));
}
A.scenario('Centre obstacle', '[[0,0,0],[0,1,0],[0,0,0]]', () => run([[0, 0, 0], [0, 1, 0], [0, 0, 0]]));
A.scenario('Wall with a gap', '[[0,0,0,0],[1,1,0,1],[0,0,0,0]]', () => run([[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0]]));
'''),

P(num=5, slug="longest-palindromic-substring", title="Longest Palindromic Substring", diff="Medium", topic="Multidimensional DP", cls="LongestPalindromicSubstring",
idea="Every palindrome has a centre; grow outward from each of the 2n − 1 centres while the ends match.",
vname="Expand around centre",
spec=r'''
Return the longest **palindromic substring** of `s`.

**Example**
```
"babad" → "bab" (or "aba"),   "cbbd" → "bb"
```

**Constraints**
* `1 <= s.length <= 1000`; digits and English letters.
''',
approach=r'''
**Centres.** A palindrome is centred on a character (odd length) or between two characters (even length). For each of these `2n - 1`
centres, expand `l--, r++` while `s[l] == s[r]` and keep the longest.

* Time: **O(n²)** — each centre can expand up to n/2 times.
* Space: **O(1)** — a few indices.
''',
tc="n2",
java=r'''
public class LongestPalindromicSubstring {

    public String longestPalindrome(String s) {
        int bestStart = 0, bestLen = 0;
        for (int center = 0; center < 2 * s.length() - 1; center++) {
            int l = center / 2, r = l + center % 2;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                l--;
                r++;
            }
            if (r - l - 1 > bestLen) {
                bestLen = r - l - 1;
                bestStart = l + 1;
            }
        }
        return s.substring(bestStart, bestStart + bestLen);
    }
}
''',
test=r'''
class LongestPalindromicSubstringTest {

    private final LongestPalindromicSubstring solution = new LongestPalindromicSubstring();

    @Test
    void odd() {
        assertTrue(Set.of("bab", "aba").contains(solution.longestPalindrome("babad")));
    }

    @Test
    void even() {
        assertEquals("bb", solution.longestPalindrome("cbbd"));
    }

    @Test
    void whole() {
        assertEquals("racecar", solution.longestPalindrome("racecar"));
        assertEquals("a", solution.longestPalindrome("a"));
    }
}
''',
trace=r'''
function run(s) {
  let bs = 0, bl = 0;
  A.step(`There are ${2 * s.length - 1} centres: on each character and between each pair. Expand from each while the ends match.`, A.chars('s', s));
  for (let c = 0; c < 2 * s.length - 1; c++) {
    let l = c >> 1, r = l + (c & 1);
    while (l >= 0 && r < s.length && s[l] === s[r]) { l--; r++; }
    const len = r - l - 1, nb = len > bl;
    if (nb) { bl = len; bs = l + 1; }
    if (len > 1 || c % 3 === 0) A.step(`Centre ${c & 1 ? `between ${c >> 1} and ${(c >> 1) + 1}` : `at ${c >> 1}`}: it grows to "${s.slice(l + 1, r)}" (length ${len}).${nb ? ' New longest.' : ''}`, A.chars('s', s, { range: len ? [l + 1, r - 1] : undefined, hl: { [c >> 1]: 'cur', ...(c & 1 ? { [(c >> 1) + 1]: 'cur' } : {}) } }), A.vars({ longest: `"${s.substr(bs, bl)}"` }));
  }
  A.step(`The longest palindrome is "${s.substr(bs, bl)}".`, A.chars('s', s, { hl: Object.fromEntries([...Array(bl).keys()].map(t => [bs + t, 'ok'])) }), A.text('Result', s.substr(bs, bl), 'ok'));
}
A.scenario('Odd length', 's = "babad"', () => run('babad'));
A.scenario('Even length', 's = "abccbaz"', () => run('abccbaz'));
''',
variants=[dict(
name="DP table",
idea="s[i..j] is a palindrome if its ends match and s[i+1..j−1] is a palindrome.",
approach=r'''
**Interval DP.** `pal[i][j] = s[i] == s[j] && (j - i < 2 || pal[i+1][j-1])`. Fill by increasing length and remember the longest true cell.

* Time: **O(n²)** — every (i, j) pair once.
* Space: **O(n²)** — the boolean table.
''',
tc="n2", sc="n2",
java=r'''
public class LongestPalindromicSubstring {

    public String longestPalindrome(String s) {
        int n = s.length(), bestStart = 0, bestLen = 1;
        boolean[][] pal = new boolean[n][n];
        for (int len = 1; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                pal[i][j] = s.charAt(i) == s.charAt(j) && (len < 3 || pal[i + 1][j - 1]);
                if (pal[i][j] && len > bestLen) {
                    bestLen = len;
                    bestStart = i;
                }
            }
        }
        return s.substring(bestStart, bestStart + bestLen);
    }
}
''',
trace=DP_GRID + r'''
function run(s) {
  const n = s.length, pal = [...Array(n)].map(() => new Array(n).fill(null)); let bs = 0, bl = 1;
  for (let len = 1; len <= n; len++) {
    const hl = {};
    for (let i = 0; i + len - 1 < n; i++) { const j = i + len - 1; pal[i][j] = s[i] === s[j] && (len < 3 || pal[i + 1][j - 1]); hl[`${i},${j}`] = pal[i][j] ? 'ok' : 'bad'; if (pal[i][j] && len > bl) { bl = len; bs = i; } }
    A.step(`Length ${len}: s[i..j] is a palindrome when its ends match and the inside (one cell down-left) is a palindrome.`, dpGrid('pal[i][j]', pal, hl, [...s], [...s]), A.vars({ longest: `"${s.substr(bs, bl)}"` }));
  }
  A.step(`Longest: "${s.substr(bs, bl)}".`, A.text('Result', s.substr(bs, bl), 'ok'));
}
A.scenario('Odd length', 's = "babad"', () => run('babad'));
''')]),

P(num=97, slug="interleaving-string", title="Interleaving String", diff="Medium", topic="Multidimensional DP", cls="InterleavingString",
idea="ok[i][j]: the first i chars of s1 and j chars of s2 can form the first i + j chars of s3.",
vname="1D DP",
spec=r'''
Return `true` if `s3` is formed by **interleaving** `s1` and `s2`: splitting both into pieces and alternating them, keeping each
string's characters in order.

**Example**
```
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac" → true
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc" → false
s1 = "",      s2 = "",      s3 = ""           → true
```

**Constraints**
* `0 <= s1.length, s2.length <= 100`; `0 <= s3.length <= 200`

**Follow-up:** O(s2.length) extra memory.
''',
approach=r'''
**Grid of prefixes.** `ok[i][j]` is true when `s3[0..i+j)` interleaves `s1[0..i)` and `s2[0..j)`: either `ok[i-1][j]` and
`s1[i-1] == s3[i+j-1]`, or `ok[i][j-1]` and `s2[j-1] == s3[i+j-1]`. Keep one row of the grid.

* Time: **O(m·n)** — every cell once.
* Space: **O(n)** — one row (n = s2.length).
''',
tc="n2", sc="n",
java=r'''
public class InterleavingString {

    public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length(), n = s2.length();
        if (m + n != s3.length()) return false;
        boolean[] ok = new boolean[n + 1];
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 && j == 0) ok[j] = true;
                else {
                    boolean fromS1 = i > 0 && ok[j] && s1.charAt(i - 1) == s3.charAt(i + j - 1);
                    boolean fromS2 = j > 0 && ok[j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1);
                    ok[j] = fromS1 || fromS2;
                }
            }
        }
        return ok[n];
    }
}
''',
test=r'''
class InterleavingStringTest {

    private final InterleavingString solution = new InterleavingString();

    @Test
    void examples() {
        assertTrue(solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"));
        assertFalse(solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"));
        assertTrue(solution.isInterleave("", "", ""));
    }

    @Test
    void lengthMismatch() {
        assertFalse(solution.isInterleave("a", "b", "a"));
    }
}
''',
trace=DP_GRID + r'''
function run(s1, s2, s3) {
  const m = s1.length, n = s2.length, ok = [...Array(m + 1)].map(() => new Array(n + 1).fill(null));
  A.step(`Cell (i, j) asks: can the first ${'i'} letters of s1 and the first ${'j'} letters of s2 form the first i + j letters of s3 ("${s3}")?`, dpGrid('ok', ok, {}, ['∅', ...s1], ['∅', ...s2]));
  for (let i = 0; i <= m; i++) for (let j = 0; j <= n; j++) {
    if (!i && !j) { ok[0][0] = true; continue; }
    const a = i > 0 && ok[i - 1][j] && s1[i - 1] === s3[i + j - 1], b = j > 0 && ok[i][j - 1] && s2[j - 1] === s3[i + j - 1];
    ok[i][j] = a || b;
    if (ok[i][j] || (i + j) % 2 === 0) A.step(`(${i},${j}): s3[${i + j - 1}] = '${s3[i + j - 1]}'. ${a ? `It matches s1[${i - 1}] coming from above.` : b ? `It matches s2[${j - 1}] coming from the left.` : 'Neither direction works.'}`, dpGrid('ok', ok, { [`${i},${j}`]: ok[i][j] ? 'ok' : 'bad', ...(a ? { [`${i - 1},${j}`]: 'sel' } : {}), ...(b ? { [`${i},${j - 1}`]: 'sel' } : {}) }, ['∅', ...s1], ['∅', ...s2]));
  }
  A.step(`The bottom-right cell is ${ok[m][n]}.`, A.text('Result', String(ok[m][n]), ok[m][n] ? 'ok' : 'bad'));
}
A.scenario('Interleaves', 's1 = "aab", s2 = "db", s3 = "adabb"', () => run('aab', 'db', 'adabb'));
A.scenario('Does not interleave', 's1 = "ab", s2 = "cd", s3 = "adbc"', () => run('ab', 'cd', 'adbc'));
''',
variants=[dict(
name="2D DP table",
idea="The same recurrence, keeping the whole (m + 1) × (n + 1) table.",
approach=r'''
**Full grid.** Same transitions as the rolling version, but every cell is kept.

* Time: **O(m·n)** — every cell once.
* Space: **O(m·n)** — the table.
''',
tc="n2", sc="n2",
java=r'''
public class InterleavingString {

    public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length(), n = s2.length();
        if (m + n != s3.length()) return false;
        boolean[][] ok = new boolean[m + 1][n + 1];
        ok[0][0] = true;
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i > 0 && ok[i - 1][j] && s1.charAt(i - 1) == s3.charAt(i + j - 1)) ok[i][j] = true;
                if (j > 0 && ok[i][j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1)) ok[i][j] = true;
            }
        }
        return ok[m][n];
    }
}
''',
trace=DP_GRID + r'''
function run(s1, s2, s3) {
  const m = s1.length, n = s2.length, ok = [...Array(m + 1)].map(() => new Array(n + 1).fill(false)); ok[0][0] = true;
  for (let i = 0; i <= m; i++) { for (let j = 0; j <= n; j++) { if (i && ok[i - 1][j] && s1[i - 1] === s3[i + j - 1]) ok[i][j] = true; if (j && ok[i][j - 1] && s2[j - 1] === s3[i + j - 1]) ok[i][j] = true; } A.step(`Row ${i} filled.`, dpGrid('ok', ok, Object.fromEntries(ok[i].map((v, j) => [`${i},${j}`, v ? 'ok' : 'dim'])), ['∅', ...s1], ['∅', ...s2])); }
  A.step(`Answer: ${ok[m][n]}.`, A.text('Result', String(ok[m][n]), ok[m][n] ? 'ok' : 'bad'));
}
A.scenario('Interleaves', 's1 = "aab", s2 = "db", s3 = "adabb"', () => run('aab', 'db', 'adabb'));
''')]),

P(num=72, slug="edit-distance", title="Edit Distance", diff="Medium", topic="Multidimensional DP", cls="EditDistance",
idea="d[i][j] = edits to turn the first i letters of word1 into the first j letters of word2; each cell takes the cheapest last edit.",
vname="2D DP table",
spec=r'''
Return the minimum number of operations (insert a character, delete a character, replace a character) to convert `word1` into `word2`.

**Example**
```
horse → ros:  3  (replace h→r, delete r, delete e)
intention → execution:  5
```

**Constraints**
* `0 <= word1.length, word2.length <= 500`; lowercase letters.
''',
approach=r'''
**Levenshtein DP.** `d[i][0] = i`, `d[0][j] = j`. If `word1[i-1] == word2[j-1]`, `d[i][j] = d[i-1][j-1]`; otherwise
`1 + min(d[i-1][j-1] (replace), d[i-1][j] (delete), d[i][j-1] (insert))`.

* Time: **O(m·n)** — every cell once.
* Space: **O(m·n)** — the table (one row would also do).
''',
tc="n2", sc="n2",
java=r'''
public class EditDistance {

    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] d = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) d[i][0] = i;
        for (int j = 0; j <= n; j++) d[0][j] = j;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) d[i][j] = d[i - 1][j - 1];
                else d[i][j] = 1 + Math.min(d[i - 1][j - 1], Math.min(d[i - 1][j], d[i][j - 1]));
            }
        }
        return d[m][n];
    }
}
''',
test=r'''
class EditDistanceTest {

    private final EditDistance solution = new EditDistance();

    @ParameterizedTest
    @CsvSource({"horse,ros,3", "intention,execution,5", "'',abc,3", "abc,abc,0", "kitten,sitting,3"})
    void distances(String a, String b, int expected) {
        assertEquals(expected, solution.minDistance(a, b));
    }
}
''',
trace=DP_GRID + r'''
function run(a, b) {
  const m = a.length, n = b.length, d = [...Array(m + 1)].map((_, i) => [...Array(n + 1)].map((_, j) => (!i ? j : !j ? i : null)));
  A.step(`d[i][j] is the cost of turning the first i letters of "${a}" into the first j letters of "${b}". The first row and column are pure inserts or deletes.`, dpGrid('d', d, {}, ['∅', ...a], ['∅', ...b]));
  for (let i = 1; i <= m; i++) for (let j = 1; j <= n; j++) {
    if (a[i - 1] === b[j - 1]) { d[i][j] = d[i - 1][j - 1]; A.step(`'${a[i - 1]}' = '${b[j - 1]}': no edit needed, so copy the diagonal (${d[i][j]}).`, dpGrid('d', d, { [`${i},${j}`]: 'ok', [`${i - 1},${j - 1}`]: 'sel' }, ['∅', ...a], ['∅', ...b])); continue; }
    const rep = d[i - 1][j - 1], del = d[i - 1][j], ins = d[i][j - 1], best = Math.min(rep, del, ins);
    d[i][j] = 1 + best;
    const which = best === rep ? 'replace' : best === del ? 'delete' : 'insert', from = best === rep ? `${i - 1},${j - 1}` : best === del ? `${i - 1},${j}` : `${i},${j - 1}`;
    A.step(`'${a[i - 1]}' ≠ '${b[j - 1]}': 1 + min(replace ${rep}, delete ${del}, insert ${ins}) = ${d[i][j]}, via ${which}.`, dpGrid('d', d, { [`${i},${j}`]: 'cur', [from]: 'sel' }, ['∅', ...a], ['∅', ...b]));
  }
  A.step(`The edit distance is ${d[m][n]}.`, A.text('Result', d[m][n], 'ok'));
}
A.scenario('horse → ros', 'word1 = "horse", word2 = "ros"', () => run('horse', 'ros'));
'''),

P(num=123, slug="best-time-to-buy-and-sell-stock-iii", title="Best Time to Buy and Sell Stock III", diff="Hard", topic="Multidimensional DP", cls="BestTimeToBuyAndSellStockIII",
idea="Track four running best balances: after the 1st buy, 1st sell, 2nd buy and 2nd sell.",
vname="Four-state machine",
spec=r'''
`prices[i]` is the stock price on day `i`. You may complete **at most two** transactions (buy then sell), and must sell before buying
again. Return the maximum profit.

**Example**
```
[3,3,5,0,0,3,1,4] → 6   (buy 0 sell 3, buy 1 sell 4)
[1,2,3,4,5]       → 4
[7,6,4,3,1]       → 0
```

**Constraints**
* `1 <= prices.length <= 10^5`; `0 <= prices[i] <= 10^5`
''',
approach=r'''
**State machine.** `buy1` = best balance after the first buy (`max(buy1, -p)`), `sell1 = max(sell1, buy1 + p)`,
`buy2 = max(buy2, sell1 - p)`, `sell2 = max(sell2, buy2 + p)`. Each state builds on the one before it, on the same day, which is
harmless (it amounts to a zero-profit trade).

* Time: **O(n)** — one pass.
* Space: **O(1)** — four numbers.
''',
java=r'''
public class BestTimeToBuyAndSellStockIII {

    public int maxProfit(int[] prices) {
        int buy1 = Integer.MIN_VALUE, sell1 = 0, buy2 = Integer.MIN_VALUE, sell2 = 0;
        for (int p : prices) {
            buy1 = Math.max(buy1, -p);
            sell1 = Math.max(sell1, buy1 + p);
            buy2 = Math.max(buy2, sell1 - p);
            sell2 = Math.max(sell2, buy2 + p);
        }
        return sell2;
    }
}
''',
test=r'''
class BestTimeToBuyAndSellStockIIITest {

    private final BestTimeToBuyAndSellStockIII solution = new BestTimeToBuyAndSellStockIII();

    @Test
    void twoTrades() {
        assertEquals(6, solution.maxProfit(new int[]{3, 3, 5, 0, 0, 3, 1, 4}));
    }

    @Test
    void oneTradeEnough() {
        assertEquals(4, solution.maxProfit(new int[]{1, 2, 3, 4, 5}));
    }

    @Test
    void none() {
        assertEquals(0, solution.maxProfit(new int[]{7, 6, 4, 3, 1}));
        assertEquals(0, solution.maxProfit(new int[]{1}));
    }
}
''',
trace=r'''
function run(p) {
  let b1 = -Infinity, s1 = 0, b2 = -Infinity, s2 = 0;
  const f = v => (v === -Infinity ? '−∞' : v);
  A.step('Four running balances: after the first buy, the first sell, the second buy and the second sell. Each builds on the one before.', A.arr('prices', p), A.vars({ buy1: '−∞', sell1: 0, buy2: '−∞', sell2: 0 }));
  p.forEach((x, i) => {
    b1 = Math.max(b1, -x); s1 = Math.max(s1, b1 + x); b2 = Math.max(b2, s1 - x); s2 = Math.max(s2, b2 + x);
    A.step(`Day ${i}, price ${x}: buy1 = ${f(b1)}, sell1 = ${s1}, buy2 = ${f(b2)}, sell2 = ${s2}.`, A.arr('prices', p, { hl: { [i]: 'cur' } }), A.vars({ buy1: f(b1), sell1: s1, buy2: f(b2), sell2: s2 }));
  });
  A.step(`The best profit with at most two trades is ${s2}.`, A.text('Result', s2, 'ok'));
}
A.scenario('Two trades', 'prices = [3,3,5,0,0,3,1,4]', () => run([3, 3, 5, 0, 0, 3, 1, 4]));
'''),

P(num=188, slug="best-time-to-buy-and-sell-stock-iv", title="Best Time to Buy and Sell Stock IV", diff="Hard", topic="Multidimensional DP", cls="BestTimeToBuyAndSellStockIV",
idea="Generalize the two-trade state machine to k trades: buy[t] and sell[t] for t = 1..k.",
vname="k-state machine",
spec=r'''
You may complete **at most `k`** transactions (buy then sell, never holding two shares). Return the maximum profit.

**Example**
```
k = 2, prices = [2,4,1]         → 2
k = 2, prices = [3,2,6,5,0,3]   → 7
```

**Constraints**
* `1 <= k <= 100`; `1 <= prices.length <= 1000`
''',
approach=r'''
**Arrays of states.** For each price and each `t = 1..k`: `buy[t] = max(buy[t], sell[t-1] - p)` and `sell[t] = max(sell[t], buy[t] + p)`.
If `k >= n/2`, the limit never binds, so simply add every positive daily rise (as in Stock II).

* Time: **O(n·k)** — k state updates per day.
* Space: **O(k)** — two arrays of size k + 1.
''',
tc="n2", sc="n",
java=r'''
public class BestTimeToBuyAndSellStockIV {

    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if (k >= n / 2) {
            int profit = 0;
            for (int i = 1; i < n; i++) profit += Math.max(0, prices[i] - prices[i - 1]);
            return profit;
        }
        int[] buy = new int[k + 1], sell = new int[k + 1];
        Arrays.fill(buy, Integer.MIN_VALUE);
        for (int p : prices) {
            for (int t = 1; t <= k; t++) {
                buy[t] = Math.max(buy[t], sell[t - 1] - p);
                sell[t] = Math.max(sell[t], buy[t] + p);
            }
        }
        return sell[k];
    }
}
''',
test=r'''
class BestTimeToBuyAndSellStockIVTest {

    private final BestTimeToBuyAndSellStockIV solution = new BestTimeToBuyAndSellStockIV();

    @Test
    void examples() {
        assertEquals(2, solution.maxProfit(2, new int[]{2, 4, 1}));
        assertEquals(7, solution.maxProfit(2, new int[]{3, 2, 6, 5, 0, 3}));
    }

    @Test
    void limitBinds() {
        assertEquals(6, solution.maxProfit(1, new int[]{1, 3, 1, 7}));
        assertEquals(8, solution.maxProfit(2, new int[]{1, 3, 1, 7}));
    }

    @Test
    void largeK() {
        assertEquals(8, solution.maxProfit(100, new int[]{1, 3, 1, 7}));
    }
}
''',
trace=DP_GRID + r'''
function run(k, p) {
  const buy = new Array(k + 1).fill(-Infinity), sell = new Array(k + 1).fill(0);
  const f = v => (v === -Infinity ? '−∞' : v);
  const table = () => dpGrid('states', [buy.slice(1).map(f), sell.slice(1)], {}, ['buy', 'sell'], [...Array(k)].map((_, t) => `t${t + 1}`));
  A.step(`buy[t] is the best balance while holding during trade t; sell[t] is the best after completing t trades. k = ${k}.`, A.arr('prices', p), table());
  p.forEach((x, i) => {
    for (let t = 1; t <= k; t++) { buy[t] = Math.max(buy[t], sell[t - 1] - x); sell[t] = Math.max(sell[t], buy[t] + x); }
    A.step(`Day ${i}, price ${x}: update every trade's buy and sell states.`, A.arr('prices', p, { hl: { [i]: 'cur' } }), table());
  });
  A.step(`The best profit with at most ${k} trades is ${sell[k]}.`, A.text('Result', sell[k], 'ok'));
}
A.scenario('k = 2', 'prices = [3,2,6,5,0,3]', () => run(2, [3, 2, 6, 5, 0, 3]));
'''),

P(num=221, slug="maximal-square", title="Maximal Square", diff="Medium", topic="Multidimensional DP", cls="MaximalSquare",
idea="side[i][j] = 1 + min(top, left, top-left): a square is limited by its smallest neighbouring square.",
vname="DP on square sides",
spec=r'''
Given an `m × n` binary matrix of `'0'` and `'1'`, return the **area** of the largest square containing only `'1'`s.

**Example**
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0   → 4
```

**Constraints**
* `1 <= m, n <= 300`
''',
approach=r'''
**Side lengths.** `side[i][j]` is the largest all-ones square whose bottom-right corner is `(i, j)`. For a `'1'` it is
`1 + min(side[i-1][j], side[i][j-1], side[i-1][j-1])`; for a `'0'` it is 0. Track the maximum side and return its square.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the side table (one row would also do).
''',
tc="n2", sc="n2",
java=r'''
public class MaximalSquare {

    public int maximalSquare(char[][] matrix) {
        int m = matrix.length, n = matrix[0].length, best = 0;
        int[][] side = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (matrix[i - 1][j - 1] == '1') {
                    side[i][j] = 1 + Math.min(side[i - 1][j - 1], Math.min(side[i - 1][j], side[i][j - 1]));
                    best = Math.max(best, side[i][j]);
                }
            }
        }
        return best * best;
    }
}
''',
test=r'''
class MaximalSquareTest {

    private final MaximalSquare solution = new MaximalSquare();

    private static char[][] m(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    @Test
    void example() {
        assertEquals(4, solution.maximalSquare(m("10100", "10111", "11111", "10010")));
    }

    @Test
    void small() {
        assertEquals(1, solution.maximalSquare(m("01", "10")));
        assertEquals(0, solution.maximalSquare(m("0")));
    }

    @Test
    void full() {
        assertEquals(9, solution.maximalSquare(m("111", "111", "111")));
    }
}
''',
trace=r'''
function run(rows) {
  const m = rows.length, n = rows[0].length, side = [...Array(m)].map(() => new Array(n).fill(''));
  let best = 0, bi = 0, bj = 0;
  const view = (msg, i, j, extra = {}) => A.step(msg, A.grid('matrix', rows.map(r => [...r]), { hl: rows.flatMap((r, x) => [...r].map((c, y) => [`${x},${y}`, c === '1' ? 'sel' : 'dim'])).concat(Object.entries(extra)) }), A.grid('side of best square ending here', side, { hl: i >= 0 ? { [`${i},${j}`]: 'cur' } : {} }), A.vars({ bestSide: best }));
  view('For each 1, compute the side of the largest all-ones square whose bottom-right corner is that cell.', -1, -1);
  for (let i = 0; i < m; i++) for (let j = 0; j < n; j++) {
    if (rows[i][j] === '0') { side[i][j] = 0; continue; }
    const up = i ? +side[i - 1][j] : 0, left = j ? +side[i][j - 1] : 0, diag = i && j ? +side[i - 1][j - 1] : 0;
    side[i][j] = 1 + Math.min(up, left, diag);
    if (side[i][j] > best) { best = side[i][j]; bi = i; bj = j; }
    if (side[i][j] > 1 || (i + j) % 3 === 0) view(`(${i},${j}): 1 + min(above ${up}, left ${left}, diagonal ${diag}) = ${side[i][j]}.`, i, j);
  }
  const sq = {}; for (let x = bi - best + 1; x <= bi; x++) for (let y = bj - best + 1; y <= bj; y++) sq[`${x},${y}`] = 'ok';
  view(`The largest square has side ${best}, so its area is ${best * best}.`, bi, bj, sq);
  A.step(`Area: ${best * best}.`, A.text('Result', best * best, 'ok'));
}
A.scenario('Classic', '4 × 5 matrix', () => run(['10100', '10111', '11111', '10010']));
'''),
]
