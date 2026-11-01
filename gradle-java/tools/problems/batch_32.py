PROBLEMS = [
P(num=594, slug="longest-harmonious-subsequence", title="Longest Harmonious Subsequence", diff="Easy", topic="Arrays & Hashing", cls="LongestHarmoniousSubsequence",
idea="A harmonious subsequence uses only two values x and x + 1; count values and try every x.",
vname="Count pairs of adjacent values",
spec=r'''
A **harmonious** array has a difference of exactly 1 between its maximum and minimum. Return the length of the longest harmonious
subsequence of `nums`.

**Example**
```
[1,3,2,2,5,2,3,7] → 5 ([3,2,2,2,3]),   [1,2,3,4] → 2,   [1,1,1,1] → 0
```

**Constraints**
* `1 <= nums.length <= 2 * 10^4`
''',
approach=r'''
**Counting.** Count each value in a `MyHashMap`. For each value `x` that also has `x + 1`, the subsequence of all `x` and `x + 1` has length
`count[x] + count[x+1]`.

* Time: **O(n)** — counting and one pass over the keys.
* Space: **O(n)** — the map.
''',
java=r'''
public class LongestHarmoniousSubsequence {

    public int findLHS(int[] nums) {
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int x : nums) count.merge(x, 1, Integer::sum);
        int best = 0;
        for (MyHashMap.Entry<Integer, Integer> e : count.entries()) {
            Integer up = count.get(e.getKey() + 1);
            if (up != null) best = Math.max(best, e.getValue() + up);
        }
        return best;
    }
}
''',
test=r'''
class LongestHarmoniousSubsequenceTest {

    private final LongestHarmoniousSubsequence solution = new LongestHarmoniousSubsequence();

    @Test
    void examples() {
        assertEquals(5, solution.findLHS(new int[]{1, 3, 2, 2, 5, 2, 3, 7}));
        assertEquals(2, solution.findLHS(new int[]{1, 2, 3, 4}));
        assertEquals(0, solution.findLHS(new int[]{1, 1, 1, 1}));
    }
}
''',
trace=r'''
function run(a) {
  const cnt = new Map(); a.forEach(x => cnt.set(x, (cnt.get(x) || 0) + 1)); let best = 0;
  A.step('Count every value.', A.arr('nums', a), A.hashTable('counts', cnt));
  for (const [x, c] of [...cnt].sort((p, q) => p[0] - q[0])) { if (cnt.has(x + 1)) { const len = c + cnt.get(x + 1); best = Math.max(best, len); A.step(`Values ${x} and ${x + 1}: ${c} + ${cnt.get(x + 1)} = ${len}. Best ${best}.`, A.arr('nums', a, { hl: Object.fromEntries(a.map((v, i) => [i, v === x || v === x + 1 ? 'ok' : 'dim'])) }), A.vars({ best })); } }
  A.step(`Longest harmonious subsequence: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', 'nums = [1,3,2,2,5,2,3,7]', () => run([1, 3, 2, 2, 5, 2, 3, 7]));
'''),

P(num=617, slug="merge-two-binary-trees", title="Merge Two Binary Trees", diff="Easy", topic="Binary Tree General", cls="MergeTwoBinaryTrees",
idea="Overlay the trees: where both have a node, add the values; otherwise take whichever node exists.",
vname="Recursive overlay", helpers=["TreeNode"],
spec=r'''
Merge two binary trees: overlapping nodes sum their values; a node present in only one tree is used as is. Return the merged tree.

**Example**
```
root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7] → [3,4,5,5,4,null,7]
```

**Constraints**
* `0 <= nodes <= 2000`
''',
approach=r'''
**Recursion.** If either side is null return the other; otherwise add the values into `t1` and merge the children pairwise.

* Time: **O(min(n, m))** — only overlapping nodes are visited.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class MergeTwoBinaryTrees {

    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null) return root2;
        if (root2 == null) return root1;
        root1.val += root2.val;
        root1.left = mergeTrees(root1.left, root2.left);
        root1.right = mergeTrees(root1.right, root2.right);
        return root1;
    }
}
''',
test=r'''
class MergeTwoBinaryTreesTest {

    private final MergeTwoBinaryTrees solution = new MergeTwoBinaryTrees();

    @Test
    void examples() {
        assertEquals(Arrays.asList(3, 4, 5, 5, 4, null, 7), TreeNode.toList(solution.mergeTrees(TreeNode.of(1, 3, 2, 5), TreeNode.of(2, 1, 3, null, 4, null, 7))));
        assertEquals(List.of(2, 2), TreeNode.toList(solution.mergeTrees(TreeNode.of(1), TreeNode.of(1, 2))));
    }
}
''',
trace=r'''
function run(x, y) {
  const t1 = A.mkTree(x), t2 = A.mkTree(y), hl = {};
  A.step('Overlay the second tree on the first.', A.tree('tree 1', t1), A.tree('tree 2', t2));
  const merge = (a, b) => { if (!a) return b; if (!b) return a; a.val += b.val; hl[a.id] = 'ok'; A.step(`Both trees have a node here: ${a.val - b.val} + ${b.val} = ${a.val}.`, A.tree('merged (tree 1)', t1, { hl: { ...hl, [a.id]: 'cur' } })); a.left = merge(a.left, b.left); a.right = merge(a.right, b.right); return a; };
  merge(t1, t2);
  A.step('Where only one tree had a node, that node is used as is.', A.tree('merged', t1, { hl }));
}
A.scenario('Classic', 'root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]', () => run([1, 3, 2, 5], [2, 1, 3, null, 4, null, 7]));
'''),

P(num=628, slug="maximum-product-of-three-numbers", title="Maximum Product of Three Numbers", diff="Easy", topic="Math", cls="MaximumProductOfThree",
idea="The best product is either the three largest values or the two smallest (most negative) times the largest.",
vname="Track top three and bottom two",
spec=r'''
Return the maximum product of three numbers in `nums`.

**Example**
```
[1,2,3] → 6,   [1,2,3,4] → 24,   [-1,-2,-3] → -6,   [-10,-10,1,3,2] → 300
```

**Constraints**
* `3 <= nums.length <= 10^4`; `-1000 <= nums[i] <= 1000`
''',
approach=r'''
**One pass.** Keep the three largest and two smallest values. Answer `max(max1·max2·max3, min1·min2·max1)`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — five numbers.
''',
java=r'''
public class MaximumProductOfThree {

    public int maximumProduct(int[] nums) {
        int max1 = Integer.MIN_VALUE, max2 = Integer.MIN_VALUE, max3 = Integer.MIN_VALUE;
        int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
        for (int x : nums) {
            if (x > max1) { max3 = max2; max2 = max1; max1 = x; }
            else if (x > max2) { max3 = max2; max2 = x; }
            else if (x > max3) max3 = x;
            if (x < min1) { min2 = min1; min1 = x; }
            else if (x < min2) min2 = x;
        }
        return Math.max(max1 * max2 * max3, min1 * min2 * max1);
    }
}
''',
test=r'''
class MaximumProductOfThreeTest {

    private final MaximumProductOfThree solution = new MaximumProductOfThree();

    @Test
    void examples() {
        assertEquals(6, solution.maximumProduct(new int[]{1, 2, 3}));
        assertEquals(24, solution.maximumProduct(new int[]{1, 2, 3, 4}));
        assertEquals(-6, solution.maximumProduct(new int[]{-1, -2, -3}));
        assertEquals(300, solution.maximumProduct(new int[]{-10, -10, 1, 3, 2}));
    }
}
''',
trace=r'''
function run(a) {
  const s = a.slice().sort((x, y) => x - y), n = s.length;
  A.step('Only five values matter: the three largest and the two smallest.', A.arr('sorted', s, { hl: { 0: 'alt', 1: 'alt', [n - 1]: 'sel', [n - 2]: 'sel', [n - 3]: 'sel' } }));
  const p1 = s[n - 1] * s[n - 2] * s[n - 3], p2 = s[0] * s[1] * s[n - 1];
  A.step(`Three largest: ${s[n - 3]} × ${s[n - 2]} × ${s[n - 1]} = ${p1}. Two smallest × largest: ${s[0]} × ${s[1]} × ${s[n - 1]} = ${p2}.`, A.vars({ threeLargest: p1, twoSmallestTimesLargest: p2 }));
  A.step(`Maximum product: ${Math.max(p1, p2)}.`, A.text('Result', Math.max(p1, p2), 'ok'));
}
A.scenario('Negatives help', 'nums = [-10,-10,1,3,2]', () => run([-10, -10, 1, 3, 2]));
'''),

P(num=645, slug="set-mismatch", title="Set Mismatch", diff="Easy", topic="Arrays & Hashing", cls="SetMismatch",
idea="Count occurrences of 1..n: the value seen twice is the duplicate, the value seen zero times is missing.",
vname="Counting array",
spec=r'''
A set held `1..n`, but one number was duplicated, replacing another. Given the resulting array `nums`, return `[duplicate, missing]`.

**Example**
```
[1,2,2,4] → [2,3],   [1,1] → [1,2]
```

**Constraints**
* `2 <= n <= 10^4`
''',
approach=r'''
**Counts.** `count[v]` for each value; the one with count 2 is the duplicate, the one with count 0 is missing.

* Time: **O(n)** — two passes.
* Space: **O(n)** — the count array.
''',
sc="n",
java=r'''
public class SetMismatch {

    public int[] findErrorNums(int[] nums) {
        int n = nums.length, dup = -1, missing = -1;
        int[] count = new int[n + 1];
        for (int x : nums) count[x]++;
        for (int v = 1; v <= n; v++) {
            if (count[v] == 2) dup = v;
            if (count[v] == 0) missing = v;
        }
        return new int[]{dup, missing};
    }
}
''',
test=r'''
class SetMismatchTest {

    private final SetMismatch solution = new SetMismatch();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 3}, solution.findErrorNums(new int[]{1, 2, 2, 4}));
        assertArrayEquals(new int[]{1, 2}, solution.findErrorNums(new int[]{1, 1}));
        assertArrayEquals(new int[]{3, 1}, solution.findErrorNums(new int[]{3, 2, 3}));
    }
}
''',
trace=r'''
function run(a) {
  const n = a.length, cnt = new Array(n + 1).fill(0);
  a.forEach(x => cnt[x]++);
  A.step('Count how often each value 1..n appears.', A.arr('nums', a), A.arr('count (index = value)', cnt, { hl: { 0: 'dim' } }));
  const dup = cnt.indexOf(2), miss = cnt.findIndex((c, v) => v > 0 && c === 0);
  A.step(`${dup} appears twice; ${miss} never appears.`, A.arr('count (index = value)', cnt, { hl: { 0: 'dim', [dup]: 'bad', [miss]: 'alt' } }), A.text('Result', `[${dup}, ${miss}]`, 'ok'));
}
A.scenario('Classic', 'nums = [1,2,2,4]', () => run([1, 2, 2, 4]));
'''),

P(num=653, slug="two-sum-iv-input-is-a-bst", title="Two Sum IV - Input is a BST", diff="Easy", topic="Binary Search Tree", cls="TwoSumIV",
idea="Traverse the tree, checking whether k − value has already been seen.",
vname="DFS with a seen set", helpers=["TreeNode"],
spec=r'''
Return `true` if two different nodes of the BST have values summing to `k`.

**Example**
```
root = [5,3,6,2,4,null,7], k = 9 → true,   k = 28 → false
```

**Constraints**
* `1 <= n <= 10^4`
''',
approach=r'''
**Hash set.** Visit every node; if `k - val` is in the `MyHashSet`, return true; otherwise add `val`.

* Time: **O(n)** — each node once.
* Space: **O(n)** — the set.
''',
tc="n", sc="n",
java=r'''
public class TwoSumIV {

    public boolean findTarget(TreeNode root, int k) {
        MyHashSet<Integer> seen = new MyHashSet<>();
        Deque<TreeNode> stack = new ArrayDeque<>(List.of(root));
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            if (seen.contains(k - n.val)) return true;
            seen.add(n.val);
            if (n.left != null) stack.push(n.left);
            if (n.right != null) stack.push(n.right);
        }
        return false;
    }
}
''',
test=r'''
class TwoSumIVTest {

    private final TwoSumIV solution = new TwoSumIV();

    @Test
    void examples() {
        assertTrue(solution.findTarget(TreeNode.of(5, 3, 6, 2, 4, null, 7), 9));
        assertFalse(solution.findTarget(TreeNode.of(5, 3, 6, 2, 4, null, 7), 28));
        assertFalse(solution.findTarget(TreeNode.of(1), 2));
    }
}
''',
trace=r'''
function run(arr, k) {
  const root = A.mkTree(arr), seen = new Set(), st = [root], hl = {};
  while (st.length) {
    const n = st.pop();
    if (seen.has(k - n.val)) { hl[n.id] = 'ok'; A.step(`${n.val} needs ${k - n.val}, which was already seen. Found a pair.`, A.tree('BST', root, { hl }), A.hashTable('seen', seen, { hl: k - n.val }), A.text('Result', 'true', 'ok')); return; }
    seen.add(n.val); hl[n.id] = 'sel';
    A.step(`${n.val} needs ${k - n.val}: not seen yet. Remember ${n.val}.`, A.tree('BST', root, { hl: { ...hl, [n.id]: 'cur' } }), A.hashTable('seen', seen, { hl: n.val }));
    if (n.left) st.push(n.left); if (n.right) st.push(n.right);
  }
  A.step('No pair adds up to k.', A.text('Result', 'false', 'bad'));
}
A.scenario('k = 9', 'root = [5,3,6,2,4,null,7]', () => run([5, 3, 6, 2, 4, null, 7], 9));
'''),

P(num=654, slug="maximum-binary-tree", title="Maximum Binary Tree", diff="Medium", topic="Stack", cls="MaximumBinaryTree",
idea="A decreasing stack builds the tree in one pass: each new value adopts the smaller values it pops as its left subtree.",
vname="Monotonic stack", helpers=["TreeNode"],
spec=r'''
Build the **maximum binary tree** of distinct `nums`: the root is the maximum; its left subtree is built from the part before it and its right
subtree from the part after it, recursively.

**Example**
```
[3,2,1,6,0,5] → [6,3,5,null,2,0,null,null,1]
```

**Constraints**
* `1 <= nums.length <= 1000`; values are distinct.
''',
approach=r'''
**Decreasing stack of nodes.** For each value create a node; pop every smaller node, the last one popped becoming its left child; if the
stack is not empty, the new node becomes the right child of the top. The bottom of the stack is the root.

* Time: **O(n)** — each node is pushed and popped once.
* Space: **O(n)** — the stack.
''',
tc="n", sc="n",
java=r'''
public class MaximumBinaryTree {

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        for (int x : nums) {
            TreeNode node = new TreeNode(x);
            while (!stack.isEmpty() && stack.peek().val < x) node.left = stack.pop();
            if (!stack.isEmpty()) stack.peek().right = node;
            stack.push(node);
        }
        return stack.peekLast();
    }
}
''',
test=r'''
class MaximumBinaryTreeTest {

    private final MaximumBinaryTree solution = new MaximumBinaryTree();

    @Test
    void examples() {
        assertEquals(Arrays.asList(6, 3, 5, null, 2, 0, null, null, 1), TreeNode.toList(solution.constructMaximumBinaryTree(new int[]{3, 2, 1, 6, 0, 5})));
        assertEquals(Arrays.asList(3, null, 2, null, 1), TreeNode.toList(solution.constructMaximumBinaryTree(new int[]{3, 2, 1})));
    }
}
''',
trace=r'''
function run(nums) {
  const st = [];
  nums.forEach((x, i) => {
    const node = A.node(x); let popped = null;
    while (st.length && st[st.length - 1].val < x) popped = st.pop();
    if (popped) node.left = popped;
    if (st.length) st[st.length - 1].right = node;
    st.push(node);
    A.step(`${x}: ${popped ? `smaller nodes are popped; the last one (${popped.val}) becomes its left child. ` : ''}${st.length > 1 ? `It is the right child of ${st[st.length - 2].val}.` : 'It is the current root.'}`, A.arr('nums', nums, { hl: { [i]: 'cur' } }), A.tree('tree so far', st[0], { hl: { [node.id]: 'cur' } }), A.stack('stack', st.map(n => n.val)));
  });
  A.step('The bottom of the stack is the root.', A.tree('maximum binary tree', st[0]));
}
A.scenario('Classic', 'nums = [3,2,1,6,0,5]', () => run([3, 2, 1, 6, 0, 5]));
'''),

P(num=658, slug="find-k-closest-elements", title="Find K Closest Elements", diff="Medium", topic="Binary Search", cls="FindKClosestElements",
idea="Binary-search the left edge of the k-length window: compare the distances of x to arr[mid] and arr[mid + k].",
vname="Binary search on the window start",
spec=r'''
Given a sorted array, return the `k` elements closest to `x`, in ascending order. `a` is closer than `b` if `|a - x| < |b - x|`, or equal
distance and `a < b`.

**Example**
```
arr = [1,2,3,4,5], k = 4, x = 3  → [1,2,3,4]
arr = [1,1,2,3,4,5], k = 4, x = -1 → [1,1,2,3]
```

**Constraints**
* `1 <= k <= arr.length <= 10^4`
''',
approach=r'''
**Search the start.** The answer is a contiguous window `[lo, lo + k)`. For a candidate `mid`, if `x - arr[mid] > arr[mid + k] - x`, the
window should move right; otherwise left (ties keep the smaller values).

* Time: **O(log(n − k) + k)** — the search plus building the output.
* Space: **O(1)** — apart from the output.
''',
tc="log",
java=r'''
public class FindKClosestElements {

    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int lo = 0, hi = arr.length - k;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (x - arr[mid] > arr[mid + k] - x) lo = mid + 1; else hi = mid;
        }
        List<Integer> out = new ArrayList<>();
        for (int i = lo; i < lo + k; i++) out.add(arr[i]);
        return out;
    }
}
''',
test=r'''
class FindKClosestElementsTest {

    private final FindKClosestElements solution = new FindKClosestElements();

    @Test
    void examples() {
        assertEquals(List.of(1, 2, 3, 4), solution.findClosestElements(new int[]{1, 2, 3, 4, 5}, 4, 3));
        assertEquals(List.of(1, 1, 2, 3), solution.findClosestElements(new int[]{1, 1, 2, 3, 4, 5}, 4, -1));
        assertEquals(List.of(3, 4), solution.findClosestElements(new int[]{1, 3, 4, 8}, 2, 5));
    }
}
''',
trace=r'''
function run(a, k, x) {
  let lo = 0, hi = a.length - k;
  A.step(`The answer is a window of ${k} elements. Search for its left edge between 0 and ${hi}.`, A.arr('arr', a), A.vars({ x }));
  while (lo < hi) {
    const mid = (lo + hi) >> 1, right = x - a[mid] > a[mid + k] - x;
    A.step(`Window starting at ${mid}: compare ${a[mid]} (distance ${x - a[mid]}) with ${a[mid + k]} just outside (distance ${a[mid + k] - x}). ${right ? 'The outside value is closer: move right.' : 'Keep this start or move left.'}`, A.arr('arr', a, { range: [mid, mid + k - 1], hl: { [mid]: 'cur', [mid + k]: 'alt' } }));
    if (right) lo = mid + 1; else hi = mid;
  }
  A.step(`The closest window starts at ${lo}: [${a.slice(lo, lo + k)}].`, A.arr('arr', a, { range: [lo, lo + k - 1], hl: Object.fromEntries([...Array(k)].map((_, t) => [lo + t, 'ok'])) }), A.text('Result', JSON.stringify(a.slice(lo, lo + k)), 'ok'));
}
A.scenario('x = 6', 'arr = [1,2,3,4,5,7,9,11], k = 3', () => run([1, 2, 3, 4, 5, 7, 9, 11], 3, 6));
'''),

P(num=662, slug="maximum-width-of-binary-tree", title="Maximum Width of Binary Tree", diff="Medium", topic="Binary Tree BFS", cls="MaximumWidth",
idea="Number nodes like a heap (left = 2i, right = 2i + 1); a level's width is last index − first index + 1.",
vname="BFS with position indices", helpers=["TreeNode"],
spec=r'''
The width of a level is the number of positions between its leftmost and rightmost non-null nodes, counting the null positions in between
as they would appear in a complete tree. Return the maximum width over all levels (it fits in 32 bits).

**Example**
```
[1,3,2,5,3,null,9]               → 4
[1,3,2,5,null,null,9,6,null,7]   → 7
```

**Constraints**
* `1 <= n <= 3000`
''',
approach=r'''
**Positions.** BFS with each node's position: children of `p` are `2p` and `2p + 1`. To avoid huge numbers, renumber each level relative to its
first position before expanding. Width = last − first + 1.

* Time: **O(n)** — each node once.
* Space: **O(w)** — the widest level.
''',
tc="n", sc="n",
java=r'''
public class MaximumWidth {

    public int widthOfBinaryTree(TreeNode root) {
        Deque<Object[]> queue = new ArrayDeque<>();
        queue.add(new Object[]{root, 0L});
        long best = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            long first = (long) queue.peekFirst()[1], last = first;
            for (int i = 0; i < size; i++) {
                Object[] item = queue.poll();
                TreeNode n = (TreeNode) item[0];
                long pos = (long) item[1] - first;
                last = pos;
                if (n.left != null) queue.add(new Object[]{n.left, 2 * pos});
                if (n.right != null) queue.add(new Object[]{n.right, 2 * pos + 1});
            }
            best = Math.max(best, last + 1);
        }
        return (int) best;
    }
}
''',
test=r'''
class MaximumWidthTest {

    private final MaximumWidth solution = new MaximumWidth();

    @Test
    void examples() {
        assertEquals(4, solution.widthOfBinaryTree(TreeNode.of(1, 3, 2, 5, 3, null, 9)));
        assertEquals(7, solution.widthOfBinaryTree(TreeNode.of(1, 3, 2, 5, null, null, 9, 6, null, 7)));
        assertEquals(2, solution.widthOfBinaryTree(TreeNode.of(1, 3, 2, 5)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr); let q = [[root, 0]], best = 0;
  for (let lvl = 0; q.length; lvl++) {
    const first = q[0][1], last = q[q.length - 1][1], w = last - first + 1; best = Math.max(best, w);
    A.step(`Level ${lvl}: positions ${q.map(([, p]) => p).join(', ')}. Width = ${last} − ${first} + 1 = ${w}. Best ${best}.`, A.tree('tree', root, { hl: Object.fromEntries(q.map(([n]) => [n.id, 'cur'])) }), A.vars({ width: w, best }));
    q = q.flatMap(([n, p]) => [[n.left, 2 * (p - first)], [n.right, 2 * (p - first) + 1]].filter(([c]) => c));
  }
  A.step(`Maximum width: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Gaps count', '[1,3,2,5,null,null,9,6,null,7]', () => run([1, 3, 2, 5, null, null, 9, 6, null, 7]));
'''),

P(num=669, slug="trim-a-binary-search-tree", title="Trim a Binary Search Tree", diff="Medium", topic="Binary Search Tree", cls="TrimBST",
idea="A node below low can only keep its right subtree; above high, only its left subtree.",
vname="Recursive trimming", helpers=["TreeNode"],
spec=r'''
Remove every node whose value lies outside `[low, high]` from a BST, keeping the relative structure of the remaining nodes. Return the new root.

**Example**
```
root = [1,0,2], low = 1, high = 2           → [1,null,2]
root = [3,0,4,null,2,null,null,1], low = 1, high = 3 → [3,2,null,1]
```

**Constraints**
* `1 <= n <= 10^4`
''',
approach=r'''
**Recursion.** If `node.val < low`, its whole left subtree is too small: return `trim(node.right)`. If `node.val > high`, return
`trim(node.left)`. Otherwise trim both children and keep the node.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class TrimBST {

    public TreeNode trimBST(TreeNode root, int low, int high) {
        if (root == null) return null;
        if (root.val < low) return trimBST(root.right, low, high);
        if (root.val > high) return trimBST(root.left, low, high);
        root.left = trimBST(root.left, low, high);
        root.right = trimBST(root.right, low, high);
        return root;
    }
}
''',
test=r'''
class TrimBSTTest {

    private final TrimBST solution = new TrimBST();

    @Test
    void examples() {
        assertEquals(Arrays.asList(1, null, 2), TreeNode.toList(solution.trimBST(TreeNode.of(1, 0, 2), 1, 2)));
        assertEquals(Arrays.asList(3, 2, null, 1), TreeNode.toList(solution.trimBST(TreeNode.of(3, 0, 4, null, 2, null, null, 1), 1, 3)));
    }
}
''',
trace=r'''
function run(arr, lo, hi) {
  let root = A.mkTree(arr); const orig = A.mkTree(arr), hl = {};
  const mark = (n, c) => { if (!n) return; hl[n.id] = c; mark(n.left, c); mark(n.right, c); };
  const trim = n => {
    if (!n) return null;
    if (n.val < lo) { hl[n.id] = 'bad'; mark(n.left, 'bad'); A.step(`${n.val} < ${lo}: drop it and its left subtree; continue in its right subtree.`, A.tree('original', orig, { hl })); return trim(n.right); }
    if (n.val > hi) { hl[n.id] = 'bad'; mark(n.right, 'bad'); A.step(`${n.val} > ${hi}: drop it and its right subtree; continue in its left subtree.`, A.tree('original', orig, { hl })); return trim(n.left); }
    hl[n.id] = 'ok'; A.step(`${n.val} is in [${lo}, ${hi}]: keep it.`, A.tree('original', orig, { hl }));
    n.left = trim(n.left); n.right = trim(n.right); return n;
  };
  root = trim(root);
  A.step('The trimmed tree.', A.tree('trimmed', root));
}
A.scenario('[1, 3]', 'root = [3,0,4,null,2,null,null,1]', () => run([3, 0, 4, null, 2, null, null, 1], 1, 3));
'''),

P(num=674, slug="longest-continuous-increasing-subsequence", title="Longest Continuous Increasing Subsequence", diff="Easy", topic="Arrays & Hashing", cls="LongestContinuousIncreasing",
idea="Extend the current strictly increasing run or restart it; keep the longest.",
vname="Running length",
spec=r'''
Return the length of the longest strictly increasing **contiguous** subarray.

**Example**
```
[1,3,5,4,7] → 3,   [2,2,2,2,2] → 1
```

**Constraints**
* `1 <= nums.length <= 10^4`
''',
approach=r'''
**One pass.** `run = nums[i] > nums[i-1] ? run + 1 : 1`; track the maximum.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two counters.
''',
java=r'''
public class LongestContinuousIncreasing {

    public int findLengthOfLCIS(int[] nums) {
        int run = 1, best = 1;
        for (int i = 1; i < nums.length; i++) {
            run = nums[i] > nums[i - 1] ? run + 1 : 1;
            best = Math.max(best, run);
        }
        return best;
    }
}
''',
test=r'''
class LongestContinuousIncreasingTest {

    private final LongestContinuousIncreasing solution = new LongestContinuousIncreasing();

    @Test
    void examples() {
        assertEquals(3, solution.findLengthOfLCIS(new int[]{1, 3, 5, 4, 7}));
        assertEquals(1, solution.findLengthOfLCIS(new int[]{2, 2, 2, 2, 2}));
    }
}
''',
trace=r'''
function run(a) {
  let run = 1, best = 1;
  for (let i = 1; i < a.length; i++) { run = a[i] > a[i - 1] ? run + 1 : 1; best = Math.max(best, run); A.step(a[i] > a[i - 1] ? `${a[i]} > ${a[i - 1]}: the run grows to ${run}.` : `${a[i]} ≤ ${a[i - 1]}: restart the run.`, A.arr('nums', a, { range: [i - run + 1, i], hl: { [i]: a[i] > a[i - 1] ? 'ok' : 'bad' } }), A.vars({ run, best })); }
  A.step(`Longest: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', 'nums = [1,3,5,4,7]', () => run([1, 3, 5, 4, 7]));
'''),
]
