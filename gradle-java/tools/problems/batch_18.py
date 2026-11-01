PROBLEMS = [
P(num=32, slug="longest-valid-parentheses", title="Longest Valid Parentheses", diff="Hard", topic="Stack", cls="LongestValidParentheses",
idea="Keep a stack of indices with a sentinel for the last unmatched ')'; each match measures a valid stretch.",
vname="Index stack with sentinel",
spec=r'''
Given a string of `'('` and `')'`, return the length of the longest **well-formed** (valid) parentheses substring.

**Example**
```
"(()" → 2,   ")()())" → 4,   "" → 0
```

**Constraints**
* `0 <= s.length <= 3 * 10^4`
''',
approach=r'''
**Index stack.** Push `-1` as a base. Push the index of each `'('`. For `')'`, pop: if the stack becomes empty this `')'` is unmatched, so
push its index as the new base; otherwise the valid stretch ends here and starts after the index now on top: `i - top`.

* Time: **O(n)** — each index is pushed and popped at most once.
* Space: **O(n)** — the stack.
''',
java=r'''
public class LongestValidParentheses {

    public int longestValidParentheses(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(-1);
        int best = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.isEmpty()) stack.push(i);
                else best = Math.max(best, i - stack.peek());
            }
        }
        return best;
    }
}
''',
test=r'''
class LongestValidParenthesesTest {

    private final LongestValidParentheses solution = new LongestValidParentheses();

    @ParameterizedTest
    @CsvSource({"'(()',2", "')()())',4", "'',0", "'()(()',2", "'()(())',6"})
    void lengths(String s, int expected) {
        assertEquals(expected, solution.longestValidParentheses(s));
    }
}
''',
trace=r'''
function run(s) {
  const st = [-1]; let best = 0, bs = 0;
  A.step('The stack holds indices of unmatched "(" above a base index: the position just before the current valid stretch.', A.chars('s', s), A.stack('stack (indices)', st));
  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') { st.push(i); A.step(`'(' at ${i}: push it.`, A.chars('s', s, { hl: { [i]: 'cur' } }), A.stack('stack (indices)', st)); continue; }
    st.pop();
    if (!st.length) { st.push(i); A.step(`')' at ${i} has no partner. It becomes the new base.`, A.chars('s', s, { hl: { [i]: 'bad' } }), A.stack('stack (indices)', st)); }
    else { const len = i - st[st.length - 1]; if (len > best) { best = len; bs = st[st.length - 1] + 1; } A.step(`')' at ${i} closes a pair. The valid stretch runs from ${st[st.length - 1] + 1} to ${i}: length ${len}.`, A.chars('s', s, { range: [st[st.length - 1] + 1, i], hl: { [i]: 'ok' } }), A.stack('stack (indices)', st), A.vars({ best })); }
  }
  A.step(`The longest valid substring has length ${best}.`, A.chars('s', s, best ? { hl: Object.fromEntries([...Array(best).keys()].map(t => [bs + t, 'ok'])) } : {}), A.text('Result', best, 'ok'));
}
A.scenario('Classic', 's = ")()())"', () => run(')()())'));
A.scenario('Nested', 's = "()(())"', () => run('()(())'));
'''),

P(num=84, slug="largest-rectangle-in-histogram", title="Largest Rectangle in Histogram", diff="Hard", topic="Stack", cls="LargestRectangleHistogram",
idea="A monotonic stack of increasing bars; when a shorter bar arrives, each popped bar's widest rectangle is known.",
vname="Monotonic stack",
spec=r'''
Bars of width 1 have heights `heights[i]`. Return the area of the largest rectangle that fits inside the histogram.

**Example**
```
[2,1,5,6,2,3] → 10   (heights 5 and 6, width 2)
[2,4]         → 4
```

**Constraints**
* `1 <= heights.length <= 10^5`; `0 <= heights[i] <= 10^4`
''',
approach=r'''
**Increasing stack.** Push indices while heights increase. When `heights[i]` is lower than the top, pop the top bar: its rectangle can
extend right up to `i - 1` and left past the new top, so `width = i - newTop - 1`. A final height-0 sentinel flushes the stack.

* Time: **O(n)** — each bar is pushed and popped once.
* Space: **O(n)** — the stack.
''',
java=r'''
public class LargestRectangleHistogram {

    public int largestRectangleArea(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int best = 0, n = heights.length;
        for (int i = 0; i <= n; i++) {
            int h = i == n ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > h) {
                int height = heights[stack.pop()];
                int left = stack.isEmpty() ? -1 : stack.peek();
                best = Math.max(best, height * (i - left - 1));
            }
            stack.push(i);
        }
        return best;
    }
}
''',
test=r'''
class LargestRectangleHistogramTest {

    private final LargestRectangleHistogram solution = new LargestRectangleHistogram();

    @Test
    void examples() {
        assertEquals(10, solution.largestRectangleArea(new int[]{2, 1, 5, 6, 2, 3}));
        assertEquals(4, solution.largestRectangleArea(new int[]{2, 4}));
    }

    @Test
    void flat() {
        assertEquals(9, solution.largestRectangleArea(new int[]{3, 3, 3}));
    }
}
''',
trace=r'''
function run(h) {
  const H = Math.max(...h), st = []; let best = 0, rect = null;
  const pic = () => { const g = []; for (let y = H; y >= 1; y--) g.push(h.map(() => '')); return g; };
  const ghl = () => { const o = []; for (let y = H; y >= 1; y--) h.forEach((v, x) => { if (v >= y) o.push([`${H - y},${x}`, rect && x >= rect[0] && x <= rect[1] && y <= rect[2] ? 'water' : st.includes(x) ? 'bar,cur' : 'bar']); }); return o; };
  A.step('Keep a stack of bars in increasing height. A shorter bar ends the rectangles of the taller bars before it.', A.grid('histogram', pic(), { hl: ghl() }), A.stack('stack (indices)', st));
  for (let i = 0; i <= h.length; i++) {
    const cur = i === h.length ? 0 : h[i];
    while (st.length && h[st[st.length - 1]] > cur) {
      const top = st.pop(), left = st.length ? st[st.length - 1] : -1, area = h[top] * (i - left - 1);
      rect = [left + 1, i - 1, h[top]];
      if (area > best) best = area;
      A.step(`${i === h.length ? 'End of input' : `Bar ${i} (${cur}) is shorter`}: pop bar ${top} (height ${h[top]}). It spans ${left + 1}..${i - 1}, area ${h[top]} × ${i - left - 1} = ${area}. Best: ${best}.`, A.grid('histogram', pic(), { hl: ghl() }), A.stack('stack (indices)', st), A.vars({ best }));
    }
    rect = null;
    if (i < h.length) st.push(i);
  }
  A.step(`The largest rectangle has area ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', 'heights = [2,1,5,6,2,3]', () => run([2, 1, 5, 6, 2, 3]));
'''),

P(num=85, slug="maximal-rectangle", title="Maximal Rectangle", diff="Hard", topic="Stack", cls="MaximalRectangle",
idea="Each row turns the matrix above it into a histogram; reuse the largest-rectangle-in-histogram stack per row.",
vname="Row histograms + monotonic stack",
spec=r'''
Given a binary matrix of `'0'` and `'1'`, return the area of the largest rectangle containing only `'1'`s.

**Example**
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0   → 6
```

**Constraints**
* `1 <= rows, cols <= 200`
''',
approach=r'''
**Histogram per row.** `heights[c]` counts consecutive `'1'`s ending at the current row in column `c` (reset to 0 on `'0'`). After each
row, the largest rectangle in that histogram is the best rectangle whose bottom edge is this row.

* Time: **O(m·n)** — each row costs O(n) for the stack.
* Space: **O(n)** — the heights and the stack.
''',
tc="n2", sc="n",
java=r'''
public class MaximalRectangle {

    public int maximalRectangle(char[][] matrix) {
        int n = matrix[0].length, best = 0;
        int[] heights = new int[n];
        for (char[] row : matrix) {
            for (int c = 0; c < n; c++) heights[c] = row[c] == '1' ? heights[c] + 1 : 0;
            best = Math.max(best, largest(heights));
        }
        return best;
    }

    private static int largest(int[] h) {
        Deque<Integer> stack = new ArrayDeque<>();
        int best = 0;
        for (int i = 0; i <= h.length; i++) {
            int cur = i == h.length ? 0 : h[i];
            while (!stack.isEmpty() && h[stack.peek()] > cur) {
                int height = h[stack.pop()];
                int left = stack.isEmpty() ? -1 : stack.peek();
                best = Math.max(best, height * (i - left - 1));
            }
            stack.push(i);
        }
        return best;
    }
}
''',
test=r'''
class MaximalRectangleTest {

    private final MaximalRectangle solution = new MaximalRectangle();

    private static char[][] m(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    @Test
    void example() {
        assertEquals(6, solution.maximalRectangle(m("10100", "10111", "11111", "10010")));
    }

    @Test
    void small() {
        assertEquals(0, solution.maximalRectangle(m("0")));
        assertEquals(1, solution.maximalRectangle(m("1")));
    }
}
''',
trace=r'''
function run(rows) {
  const n = rows[0].length, h = new Array(n).fill(0); let best = 0;
  const largest = a => { let b = 0, span = null; for (let l = 0; l < a.length; l++) { let mn = Infinity; for (let r = l; r < a.length; r++) { mn = Math.min(mn, a[r]); if (mn * (r - l + 1) > b) { b = mn * (r - l + 1); span = [l, r, mn]; } } } return [b, span]; };
  rows.forEach((row, i) => {
    for (let c = 0; c < n; c++) h[c] = row[c] === '1' ? h[c] + 1 : 0;
    const [area, span] = largest(h); best = Math.max(best, area);
    const hl = {}; if (span) for (let x = i - span[2] + 1; x <= i; x++) for (let y = span[0]; y <= span[1]; y++) hl[`${x},${y}`] = 'ok';
    A.step(`Row ${i}: column heights of 1s ending here are [${h}]. The largest rectangle in this histogram has area ${area}. Best: ${best}.`, A.grid('matrix', rows.map(r => [...r]), { hl: { ...Object.fromEntries(rows.flatMap((r, x) => [...r].map((ch, y) => [`${x},${y}`, x > i ? 'dim' : ch === '1' ? 'sel' : '']))), ...hl } }), A.arr('heights', h));
  });
  A.step(`The largest all-ones rectangle has area ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', '4 × 5 matrix', () => run(['10100', '10111', '11111', '10010']));
'''),

P(num=62, slug="unique-paths", title="Unique Paths", diff="Medium", topic="Multidimensional DP", cls="UniquePaths",
idea="Paths into a cell = paths from above + paths from the left.",
vname="One rolling row",
spec=r'''
A robot on an `m × n` grid starts at the top-left and moves only right or down. How many unique paths reach the bottom-right corner?

**Example**
```
m = 3, n = 7 → 28,   m = 3, n = 2 → 3
```

**Constraints**
* `1 <= m, n <= 100`; the answer fits in 32 bits.
''',
approach=r'''
**Row DP.** Start with a row of 1s (one way along the top edge). For each next row, `dp[j] += dp[j - 1]`.

* Time: **O(m·n)** — each cell once.
* Space: **O(n)** — one row.
''',
tc="n2", sc="n",
java=r'''
public class UniquePaths {

    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) dp[j] += dp[j - 1];
        }
        return dp[n - 1];
    }
}
''',
test=r'''
class UniquePathsTest {

    private final UniquePaths solution = new UniquePaths();

    @ParameterizedTest
    @CsvSource({"3,7,28", "3,2,3", "1,1,1", "10,10,48620"})
    void counts(int m, int n, int expected) {
        assertEquals(expected, solution.uniquePaths(m, n));
    }
}
''',
trace=r'''
function run(m, n) {
  const g = [...Array(m)].map(() => new Array(n).fill(''));
  for (let i = 0; i < m; i++) for (let j = 0; j < n; j++) {
    g[i][j] = i === 0 || j === 0 ? 1 : g[i - 1][j] + g[i][j - 1];
    A.step(i === 0 || j === 0 ? `(${i},${j}) is on the top or left edge: only 1 way.` : `(${i},${j}) = ${g[i - 1][j]} from above + ${g[i][j - 1]} from the left = ${g[i][j]}.`, A.grid('paths', g, { hl: { [`${i},${j}`]: 'cur', ...(i && j ? { [`${i - 1},${j}`]: 'sel', [`${i},${j - 1}`]: 'sel' } : {}) } }));
  }
  A.step(`${g[m - 1][n - 1]} unique paths.`, A.text('Result', g[m - 1][n - 1], 'ok'));
}
A.scenario('3 × 4', 'm = 3, n = 4', () => run(3, 4));
''',
variants=[dict(
name="Combinatorics",
idea="Every path is a sequence of (m−1) downs and (n−1) rights: choose where the downs go.",
approach=r'''
**Binomial coefficient.** The answer is `C(m + n - 2, m - 1)`; compute it incrementally with `long` to avoid overflow.

* Time: **O(min(m, n))** — one multiplication per step.
* Space: **O(1)** — one long.
''',
tc="n",
java=r'''
public class UniquePaths {

    public int uniquePaths(int m, int n) {
        long result = 1;
        int k = Math.min(m, n) - 1, total = m + n - 2;
        for (int i = 1; i <= k; i++) {
            result = result * (total - k + i) / i;
        }
        return (int) result;
    }
}
''',
trace=r'''
function run(m, n) {
  const k = Math.min(m, n) - 1, total = m + n - 2; let r = 1;
  A.step(`A path is ${m - 1} downs and ${n - 1} rights in some order: choose ${k} positions out of ${total}.`, A.vars({ total, k }));
  for (let i = 1; i <= k; i++) { r = r * (total - k + i) / i; A.step(`Multiply by ${total - k + i} and divide by ${i}: ${r}.`, A.vars({ result: r })); }
  A.step(`C(${total}, ${k}) = ${r}.`, A.text('Result', r, 'ok'));
}
A.scenario('3 × 7', 'm = 3, n = 7', () => run(3, 7));
''')]),

P(num=91, slug="decode-ways", title="Decode Ways", diff="Medium", topic="1D DP", cls="DecodeWays",
idea="ways(i) = ways(i−1) if the last digit is 1–9, plus ways(i−2) if the last two digits form 10–26.",
vname="Two rolling variables",
spec=r'''
Letters map to numbers `A=1 … Z=26`. Given a digit string `s`, return how many ways it can be decoded. `"06"` is not valid (no leading zeros).

**Example**
```
"12" → 2 ("AB", "L"),   "226" → 3,   "06" → 0
```

**Constraints**
* `1 <= s.length <= 100`; digits only.
''',
approach=r'''
**Fibonacci-like DP.** `cur = (one-digit valid ? prev1 : 0) + (two-digit 10..26 ? prev2 : 0)`, shifting the two previous counts forward.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two counts.
''',
java=r'''
public class DecodeWays {

    public int numDecodings(String s) {
        int prev2 = 1, prev1 = s.charAt(0) == '0' ? 0 : 1;
        for (int i = 1; i < s.length(); i++) {
            int cur = 0;
            if (s.charAt(i) != '0') cur += prev1;
            int two = (s.charAt(i - 1) - '0') * 10 + (s.charAt(i) - '0');
            if (two >= 10 && two <= 26) cur += prev2;
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}
''',
test=r'''
class DecodeWaysTest {

    private final DecodeWays solution = new DecodeWays();

    @ParameterizedTest
    @CsvSource({"12,2", "226,3", "06,0", "10,1", "2101,1", "11106,2"})
    void counts(String s, int expected) {
        assertEquals(expected, solution.numDecodings(s));
    }
}
''',
trace=r'''
function run(s) {
  const ways = [1, s[0] === '0' ? 0 : 1];
  A.step(`ways[i] counts decodings of the first i digits. ways[0] = 1 (empty), ways[1] = ${ways[1]}.`, A.chars('s', s), A.arr('ways', ways));
  for (let i = 1; i < s.length; i++) {
    let cur = 0; const one = s[i] !== '0', two = +s.slice(i - 1, i + 1);
    if (one) cur += ways[i];
    if (two >= 10 && two <= 26) cur += ways[i - 1];
    ways.push(cur);
    A.step(`Digit ${s[i]}: ${one ? `alone it is a letter (+${ways[i]})` : 'a lone 0 is not a letter'}; "${s.slice(i - 1, i + 1)}" ${two >= 10 && two <= 26 ? `is a letter too (+${ways[i - 1]})` : 'is not a letter'}. Total ${cur}.`, A.chars('s', s, { hl: { [i]: 'cur', [i - 1]: two >= 10 && two <= 26 ? 'sel' : '' } }), A.arr('ways', ways, { hl: { [i + 1]: 'ok' } }));
  }
  A.step(`${ways[s.length]} ways.`, A.text('Result', ways[s.length], 'ok'));
}
A.scenario('226', 's = "226"', () => run('226'));
A.scenario('With zeros', 's = "11106"', () => run('11106'));
'''),

P(num=96, slug="unique-binary-search-trees", title="Unique Binary Search Trees", diff="Medium", topic="1D DP", cls="UniqueBSTs",
idea="Choosing root r splits 1..n into r−1 left values and n−r right values: G(n) = Σ G(r−1)·G(n−r) (Catalan numbers).",
vname="Catalan DP",
spec=r'''
Return the number of structurally unique BSTs that store exactly the values `1..n`.

**Example**
```
n = 3 → 5,   n = 1 → 1
```

**Constraints**
* `1 <= n <= 19`
''',
approach=r'''
**DP over sizes.** `G(0) = G(1) = 1`. For each size `k`, sum over every root `r`: the left subtree holds `r - 1` values and the right
`k - r`, and any left shape combines with any right shape.

* Time: **O(n²)** — n sizes × up to n roots.
* Space: **O(n)** — the G array.
''',
tc="n2", sc="n",
java=r'''
public class UniqueBSTs {

    public int numTrees(int n) {
        int[] g = new int[n + 1];
        g[0] = 1;
        for (int k = 1; k <= n; k++) {
            for (int root = 1; root <= k; root++) g[k] += g[root - 1] * g[k - root];
        }
        return g[n];
    }
}
''',
test=r'''
class UniqueBSTsTest {

    private final UniqueBSTs solution = new UniqueBSTs();

    @ParameterizedTest
    @CsvSource({"1,1", "2,2", "3,5", "4,14", "19,1767263190"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.numTrees(n));
    }
}
''',
trace=r'''
function run(n) {
  const g = [1];
  A.step('G[k] is the number of BST shapes with k values. An empty tree counts as 1 shape.', A.arr('G', g));
  for (let k = 1; k <= n; k++) {
    let sum = 0; const parts = [];
    for (let r = 1; r <= k; r++) { sum += g[r - 1] * g[k - r]; parts.push(`${g[r - 1]}×${g[k - r]}`); }
    g.push(sum);
    A.step(`k = ${k}: each root r leaves r − 1 values on the left and ${k} − r on the right. Sum: ${parts.join(' + ')} = ${sum}.`, A.arr('G', g, { hl: { [k]: 'ok' } }));
  }
  A.step(`${g[n]} unique BSTs.`, A.text('Result', g[n], 'ok'));
}
A.scenario('n = 4', 'values 1..4', () => run(4));
'''),

P(num=94, slug="binary-tree-inorder-traversal", title="Binary Tree Inorder Traversal", diff="Easy", topic="Binary Tree General", cls="InorderTraversal",
idea="Left subtree, node, right subtree; iteratively, a stack holds the path of nodes still waiting to be visited.",
vname="Iterative with a stack", helpers=["TreeNode"],
spec=r'''
Return the **inorder** traversal (left, node, right) of a binary tree's values.

**Example**
```
[1,null,2,3] → [1,3,2]
```

**Constraints**
* `0 <= n <= 100`

**Follow-up:** iteratively.
''',
approach=r'''
**Stack.** Push the left spine; pop a node, record it, move to its right child, and repeat.

* Time: **O(n)** — each node is pushed and popped once.
* Space: **O(h)** — the stack.
''',
tc="n", sc="n",
java=r'''
public class InorderTraversal {

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode cur = root;
        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            out.add(cur.val);
            cur = cur.right;
        }
        return out;
    }
}
''',
test=r'''
class InorderTraversalTest {

    private final InorderTraversal solution = new InorderTraversal();

    @Test
    void examples() {
        assertEquals(List.of(1, 3, 2), solution.inorderTraversal(TreeNode.of(1, null, 2, 3)));
        assertEquals(List.of(4, 2, 5, 1, 3), solution.inorderTraversal(TreeNode.of(1, 2, 3, 4, 5)));
        assertEquals(List.of(), solution.inorderTraversal(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), st = [], out = [], done = {}; let cur = root;
  while (cur || st.length) {
    while (cur) { st.push(cur); cur = cur.left; }
    cur = st.pop(); out.push(cur.val); done[cur.id] = 'ok';
    A.step(`Pop ${cur.val}: its left side is finished, so visit it. Then go to its right child.`, A.tree('tree', root, { hl: { ...done, ...Object.fromEntries(st.map(n => [n.id, 'sel'])), [cur.id]: 'cur' } }), A.stack('stack', st.map(n => n.val)), A.arr('inorder', out));
    cur = cur.right;
  }
}
A.scenario('Five nodes', '[1,2,3,4,5]', () => run([1, 2, 3, 4, 5]));
''',
variants=[dict(
name="Recursive",
idea="inorder(left), visit, inorder(right).",
approach=r'''
**Recursion.** The call stack plays the role of the explicit stack.

* Time: **O(n)** — one call per node.
* Space: **O(h)** — the recursion depth.
''',
tc="n", sc="n",
java=r'''
public class InorderTraversal {

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        walk(root, out);
        return out;
    }

    private void walk(TreeNode n, List<Integer> out) {
        if (n == null) return;
        walk(n.left, out);
        out.add(n.val);
        walk(n.right, out);
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), out = [], done = {};
  (function walk(n) { if (!n) return; walk(n.left); out.push(n.val); done[n.id] = 'ok'; A.step(`Left of ${n.val} done: visit ${n.val}.`, A.tree('tree', root, { hl: { ...done, [n.id]: 'cur' } }), A.arr('inorder', out)); walk(n.right); })(root);
}
A.scenario('Five nodes', '[1,2,3,4,5]', () => run([1, 2, 3, 4, 5]));
''')]),

P(num=144, slug="binary-tree-preorder-traversal", title="Binary Tree Preorder Traversal", diff="Easy", topic="Binary Tree General", cls="PreorderTraversal",
idea="Visit a node, then its left subtree, then its right; with a stack, push the right child first so the left pops first.",
vname="Iterative with a stack", helpers=["TreeNode"],
spec=r'''
Return the **preorder** traversal (node, left, right) of a binary tree's values.

**Example**
```
[1,null,2,3] → [1,2,3]
```

**Constraints**
* `0 <= n <= 100`
''',
approach=r'''
**Stack.** Pop a node, record it, push its right child then its left child.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the stack.
''',
tc="n", sc="n",
java=r'''
public class PreorderTraversal {

    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> stack = new ArrayDeque<>(List.of(root));
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            out.add(n.val);
            if (n.right != null) stack.push(n.right);
            if (n.left != null) stack.push(n.left);
        }
        return out;
    }
}
''',
test=r'''
class PreorderTraversalTest {

    private final PreorderTraversal solution = new PreorderTraversal();

    @Test
    void examples() {
        assertEquals(List.of(1, 2, 3), solution.preorderTraversal(TreeNode.of(1, null, 2, 3)));
        assertEquals(List.of(1, 2, 4, 5, 3), solution.preorderTraversal(TreeNode.of(1, 2, 3, 4, 5)));
        assertEquals(List.of(), solution.preorderTraversal(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), st = [root], out = [], done = {};
  while (st.length) {
    const n = st.pop(); out.push(n.val); done[n.id] = 'ok';
    if (n.right) st.push(n.right); if (n.left) st.push(n.left);
    A.step(`Pop and visit ${n.val}. Push its right child, then its left child, so the left is visited first.`, A.tree('tree', root, { hl: { ...done, [n.id]: 'cur' } }), A.stack('stack', st.map(x => x.val)), A.arr('preorder', out));
  }
}
A.scenario('Five nodes', '[1,2,3,4,5]', () => run([1, 2, 3, 4, 5]));
'''),

P(num=145, slug="binary-tree-postorder-traversal", title="Binary Tree Postorder Traversal", diff="Easy", topic="Binary Tree General", cls="PostorderTraversal",
idea="Postorder (left, right, node) is the reverse of a node, right, left traversal, which is easy with a stack.",
vname="Reversed modified preorder", helpers=["TreeNode"],
spec=r'''
Return the **postorder** traversal (left, right, node) of a binary tree's values.

**Example**
```
[1,null,2,3] → [3,2,1]
```

**Constraints**
* `0 <= n <= 100`
''',
approach=r'''
**Reverse trick.** Traverse node, right, left with a stack (push the left child before the right), adding each value to the **front**
of the output list. The result is left, right, node.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the stack (plus the output).
''',
tc="n", sc="n",
java=r'''
public class PostorderTraversal {

    public List<Integer> postorderTraversal(TreeNode root) {
        LinkedList<Integer> out = new LinkedList<>();
        if (root == null) return out;
        Deque<TreeNode> stack = new ArrayDeque<>(List.of(root));
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            out.addFirst(n.val);
            if (n.left != null) stack.push(n.left);
            if (n.right != null) stack.push(n.right);
        }
        return out;
    }
}
''',
test=r'''
class PostorderTraversalTest {

    private final PostorderTraversal solution = new PostorderTraversal();

    @Test
    void examples() {
        assertEquals(List.of(3, 2, 1), solution.postorderTraversal(TreeNode.of(1, null, 2, 3)));
        assertEquals(List.of(4, 5, 2, 3, 1), solution.postorderTraversal(TreeNode.of(1, 2, 3, 4, 5)));
        assertEquals(List.of(), solution.postorderTraversal(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), st = [root], out = [], done = {};
  A.step('Walk node → right → left, putting each value at the front of the output. Reversed, that is left → right → node.', A.tree('tree', root));
  while (st.length) {
    const n = st.pop(); out.unshift(n.val); done[n.id] = 'ok';
    if (n.left) st.push(n.left); if (n.right) st.push(n.right);
    A.step(`Pop ${n.val} and put it at the front of the output.`, A.tree('tree', root, { hl: { ...done, [n.id]: 'cur' } }), A.stack('stack', st.map(x => x.val)), A.arr('postorder', out, { hl: { 0: 'ok' } }));
  }
}
A.scenario('Five nodes', '[1,2,3,4,5]', () => run([1, 2, 3, 4, 5]));
'''),

P(num=110, slug="balanced-binary-tree", title="Balanced Binary Tree", diff="Easy", topic="Binary Tree General", cls="BalancedBinaryTree",
idea="Compute heights bottom-up and return −1 as soon as any node's subtrees differ by more than one.",
vname="Height with early exit", helpers=["TreeNode"],
spec=r'''
Return `true` if a binary tree is **height-balanced**: for every node, the heights of its two subtrees differ by at most 1.

**Example**
```
[3,9,20,null,null,15,7]     → true
[1,2,2,3,3,null,null,4,4]   → false
```

**Constraints**
* `0 <= n <= 5000`
''',
approach=r'''
**Post-order heights.** `height(n)` returns -1 if the subtree is unbalanced, otherwise its height. Each node checks both child heights
once, so the whole tree is checked in one pass.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class BalancedBinaryTree {

    public boolean isBalanced(TreeNode root) {
        return height(root) >= 0;
    }

    private int height(TreeNode n) {
        if (n == null) return 0;
        int l = height(n.left);
        if (l < 0) return -1;
        int r = height(n.right);
        if (r < 0 || Math.abs(l - r) > 1) return -1;
        return 1 + Math.max(l, r);
    }
}
''',
test=r'''
class BalancedBinaryTreeTest {

    private final BalancedBinaryTree solution = new BalancedBinaryTree();

    @Test
    void examples() {
        assertTrue(solution.isBalanced(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertFalse(solution.isBalanced(TreeNode.of(1, 2, 2, 3, 3, null, null, 4, 4)));
        assertTrue(solution.isBalanced(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {};
  const h = n => {
    if (!n) return 0;
    const l = h(n.left); if (l < 0) return -1;
    const r = h(n.right);
    if (r < 0) return -1;
    if (Math.abs(l - r) > 1) { hl[n.id] = 'bad'; A.step(`${n.val}: left height ${l}, right height ${r}. They differ by more than 1, so the tree is not balanced.`, A.tree('tree', root, { hl })); return -1; }
    hl[n.id] = 'ok';
    A.step(`${n.val}: left ${l}, right ${r}: balanced here, height ${1 + Math.max(l, r)}.`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'cur' } }));
    return 1 + Math.max(l, r);
  };
  const ok = h(root) >= 0;
  A.step(ok ? 'Every node is balanced.' : 'Unbalanced.', A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('Balanced', '[3,9,20,null,null,15,7]', () => run([3, 9, 20, null, null, 15, 7]));
A.scenario('Unbalanced', '[1,2,2,3,3,null,null,4,4]', () => run([1, 2, 2, 3, 3, null, null, 4, 4]));
'''),
]
