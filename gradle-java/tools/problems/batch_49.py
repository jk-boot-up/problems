PROBLEMS = [
P(num=1572, slug="matrix-diagonal-sum", title="Matrix Diagonal Sum", diff="Easy", topic="Matrix", cls="MatrixDiagonalSum",
idea="Add mat[i][i] and mat[i][n−1−i] for each row; the centre cell of an odd matrix is counted once.",
vname="One pass over rows",
spec=r'''
Return the sum of a square matrix's primary diagonal and secondary diagonal, counting the shared centre element (odd `n`) only once.

**Example**
```
[[1,2,3],[4,5,6],[7,8,9]] → 25   (1 + 5 + 9 + 3 + 7)
[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]] → 8
```

**Constraints**
* `1 <= n <= 100`
''',
approach=r'''
**Both diagonals per row.** Row `i` contributes `mat[i][i]` and `mat[i][n-1-i]`; when those are the same cell (`i == n-1-i`), add it once.

* Time: **O(n)**.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class MatrixDiagonalSum {

    public int diagonalSum(int[][] mat) {
        int n = mat.length, sum = 0;
        for (int i = 0; i < n; i++) {
            sum += mat[i][i];
            if (i != n - 1 - i) sum += mat[i][n - 1 - i];
        }
        return sum;
    }
}
''',
test=r'''
class MatrixDiagonalSumTest {

    private final MatrixDiagonalSum solution = new MatrixDiagonalSum();

    @Test
    void examples() {
        assertEquals(25, solution.diagonalSum(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}));
        assertEquals(8, solution.diagonalSum(new int[][]{{1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}}));
        assertEquals(5, solution.diagonalSum(new int[][]{{5}}));
    }
}
''',
trace=r'''
function run(m) {
  const n = m.length, hl = {}; let sum = 0;
  A.step('Each row has one cell on each diagonal.', A.grid('matrix', m));
  for (let i = 0; i < n; i++) {
    const j = n - 1 - i; sum += m[i][i]; hl[`${i},${i}`] = 'ok';
    if (i !== j) { sum += m[i][j]; hl[`${i},${j}`] = 'alt'; }
    A.step(i === j ? `Row ${i}: the centre ${m[i][i]} is on both diagonals; count it once.` : `Row ${i}: add ${m[i][i]} and ${m[i][j]}.`, A.grid('matrix', m, { hl }), A.vars({ sum }));
  }
  A.step(`Diagonal sum: ${sum}.`, A.text('Result', sum, 'ok'));
}
A.scenario('Odd size', '3 × 3', () => run([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
'''),

P(num=1588, slug="sum-of-all-odd-length-subarrays", title="Sum of All Odd Length Subarrays", diff="Easy", topic="Math", cls="SumOddLengthSubarrays",
idea="Count how many odd-length subarrays contain each element and add value × count.",
vname="Contribution counting",
spec=r'''
Return the sum of all elements of all **odd-length** subarrays of `arr`.

**Example**
```
[1,4,2,5,3] → 58
[1,2]       → 3
[10,11,12]  → 66
```

**Constraints**
* `1 <= arr.length <= 100`
''',
approach=r'''
**Contribution.** Element `i` is in `(i + 1) · (n - i)` subarrays (choose a start at or before it and an end at or after it). Of these,
`((i + 1) · (n - i) + 1) / 2` have odd length. Add `arr[i]` times that count.

* Time: **O(n)**.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class SumOddLengthSubarrays {

    public int sumOddLengthSubarrays(int[] arr) {
        int n = arr.length, sum = 0;
        for (int i = 0; i < n; i++) sum += arr[i] * (((i + 1) * (n - i) + 1) / 2);
        return sum;
    }
}
''',
test=r'''
class SumOddLengthSubarraysTest {

    private final SumOddLengthSubarrays solution = new SumOddLengthSubarrays();

    @Test
    void examples() {
        assertEquals(58, solution.sumOddLengthSubarrays(new int[]{1, 4, 2, 5, 3}));
        assertEquals(3, solution.sumOddLengthSubarrays(new int[]{1, 2}));
        assertEquals(66, solution.sumOddLengthSubarrays(new int[]{10, 11, 12}));
        assertEquals(7, solution.sumOddLengthSubarrays(new int[]{7}));
    }
}
''',
trace=r'''
function run(arr) {
  const n = arr.length, counts = []; let sum = 0;
  A.step('Instead of listing subarrays, count how many odd-length ones contain each element.', A.arr('arr', arr));
  arr.forEach((v, i) => { const all = (i + 1) * (n - i), odd = Math.floor((all + 1) / 2); counts.push(odd); sum += v * odd; A.step(`Index ${i}: ${i + 1} starts × ${n - i} ends = ${all} subarrays, ${odd} of odd length. Adds ${v} × ${odd} = ${v * odd}.`, A.arr('arr', arr, { hl: { [i]: 'cur' } }), A.arr('odd count', counts), A.vars({ sum })); });
  A.step(`Total: ${sum}.`, A.text('Result', sum, 'ok'));
}
A.scenario('Example', '[1,4,2,5,3]', () => run([1, 4, 2, 5, 3]));
''',
variants=[dict(
name="Prefix sums over every odd length",
idea="Try every start and every odd length, reading each sum from prefix sums.",
approach=r'''
**Enumerate with prefix sums.** `prefix[j] - prefix[i]` is the sum of `arr[i..j-1]`. Loop over every start and every odd length.

* Time: **O(n²)**.
* Space: **O(n)** — the prefix array.
''',
tc="n2", sc="n",
java=r'''
public class SumOddLengthSubarrays {

    public int sumOddLengthSubarrays(int[] arr) {
        int n = arr.length, sum = 0;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + arr[i];
        for (int i = 0; i < n; i++)
            for (int len = 1; i + len <= n; len += 2) sum += prefix[i + len] - prefix[i];
        return sum;
    }
}
''',
trace=r'''
function run(arr) {
  const n = arr.length, p = [0]; arr.forEach(v => p.push(p[p.length - 1] + v)); let sum = 0;
  A.step('Prefix sums let each subarray sum be read in O(1).', A.arr('arr', arr), A.arr('prefix', p));
  for (let i = 0; i < n; i++) for (let len = 1; i + len <= n; len += 2) { const s = p[i + len] - p[i]; sum += s; A.step(`arr[${i}..${i + len - 1}] sums to ${s}.`, A.arr('arr', arr, { range: [i, i + len - 1] }), A.vars({ total: sum })); }
  A.step(`Total: ${sum}.`, A.text('Result', sum, 'ok'));
}
A.scenario('Small', '[10,11,12]', () => run([10, 11, 12]));
''')]),

P(num=1609, slug="even-odd-tree", title="Even Odd Tree", diff="Medium", topic="Binary Tree BFS", cls="EvenOddTree",
idea="Check each level during a BFS: parity of every value and strict direction of the sequence.",
vname="Level-order checks", helpers=["TreeNode"],
spec=r'''
A tree is **Even-Odd** if, with the root at level 0:

* on even levels, all values are **odd** and strictly increasing left to right;
* on odd levels, all values are **even** and strictly decreasing left to right.

Return whether the tree is Even-Odd.

**Example**
```
[1,10,4,3,null,7,9,12,8,6,null,null,2] → true
[5,4,2,3,3,7]                           → false
[5,9,1,3,5,7]                           → false
```

**Constraints**
* `1 <= n <= 10^5`
''',
approach=r'''
**BFS per level.** Walk each level left to right, remembering the previous value. On even levels require `val` odd and `val > prev`; on odd
levels require `val` even and `val < prev`. Fail fast on the first violation.

* Time: **O(n)**.
* Space: **O(w)** — the widest level.
''',
tc="n", sc="n",
java=r'''
public class EvenOddTree {

    public boolean isEvenOddTree(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        for (int level = 0; !queue.isEmpty(); level++) {
            boolean even = level % 2 == 0;
            long prev = even ? Long.MIN_VALUE : Long.MAX_VALUE;
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                if (even && (n.val % 2 == 0 || n.val <= prev)) return false;
                if (!even && (n.val % 2 == 1 || n.val >= prev)) return false;
                prev = n.val;
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
        }
        return true;
    }
}
''',
test=r'''
class EvenOddTreeTest {

    private final EvenOddTree solution = new EvenOddTree();

    @Test
    void examples() {
        assertTrue(solution.isEvenOddTree(TreeNode.of(1, 10, 4, 3, null, 7, 9, 12, 8, 6, null, null, 2)));
        assertFalse(solution.isEvenOddTree(TreeNode.of(5, 4, 2, 3, 3, 7)));
        assertFalse(solution.isEvenOddTree(TreeNode.of(5, 9, 1, 3, 5, 7)));
        assertTrue(solution.isEvenOddTree(TreeNode.of(1)));
        assertTrue(solution.isEvenOddTree(TreeNode.of(11, 8, 6, 1, 3, 9, 11, 30, 20, 18, 16, 12, 10, 4, 2, 17)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {}; let q = [root];
  A.step('Even levels: odd values, strictly increasing. Odd levels: even values, strictly decreasing.', A.tree('tree', root));
  for (let level = 0; q.length; level++) {
    const even = level % 2 === 0; let prev = even ? -Infinity : Infinity;
    for (const n of q) {
      const okParity = even ? n.val % 2 === 1 : n.val % 2 === 0, okOrder = even ? n.val > prev : n.val < prev;
      if (!okParity || !okOrder) { hl[n.id] = 'bad'; A.step(`Level ${level}: ${n.val} ${!okParity ? `should be ${even ? 'odd' : 'even'}` : `should be ${even ? 'greater' : 'smaller'} than ${prev}`}.`, A.tree('tree', root, { hl }), A.text('Result', 'false', 'bad')); return; }
      hl[n.id] = 'ok'; prev = n.val;
    }
    A.step(`Level ${level} [${q.map(n => n.val)}]: all ${even ? 'odd and increasing' : 'even and decreasing'}.`, A.tree('tree', root, { hl }));
    q = q.flatMap(n => [n.left, n.right].filter(Boolean));
  }
  A.step('Every level passes.', A.text('Result', 'true', 'ok'));
}
A.scenario('Valid', '[1,10,4,3,null,7,9,12,8,6,null,null,2]', () => run([1, 10, 4, 3, null, 7, 9, 12, 8, 6, null, null, 2]));
A.scenario('Bad order', '[5,4,2,3,3,7]', () => run([5, 4, 2, 3, 3, 7]));
'''),

P(num=1631, slug="path-with-minimum-effort", title="Path With Minimum Effort", diff="Medium", topic="Shortest Path", cls="PathWithMinimumEffort",
idea="Dijkstra where a path's cost is its largest single step instead of the sum of steps.",
vname="Dijkstra on the max edge",
spec=r'''
In a grid of heights, a route goes from the top-left to the bottom-right, moving up/down/left/right. Its **effort** is the largest absolute
height difference between two consecutive cells. Return the minimum effort.

**Example**
```
[[1,2,2],[3,8,2],[5,3,5]] → 2
[[1,2,3],[3,8,4],[5,3,5]] → 1
```

**Constraints**
* `1 <= rows, cols <= 100`, `1 <= heights <= 10^6`
''',
approach=r'''
**Minimax Dijkstra.** Extending a path can only keep or raise its maximum step, so the greedy order of Dijkstra still holds. Store
`effort[cell]`, pop the cell with the smallest effort, and relax each neighbour with `max(effort[cell], |height difference|)`.

* Time: **O(mn log(mn))**.
* Space: **O(mn)**.
''',
tc="nlogn", sc="n",
java=r'''
public class PathWithMinimumEffort {

    public int minimumEffortPath(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        int[][] effort = new int[m][n];
        for (int[] row : effort) Arrays.fill(row, Integer.MAX_VALUE);
        effort[0][0] = 0;
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        heap.add(new int[]{0, 0, 0});
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!heap.isEmpty()) {
            int[] top = heap.poll();
            int e = top[0], r = top[1], c = top[2];
            if (e > effort[r][c]) continue;
            if (r == m - 1 && c == n - 1) return e;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                int ne = Math.max(e, Math.abs(heights[nr][nc] - heights[r][c]));
                if (ne < effort[nr][nc]) {
                    effort[nr][nc] = ne;
                    heap.add(new int[]{ne, nr, nc});
                }
            }
        }
        return 0;
    }
}
''',
test=r'''
class PathWithMinimumEffortTest {

    private final PathWithMinimumEffort solution = new PathWithMinimumEffort();

    @Test
    void examples() {
        assertEquals(2, solution.minimumEffortPath(new int[][]{{1, 2, 2}, {3, 8, 2}, {5, 3, 5}}));
        assertEquals(1, solution.minimumEffortPath(new int[][]{{1, 2, 3}, {3, 8, 4}, {5, 3, 5}}));
        assertEquals(0, solution.minimumEffortPath(new int[][]{{1, 2, 1, 1, 1}, {1, 2, 1, 2, 1}, {1, 2, 1, 2, 1}, {1, 2, 1, 2, 1}, {1, 1, 1, 2, 1}}));
        assertEquals(0, solution.minimumEffortPath(new int[][]{{5}}));
    }
}
''',
trace=r'''
function run(h) {
  const m = h.length, n = h[0].length, eff = h.map(r => r.map(() => '∞')), done = {};
  eff[0][0] = 0;
  A.step('effort[cell] = the smallest possible largest step to reach it. Expand the cell with the smallest effort first.', A.grid('heights', h), A.grid('effort', eff, { hl: { '0,0': 'cur' } }));
  const heap = [[0, 0, 0]];
  while (heap.length) {
    heap.sort((a, b) => a[0] - b[0]); const [e, r, c] = heap.shift();
    if (done[`${r},${c}`]) continue; done[`${r},${c}`] = 'dim';
    if (r === m - 1 && c === n - 1) { A.step(`The bottom-right is reached with effort ${e}.`, A.grid('effort', eff, { hl: { ...done, [`${r},${c}`]: 'ok' } }), A.text('Result', e, 'ok')); return; }
    const upd = {};
    [[1, 0], [-1, 0], [0, 1], [0, -1]].forEach(([dr, dc]) => { const a = r + dr, b = c + dc; if (a < 0 || b < 0 || a >= m || b >= n || done[`${a},${b}`]) return; const ne = Math.max(e, Math.abs(h[a][b] - h[r][c])); if (eff[a][b] === '∞' || ne < eff[a][b]) { eff[a][b] = ne; heap.push([ne, a, b]); upd[`${a},${b}`] = 'ok'; } });
    A.step(`Settle (${r},${c}) with effort ${e}. ${Object.keys(upd).length ? `Improve ${Object.keys(upd).map(k => `(${k})`).join(', ')}.` : 'No neighbour improves.'}`, A.grid('effort', eff, { hl: { ...done, [`${r},${c}`]: 'cur', ...upd } }));
  }
}
A.scenario('Example', '3 × 3', () => run([[1, 2, 2], [3, 8, 2], [5, 3, 5]]));
'''),

P(num=1658, slug="minimum-operations-to-reduce-x-to-zero", title="Minimum Operations to Reduce X to Zero", diff="Medium", topic="Sliding Window", cls="MinOperationsReduceX",
idea="Removing from both ends leaves a middle block summing to total − x; find the longest such block.",
vname="Longest middle window",
spec=r'''
In one operation, remove the leftmost or rightmost element of `nums` and subtract it from `x`. Return the minimum number of operations to
make `x` exactly 0, or `-1`.

**Example**
```
nums = [1,1,4,2,3],    x = 5  → 2   (remove 3 and 2)
nums = [5,6,7,8,9],    x = 4  → -1
nums = [3,2,20,1,1,3], x = 10 → 5
```

**Constraints**
* `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^4`, `1 <= x <= 10^9`
''',
approach=r'''
**Flip the view.** Whatever is removed is a prefix plus a suffix; what is left is a contiguous block with sum `total - x`. Fewest removals
means the **longest** such block. All values are positive, so a sliding window finds it: grow the right end, shrink from the left while the
sum is too big, and record the length when the sum is exactly right.

* Time: **O(n)**.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class MinOperationsReduceX {

    public int minOperations(int[] nums, int x) {
        long total = 0;
        for (int v : nums) total += v;
        long need = total - x;
        if (need < 0) return -1;
        int best = -1, lo = 0;
        long sum = 0;
        for (int hi = 0; hi < nums.length; hi++) {
            sum += nums[hi];
            while (sum > need) sum -= nums[lo++];
            if (sum == need) best = Math.max(best, hi - lo + 1);
        }
        if (need == 0) best = Math.max(best, 0);
        return best < 0 ? -1 : nums.length - best;
    }
}
''',
test=r'''
class MinOperationsReduceXTest {

    private final MinOperationsReduceX solution = new MinOperationsReduceX();

    @Test
    void examples() {
        assertEquals(2, solution.minOperations(new int[]{1, 1, 4, 2, 3}, 5));
        assertEquals(-1, solution.minOperations(new int[]{5, 6, 7, 8, 9}, 4));
        assertEquals(5, solution.minOperations(new int[]{3, 2, 20, 1, 1, 3}, 10));
        assertEquals(-1, solution.minOperations(new int[]{1, 1}, 3));
        assertEquals(1, solution.minOperations(new int[]{5}, 5));
        assertEquals(3, solution.minOperations(new int[]{1, 2, 3}, 6));
    }
}
''',
trace=r'''
function run(nums, x) {
  const total = nums.reduce((a, b) => a + b, 0), need = total - x; let lo = 0, sum = 0, best = -1;
  A.step(`Removing from the ends leaves a middle block. It must sum to ${total} − ${x} = ${need}; make it as long as possible.`, A.arr('nums', nums), A.vars({ total, need }));
  for (let hi = 0; hi < nums.length; hi++) {
    sum += nums[hi]; let shrunk = 0;
    while (sum > need && lo <= hi) { sum -= nums[lo++]; shrunk++; }
    const hit = sum === need; if (hit) best = Math.max(best, hi - lo + 1);
    A.step(`Add ${nums[hi]}${shrunk ? `, drop ${shrunk} from the left` : ''}. Window sum ${sum}${hit ? ` = ${need}: keep ${hi - lo + 1}, remove ${nums.length - (hi - lo + 1)}` : ''}.`, A.arr('nums', nums, { range: [lo, hi], hl: hit ? Object.fromEntries(nums.map((_, i) => [i, i < lo || i > hi ? 'bad' : 'ok'])) : {} }), A.vars({ sum, longest: best }));
  }
  const ans = best < 0 ? -1 : nums.length - best;
  A.step(best < 0 ? 'No block has the right sum.' : `Longest block ${best}, so ${ans} removals.`, A.text('Result', ans, best < 0 ? 'bad' : 'ok'));
}
A.scenario('Both ends', '[3,2,20,1,1,3], x = 10', () => run([3, 2, 20, 1, 1, 3], 10));
A.scenario('Example', '[1,1,4,2,3], x = 5', () => run([1, 1, 4, 2, 3], 5));
'''),

P(num=1672, slug="richest-customer-wealth", title="Richest Customer Wealth", diff="Easy", topic="Matrix", cls="RichestCustomerWealth",
idea="Sum each row and keep the largest.",
vname="Row sums",
spec=r'''
`accounts[i][j]` is the money customer `i` has in bank `j`. Return the wealth (row total) of the richest customer.

**Example**
```
[[1,2,3],[3,2,1]]      → 6
[[1,5],[7,3],[3,5]]    → 10
```

**Constraints**
* `1 <= m, n <= 50`
''',
approach=r'''
**Row sums.** Add up each row and track the maximum.

* Time: **O(mn)**.
* Space: **O(1)**.
''',
tc="n2", sc="1",
java=r'''
public class RichestCustomerWealth {

    public int maximumWealth(int[][] accounts) {
        int best = 0;
        for (int[] customer : accounts) {
            int sum = 0;
            for (int money : customer) sum += money;
            best = Math.max(best, sum);
        }
        return best;
    }
}
''',
test=r'''
class RichestCustomerWealthTest {

    private final RichestCustomerWealth solution = new RichestCustomerWealth();

    @Test
    void examples() {
        assertEquals(6, solution.maximumWealth(new int[][]{{1, 2, 3}, {3, 2, 1}}));
        assertEquals(10, solution.maximumWealth(new int[][]{{1, 5}, {7, 3}, {3, 5}}));
        assertEquals(17, solution.maximumWealth(new int[][]{{2, 8, 7}, {7, 1, 3}, {1, 9, 5}}));
    }
}
''',
trace=r'''
function run(acc) {
  let best = 0; const sums = [];
  A.step('Each row is one customer. Add up their accounts.', A.grid('accounts', acc));
  acc.forEach((row, i) => { const s = row.reduce((a, b) => a + b, 0); sums.push(s); best = Math.max(best, s); A.step(`Customer ${i}: ${row.join(' + ')} = ${s}.`, A.grid('accounts', acc, { hl: Object.fromEntries(row.map((_, j) => [`${i},${j}`, 'cur'])) }), A.arr('wealth', sums), A.vars({ richest: best })); });
  A.step(`The richest customer has ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Example', '[[1,5],[7,3],[3,5]]', () => run([[1, 5], [7, 3], [3, 5]]));
'''),

P(num=1700, slug="number-of-students-unable-to-eat-lunch", title="Number of Students Unable to Eat Lunch", diff="Easy", topic="Queue", cls="StudentsUnableToEat",
idea="Queue order does not matter: the line only stalls when nobody left wants the sandwich on top.",
vname="Count preferences",
spec=r'''
Students in a queue each prefer circular (`0`) or square (`1`) sandwiches; sandwiches are in a stack (`sandwiches[0]` on top). The front
student takes the top sandwich if they like it, otherwise goes to the back of the queue. This stops when nobody in the queue wants the top
sandwich. Return how many students cannot eat.

**Example**
```
students = [1,1,0,0],     sandwiches = [0,1,0,1]     → 0
students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1] → 3
```

**Constraints**
* `1 <= n <= 100`
''',
approach=r'''
**Counts suffice.** Students rotate freely, so the top sandwich is eventually taken if anyone still wants that type. Count students per
preference. For each sandwich from the top, if its count is zero, everyone left is stuck; otherwise decrement it.

* Time: **O(n)**.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class StudentsUnableToEat {

    public int countStudents(int[] students, int[] sandwiches) {
        int[] want = new int[2];
        for (int s : students) want[s]++;
        for (int i = 0; i < sandwiches.length; i++) {
            if (want[sandwiches[i]] == 0) return sandwiches.length - i;
            want[sandwiches[i]]--;
        }
        return 0;
    }
}
''',
test=r'''
class StudentsUnableToEatTest {

    private final StudentsUnableToEat solution = new StudentsUnableToEat();

    @Test
    void examples() {
        assertEquals(0, solution.countStudents(new int[]{1, 1, 0, 0}, new int[]{0, 1, 0, 1}));
        assertEquals(3, solution.countStudents(new int[]{1, 1, 1, 0, 0, 1}, new int[]{1, 0, 0, 0, 1, 1}));
        assertEquals(1, solution.countStudents(new int[]{0}, new int[]{1}));
    }
}
''',
trace=r'''
function run(students, sandwiches) {
  const want = [0, 0]; students.forEach(s => want[s]++);
  A.step('The queue keeps rotating, so only the counts of each preference matter.', A.arr('students', students), A.arr('sandwiches (top first)', sandwiches), A.vars({ 'want 0': want[0], 'want 1': want[1] }));
  for (let i = 0; i < sandwiches.length; i++) {
    const t = sandwiches[i];
    if (!want[t]) { A.step(`Nobody left wants sandwich type ${t}. The remaining ${sandwiches.length - i} students cannot eat.`, A.arr('sandwiches (top first)', sandwiches, { hl: { [i]: 'bad' } }), A.text('Result', sandwiches.length - i, 'bad')); return; }
    want[t]--;
    A.step(`Someone wants type ${t}: they take it.`, A.arr('sandwiches (top first)', sandwiches, { hl: { ...Object.fromEntries(Array.from({ length: i }, (_, k) => [k, 'dim'])), [i]: 'ok' } }), A.vars({ 'want 0': want[0], 'want 1': want[1] }));
  }
  A.step('Everyone ate.', A.text('Result', 0, 'ok'));
}
A.scenario('Stuck', '[1,1,1,0,0,1] / [1,0,0,0,1,1]', () => run([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]));
'''),

P(num=1710, slug="maximum-units-on-a-truck", title="Maximum Units on a Truck", diff="Easy", topic="Greedy", cls="MaximumUnitsOnTruck",
idea="Load the boxes with the most units per box first.",
vname="Greedy by units per box",
spec=r'''
`boxTypes[i] = [count, unitsPerBox]`. A truck holds at most `truckSize` boxes. Return the maximum total units it can carry.

**Example**
```
boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4 → 8
boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10 → 91
```

**Constraints**
* `1 <= boxTypes.length <= 1000`, `1 <= count, unitsPerBox <= 1000`, `1 <= truckSize <= 10^6`
''',
approach=r'''
**Best boxes first.** Every box takes one slot, so a box with more units is always at least as good. Unit counts are at most 1000, so
bucket the box counts by units (no comparison sort needed) and load from 1000 down until the truck is full.

* Time: **O(n + U)** — `U = 1000`.
* Space: **O(U)**.
''',
tc="n", sc="1",
java=r'''
public class MaximumUnitsOnTruck {

    public int maximumUnits(int[][] boxTypes, int truckSize) {
        int[] boxesWithUnits = new int[1001];
        for (int[] b : boxTypes) boxesWithUnits[b[1]] += b[0];
        int units = 0;
        for (int u = 1000; u >= 1 && truckSize > 0; u--) {
            int take = Math.min(truckSize, boxesWithUnits[u]);
            units += take * u;
            truckSize -= take;
        }
        return units;
    }
}
''',
test=r'''
class MaximumUnitsOnTruckTest {

    private final MaximumUnitsOnTruck solution = new MaximumUnitsOnTruck();

    @Test
    void examples() {
        assertEquals(8, solution.maximumUnits(new int[][]{{1, 3}, {2, 2}, {3, 1}}, 4));
        assertEquals(91, solution.maximumUnits(new int[][]{{5, 10}, {2, 5}, {4, 7}, {3, 9}}, 10));
        assertEquals(10, solution.maximumUnits(new int[][]{{1, 3}, {2, 2}, {3, 1}}, 100));
    }
}
''',
trace=r'''
function run(boxes, size) {
  const sorted = boxes.slice().sort((a, b) => b[1] - a[1]); let left = size, units = 0;
  A.step(`Each box uses one of ${size} slots, so load the richest boxes first.`, A.arr('boxes [count, units]', sorted.map(b => `[${b}]`)), A.vars({ slots: left, units }));
  for (let i = 0; i < sorted.length && left > 0; i++) {
    const [c, u] = sorted[i], take = Math.min(c, left); left -= take; units += take * u;
    A.step(`Load ${take} of ${c} box${c > 1 ? 'es' : ''} with ${u} unit${u > 1 ? 's' : ''} each: +${take * u}.`, A.arr('boxes [count, units]', sorted.map(b => `[${b}]`), { hl: { [i]: take === c ? 'ok' : 'cur' } }), A.vars({ slots: left, units }));
  }
  A.step(`The truck carries ${units} units.`, A.text('Result', units, 'ok'));
}
A.scenario('Example', 'truckSize 10', () => run([[5, 10], [2, 5], [4, 7], [3, 9]], 10));
'''),

P(num=1721, slug="swapping-nodes-in-a-linked-list", title="Swapping Nodes in a Linked List", diff="Medium", topic="Linked List", cls="SwapNodesInList",
idea="Walk k − 1 steps to find the k-th node; a second pointer started at the head reaches the k-th from the end when the first one falls off.",
vname="Two pointers, swap values", helpers=["ListNode"],
spec=r'''
Swap the **values** of the `k`-th node from the beginning and the `k`-th node from the end (1-indexed) and return the head.

**Example**
```
head = [1,2,3,4,5], k = 2 → [1,4,3,2,5]
head = [7,9,6,6,7,8,3,0,9,5], k = 5 → [7,9,6,6,8,7,3,0,9,5]
```

**Constraints**
* `1 <= k <= n <= 10^5`
''',
approach=r'''
**Gap of k.** Move `fast` to the `k`-th node and remember it as `first`. Then move `fast` and `slow` (from the head) together until `fast`
is the last node; `slow` is now the `k`-th from the end. Swap the two values.

* Time: **O(n)** — one pass.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class SwapNodesInList {

    public ListNode swapNodes(ListNode head, int k) {
        ListNode fast = head;
        for (int i = 1; i < k; i++) fast = fast.next;
        ListNode first = fast, slow = head;
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        int t = first.val;
        first.val = slow.val;
        slow.val = t;
        return head;
    }
}
''',
test=r'''
class SwapNodesInListTest {

    private final SwapNodesInList solution = new SwapNodesInList();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 4, 3, 2, 5}, ListNode.toArray(solution.swapNodes(ListNode.of(1, 2, 3, 4, 5), 2)));
        assertArrayEquals(new int[]{7, 9, 6, 6, 8, 7, 3, 0, 9, 5}, ListNode.toArray(solution.swapNodes(ListNode.of(7, 9, 6, 6, 7, 8, 3, 0, 9, 5), 5)));
        assertArrayEquals(new int[]{1}, ListNode.toArray(solution.swapNodes(ListNode.of(1), 1)));
        assertArrayEquals(new int[]{2, 1}, ListNode.toArray(solution.swapNodes(ListNode.of(1, 2), 1)));
        assertArrayEquals(new int[]{1, 2, 3}, ListNode.toArray(solution.swapNodes(ListNode.of(1, 2, 3), 2)));
    }
}
''',
trace=r'''
function run(vals, k) {
  const a = vals.slice(), n = a.length; let fast = k - 1;
  A.step(`Move a pointer to the ${k}th node.`, A.list('list', a, { hl: { [fast]: 'cur' }, ptr: { [fast]: 'first' } }));
  let slow = 0;
  while (fast < n - 1) { fast++; slow++; A.step('Move fast and slow together; they stay k − 1 apart.', A.list('list', a, { hl: { [k - 1]: 'cur', [slow]: 'alt' }, ptr: { [k - 1]: 'first', [slow]: 'slow', ...(fast !== slow && fast !== k - 1 ? { [fast]: 'fast' } : {}) } })); }
  A.step(`fast is at the end, so slow is the ${k}th node from the end (value ${a[slow]}).`, A.list('list', a, { hl: { [k - 1]: 'cur', [slow]: 'alt' } }));
  [a[k - 1], a[slow]] = [a[slow], a[k - 1]];
  A.step(`Swap the values: [${a}].`, A.list('list', a, { hl: { [k - 1]: 'ok', [slow]: 'ok' } }));
}
A.scenario('Example', '[1,2,3,4,5], k = 2', () => run([1, 2, 3, 4, 5], 2));
'''),

P(num=1791, slug="find-center-of-star-graph", title="Find Center of Star Graph", diff="Easy", topic="Graph", cls="FindCenterOfStar",
idea="The centre is in every edge, so it is the endpoint the first two edges share.",
vname="Compare two edges",
spec=r'''
An undirected **star** graph has one centre connected to every other node, and no other edges. Given its edges, return the centre.

**Example**
```
[[1,2],[2,3],[4,2]]       → 2
[[1,2],[5,1],[1,3],[1,4]] → 1
```

**Constraints**
* `3 <= n <= 10^5`; the input is a valid star
''',
approach=r'''
**Shared endpoint.** Every edge touches the centre and no other node appears twice, so the node common to `edges[0]` and `edges[1]` is the
centre.

* Time: **O(1)**.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class FindCenterOfStar {

    public int findCenter(int[][] edges) {
        int a = edges[0][0], b = edges[0][1];
        return a == edges[1][0] || a == edges[1][1] ? a : b;
    }
}
''',
test=r'''
class FindCenterOfStarTest {

    private final FindCenterOfStar solution = new FindCenterOfStar();

    @Test
    void examples() {
        assertEquals(2, solution.findCenter(new int[][]{{1, 2}, {2, 3}, {4, 2}}));
        assertEquals(1, solution.findCenter(new int[][]{{1, 2}, {5, 1}, {1, 3}, {1, 4}}));
        assertEquals(3, solution.findCenter(new int[][]{{1, 3}, {3, 2}}));
    }
}
''',
trace=r'''
function run(edges) {
  const ids = [...new Set(edges.flat())], nodes = ids.map(id => ({ id }));
  A.step('In a star, the centre is an endpoint of every edge.', A.graph('graph', nodes, edges));
  const [a, b] = edges[0];
  A.step(`The first edge is ${a}–${b}: the centre is ${a} or ${b}.`, A.graph('graph', nodes, edges, { hl: { [a]: 'cur', [b]: 'cur' } }));
  const c = edges[1].includes(a) ? a : b;
  A.step(`The second edge is ${edges[1][0]}–${edges[1][1]}; it shares ${c}.`, A.graph('graph', nodes, edges, { hl: { [c]: 'ok' } }));
  A.step(`The centre is ${c}.`, A.text('Result', c, 'ok'));
}
A.scenario('Example', '[[1,2],[5,1],[1,3],[1,4]]', () => run([[1, 2], [5, 1], [1, 3], [1, 4]]));
'''),
]
