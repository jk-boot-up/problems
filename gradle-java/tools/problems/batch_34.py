PROBLEMS = [
P(num=783, slug="minimum-distance-between-bst-nodes", title="Minimum Distance Between BST Nodes", diff="Easy", topic="Binary Search Tree", cls="MinimumDistanceBST",
idea="In-order traversal visits BST values in sorted order; the minimum gap is between neighbours.",
vname="In-order with previous value", helpers=["TreeNode"],
spec=r'''
Return the minimum difference between the values of any two different nodes of a BST.

**Example**
```
[4,2,6,1,3] → 1,   [1,0,48,null,null,12,49] → 1
```

**Constraints**
* `2 <= n <= 100`
''',
approach=r'''
**Sorted neighbours.** Iterative in-order traversal; compare each value with the previous one.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the stack.
''',
tc="n", sc="n",
java=r'''
public class MinimumDistanceBST {

    public int minDiffInBST(TreeNode root) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode cur = root;
        Integer prev = null;
        int best = Integer.MAX_VALUE;
        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            if (prev != null) best = Math.min(best, cur.val - prev);
            prev = cur.val;
            cur = cur.right;
        }
        return best;
    }
}
''',
test=r'''
class MinimumDistanceBSTTest {

    private final MinimumDistanceBST solution = new MinimumDistanceBST();

    @Test
    void examples() {
        assertEquals(1, solution.minDiffInBST(TreeNode.of(4, 2, 6, 1, 3)));
        assertEquals(1, solution.minDiffInBST(TreeNode.of(1, 0, 48, null, null, 12, 49)));
        assertEquals(1, solution.minDiffInBST(TreeNode.of(90, 69, null, 49, 89, null, 52)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), seq = [], hl = {}; let prev = null, best = Infinity;
  (function ino(n) { if (!n) return; ino(n.left); seq.push(n.val); hl[n.id] = 'ok'; if (prev !== null) { best = Math.min(best, n.val - prev); } A.step(prev === null ? `Smallest value: ${n.val}.` : `${n.val} − ${prev} = ${n.val - prev}. Minimum so far ${best}.`, A.tree('BST', root, { hl: { ...hl, [n.id]: 'cur' } }), A.arr('in-order', seq)); prev = n.val; ino(n.right); })(root);
  A.step(`Minimum distance: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', '[4,2,6,1,3]', () => run([4, 2, 6, 1, 3]));
'''),

P(num=785, slug="is-graph-bipartite", title="Is Graph Bipartite?", diff="Medium", topic="Graph General", cls="IsGraphBipartite",
idea="Two-colour the graph with BFS; an edge between two nodes of the same colour means it is not bipartite.",
vname="BFS two-colouring",
spec=r'''
`graph[u]` lists the neighbours of node `u` in an undirected graph (possibly disconnected). Return `true` if the nodes can be split into two
sets so that every edge joins nodes from different sets.

**Example**
```
[[1,2,3],[0,2],[0,1,3],[0,2]] → false
[[1,3],[0,2],[1,3],[0,2]]     → true
```

**Constraints**
* `1 <= n <= 100`
''',
approach=r'''
**Colouring.** For every uncoloured node, start a BFS, colouring it 1 and each neighbour the opposite colour. A neighbour that already has
the same colour proves an odd cycle.

* Time: **O(V + E)** — each node and edge once.
* Space: **O(V)** — colours and queue.
''',
java=r'''
public class IsGraphBipartite {

    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n]; // 0 = uncoloured, 1 / -1 = the two sides
        for (int s = 0; s < n; s++) {
            if (color[s] != 0) continue;
            color[s] = 1;
            Deque<Integer> queue = new ArrayDeque<>(List.of(s));
            while (!queue.isEmpty()) {
                int u = queue.poll();
                for (int v : graph[u]) {
                    if (color[v] == color[u]) return false;
                    if (color[v] == 0) {
                        color[v] = -color[u];
                        queue.add(v);
                    }
                }
            }
        }
        return true;
    }
}
''',
test=r'''
class IsGraphBipartiteTest {

    private final IsGraphBipartite solution = new IsGraphBipartite();

    @Test
    void examples() {
        assertFalse(solution.isBipartite(new int[][]{{1, 2, 3}, {0, 2}, {0, 1, 3}, {0, 2}}));
        assertTrue(solution.isBipartite(new int[][]{{1, 3}, {0, 2}, {1, 3}, {0, 2}}));
        assertTrue(solution.isBipartite(new int[][]{{}, {2}, {1}}));
    }
}
''',
trace=r'''
function run(g) {
  const n = g.length, nodes = g.map((_, i) => ({ id: i, label: i })), edges = []; g.forEach((ns, u) => ns.forEach(v => u < v && edges.push([u, v])));
  const color = new Array(n).fill(0);
  const hl = () => Object.fromEntries(color.map((c, i) => [i, c === 1 ? 'sel' : c === -1 ? 'alt' : '']));
  for (let s = 0; s < n; s++) {
    if (color[s]) continue; color[s] = 1; const q = [s];
    A.step(`Colour node ${s} blue and spread outward, alternating colours.`, A.graph('graph', nodes, edges, { hl: hl() }));
    while (q.length) { const u = q.shift(); for (const v of g[u]) { if (color[v] === color[u]) { A.step(`Nodes ${u} and ${v} are joined but have the same colour: not bipartite.`, A.graph('graph', nodes, edges.map(e => [...e, '', (e[0] === u && e[1] === v) || (e[0] === v && e[1] === u) ? 'bad' : '']), { hl: { ...hl(), [u]: 'bad', [v]: 'bad' } }), A.text('Result', 'false', 'bad')); return; } if (!color[v]) { color[v] = -color[u]; q.push(v); A.step(`Node ${v} gets the opposite colour of ${u}.`, A.graph('graph', nodes, edges, { hl: hl() })); } } }
  }
  A.step('Every edge joins a blue node and a purple node: bipartite.', A.graph('graph', nodes, edges, { hl: hl() }), A.text('Result', 'true', 'ok'));
}
A.scenario('Bipartite square', '[[1,3],[0,2],[1,3],[0,2]]', () => run([[1, 3], [0, 2], [1, 3], [0, 2]]));
A.scenario('Triangle inside', '[[1,2,3],[0,2],[0,1,3],[0,2]]', () => run([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]));
'''),

P(num=797, slug="all-paths-from-source-to-target", title="All Paths From Source to Target", diff="Medium", topic="Backtracking", cls="AllPathsSourceTarget",
idea="DFS from node 0 over the DAG, recording the path whenever it reaches node n − 1.",
vname="DFS with backtracking",
spec=r'''
Given a **DAG** of `n` nodes where `graph[i]` lists the nodes reachable from `i`, return every path from node `0` to node `n - 1`, in any order.

**Example**
```
[[1,2],[3],[3],[]]           → [[0,1,3],[0,2,3]]
[[4,3,1],[3,2,4],[3],[4],[]] → [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```

**Constraints**
* `2 <= n <= 15`; no cycles.
''',
approach=r'''
**Backtracking.** Extend the path with each next node; at `n - 1`, record a copy. No visited set is needed because the graph has no cycles.

* Time: **O(2ⁿ · n)** — up to 2ⁿ⁻² paths, each copied in O(n).
* Space: **O(n)** — the path and recursion.
''',
tc="exp", sc="n",
java=r'''
public class AllPathsSourceTarget {

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> out = new ArrayList<>();
        List<Integer> path = new ArrayList<>(List.of(0));
        dfs(graph, 0, path, out);
        return out;
    }

    private void dfs(int[][] graph, int u, List<Integer> path, List<List<Integer>> out) {
        if (u == graph.length - 1) {
            out.add(new ArrayList<>(path));
            return;
        }
        for (int v : graph[u]) {
            path.add(v);
            dfs(graph, v, path, out);
            path.removeLast();
        }
    }
}
''',
test=r'''
class AllPathsSourceTargetTest {

    private final AllPathsSourceTarget solution = new AllPathsSourceTarget();

    @Test
    void examples() {
        assertEquals(List.of(List.of(0, 1, 3), List.of(0, 2, 3)), solution.allPathsSourceTarget(new int[][]{{1, 2}, {3}, {3}, {}}));
        assertEquals(5, solution.allPathsSourceTarget(new int[][]{{4, 3, 1}, {3, 2, 4}, {3}, {4}, {}}).size());
    }
}
''',
trace=r'''
function run(g) {
  const n = g.length, nodes = g.map((_, i) => ({ id: i, label: i })), edges = g.flatMap((ns, u) => ns.map(v => [u, v])), out = [], path = [0];
  (function dfs(u) {
    if (u === n - 1) { out.push('[' + path + ']'); A.step(`Reached ${u}: record path ${path.join(' → ')}.`, A.graph('DAG', nodes, edges.map(([a, b]) => [a, b, '', path.some((x, i) => x === a && path[i + 1] === b) ? 'ok' : '']), { directed: true, hl: Object.fromEntries(path.map(x => [x, 'ok'])) }), A.arr('paths', out)); return; }
    for (const v of g[u]) { path.push(v); dfs(v); path.pop(); }
  })(0);
  A.step(`${out.length} paths.`, A.arr('paths', out));
}
A.scenario('Five nodes', '[[4,3,1],[3,2,4],[3],[4],[]]', () => run([[4, 3, 1], [3, 2, 4], [3], [4], []]));
'''),

P(num=844, slug="backspace-string-compare", title="Backspace String Compare", diff="Easy", topic="Two Pointers", cls="BackspaceStringCompare",
idea="Walk both strings from the end, skipping characters erased by '#', and compare the survivors one by one.",
vname="Backward two pointers",
spec=r'''
`#` is a backspace. Return `true` if `s` and `t` are equal after typing both into empty editors.

**Example**
```
"ab#c", "ad#c" → true,   "ab##", "c#d#" → true,   "a#c", "b" → false
```

**Constraints**
* `1 <= s.length, t.length <= 200`

**Follow-up:** O(n) time and O(1) space.
''',
approach=r'''
**From the back.** For each string, find the next surviving character from the right by counting pending backspaces. Compare surviving
characters pairwise.

* Time: **O(m + n)** — each character once.
* Space: **O(1)** — a few indices.
''',
java=r'''
public class BackspaceStringCompare {

    public boolean backspaceCompare(String s, String t) {
        int i = s.length() - 1, j = t.length() - 1;
        while (true) {
            i = nextValid(s, i);
            j = nextValid(t, j);
            if (i < 0 || j < 0) return i < 0 && j < 0;
            if (s.charAt(i--) != t.charAt(j--)) return false;
        }
    }

    /** Index of the next character (from the right) that survives the backspaces, or -1. */
    private static int nextValid(String s, int i) {
        int skip = 0;
        while (i >= 0) {
            if (s.charAt(i) == '#') skip++;
            else if (skip > 0) skip--;
            else break;
            i--;
        }
        return i;
    }
}
''',
test=r'''
class BackspaceStringCompareTest {

    private final BackspaceStringCompare solution = new BackspaceStringCompare();

    @ParameterizedTest
    @CsvSource({"ab#c,ad#c,true", "ab##,c#d#,true", "a#c,b,false", "bxj##tw,bxo#j##tw,true"})
    void compares(String s, String t, boolean expected) {
        assertEquals(expected, solution.backspaceCompare(s, t));
    }
}
''',
trace=r'''
function run(s, t) {
  const type = str => { const st = []; for (const c of str) c === '#' ? st.pop() : st.push(c); return st; };
  const a = type(s), b = type(t);
  A.step('Typing each string: a # removes the previous character.', A.chars('s', s), A.chars('t', t));
  A.step(`s becomes "${a.join('')}" and t becomes "${b.join('')}". (Walking from the back gives the same survivors without building the strings.)`, A.arr('s typed', a), A.arr('t typed', b));
  const ok = a.join('') === b.join('');
  A.step(ok ? 'They match.' : 'They differ.', A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('Equal', 's = "ab#c", t = "ad#c"', () => run('ab#c', 'ad#c'));
'''),

P(num=852, slug="peak-index-in-a-mountain-array", title="Peak Index in a Mountain Array", diff="Medium", topic="Binary Search", cls="PeakIndexInMountain",
idea="Binary search on the slope: if arr[mid] < arr[mid + 1] the peak is to the right, otherwise at mid or to the left.",
vname="Binary search on the slope",
spec=r'''
`arr` strictly increases then strictly decreases. Return the index of the peak in O(log n).

**Example**
```
[0,1,0] → 1,   [0,2,1,0] → 1,   [0,10,5,2] → 1
```

**Constraints**
* `3 <= arr.length <= 10^5`
''',
approach=r'''
**Follow the slope.** Same as Find Peak Element: move right while rising, otherwise move `hi` to `mid`.

* Time: **O(log n)** — binary search.
* Space: **O(1)** — two indices.
''',
tc="log",
java=r'''
public class PeakIndexInMountain {

    public int peakIndexInMountainArray(int[] arr) {
        int lo = 0, hi = arr.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] < arr[mid + 1]) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
}
''',
test=r'''
class PeakIndexInMountainTest {

    private final PeakIndexInMountain solution = new PeakIndexInMountain();

    @Test
    void examples() {
        assertEquals(1, solution.peakIndexInMountainArray(new int[]{0, 1, 0}));
        assertEquals(1, solution.peakIndexInMountainArray(new int[]{0, 2, 1, 0}));
        assertEquals(4, solution.peakIndexInMountainArray(new int[]{1, 3, 5, 7, 9, 4, 2}));
    }
}
''',
trace=r'''
function run(a) {
  let lo = 0, hi = a.length - 1;
  while (lo < hi) { const mid = (lo + hi) >> 1, up = a[mid] < a[mid + 1]; A.step(`mid = ${mid}: ${a[mid]} ${up ? '<' : '>'} ${a[mid + 1]}, so the peak is ${up ? 'to the right' : 'at mid or to the left'}.`, A.arr('arr', a, { range: [lo, hi], hl: { [mid]: 'cur', [mid + 1]: 'alt' } })); if (up) lo = mid + 1; else hi = mid; }
  A.step(`The peak is ${a[lo]} at index ${lo}.`, A.arr('arr', a, { hl: { [lo]: 'ok' } }), A.text('Result', lo, 'ok'));
}
A.scenario('Mountain', 'arr = [1,3,5,7,9,4,2]', () => run([1, 3, 5, 7, 9, 4, 2]));
'''),

P(num=876, slug="middle-of-the-linked-list", title="Middle of the Linked List", diff="Easy", topic="Linked List", cls="MiddleOfLinkedList",
idea="Fast moves two steps for each step of slow; when fast reaches the end, slow is in the middle.",
vname="Slow and fast pointers", helpers=["ListNode"],
spec=r'''
Return the middle node of a linked list; with two middle nodes, return the second.

**Example**
```
1→2→3→4→5 → node 3,   1→2→3→4→5→6 → node 4
```

**Constraints**
* `1 <= n <= 100`
''',
approach=r'''
**Tortoise and hare.** Move slow by 1 and fast by 2 while fast and fast.next exist.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two pointers.
''',
java=r'''
public class MiddleOfLinkedList {

    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
''',
test=r'''
class MiddleOfLinkedListTest {

    private final MiddleOfLinkedList solution = new MiddleOfLinkedList();

    @Test
    void examples() {
        assertArrayEquals(new int[]{3, 4, 5}, ListNode.toArray(solution.middleNode(ListNode.of(1, 2, 3, 4, 5))));
        assertArrayEquals(new int[]{4, 5, 6}, ListNode.toArray(solution.middleNode(ListNode.of(1, 2, 3, 4, 5, 6))));
    }
}
''',
trace=r'''
function run(v) {
  let s = 0, f = 0;
  A.step('slow takes one step while fast takes two.', A.list('list', v, { ptr: [[0, 'slow,fast']] }));
  while (f < v.length && f + 1 < v.length) { s++; f += 2; A.step(`slow → ${v[s]}, fast → ${f < v.length ? v[f] : 'null'}.`, A.list('list', v, { ptr: [[s, 'slow'], ...(f < v.length ? [[f, 'fast']] : [])] })); }
  A.step(`fast reached the end, so slow (${v[s]}) is the middle.`, A.list('list', v, { hl: { [s]: 'ok' } }), A.text('Result', v[s], 'ok'));
}
A.scenario('Even length', '1→2→3→4→5→6', () => run([1, 2, 3, 4, 5, 6]));
'''),

P(num=881, slug="boats-to-save-people", title="Boats to Save People", diff="Medium", topic="Greedy", cls="BoatsToSavePeople",
idea="Sort; the heaviest person shares a boat with the lightest if they fit, otherwise goes alone.",
vname="Sort + two pointers",
spec=r'''
Each boat carries at most two people with total weight at most `limit` (every person weighs at most `limit`). Return the minimum number of
boats.

**Example**
```
people = [1,2], limit = 3 → 1,   [3,2,2,1], limit = 3 → 3,   [3,5,3,4], limit = 5 → 4
```

**Constraints**
* `1 <= people.length <= 5 * 10^4`
''',
approach=r'''
**Greedy pairing.** Sort. The heaviest person needs a boat anyway; if the lightest fits too, they share. Move the pointers inward.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's stack.
''',
tc="nlogn", sc="log",
java=r'''
public class BoatsToSavePeople {

    public int numRescueBoats(int[] people, int limit) {
        int[] p = people.clone();
        Arrays.sort(p);
        int boats = 0;
        for (int l = 0, r = p.length - 1; l <= r; r--) {
            if (p[l] + p[r] <= limit) l++;
            boats++;
        }
        return boats;
    }
}
''',
test=r'''
class BoatsToSavePeopleTest {

    private final BoatsToSavePeople solution = new BoatsToSavePeople();

    @Test
    void examples() {
        assertEquals(1, solution.numRescueBoats(new int[]{1, 2}, 3));
        assertEquals(3, solution.numRescueBoats(new int[]{3, 2, 2, 1}, 3));
        assertEquals(4, solution.numRescueBoats(new int[]{3, 5, 3, 4}, 5));
    }
}
''',
trace=r'''
function run(people, limit) {
  const p = people.slice().sort((a, b) => a - b); let boats = 0; const hl = {};
  A.step(`Sort the weights. The heaviest person always needs a boat; the lightest joins if the pair weighs at most ${limit}.`, A.arr('weights', p));
  for (let l = 0, r = p.length - 1; l <= r; r--) {
    const pair = l < r && p[l] + p[r] <= limit; boats++;
    hl[r] = 'ok'; if (pair) hl[l] = 'ok';
    A.step(pair ? `${p[r]} and ${p[l]} share boat ${boats} (${p[l] + p[r]} ≤ ${limit}).` : `${p[r]} goes alone in boat ${boats}.`, A.arr('weights', p, { hl: { ...hl, [r]: 'cur', ...(pair ? { [l]: 'cur' } : {}) } }), A.vars({ boats }));
    if (p[l] + p[r] <= limit) l++;
  }
  A.step(`${boats} boats.`, A.text('Result', boats, 'ok'));
}
A.scenario('limit = 3', 'people = [3,2,2,1]', () => run([3, 2, 2, 1], 3));
'''),

P(num=912, slug="sort-an-array", title="Sort an Array", diff="Medium", topic="Sorting", cls="SortAnArray",
idea="Merge sort: split in half, sort both halves, merge them; always O(n log n).",
vname="Merge sort",
spec=r'''
Sort `nums` in ascending order **without** built-in sort functions, in O(n log n) time and with as little extra space as possible.

**Example**
```
[5,2,3,1] → [1,2,3,5],   [5,1,1,2,0,0] → [0,0,1,1,2,5]
```

**Constraints**
* `1 <= nums.length <= 5 * 10^4`
''',
approach=r'''
**Top-down merge sort** with one shared buffer: sort `[lo, mid]` and `[mid+1, hi]`, then merge them through the buffer.

* Time: **O(n log n)** — log n levels of linear merges.
* Space: **O(n)** — the buffer.
''',
tc="nlogn", sc="n",
java=r'''
public class SortAnArray {

    public int[] sortArray(int[] nums) {
        int[] a = nums.clone();
        sort(a, new int[a.length], 0, a.length - 1);
        return a;
    }

    private void sort(int[] a, int[] buf, int lo, int hi) {
        if (lo >= hi) return;
        int mid = (lo + hi) >>> 1;
        sort(a, buf, lo, mid);
        sort(a, buf, mid + 1, hi);
        int i = lo, j = mid + 1, k = lo;
        while (i <= mid && j <= hi) buf[k++] = a[i] <= a[j] ? a[i++] : a[j++];
        while (i <= mid) buf[k++] = a[i++];
        while (j <= hi) buf[k++] = a[j++];
        System.arraycopy(buf, lo, a, lo, hi - lo + 1);
    }
}
''',
test=r'''
class SortAnArrayTest {

    private final SortAnArray solution = new SortAnArray();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 2, 3, 5}, solution.sortArray(new int[]{5, 2, 3, 1}));
        assertArrayEquals(new int[]{0, 0, 1, 1, 2, 5}, solution.sortArray(new int[]{5, 1, 1, 2, 0, 0}));
    }

    @Test
    void random() {
        int[] a = new Random(5).ints(5000, -50000, 50000).toArray();
        int[] e = a.clone();
        Arrays.sort(e);
        assertArrayEquals(e, solution.sortArray(a));
    }
}
''',
trace=r'''
function run(nums) {
  const a = nums.slice();
  const sort = (lo, hi) => {
    if (lo >= hi) return;
    const mid = (lo + hi) >> 1; sort(lo, mid); sort(mid + 1, hi);
    const L = a.slice(lo, mid + 1), R = a.slice(mid + 1, hi + 1), m = []; let i = 0, j = 0;
    while (i < L.length && j < R.length) m.push(L[i] <= R[j] ? L[i++] : R[j++]); m.push(...L.slice(i), ...R.slice(j));
    m.forEach((v, t) => (a[lo + t] = v));
    A.step(`Merge [${L}] and [${R}] into [${m}].`, A.arr('nums', a, { range: [lo, hi], hl: Object.fromEntries(m.map((_, t) => [lo + t, 'ok'])) }));
  };
  A.step('Split the array in halves until single elements remain, then merge back up.', A.arr('nums', a));
  sort(0, a.length - 1);
}
A.scenario('Six numbers', 'nums = [5,1,1,2,0,0]', () => run([5, 1, 1, 2, 0, 0]));
''',
variants=[dict(
name="Heap sort (in place)",
idea="Build a max-heap in the array, then repeatedly swap the maximum to the end and repair the heap.",
approach=r'''
**Heap sort.** Heapify bottom-up; then for `end = n-1 .. 1`, swap `a[0]` with `a[end]` and sift the new root down within `[0, end)`.

* Time: **O(n log n)** — n sift-downs of O(log n).
* Space: **O(1)** — in place.
''',
tc="nlogn", sc="1",
java=r'''
public class SortAnArray {

    public int[] sortArray(int[] nums) {
        int[] a = nums.clone();
        int n = a.length;
        for (int i = n / 2 - 1; i >= 0; i--) siftDown(a, i, n);
        for (int end = n - 1; end > 0; end--) {
            swap(a, 0, end);
            siftDown(a, 0, end);
        }
        return a;
    }

    private static void siftDown(int[] a, int i, int n) {
        while (true) {
            int largest = i, l = 2 * i + 1, r = l + 1;
            if (l < n && a[l] > a[largest]) largest = l;
            if (r < n && a[r] > a[largest]) largest = r;
            if (largest == i) return;
            swap(a, i, largest);
            i = largest;
        }
    }

    private static void swap(int[] a, int i, int j) {
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
}
''',
trace=r'''
function run(nums) {
  const a = nums.slice(), n = a.length;
  const sift = (i, m) => { while (true) { let b = i; const l = 2 * i + 1, r = l + 1; if (l < m && a[l] > a[b]) b = l; if (r < m && a[r] > a[b]) b = r; if (b === i) return; [a[i], a[b]] = [a[b], a[i]]; i = b; } };
  for (let i = (n >> 1) - 1; i >= 0; i--) sift(i, n);
  A.step('Turn the array into a max-heap: every parent is at least its children.', A.arr('heap', a, { hl: { 0: 'alt' } }));
  for (let end = n - 1; end > 0; end--) { [a[0], a[end]] = [a[end], a[0]]; sift(0, end); A.step(`Move the maximum to position ${end} and repair the heap.`, A.arr('nums', a, { hl: Object.fromEntries(a.map((_, i) => [i, i >= end ? 'ok' : i === 0 ? 'alt' : ''])) })); }
}
A.scenario('Six numbers', 'nums = [5,1,1,2,0,0]', () => run([5, 1, 1, 2, 0, 0]));
''')]),

P(num=977, slug="squares-of-a-sorted-array", title="Squares of a Sorted Array", diff="Easy", topic="Two Pointers", cls="SquaresOfSortedArray",
idea="The largest square is at one of the two ends; fill the result from the back with two pointers.",
vname="Two pointers from both ends",
spec=r'''
Given a sorted array (which may contain negatives), return the squares of its values in sorted order, in O(n).

**Example**
```
[-4,-1,0,3,10] → [0,1,9,16,100],   [-7,-3,2,3,11] → [4,9,9,49,121]
```

**Constraints**
* `1 <= nums.length <= 10^4`
''',
approach=r'''
**Ends hold the extremes.** Compare `|nums[l]|` and `|nums[r]|`; write the larger square at the back of the output and move that pointer.

* Time: **O(n)** — one pass.
* Space: **O(1)** — apart from the output.
''',
java=r'''
public class SquaresOfSortedArray {

    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] out = new int[n];
        for (int l = 0, r = n - 1, k = n - 1; k >= 0; k--) {
            if (Math.abs(nums[l]) > Math.abs(nums[r])) out[k] = nums[l] * nums[l++];
            else out[k] = nums[r] * nums[r--];
        }
        return out;
    }
}
''',
test=r'''
class SquaresOfSortedArrayTest {

    private final SquaresOfSortedArray solution = new SquaresOfSortedArray();

    @Test
    void examples() {
        assertArrayEquals(new int[]{0, 1, 9, 16, 100}, solution.sortedSquares(new int[]{-4, -1, 0, 3, 10}));
        assertArrayEquals(new int[]{4, 9, 9, 49, 121}, solution.sortedSquares(new int[]{-7, -3, 2, 3, 11}));
    }
}
''',
trace=r'''
function run(a) {
  const n = a.length, out = new Array(n).fill(''); let l = 0, r = n - 1;
  for (let k = n - 1; k >= 0; k--) {
    const takeL = Math.abs(a[l]) > Math.abs(a[r]); const v = takeL ? a[l] : a[r];
    out[k] = v * v;
    A.step(`|${a[l]}| vs |${a[r]}|: ${v * v} is the largest remaining square; write it at position ${k}.`, A.arr('nums', a, { ptr: [[l, 'l'], [r, 'r']], hl: { [takeL ? l : r]: 'ok' } }), A.arr('squares', out, { hl: { [k]: 'ok' } }));
    if (takeL) l++; else r--;
  }
}
A.scenario('With negatives', 'nums = [-4,-1,0,3,10]', () => run([-4, -1, 0, 3, 10]));
'''),

P(num=997, slug="find-the-town-judge", title="Find the Town Judge", diff="Easy", topic="Graph General", cls="FindTheTownJudge",
idea="The judge is trusted by everyone else and trusts nobody: in-degree n − 1 and out-degree 0.",
vname="Trust score",
spec=r'''
In a town of `n` people, `trust[i] = [a, b]` means `a` trusts `b`. The judge trusts nobody, is trusted by everybody else, and there is
exactly one such person if any. Return the judge's label, or `-1`.

**Example**
```
n = 2, trust = [[1,2]]             → 2
n = 3, trust = [[1,3],[2,3]]       → 3
n = 3, trust = [[1,3],[2,3],[3,1]] → -1
```

**Constraints**
* `1 <= n <= 1000`
''',
approach=r'''
**Net trust score.** `score[b]++` for being trusted, `score[a]--` for trusting. Only the judge reaches `n - 1`.

* Time: **O(n + t)** — one pass over trust, one over people.
* Space: **O(n)** — the scores.
''',
java=r'''
public class FindTheTownJudge {

    public int findJudge(int n, int[][] trust) {
        int[] score = new int[n + 1];
        for (int[] t : trust) {
            score[t[0]]--;
            score[t[1]]++;
        }
        for (int p = 1; p <= n; p++) {
            if (score[p] == n - 1) return p;
        }
        return -1;
    }
}
''',
test=r'''
class FindTheTownJudgeTest {

    private final FindTheTownJudge solution = new FindTheTownJudge();

    @Test
    void examples() {
        assertEquals(2, solution.findJudge(2, new int[][]{{1, 2}}));
        assertEquals(3, solution.findJudge(3, new int[][]{{1, 3}, {2, 3}}));
        assertEquals(-1, solution.findJudge(3, new int[][]{{1, 3}, {2, 3}, {3, 1}}));
        assertEquals(1, solution.findJudge(1, new int[][]{}));
    }
}
''',
trace=r'''
function run(n, trust) {
  const nodes = [...Array(n)].map((_, i) => ({ id: i + 1, label: i + 1 })), score = new Array(n + 1).fill(0);
  trust.forEach(([a, b]) => { score[a]--; score[b]++; });
  A.step('Each arrow a → b means a trusts b. Score: +1 for being trusted, −1 for trusting someone.', A.graph('trust', nodes, trust.map(([a, b]) => [a, b]), { directed: true }), A.arr('score (by person)', score.slice(1)));
  const j = score.findIndex((s, p) => p > 0 && s === n - 1);
  A.step(j > 0 ? `Person ${j} has score ${n - 1}: trusted by everyone else, trusting no one. The judge.` : `Nobody reaches ${n - 1}, so there is no judge.`, A.graph('trust', nodes, trust.map(([a, b]) => [a, b]), { directed: true, hl: j > 0 ? { [j]: 'ok' } : {} }), A.text('Result', j > 0 ? j : -1, j > 0 ? 'ok' : 'bad'));
}
A.scenario('Judge exists', 'n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]', () => run(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]));
'''),
]
