PROBLEMS = [
P(num=1304, slug="find-n-unique-integers-sum-up-to-zero", title="Find N Unique Integers Sum up to Zero", diff="Easy", topic="Math", cls="SumZero",
idea="Pair each k with −k; add a 0 when n is odd.",
vname="Symmetric pairs",
spec=r'''
Return any array of `n` **distinct** integers that add up to 0.

**Example**
```
n = 5 → [-2,-1,0,1,2]   (any valid answer is accepted)
n = 1 → [0]
```

**Constraints**
* `1 <= n <= 1000`
''',
approach=r'''
**Mirror pairs.** Put `k` and `-k` for `k = 1..n/2`; each pair cancels. If `n` is odd, the remaining slot holds `0`.

* Time: **O(n)**.
* Space: **O(1)** — besides the output.
''',
tc="n", sc="1",
java=r'''
public class SumZero {

    public int[] sumZero(int n) {
        int[] out = new int[n];
        for (int k = 1, i = 0; k <= n / 2; k++) {
            out[i++] = k;
            out[i++] = -k;
        }
        return out;
    }
}
''',
test=r'''
class SumZeroTest {

    private final SumZero solution = new SumZero();

    @ParameterizedTest
    @CsvSource({"1", "2", "3", "5", "10", "1000"})
    void valid(int n) {
        int[] a = solution.sumZero(n);
        assertEquals(n, a.length);
        assertEquals(0, Arrays.stream(a).sum());
        assertEquals(n, Arrays.stream(a).distinct().count());
    }
}
''',
trace=r'''
function run(n) {
  const out = new Array(n).fill('·');
  A.step(`Build ${n} distinct numbers that cancel out.`, A.arr('result', out));
  let i = 0;
  for (let k = 1; k <= Math.floor(n / 2); k++) { out[i++] = k; out[i++] = -k; A.step(`Add the pair ${k} and −${k}: they sum to 0.`, A.arr('result', out, { hl: { [i - 2]: 'ok', [i - 1]: 'ok' } }), A.vars({ sum: 0 })); }
  if (n % 2) { out[i] = 0; A.step('n is odd: the last slot is 0.', A.arr('result', out, { hl: { [i]: 'cur' } })); }
  A.step(`[${out}] sums to 0.`, A.text('Result', `[${out}]`, 'ok'));
}
A.scenario('Odd n', 'n = 5', () => run(5));
A.scenario('Even n', 'n = 4', () => run(4));
'''),

P(num=1305, slug="all-elements-in-two-binary-search-trees", title="All Elements in Two Binary Search Trees", diff="Medium", topic="Binary Search Tree", cls="AllElementsTwoBST",
idea="An in-order walk of each tree is sorted; merge the two sorted lists.",
vname="In-order lists, then merge", helpers=["TreeNode"],
spec=r'''
Return all values from two BSTs in one ascending list.

**Example**
```
root1 = [2,1,4], root2 = [1,0,3]   → [0,1,1,2,3,4]
root1 = [1,null,8], root2 = [8,1]  → [1,1,8,8]
```

**Constraints**
* `0 <= nodes per tree <= 5000`
''',
approach=r'''
**Two sorted runs.** An in-order traversal of a BST yields its values in order. Collect both (iteratively, with a stack) and merge them
like in merge sort.

* Time: **O(m + n)**.
* Space: **O(m + n)** — the lists.
''',
tc="n", sc="n",
java=r'''
public class AllElementsTwoBST {

    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> a = inorder(root1), b = inorder(root2), out = new ArrayList<>(a.size() + b.size());
        int i = 0, j = 0;
        while (i < a.size() || j < b.size()) {
            if (j == b.size() || (i < a.size() && a.get(i) <= b.get(j))) out.add(a.get(i++));
            else out.add(b.get(j++));
        }
        return out;
    }

    private List<Integer> inorder(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        for (TreeNode cur = root; cur != null || !stack.isEmpty(); ) {
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
class AllElementsTwoBSTTest {

    private final AllElementsTwoBST solution = new AllElementsTwoBST();

    @Test
    void examples() {
        assertEquals(List.of(0, 1, 1, 2, 3, 4), solution.getAllElements(TreeNode.of(2, 1, 4), TreeNode.of(1, 0, 3)));
        assertEquals(List.of(1, 1, 8, 8), solution.getAllElements(TreeNode.of(1, null, 8), TreeNode.of(8, 1)));
        assertEquals(List.of(5), solution.getAllElements(null, TreeNode.of(5)));
        assertEquals(List.of(), solution.getAllElements(null, null));
    }
}
''',
trace=r'''
function run(x, y) {
  const r1 = A.mkTree(x), r2 = A.mkTree(y), ino = n => (n ? [...ino(n.left), n.val, ...ino(n.right)] : []);
  const a = ino(r1), b = ino(r2), out = []; let i = 0, j = 0;
  A.step('Each BST read in order is already sorted.', A.tree('tree 1', r1), A.tree('tree 2', r2));
  A.step('In-order lists of both trees.', A.arr('tree 1', a), A.arr('tree 2', b));
  while (i < a.length || j < b.length) {
    const fromA = j === b.length || (i < a.length && a[i] <= b[j]); out.push(fromA ? a[i] : b[j]);
    A.step(`Take ${out[out.length - 1]} from tree ${fromA ? 1 : 2}.`, A.arr('tree 1', a, { hl: fromA ? { [i]: 'ok' } : {}, ptr: i < a.length ? { [i]: 'i' } : {} }), A.arr('tree 2', b, { hl: fromA ? {} : { [j]: 'ok' }, ptr: j < b.length ? { [j]: 'j' } : {} }), A.arr('merged', out));
    if (fromA) i++; else j++;
  }
  A.step(`Merged: [${out}].`, A.arr('merged', out));
}
A.scenario('Example', '[2,1,4] and [1,0,3]', () => run([2, 1, 4], [1, 0, 3]));
'''),

P(num=1325, slug="delete-leaves-with-a-given-value", title="Delete Leaves With a Given Value", diff="Medium", topic="Binary Tree DFS", cls="DeleteLeavesWithValue",
idea="Clean the children first; a node that becomes a leaf with the target value is then removed too.",
vname="Post-order pruning", helpers=["TreeNode"],
spec=r'''
Delete every leaf whose value is `target`. If deleting leaves turns a parent into a target-valued leaf, delete it too, and so on.

**Example**
```
[1,2,3,2,null,2,4], target = 2 → [1,null,3,null,4]
[1,3,3,3,2],        target = 3 → [1,3,null,null,2]
[1,2,null,2,null,2], target = 2 → [1]
```

**Constraints**
* `1 <= n <= 3000`
''',
approach=r'''
**Bottom-up.** Recurse into both children first and replace them with the pruned results. Only then check the node itself: if it has no
children left and its value is `target`, return `null`.

* Time: **O(n)**.
* Space: **O(h)** — recursion depth.
''',
tc="n", sc="n",
java=r'''
public class DeleteLeavesWithValue {

    public TreeNode removeLeafNodes(TreeNode root, int target) {
        if (root == null) return null;
        root.left = removeLeafNodes(root.left, target);
        root.right = removeLeafNodes(root.right, target);
        return root.left == null && root.right == null && root.val == target ? null : root;
    }
}
''',
test=r'''
class DeleteLeavesWithValueTest {

    private final DeleteLeavesWithValue solution = new DeleteLeavesWithValue();

    @Test
    void examples() {
        assertEquals(Arrays.asList(1, null, 3, null, 4), TreeNode.toList(solution.removeLeafNodes(TreeNode.of(1, 2, 3, 2, null, 2, 4), 2)));
        assertEquals(Arrays.asList(1, 3, null, null, 2), TreeNode.toList(solution.removeLeafNodes(TreeNode.of(1, 3, 3, 3, 2), 3)));
        assertEquals(List.of(1), TreeNode.toList(solution.removeLeafNodes(TreeNode.of(1, 2, null, 2, null, 2), 2)));
        assertNull(solution.removeLeafNodes(TreeNode.of(1, 1, 1), 1));
    }
}
''',
trace=r'''
function run(arr, target) {
  const root = A.mkTree(arr), hl = {};
  A.step(`Remove leaves with value ${target}, children first, so parents that become such leaves go too.`, A.tree('tree', root));
  const out = (function go(n) {
    if (!n) return null;
    n.left = go(n.left); n.right = go(n.right);
    if (!n.left && !n.right && n.val === target) { A.step(`${n.val} is now a leaf with the target value: delete it.`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'bad' } })); return null; }
    hl[n.id] = 'ok';
    A.step(`${n.val} stays${n.left || n.right ? ' (it still has children)' : ` (its value is not ${target})`}.`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'cur' } }));
    return n;
  })(root);
  A.step(out ? 'Pruning complete.' : 'The whole tree was deleted.', out ? A.tree('result', out, { hl }) : A.text('Result', 'null', 'bad'));
}
A.scenario('Cascade', '[1,2,3,2,null,2,4], target 2', () => run([1, 2, 3, 2, null, 2, 4], 2));
'''),

P(num=1337, slug="the-k-weakest-rows-in-a-matrix", title="The K Weakest Rows in a Matrix", diff="Easy", topic="Binary Search", cls="KWeakestRows",
idea="Soldiers (1s) come first in each row, so binary search counts them; then sort rows by (count, index).",
vname="Binary search counts + sort",
spec=r'''
Each row of a binary matrix has its soldiers (`1`) before its civilians (`0`). Row `i` is weaker than row `j` if it has fewer soldiers,
or the same number and `i < j`. Return the indices of the `k` weakest rows, weakest first.

**Example**
```
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], k = 3 → [2,0,3]
```

**Constraints**
* `2 <= m, n <= 100`, `1 <= k <= m`
''',
approach=r'''
**Count, then order.** Binary search each row for the first `0`; its index is the soldier count. Encode each row as `count * m + index`
so a plain integer sort orders by count, then by index, and take the first `k`.

* Time: **O(m log n + m log m)**.
* Space: **O(m)**.
''',
tc="nlogn", sc="n",
java=r'''
public class KWeakestRows {

    public int[] kWeakestRows(int[][] mat, int k) {
        int m = mat.length;
        int[] key = new int[m];
        for (int i = 0; i < m; i++) key[i] = soldiers(mat[i]) * m + i;
        Arrays.sort(key);
        int[] out = new int[k];
        for (int i = 0; i < k; i++) out[i] = key[i] % m;
        return out;
    }

    private int soldiers(int[] row) {
        int lo = 0, hi = row.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (row[mid] == 1) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
''',
test=r'''
class KWeakestRowsTest {

    private final KWeakestRows solution = new KWeakestRows();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 0, 3}, solution.kWeakestRows(new int[][]{{1, 1, 0, 0, 0}, {1, 1, 1, 1, 0}, {1, 0, 0, 0, 0}, {1, 1, 0, 0, 0}, {1, 1, 1, 1, 1}}, 3));
        assertArrayEquals(new int[]{0, 2}, solution.kWeakestRows(new int[][]{{1, 0, 0, 0}, {1, 1, 1, 1}, {1, 0, 0, 0}, {1, 0, 0, 0}}, 2));
        assertArrayEquals(new int[]{1, 0}, solution.kWeakestRows(new int[][]{{1, 1}, {0, 0}}, 2));
    }
}
''',
trace=r'''
function run(mat, k) {
  const m = mat.length, cnt = [];
  A.step('Each row starts with its soldiers. Binary search for the first civilian to count them.', A.grid('matrix', mat));
  mat.forEach((row, i) => { let lo = 0, hi = row.length; while (lo < hi) { const mid = (lo + hi) >> 1; if (row[mid]) lo = mid + 1; else hi = mid; } cnt.push(lo); A.step(`Row ${i}: ${lo} soldier${lo === 1 ? '' : 's'}.`, A.grid('matrix', mat, { hl: Object.fromEntries(row.map((_, c) => [`${i},${c}`, c < lo ? 'cur' : 'dim'])) }), A.arr('soldiers', cnt)); });
  const order = [...Array(m).keys()].sort((a, b) => cnt[a] - cnt[b] || a - b);
  A.step(`Sort rows by (soldiers, index): [${order}]. Take the first ${k}.`, A.arr('weakest first', order, { hl: Object.fromEntries(order.slice(0, k).map((_, i) => [i, 'ok'])) }), A.text('Result', `[${order.slice(0, k)}]`, 'ok'));
}
A.scenario('Example', 'k = 3', () => run([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3));
'''),

P(num=1351, slug="count-negative-numbers-in-a-sorted-matrix", title="Count Negative Numbers in a Sorted Matrix", diff="Easy", topic="Matrix", cls="CountNegatives",
idea="Rows and columns are non-increasing, so the boundary of the negatives is a staircase you can walk in m + n steps.",
vname="Staircase walk",
spec=r'''
A matrix is sorted in **non-increasing** order along every row and every column. Count its negative numbers.

**Example**
```
[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]] → 8
[[3,2],[1,0]] → 0
```

**Constraints**
* `1 <= m, n <= 100`
''',
approach=r'''
**Staircase.** Start at the bottom-left. If the value is negative, everything to its right in that row is too: add `n - col` and move up.
Otherwise move right. Each step leaves a row or a column for good.

* Time: **O(m + n)**.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class CountNegatives {

    public int countNegatives(int[][] grid) {
        int m = grid.length, n = grid[0].length, r = m - 1, c = 0, count = 0;
        while (r >= 0 && c < n) {
            if (grid[r][c] < 0) {
                count += n - c;
                r--;
            } else c++;
        }
        return count;
    }
}
''',
test=r'''
class CountNegativesTest {

    private final CountNegatives solution = new CountNegatives();

    @Test
    void examples() {
        assertEquals(8, solution.countNegatives(new int[][]{{4, 3, 2, -1}, {3, 2, 1, -1}, {1, 1, -1, -2}, {-1, -1, -2, -3}}));
        assertEquals(0, solution.countNegatives(new int[][]{{3, 2}, {1, 0}}));
        assertEquals(1, solution.countNegatives(new int[][]{{-1}}));
        assertEquals(3, solution.countNegatives(new int[][]{{5, 1, 0}, {-5, -5, -5}}));
    }
}
''',
trace=r'''
function run(g) {
  const m = g.length, n = g[0].length, hl = {}; let r = m - 1, c = 0, count = 0;
  A.step('Start at the bottom-left corner.', A.grid('grid', g, { hl: { [`${r},${c}`]: 'cur' } }));
  while (r >= 0 && c < n) {
    if (g[r][c] < 0) { for (let k = c; k < n; k++) hl[`${r},${k}`] = 'bad'; count += n - c; A.step(`${g[r][c]} is negative, so the rest of row ${r} is too: +${n - c}. Move up.`, A.grid('grid', g, { hl: { ...hl, [`${r},${c}`]: 'cur' } }), A.vars({ count })); r--; }
    else { hl[`${r},${c}`] = 'dim'; A.step(`${g[r][c]} is not negative: move right.`, A.grid('grid', g, { hl: { ...hl, [`${r},${c}`]: 'cur' } }), A.vars({ count })); c++; }
  }
  A.step(`${count} negative numbers.`, A.grid('grid', g, { hl }), A.text('Result', count, 'ok'));
}
A.scenario('Example', '4 × 4', () => run([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]));
'''),

P(num=1376, slug="time-needed-to-inform-all-employees", title="Time Needed to Inform All Employees", diff="Medium", topic="Tree", cls="TimeToInform",
idea="The company is a tree rooted at the head; the answer is the slowest root-to-leaf chain of inform times.",
vname="BFS down the management tree",
spec=r'''
A company has `n` employees; `manager[i]` is the direct manager of `i` (`-1` for the head, `headID`). Starting with the head, each manager
needs `informTime[i]` minutes to tell all direct reports, who then pass it on. Return the minutes until everyone knows.

**Example**
```
n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0] → 1
n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1] → 21
```

**Constraints**
* `1 <= n <= 10^5`
''',
approach=r'''
**Tree paths.** Build child lists from `manager` (as linked arrays, so no per-node lists). Traverse from the head with a queue, carrying the
time at which each employee hears the news: a child hears at `time[parent] + informTime[parent]`. The answer is the latest time. Iteration
avoids deep recursion on a 10⁵-long chain.

* Time: **O(n)**.
* Space: **O(n)**.
''',
tc="n", sc="n",
java=r'''
public class TimeToInform {

    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        int[] firstChild = new int[n], nextSibling = new int[n], time = new int[n];
        Arrays.fill(firstChild, -1);
        for (int i = 0; i < n; i++)
            if (manager[i] != -1) {
                nextSibling[i] = firstChild[manager[i]];
                firstChild[manager[i]] = i;
            }
        Deque<Integer> queue = new ArrayDeque<>(List.of(headID));
        int best = 0;
        while (!queue.isEmpty()) {
            int p = queue.poll();
            best = Math.max(best, time[p]);
            for (int c = firstChild[p]; c != -1; c = nextSibling[c]) {
                time[c] = time[p] + informTime[p];
                queue.add(c);
            }
        }
        return best;
    }
}
''',
test=r'''
class TimeToInformTest {

    private final TimeToInform solution = new TimeToInform();

    @Test
    void examples() {
        assertEquals(0, solution.numOfMinutes(1, 0, new int[]{-1}, new int[]{0}));
        assertEquals(1, solution.numOfMinutes(6, 2, new int[]{2, 2, -1, 2, 2, 2}, new int[]{0, 0, 1, 0, 0, 0}));
        assertEquals(21, solution.numOfMinutes(7, 6, new int[]{1, 2, 3, 4, 5, 6, -1}, new int[]{0, 6, 5, 4, 3, 2, 1}));
        assertEquals(3, solution.numOfMinutes(4, 0, new int[]{-1, 0, 0, 1}, new int[]{1, 2, 5, 0}));
    }

    @Test
    void longChain() {
        int n = 100_000;
        int[] manager = new int[n], inform = new int[n];
        for (int i = 0; i < n; i++) {
            manager[i] = i - 1;
            inform[i] = 1;
        }
        assertEquals(n - 1, solution.numOfMinutes(n, 0, manager, inform));
    }
}
''',
trace=r'''
function run(n, head, manager, inform) {
  const nodes = [...Array(n).keys()].map(i => ({ id: i, label: `${i}` })), edges = manager.map((m, i) => (m >= 0 ? [m, i, inform[m] + 'm'] : null)).filter(Boolean);
  const kids = p => manager.map((m, i) => (m === p ? i : -1)).filter(i => i >= 0), time = new Array(n).fill(null), hl = {};
  time[head] = 0; let q = [head], best = 0;
  A.step(`The head, ${head}, knows at minute 0. Edge labels show how long each manager takes to inform their reports.`, A.graph('company', nodes, edges, { directed: true, hl: { [head]: 'cur' } }));
  while (q.length) {
    const next = [];
    q.forEach(p => { best = Math.max(best, time[p]); hl[p] = 'ok'; kids(p).forEach(c => { time[c] = time[p] + inform[p]; next.push(c); }); });
    if (next.length) A.step(`Next to hear: ${next.map(c => `${c} at minute ${time[c]}`).join(', ')}.`, A.graph('company', nodes, edges, { directed: true, hl: { ...hl, ...Object.fromEntries(next.map(c => [c, 'cur'])) } }), A.arr('time heard', time.map(t => (t === null ? '·' : t))));
    q = next;
  }
  A.step(`The last employee hears at minute ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Two levels', 'head 0', () => run(6, 0, [-1, 0, 0, 1, 1, 2], [3, 2, 4, 0, 0, 0]));
A.scenario('Chain', 'head 3', () => run(4, 3, [1, 2, 3, -1], [0, 1, 2, 3]));
'''),

P(num=1381, slug="design-a-stack-with-increment-operation", title="Design a Stack With Increment Operation", diff="Medium", topic="Design", cls="CustomStack",
idea="Store pending increments lazily at the top affected index and pass them down when that element is popped.",
vname="Lazy increments",
spec=r'''
Implement `CustomStack`:

* `CustomStack(int maxSize)` — pushes beyond `maxSize` elements are ignored.
* `void push(int x)`, `int pop()` (returns `-1` when empty).
* `void increment(int k, int val)` — add `val` to the bottom `k` elements (all of them if fewer).

**Example**
```
CustomStack(3); push(1); push(2); pop() → 2; push(2); push(3); push(4) (ignored);
increment(5,100); increment(2,100); pop() → 103; pop() → 202; pop() → 201; pop() → -1
```

**Constraints**
* `1 <= maxSize, x, k <= 1000`; up to 1000 calls of each method
''',
approach=r'''
**Lazy tags.** Keep `inc[i]`: an amount to be added to elements `0..i`. `increment(k, val)` adds `val` to `inc[min(k, size) - 1]` only.
When popping index `i`, return `stack[i] + inc[i]` and move `inc[i]` down to `inc[i - 1]`, since it also applies below.

* Time: **O(1)** — every operation.
* Space: **O(maxSize)**.
''',
tc="1", sc="n",
java=r'''
public class CustomStack {

    private final int[] stack, inc;
    private int size;

    public CustomStack(int maxSize) {
        stack = new int[maxSize];
        inc = new int[maxSize];
    }

    public void push(int x) {
        if (size < stack.length) stack[size++] = x;
    }

    public int pop() {
        if (size == 0) return -1;
        int i = --size, v = stack[i] + inc[i];
        if (i > 0) inc[i - 1] += inc[i];
        inc[i] = 0;
        return v;
    }

    public void increment(int k, int val) {
        int top = Math.min(k, size) - 1;
        if (top >= 0) inc[top] += val;
    }
}
''',
test=r'''
class CustomStackTest {

    @Test
    void example() {
        CustomStack s = new CustomStack(3);
        s.push(1);
        s.push(2);
        assertEquals(2, s.pop());
        s.push(2);
        s.push(3);
        s.push(4);
        s.increment(5, 100);
        s.increment(2, 100);
        assertEquals(103, s.pop());
        assertEquals(202, s.pop());
        assertEquals(201, s.pop());
        assertEquals(-1, s.pop());
    }

    @Test
    void incrementOnEmptyAndReuse() {
        CustomStack s = new CustomStack(2);
        s.increment(3, 5);
        s.push(1);
        s.increment(1, 10);
        assertEquals(11, s.pop());
        s.push(7);
        assertEquals(7, s.pop());
    }
}
''',
trace=r'''
function run(max, ops) {
  const st = [], inc = new Array(max).fill(0);
  const view = () => [A.arr('stack', st.length ? st : ['·']), A.arr('lazy inc', inc, { hl: Object.fromEntries(inc.map((v, i) => [i, v ? 'cur' : ''])) })];
  A.step(`A stack of at most ${max}. inc[i] is an amount owed to elements 0..i.`, ...view());
  ops.forEach(([op, a, b]) => {
    if (op === 'push') { const ok = st.length < max; if (ok) st.push(a); A.step(ok ? `push(${a}).` : `push(${a}) ignored: the stack is full.`, ...view()); }
    else if (op === 'inc') { const top = Math.min(a, st.length) - 1; if (top >= 0) inc[top] += b; A.step(`increment(${a}, ${b}): record +${b} at index ${top} only, O(1).`, ...view()); }
    else { if (!st.length) { A.step('pop() on an empty stack → −1.', ...view()); return; } const i = st.length - 1, v = st.pop() + inc[i]; if (i > 0) inc[i - 1] += inc[i]; const pass = inc[i]; inc[i] = 0; A.step(`pop() → ${v - pass} + ${pass} = ${v}.${i > 0 && pass ? ` Pass the +${pass} down to index ${i - 1}.` : ''}`, ...view(), A.text('Returned', v, 'ok')); }
  });
}
A.scenario('Example', 'maxSize 3', () => run(3, [['push', 1], ['push', 2], ['pop'], ['push', 2], ['push', 3], ['push', 4], ['inc', 5, 100], ['inc', 2, 100], ['pop'], ['pop'], ['pop'], ['pop']]));
'''),

P(num=1396, slug="design-underground-system", title="Design Underground System", diff="Medium", topic="Hash Map", cls="UndergroundSystem",
idea="Remember each open trip by card id; on check-out, add the trip time to a running total for the station pair.",
vname="Two hash maps",
spec=r'''
Implement `UndergroundSystem`:

* `checkIn(int id, String station, int t)` and `checkOut(int id, String station, int t)` — a customer can be checked in to one place at a
  time.
* `double getAverageTime(String start, String end)` — the average time of all completed trips from `start` to `end` (at least one exists).

**Example**
```
checkIn(45,"Leyton",3); checkIn(32,"Paradise",8); checkIn(27,"Leyton",10);
checkOut(45,"Waterloo",15); checkOut(27,"Waterloo",20); checkOut(32,"Cambridge",22);
getAverageTime("Paradise","Cambridge") → 14.0
getAverageTime("Leyton","Waterloo") → 11.0
```

**Constraints**
* Up to `2 * 10^4` calls; station names are 1–10 letters
''',
approach=r'''
**Two maps.** `open` maps a card id to its check-in station and time. On check-out, remove it and add the duration to `stats` for the key
`start + "," + end`, which holds a total and a count. The average is `total / count`. Both maps are `MyHashMap`.

* Time: **O(L)** — per call, for building and hashing the station key.
* Space: **O(P + S²)** — open trips and station pairs.
''',
tc="1", sc="n",
java=r'''
public class UndergroundSystem {

    private record Trip(String station, int time) {}

    private final MyHashMap<Integer, Trip> open = new MyHashMap<>();
    private final MyHashMap<String, long[]> stats = new MyHashMap<>();

    public void checkIn(int id, String stationName, int t) {
        open.put(id, new Trip(stationName, t));
    }

    public void checkOut(int id, String stationName, int t) {
        Trip trip = open.remove(id);
        long[] s = stats.computeIfAbsent(trip.station() + "," + stationName, k -> new long[2]);
        s[0] += t - trip.time();
        s[1]++;
    }

    public double getAverageTime(String startStation, String endStation) {
        long[] s = stats.get(startStation + "," + endStation);
        return (double) s[0] / s[1];
    }
}
''',
test=r'''
class UndergroundSystemTest {

    @Test
    void example() {
        UndergroundSystem u = new UndergroundSystem();
        u.checkIn(45, "Leyton", 3);
        u.checkIn(32, "Paradise", 8);
        u.checkIn(27, "Leyton", 10);
        u.checkOut(45, "Waterloo", 15);
        u.checkOut(27, "Waterloo", 20);
        u.checkOut(32, "Cambridge", 22);
        assertEquals(14.0, u.getAverageTime("Paradise", "Cambridge"), 1e-9);
        assertEquals(11.0, u.getAverageTime("Leyton", "Waterloo"), 1e-9);
        u.checkIn(10, "Leyton", 24);
        assertEquals(11.0, u.getAverageTime("Leyton", "Waterloo"), 1e-9);
        u.checkOut(10, "Waterloo", 38);
        assertEquals(12.0, u.getAverageTime("Leyton", "Waterloo"), 1e-9);
    }

    @Test
    void directionMatters() {
        UndergroundSystem u = new UndergroundSystem();
        u.checkIn(1, "A", 0);
        u.checkOut(1, "B", 5);
        u.checkIn(1, "B", 10);
        u.checkOut(1, "A", 30);
        assertEquals(5.0, u.getAverageTime("A", "B"), 1e-9);
        assertEquals(20.0, u.getAverageTime("B", "A"), 1e-9);
    }
}
''',
trace=r'''
function run(ops) {
  const open = new Map(), stats = new Map();
  const view = hl => [A.hashTable('open trips: id → (station, time)', new Map([...open].map(([k, v]) => [k, `${v[0]}@${v[1]}`])), { hl }), A.map('pair → total / count', Object.fromEntries([...stats].map(([k, v]) => [k, `${v[0]} / ${v[1]}`])))];
  A.step('One map for trips in progress, one for totals per (start, end) pair.', ...view());
  ops.forEach(([op, ...a]) => {
    if (op === 'in') { open.set(a[0], [a[1], a[2]]); A.step(`checkIn(${a[0]}, ${a[1]}, ${a[2]}).`, ...view(a[0])); }
    else if (op === 'out') { const [st, t0] = open.get(a[0]); open.delete(a[0]); const k = `${st},${a[1]}`, s = stats.get(k) || [0, 0]; s[0] += a[2] - t0; s[1]++; stats.set(k, s); A.step(`checkOut(${a[0]}, ${a[1]}, ${a[2]}): trip ${st} → ${a[1]} took ${a[2] - t0}. Add it to that pair.`, ...view()); }
    else { const s = stats.get(`${a[0]},${a[1]}`); A.step(`getAverageTime(${a[0]}, ${a[1]}) = ${s[0]} / ${s[1]} = ${(s[0] / s[1]).toFixed(1)}.`, ...view(), A.text('Returned', (s[0] / s[1]).toFixed(1), 'ok')); }
  });
}
A.scenario('Example', 'three trips', () => run([['in', 45, 'Leyton', 3], ['in', 32, 'Paradise', 8], ['in', 27, 'Leyton', 10], ['out', 45, 'Waterloo', 15], ['out', 27, 'Waterloo', 20], ['out', 32, 'Cambridge', 22], ['avg', 'Paradise', 'Cambridge'], ['avg', 'Leyton', 'Waterloo']]));
'''),

P(num=1405, slug="longest-happy-string", title="Longest Happy String", diff="Medium", topic="Greedy", cls="LongestHappyString",
idea="Always append the letter with the most copies left, unless that would make three in a row; then use the next one.",
vname="Greedy by remaining count",
spec=r'''
A string is **happy** if it uses only `'a'`, `'b'`, `'c'`, never contains `"aaa"`, `"bbb"` or `"ccc"`, and uses at most `a`, `b`, `c`
copies of each letter. Return any longest happy string (`""` if none).

**Example**
```
a = 1, b = 1, c = 7 → "ccaccbcc"  (length 8)
a = 7, b = 1, c = 0 → "aabaa"     (length 5)
```

**Constraints**
* `0 <= a, b, c <= 100`, `a + b + c > 0`
''',
approach=r'''
**Spend the biggest pile.** Repeatedly try the letters from most to fewest remaining copies. Append the first one that would not create
three equal letters in a row. Stop when nothing can be appended. Using the largest pile whenever allowed keeps the others available as
separators for as long as possible.

* Time: **O(a + b + c)** — one letter per round (sorting three items is constant).
* Space: **O(1)** — besides the output.
''',
tc="n", sc="1",
java=r'''
public class LongestHappyString {

    public String longestDiverseString(int a, int b, int c) {
        int[] left = {a, b, c};
        StringBuilder sb = new StringBuilder();
        while (true) {
            Integer[] order = {0, 1, 2};
            Arrays.sort(order, (x, y) -> left[y] - left[x]);
            boolean placed = false;
            for (int i : order) {
                if (left[i] == 0) break;
                char ch = (char) ('a' + i);
                int n = sb.length();
                if (n >= 2 && sb.charAt(n - 1) == ch && sb.charAt(n - 2) == ch) continue;
                sb.append(ch);
                left[i]--;
                placed = true;
                break;
            }
            if (!placed) return sb.toString();
        }
    }
}
''',
test=r'''
class LongestHappyStringTest {

    private final LongestHappyString solution = new LongestHappyString();

    private void check(int a, int b, int c, int expectedLength) {
        String s = solution.longestDiverseString(a, b, c);
        assertEquals(expectedLength, s.length(), s);
        assertFalse(s.contains("aaa") || s.contains("bbb") || s.contains("ccc"), s);
        assertTrue(s.chars().filter(ch -> ch == 'a').count() <= a);
        assertTrue(s.chars().filter(ch -> ch == 'b').count() <= b);
        assertTrue(s.chars().filter(ch -> ch == 'c').count() <= c);
    }

    @Test
    void examples() {
        check(1, 1, 7, 8);
        check(7, 1, 0, 5);
        check(2, 2, 1, 5);
        check(0, 0, 5, 2);
        check(4, 4, 4, 12);
    }
}
''',
trace=r'''
function run(a, b, c) {
  const left = { a, b, c }; let s = '';
  A.step('Each round, use the letter with the most copies left, unless it would make three in a row.', A.map('copies left', left), A.chars('string', ' '));
  while (true) {
    const order = Object.keys(left).sort((x, y) => left[y] - left[x]); let used = null, skipped = null;
    for (const ch of order) { if (!left[ch]) break; if (s.endsWith(ch + ch)) { skipped = ch; continue; } used = ch; break; }
    if (!used) { A.step(skipped ? `Only '${skipped}' is left, and it would make three in a row. Stop.` : 'No letters are left. Stop.', A.map('copies left', left), A.chars('string', s || ' ')); break; }
    s += used; left[used]--;
    A.step(skipped ? `'${skipped}' would make three in a row; use '${used}' instead.` : `Use '${used}', the largest pile.`, A.map('copies left', left), A.chars('string', s, { hl: { [s.length - 1]: skipped ? 'alt' : 'ok' } }));
  }
  A.step(`Happy string of length ${s.length}: "${s}".`, A.text('Result', s, 'ok'));
}
A.scenario('One big pile', 'a = 1, b = 1, c = 7', () => run(1, 1, 7));
'''),

P(num=1424, slug="diagonal-traverse-ii", title="Diagonal Traverse II", diff="Medium", topic="Matrix", cls="DiagonalTraverseII",
idea="Cells on one anti-diagonal share i + j; bucket them, visiting rows bottom-up so each bucket is already in output order.",
vname="Buckets by i + j",
spec=r'''
Given a jagged 2-D list `nums` (rows may have different lengths), return all elements in diagonal order: anti-diagonals `i + j = 0, 1, 2,
…`, each read from bottom-left to top-right.

**Example**
```
[[1,2,3],[4,5,6],[7,8,9]] → [1,4,2,7,5,3,8,6,9]
[[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]] → [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
```

**Constraints**
* Up to `10^5` elements in total
''',
approach=r'''
**Group by diagonal.** Element `(i, j)` belongs to diagonal `i + j`. Walk the rows from the **last** to the first and append each element to
its diagonal's bucket: within a bucket the larger `i` comes first, which is the bottom-left-to-top-right order. Concatenate the buckets.
Only existing cells are touched, which matters for very jagged input.

* Time: **O(N)** — `N` elements.
* Space: **O(N)** — the buckets.
''',
tc="n", sc="n",
java=r'''
public class DiagonalTraverseII {

    public int[] findDiagonalOrder(List<List<Integer>> nums) {
        List<List<Integer>> buckets = new ArrayList<>();
        int total = 0;
        for (int i = nums.size() - 1; i >= 0; i--) {
            List<Integer> row = nums.get(i);
            for (int j = 0; j < row.size(); j++) {
                while (buckets.size() <= i + j) buckets.add(new ArrayList<>());
                buckets.get(i + j).add(row.get(j));
                total++;
            }
        }
        int[] out = new int[total];
        int k = 0;
        for (List<Integer> b : buckets) for (int v : b) out[k++] = v;
        return out;
    }
}
''',
test=r'''
class DiagonalTraverseIITest {

    private final DiagonalTraverseII solution = new DiagonalTraverseII();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 4, 2, 7, 5, 3, 8, 6, 9},
                solution.findDiagonalOrder(List.of(List.of(1, 2, 3), List.of(4, 5, 6), List.of(7, 8, 9))));
        assertArrayEquals(new int[]{1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16},
                solution.findDiagonalOrder(List.of(List.of(1, 2, 3, 4, 5), List.of(6, 7), List.of(8), List.of(9, 10, 11), List.of(12, 13, 14, 15, 16))));
        assertArrayEquals(new int[]{1, 2, 3}, solution.findDiagonalOrder(List.of(List.of(1, 2, 3))));
    }
}
''',
trace=r'''
function run(rows) {
  const w = Math.max(...rows.map(r => r.length)), grid = rows.map(r => [...r, ...new Array(w - r.length).fill('')]), buckets = [];
  A.step('Cells on the same anti-diagonal share the same i + j.', A.grid('nums', grid));
  for (let i = rows.length - 1; i >= 0; i--) {
    rows[i].forEach((v, j) => { while (buckets.length <= i + j) buckets.push([]); buckets[i + j].push(v); });
    A.step(`Row ${i} (walking bottom-up): each value joins bucket i + j. Lower rows go first, so each bucket reads bottom-left to top-right.`, A.grid('nums', grid, { hl: Object.fromEntries(rows[i].map((_, j) => [`${i},${j}`, 'cur'])) }), A.arr('buckets', buckets.map(b => b.join(',') || '·')));
  }
  const out = buckets.flat();
  A.step(`Concatenate the buckets: [${out}].`, A.arr('result', out));
}
A.scenario('Square', '3 × 3', () => run([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
A.scenario('Jagged', 'rows of different lengths', () => run([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]));
'''),
]
