PROBLEMS = [
P(num=111, slug="minimum-depth-of-binary-tree", title="Minimum Depth of Binary Tree", diff="Easy", topic="Binary Tree BFS", cls="MinimumDepth",
idea="Breadth-first search stops at the first leaf it meets: that leaf is on the shallowest level.",
vname="BFS to the first leaf", helpers=["TreeNode"],
spec=r'''
Return the **minimum depth** of a binary tree: the number of nodes on the shortest path from the root down to a **leaf** (a node with no
children).

**Example**
```
[3,9,20,null,null,15,7]          → 2
[2,null,3,null,4,null,5,null,6]  → 5
```

**Constraints**
* `0 <= n <= 10^5`
''',
approach=r'''
**Level-order search.** Process the tree level by level; the first leaf found ends the search, so deeper levels are never visited.
(A plain `min(left, right)` recursion is wrong when one child is missing.)

* Time: **O(n)** — in the worst case all nodes are visited, but usually far fewer.
* Space: **O(w)** — the widest level in the queue.
''',
tc="n", sc="n",
java=r'''
public class MinimumDepth {

    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        for (int depth = 1; ; depth++) {
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                if (n.left == null && n.right == null) return depth;
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
        }
    }
}
''',
test=r'''
class MinimumDepthTest {

    private final MinimumDepth solution = new MinimumDepth();

    @Test
    void examples() {
        assertEquals(2, solution.minDepth(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertEquals(5, solution.minDepth(TreeNode.of(2, null, 3, null, 4, null, 5, null, 6)));
        assertEquals(0, solution.minDepth(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {}; let q = [root];
  for (let d = 1; q.length; d++) {
    const leaf = q.find(n => !n.left && !n.right);
    q.forEach(n => (hl[n.id] = n === leaf ? 'ok' : 'sel'));
    if (leaf) { A.step(`Level ${d}: ${leaf.val} has no children, so it is a leaf. The minimum depth is ${d}; deeper levels are never visited.`, A.tree('tree', root, { hl }), A.text('Result', d, 'ok')); return; }
    A.step(`Level ${d}: ${q.map(n => n.val).join(', ')} all have children. Go one level deeper.`, A.tree('tree', root, { hl }));
    q = q.flatMap(n => [n.left, n.right].filter(Boolean));
  }
}
A.scenario('Shallow leaf', '[3,9,20,null,null,15,7]', () => run([3, 9, 20, null, null, 15, 7]));
A.scenario('Chain', '[2,null,3,null,4]', () => run([2, null, 3, null, 4]));
'''),

P(num=113, slug="path-sum-ii", title="Path Sum II", diff="Medium", topic="Backtracking", cls="PathSumII",
idea="DFS with a running path; at each leaf whose remaining sum is zero, copy the path into the answer.",
vname="DFS with backtracking", helpers=["TreeNode"],
spec=r'''
Return every **root-to-leaf** path whose node values add up to `targetSum`, each as a list of values.

**Example**
```
root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
→ [[5,4,11,2],[5,8,4,5]]
```

**Constraints**
* `0 <= n <= 5000`
''',
approach=r'''
**Backtracking.** Push the node onto the path and subtract its value. At a leaf with remaining 0, record a copy. Recurse into children,
then pop the node.

* Time: **O(n · h)** — each node is visited once; copying a path costs O(h).
* Space: **O(h)** — the path and the recursion stack.
''',
tc="n2", sc="n",
java=r'''
public class PathSumII {

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> out = new ArrayList<>();
        dfs(root, targetSum, new ArrayList<>(), out);
        return out;
    }

    private void dfs(TreeNode n, int remaining, List<Integer> path, List<List<Integer>> out) {
        if (n == null) return;
        path.add(n.val);
        remaining -= n.val;
        if (n.left == null && n.right == null && remaining == 0) out.add(new ArrayList<>(path));
        dfs(n.left, remaining, path, out);
        dfs(n.right, remaining, path, out);
        path.removeLast();
    }
}
''',
test=r'''
class PathSumIITest {

    private final PathSumII solution = new PathSumII();

    @Test
    void example() {
        assertEquals(List.of(List.of(5, 4, 11, 2), List.of(5, 8, 4, 5)),
                solution.pathSum(TreeNode.of(5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1), 22));
    }

    @Test
    void none() {
        assertEquals(List.of(), solution.pathSum(TreeNode.of(1, 2, 3), 5));
    }
}
''',
trace=r'''
function run(arr, target) {
  const root = A.mkTree(arr), path = [], out = [];
  (function dfs(n, rem) {
    if (!n) return;
    path.push(n); rem -= n.val;
    const leaf = !n.left && !n.right, hit = leaf && rem === 0;
    if (hit) out.push('[' + path.map(x => x.val) + ']');
    if (leaf) A.step(`Leaf ${n.val}: ${rem} remains. ${hit ? 'A match: record the path.' : 'Not a match.'}`, A.tree('tree', root, { hl: Object.fromEntries(path.map(x => [x.id, hit ? 'ok' : 'sel']).concat(hit ? [] : [[n.id, 'bad']])) }), A.arr('paths', out));
    dfs(n.left, rem); dfs(n.right, rem); path.pop();
  })(root, target);
  A.step(`${out.length} path${out.length === 1 ? '' : 's'} found.`, A.arr('paths', out, { hl: out.map((_, i) => [i, 'ok']) }));
}
A.scenario('Two paths', 'targetSum = 22', () => run([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], 22));
'''),

P(num=118, slug="pascals-triangle", title="Pascal's Triangle", diff="Easy", topic="1D DP", cls="PascalsTriangle",
idea="Each inner value is the sum of the two values above it; every row starts and ends with 1.",
vname="Row by row",
spec=r'''
Return the first `numRows` rows of Pascal's triangle.

**Example**
```
numRows = 5 → [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**Constraints**
* `1 <= numRows <= 30`
''',
approach=r'''
**Build from the previous row.** Row `i` has `i + 1` values: 1 at both ends, `prev[j-1] + prev[j]` in between.

* Time: **O(n²)** — n rows of up to n values.
* Space: **O(1)** — apart from the output.
''',
tc="n2", sc="1",
java=r'''
public class PascalsTriangle {

    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> rows = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j <= i; j++) {
                row.add(j == 0 || j == i ? 1 : rows.get(i - 1).get(j - 1) + rows.get(i - 1).get(j));
            }
            rows.add(row);
        }
        return rows;
    }
}
''',
test=r'''
class PascalsTriangleTest {

    private final PascalsTriangle solution = new PascalsTriangle();

    @Test
    void five() {
        assertEquals(List.of(List.of(1), List.of(1, 1), List.of(1, 2, 1), List.of(1, 3, 3, 1), List.of(1, 4, 6, 4, 1)), solution.generate(5));
    }

    @Test
    void one() {
        assertEquals(List.of(List.of(1)), solution.generate(1));
    }
}
''',
trace=r'''
function run(n) {
  const g = [...Array(n)].map(() => new Array(n).fill(''));
  for (let i = 0; i < n; i++) for (let j = 0; j <= i; j++) {
    g[i][j] = j === 0 || j === i ? 1 : g[i - 1][j - 1] + g[i - 1][j];
    A.step(j === 0 || j === i ? `Row ${i}: the edge value is 1.` : `Row ${i}, position ${j}: ${g[i - 1][j - 1]} + ${g[i - 1][j]} = ${g[i][j]}.`, A.grid('triangle', g, { hl: { [`${i},${j}`]: 'cur', ...(j && j < i ? { [`${i - 1},${j - 1}`]: 'sel', [`${i - 1},${j}`]: 'sel' } : {}) } }));
  }
}
A.scenario('Five rows', 'numRows = 5', () => run(5));
'''),

P(num=115, slug="distinct-subsequences", title="Distinct Subsequences", diff="Hard", topic="Multidimensional DP", cls="DistinctSubsequences",
idea="ways[j] = number of ways to form t[..j) from the characters seen so far; a matching character adds ways[j−1].",
vname="1D DP",
spec=r'''
Return the number of distinct **subsequences** of `s` that equal `t` (the answer fits in 32 bits).

**Example**
```
s = "rabbbit", t = "rabbit" → 3
s = "babgbag", t = "bag"    → 5
```

**Constraints**
* `1 <= s.length, t.length <= 1000`
''',
approach=r'''
**Rolling DP.** `ways[0] = 1` (the empty prefix of `t`). For each character `c` of `s`, go through `j` from high to low: if `t[j-1] == c`,
then `ways[j] += ways[j-1]` (use `c` as the j-th character). Going right to left uses each `c` at most once per subsequence.

* Time: **O(m·n)** — every pair of positions.
* Space: **O(n)** — one row (n = t.length).
''',
tc="n2", sc="n",
java=r'''
public class DistinctSubsequences {

    public int numDistinct(String s, String t) {
        int n = t.length();
        long[] ways = new long[n + 1];
        ways[0] = 1;
        for (char c : s.toCharArray()) {
            for (int j = n; j >= 1; j--) {
                if (t.charAt(j - 1) == c) ways[j] += ways[j - 1];
            }
        }
        return (int) ways[n];
    }
}
''',
test=r'''
class DistinctSubsequencesTest {

    private final DistinctSubsequences solution = new DistinctSubsequences();

    @ParameterizedTest
    @CsvSource({"rabbbit,rabbit,3", "babgbag,bag,5", "abc,abcd,0", "aaa,a,3"})
    void counts(String s, String t, int expected) {
        assertEquals(expected, solution.numDistinct(s, t));
    }
}
''',
trace=r'''
function run(s, t) {
  const n = t.length, ways = [1, ...new Array(n).fill(0)];
  A.step(`ways[j] counts ways to build the first j letters of "${t}" from the letters of s read so far. ways[0] = 1.`, A.chars('s', s), A.arr('ways (by prefix of t)', ways));
  [...s].forEach((c, i) => {
    const hl = {};
    for (let j = n; j >= 1; j--) if (t[j - 1] === c) { ways[j] += ways[j - 1]; hl[j] = 'ok'; }
    A.step(`Read '${c}'. ${Object.keys(hl).length ? `It can extend prefixes ending before each '${c}' in t.` : `'${c}' does not occur in t.`}`, A.chars('s', s, { hl: { [i]: 'cur' } }), A.chars('t', t, { hl: Object.fromEntries(Object.keys(hl).map(j => [j - 1, 'sel'])) }), A.arr('ways (by prefix of t)', ways, { hl }));
  });
  A.step(`${ways[n]} distinct subsequences.`, A.text('Result', ways[n], 'ok'));
}
A.scenario('bag in babgbag', 's = "babgbag", t = "bag"', () => run('babgbag', 'bag'));
'''),

P(num=142, slug="linked-list-cycle-ii", title="Linked List Cycle II", diff="Medium", topic="Linked List", cls="LinkedListCycleII",
idea="After slow and fast meet, a pointer from the head and one from the meeting point reach the cycle start together.",
vname="Floyd: meet, then find the entrance", helpers=["ListNode"],
spec=r'''
Return the node where the cycle in a linked list begins, or `null` if there is no cycle. Do not modify the list.

**Example**
```
3 → 2 → 0 → -4 → (back to 2)   → the node with value 2
1 → 2 → (back to 1)            → the node with value 1
```

**Constraints**
* `0 <= n <= 10^4`

**Follow-up:** O(1) memory.
''',
approach=r'''
**Floyd's algorithm, phase 2.** Let `a` be the distance from the head to the cycle start. When slow and fast meet, slow has walked
`a + b`, fast `2(a + b)`, so `a + b` is a multiple of the cycle length. Walking `a` more steps from the meeting point therefore lands on
the cycle start, exactly when a pointer from the head gets there.

* Time: **O(n)** — two linear phases.
* Space: **O(1)** — two pointers.
''',
java=r'''
public class LinkedListCycleII {

    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                for (ListNode p = head; ; p = p.next, slow = slow.next) {
                    if (p == slow) return p;
                }
            }
        }
        return null;
    }
}
''',
test=r'''
class LinkedListCycleIITest {

    private final LinkedListCycleII solution = new LinkedListCycleII();

    private static ListNode[] build(int pos, int... values) {
        ListNode[] nodes = new ListNode[values.length];
        for (int i = 0; i < values.length; i++) nodes[i] = new ListNode(values[i]);
        for (int i = 0; i + 1 < values.length; i++) nodes[i].next = nodes[i + 1];
        if (pos >= 0) nodes[values.length - 1].next = nodes[pos];
        return nodes;
    }

    @Test
    void cycle() {
        ListNode[] n = build(1, 3, 2, 0, -4);
        assertSame(n[1], solution.detectCycle(n[0]));
        ListNode[] m = build(0, 1, 2);
        assertSame(m[0], solution.detectCycle(m[0]));
    }

    @Test
    void noCycle() {
        assertNull(solution.detectCycle(build(-1, 1, 2, 3)[0]));
    }
}
''',
trace=r'''
function run(vals, pos) {
  const n = vals.length, nx = i => (i + 1 < n ? i + 1 : pos), note = `back to ${vals[pos]}`;
  let slow = 0, fast = 0;
  do { slow = nx(slow); fast = nx(nx(fast)); A.step(`Phase 1: slow → ${vals[slow]}, fast → ${vals[fast]}.`, A.list('list', vals, { ptr: [[slow, 'slow'], [fast, 'fast']], note })); } while (slow !== fast);
  A.step(`They meet at ${vals[slow]}. Phase 2: start p at the head and move p and slow one step at a time.`, A.list('list', vals, { ptr: [[0, 'p'], [slow, 'slow']], hl: { [slow]: 'sel' }, note }));
  let p = 0;
  while (p !== slow) { p = nx(p); slow = nx(slow); A.step(`p → ${vals[p]}, slow → ${vals[slow]}.`, A.list('list', vals, { ptr: [[p, 'p'], [slow, 'slow']], note })); }
  A.step(`They meet at ${vals[p]}: the start of the cycle.`, A.list('list', vals, { hl: { [p]: 'ok' }, note }), A.text('Result', `node ${vals[p]} (index ${p})`, 'ok'));
}
A.scenario('Cycle at index 2', '1→2→3→4→5→6 → back to 3', () => run([1, 2, 3, 4, 5, 6], 2));
''',
variants=[dict(
name="Visited-node set",
idea="The first node visited twice is the start of the cycle.",
approach=r'''
**`MyHashSet` of nodes.** Walk the list; the first node already in the set is where the cycle begins.

* Time: **O(n)** — each node once.
* Space: **O(n)** — the set.
''',
java=r'''
public class LinkedListCycleII {

    public ListNode detectCycle(ListNode head) {
        MyHashSet<ListNode> seen = new MyHashSet<>();
        for (ListNode n = head; n != null; n = n.next) {
            if (!seen.add(n)) return n;
        }
        return null;
    }
}
''',
trace=r'''
function run(vals, pos) {
  const n = vals.length, seen = new Set();
  for (let i = 0; ; i = i + 1 < n ? i + 1 : pos) {
    if (seen.has(i)) { A.step(`Node ${vals[i]} is visited a second time: the cycle starts here.`, A.list('list', vals, { hl: { [i]: 'ok' }, note: `back to ${vals[pos]}` }), A.text('Result', vals[i], 'ok')); return; }
    seen.add(i);
    A.step(`Visit ${vals[i]}.`, A.list('list', vals, { hl: Object.fromEntries([...seen].map(k => [k, k === i ? 'cur' : 'sel'])), note: `back to ${vals[pos]}` }), A.hashTable('visited', new Set([...seen].map(k => 'node' + vals[k]))));
  }
}
A.scenario('Cycle at index 2', '1→2→3→4→5→6 → back to 3', () => run([1, 2, 3, 4, 5, 6], 2));
''')]),

P(num=143, slug="reorder-list", title="Reorder List", diff="Medium", topic="Linked List", cls="ReorderList",
idea="Split at the middle, reverse the second half, then weave the two halves together.",
vname="Split, reverse, merge", helpers=["ListNode"],
spec=r'''
Reorder `L0 → L1 → … → Ln` into `L0 → Ln → L1 → Ln-1 → L2 → …` in place (re-link nodes, do not change values).

**Example**
```
1 → 2 → 3 → 4       becomes 1 → 4 → 2 → 3
1 → 2 → 3 → 4 → 5   becomes 1 → 5 → 2 → 4 → 3
```

**Constraints**
* `1 <= n <= 5 * 10^4`
''',
approach=r'''
**Three linear steps.** Find the middle with slow/fast pointers and cut the list there; reverse the second half; then alternately take one
node from each half.

* Time: **O(n)** — three passes.
* Space: **O(1)** — pointers only.
''',
java=r'''
public class ReorderList {

    public void reorderList(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode second = null, cur = slow.next;
        slow.next = null;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = second;
            second = cur;
            cur = next;
        }
        for (ListNode first = head; second != null; ) {
            ListNode n1 = first.next, n2 = second.next;
            first.next = second;
            second.next = n1;
            first = n1;
            second = n2;
        }
    }
}
''',
test=r'''
class ReorderListTest {

    private final ReorderList solution = new ReorderList();

    private int[] reorder(int... v) {
        ListNode head = ListNode.of(v);
        solution.reorderList(head);
        return ListNode.toArray(head);
    }

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 4, 2, 3}, reorder(1, 2, 3, 4));
        assertArrayEquals(new int[]{1, 5, 2, 4, 3}, reorder(1, 2, 3, 4, 5));
        assertArrayEquals(new int[]{1}, reorder(1));
    }
}
''',
trace=r'''
function run(vals) {
  const mid = Math.ceil(vals.length / 2), first = vals.slice(0, mid), second = vals.slice(mid);
  A.step(`Find the middle with slow and fast pointers and cut the list into two halves.`, A.list('first half', first, { hl: first.map((_, i) => [i, 'sel']) }), A.list('second half', second, { hl: second.map((_, i) => [i, 'alt']) }));
  second.reverse();
  A.step('Reverse the second half.', A.list('first half', first), A.list('second half (reversed)', second, { hl: second.map((_, i) => [i, 'alt']) }));
  const out = [];
  for (let i = 0; i < first.length; i++) { out.push(first[i]); if (i < second.length) out.push(second[i]); A.step(`Take ${first[i]} from the first half${i < second.length ? `, then ${second[i]} from the second` : ''}.`, A.list('result', out, { hl: { [out.length - 1]: 'ok' } })); }
}
A.scenario('Five nodes', '1→2→3→4→5', () => run([1, 2, 3, 4, 5]));
'''),

P(num=152, slug="maximum-product-subarray", title="Maximum Product Subarray", diff="Medium", topic="1D DP", cls="MaximumProductSubarray",
idea="Track both the largest and smallest product ending here: a negative number swaps their roles.",
vname="Max and min running products",
spec=r'''
Return the largest product of a contiguous non-empty subarray of `nums` (it fits in 32 bits).

**Example**
```
[2,3,-2,4] → 6,   [-2,0,-1] → 0,   [-2,3,-4] → 24
```

**Constraints**
* `1 <= nums.length <= 2 * 10^4`; `-10 <= nums[i] <= 10`
''',
approach=r'''
**Kadane with two values.** `hi` and `lo` are the largest and smallest products of a subarray ending at `i`. For a negative `x`, swap
them first. Then `hi = max(x, hi·x)`, `lo = min(x, lo·x)`, and track the best `hi`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — three numbers.
''',
java=r'''
public class MaximumProductSubarray {

    public int maxProduct(int[] nums) {
        int hi = nums[0], lo = nums[0], best = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int x = nums[i];
            if (x < 0) {
                int t = hi;
                hi = lo;
                lo = t;
            }
            hi = Math.max(x, hi * x);
            lo = Math.min(x, lo * x);
            best = Math.max(best, hi);
        }
        return best;
    }
}
''',
test=r'''
class MaximumProductSubarrayTest {

    private final MaximumProductSubarray solution = new MaximumProductSubarray();

    @Test
    void examples() {
        assertEquals(6, solution.maxProduct(new int[]{2, 3, -2, 4}));
        assertEquals(0, solution.maxProduct(new int[]{-2, 0, -1}));
        assertEquals(24, solution.maxProduct(new int[]{-2, 3, -4}));
    }

    @Test
    void single() {
        assertEquals(-3, solution.maxProduct(new int[]{-3}));
    }
}
''',
trace=r'''
function run(a) {
  let hi = a[0], lo = a[0], best = a[0];
  A.step('hi and lo are the largest and smallest products of a subarray ending at the current index. A negative number turns the smallest into the largest.', A.arr('nums', a, { hl: { 0: 'cur' } }), A.vars({ hi, lo, best }));
  for (let i = 1; i < a.length; i++) {
    const x = a[i]; let swapped = false;
    if (x < 0) { [hi, lo] = [lo, hi]; swapped = true; }
    hi = Math.max(x, hi * x); lo = Math.min(x, lo * x); best = Math.max(best, hi);
    A.step(`${x}${swapped ? ' is negative, so hi and lo swap first' : ''}: hi = ${hi}, lo = ${lo}. Best: ${best}.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.vars({ hi, lo, best }));
  }
  A.step(`The maximum product is ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Two negatives', 'nums = [-2,3,-4]', () => run([-2, 3, -4]));
A.scenario('Classic', 'nums = [2,3,-2,4]', () => run([2, 3, -2, 4]));
'''),

P(num=160, slug="intersection-of-two-linked-lists", title="Intersection of Two Linked Lists", diff="Easy", topic="Linked List", cls="IntersectionOfTwoLists",
idea="Two pointers walk A then B and B then A; after equal total distances they meet at the intersection (or both reach null).",
vname="Switching pointers", helpers=["ListNode"],
spec=r'''
Two singly linked lists may merge into a shared tail. Return the first shared **node**, or `null` if they do not intersect. Do not modify
the lists.

**Example**
```
A: 4 → 1 ↘
            8 → 4 → 5
B: 5 → 6 → 1 ↗          → the node with value 8
```

**Constraints**
* `1 <= m, n <= 3 * 10^4`

**Follow-up:** O(m + n) time and O(1) memory.
''',
approach=r'''
**Equalize the distances.** `p` walks A then B; `q` walks B then A. Each travels `a + c + b` steps before reaching the intersection
(where `c` is the shared length), so they arrive together, or both reach `null` if there is no intersection.

* Time: **O(m + n)** — each pointer walks both lists once.
* Space: **O(1)** — two pointers.
''',
java=r'''
public class IntersectionOfTwoLists {

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode p = headA, q = headB;
        while (p != q) {
            p = p == null ? headB : p.next;
            q = q == null ? headA : q.next;
        }
        return p;
    }
}
''',
test=r'''
class IntersectionOfTwoListsTest {

    private final IntersectionOfTwoLists solution = new IntersectionOfTwoLists();

    @Test
    void shared() {
        ListNode shared = ListNode.of(8, 4, 5);
        ListNode a = new ListNode(4, new ListNode(1, shared));
        ListNode b = new ListNode(5, new ListNode(6, new ListNode(1, shared)));
        assertSame(shared, solution.getIntersectionNode(a, b));
    }

    @Test
    void disjoint() {
        assertNull(solution.getIntersectionNode(ListNode.of(2, 6, 4), ListNode.of(1, 5)));
    }
}
''',
trace=r'''
function run(aOnly, bOnly, shared) {
  const A1 = [...aOnly, ...shared], B1 = [...bOnly, ...shared];
  const pathP = [...A1.map((v, i) => ['A', i]), ['null', 0], ...B1.map((v, i) => ['B', i])], pathQ = [...B1.map((v, i) => ['B', i]), ['null', 0], ...A1.map((v, i) => ['A', i])];
  const same = (x, y) => { const sx = x[0] === 'A' ? x[1] - aOnly.length : x[0] === 'B' ? x[1] - bOnly.length : -9; const sy = y[0] === 'A' ? y[1] - aOnly.length : y[0] === 'B' ? y[1] - bOnly.length : -9; return sx >= 0 && sx === sy; };
  A.step(`List A has ${aOnly.length} nodes of its own, list B has ${bOnly.length}; they share ${shared.length}. p walks A then B; q walks B then A.`, A.list('A', A1, { hl: Object.fromEntries(shared.map((_, i) => [aOnly.length + i, 'alt'])) }), A.list('B', B1, { hl: Object.fromEntries(shared.map((_, i) => [bOnly.length + i, 'alt'])) }));
  for (let s = 0; s < pathP.length; s++) {
    const p = pathP[s], q = pathQ[s];
    const ptrA = [], ptrB = [];
    if (p[0] === 'A') ptrA.push([p[1], 'p']); if (p[0] === 'B') ptrB.push([p[1], 'p']);
    if (q[0] === 'A') ptrA.push([q[1], 'q']); if (q[0] === 'B') ptrB.push([q[1], 'q']);
    const meet = same(p, q);
    A.step(meet ? `p and q are on the same node, ${shared[p[0] === 'A' ? p[1] - aOnly.length : p[1] - bOnly.length]}: the intersection.` : `Step ${s}: ${p[0] === 'null' ? 'p reached the end and jumps to B' : 'p moves on'}; ${q[0] === 'null' ? 'q reached the end and jumps to A' : 'q moves on'}.`, A.list('A', A1, { ptr: ptrA }), A.list('B', B1, { ptr: ptrB }));
    if (meet) { A.step('Both pointers walked the same total distance, so they arrived together.', A.text('Result', 'node ' + shared[0], 'ok')); return; }
  }
}
A.scenario('Shared tail', 'A = 4→1→[8→4→5], B = 5→6→1→[8→4→5]', () => run([4, 1], [5, 6, 1], [8, 4, 5]));
'''),

P(num=234, slug="palindrome-linked-list", title="Palindrome Linked List", diff="Easy", topic="Linked List", cls="PalindromeLinkedList",
idea="Reverse the second half in place and compare it with the first half.",
vname="Reverse second half", helpers=["ListNode"],
spec=r'''
Return `true` if a singly linked list reads the same forward and backward.

**Example**
```
1 → 2 → 2 → 1 → true,   1 → 2 → false
```

**Constraints**
* `1 <= n <= 10^5`

**Follow-up:** O(n) time and O(1) space.
''',
approach=r'''
**Half reversal.** Find the middle with slow/fast pointers, reverse the second half, then walk both halves comparing values.

* Time: **O(n)** — a few linear passes.
* Space: **O(1)** — pointers only.
''',
java=r'''
public class PalindromeLinkedList {

    public boolean isPalindrome(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode prev = null;
        while (slow != null) {
            ListNode next = slow.next;
            slow.next = prev;
            prev = slow;
            slow = next;
        }
        for (ListNode a = head, b = prev; b != null; a = a.next, b = b.next) {
            if (a.val != b.val) return false;
        }
        return true;
    }
}
''',
test=r'''
class PalindromeLinkedListTest {

    private final PalindromeLinkedList solution = new PalindromeLinkedList();

    @Test
    void examples() {
        assertTrue(solution.isPalindrome(ListNode.of(1, 2, 2, 1)));
        assertFalse(solution.isPalindrome(ListNode.of(1, 2)));
        assertTrue(solution.isPalindrome(ListNode.of(1, 2, 3, 2, 1)));
    }
}
''',
trace=r'''
function run(vals) {
  const half2 = vals.slice(Math.ceil(vals.length / 2)).reverse();
  A.step('Find the middle and reverse the second half.', A.list('first half', vals.slice(0, vals.length - half2.length)), A.list('second half reversed', half2, { hl: half2.map((_, i) => [i, 'alt']) }));
  for (let i = 0; i < half2.length; i++) {
    const ok = vals[i] === half2[i];
    A.step(`${vals[i]} vs ${half2[i]}: ${ok ? 'equal' : 'different'}.`, A.list('first half', vals.slice(0, vals.length - half2.length), { hl: { [i]: ok ? 'ok' : 'bad' } }), A.list('second half reversed', half2, { hl: { [i]: ok ? 'ok' : 'bad' } }));
    if (!ok) { A.step('Not a palindrome.', A.text('Result', 'false', 'bad')); return; }
  }
  A.step('All pairs matched: a palindrome.', A.text('Result', 'true', 'ok'));
}
A.scenario('Odd length', '1→2→3→2→1', () => run([1, 2, 3, 2, 1]));
A.scenario('Not a palindrome', '1→2→3→1', () => run([1, 2, 3, 1]));
'''),

P(num=24, slug="swap-nodes-in-pairs", title="Swap Nodes in Pairs", diff="Medium", topic="Linked List", cls="SwapNodesInPairs",
idea="With a dummy head, repeatedly re-link the next two nodes in swapped order.",
vname="Iterative re-linking", helpers=["ListNode"],
spec=r'''
Swap every two adjacent nodes of a linked list and return its head. Change the links, not the values.

**Example**
```
1 → 2 → 3 → 4 becomes 2 → 1 → 4 → 3,   1 stays 1,   (empty) stays empty
```

**Constraints**
* `0 <= n <= 100`
''',
approach=r'''
**Dummy + pointer.** `prev` sits before a pair `a → b`. Re-link as `prev → b → a → (rest)` and move `prev` to `a`.

* Time: **O(n)** — each pair once.
* Space: **O(1)** — pointers only.
''',
java=r'''
public class SwapNodesInPairs {

    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0, head), prev = dummy;
        while (prev.next != null && prev.next.next != null) {
            ListNode a = prev.next, b = a.next;
            a.next = b.next;
            b.next = a;
            prev.next = b;
            prev = a;
        }
        return dummy.next;
    }
}
''',
test=r'''
class SwapNodesInPairsTest {

    private final SwapNodesInPairs solution = new SwapNodesInPairs();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 1, 4, 3}, ListNode.toArray(solution.swapPairs(ListNode.of(1, 2, 3, 4))));
        assertArrayEquals(new int[]{2, 1, 3}, ListNode.toArray(solution.swapPairs(ListNode.of(1, 2, 3))));
        assertNull(solution.swapPairs(null));
    }
}
''',
trace=r'''
function run(vals) {
  const a = vals.slice();
  A.step('Swap the nodes two at a time.', A.list('list', a));
  for (let i = 0; i + 1 < a.length; i += 2) { [a[i], a[i + 1]] = [a[i + 1], a[i]]; A.step(`Re-link the pair so ${a[i]} comes before ${a[i + 1]}.`, A.list('list', a, { hl: { [i]: 'ok', [i + 1]: 'ok' } })); }
  A.step(a.length % 2 ? 'The last node has no partner and stays where it is.' : 'All pairs are swapped.', A.text('Result', a.join(' → '), 'ok'));
}
A.scenario('Five nodes', '1→2→3→4→5', () => run([1, 2, 3, 4, 5]));
'''),
]
