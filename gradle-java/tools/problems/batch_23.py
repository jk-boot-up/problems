PROBLEMS = [
P(num=235, slug="lowest-common-ancestor-of-a-binary-search-tree", title="Lowest Common Ancestor of a Binary Search Tree", diff="Medium", topic="Binary Search Tree", cls="LowestCommonAncestorBST",
idea="In a BST, walk down from the root: go left if both values are smaller, right if both are larger; otherwise you are at the split.",
vname="Walk down by value", helpers=["TreeNode"],
spec=r'''
Given a BST and two of its nodes `p` and `q`, return their lowest common ancestor (a node is a descendant of itself).

**Example**
```
root = [6,2,8,0,4,7,9,null,null,3,5]: p = 2, q = 8 → 6;  p = 2, q = 4 → 2
```

**Constraints**
* `2 <= n <= 10^5`; values are unique; `p` and `q` exist.
''',
approach=r'''
**Use the ordering.** If both values are below the current node, the LCA is in the left subtree; if both are above, in the right. Otherwise
the current node separates them (or equals one of them): it is the LCA.

* Time: **O(h)** — one root-to-node walk.
* Space: **O(1)** — iterative.
''',
tc="log", sc="1",
java=r'''
public class LowestCommonAncestorBST {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode n = root;
        while (true) {
            if (p.val < n.val && q.val < n.val) n = n.left;
            else if (p.val > n.val && q.val > n.val) n = n.right;
            else return n;
        }
    }
}
''',
test=r'''
class LowestCommonAncestorBSTTest {

    private final LowestCommonAncestorBST solution = new LowestCommonAncestorBST();
    private final TreeNode root = TreeNode.of(6, 2, 8, 0, 4, 7, 9, null, null, 3, 5);

    private TreeNode node(int v) {
        TreeNode n = root;
        while (n.val != v) n = v < n.val ? n.left : n.right;
        return n;
    }

    @Test
    void examples() {
        assertEquals(6, solution.lowestCommonAncestor(root, node(2), node(8)).val);
        assertEquals(2, solution.lowestCommonAncestor(root, node(2), node(4)).val);
        assertEquals(4, solution.lowestCommonAncestor(root, node(3), node(5)).val);
    }
}
''',
trace=r'''
function run(arr, p, q) {
  const root = A.mkTree(arr), hl = {}; let n = root;
  const find = (x, v) => (!x ? null : x.val === v ? x : find(v < x.val ? x.left : x.right, v));
  hl[find(root, p).id] = hl[find(root, q).id] = 'alt';
  A.step(`Find the lowest common ancestor of ${p} and ${q} (purple). Start at the root and use the BST order to choose a direction.`, A.tree('BST', root, { hl }));
  while (true) {
    if (p < n.val && q < n.val) { A.step(`${p} and ${q} are both smaller than ${n.val}: go left.`, A.tree('BST', root, { hl: { ...hl, [n.id]: 'cur' } })); n = n.left; }
    else if (p > n.val && q > n.val) { A.step(`${p} and ${q} are both larger than ${n.val}: go right.`, A.tree('BST', root, { hl: { ...hl, [n.id]: 'cur' } })); n = n.right; }
    else { A.step(`${n.val} separates ${p} and ${q} (or is one of them): it is the LCA.`, A.tree('BST', root, { hl: { ...hl, [n.id]: 'ok' } }), A.text('Result', n.val, 'ok')); return; }
  }
}
A.scenario('Split deep', 'p = 3, q = 5', () => run([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], 3, 5));
A.scenario('Split at the root', 'p = 2, q = 8', () => run([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], 2, 8));
'''),

P(num=450, slug="delete-node-in-a-bst", title="Delete Node in a BST", diff="Medium", topic="Binary Search Tree", cls="DeleteNodeInBST",
idea="Find the node; if it has two children, replace its value with its in-order successor and delete that successor instead.",
vname="Recursive delete with successor", helpers=["TreeNode"],
spec=r'''
Delete the node with value `key` from a BST (if present) and return the root of the still-valid BST.

**Example**
```
root = [5,3,6,2,4,null,7], key = 3 → [5,4,6,2,null,null,7]  (or [5,2,6,null,4,null,7])
```

**Constraints**
* `0 <= n <= 10^4`; values are unique.
''',
approach=r'''
**Three cases.** Recurse toward `key`. A node with no left child is replaced by its right child (and vice versa). A node with two children
copies the smallest value of its right subtree (the in-order successor) and deletes that value from the right subtree.

* Time: **O(h)** — one walk down, plus one walk to the successor.
* Space: **O(h)** — the recursion stack.
''',
tc="log", sc="log",
java=r'''
public class DeleteNodeInBST {

    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else {
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            TreeNode succ = root.right;
            while (succ.left != null) succ = succ.left;
            root.val = succ.val;
            root.right = deleteNode(root.right, succ.val);
        }
        return root;
    }
}
''',
test=r'''
class DeleteNodeInBSTTest {

    private final DeleteNodeInBST solution = new DeleteNodeInBST();

    private static void inorder(TreeNode n, List<Integer> out) {
        if (n == null) return;
        inorder(n.left, out);
        out.add(n.val);
        inorder(n.right, out);
    }

    private List<Integer> afterDelete(int key, Integer... tree) {
        List<Integer> out = new ArrayList<>();
        inorder(solution.deleteNode(TreeNode.of(tree), key), out);
        return out;
    }

    @Test
    void twoChildren() {
        assertEquals(List.of(2, 4, 5, 6, 7), afterDelete(3, 5, 3, 6, 2, 4, null, 7));
    }

    @Test
    void leafRootAndMissing() {
        assertEquals(List.of(2, 3, 4, 5, 6), afterDelete(7, 5, 3, 6, 2, 4, null, 7));
        assertEquals(List.of(2, 3, 4, 6, 7), afterDelete(5, 5, 3, 6, 2, 4, null, 7));
        assertEquals(List.of(2, 3, 4, 5, 6, 7), afterDelete(0, 5, 3, 6, 2, 4, null, 7));
    }
}
''',
trace=r'''
function run(arr, key) {
  let root = A.mkTree(arr);
  const del = (n, k) => {
    if (!n) return null;
    if (k < n.val) { A.step(`${k} < ${n.val}: go left.`, A.tree('BST', root, { hl: { [n.id]: 'cur' } })); n.left = del(n.left, k); return n; }
    if (k > n.val) { A.step(`${k} > ${n.val}: go right.`, A.tree('BST', root, { hl: { [n.id]: 'cur' } })); n.right = del(n.right, k); return n; }
    if (!n.left || !n.right) { A.step(`Found ${k}. It has ${!n.left && !n.right ? 'no children: just remove it' : 'one child: that child takes its place'}.`, A.tree('BST', root, { hl: { [n.id]: 'bad' } })); return n.left || n.right; }
    let s = n.right; while (s.left) s = s.left;
    A.step(`Found ${k} with two children. Its in-order successor is ${s.val}, the smallest value on its right. Copy ${s.val} here, then delete it from the right subtree.`, A.tree('BST', root, { hl: { [n.id]: 'bad', [s.id]: 'alt' } }));
    n.val = s.val; n.right = del(n.right, s.val); return n;
  };
  root = del(root, key);
  A.step('The tree is still a valid BST.', A.tree('BST', root));
}
A.scenario('Two children', 'delete 3 from [5,3,6,2,4,null,7]', () => run([5, 3, 6, 2, 4, null, 7], 3));
A.scenario('Leaf', 'delete 7', () => run([5, 3, 6, 2, 4, null, 7], 7));
'''),

P(num=700, slug="search-in-a-binary-search-tree", title="Search in a Binary Search Tree", diff="Easy", topic="Binary Search Tree", cls="SearchInBST",
idea="Compare with the current node and go left or right; the BST order tells you which way.",
vname="Iterative descent", helpers=["TreeNode"],
spec=r'''
Return the subtree rooted at the node whose value is `val` in a BST, or `null` if it does not exist.

**Example**
```
root = [4,2,7,1,3], val = 2 → [2,1,3],   val = 5 → null
```

**Constraints**
* `1 <= n <= 5000`
''',
approach=r'''
**Descend.** While the node exists and differs from `val`, move to `left` if `val` is smaller, else `right`.

* Time: **O(h)** — one root-to-node path.
* Space: **O(1)** — iterative.
''',
tc="log", sc="1",
java=r'''
public class SearchInBST {

    public TreeNode searchBST(TreeNode root, int val) {
        TreeNode n = root;
        while (n != null && n.val != val) n = val < n.val ? n.left : n.right;
        return n;
    }
}
''',
test=r'''
class SearchInBSTTest {

    private final SearchInBST solution = new SearchInBST();

    @Test
    void examples() {
        assertEquals(List.of(2, 1, 3), TreeNode.toList(solution.searchBST(TreeNode.of(4, 2, 7, 1, 3), 2)));
        assertNull(solution.searchBST(TreeNode.of(4, 2, 7, 1, 3), 5));
    }
}
''',
trace=r'''
function run(arr, v) {
  const root = A.mkTree(arr); let n = root; const path = {};
  while (n && n.val !== v) { path[n.id] = 'sel'; A.step(`${v} ${v < n.val ? '<' : '>'} ${n.val}: go ${v < n.val ? 'left' : 'right'}.`, A.tree('BST', root, { hl: { ...path, [n.id]: 'cur' } })); n = v < n.val ? n.left : n.right; }
  A.step(n ? `Found ${v}.` : `Fell off the tree: ${v} is not present.`, A.tree('BST', root, { hl: n ? { ...path, [n.id]: 'ok' } : path }), A.text('Result', n ? `subtree at ${v}` : 'null', n ? 'ok' : 'bad'));
}
A.scenario('Found', 'val = 3', () => run([4, 2, 7, 1, 3], 3));
A.scenario('Missing', 'val = 5', () => run([4, 2, 7, 1, 3], 5));
'''),

P(num=701, slug="insert-into-a-binary-search-tree", title="Insert into a Binary Search Tree", diff="Medium", topic="Binary Search Tree", cls="InsertIntoBST",
idea="Walk down as if searching for the value; attach it where the search falls off the tree.",
vname="Iterative descent", helpers=["TreeNode"],
spec=r'''
Insert `val` (not already present) into a BST and return the root. Any valid BST is accepted.

**Example**
```
root = [4,2,7,1,3], val = 5 → [4,2,7,1,3,5]
```

**Constraints**
* `0 <= n <= 10^4`
''',
approach=r'''
**Search, then attach.** Descend left or right; when the chosen child is null, place the new node there.

* Time: **O(h)** — one root-to-leaf path.
* Space: **O(1)** — iterative.
''',
tc="log", sc="1",
java=r'''
public class InsertIntoBST {

    public TreeNode insertIntoBST(TreeNode root, int val) {
        TreeNode node = new TreeNode(val);
        if (root == null) return node;
        TreeNode n = root;
        while (true) {
            if (val < n.val) {
                if (n.left == null) { n.left = node; break; }
                n = n.left;
            } else {
                if (n.right == null) { n.right = node; break; }
                n = n.right;
            }
        }
        return root;
    }
}
''',
test=r'''
class InsertIntoBSTTest {

    private final InsertIntoBST solution = new InsertIntoBST();

    @Test
    void examples() {
        assertEquals(List.of(4, 2, 7, 1, 3, 5), TreeNode.toList(solution.insertIntoBST(TreeNode.of(4, 2, 7, 1, 3), 5)));
        assertEquals(List.of(5), TreeNode.toList(solution.insertIntoBST(null, 5)));
    }
}
''',
trace=r'''
function run(arr, v) {
  const root = A.mkTree(arr); let n = root; const path = {};
  while (true) {
    path[n.id] = 'sel';
    const left = v < n.val, child = left ? n.left : n.right;
    if (!child) { const node = A.node(v); if (left) n.left = node; else n.right = node; A.step(`${v} ${left ? '<' : '>'} ${n.val} and that side is empty: attach ${v} as the ${left ? 'left' : 'right'} child.`, A.tree('BST', root, { hl: { ...path, [node.id]: 'ok' } })); return; }
    A.step(`${v} ${left ? '<' : '>'} ${n.val}: go ${left ? 'left' : 'right'}.`, A.tree('BST', root, { hl: { ...path, [n.id]: 'cur' } }));
    n = child;
  }
}
A.scenario('Insert 5', 'root = [4,2,7,1,3]', () => run([4, 2, 7, 1, 3], 5));
'''),

P(num=994, slug="rotting-oranges", title="Rotting Oranges", diff="Medium", topic="Graph BFS", cls="RottingOranges",
idea="Multi-source BFS: all rotten oranges spread together, one minute per BFS level.",
vname="Multi-source BFS",
spec=r'''
In a grid, `0` is empty, `1` a fresh orange and `2` a rotten one. Every minute, fresh oranges next to (4-directionally) a rotten one
become rotten. Return the minutes until no fresh orange remains, or `-1` if that never happens.

**Example**
```
[[2,1,1],[1,1,0],[0,1,1]] → 4
[[2,1,1],[0,1,1],[1,0,1]] → -1
[[0,2]]                   → 0
```

**Constraints**
* `1 <= m, n <= 10`
''',
approach=r'''
**BFS from every rotten orange at once.** Queue all rotten cells and count fresh ones. Each BFS level is one minute: rot the fresh
neighbours of the current level. At the end, any fresh orange left means `-1`.

* Time: **O(m·n)** — each cell is processed once.
* Space: **O(m·n)** — the queue.
''',
tc="n2", sc="n2",
java=r'''
public class RottingOranges {

    public int orangesRotting(int[][] grid) {
        int m = grid.length, n = grid[0].length, fresh = 0;
        Deque<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 2) queue.add(new int[]{r, c});
                else if (grid[r][c] == 1) fresh++;
            }
        }
        int minutes = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (fresh > 0 && !queue.isEmpty()) {
            minutes++;
            for (int size = queue.size(); size > 0; size--) {
                int[] cell = queue.poll();
                for (int[] d : dirs) {
                    int r = cell[0] + d[0], c = cell[1] + d[1];
                    if (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] == 1) {
                        grid[r][c] = 2;
                        fresh--;
                        queue.add(new int[]{r, c});
                    }
                }
            }
        }
        return fresh == 0 ? minutes : -1;
    }
}
''',
test=r'''
class RottingOrangesTest {

    private final RottingOranges solution = new RottingOranges();

    @Test
    void examples() {
        assertEquals(4, solution.orangesRotting(new int[][]{{2, 1, 1}, {1, 1, 0}, {0, 1, 1}}));
        assertEquals(-1, solution.orangesRotting(new int[][]{{2, 1, 1}, {0, 1, 1}, {1, 0, 1}}));
        assertEquals(0, solution.orangesRotting(new int[][]{{0, 2}}));
    }
}
''',
trace=r'''
function run(g0) {
  const g = g0.map(r => r.slice()), m = g.length, n = g[0].length; let q = [], fresh = 0;
  g.forEach((r, i) => r.forEach((v, j) => { if (v === 2) q.push([i, j]); else if (v === 1) fresh++; }));
  const view = (msg, now = []) => A.step(msg, A.grid('grid', g.map(r => r.map(v => (v === 0 ? '' : v === 1 ? '🍊' : '🟤'))), { hl: g.flatMap((r, i) => r.map((v, j) => [`${i},${j}`, now.some(([a, b]) => a === i && b === j) ? 'bad' : v === 2 ? 'dim' : v === 1 ? 'ok' : ''])) }), A.vars({ fresh }));
  view('Every rotten orange spreads at the same time. Each round of the BFS is one minute.');
  let minutes = 0;
  while (fresh && q.length) {
    minutes++; const nq = [];
    for (const [r, c] of q) for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const a = r + dr, b = c + dc; if (a >= 0 && a < m && b >= 0 && b < n && g[a][b] === 1) { g[a][b] = 2; fresh--; nq.push([a, b]); } }
    q = nq;
    view(`Minute ${minutes}: ${nq.length} orange${nq.length === 1 ? '' : 's'} rot.`, nq);
  }
  A.step(fresh ? `${fresh} orange${fresh === 1 ? ' is' : 's are'} cut off and never rot: the answer is -1.` : `All oranges are rotten after ${minutes} minutes.`, A.text('Result', fresh ? -1 : minutes, fresh ? 'bad' : 'ok'));
}
A.scenario('Four minutes', '[[2,1,1],[1,1,0],[0,1,1]]', () => run([[2, 1, 1], [1, 1, 0], [0, 1, 1]]));
A.scenario('Unreachable orange', '[[2,1,1],[0,1,1],[1,0,1]]', () => run([[2, 1, 1], [0, 1, 1], [1, 0, 1]]));
'''),

P(num=695, slug="max-area-of-island", title="Max Area of Island", diff="Medium", topic="Graph General", cls="MaxAreaOfIsland",
idea="Flood-fill each island once, counting its cells, and keep the largest count.",
vname="DFS flood fill",
spec=r'''
In a binary grid, an island is a group of `1`s connected 4-directionally. Return the area of the largest island (0 if none).

**Example**
```
A grid with islands of sizes 1, 3, 4 and 6 → 6
```

**Constraints**
* `1 <= m, n <= 50`
''',
approach=r'''
**Flood fill.** For each unvisited `1`, run DFS with an explicit stack, zeroing cells as they are counted.

* Time: **O(m·n)** — each cell is visited once.
* Space: **O(m·n)** — the stack in the worst case.
''',
tc="n2", sc="n2",
java=r'''
public class MaxAreaOfIsland {

    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length, best = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] != 1) continue;
                int area = 0;
                Deque<int[]> stack = new ArrayDeque<>();
                stack.push(new int[]{r, c});
                grid[r][c] = 0;
                while (!stack.isEmpty()) {
                    int[] cell = stack.pop();
                    area++;
                    for (int[] d : dirs) {
                        int a = cell[0] + d[0], b = cell[1] + d[1];
                        if (a >= 0 && a < m && b >= 0 && b < n && grid[a][b] == 1) {
                            grid[a][b] = 0;
                            stack.push(new int[]{a, b});
                        }
                    }
                }
                best = Math.max(best, area);
            }
        }
        return best;
    }
}
''',
test=r'''
class MaxAreaOfIslandTest {

    private final MaxAreaOfIsland solution = new MaxAreaOfIsland();

    @Test
    void examples() {
        int[][] g = {{0, 0, 1, 0, 0}, {0, 1, 1, 0, 1}, {0, 0, 0, 1, 1}, {1, 1, 0, 1, 1}};
        assertEquals(5, solution.maxAreaOfIsland(g));
        assertEquals(0, solution.maxAreaOfIsland(new int[][]{{0, 0, 0}}));
    }
}
''',
trace=r'''
function run(g0) {
  const g = g0.map(r => r.slice()), m = g.length, n = g[0].length, col = {}; let best = 0, k = 0;
  const hues = ['sel', 'alt', 'cur', 'ok'];
  const view = msg => A.step(msg, A.grid('grid', g0.map(r => r.map(() => '')), { hl: g0.flatMap((r, i) => r.map((v, j) => [`${i},${j}`, col[`${i},${j}`] || (v ? 'bar' : '')])) }), A.vars({ best }));
  view('Grey cells are land. Flood-fill each island and count its cells.');
  for (let r = 0; r < m; r++) for (let c = 0; c < n; c++) {
    if (g[r][c] !== 1) continue;
    const hue = hues[k++ % 4], st = [[r, c]]; g[r][c] = 0; let area = 0;
    while (st.length) { const [x, y] = st.pop(); area++; col[`${x},${y}`] = hue; for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const a = x + dx, b = y + dy; if (a >= 0 && a < m && b >= 0 && b < n && g[a][b] === 1) { g[a][b] = 0; st.push([a, b]); } } }
    best = Math.max(best, area);
    view(`Island starting at (${r},${c}) has area ${area}. Largest so far: ${best}.`);
  }
  A.step(`The largest island has area ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Several islands', '4 × 5 grid', () => run([[0, 0, 1, 0, 0], [0, 1, 1, 0, 1], [0, 0, 0, 1, 1], [1, 1, 0, 1, 1]]));
'''),

P(num=417, slug="pacific-atlantic-water-flow", title="Pacific Atlantic Water Flow", diff="Medium", topic="Graph General", cls="PacificAtlanticWaterFlow",
idea="Flow backwards: climb uphill from each ocean's border; cells reached from both oceans are the answer.",
vname="Reverse BFS from both oceans",
spec=r'''
Rain flows from a cell to a 4-directional neighbour of **equal or lower** height. The Pacific touches the top and left edges, the
Atlantic the bottom and right edges. Return all cells from which water can reach **both** oceans.

**Example**
```
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
→ [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**Constraints**
* `1 <= m, n <= 200`
''',
approach=r'''
**Reverse the flow.** From every Pacific border cell, BFS to neighbours that are **higher or equal** (water could flow down from them);
do the same for the Atlantic. Return the cells marked by both searches.

* Time: **O(m·n)** — two BFS passes.
* Space: **O(m·n)** — two visited grids.
''',
tc="n2", sc="n2",
java=r'''
public class PacificAtlanticWaterFlow {

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        boolean[][] pac = new boolean[m][n], atl = new boolean[m][n];
        Deque<int[]> pq = new ArrayDeque<>(), aq = new ArrayDeque<>();
        for (int r = 0; r < m; r++) {
            mark(pac, pq, r, 0);
            mark(atl, aq, r, n - 1);
        }
        for (int c = 0; c < n; c++) {
            mark(pac, pq, 0, c);
            mark(atl, aq, m - 1, c);
        }
        bfs(heights, pac, pq);
        bfs(heights, atl, aq);
        List<List<Integer>> out = new ArrayList<>();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (pac[r][c] && atl[r][c]) out.add(List.of(r, c));
            }
        }
        return out;
    }

    private static void mark(boolean[][] seen, Deque<int[]> q, int r, int c) {
        if (!seen[r][c]) {
            seen[r][c] = true;
            q.add(new int[]{r, c});
        }
    }

    private static void bfs(int[][] h, boolean[][] seen, Deque<int[]> q) {
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty()) {
            int[] cell = q.poll();
            for (int[] d : dirs) {
                int r = cell[0] + d[0], c = cell[1] + d[1];
                if (r >= 0 && r < h.length && c >= 0 && c < h[0].length && !seen[r][c] && h[r][c] >= h[cell[0]][cell[1]]) {
                    mark(seen, q, r, c);
                }
            }
        }
    }
}
''',
test=r'''
class PacificAtlanticWaterFlowTest {

    private final PacificAtlanticWaterFlow solution = new PacificAtlanticWaterFlow();

    @Test
    void example() {
        int[][] h = {{1, 2, 2, 3, 5}, {3, 2, 3, 4, 4}, {2, 4, 5, 3, 1}, {6, 7, 1, 4, 5}, {5, 1, 1, 2, 4}};
        assertEquals(List.of(List.of(0, 4), List.of(1, 3), List.of(1, 4), List.of(2, 2), List.of(3, 0), List.of(3, 1), List.of(4, 0)),
                solution.pacificAtlantic(h));
    }

    @Test
    void single() {
        assertEquals(List.of(List.of(0, 0)), solution.pacificAtlantic(new int[][]{{1}}));
    }
}
''',
trace=r'''
function run(h) {
  const m = h.length, n = h[0].length;
  const climb = starts => { const seen = new Set(starts.map(([r, c]) => `${r},${c}`)), q = starts.slice(); while (q.length) { const [r, c] = q.shift(); for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const a = r + dr, b = c + dc, k = `${a},${b}`; if (a >= 0 && a < m && b >= 0 && b < n && !seen.has(k) && h[a][b] >= h[r][c]) { seen.add(k); q.push([a, b]); } } } return seen; };
  const pS = [], aS = []; for (let r = 0; r < m; r++) { pS.push([r, 0]); aS.push([r, n - 1]); } for (let c = 0; c < n; c++) { pS.push([0, c]); aS.push([m - 1, c]); }
  const pac = climb(pS);
  A.step('Pacific (top and left edges): climb uphill from the border. Every blue cell can drain into the Pacific.', A.grid('heights', h, { hl: [...pac].map(k => [k, 'sel']) }));
  const atl = climb(aS);
  A.step('Atlantic (bottom and right edges): the same from the other border. Purple cells drain into the Atlantic.', A.grid('heights', h, { hl: [...atl].map(k => [k, 'alt']) }));
  const both = [...pac].filter(k => atl.has(k));
  A.step(`${both.length} cells drain into both oceans (green).`, A.grid('heights', h, { hl: both.map(k => [k, 'ok']) }), A.text('Result', both.map(k => `[${k}]`).join(' '), 'ok'));
}
A.scenario('Classic', '5 × 5 heights', () => run([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]));
'''),

P(num=684, slug="redundant-connection", title="Redundant Connection", diff="Medium", topic="Graph General", cls="RedundantConnection",
idea="Union-find: the first edge whose endpoints are already connected closes the cycle.",
vname="Union-find",
spec=r'''
A tree on nodes `1..n` had one extra edge added. Given the `n` edges, return an edge that can be removed so the graph becomes a tree; if
several work, return the one that appears last in the input.

**Example**
```
[[1,2],[1,3],[2,3]]                 → [2,3]
[[1,2],[2,3],[3,4],[1,4],[1,5]]     → [1,4]
```

**Constraints**
* `3 <= n <= 1000`
''',
approach=r'''
**Disjoint sets.** Process edges in order; `union(a, b)` fails exactly when `a` and `b` already share a root, so that edge is redundant
(and it is the last edge of the cycle in input order). Path compression and union by size keep operations nearly O(1).

* Time: **O(n·α(n))** — essentially linear.
* Space: **O(n)** — the parent array.
''',
java=r'''
public class RedundantConnection {

    private int[] parent, size;

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        parent = new int[n + 1];
        size = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        for (int[] e : edges) {
            int a = find(e[0]), b = find(e[1]);
            if (a == b) return e;
            if (size[a] < size[b]) { int t = a; a = b; b = t; }
            parent[b] = a;
            size[a] += size[b];
        }
        return new int[0];
    }
}
''',
test=r'''
class RedundantConnectionTest {

    private final RedundantConnection solution = new RedundantConnection();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 3}, solution.findRedundantConnection(new int[][]{{1, 2}, {1, 3}, {2, 3}}));
        assertArrayEquals(new int[]{1, 4}, solution.findRedundantConnection(new int[][]{{1, 2}, {2, 3}, {3, 4}, {1, 4}, {1, 5}}));
    }
}
''',
trace=r'''
function run(edges) {
  const n = edges.length, par = [...Array(n + 1).keys()];
  const find = x => (par[x] === x ? x : (par[x] = find(par[x])));
  const nodes = [...Array(n)].map((_, i) => ({ id: i + 1, label: i + 1 }));
  const shown = [];
  for (const [a, b] of edges) {
    const ra = find(a), rb = find(b);
    if (ra === rb) { A.step(`${a} and ${b} are already in the same group. Edge [${a},${b}] closes a cycle: it is redundant.`, A.graph('graph', nodes, shown.concat([[a, b, '', 'bad']]), { hl: { [a]: 'bad', [b]: 'bad' } }), A.text('Result', `[${a},${b}]`, 'ok')); return; }
    par[rb] = ra; shown.push([a, b, '', 'ok']);
    A.step(`Edge [${a},${b}] joins two different groups. Merge them.`, A.graph('graph', nodes, shown, { hl: Object.fromEntries(nodes.map(x => [x.id, find(x.id) === find(a) ? 'sel' : ''])) }), A.arr('parent', par.slice(1)));
  }
}
A.scenario('Cycle 1-2-3-4', '[[1,2],[2,3],[3,4],[1,4],[1,5]]', () => run([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]));
'''),

P(num=743, slug="network-delay-time", title="Network Delay Time", diff="Medium", topic="Graph General", cls="NetworkDelayTime",
idea="Dijkstra from the source; the answer is the largest shortest-path distance (or -1 if a node is unreachable).",
vname="Dijkstra with a heap",
spec=r'''
`times[i] = [u, v, w]` is a directed edge from node `u` to `v` taking `w` time. A signal starts at node `k`. Return the time for all `n`
nodes to receive it, or `-1` if some node never does.

**Example**
```
times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2 → 2
times = [[1,2,1]], n = 2, k = 2                  → -1
```

**Constraints**
* `1 <= k <= n <= 100`; `1 <= times.length <= 6000`; `0 <= w <= 100`
''',
approach=r'''
**Dijkstra.** Build adjacency lists. Pop the closest unsettled node from a min-heap, settle it, and relax its edges. The latest settle time is
the answer if all `n` nodes were settled.

* Time: **O(E log V)** — each edge may push one heap entry.
* Space: **O(V + E)** — graph, distances and heap.
''',
tc="nlogn", sc="n",
java=r'''
public class NetworkDelayTime {

    public int networkDelayTime(int[][] times, int n, int k) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        for (int[] t : times) graph.get(t[0]).add(new int[]{t[1], t[2]});
        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        heap.add(new int[]{k, 0});
        int settled = 0, latest = 0;
        boolean[] done = new boolean[n + 1];
        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int u = cur[0];
            if (done[u]) continue;
            done[u] = true;
            settled++;
            latest = cur[1];
            for (int[] e : graph.get(u)) {
                if (cur[1] + e[1] < dist[e[0]]) {
                    dist[e[0]] = cur[1] + e[1];
                    heap.add(new int[]{e[0], dist[e[0]]});
                }
            }
        }
        return settled == n ? latest : -1;
    }
}
''',
test=r'''
class NetworkDelayTimeTest {

    private final NetworkDelayTime solution = new NetworkDelayTime();

    @Test
    void examples() {
        assertEquals(2, solution.networkDelayTime(new int[][]{{2, 1, 1}, {2, 3, 1}, {3, 4, 1}}, 4, 2));
        assertEquals(1, solution.networkDelayTime(new int[][]{{1, 2, 1}}, 2, 1));
        assertEquals(-1, solution.networkDelayTime(new int[][]{{1, 2, 1}}, 2, 2));
    }

    @Test
    void shorterIndirectPath() {
        assertEquals(3, solution.networkDelayTime(new int[][]{{1, 2, 5}, {1, 3, 1}, {3, 2, 2}}, 3, 1));
    }
}
''',
trace=r'''
function run(times, n, k) {
  const nodes = [...Array(n)].map((_, i) => ({ id: i + 1, label: i + 1 })), edges = times.map(([u, v, w]) => [u, v, w]);
  const dist = new Array(n + 1).fill(Infinity), done = new Set(); dist[k] = 0; const heap = [[k, 0]];
  const f = d => (d === Infinity ? '∞' : d);
  A.step(`The signal starts at node ${k}. Always settle the closest unsettled node next.`, A.graph('network', nodes, edges, { directed: true, hl: { [k]: 'cur' } }), A.arr('dist', dist.slice(1).map(f)));
  while (heap.length) {
    heap.sort((a, b) => a[1] - b[1]); const [u, d] = heap.shift();
    if (done.has(u)) continue; done.add(u);
    const relaxed = [];
    for (const [a, b, w] of times) if (a === u && d + w < dist[b]) { dist[b] = d + w; heap.push([b, dist[b]]); relaxed.push(b); }
    A.step(`Settle node ${u} at time ${d}.${relaxed.length ? ` Its edges improve node${relaxed.length > 1 ? 's' : ''} ${relaxed.join(', ')}.` : ''}`, A.graph('network', nodes, edges.map(([a, b, w]) => [a, b, w, a === u ? 'cur' : '']), { directed: true, hl: Object.fromEntries([...done].map(x => [x, x === u ? 'cur' : 'ok'])) }), A.arr('dist', dist.slice(1).map(f), { hl: Object.fromEntries(relaxed.map(x => [x - 1, 'sel'])) }));
  }
  const ans = done.size === n ? Math.max(...dist.slice(1)) : -1;
  A.step(ans < 0 ? 'Some node was never reached: -1.' : `Every node is reached; the last one gets the signal at time ${ans}.`, A.text('Result', ans, ans < 0 ? 'bad' : 'ok'));
}
A.scenario('Shorter indirect path', 'n = 4, k = 1', () => run([[1, 2, 5], [1, 3, 1], [3, 2, 2], [2, 4, 1]], 4, 1));
'''),

P(num=787, slug="cheapest-flights-within-k-stops", title="Cheapest Flights Within K Stops", diff="Medium", topic="Graph General", cls="CheapestFlights",
idea="Bellman–Ford limited to k + 1 rounds: round i finds the cheapest prices using at most i flights.",
vname="Bellman–Ford with k + 1 rounds",
spec=r'''
`flights[i] = [from, to, price]`. Return the cheapest price from `src` to `dst` using at most `k` stops (k + 1 flights), or `-1`.

**Example**
```
n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1 → 700
n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0 → 500
```

**Constraints**
* `1 <= n <= 100`; `0 <= k < n`
''',
approach=r'''
**Bounded relaxation.** Keep `cost[]` (∞ except `src = 0`). Repeat `k + 1` times: copy `cost` to `next`, and for each flight relax
`next[to] = min(next[to], cost[from] + price)`, reading from the **previous** round so each round adds at most one flight.

* Time: **O(k · E)** — k + 1 rounds over all flights.
* Space: **O(n)** — two price arrays.
''',
tc="n2", sc="n",
java=r'''
public class CheapestFlights {

    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int inf = Integer.MAX_VALUE;
        int[] cost = new int[n];
        Arrays.fill(cost, inf);
        cost[src] = 0;
        for (int round = 0; round <= k; round++) {
            int[] next = cost.clone();
            for (int[] f : flights) {
                if (cost[f[0]] != inf && cost[f[0]] + f[2] < next[f[1]]) next[f[1]] = cost[f[0]] + f[2];
            }
            cost = next;
        }
        return cost[dst] == inf ? -1 : cost[dst];
    }
}
''',
test=r'''
class CheapestFlightsTest {

    private final CheapestFlights solution = new CheapestFlights();

    @Test
    void examples() {
        assertEquals(700, solution.findCheapestPrice(4, new int[][]{{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}}, 0, 3, 1));
        assertEquals(200, solution.findCheapestPrice(3, new int[][]{{0, 1, 100}, {1, 2, 100}, {0, 2, 500}}, 0, 2, 1));
        assertEquals(500, solution.findCheapestPrice(3, new int[][]{{0, 1, 100}, {1, 2, 100}, {0, 2, 500}}, 0, 2, 0));
    }
}
''',
trace=r'''
function run(n, flights, src, dst, k) {
  const nodes = [...Array(n)].map((_, i) => ({ id: i, label: i })), f = c => (c === Infinity ? '∞' : c);
  let cost = new Array(n).fill(Infinity); cost[src] = 0;
  A.step(`Round i finds the cheapest prices using at most i flights. We may take ${k + 1} flight${k ? 's' : ''}.`, A.graph('flights', nodes, flights.map(([a, b, p]) => [a, b, p]), { directed: true, hl: { [src]: 'cur', [dst]: 'alt' } }), A.arr('cost', cost.map(f)));
  for (let r = 0; r <= k; r++) {
    const next = cost.slice(), used = [];
    for (const [a, b, p] of flights) if (cost[a] !== Infinity && cost[a] + p < next[b]) { next[b] = cost[a] + p; used.push([a, b]); }
    cost = next;
    A.step(`Round ${r + 1}: each flight extends a route found in the previous round.`, A.graph('flights', nodes, flights.map(([a, b, p]) => [a, b, p, used.some(([x, y]) => x === a && y === b) ? 'ok' : '']), { directed: true, hl: { [src]: 'cur', [dst]: 'alt' } }), A.arr('cost', cost.map(f), { hl: Object.fromEntries(used.map(([, b]) => [b, 'ok'])) }));
  }
  A.step(cost[dst] === Infinity ? 'The destination is unreachable within the stop limit.' : `Cheapest price within ${k} stop${k === 1 ? '' : 's'}: ${cost[dst]}.`, A.text('Result', cost[dst] === Infinity ? -1 : cost[dst], 'ok'));
}
A.scenario('k = 1', 'n = 4, src = 0, dst = 3', () => run(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1));
A.scenario('k = 0', 'n = 3, src = 0, dst = 2', () => run(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0));
'''),
]
