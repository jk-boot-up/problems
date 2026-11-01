PROBLEMS = [
P(num=236, slug="lowest-common-ancestor-of-a-binary-tree", title="Lowest Common Ancestor of a Binary Tree", diff="Medium", topic="Binary Tree General", cls="LowestCommonAncestor",
idea="A node is the LCA when p and q are found in different subtrees, or the node is one of them and the other is below.",
vname="Recursive search", helpers=["TreeNode"],
spec=r'''
Given a binary tree and two of its nodes `p` and `q`, return their **lowest common ancestor**: the deepest node that has both `p`
and `q` as descendants (a node counts as a descendant of itself).

**Example 1**
```
Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
```

**Example 2**
```
Input:  same tree, p = 5, q = 4
Output: 5
```

**Constraints**
* `2 <= n <= 10^5`; values are unique; `p != q`; both exist in the tree.
''',
approach=r'''
**Bubble up what you find.** `lca(n)` returns `n` if `n` is null, `p` or `q`. Otherwise recurse into both children: if both return a
node, `n` is the split point, so return `n`. Otherwise return whichever side found something.

* Time: **O(n)** — each node is visited at most once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class LowestCommonAncestor {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root;
        return left != null ? left : right;
    }
}
''',
test=r'''
class LowestCommonAncestorTest {

    private final LowestCommonAncestor solution = new LowestCommonAncestor();

    private static TreeNode find(TreeNode n, int val) {
        if (n == null || n.val == val) return n;
        TreeNode l = find(n.left, val);
        return l != null ? l : find(n.right, val);
    }

    private final TreeNode root = TreeNode.of(3, 5, 1, 6, 2, 0, 8, null, null, 7, 4);

    @Test
    void differentSides() {
        assertEquals(3, solution.lowestCommonAncestor(root, find(root, 5), find(root, 1)).val);
    }

    @Test
    void ancestorOfItself() {
        assertEquals(5, solution.lowestCommonAncestor(root, find(root, 5), find(root, 4)).val);
    }

    @Test
    void deepPair() {
        assertEquals(2, solution.lowestCommonAncestor(root, find(root, 7), find(root, 4)).val);
    }
}
''',
trace=r'''
function run(arr, pv, qv) {
  const root = A.mkTree(arr), hl = {};
  const find = (n, v) => (!n ? null : n.val === v ? n : find(n.left, v) || find(n.right, v));
  const p = find(root, pv), q = find(root, qv);
  hl[p.id] = hl[q.id] = 'alt';
  A.step(`Find the lowest common ancestor of ${pv} and ${qv} (purple). Each call reports which target, if any, it found below.`, A.tree('tree', root, { hl }));
  const res = (function lca(n) {
    if (!n) return null;
    if (n === p || n === q) { A.step(`${n.val} is a target. Report it upward without looking further down.`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'cur' } })); return n; }
    const l = lca(n.left), r = lca(n.right);
    if (l && r) { hl[n.id] = 'ok'; A.step(`${n.val} receives ${l.val} from the left and ${r.val} from the right, so it is the split point: the LCA.`, A.tree('tree', root, { hl })); return n; }
    const got = l || r;
    if (got) A.step(`${n.val} found only ${got.val} below it. Pass ${got.val} up.`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'sel' } }));
    return got;
  })(root);
  A.step(`The lowest common ancestor is ${res.val}.`, A.tree('tree', root, { hl: { ...hl, [res.id]: 'ok' } }), A.text('Result', res.val, 'ok'));
}
A.scenario('Different subtrees', 'p = 5, q = 1', () => run([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], 5, 1));
A.scenario('One is the ancestor', 'p = 5, q = 4', () => run([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], 5, 4));
''',
variants=[dict(
name="Parent map and ancestor set",
idea="Record every node's parent, collect p's ancestors in a set, then climb from q until hitting one.",
approach=r'''
**Parent pointers.** Traverse once to fill a `MyHashMap<node, parent>`. Put all ancestors of `p` (including `p`) in a `MyHashSet`.
Climb from `q` until reaching a node in that set.

* Time: **O(n)** — one traversal plus two climbs.
* Space: **O(n)** — the parent map.
''',
tc="n", sc="n",
java=r'''
public class LowestCommonAncestor {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        MyHashMap<TreeNode, TreeNode> parent = new MyHashMap<>();
        Deque<TreeNode> stack = new ArrayDeque<>(List.of(root));
        parent.put(root, null);
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            if (n.left != null) { parent.put(n.left, n); stack.push(n.left); }
            if (n.right != null) { parent.put(n.right, n); stack.push(n.right); }
        }
        MyHashSet<TreeNode> ancestors = new MyHashSet<>();
        for (TreeNode a = p; a != null; a = parent.get(a)) ancestors.add(a);
        TreeNode b = q;
        while (!ancestors.contains(b)) b = parent.get(b);
        return b;
    }
}
''',
trace=r'''
function run(arr, pv, qv) {
  const root = A.mkTree(arr), par = new Map(), stack = [root];
  par.set(root, null);
  while (stack.length) { const n = stack.pop(); [n.left, n.right].forEach(c => { if (c) { par.set(c, n); stack.push(c); } }); }
  const find = (n, v) => (!n ? null : n.val === v ? n : find(n.left, v) || find(n.right, v));
  const p = find(root, pv), q = find(root, qv), anc = new Set(), hl = {};
  A.step('Traverse once and record every node’s parent.', A.tree('tree', root), A.hashTable('node → parent', new Map([...par].map(([k, v]) => [k.val, v ? v.val : 'null']))));
  for (let a = p; a; a = par.get(a)) { anc.add(a.val); hl[a.id] = 'sel'; }
  A.step(`Climb from ${pv} to the root, storing every ancestor in a set.`, A.tree('tree', root, { hl }), A.hashTable('ancestors of p', anc));
  let b = q; while (!anc.has(b.val)) { hl[b.id] = 'cur'; b = par.get(b); }
  hl[b.id] = 'ok';
  A.step(`Climb from ${qv} until we hit an ancestor of ${pv}: ${b.val}. That is the LCA.`, A.tree('tree', root, { hl }), A.text('Result', b.val, 'ok'));
}
A.scenario('Deep pair', 'p = 7, q = 0', () => run([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], 7, 0));
''')]),

P(num=199, slug="binary-tree-right-side-view", title="Binary Tree Right Side View", diff="Medium", topic="Binary Tree BFS", cls="RightSideView",
idea="Standing on the right, you see the last node of every level.",
vname="Level-order BFS", helpers=["TreeNode"],
spec=r'''
Imagine standing on the right side of a binary tree. Return the values you can see, from top to bottom.

**Example 1**
```
Input:  [1,2,3,null,5,null,4]
Output: [1,3,4]
```

**Example 2**
```
Input:  [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
```

**Constraints**
* `0 <= n <= 100`
''',
approach=r'''
**BFS by levels.** Process the queue one level at a time; the last node popped in each level is visible.

* Time: **O(n)** — each node is enqueued once.
* Space: **O(w)** — the widest level.
''',
tc="n", sc="n",
java=r'''
public class RightSideView {

    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        while (!queue.isEmpty()) {
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                if (size == 1) out.add(n.val);
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
        }
        return out;
    }
}
''',
test=r'''
class RightSideViewTest {

    private final RightSideView solution = new RightSideView();

    @Test
    void example1() {
        assertEquals(List.of(1, 3, 4), solution.rightSideView(TreeNode.of(1, 2, 3, null, 5, null, 4)));
    }

    @Test
    void leftDeeper() {
        assertEquals(List.of(1, 3, 4, 5), solution.rightSideView(TreeNode.of(1, 2, 3, 4, null, null, null, 5)));
    }

    @Test
    void empty() {
        assertEquals(List.of(), solution.rightSideView(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), out = [], hl = {}; let q = [root];
  A.step('Visit the tree level by level. The last node of each level is what you see from the right.', A.tree('tree', root));
  while (q.length) {
    const last = q[q.length - 1]; out.push(last.val);
    q.forEach(n => (hl[n.id] = 'sel')); hl[last.id] = 'ok';
    A.step(`Level ${q.map(n => n.val).join(', ')}: the rightmost node is ${last.val}.`, A.tree('tree', root, { hl }), A.arr('queue', q.map(n => n.val), { hl: { [q.length - 1]: 'ok' } }), A.arr('view', out));
    q.forEach(n => hl[n.id] === 'sel' && (hl[n.id] = 'dim'));
    q = q.flatMap(n => [n.left, n.right].filter(Boolean));
  }
  A.step(`Right side view: [${out}].`, A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Classic', '[1,2,3,null,5,null,4]', () => run([1, 2, 3, null, 5, null, 4]));
A.scenario('Left side is deeper', '[1,2,3,4,null,null,null,5]', () => run([1, 2, 3, 4, null, null, null, 5]));
''',
variants=[dict(
name="Right-first DFS",
idea="Visit right children before left; the first node reached at each depth is visible.",
approach=r'''
**DFS, right child first.** When `depth == out.size()`, this is the first node seen at that depth, and right-first order makes
it the rightmost.

* Time: **O(n)** — each node is visited once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class RightSideView {

    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        dfs(root, 0, out);
        return out;
    }

    private void dfs(TreeNode n, int depth, List<Integer> out) {
        if (n == null) return;
        if (depth == out.size()) out.add(n.val);
        dfs(n.right, depth + 1, out);
        dfs(n.left, depth + 1, out);
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), out = [], hl = {};
  (function dfs(n, d) {
    if (!n) return;
    const first = d === out.length; if (first) out.push(n.val);
    hl[n.id] = first ? 'ok' : 'dim';
    A.step(first ? `${n.val} is the first node reached at depth ${d}, so it is visible.` : `${n.val} is at depth ${d}, which already has a visible node. It is hidden.`, A.tree('tree', root, { hl }), A.arr('view', out));
    dfs(n.right, d + 1); dfs(n.left, d + 1);
  })(root, 0);
}
A.scenario('Left side is deeper', '[1,2,3,4,null,null,null,5]', () => run([1, 2, 3, 4, null, null, null, 5]));
''')]),

P(num=637, slug="average-of-levels-in-binary-tree", title="Average of Levels in Binary Tree", diff="Easy", topic="Binary Tree BFS", cls="AverageOfLevels",
idea="Sum each level during a level-order traversal and divide by its size.",
vname="Level-order BFS", helpers=["TreeNode"],
spec=r'''
Return the average value of the nodes on each level of a binary tree, from top to bottom. Answers within `10^-5` are accepted.

**Example**
```
Input:  [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
```

**Constraints**
* `1 <= n <= 10^4`; `-2^31 <= Node.val <= 2^31 - 1`
''',
approach=r'''
**BFS by levels.** Pop exactly one level at a time, summing values in a `long` (to avoid overflow), and divide by the level size.

* Time: **O(n)** — each node is enqueued once.
* Space: **O(w)** — the widest level.
''',
tc="n", sc="n",
java=r'''
public class AverageOfLevels {

    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> out = new ArrayList<>();
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        while (!queue.isEmpty()) {
            int size = queue.size();
            long sum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode n = queue.poll();
                sum += n.val;
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
            out.add((double) sum / size);
        }
        return out;
    }
}
''',
test=r'''
class AverageOfLevelsTest {

    private final AverageOfLevels solution = new AverageOfLevels();

    @Test
    void example() {
        assertEquals(List.of(3.0, 14.5, 11.0), solution.averageOfLevels(TreeNode.of(3, 9, 20, null, null, 15, 7)));
    }

    @Test
    void noOverflow() {
        assertEquals(List.of(2147483647.0, 2147483647.0), solution.averageOfLevels(TreeNode.of(2147483647, 2147483647, 2147483647)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), out = [], hl = {}; let q = [root];
  while (q.length) {
    const sum = q.reduce((s, n) => s + n.val, 0), avg = sum / q.length;
    out.push(+avg.toFixed(2));
    q.forEach(n => (hl[n.id] = 'cur'));
    A.step(`Level ${q.map(n => n.val).join(', ')}: sum ${sum} ÷ ${q.length} = ${avg}.`, A.tree('tree', root, { hl }), A.arr('averages', out, { hl: { [out.length - 1]: 'ok' } }));
    q.forEach(n => (hl[n.id] = 'ok'));
    q = q.flatMap(n => [n.left, n.right].filter(Boolean));
  }
  A.step(`Averages: [${out}].`, A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Classic', '[3,9,20,null,null,15,7]', () => run([3, 9, 20, null, null, 15, 7]));
'''),

P(num=102, slug="binary-tree-level-order-traversal", title="Binary Tree Level Order Traversal", diff="Medium", topic="Binary Tree BFS", cls="LevelOrderTraversal",
idea="A queue visits nodes in level order; cut it into levels by processing exactly the current queue size each round.",
vname="Queue, level by level", helpers=["TreeNode"],
spec=r'''
Return the level-order traversal of a binary tree's values: left to right, level by level, as a list of lists.

**Example**
```
Input:  [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Constraints**
* `0 <= n <= 2000`
''',
approach=r'''
**BFS.** Each round, remember `size = queue.size()`; pop exactly `size` nodes into one list and enqueue their children.

* Time: **O(n)** — each node is enqueued once.
* Space: **O(w)** — the widest level (plus the output).
''',
tc="n", sc="n",
java=r'''
public class LevelOrderTraversal {

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                level.add(n.val);
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
            out.add(level);
        }
        return out;
    }
}
''',
test=r'''
class LevelOrderTraversalTest {

    private final LevelOrderTraversal solution = new LevelOrderTraversal();

    @Test
    void example() {
        assertEquals(List.of(List.of(3), List.of(9, 20), List.of(15, 7)), solution.levelOrder(TreeNode.of(3, 9, 20, null, null, 15, 7)));
    }

    @Test
    void empty() {
        assertEquals(List.of(), solution.levelOrder(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), out = [], hl = {}; let q = [root];
  A.step('Start with the root in the queue.', A.tree('tree', root), A.arr('queue', [root.val]));
  while (q.length) {
    out.push(q.map(n => n.val));
    q.forEach(n => (hl[n.id] = 'cur'));
    const nextQ = q.flatMap(n => [n.left, n.right].filter(Boolean));
    A.step(`The queue holds exactly one level: [${out[out.length - 1]}]. Pop them all and queue their children: [${nextQ.map(n => n.val)}].`, A.tree('tree', root, { hl }), A.arr('levels', out.map(l => `[${l}]`), { hl: { [out.length - 1]: 'ok' } }), A.arr('next queue', nextQ.map(n => n.val)));
    q.forEach(n => (hl[n.id] = 'ok'));
    q = nextQ;
  }
  A.step(`Level order: ${JSON.stringify(out)}.`, A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Classic', '[3,9,20,null,null,15,7]', () => run([3, 9, 20, null, null, 15, 7]));
'''),

P(num=103, slug="binary-tree-zigzag-level-order-traversal", title="Binary Tree Zigzag Level Order Traversal", diff="Medium", topic="Binary Tree BFS", cls="ZigzagLevelOrder",
idea="Do a normal level-order traversal, but fill every other level from the right.",
vname="BFS with alternating direction", helpers=["TreeNode"],
spec=r'''
Return the zigzag level-order traversal: the first level left to right, the next right to left, and so on.

**Example**
```
Input:  [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

**Constraints**
* `0 <= n <= 2000`
''',
approach=r'''
**BFS + deque per level.** Process levels as usual. For left-to-right levels append values at the back; for right-to-left levels
add them at the front. Flip the direction after each level.

* Time: **O(n)** — each node is processed once.
* Space: **O(w)** — the widest level.
''',
tc="n", sc="n",
java=r'''
public class ZigzagLevelOrder {

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        boolean leftToRight = true;
        while (!queue.isEmpty()) {
            LinkedList<Integer> level = new LinkedList<>();
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                if (leftToRight) level.addLast(n.val); else level.addFirst(n.val);
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
            out.add(level);
            leftToRight = !leftToRight;
        }
        return out;
    }
}
''',
test=r'''
class ZigzagLevelOrderTest {

    private final ZigzagLevelOrder solution = new ZigzagLevelOrder();

    @Test
    void example() {
        assertEquals(List.of(List.of(3), List.of(20, 9), List.of(15, 7)), solution.zigzagLevelOrder(TreeNode.of(3, 9, 20, null, null, 15, 7)));
    }

    @Test
    void fourLevels() {
        assertEquals(List.of(List.of(1), List.of(3, 2), List.of(4, 5, 6, 7), List.of(8)),
                solution.zigzagLevelOrder(TreeNode.of(1, 2, 3, 4, 5, 6, 7, 8)));
    }

    @Test
    void empty() {
        assertEquals(List.of(), solution.zigzagLevelOrder(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), out = [], hl = {}; let q = [root], ltr = true;
  while (q.length) {
    const vals = q.map(n => n.val); if (!ltr) vals.reverse();
    out.push(vals);
    q.forEach(n => (hl[n.id] = 'cur'));
    A.step(`Level ${out.length}, read ${ltr ? 'left to right' : 'right to left'}: [${vals}].`, A.tree('tree', root, { hl }), A.arr('levels', out.map(l => `[${l}]`), { hl: { [out.length - 1]: 'ok' } }));
    q.forEach(n => (hl[n.id] = 'ok'));
    q = q.flatMap(n => [n.left, n.right].filter(Boolean)); ltr = !ltr;
  }
  A.step(`Zigzag order: ${JSON.stringify(out)}.`, A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Four levels', '[1,2,3,4,5,6,7,8]', () => run([1, 2, 3, 4, 5, 6, 7, 8]));
'''),

P(num=530, slug="minimum-absolute-difference-in-bst", title="Minimum Absolute Difference in BST", diff="Easy", topic="Binary Search Tree", cls="MinimumDifferenceBST",
idea="In-order traversal of a BST is sorted, so the closest pair is always adjacent in that order.",
vname="In-order with previous value", helpers=["TreeNode"],
spec=r'''
Given the root of a **BST**, return the minimum absolute difference between the values of any two different nodes.

**Example 1**
```
Input:  [4,2,6,1,3]
Output: 1
```

**Example 2**
```
Input:  [1,0,48,null,null,12,49]
Output: 1
```

**Constraints**
* `2 <= n <= 10^4`; `0 <= Node.val <= 10^5`
''',
approach=r'''
**Sorted order.** An in-order traversal visits values in increasing order; compare each value with the previous one and keep the smallest gap.

* Time: **O(n)** — one traversal.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class MinimumDifferenceBST {

    private Integer prev;
    private int best;

    public int getMinimumDifference(TreeNode root) {
        prev = null;
        best = Integer.MAX_VALUE;
        inorder(root);
        return best;
    }

    private void inorder(TreeNode n) {
        if (n == null) return;
        inorder(n.left);
        if (prev != null) best = Math.min(best, n.val - prev);
        prev = n.val;
        inorder(n.right);
    }
}
''',
test=r'''
class MinimumDifferenceBSTTest {

    private final MinimumDifferenceBST solution = new MinimumDifferenceBST();

    @Test
    void example1() {
        assertEquals(1, solution.getMinimumDifference(TreeNode.of(4, 2, 6, 1, 3)));
    }

    @Test
    void example2() {
        assertEquals(1, solution.getMinimumDifference(TreeNode.of(1, 0, 48, null, null, 12, 49)));
    }

    @Test
    void twoNodes() {
        assertEquals(7, solution.getMinimumDifference(TreeNode.of(10, 3)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), seq = [], hl = {}; let prev = null, best = Infinity;
  A.step('In-order traversal of a BST gives the values in sorted order, so only neighbours in that order need comparing.', A.tree('BST', root));
  (function ino(n) {
    if (!n) return;
    ino(n.left);
    seq.push(n.val); hl[n.id] = 'ok';
    if (prev !== null) { const d = n.val - prev, nb = d < best; if (nb) best = d; A.step(`Visit ${n.val}. The gap to the previous value ${prev} is ${d}.${nb ? ' New minimum.' : ''}`, A.tree('BST', root, { hl: { ...hl, [n.id]: 'cur' } }), A.arr('in-order', seq, { hl: { [seq.length - 2]: 'sel', [seq.length - 1]: 'cur' } }), A.vars({ best })); }
    else A.step(`Visit ${n.val}, the smallest value.`, A.tree('BST', root, { hl: { ...hl, [n.id]: 'cur' } }), A.arr('in-order', seq));
    prev = n.val;
    ino(n.right);
  })(root);
  A.step(`The minimum difference is ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', '[4,2,6,1,3]', () => run([4, 2, 6, 1, 3]));
A.scenario('Wide gaps', '[1,0,48,null,null,12,49]', () => run([1, 0, 48, null, null, 12, 49]));
'''),

P(num=230, slug="kth-smallest-element-in-a-bst", title="Kth Smallest Element in a BST", diff="Medium", topic="Binary Search Tree", cls="KthSmallestBST",
idea="Walk the BST in order and stop at the k-th visited node.",
vname="Iterative in-order, stop early", helpers=["TreeNode"],
spec=r'''
Given the root of a BST and an integer `k`, return the `k`-th smallest value (1-indexed).

**Example 1**
```
Input:  root = [3,1,4,null,2], k = 1
Output: 1
```

**Example 2**
```
Input:  root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

**Constraints**
* `1 <= k <= n <= 10^4`
''',
approach=r'''
**Stack-based in-order.** Push the left spine; pop a node (the next smallest), decrement `k`; when `k` hits 0, return it. Otherwise
push the left spine of its right child.

* Time: **O(h + k)** — descend once, then pop k nodes.
* Space: **O(h)** — the stack.
''',
tc="log", sc="log",
java=r'''
public class KthSmallestBST {

    public int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode n = root;
        while (true) {
            for (; n != null; n = n.left) stack.push(n);
            n = stack.pop();
            if (--k == 0) return n.val;
            n = n.right;
        }
    }
}
''',
test=r'''
class KthSmallestBSTTest {

    private final KthSmallestBST solution = new KthSmallestBST();

    @Test
    void first() {
        assertEquals(1, solution.kthSmallest(TreeNode.of(3, 1, 4, null, 2), 1));
    }

    @Test
    void third() {
        assertEquals(3, solution.kthSmallest(TreeNode.of(5, 3, 6, 2, 4, null, null, 1), 3));
    }

    @Test
    void largest() {
        assertEquals(6, solution.kthSmallest(TreeNode.of(5, 3, 6, 2, 4, null, null, 1), 6));
    }
}
''',
trace=r'''
function run(arr, k) {
  const root = A.mkTree(arr), st = [], hl = {}; let n = root, count = 0;
  A.step(`Walk the BST in order with a stack and stop at the ${k}th node.`, A.tree('BST', root));
  while (true) {
    for (; n; n = n.left) { st.push(n); hl[n.id] = 'sel'; }
    n = st.pop(); count++;
    if (count === k) { hl[n.id] = 'ok'; A.step(`Pop ${n.val}: it is visit number ${k}. Stop here; the rest of the tree is never touched.`, A.tree('BST', root, { hl }), A.stack('stack', st.map(x => x.val)), A.text('Result', n.val, 'ok')); return; }
    hl[n.id] = 'dim';
    A.step(`Pop ${n.val}: visit number ${count}. Continue with its right subtree.`, A.tree('BST', root, { hl: { ...hl, [n.id]: 'cur' } }), A.stack('stack', st.map(x => x.val)));
    n = n.right;
  }
}
A.scenario('k = 3', '[5,3,6,2,4,null,null,1]', () => run([5, 3, 6, 2, 4, null, null, 1], 3));
''',
variants=[dict(
name="Full in-order list",
idea="Collect every value in sorted order, then index k − 1.",
approach=r'''
**Collect everything.** A recursive in-order traversal fills a list; return `list.get(k - 1)`.

* Time: **O(n)** — the whole tree is traversed even for small k.
* Space: **O(n)** — the list.
''',
tc="n", sc="n",
java=r'''
public class KthSmallestBST {

    public int kthSmallest(TreeNode root, int k) {
        List<Integer> values = new ArrayList<>();
        inorder(root, values);
        return values.get(k - 1);
    }

    private void inorder(TreeNode n, List<Integer> out) {
        if (n == null) return;
        inorder(n.left, out);
        out.add(n.val);
        inorder(n.right, out);
    }
}
''',
trace=r'''
function run(arr, k) {
  const root = A.mkTree(arr), vals = [], hl = {};
  (function ino(n) { if (!n) return; ino(n.left); vals.push(n.val); hl[n.id] = 'sel'; A.step(`Collect ${n.val}.`, A.tree('BST', root, { hl }), A.arr('sorted values', vals)); ino(n.right); })(root);
  A.step(`The answer is values[${k - 1}] = ${vals[k - 1]}, but we visited all ${vals.length} nodes.`, A.arr('sorted values', vals, { hl: { [k - 1]: 'ok' } }), A.text('Result', vals[k - 1], 'ok'));
}
A.scenario('k = 3', '[5,3,6,2,4,null,null,1]', () => run([5, 3, 6, 2, 4, null, null, 1], 3));
''')]),

P(num=98, slug="validate-binary-search-tree", title="Validate Binary Search Tree", diff="Medium", topic="Binary Search Tree", cls="ValidateBST",
idea="Every node must lie strictly inside the (low, high) window inherited from its ancestors.",
vname="Bounds recursion", helpers=["TreeNode"],
spec=r'''
Return `true` if a binary tree is a valid **BST**: every node's left subtree holds only smaller values, its right subtree only larger
values, and both subtrees are BSTs.

**Example 1**
```
Input:  [2,1,3]
Output: true
```

**Example 2**
```
Input:  [5,1,4,null,null,3,6]
Output: false   (3 is in the right subtree of 5 but smaller than 5)
```

**Constraints**
* `1 <= n <= 10^4`; `-2^31 <= Node.val <= 2^31 - 1`
''',
approach=r'''
**Pass down bounds.** `valid(n, low, high)` requires `low < n.val < high`; the left child gets `(low, n.val)` and the right child
`(n.val, high)`. Use `long` bounds so values equal to `Integer.MIN_VALUE` / `MAX_VALUE` work.

* Time: **O(n)** — each node is checked once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class ValidateBST {

    public boolean isValidBST(TreeNode root) {
        return valid(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean valid(TreeNode n, long low, long high) {
        if (n == null) return true;
        if (n.val <= low || n.val >= high) return false;
        return valid(n.left, low, n.val) && valid(n.right, n.val, high);
    }
}
''',
test=r'''
class ValidateBSTTest {

    private final ValidateBST solution = new ValidateBST();

    @Test
    void valid() {
        assertTrue(solution.isValidBST(TreeNode.of(2, 1, 3)));
    }

    @Test
    void deepViolation() {
        assertFalse(solution.isValidBST(TreeNode.of(5, 1, 4, null, null, 3, 6)));
        assertFalse(solution.isValidBST(TreeNode.of(5, 4, 6, null, null, 3, 7)));
    }

    @Test
    void duplicatesAndExtremes() {
        assertFalse(solution.isValidBST(TreeNode.of(2, 2, 2)));
        assertTrue(solution.isValidBST(TreeNode.of(2147483647)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {};
  const fmt = x => (x === -Infinity ? '−∞' : x === Infinity ? '+∞' : x);
  A.step('Each node must stay strictly inside the window of values allowed by its ancestors.', A.tree('tree', root));
  const ok = (function valid(n, lo, hi) {
    if (!n) return true;
    const good = n.val > lo && n.val < hi;
    hl[n.id] = good ? 'ok' : 'bad';
    A.step(`${n.val} must be between ${fmt(lo)} and ${fmt(hi)}. ${good ? 'It is.' : 'It is not, so this is not a BST.'}`, A.tree('tree', root, { hl: { ...hl, ...(good ? { [n.id]: 'cur' } : {}) } }), A.vars({ low: fmt(lo), high: fmt(hi) }));
    return good && valid(n.left, lo, n.val) && valid(n.right, n.val, hi);
  })(root, -Infinity, Infinity);
  A.step(ok ? 'Every node respected its window. Valid BST.' : 'A node broke its window.', A.tree('tree', root, { hl }), A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('Valid', '[5,3,8,1,4,7,9]', () => run([5, 3, 8, 1, 4, 7, 9]));
A.scenario('Deep violation', '[5,4,6,null,null,3,7]', () => run([5, 4, 6, null, null, 3, 7]));
''',
variants=[dict(
name="In-order must increase",
idea="A BST's in-order traversal is strictly increasing; check each value against the previous one.",
approach=r'''
**Sorted check.** Traverse in order, keeping the previous value; any value not greater than it means the tree is not a BST.

* Time: **O(n)** — one traversal.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class ValidateBST {

    private Integer prev;

    public boolean isValidBST(TreeNode root) {
        prev = null;
        return inorder(root);
    }

    private boolean inorder(TreeNode n) {
        if (n == null) return true;
        if (!inorder(n.left)) return false;
        if (prev != null && n.val <= prev) return false;
        prev = n.val;
        return inorder(n.right);
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), seq = [], hl = {}; let prev = null, bad = false;
  (function ino(n) {
    if (!n || bad) return;
    ino(n.left); if (bad) return;
    seq.push(n.val);
    if (prev !== null && n.val <= prev) { bad = true; hl[n.id] = 'bad'; A.step(`${n.val} comes after ${prev} in order but is not larger. Not a BST.`, A.tree('tree', root, { hl }), A.arr('in-order', seq, { hl: { [seq.length - 1]: 'bad' } })); return; }
    hl[n.id] = 'ok'; prev = n.val;
    A.step(`In-order visits ${n.val}: still increasing.`, A.tree('tree', root, { hl }), A.arr('in-order', seq));
    ino(n.right);
  })(root);
  A.step(bad ? 'Invalid BST.' : 'The in-order sequence is strictly increasing. Valid BST.', A.text('Result', String(!bad), bad ? 'bad' : 'ok'));
}
A.scenario('Deep violation', '[5,4,6,null,null,3,7]', () => run([5, 4, 6, null, null, 3, 7]));
''')]),

P(num=200, slug="number-of-islands", title="Number of Islands", diff="Medium", topic="Graph General", cls="NumberOfIslands",
idea="Scan the grid; each unvisited land cell starts a new island, which a flood fill sinks completely.",
vname="DFS flood fill",
spec=r'''
Given an `m × n` grid of `'1'` (land) and `'0'` (water), count the **islands**. An island is a group of land cells connected
horizontally or vertically; the grid is surrounded by water.

**Example 1**
```
Input:
11110
11010
11000
00000
Output: 1
```

**Example 2**
```
Input:
11000
11000
00100
00011
Output: 3
```

**Constraints**
* `1 <= m, n <= 300`
''',
approach=r'''
**Flood fill.** For each `'1'`, count one island and run DFS to turn the whole connected region into `'0'`, so it is never counted
again. (Iterative DFS with an explicit stack avoids deep recursion on large islands.)

* Time: **O(m·n)** — each cell is visited a constant number of times.
* Space: **O(m·n)** — the stack in the worst case (one giant island).
''',
tc="n2", sc="n2",
java=r'''
public class NumberOfIslands {

    public int numIslands(char[][] grid) {
        int m = grid.length, n = grid[0].length, islands = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] != '1') continue;
                islands++;
                Deque<int[]> stack = new ArrayDeque<>();
                stack.push(new int[]{r, c});
                grid[r][c] = '0';
                while (!stack.isEmpty()) {
                    int[] cell = stack.pop();
                    for (int[] d : dirs) {
                        int nr = cell[0] + d[0], nc = cell[1] + d[1];
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == '1') {
                            grid[nr][nc] = '0';
                            stack.push(new int[]{nr, nc});
                        }
                    }
                }
            }
        }
        return islands;
    }
}
''',
test=r'''
class NumberOfIslandsTest {

    private final NumberOfIslands solution = new NumberOfIslands();

    private static char[][] grid(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    @Test
    void oneIsland() {
        assertEquals(1, solution.numIslands(grid("11110", "11010", "11000", "00000")));
    }

    @Test
    void threeIslands() {
        assertEquals(3, solution.numIslands(grid("11000", "11000", "00100", "00011")));
    }

    @Test
    void noLand() {
        assertEquals(0, solution.numIslands(grid("000")));
    }
}
''',
trace=r'''
function run(rows) {
  const g = rows.map(r => [...r]), m = g.length, n = g[0].length, color = {};
  const hues = ['ok', 'sel', 'alt', 'cur'];
  const view = () => A.grid('grid', g.map(r => r.map(() => '')), { hl: Object.entries(color).concat(rows.flatMap((r, i) => [...r].map((ch, j) => (ch === '1' && !color[`${i},${j}`] ? [`${i},${j}`, 'bar'] : null)).filter(Boolean))) });
  let count = 0;
  A.step('Grey cells are unvisited land. Scan the grid; each new land cell starts an island, and a flood fill colours all of it.', view(), A.vars({ islands: 0 }));
  for (let r = 0; r < m; r++) for (let c = 0; c < n; c++) {
    if (g[r][c] !== '1') continue;
    count++; const hue = hues[(count - 1) % hues.length];
    const st = [[r, c]]; g[r][c] = '0'; color[`${r},${c}`] = hue; let size = 1;
    while (st.length) { const [x, y] = st.pop(); for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const a = x + dx, b = y + dy; if (a >= 0 && a < m && b >= 0 && b < n && g[a][b] === '1') { g[a][b] = '0'; color[`${a},${b}`] = hue; st.push([a, b]); size++; } } }
    A.step(`Land at (${r},${c}) is new: island #${count}. The flood fill marks all ${size} of its cells as visited.`, view(), A.vars({ islands: count }));
  }
  A.step(`The scan is complete. There ${count === 1 ? 'is 1 island' : `are ${count} islands`}.`, view(), A.text('Result', count, 'ok'));
}
A.scenario('Three islands', 'the second example', () => run(['11000', '11000', '00100', '00011']));
A.scenario('One big island', 'the first example', () => run(['11110', '11010', '11000', '00000']));
''',
variants=[dict(
name="BFS flood fill",
idea="Same scan, but explore each island breadth-first with a queue.",
approach=r'''
**Queue instead of stack.** Each new land cell is enqueued and marked; neighbours are explored level by level.

* Time: **O(m·n)** — each cell is processed once.
* Space: **O(min(m, n))** — the BFS frontier of a grid stays roughly as wide as its smaller side.
''',
tc="n2", sc="n",
java=r'''
public class NumberOfIslands {

    public int numIslands(char[][] grid) {
        int m = grid.length, n = grid[0].length, islands = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] != '1') continue;
                islands++;
                Deque<int[]> queue = new ArrayDeque<>();
                queue.add(new int[]{r, c});
                grid[r][c] = '0';
                while (!queue.isEmpty()) {
                    int[] cell = queue.poll();
                    for (int[] d : dirs) {
                        int nr = cell[0] + d[0], nc = cell[1] + d[1];
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == '1') {
                            grid[nr][nc] = '0';
                            queue.add(new int[]{nr, nc});
                        }
                    }
                }
            }
        }
        return islands;
    }
}
''',
trace=r'''
function run(rows) {
  const g = rows.map(r => [...r]), m = g.length, n = g[0].length, color = {};
  let count = 0;
  for (let r = 0; r < m; r++) for (let c = 0; c < n; c++) {
    if (g[r][c] !== '1') continue;
    count++; let q = [[r, c]]; g[r][c] = '0'; let wave = 0;
    while (q.length) {
      q.forEach(([x, y]) => (color[`${x},${y}`] = wave ? 'sel' : 'cur'));
      A.step(`Island #${count}, BFS wave ${wave}: ${q.length} cell${q.length > 1 ? 's' : ''}.`, A.grid('grid', g.map(rw => rw.map(() => '')), { hl: Object.entries(color).concat(rows.flatMap((rw, i) => [...rw].map((ch, j) => (ch === '1' && !color[`${i},${j}`] ? [`${i},${j}`, 'bar'] : null)).filter(Boolean))) }), A.vars({ islands: count }));
      q.forEach(([x, y]) => (color[`${x},${y}`] = 'ok'));
      const nq = [];
      for (const [x, y] of q) for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const a = x + dx, b = y + dy; if (a >= 0 && a < m && b >= 0 && b < n && g[a][b] === '1') { g[a][b] = '0'; nq.push([a, b]); } }
      q = nq; wave++;
    }
  }
  A.step(`${count} islands.`, A.text('Result', count, 'ok'));
}
A.scenario('One big island', 'the first example', () => run(['11110', '11010', '11000', '00000']));
''')]),

P(num=130, slug="surrounded-regions", title="Surrounded Regions", diff="Medium", topic="Graph General", cls="SurroundedRegions",
idea="Only O regions touching the border survive; mark them from the border, then flip everything else.",
vname="Flood fill from the border",
spec=r'''
Given an `m × n` board of `'X'` and `'O'`, capture every region of `'O'` that is **completely surrounded** by `'X'` (connected
horizontally or vertically) by flipping it to `'X'`. Regions touching the border are not surrounded.

**Example**
```
Input:          Output:
X X X X         X X X X
X O O X         X X X X
X X O X         X X X X
X O X X         X O X X
```

**Constraints**
* `1 <= m, n <= 200`
''',
approach=r'''
**Think in reverse.** Flood fill from every border `'O'` and mark its region as safe (`'#'`). Then scan: remaining `'O'` cells are
surrounded, so flip them to `'X'`; turn `'#'` back into `'O'`.

* Time: **O(m·n)** — each cell is visited a constant number of times.
* Space: **O(m·n)** — the flood-fill stack in the worst case.
''',
tc="n2", sc="n2",
java=r'''
public class SurroundedRegions {

    public void solve(char[][] board) {
        int m = board.length, n = board[0].length;
        Deque<int[]> stack = new ArrayDeque<>();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if ((r == 0 || c == 0 || r == m - 1 || c == n - 1) && board[r][c] == 'O') {
                    board[r][c] = '#';
                    stack.push(new int[]{r, c});
                }
            }
        }
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.isEmpty()) {
            int[] cell = stack.pop();
            for (int[] d : dirs) {
                int nr = cell[0] + d[0], nc = cell[1] + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && board[nr][nc] == 'O') {
                    board[nr][nc] = '#';
                    stack.push(new int[]{nr, nc});
                }
            }
        }
        for (char[] row : board) {
            for (int c = 0; c < n; c++) {
                row[c] = row[c] == '#' ? 'O' : 'X';
            }
        }
    }
}
''',
test=r'''
class SurroundedRegionsTest {

    private final SurroundedRegions solution = new SurroundedRegions();

    private static char[][] board(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    @Test
    void example() {
        char[][] b = board("XXXX", "XOOX", "XXOX", "XOXX");
        solution.solve(b);
        assertArrayEquals(board("XXXX", "XXXX", "XXXX", "XOXX"), b);
    }

    @Test
    void borderConnected() {
        char[][] b = board("OOO", "OXO", "OOO");
        solution.solve(b);
        assertArrayEquals(board("OOO", "OXO", "OOO"), b);
    }

    @Test
    void single() {
        char[][] b = board("X");
        solution.solve(b);
        assertArrayEquals(board("X"), b);
    }
}
''',
trace=r'''
function run(rows) {
  const b = rows.map(r => [...r]), m = b.length, n = b[0].length;
  const view = (msg, extra = {}) => A.step(msg, A.grid('board', b, { hl: b.flatMap((r, i) => r.map((ch, j) => [`${i},${j}`, extra[`${i},${j}`] || (ch === '#' ? 'ok' : ch === 'O' ? 'sel' : 'dim')])) }));
  view('O regions that touch the border can never be surrounded. Start from the border.');
  const st = [];
  for (let r = 0; r < m; r++) for (let c = 0; c < n; c++) if ((r === 0 || c === 0 || r === m - 1 || c === n - 1) && b[r][c] === 'O') { b[r][c] = '#'; st.push([r, c]); }
  view(`Mark the ${st.length} border O cell${st.length === 1 ? '' : 's'} as safe (#).`);
  while (st.length) { const [x, y] = st.pop(); for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const a = x + dx, c = y + dy; if (a >= 0 && a < m && c >= 0 && c < n && b[a][c] === 'O') { b[a][c] = '#'; st.push([a, c]); view(`(${a},${c}) connects to a safe cell, so it is safe too.`, { [`${a},${c}`]: 'cur' }); } } }
  const flipped = {};
  b.forEach((r, i) => r.forEach((ch, j) => { if (ch === 'O') flipped[`${i},${j}`] = 'bad'; }));
  view('Any O still unmarked is surrounded by X.', flipped);
  b.forEach(r => r.forEach((ch, j) => (r[j] = ch === '#' ? 'O' : 'X')));
  view('Flip surrounded O cells to X and restore the safe ones to O.');
}
A.scenario('Classic', '4 × 4 board', () => run(['XXXX', 'XOOX', 'XXOX', 'XOXX']));
A.scenario('Region reaching the border', '5 × 5 board', () => run(['XXXXX', 'XOOXX', 'XXOXX', 'XXOOO', 'XOXXX']));
'''),
]
