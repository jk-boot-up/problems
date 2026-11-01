NARY_LAYOUT = r'''
function nary(spec) {
  const nodes = [], edges = []; let slot = 0, id = 0;
  (function place(t, d, parent) {
    const me = id++, node = { id: me, label: t.v, depth: d };
    nodes.push(node);
    if (parent !== null) edges.push([parent, me]);
    const kids = (t.c || []).map(k => place(k, d + 1, me));
    node.x = kids.length ? (kids[0].x + kids[kids.length - 1].x) / 2 : 40 + 60 * slot++;
    node.y = 40 + 70 * d;
    node.spec = t;
    return node;
  })(spec, 0, null);
  return { nodes, edges };
}
'''

NODE_CLASS = r'''
    public static final class Node {
        public int val;
        public List<Node> children;

        public Node(int val, Node... children) {
            this.val = val;
            this.children = new ArrayList<>(List.of(children));
        }
    }
'''

PROBLEMS = [
P(num=513, slug="find-bottom-left-tree-value", title="Find Bottom Left Tree Value", diff="Medium", topic="Binary Tree BFS", cls="BottomLeftValue",
idea="Do a BFS that visits each level right to left; the very last node dequeued is the bottom-left one.",
vname="Right-to-left BFS", helpers=["TreeNode"],
spec=r'''
Return the leftmost value in the **last** row of a binary tree.

**Example**
```
[2,1,3]                          → 1
[1,2,3,4,null,5,6,null,null,7]   → 7
```

**Constraints**
* `1 <= n <= 10^4`
''',
approach=r'''
**Reverse BFS.** Enqueue the right child before the left child. Then the last node dequeued is in the deepest level and is its leftmost
node.

* Time: **O(n)**.
* Space: **O(w)** — the widest level.
''',
tc="n", sc="n",
java=r'''
public class BottomLeftValue {

    public int findBottomLeftValue(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        TreeNode node = root;
        while (!queue.isEmpty()) {
            node = queue.poll();
            if (node.right != null) queue.add(node.right);
            if (node.left != null) queue.add(node.left);
        }
        return node.val;
    }
}
''',
test=r'''
class BottomLeftValueTest {

    private final BottomLeftValue solution = new BottomLeftValue();

    @Test
    void examples() {
        assertEquals(1, solution.findBottomLeftValue(TreeNode.of(2, 1, 3)));
        assertEquals(7, solution.findBottomLeftValue(TreeNode.of(1, 2, 3, 4, null, 5, 6, null, null, 7)));
        assertEquals(5, solution.findBottomLeftValue(TreeNode.of(5)));
        assertEquals(3, solution.findBottomLeftValue(TreeNode.of(1, null, 2, null, 3)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), q = [root], hl = {}; let last = root;
  A.step('BFS, but push the right child before the left. The last node out is the leftmost node of the deepest row.', A.tree('tree', root), A.arr('queue', [root.val]));
  while (q.length) {
    last = q.shift(); hl[last.id] = 'dim';
    if (last.right) q.push(last.right); if (last.left) q.push(last.left);
    A.step(`Dequeue ${last.val}; enqueue ${[last.right, last.left].filter(Boolean).map(n => n.val).join(' then ') || 'nothing'}.`, A.tree('tree', root, { hl: { ...hl, [last.id]: 'cur' } }), A.arr('queue', q.map(n => n.val)));
  }
  A.step(`The last node dequeued is ${last.val}.`, A.tree('tree', root, { hl: { [last.id]: 'ok' } }), A.text('Result', last.val, 'ok'));
}
A.scenario('Deep left', '[1,2,3,4,null,5,6,null,null,7]', () => run([1, 2, 3, 4, null, 5, 6, null, null, 7]));
'''),

P(num=515, slug="find-largest-value-in-each-tree-row", title="Find Largest Value in Each Tree Row", diff="Medium", topic="Binary Tree BFS", cls="LargestValuePerRow",
idea="Level-order traversal, keeping the maximum of each level.",
vname="BFS with a level maximum", helpers=["TreeNode"],
spec=r'''
Return the largest value in each row of a binary tree, from top to bottom.

**Example**
```
[1,3,2,5,3,null,9] → [1,3,9]
[1,2,3]            → [1,3]
```

**Constraints**
* `0 <= n <= 10^4`
''',
approach=r'''
**Level by level.** Process the queue one level at a time (its size at the start of the level) and track the maximum.

* Time: **O(n)**.
* Space: **O(w)** — the widest level.
''',
tc="n", sc="n",
java=r'''
public class LargestValuePerRow {

    public List<Integer> largestValues(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        while (!queue.isEmpty()) {
            int best = Integer.MIN_VALUE;
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                best = Math.max(best, n.val);
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
            out.add(best);
        }
        return out;
    }
}
''',
test=r'''
class LargestValuePerRowTest {

    private final LargestValuePerRow solution = new LargestValuePerRow();

    @Test
    void examples() {
        assertEquals(List.of(1, 3, 9), solution.largestValues(TreeNode.of(1, 3, 2, 5, 3, null, 9)));
        assertEquals(List.of(1, 3), solution.largestValues(TreeNode.of(1, 2, 3)));
        assertEquals(List.of(), solution.largestValues(null));
        assertEquals(List.of(Integer.MIN_VALUE), solution.largestValues(TreeNode.of(Integer.MIN_VALUE)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), out = []; let q = [root];
  A.step('Walk the tree one row at a time.', A.tree('tree', root));
  while (q.length) {
    const best = Math.max(...q.map(n => n.val)), hl = {};
    q.forEach(n => (hl[n.id] = n.val === best ? 'ok' : 'cur')); out.push(best);
    A.step(`Row [${q.map(n => n.val)}]: the largest is ${best}.`, A.tree('tree', root, { hl }), A.arr('row maxima', out, { hl: { [out.length - 1]: 'ok' } }));
    q = q.flatMap(n => [n.left, n.right].filter(Boolean));
  }
  A.step(`Row maxima: [${out}].`, A.arr('row maxima', out));
}
A.scenario('Example', '[1,3,2,5,3,null,9]', () => run([1, 3, 2, 5, 3, null, 9]));
'''),

P(num=523, slug="continuous-subarray-sum", title="Continuous Subarray Sum", diff="Medium", topic="Prefix Sum", cls="ContinuousSubarraySum",
idea="Two prefix sums with the same remainder mod k bracket a subarray whose sum is a multiple of k.",
vname="Prefix remainders in a hash map",
spec=r'''
Return `true` if `nums` has a contiguous subarray of length **at least 2** whose sum is a multiple of `k` (0 counts as a multiple).

**Example**
```
nums = [23,2,4,6,7], k = 6  → true   ([2,4])
nums = [23,2,6,4,7], k = 6  → true   (whole array, 42)
nums = [23,2,6,4,7], k = 13 → false
```

**Constraints**
* `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^9`, `1 <= k <= 2^31 - 1`
''',
approach=r'''
**Same remainder.** If `prefix[j] % k == prefix[i] % k` then `nums[i..j-1]` sums to a multiple of `k`. Record the **earliest** index of
each remainder in a `MyHashMap` (remainder 0 at index -1, for subarrays starting at 0); if a remainder repeats at least two positions
later, return `true`. Use `long` because the running value plus `nums[i]` can pass `2^31`.

* Time: **O(n)**.
* Space: **O(min(n, k))** — distinct remainders.
''',
tc="n", sc="n",
java=r'''
public class ContinuousSubarraySum {

    public boolean checkSubarraySum(int[] nums, int k) {
        MyHashMap<Long, Integer> first = new MyHashMap<>();
        first.put(0L, -1);
        long mod = 0;
        for (int i = 0; i < nums.length; i++) {
            mod = (mod + nums[i]) % k;
            Integer j = first.get(mod);
            if (j == null) first.put(mod, i);
            else if (i - j >= 2) return true;
        }
        return false;
    }
}
''',
test=r'''
class ContinuousSubarraySumTest {

    private final ContinuousSubarraySum solution = new ContinuousSubarraySum();

    @Test
    void examples() {
        assertTrue(solution.checkSubarraySum(new int[]{23, 2, 4, 6, 7}, 6));
        assertTrue(solution.checkSubarraySum(new int[]{23, 2, 6, 4, 7}, 6));
        assertFalse(solution.checkSubarraySum(new int[]{23, 2, 6, 4, 7}, 13));
    }

    @Test
    void edgeCases() {
        assertFalse(solution.checkSubarraySum(new int[]{0}, 1));
        assertTrue(solution.checkSubarraySum(new int[]{0, 0}, 1));
        assertTrue(solution.checkSubarraySum(new int[]{5, 0, 0, 0}, 3));
        assertFalse(solution.checkSubarraySum(new int[]{1, 0}, 2));
        assertFalse(solution.checkSubarraySum(new int[]{1_000_000_000, 1_000_000_000, 1_000_000_000}, Integer.MAX_VALUE));
    }
}
''',
trace=r'''
function run(nums, k) {
  const first = new Map([[0, -1]]); let mod = 0;
  A.step(`Remainder 0 is "seen" before the array starts (index −1). Equal remainders mod ${k} bracket a multiple of ${k}.`, A.arr('nums', nums), A.hashTable('remainder → first index', first));
  for (let i = 0; i < nums.length; i++) {
    mod = (mod + nums[i]) % k;
    if (!first.has(mod)) { first.set(mod, i); A.step(`Prefix through index ${i} has remainder ${mod}. New: remember index ${i}.`, A.arr('nums', nums, { hl: { [i]: 'cur' } }), A.hashTable('remainder → first index', first, { hl: mod })); continue; }
    const j = first.get(mod);
    if (i - j >= 2) { A.step(`Remainder ${mod} was first seen at index ${j}. nums[${j + 1}..${i}] sums to a multiple of ${k}.`, A.arr('nums', nums, { range: [j + 1, i] }), A.hashTable('remainder → first index', first, { hl: mod }), A.text('Result', 'true', 'ok')); return; }
    A.step(`Remainder ${mod} repeats, but only one element apart (index ${j}): too short.`, A.arr('nums', nums, { hl: { [i]: 'bad' } }), A.hashTable('remainder → first index', first, { hl: mod }));
  }
  A.step('No remainder repeated far enough apart.', A.text('Result', 'false', 'bad'));
}
A.scenario('Found', '[23,2,4,6,7], k = 6', () => run([23, 2, 4, 6, 7], 6));
A.scenario('Not found', '[23,2,6,4,7], k = 13', () => run([23, 2, 6, 4, 7], 13));
'''),

P(num=525, slug="contiguous-array", title="Contiguous Array", diff="Medium", topic="Prefix Sum", cls="ContiguousArray",
idea="Count 0 as −1; equal running balances mark a stretch with as many 0s as 1s.",
vname="Earliest index of each balance",
spec=r'''
Given a binary array, return the length of the longest contiguous subarray with an equal number of 0s and 1s.

**Example**
```
[0,1]                 → 2
[0,1,0]               → 2
[0,1,1,1,1,1,0,0,0]   → 6
```

**Constraints**
* `1 <= nums.length <= 10^5`
''',
approach=r'''
**Balance.** Add +1 for a 1 and -1 for a 0. A subarray is balanced exactly when the running balance is the same at both ends. The balance
stays within `[-n, n]`, so a plain array (offset by `n`) stores the earliest index of each balance; no hash map is needed.

* Time: **O(n)**.
* Space: **O(n)** — the `2n + 1` slots.
''',
tc="n", sc="n",
java=r'''
public class ContiguousArray {

    public int findMaxLength(int[] nums) {
        int n = nums.length, balance = n, best = 0;
        int[] first = new int[2 * n + 1];
        Arrays.fill(first, -2);
        first[n] = -1;
        for (int i = 0; i < n; i++) {
            balance += nums[i] == 1 ? 1 : -1;
            if (first[balance] == -2) first[balance] = i;
            else best = Math.max(best, i - first[balance]);
        }
        return best;
    }
}
''',
test=r'''
class ContiguousArrayTest {

    private final ContiguousArray solution = new ContiguousArray();

    @Test
    void examples() {
        assertEquals(2, solution.findMaxLength(new int[]{0, 1}));
        assertEquals(2, solution.findMaxLength(new int[]{0, 1, 0}));
        assertEquals(6, solution.findMaxLength(new int[]{0, 1, 1, 1, 1, 1, 0, 0, 0}));
        assertEquals(6, solution.findMaxLength(new int[]{0, 0, 1, 0, 0, 0, 1, 1}));
        assertEquals(0, solution.findMaxLength(new int[]{1, 1, 1}));
    }
}
''',
trace=r'''
function run(nums) {
  const first = new Map([[0, -1]]); let bal = 0, best = 0, range = null;
  A.step('Treat 0 as −1 and 1 as +1. Balance 0 is seen before the array (index −1).', A.arr('nums', nums), A.vars({ balance: 0, best }));
  for (let i = 0; i < nums.length; i++) {
    bal += nums[i] ? 1 : -1;
    if (!first.has(bal)) { first.set(bal, i); A.step(`Balance ${bal} first appears at index ${i}.`, A.arr('nums', nums, { hl: { [i]: 'cur' } }), A.vars({ balance: bal, best }), A.map('balance → first index', first)); }
    else { const len = i - first.get(bal); if (len > best) { best = len; range = [first.get(bal) + 1, i]; } A.step(`Balance ${bal} was seen at index ${first.get(bal)}: nums[${first.get(bal) + 1}..${i}] is balanced, length ${len}.`, A.arr('nums', nums, { range: [first.get(bal) + 1, i] }), A.vars({ balance: bal, best })); }
  }
  A.step(`Longest balanced stretch: ${best}.`, A.arr('nums', nums, range ? { range } : {}), A.text('Result', best, 'ok'));
}
A.scenario('Long run', '[0,1,1,1,1,1,0,0,0]', () => run([0, 1, 1, 1, 1, 1, 0, 0, 0]));
'''),

P(num=538, slug="convert-bst-to-greater-tree", title="Convert BST to Greater Tree", diff="Medium", topic="Binary Search Tree", cls="BSTToGreaterTree",
idea="Visit nodes from largest to smallest (reverse in-order) and keep a running sum.",
vname="Reverse in-order with a running sum", helpers=["TreeNode"],
spec=r'''
Change every node's value in a BST to the sum of its original value and all values **greater** than it.

**Example**
```
[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
  → [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
[0,null,1] → [1,null,1]
```

**Constraints**
* `0 <= n <= 10^4`; values are unique
''',
approach=r'''
**Right, root, left.** A reverse in-order walk visits values in decreasing order. Keep `sum` of everything visited; add the current value
to it and store `sum` in the node.

* Time: **O(n)**.
* Space: **O(h)** — recursion depth.
''',
tc="n", sc="n",
java=r'''
public class BSTToGreaterTree {

    private int sum;

    public TreeNode convertBST(TreeNode root) {
        sum = 0;
        walk(root);
        return root;
    }

    private void walk(TreeNode node) {
        if (node == null) return;
        walk(node.right);
        sum += node.val;
        node.val = sum;
        walk(node.left);
    }
}
''',
test=r'''
class BSTToGreaterTreeTest {

    private final BSTToGreaterTree solution = new BSTToGreaterTree();

    @Test
    void examples() {
        assertEquals(Arrays.asList(30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8),
                TreeNode.toList(solution.convertBST(TreeNode.of(4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8))));
        assertEquals(Arrays.asList(1, null, 1), TreeNode.toList(solution.convertBST(TreeNode.of(0, null, 1))));
        assertNull(solution.convertBST(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {}; let sum = 0;
  A.step('Visit the largest value first: right subtree, then the node, then the left subtree.', A.tree('tree', root), A.vars({ sum }));
  (function walk(n) {
    if (!n) return;
    walk(n.right);
    const old = n.val; sum += old; n.val = sum; hl[n.id] = 'ok';
    A.step(`${old}: running sum ${sum - old} + ${old} = ${sum}. Store it.`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'cur' } }), A.vars({ sum }));
    walk(n.left);
  })(root);
  A.step('Every node now holds itself plus everything greater.', A.tree('tree', root, { hl }));
}
A.scenario('Example', '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]', () => run([4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]));
'''),

P(num=565, slug="array-nesting", title="Array Nesting", diff="Medium", topic="Array", cls="ArrayNesting",
idea="A permutation splits into cycles; the answer is the longest cycle, and each cycle needs to be walked only once.",
vname="Walk each cycle once",
spec=r'''
`nums` is a permutation of `0..n-1`. Starting at `k`, build `s[k] = {nums[k], nums[nums[k]], …}` until a value repeats. Return the size of
the largest `s[k]`.

**Example**
```
[5,4,0,3,1,6,2] → 4   (0 → 5 → 6 → 2 → 0)
[0,1,2]         → 1
```

**Constraints**
* `1 <= nums.length <= 10^5`
''',
approach=r'''
**Cycles.** Following `i → nums[i]` in a permutation always returns to the start, and every starting point on the same cycle gives the same
set. Walk each cycle from its first unvisited index, marking indices as visited (by writing `-1`, on a copy), and keep the longest length.

* Time: **O(n)** — every index is visited once.
* Space: **O(n)** — the copy (O(1) if the input may be modified).
''',
tc="n", sc="n",
java=r'''
public class ArrayNesting {

    public int arrayNesting(int[] nums) {
        int[] a = nums.clone();
        int best = 0;
        for (int i = 0; i < a.length; i++) {
            int len = 0;
            for (int j = i; a[j] != -1; len++) {
                int next = a[j];
                a[j] = -1;
                j = next;
            }
            best = Math.max(best, len);
        }
        return best;
    }
}
''',
test=r'''
class ArrayNestingTest {

    private final ArrayNesting solution = new ArrayNesting();

    @Test
    void examples() {
        assertEquals(4, solution.arrayNesting(new int[]{5, 4, 0, 3, 1, 6, 2}));
        assertEquals(1, solution.arrayNesting(new int[]{0, 1, 2}));
        assertEquals(3, solution.arrayNesting(new int[]{1, 2, 0}));
        assertEquals(2, solution.arrayNesting(new int[]{1, 0, 3, 2}));
    }
}
''',
trace=r'''
function run(nums) {
  const seen = new Array(nums.length).fill(false), hl = {}; let best = 0, cyc = 0;
  A.step('Follow i → nums[i]. In a permutation this always loops back, so the array splits into cycles.', A.arr('nums', nums));
  for (let i = 0; i < nums.length; i++) {
    if (seen[i]) continue;
    const path = []; let j = i; while (!seen[j]) { seen[j] = true; path.push(j); j = nums[j]; }
    cyc++; const c = cyc % 2 ? 'cur' : 'alt'; path.forEach(p => (hl[p] = c)); best = Math.max(best, path.length);
    A.step(`Cycle from index ${i}: ${path.join(' → ')} → ${i}. Length ${path.length}.`, A.arr('nums', nums, { hl }), A.vars({ longest: best }));
  }
  A.step(`Longest cycle: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Example', '[5,4,0,3,1,6,2]', () => run([5, 4, 0, 3, 1, 6, 2]));
'''),

P(num=581, slug="shortest-unsorted-continuous-subarray", title="Shortest Unsorted Continuous Subarray", diff="Medium", topic="Array", cls="ShortestUnsortedSubarray",
idea="The right end is the last element smaller than the maximum before it; the left end is the first element bigger than the minimum after it.",
vname="Two passes with running max and min",
spec=r'''
Find the shortest contiguous subarray that, if sorted, makes the whole array sorted ascending. Return its length.

**Example**
```
[2,6,4,8,10,9,15] → 5   (sort [6,4,8,10,9])
[1,2,3,4]         → 0
[1]               → 0
```

**Constraints**
* `1 <= nums.length <= 10^4`
''',
approach=r'''
**Running extremes.** Left to right, track the maximum so far: any element smaller than it is out of place, so the last such index is the
right end. Right to left, track the minimum so far: the last index (going left) bigger than it is the left end.

* Time: **O(n)** — two passes.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class ShortestUnsortedSubarray {

    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length, end = -1, start = 0;
        int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, nums[i]);
            if (nums[i] < max) end = i;
        }
        for (int i = n - 1; i >= 0; i--) {
            min = Math.min(min, nums[i]);
            if (nums[i] > min) start = i;
        }
        return end == -1 ? 0 : end - start + 1;
    }
}
''',
test=r'''
class ShortestUnsortedSubarrayTest {

    private final ShortestUnsortedSubarray solution = new ShortestUnsortedSubarray();

    @Test
    void examples() {
        assertEquals(5, solution.findUnsortedSubarray(new int[]{2, 6, 4, 8, 10, 9, 15}));
        assertEquals(0, solution.findUnsortedSubarray(new int[]{1, 2, 3, 4}));
        assertEquals(0, solution.findUnsortedSubarray(new int[]{1}));
        assertEquals(4, solution.findUnsortedSubarray(new int[]{1, 3, 2, 2, 2}));
        assertEquals(2, solution.findUnsortedSubarray(new int[]{2, 1}));
        assertEquals(0, solution.findUnsortedSubarray(new int[]{2, 2, 2}));
    }
}
''',
trace=r'''
function run(nums) {
  const n = nums.length; let max = -Infinity, min = Infinity, end = -1, start = 0;
  A.step('Pass 1, left to right: an element smaller than the max before it is out of place. The last one is the right end.', A.arr('nums', nums));
  for (let i = 0; i < n; i++) { max = Math.max(max, nums[i]); if (nums[i] < max) end = i; }
  A.step(end === -1 ? 'Nothing is smaller than an earlier value: already sorted.' : `Right end: index ${end} (${nums[end]} < max ${max} before it).`, A.arr('nums', nums, end >= 0 ? { hl: { [end]: 'bad' } } : {}), A.vars({ end }));
  if (end === -1) { A.step('Length 0.', A.text('Result', 0, 'ok')); return; }
  for (let i = n - 1; i >= 0; i--) { min = Math.min(min, nums[i]); if (nums[i] > min) start = i; }
  A.step(`Pass 2, right to left: an element bigger than the min after it is out of place. Left end: index ${start}.`, A.arr('nums', nums, { hl: { [start]: 'bad', [end]: 'bad' } }), A.vars({ start, end }));
  A.step(`Sorting nums[${start}..${end}] fixes everything: length ${end - start + 1}.`, A.arr('nums', nums, { range: [start, end] }), A.text('Result', end - start + 1, 'ok'));
}
A.scenario('Example', '[2,6,4,8,10,9,15]', () => run([2, 6, 4, 8, 10, 9, 15]));
A.scenario('Duplicates', '[1,3,2,2,2]', () => run([1, 3, 2, 2, 2]));
''',
variants=[dict(
name="Compare with a sorted copy",
idea="Sort a copy; the first and last positions that differ bound the subarray.",
approach=r'''
**Sort and diff.** Positions where the array already matches its sorted version can stay; the answer spans from the first mismatch to the
last.

* Time: **O(n log n)** — sorting.
* Space: **O(n)** — the copy.
''',
tc="nlogn", sc="n",
java=r'''
public class ShortestUnsortedSubarray {

    public int findUnsortedSubarray(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi && nums[lo] == sorted[lo]) lo++;
        while (hi >= lo && nums[hi] == sorted[hi]) hi--;
        return hi - lo + 1;
    }
}
''',
trace=r'''
function run(nums) {
  const s = nums.slice().sort((a, b) => a - b); let lo = 0, hi = nums.length - 1;
  A.step('Sort a copy.', A.arr('nums', nums), A.arr('sorted', s));
  while (lo <= hi && nums[lo] === s[lo]) lo++;
  A.step(`First mismatch from the left: index ${lo}.`, A.arr('nums', nums, { hl: { [lo]: 'bad' } }), A.arr('sorted', s, { hl: { [lo]: 'bad' } }));
  while (hi >= lo && nums[hi] === s[hi]) hi--;
  A.step(`First mismatch from the right: index ${hi}.`, A.arr('nums', nums, { hl: { [lo]: 'bad', [hi]: 'bad' } }), A.arr('sorted', s, { hl: { [lo]: 'bad', [hi]: 'bad' } }));
  A.step(`Length ${hi - lo + 1}.`, A.arr('nums', nums, { range: [lo, hi] }), A.text('Result', hi - lo + 1, 'ok'));
}
A.scenario('Example', '[2,6,4,8,10,9,15]', () => run([2, 6, 4, 8, 10, 9, 15]));
''')]),

P(num=583, slug="delete-operation-for-two-strings", title="Delete Operation for Two Strings", diff="Medium", topic="Dynamic Programming", cls="DeleteOperationTwoStrings",
idea="Keep the longest common subsequence and delete everything else.",
vname="Longest common subsequence",
spec=r'''
Return the minimum number of single-character deletions (from either string) needed to make `word1` and `word2` equal.

**Example**
```
"sea", "eat"       → 2   (delete 's' and 't')
"leetcode", "etco" → 4
```

**Constraints**
* `1 <= length <= 500`, lower-case letters
''',
approach=r'''
**LCS.** What survives in both strings is a common subsequence; to delete as little as possible, keep the longest one. Compute the LCS
length with the standard table (`dp[i][j] = dp[i-1][j-1] + 1` on a match, else the max of the two neighbours) using one row. Answer:
`m + n - 2 · LCS`.

* Time: **O(mn)**.
* Space: **O(n)** — one row.
''',
tc="n2", sc="n",
java=r'''
public class DeleteOperationTwoStrings {

    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[] dp = new int[n + 1];
        for (int i = 1; i <= m; i++) {
            int diag = 0;
            for (int j = 1; j <= n; j++) {
                int up = dp[j];
                dp[j] = word1.charAt(i - 1) == word2.charAt(j - 1) ? diag + 1 : Math.max(dp[j], dp[j - 1]);
                diag = up;
            }
        }
        return m + n - 2 * dp[n];
    }
}
''',
test=r'''
class DeleteOperationTwoStringsTest {

    private final DeleteOperationTwoStrings solution = new DeleteOperationTwoStrings();

    @ParameterizedTest
    @CsvSource({"sea,eat,2", "leetcode,etco,4", "a,a,0", "abc,def,6", "abcde,ace,2"})
    void deletions(String a, String b, int expected) {
        assertEquals(expected, solution.minDistance(a, b));
    }
}
''',
trace=r'''
function run(a, b) {
  const m = a.length, n = b.length, dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
  A.step('dp[i][j] = length of the longest common subsequence of the first i letters of word1 and the first j of word2.', A.chars('word1', a), A.chars('word2', b), A.grid('dp', dp));
  for (let i = 1; i <= m; i++) {
    const hl = {};
    for (let j = 1; j <= n; j++) { const match = a[i - 1] === b[j - 1]; dp[i][j] = match ? dp[i - 1][j - 1] + 1 : Math.max(dp[i - 1][j], dp[i][j - 1]); hl[`${i},${j}`] = match ? 'ok' : 'cur'; }
    A.step(`Row ${i} ('${a[i - 1]}'): green cells are matches, which extend the diagonal by one.`, A.grid('dp', dp, { hl }));
  }
  const l = dp[m][n];
  A.step(`The LCS has length ${l}. Delete everything else: ${m} + ${n} − 2 × ${l} = ${m + n - 2 * l}.`, A.grid('dp', dp, { hl: { [`${m},${n}`]: 'ok' } }), A.text('Result', m + n - 2 * l, 'ok'));
}
A.scenario('Example', '"sea" and "eat"', () => run('sea', 'eat'));
'''),

P(num=589, slug="n-ary-tree-preorder-traversal", title="N-ary Tree Preorder Traversal", diff="Easy", topic="Tree", cls="NaryPreorder",
idea="Use a stack; push children in reverse so the leftmost child is processed first.",
vname="Iterative with a stack",
spec=r'''
Return the preorder traversal (node, then its children left to right) of an n-ary tree.

The tree uses `NaryPreorder.Node`, which has `val` and `children`.

**Example**
```
1
├─ 3
│  ├─ 5
│  └─ 6
├─ 2
└─ 4                → [1,3,5,6,2,4]
```

**Constraints**
* `0 <= n <= 10^4`, height at most 1000
''',
approach=r'''
**Explicit stack.** Pop a node, record it, then push its children from right to left so the leftmost child is on top. This avoids deep
recursion.

* Time: **O(n)**.
* Space: **O(n)** — the stack.
''',
tc="n", sc="n",
java=r'''
public class NaryPreorder {
''' + NODE_CLASS + r'''
    public List<Integer> preorder(Node root) {
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<Node> stack = new ArrayDeque<>(List.of(root));
        while (!stack.isEmpty()) {
            Node n = stack.pop();
            out.add(n.val);
            for (int i = n.children.size() - 1; i >= 0; i--) stack.push(n.children.get(i));
        }
        return out;
    }
}
''',
test=r'''
class NaryPreorderTest {

    private final NaryPreorder solution = new NaryPreorder();

    private static NaryPreorder.Node n(int v, NaryPreorder.Node... kids) {
        return new NaryPreorder.Node(v, kids);
    }

    @Test
    void examples() {
        assertEquals(List.of(1, 3, 5, 6, 2, 4), solution.preorder(n(1, n(3, n(5), n(6)), n(2), n(4))));
        assertEquals(List.of(), solution.preorder(null));
        assertEquals(List.of(1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10),
                solution.preorder(n(1, n(2), n(3, n(6), n(7, n(11, n(14)))), n(4, n(8, n(12))), n(5, n(9, n(13)), n(10)))));
    }
}
''',
trace=NARY_LAYOUT + r'''
function run(spec) {
  const { nodes, edges } = nary(spec), hl = {}, out = [], st = [nodes[0]];
  const kids = nd => edges.filter(e => e[0] === nd.id).map(e => nodes[e[1]]);
  A.step('Start with the root on the stack.', A.graph('tree', nodes, edges), A.stack('stack', st.map(x => x.label)));
  while (st.length) {
    const nd = st.pop(); out.push(nd.label); hl[nd.id] = 'ok';
    const ks = kids(nd); for (let i = ks.length - 1; i >= 0; i--) st.push(ks[i]);
    A.step(`Pop ${nd.label} and record it.${ks.length ? ` Push its children right to left (${ks.slice().reverse().map(k => k.label).join(', ')}) so ${ks[0].label} comes next.` : ''}`, A.graph('tree', nodes, edges, { hl: { ...hl, [nd.id]: 'cur' } }), A.stack('stack', st.map(x => x.label)), A.arr('preorder', out));
  }
  A.step(`Preorder: [${out}].`, A.arr('preorder', out));
}
A.scenario('Example', '1 → (3 → 5, 6), 2, 4', () => run({ v: 1, c: [{ v: 3, c: [{ v: 5 }, { v: 6 }] }, { v: 2 }, { v: 4 }] }));
'''),

P(num=559, slug="maximum-depth-of-n-ary-tree", title="Maximum Depth of N-ary Tree", diff="Easy", topic="Tree", cls="NaryMaxDepth",
idea="The depth of a node is one more than the deepest of its children.",
vname="Recursive depth",
spec=r'''
Return the maximum depth (number of nodes on the longest root-to-leaf path) of an n-ary tree.

The tree uses `NaryMaxDepth.Node`, which has `val` and `children`.

**Example**
```
1 → (3 → 5, 6), 2, 4   → 3
```

**Constraints**
* `0 <= n <= 10^4`, height at most 1000
''',
approach=r'''
**Recursion.** An empty tree has depth 0. Otherwise the depth is `1 + max(depth(child))` over the children (0 if there are none).

* Time: **O(n)**.
* Space: **O(h)** — recursion depth.
''',
tc="n", sc="n",
java=r'''
public class NaryMaxDepth {
''' + NODE_CLASS + r'''
    public int maxDepth(Node root) {
        if (root == null) return 0;
        int deepest = 0;
        for (Node child : root.children) deepest = Math.max(deepest, maxDepth(child));
        return deepest + 1;
    }
}
''',
test=r'''
class NaryMaxDepthTest {

    private final NaryMaxDepth solution = new NaryMaxDepth();

    private static NaryMaxDepth.Node n(int v, NaryMaxDepth.Node... kids) {
        return new NaryMaxDepth.Node(v, kids);
    }

    @Test
    void examples() {
        assertEquals(3, solution.maxDepth(n(1, n(3, n(5), n(6)), n(2), n(4))));
        assertEquals(0, solution.maxDepth(null));
        assertEquals(1, solution.maxDepth(n(1)));
        assertEquals(5, solution.maxDepth(n(1, n(2), n(3, n(6), n(7, n(11, n(14)))), n(4, n(8, n(12))), n(5, n(9, n(13)), n(10)))));
    }
}
''',
trace=NARY_LAYOUT + r'''
function run(spec) {
  const { nodes, edges } = nary(spec), hl = {}, depth = {};
  const kids = nd => edges.filter(e => e[0] === nd.id).map(e => nodes[e[1]]);
  A.step('Each node reports 1 + the deepest child. Leaves report 1.', A.graph('tree', nodes, edges));
  (function go(nd) {
    const ks = kids(nd); ks.forEach(go);
    depth[nd.id] = 1 + Math.max(0, ...ks.map(k => depth[k.id])); hl[nd.id] = 'ok';
    A.step(ks.length ? `${nd.label}: deepest child depth ${depth[nd.id] - 1}, so depth ${depth[nd.id]}.` : `${nd.label} is a leaf: depth 1.`, A.graph('tree', nodes.map(x => ({ ...x, label: depth[x.id] ? `${x.label}:${depth[x.id]}` : x.label })), edges, { hl: { ...hl, [nd.id]: 'cur' } }));
  })(nodes[0]);
  A.step(`Maximum depth: ${depth[0]}.`, A.text('Result', depth[0], 'ok'));
}
A.scenario('Example', '1 → (3 → 5, 6), 2, 4', () => run({ v: 1, c: [{ v: 3, c: [{ v: 5 }, { v: 6 }] }, { v: 2 }, { v: 4 }] }));
'''),
]
