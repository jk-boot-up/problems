PROBLEMS = [
P(num=841, slug="keys-and-rooms", title="Keys and Rooms", diff="Medium", topic="Graph General", cls="KeysAndRooms",
idea="Rooms are nodes and keys are edges; DFS from room 0 and check that every room was reached.",
vname="DFS from room 0",
spec=r'''
There are `n` locked rooms except room 0. `rooms[i]` lists the keys found in room `i`. Return `true` if you can visit every room.

**Example**
```
[[1],[2],[3],[]]        → true
[[1,3],[3,0,1],[2],[0]] → false
```

**Constraints**
* `2 <= n <= 1000`
''',
approach=r'''
**Graph reachability.** DFS with a stack from room 0, marking rooms as visited; count visits.

* Time: **O(n + k)** — k is the total number of keys.
* Space: **O(n)** — visited flags and the stack.
''',
java=r'''
public class KeysAndRooms {

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] seen = new boolean[rooms.size()];
        Deque<Integer> stack = new ArrayDeque<>(List.of(0));
        seen[0] = true;
        int visited = 1;
        while (!stack.isEmpty()) {
            for (int key : rooms.get(stack.pop())) {
                if (!seen[key]) {
                    seen[key] = true;
                    visited++;
                    stack.push(key);
                }
            }
        }
        return visited == rooms.size();
    }
}
''',
test=r'''
class KeysAndRoomsTest {

    private final KeysAndRooms solution = new KeysAndRooms();

    @Test
    void examples() {
        assertTrue(solution.canVisitAllRooms(List.of(List.of(1), List.of(2), List.of(3), List.of())));
        assertFalse(solution.canVisitAllRooms(List.of(List.of(1, 3), List.of(3, 0, 1), List.of(2), List.of(0))));
    }
}
''',
trace=r'''
function run(rooms) {
  const nodes = rooms.map((_, i) => ({ id: i, label: i })), edges = rooms.flatMap((ks, i) => ks.map(k => [i, k]));
  const seen = new Set([0]), st = [0];
  A.step('Each room is a node; each key is an arrow to the room it opens. Start in room 0.', A.graph('rooms', nodes, edges, { directed: true, hl: { 0: 'cur' } }));
  while (st.length) {
    const r = st.pop(), found = [];
    for (const k of rooms[r]) if (!seen.has(k)) { seen.add(k); st.push(k); found.push(k); }
    A.step(`Room ${r} has keys ${rooms[r].length ? rooms[r].join(', ') : 'none'}.${found.length ? ` New rooms opened: ${found.join(', ')}.` : ''}`, A.graph('rooms', nodes, edges, { directed: true, hl: Object.fromEntries([...seen].map(x => [x, x === r ? 'cur' : 'ok'])) }), A.stack('to explore', st));
  }
  const ok = seen.size === rooms.length;
  A.step(ok ? 'Every room was reached.' : `Room${rooms.length - seen.size > 1 ? 's' : ''} ${rooms.map((_, i) => i).filter(i => !seen.has(i)).join(', ')} stay locked.`, A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('All reachable', 'rooms = [[1],[2],[3],[]]', () => run([[1], [2], [3], []]));
A.scenario('One locked', 'rooms = [[1,3],[3,0,1],[2],[0]]', () => run([[1, 3], [3, 0, 1], [2], [0]]));
'''),

P(num=547, slug="number-of-provinces", title="Number of Provinces", diff="Medium", topic="Graph General", cls="NumberOfProvinces",
idea="Count connected components with union-find: every successful union merges two provinces.",
vname="Union-find",
spec=r'''
`isConnected[i][j] = 1` means cities `i` and `j` are directly connected. A province is a group of directly or indirectly connected cities.
Return the number of provinces.

**Example**
```
[[1,1,0],[1,1,0],[0,0,1]] → 2,   [[1,0,0],[0,1,0],[0,0,1]] → 3
```

**Constraints**
* `1 <= n <= 200`
''',
approach=r'''
**Disjoint sets.** Start with `n` provinces; for each connected pair `(i, j)` with `j > i`, a union of two different roots reduces the count.

* Time: **O(n²·α(n))** — every matrix cell is examined.
* Space: **O(n)** — the parent array.
''',
tc="n2", sc="n",
java=r'''
public class NumberOfProvinces {

    private int[] parent;

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length, provinces = n;
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    int a = find(i), b = find(j);
                    if (a != b) {
                        parent[a] = b;
                        provinces--;
                    }
                }
            }
        }
        return provinces;
    }
}
''',
test=r'''
class NumberOfProvincesTest {

    private final NumberOfProvinces solution = new NumberOfProvinces();

    @Test
    void examples() {
        assertEquals(2, solution.findCircleNum(new int[][]{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}}));
        assertEquals(3, solution.findCircleNum(new int[][]{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}));
    }
}
''',
trace=r'''
function run(m) {
  const n = m.length, par = [...Array(n).keys()], find = x => (par[x] === x ? x : (par[x] = find(par[x])));
  const nodes = [...Array(n)].map((_, i) => ({ id: i, label: i })), edges = [];
  for (let i = 0; i < n; i++) for (let j = i + 1; j < n; j++) if (m[i][j]) edges.push([i, j]);
  let count = n; const hues = ['ok', 'sel', 'alt', 'cur'];
  const color = () => { const roots = [...new Set(nodes.map(x => find(x.id)))]; return Object.fromEntries(nodes.map(x => [x.id, hues[roots.indexOf(find(x.id)) % 4]])); };
  A.step(`Start with ${n} provinces, one per city.`, A.graph('cities', nodes, edges, { hl: color() }), A.vars({ provinces: count }));
  for (const [i, j] of edges) { const a = find(i), b = find(j); if (a !== b) { par[a] = b; count--; } A.step(a !== b ? `Cities ${i} and ${j} are connected: merge their provinces. ${count} left.` : `Cities ${i} and ${j} are already in the same province.`, A.graph('cities', nodes, edges.map(e => [...e, '', e[0] === i && e[1] === j ? 'cur' : '']), { hl: color() }), A.vars({ provinces: count })); }
  A.step(`${count} provinces.`, A.text('Result', count, 'ok'));
}
A.scenario('Two provinces', '[[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]', () => run([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]));
'''),

P(num=1466, slug="reorder-routes-to-make-all-paths-lead-to-the-city-zero", title="Reorder Routes to Make All Paths Lead to the City Zero", diff="Medium", topic="Graph General", cls="ReorderRoutes",
idea="Walk outward from city 0 ignoring direction; every road that points away from 0 must be flipped.",
vname="DFS from city 0 counting outward roads",
spec=r'''
`n` cities form a tree of `n - 1` one-way roads `connections[i] = [a, b]` (from `a` to `b`). Return the minimum number of roads to reverse
so that every city can reach city 0.

**Example**
```
n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]] → 3
n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]       → 2
```

**Constraints**
* `2 <= n <= 5 * 10^4`
''',
approach=r'''
**Signed adjacency.** Store each road in both directions, tagged `1` if it is an original road (pointing away from the walk) and `0` if it is
the reverse. DFS from 0: whenever we cross an original road outward, it points away from 0 and must be flipped.

* Time: **O(n)** — each road is seen twice.
* Space: **O(n)** — the adjacency lists.
''',
java=r'''
public class ReorderRoutes {

    public int minReorder(int n, int[][] connections) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] c : connections) {
            adj.get(c[0]).add(new int[]{c[1], 1}); // original direction: away from c[0]
            adj.get(c[1]).add(new int[]{c[0], 0});
        }
        boolean[] seen = new boolean[n];
        Deque<Integer> stack = new ArrayDeque<>(List.of(0));
        seen[0] = true;
        int flips = 0;
        while (!stack.isEmpty()) {
            int u = stack.pop();
            for (int[] e : adj.get(u)) {
                if (!seen[e[0]]) {
                    seen[e[0]] = true;
                    flips += e[1];
                    stack.push(e[0]);
                }
            }
        }
        return flips;
    }
}
''',
test=r'''
class ReorderRoutesTest {

    private final ReorderRoutes solution = new ReorderRoutes();

    @Test
    void examples() {
        assertEquals(3, solution.minReorder(6, new int[][]{{0, 1}, {1, 3}, {2, 3}, {4, 0}, {4, 5}}));
        assertEquals(2, solution.minReorder(5, new int[][]{{1, 0}, {1, 2}, {3, 2}, {3, 4}}));
        assertEquals(0, solution.minReorder(3, new int[][]{{1, 0}, {2, 0}}));
    }
}
''',
trace=r'''
function run(n, con) {
  const nodes = [...Array(n)].map((_, i) => ({ id: i, label: i })), seen = new Set([0]), st = [0], flipped = []; let flips = 0;
  A.step('Walk outward from city 0, ignoring direction. A road pointing away from 0 along our walk must be reversed.', A.graph('roads', nodes, con.map(([a, b]) => [a, b]), { directed: true, hl: { 0: 'cur' } }));
  while (st.length) {
    const u = st.pop();
    for (const [a, b] of con) {
      if (a === u && !seen.has(b)) { seen.add(b); st.push(b); flips++; flipped.push([a, b]); A.step(`Road ${a} → ${b} points away from 0: reverse it. Flips: ${flips}.`, A.graph('roads', nodes, con.map(([x, y]) => (flipped.some(f => f[0] === x && f[1] === y) ? [y, x, '', 'ok'] : [x, y])), { directed: true, hl: Object.fromEntries([...seen].map(x => [x, x === b ? 'cur' : 'sel'])) })); }
      else if (b === u && !seen.has(a)) { seen.add(a); st.push(a); A.step(`Road ${a} → ${b} already points toward 0.`, A.graph('roads', nodes, con.map(([x, y]) => (flipped.some(f => f[0] === x && f[1] === y) ? [y, x, '', 'ok'] : [x, y])), { directed: true, hl: Object.fromEntries([...seen].map(x => [x, x === a ? 'cur' : 'sel'])) })); }
    }
  }
  A.step(`${flips} roads reversed; every city now reaches 0.`, A.text('Result', flips, 'ok'));
}
A.scenario('Six cities', 'connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]', () => run(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]));
'''),

P(num=1926, slug="nearest-exit-from-entrance-in-maze", title="Nearest Exit from Entrance in Maze", diff="Medium", topic="Graph BFS", cls="NearestExit",
idea="BFS from the entrance; the first empty border cell reached (other than the entrance) is the nearest exit.",
vname="BFS from the entrance",
spec=r'''
In a maze of `'.'` (empty) and `'+'` (wall), starting at `entrance`, return the number of steps to the nearest **exit**: an empty cell on the
border that is not the entrance. Return `-1` if none is reachable.

**Example**
```
maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2] → 1
maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]             → 2
```

**Constraints**
* `1 <= m, n <= 100`
''',
approach=r'''
**Level-order BFS.** Mark cells as visited when enqueued. Each level is one step; the first border cell dequeued (excluding the start)
is the answer.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the queue and marks.
''',
tc="n2", sc="n2",
java=r'''
public class NearestExit {

    public int nearestExit(char[][] maze, int[] entrance) {
        int m = maze.length, n = maze[0].length;
        boolean[][] seen = new boolean[m][n];
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(entrance);
        seen[entrance[0]][entrance[1]] = true;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int steps = 0; !queue.isEmpty(); steps++) {
            for (int size = queue.size(); size > 0; size--) {
                int[] c = queue.poll();
                boolean border = c[0] == 0 || c[1] == 0 || c[0] == m - 1 || c[1] == n - 1;
                if (border && steps > 0) return steps;
                for (int[] d : dirs) {
                    int r = c[0] + d[0], k = c[1] + d[1];
                    if (r >= 0 && r < m && k >= 0 && k < n && maze[r][k] == '.' && !seen[r][k]) {
                        seen[r][k] = true;
                        queue.add(new int[]{r, k});
                    }
                }
            }
        }
        return -1;
    }
}
''',
test=r'''
class NearestExitTest {

    private final NearestExit solution = new NearestExit();

    private static char[][] m(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    @Test
    void examples() {
        assertEquals(1, solution.nearestExit(m("++.+", "...+", "+++."), new int[]{1, 2}));
        assertEquals(2, solution.nearestExit(m("+++", "...", "+++"), new int[]{1, 0}));
        assertEquals(-1, solution.nearestExit(m(".+"), new int[]{0, 0}));
    }
}
''',
trace=r'''
function run(rows, ent) {
  const g = rows.map(r => [...r]), m = g.length, n = g[0].length, seen = new Set([ent.join()]); let q = [ent];
  const view = (msg, extra = {}) => A.step(msg, A.grid('maze', g.map(r => r.map(c => (c === '+' ? '' : ''))), { hl: { ...Object.fromEntries(g.flatMap((r, i) => r.map((c, j) => [`${i},${j}`, c === '+' ? 'bar' : seen.has(`${i},${j}`) ? 'sel' : '']))), [`${ent[0]},${ent[1]}`]: 'alt', ...extra } }));
  view('Grey cells are walls; purple is the entrance. Search outward one step at a time.');
  for (let s = 0; q.length; s++) {
    const exit = q.find(([r, c]) => s > 0 && (r === 0 || c === 0 || r === m - 1 || c === n - 1));
    if (exit) { view(`After ${s} step${s > 1 ? 's' : ''}, (${exit}) is on the border: the nearest exit.`, { [`${exit[0]},${exit[1]}`]: 'ok' }); A.step('Done.', A.text('Result', s, 'ok')); return; }
    const nq = [];
    for (const [r, c] of q) for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const a = r + dr, b = c + dc, k = `${a},${b}`; if (a >= 0 && a < m && b >= 0 && b < n && g[a][b] === '.' && !seen.has(k)) { seen.add(k); nq.push([a, b]); } }
    q = nq;
    view(`Step ${s + 1}: the frontier reaches ${nq.length} new cell${nq.length === 1 ? '' : 's'}.`, Object.fromEntries(nq.map(([a, b]) => [`${a},${b}`, 'cur'])));
  }
  A.step('No exit is reachable.', A.text('Result', -1, 'bad'));
}
A.scenario('Corridor', 'maze = ["+++","...","+++"], entrance = [1,0]', () => run(['+++', '...', '+++'], [1, 0]));
'''),

P(num=2336, slug="smallest-number-in-infinite-set", title="Smallest Number in Infinite Set", diff="Medium", topic="Heap", cls="SmallestInfiniteSet",
idea="Numbers from 'next' upward are implicitly present; returned numbers below 'next' live in a min-heap (with a set to avoid duplicates).",
vname="Counter + min-heap of returned numbers",
spec=r'''
The set initially contains every positive integer. Implement:
* `popSmallest()`: remove and return the smallest number;
* `addBack(num)`: put `num` back if it is not already in the set.

**Example**
```
addBack(2); popSmallest() → 1; popSmallest() → 2; popSmallest() → 3;
addBack(1); popSmallest() → 1; popSmallest() → 4; popSmallest() → 5
```

**Constraints**
* `1 <= num <= 1000`; at most 1000 calls.
''',
approach=r'''
**Two parts.** `next` is the smallest number never popped; everything from `next` upward is present. Numbers added back below `next` go into a
min-heap, with a `MyHashSet` to prevent duplicates. `popSmallest` takes from the heap if it is not empty, otherwise returns `next++`.

* Time: **O(log n)** — per operation.
* Space: **O(n)** — the heap and set.
''',
tc="log", sc="n",
java=r'''
public class SmallestInfiniteSet {

    private int next = 1;
    private final PriorityQueue<Integer> returned = new PriorityQueue<>();
    private final MyHashSet<Integer> inHeap = new MyHashSet<>();

    public int popSmallest() {
        if (!returned.isEmpty()) {
            int x = returned.poll();
            inHeap.remove(x);
            return x;
        }
        return next++;
    }

    public void addBack(int num) {
        if (num < next && inHeap.add(num)) returned.add(num);
    }
}
''',
test=r'''
class SmallestInfiniteSetTest {

    @Test
    void example() {
        SmallestInfiniteSet s = new SmallestInfiniteSet();
        s.addBack(2);
        assertEquals(1, s.popSmallest());
        assertEquals(2, s.popSmallest());
        assertEquals(3, s.popSmallest());
        s.addBack(1);
        s.addBack(1);
        assertEquals(1, s.popSmallest());
        assertEquals(4, s.popSmallest());
        assertEquals(5, s.popSmallest());
    }
}
''',
trace=r'''
A.scenario('LeetCode example', 'addBack 2 · pop ×3 · addBack 1 · pop ×3', () => {
  let next = 1; const heap = [];
  const view = msg => A.step(msg, A.vars({ next }), A.arr('returned numbers (min-heap)', heap.slice().sort((a, b) => a - b)));
  const pop = () => { let x; if (heap.length) { heap.sort((a, b) => a - b); x = heap.shift(); view(`popSmallest() → ${x}, taken from the returned numbers.`); } else { x = next++; view(`popSmallest() → ${x}, the counter; it advances to ${next}.`); } };
  const add = x => { if (x < next && !heap.includes(x)) { heap.push(x); view(`addBack(${x}): ${x} was popped before, so put it in the heap.`); } else view(`addBack(${x}): ${x} is already in the set; nothing changes.`); };
  view('Every number from next upward is in the set. Numbers given back below next go into a min-heap.');
  add(2); pop(); pop(); pop(); add(1); add(1); pop(); pop(); pop();
});
'''),

P(num=2542, slug="maximum-subsequence-score", title="Maximum Subsequence Score", diff="Medium", topic="Heap", cls="MaximumSubsequenceScore",
idea="Fix the minimum of nums2 by sorting it in descending order; keep the k largest nums1 values seen so far in a min-heap.",
vname="Sort by nums2 + min-heap of nums1",
spec=r'''
Choose `k` indices. The score is `(sum of chosen nums1) × (minimum of chosen nums2)`. Return the maximum score.

**Example**
```
nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3 → 12
nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1 → 30
```

**Constraints**
* `1 <= k <= n <= 10^5`
''',
approach=r'''
**Enumerate the minimum.** Sort index pairs by `nums2` descending. When we reach pair `i`, its `nums2` is the smallest so far, so it can be
the minimum; pair it with the `k - 1` largest `nums1` values from earlier pairs, maintained in a min-heap with a running sum (in a `long`).

* Time: **O(n log n)** — sorting plus heap operations.
* Space: **O(n)** — the sorted indices and the heap.
''',
tc="nlogn", sc="n",
java=r'''
public class MaximumSubsequenceScore {

    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, (a, b) -> Integer.compare(nums2[b], nums2[a]));
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        long sum = 0, best = 0;
        for (int i : order) {
            heap.add(nums1[i]);
            sum += nums1[i];
            if (heap.size() > k) sum -= heap.poll();
            if (heap.size() == k) best = Math.max(best, sum * nums2[i]);
        }
        return best;
    }
}
''',
test=r'''
class MaximumSubsequenceScoreTest {

    private final MaximumSubsequenceScore solution = new MaximumSubsequenceScore();

    @Test
    void examples() {
        assertEquals(12, solution.maxScore(new int[]{1, 3, 3, 2}, new int[]{2, 1, 3, 4}, 3));
        assertEquals(30, solution.maxScore(new int[]{4, 2, 3, 1, 1}, new int[]{7, 5, 10, 9, 6}, 1));
    }
}
''',
trace=r'''
function run(a, b, k) {
  const ord = a.map((_, i) => i).sort((x, y) => b[y] - b[x]), heap = []; let sum = 0, best = 0;
  A.step(`Sort the pairs by nums2, largest first. Each pair in turn can be the one setting the minimum.`, A.arr('nums2 (sorted desc)', ord.map(i => b[i])), A.arr('nums1 (same order)', ord.map(i => a[i])));
  ord.forEach((i, t) => {
    heap.push(a[i]); sum += a[i]; heap.sort((x, y) => x - y);
    let dropped = null; if (heap.length > k) { dropped = heap.shift(); sum -= dropped; }
    const score = heap.length === k ? sum * b[i] : null; if (score !== null) best = Math.max(best, score);
    A.step(`Minimum nums2 = ${b[i]}. Keep the ${k} largest nums1 values so far${dropped !== null ? ` (drop ${dropped})` : ''}: sum ${sum}.${score !== null ? ` Score ${sum} × ${b[i]} = ${score}.` : ''}`, A.arr('nums2 (sorted desc)', ord.map(j => b[j]), { hl: { [t]: 'cur' } }), A.arr(`min-heap (k = ${k})`, heap), A.vars({ sum, best }));
  });
  A.step(`Maximum score: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('k = 3', 'nums1 = [1,3,3,2], nums2 = [2,1,3,4]', () => run([1, 3, 3, 2], [2, 1, 3, 4], 3));
'''),

P(num=2462, slug="total-cost-to-hire-k-workers", title="Total Cost to Hire K Workers", diff="Medium", topic="Heap", cls="TotalCostToHire",
idea="Two min-heaps hold the first and last `candidates` workers; each round hire the cheaper top and refill that side.",
vname="Two heaps from both ends",
spec=r'''
Hire exactly `k` workers in `k` sessions. In each session, choose the cheapest worker among the first `candidates` and the last `candidates`
remaining workers (ties go to the smaller index). Return the total cost.

**Example**
```
costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4 → 11
costs = [1,2,4,1], k = 3, candidates = 3               → 4
```

**Constraints**
* `1 <= k, candidates <= costs.length <= 10^5`
''',
approach=r'''
**Two heaps + two pointers.** Fill `left` with the first `candidates` and `right` with the last (without overlap). Each session, take the
smaller top (left on ties, since it has the smaller index) and refill that heap from its pointer if workers remain between the pointers.

* Time: **O((k + candidates) log candidates)** — heap operations.
* Space: **O(candidates)** — the two heaps.
''',
tc="nlogn", sc="n",
java=r'''
public class TotalCostToHire {

    public long totalCost(int[] costs, int k, int candidates) {
        PriorityQueue<Integer> left = new PriorityQueue<>(), right = new PriorityQueue<>();
        int lo = 0, hi = costs.length - 1;
        long total = 0;
        for (int session = 0; session < k; session++) {
            while (left.size() < candidates && lo <= hi) left.add(costs[lo++]);
            while (right.size() < candidates && lo <= hi) right.add(costs[hi--]);
            int a = left.isEmpty() ? Integer.MAX_VALUE : left.peek();
            int b = right.isEmpty() ? Integer.MAX_VALUE : right.peek();
            if (a <= b) total += left.poll(); else total += right.poll();
        }
        return total;
    }
}
''',
test=r'''
class TotalCostToHireTest {

    private final TotalCostToHire solution = new TotalCostToHire();

    @Test
    void examples() {
        assertEquals(11, solution.totalCost(new int[]{17, 12, 10, 2, 7, 2, 11, 20, 8}, 3, 4));
        assertEquals(4, solution.totalCost(new int[]{1, 2, 4, 1}, 3, 3));
    }
}
''',
trace=r'''
function run(c, k, cand) {
  const L = [], R = []; let lo = 0, hi = c.length - 1, total = 0; const hired = {};
  for (let s = 0; s < k; s++) {
    while (L.length < cand && lo <= hi) L.push([c[lo], lo++]);
    while (R.length < cand && lo <= hi) R.push([c[hi], hi--]);
    L.sort((x, y) => x[0] - y[0] || x[1] - y[1]); R.sort((x, y) => x[0] - y[0] || x[1] - y[1]);
    const a = L[0] ? L[0][0] : Infinity, b = R[0] ? R[0][0] : Infinity;
    const [cost, idx] = a <= b ? L.shift() : R.shift(); total += cost; hired[idx] = 'ok';
    A.step(`Session ${s + 1}: the cheapest of the front group is ${a === Infinity ? '—' : a}, of the back group ${b === Infinity ? '—' : b}. Hire worker ${idx} for ${cost}. Total ${total}.`, A.arr('costs', c, { hl: { ...Object.fromEntries(L.map(([, i]) => [i, 'sel'])), ...Object.fromEntries(R.map(([, i]) => [i, 'alt'])), ...hired, [idx]: 'cur' } }), A.vars({ total }));
  }
  A.step(`Total cost: ${total}.`, A.text('Result', total, 'ok'));
}
A.scenario('k = 3, candidates = 4', 'costs = [17,12,10,2,7,2,11,20,8]', () => run([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4));
'''),

P(num=374, slug="guess-number-higher-or-lower", title="Guess Number Higher or Lower", diff="Easy", topic="Binary Search", cls="GuessNumber",
idea="Binary search guided by the hint: too high, too low, or correct.",
vname="Binary search on the hint",
spec=r'''
A number `pick` is chosen from `1..n`. The API `guess(num)` returns `-1` if `num > pick`, `1` if `num < pick`, `0` if correct. Return `pick`.
(Here the API is a method of the same class, initialised with the hidden pick.)

**Example**
```
n = 10, pick = 6 → 6,   n = 1, pick = 1 → 1
```

**Constraints**
* `1 <= pick <= n <= 2^31 - 1`
''',
approach=r'''
**Binary search.** Halve `[lo, hi]` according to `guess(mid)`, using `>>>` so `lo + hi` never overflows.

* Time: **O(log n)** — about 31 guesses at most.
* Space: **O(1)** — two bounds.
''',
tc="log",
java=r'''
public class GuessNumber {

    private final int pick;

    public GuessNumber(int pick) {
        this.pick = pick;
    }

    /** The game's API: -1 if num is too high, 1 if too low, 0 if correct. */
    int guess(int num) {
        return Integer.compare(pick, num);
    }

    public int guessNumber(int n) {
        int lo = 1, hi = n;
        while (true) {
            int mid = (lo + hi) >>> 1;
            int r = guess(mid);
            if (r == 0) return mid;
            if (r < 0) hi = mid - 1; else lo = mid + 1;
        }
    }
}
''',
test=r'''
class GuessNumberTest {

    @ParameterizedTest
    @CsvSource({"10,6", "1,1", "2,2", "2147483647,2147483647", "2126753390,1702766719"})
    void finds(int n, int pick) {
        assertEquals(pick, new GuessNumber(pick).guessNumber(n));
    }
}
''',
trace=r'''
function run(n, pick) {
  let lo = 1, hi = n, tries = 0;
  const nums = [...Array(n)].map((_, i) => i + 1);
  while (true) {
    const mid = (lo + hi) >> 1; tries++;
    const r = Math.sign(pick - mid);
    A.step(`Guess ${mid}: ${r === 0 ? 'correct' : r < 0 ? 'too high, so search below' : 'too low, so search above'}.`, A.arr('1..n', nums, { range: [lo - 1, hi - 1], hl: { [mid - 1]: r === 0 ? 'ok' : 'cur' }, noIdx: true }), A.vars({ guesses: tries }));
    if (r === 0) { A.step(`Found ${mid} in ${tries} guesses.`, A.text('Result', mid, 'ok')); return; }
    if (r < 0) hi = mid - 1; else lo = mid + 1;
  }
}
A.scenario('n = 20', 'pick = 13', () => run(20, 13));
'''),

P(num=2300, slug="successful-pairs-of-spells-and-potions", title="Successful Pairs of Spells and Potions", diff="Medium", topic="Binary Search", cls="SuccessfulPairs",
idea="Sort potions; for each spell, binary-search the weakest potion that still succeeds.",
vname="Sort + binary search",
spec=r'''
A spell and potion pair succeeds if `spell × potion >= success`. For each spell, return how many potions form a successful pair with it.

**Example**
```
spells = [5,1,3], potions = [1,2,3,4,5], success = 7 → [4,0,3]
```

**Constraints**
* `1 <= n, m <= 10^5`; `1 <= success <= 10^10`
''',
approach=r'''
**Lower bound.** Sort potions. For a spell `s`, the smallest potion needed is `ceil(success / s)`; binary-search its position; every potion
from there on works. Use `long` arithmetic.

* Time: **O((n + m) log m)** — sort plus one search per spell.
* Space: **O(m)** — the sorted copy.
''',
tc="nlogn", sc="n",
java=r'''
public class SuccessfulPairs {

    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int[] p = potions.clone();
        Arrays.sort(p);
        int[] out = new int[spells.length];
        for (int i = 0; i < spells.length; i++) {
            long need = (success + spells[i] - 1) / spells[i];
            int lo = 0, hi = p.length;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (p[mid] < need) lo = mid + 1; else hi = mid;
            }
            out[i] = p.length - lo;
        }
        return out;
    }
}
''',
test=r'''
class SuccessfulPairsTest {

    private final SuccessfulPairs solution = new SuccessfulPairs();

    @Test
    void examples() {
        assertArrayEquals(new int[]{4, 0, 3}, solution.successfulPairs(new int[]{5, 1, 3}, new int[]{1, 2, 3, 4, 5}, 7));
        assertArrayEquals(new int[]{2, 0, 2}, solution.successfulPairs(new int[]{3, 1, 2}, new int[]{8, 5, 8}, 16));
    }
}
''',
trace=r'''
function run(spells, potions, success) {
  const p = potions.slice().sort((a, b) => a - b), out = [];
  A.step('Sort the potions so the strong ones are at the end.', A.arr('potions (sorted)', p), A.vars({ success }));
  spells.forEach(s => {
    const need = Math.ceil(success / s); let lo = 0; while (lo < p.length && p[lo] < need) lo++;
    out.push(p.length - lo);
    A.step(`Spell ${s} needs a potion of at least ${need}. Binary search finds index ${lo}: ${p.length - lo} potion${p.length - lo === 1 ? '' : 's'} work.`, A.arr('potions (sorted)', p, { hl: Object.fromEntries(p.map((_, i) => [i, i >= lo ? 'ok' : 'dim'])) }), A.arr('answer', out));
  });
}
A.scenario('Classic', 'spells = [5,1,3], potions = [1,2,3,4,5], success = 7', () => run([5, 1, 3], [1, 2, 3, 4, 5], 7));
'''),

P(num=1137, slug="n-th-tribonacci-number", title="N-th Tribonacci Number", diff="Easy", topic="1D DP", cls="Tribonacci",
idea="Each term is the sum of the previous three; keep only three rolling values.",
vname="Three rolling values",
spec=r'''
`T0 = 0`, `T1 = 1`, `T2 = 1`, and `T(n+3) = T(n) + T(n+1) + T(n+2)`. Return `Tn`.

**Example**
```
n = 4 → 4,   n = 25 → 1389537
```

**Constraints**
* `0 <= n <= 37`
''',
approach=r'''
**Rolling window.** Shift `(a, b, c)` forward `n - 2` times.

* Time: **O(n)** — one loop.
* Space: **O(1)** — three ints.
''',
java=r'''
public class Tribonacci {

    public int tribonacci(int n) {
        if (n == 0) return 0;
        int a = 0, b = 1, c = 1;
        for (int i = 3; i <= n; i++) {
            int d = a + b + c;
            a = b;
            b = c;
            c = d;
        }
        return c;
    }
}
''',
test=r'''
class TribonacciTest {

    private final Tribonacci solution = new Tribonacci();

    @ParameterizedTest
    @CsvSource({"0,0", "1,1", "2,1", "4,4", "25,1389537", "37,2082876103"})
    void values(int n, int expected) {
        assertEquals(expected, solution.tribonacci(n));
    }
}
''',
trace=r'''
function run(n) {
  const t = [0, 1, 1];
  A.step('T0 = 0, T1 = 1, T2 = 1.', A.arr('T', t));
  for (let i = 3; i <= n; i++) { t.push(t[i - 1] + t[i - 2] + t[i - 3]); A.step(`T${i} = ${t[i - 3]} + ${t[i - 2]} + ${t[i - 1]} = ${t[i]}.`, A.arr('T', t, { hl: { [i]: 'ok', [i - 1]: 'sel', [i - 2]: 'sel', [i - 3]: 'sel' } })); }
  A.step(`T${n} = ${t[n]}. Only the last three values are ever needed.`, A.text('Result', t[n], 'ok'));
}
A.scenario('n = 7', 'T7', () => run(7));
'''),
]
