PROBLEMS = [
P(num=946, slug="validate-stack-sequences", title="Validate Stack Sequences", diff="Medium", topic="Stack", cls="ValidateStackSequences",
idea="Replay the pushes on a real stack and pop greedily whenever the top is the next value to pop.",
vname="Simulate with a stack",
spec=r'''
Given two arrays `pushed` and `popped` with distinct values, return `true` if they could be the result of a sequence of push and pop
operations on an initially empty stack.

**Example**
```
pushed = [1,2,3,4,5], popped = [4,5,3,2,1] → true
pushed = [1,2,3,4,5], popped = [4,3,5,1,2] → false
```

**Constraints**
* `1 <= n <= 1000`; `popped` is a permutation of `pushed`
''',
approach=r'''
**Greedy replay.** Push values in order. After each push, pop while the top equals the next expected popped value. Popping as early as
possible never hurts, because a value on top can only leave by being popped now or later, and later only buries it. The sequence is valid
iff the stack ends empty.

* Time: **O(n)** — each value is pushed and popped once.
* Space: **O(n)** — the stack.
''',
tc="n", sc="n",
java=r'''
public class ValidateStackSequences {

    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Deque<Integer> stack = new ArrayDeque<>();
        int j = 0;
        for (int v : pushed) {
            stack.push(v);
            while (!stack.isEmpty() && stack.peek() == popped[j]) {
                stack.pop();
                j++;
            }
        }
        return stack.isEmpty();
    }
}
''',
test=r'''
class ValidateStackSequencesTest {

    private final ValidateStackSequences solution = new ValidateStackSequences();

    @Test
    void examples() {
        assertTrue(solution.validateStackSequences(new int[]{1, 2, 3, 4, 5}, new int[]{4, 5, 3, 2, 1}));
        assertFalse(solution.validateStackSequences(new int[]{1, 2, 3, 4, 5}, new int[]{4, 3, 5, 1, 2}));
        assertTrue(solution.validateStackSequences(new int[]{1}, new int[]{1}));
        assertTrue(solution.validateStackSequences(new int[]{2, 1, 0}, new int[]{1, 2, 0}));
    }
}
''',
trace=r'''
function run(pushed, popped) {
  const st = []; let j = 0;
  A.step('Push in order; pop whenever the top is the next value we must pop.', A.arr('pushed', pushed), A.arr('popped', popped), A.stack('stack', st));
  pushed.forEach((v, i) => {
    st.push(v); const out = [];
    while (st.length && st[st.length - 1] === popped[j]) { out.push(st.pop()); j++; }
    A.step(`Push ${v}.${out.length ? ` The top matches the next pop: pop ${out.join(', ')}.` : ''}`, A.arr('pushed', pushed, { hl: { [i]: 'cur' } }), A.arr('popped', popped, { hl: Object.fromEntries(Array.from({ length: j }, (_, k) => [k, 'ok'])), ptr: j < popped.length ? { [j]: 'next' } : {} }), A.stack('stack', st));
  });
  const ok = st.length === 0;
  A.step(ok ? 'The stack is empty: the sequences are consistent.' : `${st[st.length - 1]} is stuck on top but ${popped[j]} must come out next.`, A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('Valid', '[4,5,3,2,1]', () => run([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]));
A.scenario('Invalid', '[4,3,5,1,2]', () => run([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]));
'''),

P(num=950, slug="reveal-cards-in-increasing-order", title="Reveal Cards In Increasing Order", diff="Medium", topic="Queue", cls="RevealCardsIncreasing",
idea="Simulate the reveal process on positions instead of cards, then drop the sorted cards into the positions in reveal order.",
vname="Simulate on indices",
spec=r'''
A deck is revealed like this: reveal the top card and remove it, then move the next top card to the bottom; repeat until empty. Order the
deck so the cards are revealed in **increasing** order.

**Example**
```
[17,13,11,2,3,5,7] → [2,13,3,11,5,17,7]
```

**Constraints**
* `1 <= deck.length <= 1000`, distinct values
''',
approach=r'''
**Positions.** Put positions `0..n-1` in a queue. Run the process on the queue: the position at the front is revealed next (give it the
next smallest card), then the following position moves to the back.

* Time: **O(n log n)** — sorting.
* Space: **O(n)** — the queue.
''',
tc="nlogn", sc="n",
java=r'''
public class RevealCardsIncreasing {

    public int[] deckRevealedIncreasing(int[] deck) {
        int n = deck.length;
        int[] sorted = deck.clone(), out = new int[n];
        Arrays.sort(sorted);
        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) queue.add(i);
        for (int card : sorted) {
            out[queue.poll()] = card;
            if (!queue.isEmpty()) queue.add(queue.poll());
        }
        return out;
    }
}
''',
test=r'''
class RevealCardsIncreasingTest {

    private final RevealCardsIncreasing solution = new RevealCardsIncreasing();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 13, 3, 11, 5, 17, 7}, solution.deckRevealedIncreasing(new int[]{17, 13, 11, 2, 3, 5, 7}));
        assertArrayEquals(new int[]{1, 1000}, solution.deckRevealedIncreasing(new int[]{1000, 1}));
        assertArrayEquals(new int[]{4}, solution.deckRevealedIncreasing(new int[]{4}));
    }
}
''',
trace=r'''
function run(deck) {
  const n = deck.length, s = deck.slice().sort((a, b) => a - b), out = new Array(n).fill('·'), q = [...Array(n).keys()];
  A.step('Play the reveal process on positions. Whatever position is revealed k-th gets the k-th smallest card.', A.arr('sorted cards', s), A.arr('queue of positions', q));
  s.forEach((c, k) => {
    const p = q.shift(); out[p] = c; let moved = null;
    if (q.length) { moved = q.shift(); q.push(moved); }
    A.step(`Reveal position ${p}: it gets ${c}.${moved !== null ? ` Then position ${moved} goes to the back.` : ''}`, A.arr('sorted cards', s, { hl: { [k]: 'ok' } }), A.arr('deck', out, { hl: { [p]: 'ok' } }), A.arr('queue of positions', q));
  });
  A.step(`Deck order: [${out}].`, A.arr('deck', out));
}
A.scenario('Example', '[17,13,11,2,3,5,7]', () => run([17, 13, 11, 2, 3, 5, 7]));
'''),

P(num=979, slug="distribute-coins-in-binary-tree", title="Distribute Coins in Binary Tree", diff="Medium", topic="Binary Tree DFS", cls="DistributeCoins",
idea="Every edge must carry the surplus (or deficit) of the subtree below it; the answer is the sum of |surplus| over all edges.",
vname="Post-order surplus",
spec=r'''
A binary tree has `n` nodes and `n` coins in total (`node.val` coins on each node). One move sends one coin across one edge. Return the
fewest moves so that every node has exactly one coin.

**Example**
```
[3,0,0] → 2
[0,3,0] → 3
```

**Constraints**
* `1 <= n <= 100`
''',
approach=r'''
**Edge flow.** A subtree with `s` nodes and `c` coins has surplus `c - s`. Exactly `|c - s|` coins must cross the edge above it (out if
positive, in if negative), and that is achievable. A post-order walk returns `node.val - 1 + left + right`, adding `|left| + |right|` to
the move count.

* Time: **O(n)**.
* Space: **O(h)** — recursion depth.
''',
tc="n", sc="n",
java=r'''
public class DistributeCoins {

    private int moves;

    public int distributeCoins(TreeNode root) {
        moves = 0;
        surplus(root);
        return moves;
    }

    private int surplus(TreeNode node) {
        if (node == null) return 0;
        int l = surplus(node.left), r = surplus(node.right);
        moves += Math.abs(l) + Math.abs(r);
        return node.val - 1 + l + r;
    }
}
''',
helpers=["TreeNode"],
test=r'''
class DistributeCoinsTest {

    private final DistributeCoins solution = new DistributeCoins();

    @Test
    void examples() {
        assertEquals(2, solution.distributeCoins(TreeNode.of(3, 0, 0)));
        assertEquals(3, solution.distributeCoins(TreeNode.of(0, 3, 0)));
        assertEquals(2, solution.distributeCoins(TreeNode.of(1, 0, 2)));
        assertEquals(0, solution.distributeCoins(TreeNode.of(1)));
        assertEquals(4, solution.distributeCoins(TreeNode.of(1, 0, 0, null, 3)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {}; let moves = 0;
  A.step('Each subtree reports its surplus: coins minus nodes. That many coins must cross the edge above it.', A.tree('tree (coins)', root));
  (function go(n) {
    if (!n) return 0;
    const l = go(n.left), r = go(n.right); moves += Math.abs(l) + Math.abs(r);
    const s = n.val - 1 + l + r; hl[n.id] = s === 0 ? 'ok' : s > 0 ? 'cur' : 'bad';
    A.step(`Node with ${n.val} coin${n.val === 1 ? '' : 's'}: children report ${l} and ${r}, costing ${Math.abs(l) + Math.abs(r)} move${Math.abs(l) + Math.abs(r) === 1 ? '' : 's'}. Its subtree's surplus is ${s}${s > 0 ? ' (send up)' : s < 0 ? ' (needs coins from above)' : ''}.`, A.tree('tree (coins)', root, { hl }), A.vars({ moves }));
    return s;
  })(root);
  A.step(`Total moves: ${moves}.`, A.text('Result', moves, 'ok'));
}
A.scenario('Coins in a leaf', '[0,3,0]', () => run([0, 3, 0]));
A.scenario('Deeper', '[1,0,0,null,3]', () => run([1, 0, 0, null, 3]));
'''),

P(num=1020, slug="number-of-enclaves", title="Number of Enclaves", diff="Medium", topic="Graph DFS", cls="NumberOfEnclaves",
idea="Sink every land cell reachable from the border; whatever land is left cannot walk off the grid.",
vname="Flood fill from the border",
spec=r'''
In a grid of `0` (sea) and `1` (land), a move goes to a 4-adjacent land cell or off the grid edge. Return the number of land cells from
which you **cannot** walk off the grid.

**Example**
```
0 0 0 0
1 0 1 0
0 1 1 0      → 3
0 0 0 0
```

**Constraints**
* `1 <= m, n <= 500`
''',
approach=r'''
**Reverse the question.** A land cell can escape iff it is connected to a border land cell. Flood fill (iteratively, with a stack) from
every border land cell, marking cells as visited. Count the land cells that were never reached.

* Time: **O(mn)**.
* Space: **O(mn)** — the visited marks and stack.
''',
tc="n2", sc="n2",
java=r'''
public class NumberOfEnclaves {

    public int numEnclaves(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        boolean[][] seen = new boolean[m][n];
        Deque<int[]> stack = new ArrayDeque<>();
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                if ((r == 0 || c == 0 || r == m - 1 || c == n - 1) && grid[r][c] == 1) {
                    seen[r][c] = true;
                    stack.push(new int[]{r, c});
                }
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.isEmpty()) {
            int[] p = stack.pop();
            for (int[] d : dirs) {
                int r = p[0] + d[0], c = p[1] + d[1];
                if (r >= 0 && c >= 0 && r < m && c < n && grid[r][c] == 1 && !seen[r][c]) {
                    seen[r][c] = true;
                    stack.push(new int[]{r, c});
                }
            }
        }
        int count = 0;
        for (int r = 0; r < m; r++) for (int c = 0; c < n; c++) if (grid[r][c] == 1 && !seen[r][c]) count++;
        return count;
    }
}
''',
test=r'''
class NumberOfEnclavesTest {

    private final NumberOfEnclaves solution = new NumberOfEnclaves();

    @Test
    void examples() {
        assertEquals(3, solution.numEnclaves(new int[][]{{0, 0, 0, 0}, {1, 0, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}}));
        assertEquals(0, solution.numEnclaves(new int[][]{{0, 1, 1, 0}, {0, 0, 1, 0}, {0, 0, 1, 0}, {0, 0, 0, 0}}));
        assertEquals(0, solution.numEnclaves(new int[][]{{1}}));
        assertEquals(1, solution.numEnclaves(new int[][]{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}));
    }
}
''',
trace=r'''
function run(g) {
  const m = g.length, n = g[0].length, seen = new Set(), hl = {}, st = [];
  for (let r = 0; r < m; r++) for (let c = 0; c < n; c++) if ((r === 0 || c === 0 || r === m - 1 || c === n - 1) && g[r][c] === 1) { seen.add(`${r},${c}`); st.push([r, c]); hl[`${r},${c}`] = 'bad'; }
  A.step(`Land on the border can walk off directly: ${st.length} cell${st.length === 1 ? '' : 's'} (red).`, A.grid('grid', g, { hl }));
  while (st.length) {
    const [r, c] = st.pop(), added = [];
    [[1, 0], [-1, 0], [0, 1], [0, -1]].forEach(([dr, dc]) => { const a = r + dr, b = c + dc, k = `${a},${b}`; if (a >= 0 && b >= 0 && a < m && b < n && g[a][b] === 1 && !seen.has(k)) { seen.add(k); st.push([a, b]); hl[k] = 'bad'; added.push(k); } });
    if (added.length) A.step(`From (${r},${c}) the walk reaches ${added.map(k => `(${k})`).join(', ')}: they can escape too.`, A.grid('grid', g, { hl }));
  }
  let count = 0;
  for (let r = 0; r < m; r++) for (let c = 0; c < n; c++) if (g[r][c] === 1 && !seen.has(`${r},${c}`)) { count++; hl[`${r},${c}`] = 'ok'; }
  A.step(`Land never reached from the border (green) is trapped: ${count} cell${count === 1 ? '' : 's'}.`, A.grid('grid', g, { hl }));
  A.step(`Enclaves: ${count}.`, A.text('Result', count, 'ok'));
}
A.scenario('Example', '4 × 4', () => run([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]));
A.scenario('All escape', 'touches the edge', () => run([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]));
'''),

P(num=1091, slug="shortest-path-in-binary-matrix", title="Shortest Path in Binary Matrix", diff="Medium", topic="Graph BFS", cls="ShortestPathBinaryMatrix",
idea="BFS over the 8-connected open cells from the top-left; the first time it reaches the bottom-right is the shortest path.",
vname="8-direction BFS",
spec=r'''
In an `n × n` grid of `0` (open) and `1` (blocked), return the number of cells on the shortest path from the top-left to the
bottom-right moving in any of the 8 directions through open cells, or `-1`.

**Example**
```
[[0,1],[1,0]]                 → 2
[[0,0,0],[1,1,0],[1,1,0]]     → 4
[[1,0,0],[1,1,0],[1,1,0]]     → -1
```

**Constraints**
* `1 <= n <= 100`
''',
approach=r'''
**BFS.** Every move costs the same, so breadth-first search finds the shortest path. Start from `(0,0)` with length 1 (if it is open), mark
cells when they are queued, and explore all 8 neighbours. The length when `(n-1, n-1)` is dequeued is the answer.

* Time: **O(n²)** — each cell once, 8 neighbours.
* Space: **O(n²)** — the queue and marks.
''',
tc="n2", sc="n2",
java=r'''
public class ShortestPathBinaryMatrix {

    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;
        int[][] dist = new int[n][n];
        dist[0][0] = 1;
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{0, 0});
        while (!queue.isEmpty()) {
            int[] p = queue.poll();
            if (p[0] == n - 1 && p[1] == n - 1) return dist[p[0]][p[1]];
            for (int dr = -1; dr <= 1; dr++)
                for (int dc = -1; dc <= 1; dc++) {
                    int r = p[0] + dr, c = p[1] + dc;
                    if (r < 0 || c < 0 || r >= n || c >= n || grid[r][c] == 1 || dist[r][c] != 0) continue;
                    dist[r][c] = dist[p[0]][p[1]] + 1;
                    queue.add(new int[]{r, c});
                }
        }
        return -1;
    }
}
''',
test=r'''
class ShortestPathBinaryMatrixTest {

    private final ShortestPathBinaryMatrix solution = new ShortestPathBinaryMatrix();

    @Test
    void examples() {
        assertEquals(2, solution.shortestPathBinaryMatrix(new int[][]{{0, 1}, {1, 0}}));
        assertEquals(4, solution.shortestPathBinaryMatrix(new int[][]{{0, 0, 0}, {1, 1, 0}, {1, 1, 0}}));
        assertEquals(-1, solution.shortestPathBinaryMatrix(new int[][]{{1, 0, 0}, {1, 1, 0}, {1, 1, 0}}));
        assertEquals(1, solution.shortestPathBinaryMatrix(new int[][]{{0}}));
        assertEquals(-1, solution.shortestPathBinaryMatrix(new int[][]{{0, 1}, {1, 1}}));
    }
}
''',
trace=r'''
function run(g) {
  const n = g.length, dist = g.map(r => r.map(v => (v ? '■' : ''))), q = [[0, 0]];
  if (g[0][0] || g[n - 1][n - 1]) { A.step('A corner is blocked: no path.', A.grid('grid', g), A.text('Result', -1, 'bad')); return; }
  dist[0][0] = 1;
  A.step('BFS from the top-left. Each cell shows the path length when it is first reached (8 directions allowed).', A.grid('distance', dist, { hl: { '0,0': 'cur' } }));
  let level = 1;
  while (q.length) {
    const next = [];
    for (const [r, c] of q) for (let dr = -1; dr <= 1; dr++) for (let dc = -1; dc <= 1; dc++) { const a = r + dr, b = c + dc; if (a < 0 || b < 0 || a >= n || b >= n || g[a][b] || dist[a][b] !== '') continue; dist[a][b] = level + 1; next.push([a, b]); }
    if (dist[n - 1][n - 1] !== '' && typeof dist[n - 1][n - 1] === 'number') { A.step(`The bottom-right is reached with length ${dist[n - 1][n - 1]}.`, A.grid('distance', dist, { hl: { [`${n - 1},${n - 1}`]: 'ok' } }), A.text('Result', dist[n - 1][n - 1], 'ok')); return; }
    if (!next.length) break;
    level++;
    A.step(`Length ${level}: ${next.length} new cell${next.length === 1 ? '' : 's'}.`, A.grid('distance', dist, { hl: Object.fromEntries(next.map(([a, b]) => [`${a},${b}`, 'cur'])) }));
    q.length = 0; q.push(...next);
  }
  A.step('The search ran out of cells.', A.text('Result', -1, 'bad'));
}
A.scenario('Detour', '3 × 3', () => run([[0, 0, 0], [1, 1, 0], [1, 1, 0]]));
A.scenario('Diagonal', '4 × 4', () => run([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 0]]));
'''),

P(num=1162, slug="as-far-from-land-as-possible", title="As Far from Land as Possible", diff="Medium", topic="Graph BFS", cls="AsFarFromLand",
idea="Multi-source BFS from all land cells at once; the last water cell reached is the farthest.",
vname="Multi-source BFS",
spec=r'''
In an `n × n` grid of `0` (water) and `1` (land), find a water cell whose Manhattan distance to the nearest land is as large as possible,
and return that distance. Return `-1` if there is no land or no water.

**Example**
```
[[1,0,1],[0,0,0],[1,0,1]] → 2
[[1,0,0],[0,0,0],[0,0,0]] → 4
```

**Constraints**
* `1 <= n <= 100`
''',
approach=r'''
**All sources at once.** Put every land cell in the queue at distance 0 and BFS outward in 4 directions. On a grid without obstacles the
BFS distance equals the Manhattan distance to the nearest land. The number of BFS rounds needed to cover all water is the answer.

* Time: **O(n²)**.
* Space: **O(n²)**.
''',
tc="n2", sc="n2",
java=r'''
public class AsFarFromLand {

    public int maxDistance(int[][] grid) {
        int n = grid.length;
        int[][] dist = new int[n][n];
        Deque<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) queue.add(new int[]{r, c});
                else dist[r][c] = -1;
            }
        if (queue.isEmpty() || queue.size() == n * n) return -1;
        int best = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] p = queue.poll();
            for (int[] d : dirs) {
                int r = p[0] + d[0], c = p[1] + d[1];
                if (r < 0 || c < 0 || r >= n || c >= n || dist[r][c] != -1) continue;
                dist[r][c] = dist[p[0]][p[1]] + 1;
                best = Math.max(best, dist[r][c]);
                queue.add(new int[]{r, c});
            }
        }
        return best;
    }
}
''',
test=r'''
class AsFarFromLandTest {

    private final AsFarFromLand solution = new AsFarFromLand();

    @Test
    void examples() {
        assertEquals(2, solution.maxDistance(new int[][]{{1, 0, 1}, {0, 0, 0}, {1, 0, 1}}));
        assertEquals(4, solution.maxDistance(new int[][]{{1, 0, 0}, {0, 0, 0}, {0, 0, 0}}));
        assertEquals(-1, solution.maxDistance(new int[][]{{1, 1}, {1, 1}}));
        assertEquals(-1, solution.maxDistance(new int[][]{{0, 0}, {0, 0}}));
    }
}
''',
trace=r'''
function run(g) {
  const n = g.length, d = g.map(r => r.map(v => (v ? 0 : ''))); let q = [];
  g.forEach((row, r) => row.forEach((v, c) => v && q.push([r, c])));
  A.step(`Start from all ${q.length} land cells at once (distance 0).`, A.grid('distance to land', d, { hl: Object.fromEntries(q.map(([r, c]) => [`${r},${c}`, 'ok'])) }));
  let level = 0;
  while (true) {
    const next = [];
    q.forEach(([r, c]) => [[1, 0], [-1, 0], [0, 1], [0, -1]].forEach(([dr, dc]) => { const a = r + dr, b = c + dc; if (a >= 0 && b >= 0 && a < n && b < n && d[a][b] === '') { d[a][b] = level + 1; next.push([a, b]); } }));
    if (!next.length) break;
    level++; q = next;
    A.step(`Round ${level}: ${next.length} water cell${next.length === 1 ? '' : 's'} are ${level} step${level === 1 ? '' : 's'} from the nearest land.`, A.grid('distance to land', d, { hl: Object.fromEntries(next.map(([a, b]) => [`${a},${b}`, 'cur'])) }));
  }
  A.step(`The last water cells were reached in round ${level}.`, A.text('Result', level || -1, 'ok'));
}
A.scenario('Four islands', '[[1,0,1],[0,0,0],[1,0,1]]', () => run([[1, 0, 1], [0, 0, 0], [1, 0, 1]]));
A.scenario('One corner', '[[1,0,0],[0,0,0],[0,0,0]]', () => run([[1, 0, 0], [0, 0, 0], [0, 0, 0]]));
'''),

P(num=1219, slug="path-with-maximum-gold", title="Path with Maximum Gold", diff="Medium", topic="Backtracking", cls="PathWithMaximumGold",
idea="Start a backtracking walk from every gold cell, temporarily emptying cells on the current path.",
vname="Backtracking from every cell",
spec=r'''
Each grid cell holds some gold (0 means empty). You may start and stop at any cell with gold, move up/down/left/right, never visit a
cell twice and never enter an empty cell. Return the most gold you can collect.

**Example**
```
[[0,6,0],[5,8,7],[0,9,0]] → 24   (9 → 8 → 7)
[[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]] → 28
```

**Constraints**
* `1 <= m, n <= 15`, at most 25 cells contain gold
''',
approach=r'''
**DFS with undo.** From a cell, take its gold, set it to 0 so the path cannot reuse it, try the four neighbours, then restore it. Run this
from every gold cell and keep the best total.

* Time: **O(k · 3ᵏ)** — `k <= 25` gold cells; after the first move each step has at most 3 new directions.
* Space: **O(k)** — recursion depth.
''',
tc="exp", sc="n",
java=r'''
public class PathWithMaximumGold {

    public int getMaximumGold(int[][] grid) {
        int best = 0;
        for (int r = 0; r < grid.length; r++)
            for (int c = 0; c < grid[0].length; c++)
                if (grid[r][c] > 0) best = Math.max(best, dfs(grid, r, c));
        return best;
    }

    private int dfs(int[][] g, int r, int c) {
        if (r < 0 || c < 0 || r >= g.length || c >= g[0].length || g[r][c] == 0) return 0;
        int gold = g[r][c];
        g[r][c] = 0;
        int more = Math.max(Math.max(dfs(g, r + 1, c), dfs(g, r - 1, c)), Math.max(dfs(g, r, c + 1), dfs(g, r, c - 1)));
        g[r][c] = gold;
        return gold + more;
    }
}
''',
test=r'''
class PathWithMaximumGoldTest {

    private final PathWithMaximumGold solution = new PathWithMaximumGold();

    @Test
    void examples() {
        assertEquals(24, solution.getMaximumGold(new int[][]{{0, 6, 0}, {5, 8, 7}, {0, 9, 0}}));
        assertEquals(28, solution.getMaximumGold(new int[][]{{1, 0, 7}, {2, 0, 6}, {3, 4, 5}, {0, 3, 0}, {9, 0, 20}}));
        assertEquals(0, solution.getMaximumGold(new int[][]{{0}}));
    }

    @Test
    void gridIsRestored() {
        int[][] g = {{0, 6, 0}, {5, 8, 7}, {0, 9, 0}};
        solution.getMaximumGold(g);
        assertArrayEquals(new int[][]{{0, 6, 0}, {5, 8, 7}, {0, 9, 0}}, g);
    }
}
''',
trace=r'''
function run(g) {
  const m = g.length, n = g[0].length; let best = 0, bestPath = [];
  A.step('Try every gold cell as a start. A path may not revisit cells or step on empty ones.', A.grid('gold', g));
  for (let r = 0; r < m; r++) for (let c = 0; c < n; c++) {
    if (!g[r][c]) continue;
    let local = 0, localPath = [];
    (function dfs(a, b, sum, path) {
      if (a < 0 || b < 0 || a >= m || b >= n || !g[a][b] || path.some(([x, y]) => x === a && y === b)) return;
      const p = [...path, [a, b]], s = sum + g[a][b];
      if (s > local) { local = s; localPath = p; }
      [[1, 0], [-1, 0], [0, 1], [0, -1]].forEach(([dr, dc]) => dfs(a + dr, b + dc, s, p));
    })(r, c, 0, []);
    const better = local > best; if (better) { best = local; bestPath = localPath; }
    A.step(`Starting at (${r},${c}): the best path collects ${local}${better ? ', the best so far' : ''}.`, A.grid('gold', g, { hl: Object.fromEntries(localPath.map(([a, b], i) => [`${a},${b}`, i === 0 ? 'cur' : better ? 'ok' : 'alt'])) }), A.vars({ best }));
  }
  A.step(`Most gold: ${best} along ${bestPath.map(([a, b]) => g[a][b]).join(' → ')}.`, A.grid('gold', g, { hl: Object.fromEntries(bestPath.map(([a, b]) => [`${a},${b}`, 'ok'])) }), A.text('Result', best, 'ok'));
}
A.scenario('Example', '[[0,6,0],[5,8,7],[0,9,0]]', () => run([[0, 6, 0], [5, 8, 7], [0, 9, 0]]));
'''),

P(num=1254, slug="number-of-closed-islands", title="Number of Closed Islands", diff="Medium", topic="Graph DFS", cls="NumberOfClosedIslands",
idea="Remove islands that touch the border, then count the islands that remain.",
vname="Sink border islands, then count",
spec=r'''
In this grid **`0` is land** and `1` is water. An island is a 4-connected group of `0`s; it is **closed** if it is completely surrounded
by water (it does not touch the grid border). Return the number of closed islands.

**Example**
```
1 1 1 1 1 1 1 0
1 0 0 0 0 1 1 0
1 0 1 0 1 1 1 0      → 2
1 0 0 0 0 1 0 1
1 1 1 1 1 1 1 0
```

**Constraints**
* `1 <= rows, cols <= 100`
''',
approach=r'''
**Two flood fills.** First sink (turn into water) every island reachable from a border land cell; those are not closed. Then every
remaining island is closed: count them, sinking each as it is found. Work on a copy so the input is untouched.

* Time: **O(mn)**.
* Space: **O(mn)** — the copy and the fill stack.
''',
tc="n2", sc="n2",
java=r'''
public class NumberOfClosedIslands {

    public int closedIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] g = new int[m][];
        for (int r = 0; r < m; r++) g[r] = grid[r].clone();
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                if ((r == 0 || c == 0 || r == m - 1 || c == n - 1) && g[r][c] == 0) sink(g, r, c);
        int count = 0;
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                if (g[r][c] == 0) {
                    count++;
                    sink(g, r, c);
                }
        return count;
    }

    private void sink(int[][] g, int r0, int c0) {
        Deque<int[]> stack = new ArrayDeque<>();
        g[r0][c0] = 1;
        stack.push(new int[]{r0, c0});
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.isEmpty()) {
            int[] p = stack.pop();
            for (int[] d : dirs) {
                int r = p[0] + d[0], c = p[1] + d[1];
                if (r >= 0 && c >= 0 && r < g.length && c < g[0].length && g[r][c] == 0) {
                    g[r][c] = 1;
                    stack.push(new int[]{r, c});
                }
            }
        }
    }
}
''',
test=r'''
class NumberOfClosedIslandsTest {

    private final NumberOfClosedIslands solution = new NumberOfClosedIslands();

    @Test
    void examples() {
        assertEquals(2, solution.closedIsland(new int[][]{{1, 1, 1, 1, 1, 1, 1, 0}, {1, 0, 0, 0, 0, 1, 1, 0}, {1, 0, 1, 0, 1, 1, 1, 0}, {1, 0, 0, 0, 0, 1, 0, 1}, {1, 1, 1, 1, 1, 1, 1, 0}}));
        assertEquals(1, solution.closedIsland(new int[][]{{0, 0, 1, 0, 0}, {0, 1, 0, 1, 0}, {0, 1, 1, 1, 0}}));
        assertEquals(2, solution.closedIsland(new int[][]{{1, 1, 1, 1, 1, 1, 1}, {1, 0, 0, 0, 0, 0, 1}, {1, 0, 1, 1, 1, 0, 1}, {1, 0, 1, 0, 1, 0, 1}, {1, 0, 1, 1, 1, 0, 1}, {1, 0, 0, 0, 0, 0, 1}, {1, 1, 1, 1, 1, 1, 1}}));
    }
}
''',
trace=r'''
function run(grid) {
  const g = grid.map(r => r.slice()), m = g.length, n = g[0].length, hl = {};
  const fill = (r0, c0, cls) => { const st = [[r0, c0]], cells = []; g[r0][c0] = 1; while (st.length) { const [r, c] = st.pop(); cells.push([r, c]); hl[`${r},${c}`] = cls; [[1, 0], [-1, 0], [0, 1], [0, -1]].forEach(([dr, dc]) => { const a = r + dr, b = c + dc; if (a >= 0 && b >= 0 && a < m && b < n && g[a][b] === 0) { g[a][b] = 1; st.push([a, b]); } }); } return cells; };
  A.step('Here 0 is land. Islands touching the border are not closed, so remove them first.', A.grid('grid', grid));
  for (let r = 0; r < m; r++) for (let c = 0; c < n; c++) if ((r === 0 || c === 0 || r === m - 1 || c === n - 1) && g[r][c] === 0) { const cells = fill(r, c, 'bad'); A.step(`The island at (${r},${c}) touches the border (${cells.length} cell${cells.length === 1 ? '' : 's'}): not closed.`, A.grid('grid', grid, { hl })); }
  let count = 0;
  for (let r = 0; r < m; r++) for (let c = 0; c < n; c++) if (g[r][c] === 0) { count++; const cells = fill(r, c, 'ok'); A.step(`Island #${count} at (${r},${c}) is surrounded by water: closed (${cells.length} cell${cells.length === 1 ? '' : 's'}).`, A.grid('grid', grid, { hl })); }
  A.step(`Closed islands: ${count}.`, A.text('Result', count, 'ok'));
}
A.scenario('Example', '5 × 8', () => run([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]));
'''),

P(num=1283, slug="find-the-smallest-divisor-given-a-threshold", title="Find the Smallest Divisor Given a Threshold", diff="Medium", topic="Binary Search", cls="SmallestDivisor",
idea="The rounded-up quotient sum only shrinks as the divisor grows, so binary search for the first divisor that fits.",
vname="Binary search on the divisor",
spec=r'''
Choose a positive integer divisor, divide every element of `nums` by it rounding **up**, and add the results. Return the smallest divisor
for which this sum is at most `threshold`.

**Example**
```
nums = [1,2,5,9], threshold = 6 → 5   (1 + 1 + 1 + 2 = 5)
nums = [44,22,33,11,1], threshold = 5 → 44
```

**Constraints**
* `1 <= nums.length <= 5 * 10^4 <= threshold <= 10^6`, `1 <= nums[i] <= 10^6`
''',
approach=r'''
**Monotone check.** A larger divisor never increases any `ceil(x / d)`, so the sum is non-increasing in `d`. Binary search `d` in
`1..max(nums)` (at `max`, every term is 1 and the sum is `n <= threshold`). `ceil(x / d)` is `(x + d - 1) / d`.

* Time: **O(n log M)** — `M = max(nums)`.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class SmallestDivisor {

    public int smallestDivisor(int[] nums, int threshold) {
        int lo = 1, hi = 1;
        for (int v : nums) hi = Math.max(hi, v);
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            long sum = 0;
            for (int v : nums) sum += (v + mid - 1) / mid;
            if (sum <= threshold) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
''',
test=r'''
class SmallestDivisorTest {

    private final SmallestDivisor solution = new SmallestDivisor();

    @Test
    void examples() {
        assertEquals(5, solution.smallestDivisor(new int[]{1, 2, 5, 9}, 6));
        assertEquals(44, solution.smallestDivisor(new int[]{44, 22, 33, 11, 1}, 5));
        assertEquals(1, solution.smallestDivisor(new int[]{21212, 10101, 12121}, 1_000_000));
        assertEquals(3, solution.smallestDivisor(new int[]{2, 3, 5, 7, 11}, 11));
        assertEquals(1_000_000, solution.smallestDivisor(new int[]{1_000_000}, 1));
    }
}
''',
trace=r'''
function run(nums, t) {
  let lo = 1, hi = Math.max(...nums);
  A.step(`Search the divisor between ${lo} and ${hi}. Bigger divisors give smaller sums.`, A.arr('nums', nums), A.vars({ threshold: t, lo, hi }));
  while (lo < hi) {
    const mid = lo + Math.floor((hi - lo) / 2), parts = nums.map(v => Math.ceil(v / mid)), s = parts.reduce((a, b) => a + b, 0);
    A.step(`d = ${mid}: ${parts.join(' + ')} = ${s}, ${s <= t ? `within ${t}. Try smaller.` : `over ${t}. Go bigger.`}`, A.arr('ceil(x / d)', parts, { hl: Object.fromEntries(parts.map((_, i) => [i, s <= t ? 'ok' : 'bad'])) }), A.vars({ lo, hi, d: mid, sum: s }));
    if (s <= t) hi = mid; else lo = mid + 1;
  }
  A.step(`Smallest divisor: ${lo}.`, A.text('Result', lo, 'ok'));
}
A.scenario('Example', '[1,2,5,9], threshold 6', () => run([1, 2, 5, 9], 6));
'''),

P(num=1291, slug="sequential-digits", title="Sequential Digits", diff="Medium", topic="Enumeration", cls="SequentialDigits",
idea="There are only 36 numbers with consecutive increasing digits; generate them in order and keep those in range.",
vname="Enumerate by length and start",
spec=r'''
A number has **sequential digits** if each digit is one more than the previous (like `1234`). Return all such numbers in `[low, high]`,
sorted.

**Example**
```
low = 100,  high = 300   → [123,234]
low = 1000, high = 13000 → [1234,2345,3456,4567,5678,6789,12345]
```

**Constraints**
* `10 <= low <= high <= 10^9`
''',
approach=r'''
**Enumerate.** Such a number is fixed by its length `L` (2..9) and first digit `s` (1..10-L). Loop over lengths, then starts; within a length
the numbers increase with the start, and longer numbers are bigger, so they come out sorted. Each is a substring of `"123456789"`.

* Time: **O(1)** — 36 candidates.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class SequentialDigits {

    public List<Integer> sequentialDigits(int low, int high) {
        String digits = "123456789";
        List<Integer> out = new ArrayList<>();
        for (int len = 2; len <= 9; len++)
            for (int start = 0; start + len <= 9; start++) {
                int v = Integer.parseInt(digits.substring(start, start + len));
                if (v >= low && v <= high) out.add(v);
            }
        return out;
    }
}
''',
test=r'''
class SequentialDigitsTest {

    private final SequentialDigits solution = new SequentialDigits();

    @Test
    void examples() {
        assertEquals(List.of(123, 234), solution.sequentialDigits(100, 300));
        assertEquals(List.of(1234, 2345, 3456, 4567, 5678, 6789, 12345), solution.sequentialDigits(1000, 13000));
        assertEquals(36, solution.sequentialDigits(10, 1_000_000_000).size());
        assertEquals(List.of(), solution.sequentialDigits(58, 66));
    }
}
''',
trace=r'''
function run(low, high) {
  const digits = '123456789', out = [];
  A.step(`Every answer is a slice of "123456789". Try every length, then every start, keeping slices in [${low}, ${high}].`, A.chars('digits', digits));
  for (let len = 2; len <= 9; len++) {
    const cands = []; for (let s = 0; s + len <= 9; s++) cands.push(+digits.slice(s, s + len));
    const keep = cands.filter(v => v >= low && v <= high);
    if (cands[cands.length - 1] < low) continue;
    out.push(...keep);
    A.step(`Length ${len}: ${cands.join(', ')}. Keep ${keep.length ? keep.join(', ') : 'none'}.`, A.arr(`length ${len}`, cands, { hl: Object.fromEntries(cands.map((v, i) => [i, v >= low && v <= high ? 'ok' : 'dim'])) }), A.arr('result', out));
    if (cands[0] > high) break;
  }
  A.step(`${out.length} number${out.length === 1 ? '' : 's'}, already sorted.`, A.arr('result', out));
}
A.scenario('Example', '1000..13000', () => run(1000, 13000));
A.scenario('Three digits', '100..300', () => run(100, 300));
'''),
]
