PROBLEMS = [
P(num=101, slug="symmetric-tree", title="Symmetric Tree", diff="Easy", topic="Binary Tree General", cls="SymmetricTree",
idea="A tree is symmetric when its left subtree mirrors its right: outer pairs and inner pairs must both match.",
vname="Recursive mirror check", helpers=["TreeNode"],
spec=r'''
Return `true` if a binary tree is a mirror of itself (symmetric around its centre).

**Example 1**
```
Input:  [1,2,2,3,4,4,3]
Output: true
```

**Example 2**
```
Input:  [1,2,2,null,3,null,3]
Output: false
```

**Constraints**
* `1 <= n <= 1000`; `-100 <= Node.val <= 100`
''',
approach=r'''
**Mirror pairs.** `mirror(a, b)`: both null → true; one null or values differ → false; otherwise
`mirror(a.left, b.right) && mirror(a.right, b.left)`. Start with `mirror(root.left, root.right)`.

* Time: **O(n)** — each node is compared once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class SymmetricTree {

    public boolean isSymmetric(TreeNode root) {
        return root == null || mirror(root.left, root.right);
    }

    private boolean mirror(TreeNode a, TreeNode b) {
        if (a == null || b == null) return a == b;
        return a.val == b.val && mirror(a.left, b.right) && mirror(a.right, b.left);
    }
}
''',
test=r'''
class SymmetricTreeTest {

    private final SymmetricTree solution = new SymmetricTree();

    @Test
    void symmetric() {
        assertTrue(solution.isSymmetric(TreeNode.of(1, 2, 2, 3, 4, 4, 3)));
    }

    @Test
    void notSymmetric() {
        assertFalse(solution.isSymmetric(TreeNode.of(1, 2, 2, null, 3, null, 3)));
    }

    @Test
    void single() {
        assertTrue(solution.isSymmetric(TreeNode.of(1)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {};
  A.step('Compare the left subtree with the mirror image of the right subtree.', A.tree('tree', root, { hl: { [root.id]: 'alt' } }));
  function mirror(a, b) {
    if (!a || !b) { if (a !== b) { hl[(a || b).id] = 'bad'; A.step(`Node ${(a || b).val} has no mirror partner. Not symmetric.`, A.tree('tree', root, { hl })); } return a === b; }
    hl[a.id] = hl[b.id] = 'cur';
    if (a.val !== b.val) { hl[a.id] = hl[b.id] = 'bad'; A.step(`${a.val} and ${b.val} are mirror partners but differ. Not symmetric.`, A.tree('tree', root, { hl })); return false; }
    A.step(`${a.val} mirrors ${b.val}. Next compare outer with outer, and inner with inner.`, A.tree('tree', root, { hl }));
    hl[a.id] = hl[b.id] = 'ok';
    return mirror(a.left, b.right) && mirror(a.right, b.left);
  }
  const r = mirror(root.left, root.right);
  A.step(r ? 'Every pair matched, so the tree is symmetric.' : 'A pair did not match.', A.tree('tree', root, { hl }), A.text('Result', String(r), r ? 'ok' : 'bad'));
}
A.scenario('Symmetric', '[1,2,2,3,4,4,3]', () => run([1, 2, 2, 3, 4, 4, 3]));
A.scenario('Not symmetric', '[1,2,2,null,3,null,3]', () => run([1, 2, 2, null, 3, null, 3]));
''',
variants=[dict(
name="Iterative queue of pairs",
idea="Push mirror pairs onto a queue and check them one by one.",
approach=r'''
**Queue of pairs.** Start with `(root.left, root.right)`. Pop a pair; skip if both null; fail if one is null or the values differ;
otherwise push `(a.left, b.right)` and `(a.right, b.left)`.

* Time: **O(n)** — each node is enqueued once.
* Space: **O(w)** — the queue holds about one level.
''',
tc="n", sc="n",
java=r'''
public class SymmetricTree {

    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        Deque<TreeNode> queue = new LinkedList<>();
        queue.add(root.left);
        queue.add(root.right);
        while (!queue.isEmpty()) {
            TreeNode a = queue.poll(), b = queue.poll();
            if (a == null && b == null) continue;
            if (a == null || b == null || a.val != b.val) return false;
            queue.add(a.left);
            queue.add(b.right);
            queue.add(a.right);
            queue.add(b.left);
        }
        return true;
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), q = [[root.left, root.right]], hl = {};
  while (q.length) {
    const [a, b] = q.shift();
    if (!a && !b) continue;
    if (!a || !b || a.val !== b.val) { [a, b].forEach(x => x && (hl[x.id] = 'bad')); A.step('A pair does not match. Not symmetric.', A.tree('tree', root, { hl }), A.text('Result', 'false', 'bad')); return; }
    hl[a.id] = hl[b.id] = 'ok';
    q.push([a.left, b.right], [a.right, b.left]);
    A.step(`Pair (${a.val}, ${b.val}) matches. Queue its outer and inner child pairs.`, A.tree('tree', root, { hl }), A.arr('queued pairs', q.map(([x, y]) => `(${x ? x.val : '∅'},${y ? y.val : '∅'})`)));
  }
  A.step('All pairs matched. Symmetric.', A.text('Result', 'true', 'ok'));
}
A.scenario('Symmetric', '[1,2,2,3,4,4,3]', () => run([1, 2, 2, 3, 4, 4, 3]));
''')]),

P(num=105, slug="construct-binary-tree-from-preorder-and-inorder-traversal", title="Construct Binary Tree from Preorder and Inorder Traversal", diff="Medium", topic="Binary Tree General", cls="BuildTreePreIn",
idea="Preorder's first value is the root; its position in inorder splits the left and right subtrees.",
vname="Hash map of inorder positions", helpers=["TreeNode"],
spec=r'''
Given the `preorder` and `inorder` traversals of a binary tree with **unique** values, build and return the tree.

**Example 1**
```
Input:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2**
```
Input:  preorder = [-1], inorder = [-1]
Output: [-1]
```

**Constraints**
* `1 <= n <= 3000`; values are unique.
''',
approach=r'''
**Divide by the root.** The next unused preorder value is the root of the current inorder range `[lo, hi]`. Its inorder index `m`
splits the range: `[lo, m-1]` is the left subtree, `[m+1, hi]` the right. Build left first, because preorder lists the left subtree
before the right. A `MyHashMap` from value to inorder index makes each split O(1).

* Time: **O(n)** — one map lookup per node.
* Space: **O(n)** — the map and the recursion stack.
''',
java=r'''
public class BuildTreePreIn {

    private int next;
    private MyHashMap<Integer, Integer> inorderIndex;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        inorderIndex = new MyHashMap<>();
        for (int i = 0; i < inorder.length; i++) inorderIndex.put(inorder[i], i);
        next = 0;
        return build(preorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int lo, int hi) {
        if (lo > hi) return null;
        TreeNode root = new TreeNode(preorder[next++]);
        int m = inorderIndex.get(root.val);
        root.left = build(preorder, lo, m - 1);
        root.right = build(preorder, m + 1, hi);
        return root;
    }
}
''',
test=r'''
class BuildTreePreInTest {

    private final BuildTreePreIn solution = new BuildTreePreIn();

    @Test
    void example1() {
        assertEquals(Arrays.asList(3, 9, 20, null, null, 15, 7), TreeNode.toList(solution.buildTree(new int[]{3, 9, 20, 15, 7}, new int[]{9, 3, 15, 20, 7})));
    }

    @Test
    void single() {
        assertEquals(List.of(-1), TreeNode.toList(solution.buildTree(new int[]{-1}, new int[]{-1})));
    }

    @Test
    void leftChain() {
        assertEquals(Arrays.asList(3, 2, null, 1), TreeNode.toList(solution.buildTree(new int[]{3, 2, 1}, new int[]{1, 2, 3})));
    }
}
''',
trace=r'''
function run(pre, ino) {
  let next = 0; const idx = new Map(ino.map((v, i) => [v, i]));
  let root = null;
  A.step('Map each value to its inorder position. Preorder gives the roots in order; inorder tells what is left and right of each root.', A.arr('preorder', pre), A.arr('inorder', ino), A.hashTable('value → inorder index', idx));
  function build(lo, hi, attach) {
    if (lo > hi) return null;
    const v = pre[next], n = A.node(v), m = idx.get(v);
    if (!root) root = n; attach(n);
    A.step(`preorder[${next}] = ${v} is the root of inorder range ${lo}..${hi}. It sits at inorder index ${m}: left subtree ${lo}..${m - 1}, right subtree ${m + 1}..${hi}.`, A.arr('preorder', pre, { hl: { [next]: 'cur' } }), A.arr('inorder', ino, { range: [lo, hi], hl: { [m]: 'cur' } }), A.tree('tree being built', root, { hl: { [n.id]: 'cur' } }));
    next++;
    build(lo, m - 1, c => (n.left = c));
    build(m + 1, hi, c => (n.right = c));
    return n;
  }
  build(0, ino.length - 1, () => {});
  A.step('Every value has been placed.', A.tree('tree', root), A.text('Result', 'tree built', 'ok'));
}
A.scenario('Classic', 'preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]', () => run([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]));
''',
variants=[dict(
name="Linear search for the root",
idea="Same divide-and-conquer, but scan the inorder range to find each root.",
approach=r'''
**No map.** Find the root's inorder position by scanning `inorder[lo..hi]`.

* Time: **O(n²)** — a skewed tree makes each scan linear.
* Space: **O(h)** — the recursion stack.
''',
tc="n2", sc="n",
java=r'''
public class BuildTreePreIn {

    private int next;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        next = 0;
        return build(preorder, inorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int[] inorder, int lo, int hi) {
        if (lo > hi) return null;
        TreeNode root = new TreeNode(preorder[next++]);
        int m = lo;
        while (inorder[m] != root.val) m++;
        root.left = build(preorder, inorder, lo, m - 1);
        root.right = build(preorder, inorder, m + 1, hi);
        return root;
    }
}
''',
trace=r'''
function run(pre, ino) {
  let next = 0, root = null, scans = 0;
  function build(lo, hi, attach) {
    if (lo > hi) return;
    const v = pre[next++], n = A.node(v); if (!root) root = n; attach(n);
    let m = lo; while (ino[m] !== v) { m++; scans++; }
    scans++;
    A.step(`Root ${v}: scan inorder ${lo}..${hi} to find it at ${m}.`, A.arr('inorder', ino, { range: [lo, hi], hl: { [m]: 'cur' } }), A.tree('tree', root, { hl: { [n.id]: 'cur' } }), A.vars({ comparisons: scans }));
    build(lo, m - 1, c => (n.left = c)); build(m + 1, hi, c => (n.right = c));
  }
  build(0, ino.length - 1, () => {});
  A.step(`Done after ${scans} comparisons. A skewed tree needs about n²/2.`, A.tree('tree', root));
}
A.scenario('Skewed tree', 'preorder = [1,2,3,4], inorder = [4,3,2,1]', () => run([1, 2, 3, 4], [4, 3, 2, 1]));
''')]),

P(num=106, slug="construct-binary-tree-from-inorder-and-postorder-traversal", title="Construct Binary Tree from Inorder and Postorder Traversal", diff="Medium", topic="Binary Tree General", cls="BuildTreeInPost",
idea="Postorder's last value is the root; build the right subtree first while walking postorder backwards.",
vname="Hash map, walk postorder backwards", helpers=["TreeNode"],
spec=r'''
Given the `inorder` and `postorder` traversals of a binary tree with **unique** values, build and return the tree.

**Example 1**
```
Input:  inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
```

**Example 2**
```
Input:  inorder = [-1], postorder = [-1]
Output: [-1]
```

**Constraints**
* `1 <= n <= 3000`; values are unique.
''',
approach=r'''
**Mirror of the preorder version.** Read postorder from the end: each value is the root of the current inorder range. Split at its
inorder index (from a `MyHashMap`), and build the **right** subtree before the left, because postorder read backwards visits
root, right, left.

* Time: **O(n)** — one map lookup per node.
* Space: **O(n)** — the map and the recursion stack.
''',
java=r'''
public class BuildTreeInPost {

    private int next;
    private MyHashMap<Integer, Integer> inorderIndex;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        inorderIndex = new MyHashMap<>();
        for (int i = 0; i < inorder.length; i++) inorderIndex.put(inorder[i], i);
        next = postorder.length - 1;
        return build(postorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] postorder, int lo, int hi) {
        if (lo > hi) return null;
        TreeNode root = new TreeNode(postorder[next--]);
        int m = inorderIndex.get(root.val);
        root.right = build(postorder, m + 1, hi);
        root.left = build(postorder, lo, m - 1);
        return root;
    }
}
''',
test=r'''
class BuildTreeInPostTest {

    private final BuildTreeInPost solution = new BuildTreeInPost();

    @Test
    void example1() {
        assertEquals(Arrays.asList(3, 9, 20, null, null, 15, 7), TreeNode.toList(solution.buildTree(new int[]{9, 3, 15, 20, 7}, new int[]{9, 15, 7, 20, 3})));
    }

    @Test
    void single() {
        assertEquals(List.of(-1), TreeNode.toList(solution.buildTree(new int[]{-1}, new int[]{-1})));
    }

    @Test
    void rightChain() {
        assertEquals(Arrays.asList(1, null, 2, null, 3), TreeNode.toList(solution.buildTree(new int[]{1, 2, 3}, new int[]{3, 2, 1})));
    }
}
''',
trace=r'''
function run(ino, post) {
  let next = post.length - 1, root = null; const idx = new Map(ino.map((v, i) => [v, i]));
  A.step('Read postorder from the end: root, then the right subtree, then the left.', A.arr('inorder', ino), A.arr('postorder', post), A.hashTable('value → inorder index', idx));
  function build(lo, hi, attach) {
    if (lo > hi) return;
    const v = post[next], n = A.node(v), m = idx.get(v); if (!root) root = n; attach(n);
    A.step(`postorder[${next}] = ${v} is the root of inorder ${lo}..${hi}. Build its right part ${m + 1}..${hi} first, then its left part ${lo}..${m - 1}.`, A.arr('postorder', post, { hl: { [next]: 'cur' } }), A.arr('inorder', ino, { range: [lo, hi], hl: { [m]: 'cur' } }), A.tree('tree being built', root, { hl: { [n.id]: 'cur' } }));
    next--;
    build(m + 1, hi, c => (n.right = c)); build(lo, m - 1, c => (n.left = c));
  }
  build(0, ino.length - 1, () => {});
  A.step('The tree is complete.', A.tree('tree', root), A.text('Result', 'tree built', 'ok'));
}
A.scenario('Classic', 'inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]', () => run([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]));
'''),

P(num=117, slug="populating-next-right-pointers-in-each-node-ii", title="Populating Next Right Pointers in Each Node II", diff="Medium", topic="Binary Tree General", cls="PopulatingNextRight",
idea="Walk each level through the next pointers already set, and link the children into the level below.",
vname="Level walk with O(1) space",
spec=r'''
Each node of a binary tree has an extra pointer `next`. Set every `next` to the node immediately to its right on the same level, or
to `null` if there is none. The tree is not necessarily perfect.

**Example**
```
Input:  [1,2,3,4,5,null,7]
Output: levels linked as  1 → null,  2 → 3 → null,  4 → 5 → 7 → null
```

**Constraints**
* `0 <= n <= 6000`; `-100 <= Node.val <= 100`

**Follow-up:** constant extra space (the recursion stack does not count).
''',
approach=r'''
**Use the current level as a linked list.** Starting from `levelStart`, walk the level through `next`. For each node, append its
children to a chain for the next level, using a `dummy` head and a `tail` pointer. When the level ends, move to `dummy.next`.

* Time: **O(n)** — each node is visited once.
* Space: **O(1)** — a dummy node and two pointers.
''',
java=r'''
public class PopulatingNextRight {

    /** Tree node with a next pointer. */
    public static class Node {
        public int val;
        public Node left, right, next;

        public Node(int val) { this.val = val; }

        public Node(int val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public Node connect(Node root) {
        Node levelStart = root;
        while (levelStart != null) {
            Node dummy = new Node(0), tail = dummy;
            for (Node n = levelStart; n != null; n = n.next) {
                if (n.left != null) { tail.next = n.left; tail = tail.next; }
                if (n.right != null) { tail.next = n.right; tail = tail.next; }
            }
            levelStart = dummy.next;
        }
        return root;
    }
}
''',
test=r'''
class PopulatingNextRightTest {

    private final PopulatingNextRight solution = new PopulatingNextRight();

    private static List<String> levels(PopulatingNextRight.Node root) {
        List<String> out = new ArrayList<>();
        for (PopulatingNextRight.Node start = root; start != null; ) {
            StringBuilder sb = new StringBuilder();
            PopulatingNextRight.Node nextStart = null;
            for (PopulatingNextRight.Node n = start; n != null; n = n.next) {
                sb.append(n.val).append(' ');
                if (nextStart == null) nextStart = n.left != null ? n.left : n.right;
            }
            out.add(sb.toString().trim());
            PopulatingNextRight.Node probe = start;
            while (nextStart == null && probe != null) {
                nextStart = probe.left != null ? probe.left : probe.right;
                probe = probe.next;
            }
            start = nextStart;
        }
        return out;
    }

    @Test
    void example() {
        var n4 = new PopulatingNextRight.Node(4);
        var n5 = new PopulatingNextRight.Node(5);
        var n7 = new PopulatingNextRight.Node(7);
        var root = new PopulatingNextRight.Node(1, new PopulatingNextRight.Node(2, n4, n5), new PopulatingNextRight.Node(3, null, n7));
        solution.connect(root);
        assertEquals(List.of("1", "2 3", "4 5 7"), levels(root));
        assertNull(n7.next);
    }

    @Test
    void empty() {
        assertNull(solution.connect(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr);
  let start = root;
  A.step('Walk each level through its next pointers, linking the children into the level below as we go.', A.tree('tree', root, { next: true }));
  while (start) {
    const dummy = { next: null }; let tail = dummy; const hl = {};
    for (let n = start; n; n = n.next) {
      hl[n.id] = 'cur';
      for (const c of [n.left, n.right]) if (c) { tail.next = c; tail = c; hl[c.id] = 'ok'; }
      A.step(`At ${n.val}: append its children to the next level's chain${tail !== dummy ? `, which now ends at ${tail.val}` : ''}.`, A.tree('tree', root, { next: true, hl }));
      hl[n.id] = 'sel';
    }
    start = dummy.next;
  }
  A.step('Every level is linked left to right. The dashed arrows are the next pointers.', A.tree('tree', root, { next: true }));
}
A.scenario('Gaps in the tree', '[1,2,3,4,5,null,7]', () => run([1, 2, 3, 4, 5, null, 7]));
''',
variants=[dict(
name="BFS with a queue",
idea="Process the tree level by level; link each node to the next one in its level.",
approach=r'''
**Level-order queue.** For each level, pop its nodes in order and set `prev.next = node`.

* Time: **O(n)** — each node is enqueued once.
* Space: **O(w)** — the queue holds a whole level.
''',
tc="n", sc="n",
java=r'''
public class PopulatingNextRight {

    /** Tree node with a next pointer. */
    public static class Node {
        public int val;
        public Node left, right, next;

        public Node(int val) { this.val = val; }

        public Node(int val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public Node connect(Node root) {
        if (root == null) return null;
        Deque<Node> queue = new ArrayDeque<>(List.of(root));
        while (!queue.isEmpty()) {
            Node prev = null;
            for (int size = queue.size(); size > 0; size--) {
                Node n = queue.poll();
                if (prev != null) prev.next = n;
                prev = n;
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
        }
        return root;
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr); let q = [root];
  while (q.length) {
    for (let i = 0; i + 1 < q.length; i++) q[i].next = q[i + 1];
    A.step(`Level ${q.map(n => n.val).join(', ')}: link each node to the next one in the queue.`, A.tree('tree', root, { next: true, hl: Object.fromEntries(q.map(n => [n.id, 'ok'])) }), A.arr('queue', q.map(n => n.val)));
    q = q.flatMap(n => [n.left, n.right].filter(Boolean));
  }
}
A.scenario('Gaps in the tree', '[1,2,3,4,5,null,7]', () => run([1, 2, 3, 4, 5, null, 7]));
''')]),

P(num=114, slug="flatten-binary-tree-to-linked-list", title="Flatten Binary Tree to Linked List", diff="Medium", topic="Binary Tree General", cls="FlattenTree",
idea="For each node with a left child, splice the left subtree between the node and its right subtree.",
vname="In-place splicing (O(1) space)", helpers=["TreeNode"],
spec=r'''
Flatten a binary tree **in place** into a "linked list" that uses the `right` pointers, with every `left` set to `null`, in
**preorder** order.

**Example**
```
Input:  [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

**Constraints**
* `0 <= n <= 2000`

**Follow-up:** O(1) extra space.
''',
approach=r'''
**Splice like Morris traversal.** For the current node with a left child, find the rightmost node of the left subtree (the last
node of the left part in preorder). Attach the current right subtree there, move the left subtree to the right, and clear `left`.
Advance to `right`.

* Time: **O(n)** — each edge is walked a constant number of times.
* Space: **O(1)** — no stack or list.
''',
java=r'''
public class FlattenTree {

    public void flatten(TreeNode root) {
        for (TreeNode cur = root; cur != null; cur = cur.right) {
            if (cur.left != null) {
                TreeNode rightmost = cur.left;
                while (rightmost.right != null) rightmost = rightmost.right;
                rightmost.right = cur.right;
                cur.right = cur.left;
                cur.left = null;
            }
        }
    }
}
''',
test=r'''
class FlattenTreeTest {

    private final FlattenTree solution = new FlattenTree();

    @Test
    void example() {
        TreeNode root = TreeNode.of(1, 2, 5, 3, 4, null, 6);
        solution.flatten(root);
        assertEquals(Arrays.asList(1, null, 2, null, 3, null, 4, null, 5, null, 6), TreeNode.toList(root));
    }

    @Test
    void empty() {
        solution.flatten(null);
    }

    @Test
    void leftOnly() {
        TreeNode root = TreeNode.of(1, 2);
        solution.flatten(root);
        assertEquals(Arrays.asList(1, null, 2), TreeNode.toList(root));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr);
  A.step('Goal: a right-only chain in preorder. Splice each left subtree in between a node and its right subtree.', A.tree('tree', root));
  for (let cur = root; cur; cur = cur.right) {
    if (!cur.left) { A.step(`${cur.val} has no left child. Move right.`, A.tree('tree', root, { hl: { [cur.id]: 'cur' } })); continue; }
    let rm = cur.left; while (rm.right) rm = rm.right;
    A.step(`${cur.val} has a left subtree. Its rightmost node is ${rm.val}; the right subtree of ${cur.val} will hang from there.`, A.tree('tree', root, { hl: { [cur.id]: 'cur', [rm.id]: 'alt', ...(cur.right ? { [cur.right.id]: 'sel' } : {}) } }));
    rm.right = cur.right; cur.right = cur.left; cur.left = null;
    A.step(`Moved: the left subtree is now on the right of ${cur.val}, followed by the old right subtree.`, A.tree('tree', root, { hl: { [cur.id]: 'ok' } }));
  }
  A.step('The tree is a single right-leaning chain in preorder.', A.tree('tree', root));
}
A.scenario('Classic', '[1,2,5,3,4,null,6]', () => run([1, 2, 5, 3, 4, null, 6]));
''',
variants=[dict(
name="Preorder list, then relink",
idea="Record the nodes in preorder, then link each to the next.",
approach=r'''
**Collect and relink.** A preorder traversal fills a list; then `list[i].left = null`, `list[i].right = list[i+1]`.

* Time: **O(n)** — one traversal and one relinking pass.
* Space: **O(n)** — the list of nodes.
''',
tc="n", sc="n",
java=r'''
public class FlattenTree {

    public void flatten(TreeNode root) {
        List<TreeNode> order = new ArrayList<>();
        preorder(root, order);
        for (int i = 0; i < order.size(); i++) {
            order.get(i).left = null;
            order.get(i).right = i + 1 < order.size() ? order.get(i + 1) : null;
        }
    }

    private void preorder(TreeNode n, List<TreeNode> out) {
        if (n == null) return;
        out.add(n);
        preorder(n.left, out);
        preorder(n.right, out);
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), order = [];
  (function pre(n) { if (!n) return; order.push(n); A.step(`Preorder visits ${n.val}.`, A.tree('tree', root, { hl: Object.fromEntries(order.map(x => [x.id, 'ok'])) }), A.arr('preorder list', order.map(x => x.val))); pre(n.left); pre(n.right); })(root);
  A.step('Relink: each node’s right points to the next one in the list. This used O(n) extra space.', A.list('flattened', order.map(x => x.val), { hl: order.map((_, i) => [i, 'ok']) }));
}
A.scenario('Classic', '[1,2,5,3,4,null,6]', () => run([1, 2, 5, 3, 4, null, 6]));
''')]),

P(num=112, slug="path-sum", title="Path Sum", diff="Easy", topic="Binary Tree General", cls="PathSum",
idea="Subtract each node's value from the target on the way down; a leaf must leave exactly zero.",
vname="Recursive DFS", helpers=["TreeNode"],
spec=r'''
Return `true` if the tree has a **root-to-leaf** path whose values add up to `targetSum`. A leaf has no children.

**Example 1**
```
Input:  root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true   (5 → 4 → 11 → 2)
```

**Example 2**
```
Input:  root = [1,2,3], targetSum = 5
Output: false
```

**Constraints**
* `0 <= n <= 5000`; `-1000 <= Node.val, targetSum <= 1000`
''',
approach=r'''
**Remaining sum.** At each node subtract its value. At a leaf, check whether the remainder is 0. Otherwise ask either child.

* Time: **O(n)** — each node is visited at most once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class PathSum {

    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        int rest = targetSum - root.val;
        if (root.left == null && root.right == null) return rest == 0;
        return hasPathSum(root.left, rest) || hasPathSum(root.right, rest);
    }
}
''',
test=r'''
class PathSumTest {

    private final PathSum solution = new PathSum();

    @Test
    void found() {
        assertTrue(solution.hasPathSum(TreeNode.of(5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1), 22));
    }

    @Test
    void notFound() {
        assertFalse(solution.hasPathSum(TreeNode.of(1, 2, 3), 5));
    }

    @Test
    void empty() {
        assertFalse(solution.hasPathSum(null, 0));
    }
}
''',
trace=r'''
function run(arr, target) {
  const root = A.mkTree(arr), path = [];
  A.step(`Walk down, subtracting each value from ${target}. A leaf must leave exactly 0.`, A.tree('tree', root));
  function dfs(n, rest) {
    if (!n) return false;
    path.push(n.id); rest -= n.val;
    const hl = Object.fromEntries(path.map(id => [id, 'sel']));
    if (!n.left && !n.right) {
      const ok = rest === 0; hl[n.id] = ok ? 'ok' : 'bad';
      A.step(`Leaf ${n.val}: ${rest} remains. ${ok ? 'Exactly zero, so this path works.' : 'Not zero, so backtrack.'}`, A.tree('tree', root, { hl }), A.vars({ remaining: rest }));
      if (ok) return true;
    } else {
      hl[n.id] = 'cur';
      A.step(`At ${n.val}: ${rest} remains for the rest of the path.`, A.tree('tree', root, { hl }), A.vars({ remaining: rest }));
      if (dfs(n.left, rest) || dfs(n.right, rest)) return true;
    }
    path.pop(); return false;
  }
  const r = dfs(root, target);
  A.step(r ? 'Found a root-to-leaf path with the target sum.' : 'No root-to-leaf path adds up to the target.', A.tree('tree', root, { hl: Object.fromEntries(path.map(id => [id, 'ok'])) }), A.text('Result', String(r), r ? 'ok' : 'bad'));
}
A.scenario('Path exists', 'target = 22', () => run([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], 22));
A.scenario('No path', '[1,2,3], target = 5', () => run([1, 2, 3], 5));
'''),

P(num=129, slug="sum-root-to-leaf-numbers", title="Sum Root to Leaf Numbers", diff="Medium", topic="Binary Tree General", cls="SumRootToLeaf",
idea="Carry the number formed so far down the tree (times 10 plus the digit) and add it up at the leaves.",
vname="DFS carrying the number", helpers=["TreeNode"],
spec=r'''
Every node holds a digit `0-9`. Each root-to-leaf path forms a number (e.g. `1 → 2 → 3` is `123`). Return the sum of all
these numbers.

**Example 1**
```
Input:  [1,2,3]
Output: 25   (12 + 13)
```

**Example 2**
```
Input:  [4,9,0,5,1]
Output: 1026   (495 + 491 + 40)
```

**Constraints**
* `1 <= n <= 1000`; depth at most 10; answer fits in 32 bits.
''',
approach=r'''
**Pass the prefix down.** `dfs(node, prefix)`: `value = prefix * 10 + node.val`. At a leaf return `value`; otherwise return the sum
of both children's results.

* Time: **O(n)** — each node is visited once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class SumRootToLeaf {

    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode n, int prefix) {
        if (n == null) return 0;
        int value = prefix * 10 + n.val;
        if (n.left == null && n.right == null) return value;
        return dfs(n.left, value) + dfs(n.right, value);
    }
}
''',
test=r'''
class SumRootToLeafTest {

    private final SumRootToLeaf solution = new SumRootToLeaf();

    @Test
    void small() {
        assertEquals(25, solution.sumNumbers(TreeNode.of(1, 2, 3)));
    }

    @Test
    void example2() {
        assertEquals(1026, solution.sumNumbers(TreeNode.of(4, 9, 0, 5, 1)));
    }

    @Test
    void single() {
        assertEquals(7, solution.sumNumbers(TreeNode.of(7)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr); let total = 0; const done = {};
  A.step('Carry the number formed so far down each path: multiply by 10 and add the digit.', A.tree('tree', root), A.vars({ total }));
  (function dfs(n, pre) {
    if (!n) return;
    const v = pre * 10 + n.val;
    if (!n.left && !n.right) { total += v; done[n.id] = 'ok'; A.step(`Leaf ${n.val}: this path spells ${v}. Running total: ${total}.`, A.tree('tree', root, { hl: { ...done, [n.id]: 'ok' } }), A.vars({ number: v, total })); return; }
    A.step(`At ${n.val}: the number so far is ${pre} × 10 + ${n.val} = ${v}.`, A.tree('tree', root, { hl: { ...done, [n.id]: 'cur' } }), A.vars({ number: v, total }));
    dfs(n.left, v); dfs(n.right, v);
  })(root, 0);
  A.step(`The sum of all root-to-leaf numbers is ${total}.`, A.text('Result', total, 'ok'));
}
A.scenario('Three paths', '[4,9,0,5,1]', () => run([4, 9, 0, 5, 1]));
'''),

P(num=124, slug="binary-tree-maximum-path-sum", title="Binary Tree Maximum Path Sum", diff="Hard", topic="Binary Tree General", cls="MaximumPathSum",
idea="Each node reports its best downward branch; the best path through it is the node plus both non-negative branches.",
vname="Post-order DFS with gains", helpers=["TreeNode"],
spec=r'''
A **path** is a sequence of nodes connected by edges, each node used at most once; it need not pass through the root. Return the
maximum sum of node values over all non-empty paths.

**Example 1**
```
Input:  [1,2,3]
Output: 6   (2 → 1 → 3)
```

**Example 2**
```
Input:  [-10,9,20,null,null,15,7]
Output: 42   (15 → 20 → 7)
```

**Constraints**
* `1 <= n <= 3 * 10^4`; `-1000 <= Node.val <= 1000`
''',
approach=r'''
**Gain per node.** `gain(n)` = the best sum of a path that starts at `n` and goes down one side: `n.val + max(0, gain(left), gain(right))`.
While computing it, the best path that **bends** at `n` is `n.val + max(0, gain(left)) + max(0, gain(right))`; keep the maximum
over all nodes. Negative branches are dropped (max with 0).

* Time: **O(n)** — each node is visited once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class MaximumPathSum {

    private int best;

    public int maxPathSum(TreeNode root) {
        best = Integer.MIN_VALUE;
        gain(root);
        return best;
    }

    private int gain(TreeNode n) {
        if (n == null) return 0;
        int left = Math.max(0, gain(n.left));
        int right = Math.max(0, gain(n.right));
        best = Math.max(best, n.val + left + right);
        return n.val + Math.max(left, right);
    }
}
''',
test=r'''
class MaximumPathSumTest {

    private final MaximumPathSum solution = new MaximumPathSum();

    @Test
    void small() {
        assertEquals(6, solution.maxPathSum(TreeNode.of(1, 2, 3)));
    }

    @Test
    void avoidsRoot() {
        assertEquals(42, solution.maxPathSum(TreeNode.of(-10, 9, 20, null, null, 15, 7)));
    }

    @Test
    void allNegative() {
        assertEquals(-3, solution.maxPathSum(TreeNode.of(-3)));
        assertEquals(-1, solution.maxPathSum(TreeNode.of(-2, -1)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr); let best = -Infinity; const done = {};
  A.step('Each node reports its best downward branch (its gain). The best path that bends at a node uses both branches.', A.tree('tree', root), A.vars({ best: '-∞' }));
  (function gain(n) {
    if (!n) return 0;
    const l = Math.max(0, gain(n.left)), r = Math.max(0, gain(n.right)), through = n.val + l + r;
    const nb = through > best; if (nb) best = through;
    done[n.id] = nb ? 'ok' : 'sel';
    A.step(`${n.val}: left gain ${l}, right gain ${r}. A path bending here sums to ${through}${nb ? ', a new best' : ''}. ${n.val} reports gain ${n.val + Math.max(l, r)} to its parent.`, A.tree('tree', root, { hl: { ...done, [n.id]: 'cur' } }), A.vars({ gain: n.val + Math.max(l, r), best }));
    return n.val + Math.max(l, r);
  })(root);
  A.step(`The maximum path sum is ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Path avoids the root', '[-10,9,20,null,null,15,7]', () => run([-10, 9, 20, null, null, 15, 7]));
A.scenario('Small', '[1,2,3]', () => run([1, 2, 3]));
'''),

P(num=173, slug="binary-search-tree-iterator", title="Binary Search Tree Iterator", diff="Medium", topic="Binary Tree General", cls="BSTIterator",
idea="Keep a stack of the leftmost path; next() pops a node and pushes the leftmost path of its right child.",
vname="Controlled stack", helpers=["TreeNode"],
spec=r'''
Implement an iterator over a BST that returns values in **ascending** (in-order) order:
* `BSTIterator(TreeNode root)`
* `int next()`: the next smallest value (always valid when called)
* `boolean hasNext()`

**Example**
```
root = [7,3,15,null,null,9,20]
next() → 3, next() → 7, hasNext() → true, next() → 9, next() → 15, next() → 20, hasNext() → false
```

**Constraints**
* `1 <= n <= 10^5`

**Follow-up:** O(1) average time per call and O(h) memory.
''',
approach=r'''
**Stack of pending ancestors.** Push the whole left spine from the root. `next()` pops the top (the smallest unvisited value), then
pushes the left spine of its right child.

* Time: **O(1)** — amortized per call: each node is pushed and popped once over the whole iteration.
* Space: **O(h)** — the stack holds at most one root-to-leaf path.
''',
tc="1", sc="log",
java=r'''
public class BSTIterator {

    private final Deque<TreeNode> stack = new ArrayDeque<>();

    public BSTIterator(TreeNode root) {
        pushLeft(root);
    }

    public int next() {
        TreeNode n = stack.pop();
        pushLeft(n.right);
        return n.val;
    }

    public boolean hasNext() {
        return !stack.isEmpty();
    }

    private void pushLeft(TreeNode n) {
        for (; n != null; n = n.left) stack.push(n);
    }
}
''',
test=r'''
class BSTIteratorTest {

    @Test
    void example() {
        BSTIterator it = new BSTIterator(TreeNode.of(7, 3, 15, null, null, 9, 20));
        assertEquals(3, it.next());
        assertEquals(7, it.next());
        assertTrue(it.hasNext());
        assertEquals(9, it.next());
        assertEquals(15, it.next());
        assertEquals(20, it.next());
        assertFalse(it.hasNext());
    }

    @Test
    void single() {
        BSTIterator it = new BSTIterator(TreeNode.of(1));
        assertEquals(1, it.next());
        assertFalse(it.hasNext());
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), st = [], out = [], done = {};
  const pushLeft = n => { for (; n; n = n.left) st.push(n); };
  pushLeft(root);
  A.step('The constructor pushes the left spine. The top of the stack is always the next smallest value.', A.tree('BST', root, { hl: Object.fromEntries(st.map(n => [n.id, 'sel'])) }), A.stack('stack', st.map(n => n.val)));
  while (st.length) {
    const n = st.pop(); out.push(n.val); done[n.id] = 'ok';
    pushLeft(n.right);
    A.step(`next() pops ${n.val}${n.right ? ` and pushes the left spine of its right child ${n.right.val}` : ''}.`, A.tree('BST', root, { hl: { ...done, ...Object.fromEntries(st.map(x => [x.id, 'sel'])), [n.id]: 'cur' } }), A.stack('stack', st.map(x => x.val)), A.arr('returned', out));
  }
  A.step('hasNext() is false: the stack is empty. Each node was pushed and popped exactly once.', A.arr('returned', out, { hl: out.map((_, i) => [i, 'ok']) }));
}
A.scenario('Example BST', '[7,3,15,null,null,9,20]', () => run([7, 3, 15, null, null, 9, 20]));
''',
variants=[dict(
name="Flatten to a list first",
idea="Do a full in-order traversal up front; next() just walks the list.",
approach=r'''
**Precompute.** The constructor collects all values in order into a list; `next` and `hasNext` read it with an index.

* Time: **O(1)** — per call after an O(n) constructor.
* Space: **O(n)** — the full list of values.
''',
tc="1", sc="n",
java=r'''
public class BSTIterator {

    private final List<Integer> values = new ArrayList<>();
    private int index;

    public BSTIterator(TreeNode root) {
        inorder(root);
    }

    private void inorder(TreeNode n) {
        if (n == null) return;
        inorder(n.left);
        values.add(n.val);
        inorder(n.right);
    }

    public int next() {
        return values.get(index++);
    }

    public boolean hasNext() {
        return index < values.size();
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), vals = [];
  (function ino(n) { if (!n) return; ino(n.left); vals.push(n.val); A.step(`In-order visits ${n.val}.`, A.tree('BST', root, { hl: { [n.id]: 'ok' } }), A.arr('values', vals)); ino(n.right); })(root);
  A.step('next() now just reads the list with an index, but the list holds all n values.', A.arr('values', vals, { ptr: [[0, 'index']] }));
}
A.scenario('Example BST', '[7,3,15,null,null,9,20]', () => run([7, 3, 15, null, null, 9, 20]));
''')]),

P(num=222, slug="count-complete-tree-nodes", title="Count Complete Tree Nodes", diff="Easy", topic="Binary Tree General", cls="CountCompleteTreeNodes",
idea="If the leftmost and rightmost depths match, the subtree is perfect (2^h − 1 nodes); otherwise recurse.",
vname="Perfect-subtree shortcut", helpers=["TreeNode"],
spec=r'''
Count the nodes of a **complete** binary tree: every level is full except possibly the last, which is filled from the left.

**Example 1**
```
Input:  [1,2,3,4,5,6]
Output: 6
```

**Example 2**
```
Input:  []
Output: 0
```

**Constraints**
* `0 <= n <= 5 * 10^4`; the tree is complete.

**Follow-up:** faster than O(n).
''',
approach=r'''
**Compare edge heights.** Walk down the left edge and the right edge. If both heights are `h`, the subtree is perfect and has
`2^h - 1` nodes. Otherwise count `1 + count(left) + count(right)`; one of the two halves is always perfect, so only one branch goes deep.

* Time: **O(log² n)** — O(log n) levels of recursion, each measuring heights in O(log n).
* Space: **O(log n)** — the recursion depth.
''',
tc="log", sc="log",
java=r'''
public class CountCompleteTreeNodes {

    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        int left = 0, right = 0;
        for (TreeNode n = root; n != null; n = n.left) left++;
        for (TreeNode n = root; n != null; n = n.right) right++;
        if (left == right) return (1 << left) - 1;
        return 1 + countNodes(root.left) + countNodes(root.right);
    }
}
''',
test=r'''
class CountCompleteTreeNodesTest {

    private final CountCompleteTreeNodes solution = new CountCompleteTreeNodes();

    @Test
    void lastLevelPartial() {
        assertEquals(6, solution.countNodes(TreeNode.of(1, 2, 3, 4, 5, 6)));
    }

    @Test
    void perfect() {
        assertEquals(7, solution.countNodes(TreeNode.of(1, 2, 3, 4, 5, 6, 7)));
    }

    @Test
    void empty() {
        assertEquals(0, solution.countNodes(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {};
  A.step('In a complete tree, if the left edge and the right edge have the same height, that subtree is perfect.', A.tree('tree', root));
  function count(n) {
    if (!n) return 0;
    let l = 0, r = 0; for (let x = n; x; x = x.left) l++; for (let x = n; x; x = x.right) r++;
    if (l === r) {
      const mark = x => { if (!x) return; hl[x.id] = 'ok'; mark(x.left); mark(x.right); }; mark(n);
      A.step(`Subtree at ${n.val}: left and right heights are both ${l}, so it is perfect with 2^${l} − 1 = ${(1 << l) - 1} nodes. No need to visit them.`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'cur' } }));
      return (1 << l) - 1;
    }
    hl[n.id] = 'sel';
    A.step(`Subtree at ${n.val}: left height ${l}, right height ${r}. Not perfect, so count 1 plus both children.`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'cur' } }));
    return 1 + count(n.left) + count(n.right);
  }
  const c = count(root);
  A.step(`Total: ${c} nodes.`, A.tree('tree', root, { hl }), A.text('Result', c, 'ok'));
}
A.scenario('Partial last level', '[1,2,3,4,5,6]', () => run([1, 2, 3, 4, 5, 6]));
A.scenario('Larger tree', '[1..12]', () => run([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]));
''',
variants=[dict(
name="Count every node",
idea="Ignore completeness and count all nodes recursively.",
approach=r'''
**Plain traversal.** `count(n) = n == null ? 0 : 1 + count(left) + count(right)`.

* Time: **O(n)** — every node is visited.
* Space: **O(log n)** — the recursion depth of a complete tree.
''',
tc="n", sc="log",
java=r'''
public class CountCompleteTreeNodes {

    public int countNodes(TreeNode root) {
        return root == null ? 0 : 1 + countNodes(root.left) + countNodes(root.right);
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {}; let c = 0;
  (function walk(n) { if (!n) return; c++; hl[n.id] = 'ok'; A.step(`Visit ${n.val}: ${c} so far.`, A.tree('tree', root, { hl })); walk(n.left); walk(n.right); })(root);
  A.step(`${c} nodes, after visiting every one of them.`, A.text('Result', c, 'ok'));
}
A.scenario('Partial last level', '[1,2,3,4,5,6]', () => run([1, 2, 3, 4, 5, 6]));
''')]),
]
