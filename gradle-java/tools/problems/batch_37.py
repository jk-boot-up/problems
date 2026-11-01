PROBLEMS = [
P(num=99, slug="recover-binary-search-tree", title="Recover Binary Search Tree", diff="Medium", topic="Binary Search Tree", cls="RecoverBST",
idea="In-order order of a BST is sorted; the two swapped nodes show up as the first and last 'descents'.",
vname="In-order scan for inversions", helpers=["TreeNode"],
spec=r'''
Exactly two nodes of a BST had their values swapped by mistake. Recover the tree **without changing its structure**.

**Example**
```
[1,3,null,null,2] → [3,1,null,null,2]
[3,1,4,null,null,2] → [2,1,4,null,null,3]
```

**Constraints**
* `2 <= n <= 1000`
''',
approach=r'''
**Find the inversions.** During an in-order traversal, a node smaller than its predecessor is a descent. The first swapped node is the
predecessor of the first descent; the second is the current node of the last descent (adjacent swaps give a single descent). Swap their
values back.

* Time: **O(n)** — one traversal.
* Space: **O(h)** — the traversal stack.
''',
tc="n", sc="n",
java=r'''
public class RecoverBST {

    public void recoverTree(TreeNode root) {
        TreeNode first = null, second = null, prev = null, cur = root;
        Deque<TreeNode> stack = new ArrayDeque<>();
        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            if (prev != null && cur.val < prev.val) {
                if (first == null) first = prev;
                second = cur;
            }
            prev = cur;
            cur = cur.right;
        }
        int t = first.val;
        first.val = second.val;
        second.val = t;
    }
}
''',
test=r'''
class RecoverBSTTest {

    private final RecoverBST solution = new RecoverBST();

    @Test
    void examples() {
        TreeNode a = TreeNode.of(1, 3, null, null, 2);
        solution.recoverTree(a);
        assertEquals(Arrays.asList(3, 1, null, null, 2), TreeNode.toList(a));
        TreeNode b = TreeNode.of(3, 1, 4, null, null, 2);
        solution.recoverTree(b);
        assertEquals(Arrays.asList(2, 1, 4, null, null, 3), TreeNode.toList(b));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), seq = [], nodes = [];
  (function ino(n) { if (!n) return; ino(n.left); seq.push(n.val); nodes.push(n); ino(n.right); })(root);
  A.step('An in-order walk of a BST must be increasing. Look for the places where it goes down.', A.tree('tree', root), A.arr('in-order', seq));
  let first = null, second = null;
  for (let i = 1; i < seq.length; i++) if (seq[i] < seq[i - 1]) { if (first === null) first = i - 1; second = i; A.step(`${seq[i - 1]} > ${seq[i]}: a descent.`, A.arr('in-order', seq, { hl: { [i - 1]: 'bad', [i]: 'bad' } })); }
  A.step(`The swapped values are ${seq[first]} and ${seq[second]}. Swap them back.`, A.tree('tree', root, { hl: { [nodes[first].id]: 'bad', [nodes[second].id]: 'bad' } }));
  [nodes[first].val, nodes[second].val] = [nodes[second].val, nodes[first].val];
  A.step('The tree is a valid BST again; only two values moved.', A.tree('tree', root, { hl: { [nodes[first].id]: 'ok', [nodes[second].id]: 'ok' } }));
}
A.scenario('Far apart', '[3,1,4,null,null,2]', () => run([3, 1, 4, null, null, 2]));
'''),

P(num=107, slug="binary-tree-level-order-traversal-ii", title="Binary Tree Level Order Traversal II", diff="Medium", topic="Binary Tree BFS", cls="LevelOrderBottom",
idea="A normal level-order traversal, adding each level to the front of the result.",
vname="BFS, prepend levels", helpers=["TreeNode"],
spec=r'''
Return the level-order traversal from the **bottom** level up (each level left to right).

**Example**
```
[3,9,20,null,null,15,7] → [[15,7],[9,20],[3]]
```

**Constraints**
* `0 <= n <= 2000`
''',
approach=r'''
**BFS + addFirst.** Collect each level as usual and insert it at the front of a `LinkedList`.

* Time: **O(n)** — each node once.
* Space: **O(w)** — the widest level.
''',
tc="n", sc="n",
java=r'''
public class LevelOrderBottom {

    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        LinkedList<List<Integer>> out = new LinkedList<>();
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
            out.addFirst(level);
        }
        return out;
    }
}
''',
test=r'''
class LevelOrderBottomTest {

    private final LevelOrderBottom solution = new LevelOrderBottom();

    @Test
    void examples() {
        assertEquals(List.of(List.of(15, 7), List.of(9, 20), List.of(3)), solution.levelOrderBottom(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertEquals(List.of(), solution.levelOrderBottom(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), out = [], hl = {}; let q = [root];
  while (q.length) { out.unshift(q.map(n => n.val)); q.forEach(n => (hl[n.id] = 'ok')); A.step(`Level [${q.map(n => n.val)}] goes to the front of the result.`, A.tree('tree', root, { hl }), A.arr('result (bottom up)', out.map(l => `[${l}]`), { hl: { 0: 'ok' } })); q = q.flatMap(n => [n.left, n.right].filter(Boolean)); }
}
A.scenario('Classic', '[3,9,20,null,null,15,7]', () => run([3, 9, 20, null, null, 15, 7]));
'''),

P(num=109, slug="convert-sorted-list-to-binary-search-tree", title="Convert Sorted List to Binary Search Tree", diff="Medium", topic="Divide & Conquer", cls="SortedListToBST",
idea="Build the tree in in-order: recurse on the left half's size, then consume the list node as the root, then the right half.",
vname="In-order simulation", helpers=["ListNode", "TreeNode"],
spec=r'''
Convert a sorted singly linked list into a height-balanced BST.

**Example**
```
-10 → -3 → 0 → 5 → 9  →  [0,-3,9,-10,null,5]  (one valid answer)
```

**Constraints**
* `0 <= n <= 2 * 10^4`
''',
approach=r'''
**In-order construction.** Count the nodes. `build(lo, hi)` builds the left subtree from `lo..mid-1` first, which advances a shared list
pointer exactly to the middle value; create the root from it, advance, then build the right subtree. No random access is needed.

* Time: **O(n)** — each list node becomes one tree node.
* Space: **O(log n)** — the recursion depth of a balanced tree.
''',
tc="n", sc="log",
java=r'''
public class SortedListToBST {

    private ListNode cur;

    public TreeNode sortedListToBST(ListNode head) {
        int n = 0;
        for (ListNode p = head; p != null; p = p.next) n++;
        cur = head;
        return build(0, n - 1);
    }

    private TreeNode build(int lo, int hi) {
        if (lo > hi) return null;
        int mid = (lo + hi) >>> 1;
        TreeNode left = build(lo, mid - 1);
        TreeNode root = new TreeNode(cur.val);
        cur = cur.next;
        root.left = left;
        root.right = build(mid + 1, hi);
        return root;
    }
}
''',
test=r'''
class SortedListToBSTTest {

    private final SortedListToBST solution = new SortedListToBST();

    private static void inorder(TreeNode n, List<Integer> out) {
        if (n == null) return;
        inorder(n.left, out);
        out.add(n.val);
        inorder(n.right, out);
    }

    private static int height(TreeNode n) {
        return n == null ? 0 : 1 + Math.max(height(n.left), height(n.right));
    }

    @Test
    void balancedAndSorted() {
        TreeNode root = solution.sortedListToBST(ListNode.of(-10, -3, 0, 5, 9));
        List<Integer> values = new ArrayList<>();
        inorder(root, values);
        assertEquals(List.of(-10, -3, 0, 5, 9), values);
        assertEquals(3, height(root));
        assertNull(solution.sortedListToBST(null));
    }
}
''',
trace=r'''
function run(vals) {
  let ptr = 0, root = null;
  A.step('Build the tree in in-order: the list is consumed left to right, exactly when each value is needed.', A.list('list', vals, { ptr: [[0, 'cur']] }));
  (function build(lo, hi, attach) {
    if (lo > hi) return;
    const mid = (lo + hi) >> 1, node = A.node(null);
    if (!root) root = node; attach(node);
    build(lo, mid - 1, c => (node.left = c));
    node.val = vals[ptr++];
    A.step(`The left part ${lo}..${mid - 1} is done, so the list pointer is at ${node.val}: it becomes the root of ${lo}..${hi}.`, A.list('list', vals, { ptr: ptr < vals.length ? [[ptr, 'cur']] : [], hl: Object.fromEntries([...Array(ptr)].map((_, t) => [t, 'ok'])) }), A.tree('tree', root, { hl: { [node.id]: 'cur' } }));
    build(mid + 1, hi, c => (node.right = c));
  })(0, vals.length - 1, () => {});
}
A.scenario('Five values', '-10 → -3 → 0 → 5 → 9', () => run([-10, -3, 0, 5, 9]));
'''),

P(num=116, slug="populating-next-right-pointers-in-each-node", title="Populating Next Right Pointers in Each Node", diff="Medium", topic="Binary Tree BFS", cls="PopulatingNextRightPerfect",
idea="In a perfect tree, link left → right child, and right child → the next node's left child, level by level.",
vname="Use the level above",
spec=r'''
In a **perfect** binary tree (all leaves on the same level, every parent has two children), set each `next` pointer to the node on its right,
or `null` at the end of a level. Use O(1) extra space.

**Example**
```
[1,2,3,4,5,6,7] → levels linked: 1 → null; 2 → 3 → null; 4 → 5 → 6 → 7 → null
```

**Constraints**
* `0 <= n <= 2^12 - 1`
''',
approach=r'''
**Leftmost walk.** For each level starting at `leftmost`, walk it via `next`: set `node.left.next = node.right` and, if `node.next` exists,
`node.right.next = node.next.left`. Move to `leftmost.left`.

* Time: **O(n)** — each node once.
* Space: **O(1)** — pointers only.
''',
java=r'''
public class PopulatingNextRightPerfect {

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
        for (Node leftmost = root; leftmost != null && leftmost.left != null; leftmost = leftmost.left) {
            for (Node n = leftmost; n != null; n = n.next) {
                n.left.next = n.right;
                if (n.next != null) n.right.next = n.next.left;
            }
        }
        return root;
    }
}
''',
test=r'''
class PopulatingNextRightPerfectTest {

    private final PopulatingNextRightPerfect solution = new PopulatingNextRightPerfect();

    @Test
    void perfectTree() {
        PopulatingNextRightPerfect.Node[] n = new PopulatingNextRightPerfect.Node[8];
        for (int i = 7; i >= 1; i--) n[i] = new PopulatingNextRightPerfect.Node(i, 2 * i < 8 ? n[2 * i] : null, 2 * i + 1 < 8 ? n[2 * i + 1] : null);
        solution.connect(n[1]);
        assertNull(n[1].next);
        assertSame(n[3], n[2].next);
        assertSame(n[5], n[4].next);
        assertSame(n[6], n[5].next);
        assertSame(n[7], n[6].next);
        assertNull(n[7].next);
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr);
  A.step('Use the next pointers of each level to wire up the level below it.', A.tree('tree', root, { next: true }));
  for (let lm = root; lm && lm.left; lm = lm.left) {
    for (let n = lm; n; n = n.next) { n.left.next = n.right; if (n.next) n.right.next = n.next.left; A.step(`At ${n.val}: link ${n.left.val} → ${n.right.val}${n.next ? ` and ${n.right.val} → ${n.next.left.val} (the next node's left child)` : ''}.`, A.tree('tree', root, { next: true, hl: { [n.id]: 'cur', [n.left.id]: 'ok', [n.right.id]: 'ok' } })); }
  }
  A.step('Every level is linked.', A.tree('tree', root, { next: true }));
}
A.scenario('Perfect tree', '[1,2,3,4,5,6,7]', () => run([1, 2, 3, 4, 5, 6, 7]));
'''),

P(num=119, slug="pascals-triangle-ii", title="Pascal's Triangle II", diff="Easy", topic="1D DP", cls="PascalsTriangleII",
idea="Update one row in place from right to left: row[j] += row[j − 1].",
vname="One row, updated right to left",
spec=r'''
Return row `rowIndex` (0-based) of Pascal's triangle.

**Example**
```
3 → [1,3,3,1],   0 → [1],   1 → [1,1]
```

**Constraints**
* `0 <= rowIndex <= 33`

**Follow-up:** O(rowIndex) extra space.
''',
approach=r'''
**In-place update.** Start with `[1]`. For each new row, append 1 and update `j` from right to left with `row[j] += row[j-1]`, so each
update still reads the previous row's values.

* Time: **O(k²)** — k rows of up to k updates.
* Space: **O(k)** — the single row.
''',
tc="n2", sc="n",
java=r'''
public class PascalsTriangleII {

    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>(List.of(1));
        for (int i = 1; i <= rowIndex; i++) {
            row.add(1);
            for (int j = i - 1; j >= 1; j--) row.set(j, row.get(j) + row.get(j - 1));
        }
        return row;
    }
}
''',
test=r'''
class PascalsTriangleIITest {

    private final PascalsTriangleII solution = new PascalsTriangleII();

    @Test
    void examples() {
        assertEquals(List.of(1, 3, 3, 1), solution.getRow(3));
        assertEquals(List.of(1), solution.getRow(0));
        assertEquals(List.of(1, 1), solution.getRow(1));
        assertEquals(1166803110, solution.getRow(33).get(16));
    }
}
''',
trace=r'''
function run(k) {
  const row = [1];
  A.step('Start with row 0: [1].', A.arr('row', row));
  for (let i = 1; i <= k; i++) { row.push(1); for (let j = i - 1; j >= 1; j--) row[j] += row[j - 1]; A.step(`Row ${i}: append 1, then from right to left add each value's left neighbour.`, A.arr('row', row, { hl: Object.fromEntries(row.map((_, j) => [j, j === 0 || j === i ? 'dim' : 'ok'])) })); }
}
A.scenario('Row 5', 'rowIndex = 5', () => run(5));
'''),

P(num=132, slug="palindrome-partitioning-ii", title="Palindrome Partitioning II", diff="Hard", topic="Multidimensional DP", cls="PalindromePartitioningII",
idea="Expand around every centre; each palindrome s[l..r] offers cuts[r + 1] = cuts[l] + 1.",
vname="Centre expansion + cut DP",
spec=r'''
Return the minimum number of cuts needed to partition `s` so that every piece is a palindrome.

**Example**
```
"aab" → 1 ("aa" | "b"),   "a" → 0,   "ab" → 1
```

**Constraints**
* `1 <= s.length <= 2000`
''',
approach=r'''
**DP on prefix lengths.** `cuts[i]` = minimum pieces for `s[0..i)` minus 1 (`cuts[0] = -1`). For each centre, expand outward; every palindrome
`s[l..r]` gives `cuts[r+1] = min(cuts[r+1], cuts[l] + 1)`.

* Time: **O(n²)** — every palindrome is enumerated once from its centre.
* Space: **O(n)** — the cuts array.
''',
tc="n2", sc="n",
java=r'''
public class PalindromePartitioningII {

    public int minCut(String s) {
        int n = s.length();
        int[] cuts = new int[n + 1];
        for (int i = 0; i <= n; i++) cuts[i] = i - 1;
        for (int c = 0; c < n; c++) {
            for (int l = c, r = c; l >= 0 && r < n && s.charAt(l) == s.charAt(r); l--, r++) cuts[r + 1] = Math.min(cuts[r + 1], cuts[l] + 1);
            for (int l = c, r = c + 1; l >= 0 && r < n && s.charAt(l) == s.charAt(r); l--, r++) cuts[r + 1] = Math.min(cuts[r + 1], cuts[l] + 1);
        }
        return cuts[n];
    }
}
''',
test=r'''
class PalindromePartitioningIITest {

    private final PalindromePartitioningII solution = new PalindromePartitioningII();

    @ParameterizedTest
    @CsvSource({"aab,1", "a,0", "ab,1", "abccba,0", "abacdc,1"})
    void cuts(String s, int expected) {
        assertEquals(expected, solution.minCut(s));
    }
}
''',
trace=r'''
function run(s) {
  const n = s.length, cuts = [...Array(n + 1)].map((_, i) => i - 1);
  A.step('cuts[i] is the fewest cuts for the first i letters. With no palindromes longer than one letter, it would be i − 1.', A.chars('s', s), A.arr('cuts', cuts));
  for (let c = 0; c < n; c++) for (const odd of [true, false]) {
    for (let l = c, r = odd ? c : c + 1; l >= 0 && r < n && s[l] === s[r]; l--, r++) {
      if (cuts[l] + 1 < cuts[r + 1]) { cuts[r + 1] = cuts[l] + 1; A.step(`"${s.slice(l, r + 1)}" is a palindrome, so the first ${r + 1} letters need at most cuts[${l}] + 1 = ${cuts[r + 1]} cuts.`, A.chars('s', s, { range: [l, r] }), A.arr('cuts', cuts, { hl: { [r + 1]: 'ok', [l]: 'sel' } })); }
    }
  }
  A.step(`Minimum cuts: ${cuts[n]}.`, A.text('Result', cuts[n], 'ok'));
}
A.scenario('abacdc', 's = "abacdc"', () => run('abacdc'));
'''),

P(num=140, slug="word-break-ii", title="Word Break II", diff="Hard", topic="Backtracking", cls="WordBreakII",
idea="Backtrack over dictionary-word prefixes, memoizing all sentences for each suffix.",
vname="Memoized backtracking",
spec=r'''
Return every way to split `s` into a space-separated sentence of dictionary words (words may be reused), in any order.

**Example**
```
s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"] → ["cats and dog","cat sand dog"]
s = "catsandog", same dict → []
```

**Constraints**
* `1 <= s.length <= 20`
''',
approach=r'''
**Memo on the start index.** `sentences(i)` lists all sentences for `s[i..]`: for each dictionary word that starts at `i`, prepend it to every
sentence of the remainder. Cache results per index in a `MyHashMap`.

* Time: **O(2ⁿ)** — the number of sentences itself can be exponential.
* Space: **O(2ⁿ)** — the memoized sentences.
''',
tc="exp", sc="exp",
java=r'''
public class WordBreakII {

    private final MyHashMap<Integer, List<String>> memo = new MyHashMap<>();
    private MyHashSet<String> dict;

    public List<String> wordBreak(String s, List<String> wordDict) {
        dict = new MyHashSet<>();
        for (String w : wordDict) dict.add(w);
        return sentences(s, 0);
    }

    private List<String> sentences(String s, int i) {
        List<String> cached = memo.get(i);
        if (cached != null) return cached;
        List<String> out = new ArrayList<>();
        if (i == s.length()) out.add("");
        for (int j = i + 1; j <= s.length(); j++) {
            String word = s.substring(i, j);
            if (!dict.contains(word)) continue;
            for (String rest : sentences(s, j)) out.add(rest.isEmpty() ? word : word + " " + rest);
        }
        memo.put(i, out);
        return out;
    }
}
''',
test=r'''
class WordBreakIITest {

    @Test
    void examples() {
        assertEquals(Set.of("cats and dog", "cat sand dog"), new HashSet<>(new WordBreakII().wordBreak("catsanddog", List.of("cat", "cats", "and", "sand", "dog"))));
        assertEquals(Set.of("pine apple pen apple", "pineapple pen apple", "pine applepen apple"),
                new HashSet<>(new WordBreakII().wordBreak("pineapplepenapple", List.of("apple", "pen", "applepen", "pine", "pineapple"))));
        assertEquals(List.of(), new WordBreakII().wordBreak("catsandog", List.of("cats", "dog", "sand", "and", "cat")));
    }
}
''',
trace=r'''
function run(s, dict) {
  const words = new Set(dict), memo = new Map();
  const sent = i => {
    if (memo.has(i)) return memo.get(i);
    const out = i === s.length ? [''] : [];
    for (let j = i + 1; j <= s.length; j++) { const w = s.slice(i, j); if (!words.has(w)) continue; for (const rest of sent(j)) out.push(rest ? w + ' ' + rest : w); }
    memo.set(i, out);
    A.step(`Suffix "${s.slice(i)}" can be written as: ${out.length ? out.map(x => `"${x}"`).join(', ') : 'nothing'}.`, A.chars('s', s, { range: [i, s.length - 1] }), A.hashTable('memo (start → sentences)', new Map([...memo].map(([k, v]) => [k, v.length]))));
    return out;
  };
  const r = sent(0);
  A.step(`${r.length} sentence${r.length === 1 ? '' : 's'}.`, A.arr('sentences', r));
}
A.scenario('catsanddog', 'dict = [cat, cats, and, sand, dog]', () => run('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']));
'''),

P(num=147, slug="insertion-sort-list", title="Insertion Sort List", diff="Medium", topic="Linked List", cls="InsertionSortList",
idea="Take nodes one by one and splice each into its place in a growing sorted list.",
vname="Splice into a sorted list", helpers=["ListNode"],
spec=r'''
Sort a linked list using insertion sort and return its head.

**Example**
```
4 → 2 → 1 → 3 becomes 1 → 2 → 3 → 4,   -1 → 5 → 3 → 4 → 0 becomes -1 → 0 → 3 → 4 → 5
```

**Constraints**
* `1 <= n <= 5000`
''',
approach=r'''
**Dummy-headed sorted list.** For each node, walk from the dummy to find the last node smaller than it and splice it in. (A small speed-up:
restart the walk only when the new value is smaller than the previous insertion point.)

* Time: **O(n²)** — each insertion may walk the whole sorted part.
* Space: **O(1)** — nodes are re-linked.
''',
tc="n2",
java=r'''
public class InsertionSortList {

    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode(0), prev = dummy;
        for (ListNode cur = head; cur != null; ) {
            ListNode next = cur.next;
            if (prev.val >= cur.val || prev == dummy) prev = dummy;
            while (prev.next != null && prev.next.val < cur.val) prev = prev.next;
            cur.next = prev.next;
            prev.next = cur;
            cur = next;
        }
        return dummy.next;
    }
}
''',
test=r'''
class InsertionSortListTest {

    private final InsertionSortList solution = new InsertionSortList();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 2, 3, 4}, ListNode.toArray(solution.insertionSortList(ListNode.of(4, 2, 1, 3))));
        assertArrayEquals(new int[]{-1, 0, 3, 4, 5}, ListNode.toArray(solution.insertionSortList(ListNode.of(-1, 5, 3, 4, 0))));
    }
}
''',
trace=r'''
function run(vals) {
  const sorted = [];
  vals.forEach((v, i) => { let k = 0; while (k < sorted.length && sorted[k] < v) k++; sorted.splice(k, 0, v); A.step(`Take ${v} and splice it in at position ${k} of the sorted list.`, A.list('unsorted', vals.slice(i + 1)), A.list('sorted', sorted, { hl: { [k]: 'ok' } })); });
}
A.scenario('Five values', '-1 → 5 → 3 → 4 → 0', () => run([-1, 5, 3, 4, 0]));
'''),

P(num=154, slug="find-minimum-in-rotated-sorted-array-ii", title="Find Minimum in Rotated Sorted Array II", diff="Hard", topic="Binary Search", cls="FindMinimumRotatedII",
idea="Compare mid with hi: bigger → minimum is right, smaller → left half, equal → just drop hi.",
vname="Binary search with duplicate shrinking",
spec=r'''
A sorted array that may contain **duplicates** was rotated. Return its minimum value.

**Example**
```
[1,3,5] → 1,   [2,2,2,0,1] → 0,   [3,1,3] → 1
```

**Constraints**
* `1 <= n <= 5000`
''',
approach=r'''
**Three cases.** `nums[mid] > nums[hi]`: the minimum is right of mid. `<`: it is mid or left. `==`: we cannot tell, but `nums[hi]` has a copy
at `mid`, so dropping `hi` is safe.

* Time: **O(n)** — worst case with many duplicates; O(log n) for distinct values.
* Space: **O(1)** — indices.
''',
tc="n",
java=r'''
public class FindMinimumRotatedII {

    public int findMin(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] > nums[hi]) lo = mid + 1;
            else if (nums[mid] < nums[hi]) hi = mid;
            else hi--;
        }
        return nums[lo];
    }
}
''',
test=r'''
class FindMinimumRotatedIITest {

    private final FindMinimumRotatedII solution = new FindMinimumRotatedII();

    @Test
    void examples() {
        assertEquals(1, solution.findMin(new int[]{1, 3, 5}));
        assertEquals(0, solution.findMin(new int[]{2, 2, 2, 0, 1}));
        assertEquals(1, solution.findMin(new int[]{3, 1, 3}));
        assertEquals(1, solution.findMin(new int[]{1, 1, 1, 1}));
    }
}
''',
trace=r'''
function run(a) {
  let lo = 0, hi = a.length - 1;
  while (lo < hi) { const mid = (lo + hi) >> 1; const c = a[mid] > a[hi] ? 'right' : a[mid] < a[hi] ? 'left' : 'eq'; A.step(c === 'right' ? `${a[mid]} > ${a[hi]}: the minimum is right of mid.` : c === 'left' ? `${a[mid]} < ${a[hi]}: the minimum is at mid or to its left.` : `${a[mid]} = ${a[hi]}: unclear, but hi has a copy at mid, so drop hi.`, A.arr('nums', a, { range: [lo, hi], hl: { [mid]: 'cur', [hi]: c === 'eq' ? 'bad' : 'alt' } })); if (c === 'right') lo = mid + 1; else if (c === 'left') hi = mid; else hi--; }
  A.step(`Minimum: ${a[lo]}.`, A.arr('nums', a, { hl: { [lo]: 'ok' } }), A.text('Result', a[lo], 'ok'));
}
A.scenario('Duplicates', 'nums = [2,2,2,0,1]', () => run([2, 2, 2, 0, 1]));
'''),

P(num=165, slug="compare-version-numbers", title="Compare Version Numbers", diff="Medium", topic="Two Pointers", cls="CompareVersionNumbers",
idea="Compare revision by revision as integers, treating missing revisions as 0.",
vname="Revision-wise parsing",
spec=r'''
Compare two version strings made of revisions separated by dots. Revisions compare as integers (leading zeros ignored); a missing revision
counts as 0. Return `-1`, `0` or `1`.

**Example**
```
"1.2", "1.10" → -1,   "1.01", "1.001" → 0,   "1.0", "1.0.0.0" → 0
```

**Constraints**
* `1 <= length <= 500`; revisions fit in 32 bits.
''',
approach=r'''
**Two pointers.** Parse the next revision of each string digit by digit (0 if exhausted) and compare; continue while either string has
characters left.

* Time: **O(m + n)** — each character once.
* Space: **O(1)** — no splitting.
''',
java=r'''
public class CompareVersionNumbers {

    public int compareVersion(String version1, String version2) {
        int i = 0, j = 0;
        while (i < version1.length() || j < version2.length()) {
            int a = 0, b = 0;
            while (i < version1.length() && version1.charAt(i) != '.') a = a * 10 + (version1.charAt(i++) - '0');
            while (j < version2.length() && version2.charAt(j) != '.') b = b * 10 + (version2.charAt(j++) - '0');
            if (a != b) return a < b ? -1 : 1;
            i++;
            j++;
        }
        return 0;
    }
}
''',
test=r'''
class CompareVersionNumbersTest {

    private final CompareVersionNumbers solution = new CompareVersionNumbers();

    @ParameterizedTest
    @CsvSource({"1.2,1.10,-1", "1.01,1.001,0", "1.0,1.0.0.0,0", "0.1,1.1,-1", "1.0.1,1,1"})
    void compares(String a, String b, int expected) {
        assertEquals(expected, solution.compareVersion(a, b));
    }
}
''',
trace=r'''
function run(a, b) {
  const x = a.split('.'), y = b.split('.'), n = Math.max(x.length, y.length);
  for (let k = 0; k < n; k++) {
    const p = +(x[k] || 0), q = +(y[k] || 0);
    A.step(`Revision ${k}: ${x[k] ?? '(missing)'} → ${p} vs ${y[k] ?? '(missing)'} → ${q}.`, A.arr('version1', x, { hl: { [k]: p === q ? 'ok' : 'cur' } }), A.arr('version2', y, { hl: { [k]: p === q ? 'ok' : 'cur' } }));
    if (p !== q) { A.step(`${p} ${p < q ? '<' : '>'} ${q}.`, A.text('Result', p < q ? -1 : 1, 'ok')); return; }
  }
  A.step('Every revision is equal.', A.text('Result', 0, 'ok'));
}
A.scenario('Numeric, not text', 'version1 = "1.2", version2 = "1.10"', () => run('1.2', '1.10'));
'''),
]
