PROBLEMS = [
P(num=1584, slug="min-cost-to-connect-all-points", title="Min Cost to Connect All Points", diff="Medium", topic="Graph General", cls="MinCostConnectPoints",
idea="Prim's algorithm on the complete graph: repeatedly attach the cheapest point not yet connected.",
vname="Prim's algorithm (dense O(n²))",
spec=r'''
Connect all `points` (2-D, integer coordinates) so every pair is linked by some path; connecting two points costs their Manhattan distance
`|x1 - x2| + |y1 - y2|`. Return the minimum total cost.

**Example**
```
[[0,0],[2,2],[3,10],[5,2],[7,0]] → 20
[[3,12],[-2,5],[-4,1]]           → 18
```

**Constraints**
* `1 <= n <= 1000`; all points distinct.
''',
approach=r'''
**Array-based Prim.** Keep `best[i]`, the cheapest edge from point `i` into the growing tree. Each round, pick the unconnected point with the
smallest `best`, add its cost, and lower `best[j]` for every other unconnected point through it. A dense graph makes this O(n²) version
faster than a heap.

* Time: **O(n²)** — n rounds, each scanning all points.
* Space: **O(n)** — the best and visited arrays.
''',
tc="n2", sc="n",
java=r'''
public class MinCostConnectPoints {

    public int minCostConnectPoints(int[][] points) {
        int n = points.length, total = 0;
        int[] best = new int[n];
        boolean[] inTree = new boolean[n];
        Arrays.fill(best, Integer.MAX_VALUE);
        best[0] = 0;
        for (int round = 0; round < n; round++) {
            int u = -1;
            for (int i = 0; i < n; i++) {
                if (!inTree[i] && (u < 0 || best[i] < best[u])) u = i;
            }
            inTree[u] = true;
            total += best[u];
            for (int v = 0; v < n; v++) {
                if (!inTree[v]) {
                    int d = Math.abs(points[u][0] - points[v][0]) + Math.abs(points[u][1] - points[v][1]);
                    if (d < best[v]) best[v] = d;
                }
            }
        }
        return total;
    }
}
''',
test=r'''
class MinCostConnectPointsTest {

    private final MinCostConnectPoints solution = new MinCostConnectPoints();

    @Test
    void examples() {
        assertEquals(20, solution.minCostConnectPoints(new int[][]{{0, 0}, {2, 2}, {3, 10}, {5, 2}, {7, 0}}));
        assertEquals(18, solution.minCostConnectPoints(new int[][]{{3, 12}, {-2, 5}, {-4, 1}}));
        assertEquals(0, solution.minCostConnectPoints(new int[][]{{0, 0}}));
    }
}
''',
trace=r'''
function run(pts) {
  const n = pts.length, best = new Array(n).fill(Infinity), inT = new Array(n).fill(false), from = new Array(n).fill(-1), edges = [];
  const nodes = pts.map(([x, y], i) => ({ id: i, label: `${x},${y}`, x: 40 + x * 30, y: 330 - y * 30 }));
  const d = (a, b) => Math.abs(pts[a][0] - pts[b][0]) + Math.abs(pts[a][1] - pts[b][1]);
  best[0] = 0; let total = 0;
  A.step('Grow a tree from the first point, always attaching the point that is cheapest to reach.', A.graph('points', nodes, []));
  for (let r = 0; r < n; r++) {
    let u = -1; for (let i = 0; i < n; i++) if (!inT[i] && (u < 0 || best[i] < best[u])) u = i;
    inT[u] = true; total += best[u]; if (from[u] >= 0) edges.push([from[u], u, best[u], 'ok']);
    for (let v = 0; v < n; v++) if (!inT[v] && d(u, v) < best[v]) { best[v] = d(u, v); from[v] = u; }
    A.step(r ? `Attach (${pts[u]}) for ${best[u]}. Total: ${total}.` : `Start the tree at (${pts[u]}).`, A.graph('points', nodes, edges, { hl: Object.fromEntries(pts.map((_, i) => [i, i === u ? 'cur' : inT[i] ? 'ok' : ''])) }), A.arr('cheapest link to the tree', best.map((b, i) => (inT[i] ? '✓' : b))));
  }
  A.step(`Minimum total cost: ${total}.`, A.text('Result', total, 'ok'));
}
A.scenario('Five points', '[[0,0],[2,2],[3,10],[5,2],[7,0]]', () => run([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]));
'''),

P(num=778, slug="swim-in-rising-water", title="Swim in Rising Water", diff="Hard", topic="Graph General", cls="SwimInRisingWater",
idea="Dijkstra where a path's cost is its highest cell: always expand the lowest reachable cell next.",
vname="Min-heap on path maximum",
spec=r'''
`grid[i][j]` is the elevation of a cell in an `n × n` grid. At time `t` the water level is `t`, and you can swim between adjacent cells whose
elevations are both at most `t`. Return the least time to go from the top-left to the bottom-right.

**Example**
```
[[0,2],[1,3]] → 3
```

**Constraints**
* `1 <= n <= 50`; values are a permutation of `0 .. n²-1`.
''',
approach=r'''
**Minimax Dijkstra.** A path's cost is the maximum elevation on it. Pop the cell with the smallest current maximum from a heap, push its
unvisited neighbours with cost `max(current, elevation)`. The first time the target is popped, its cost is the answer.

* Time: **O(n² log n)** — each cell is pushed once into a heap of size up to n².
* Space: **O(n²)** — visited grid and heap.
''',
tc="nlogn", sc="n2",
java=r'''
public class SwimInRisingWater {

    public int swimInWater(int[][] grid) {
        int n = grid.length;
        boolean[][] seen = new boolean[n][n];
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.add(new int[]{grid[0][0], 0, 0});
        seen[0][0] = true;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (true) {
            int[] cur = heap.poll();
            if (cur[1] == n - 1 && cur[2] == n - 1) return cur[0];
            for (int[] d : dirs) {
                int r = cur[1] + d[0], c = cur[2] + d[1];
                if (r >= 0 && r < n && c >= 0 && c < n && !seen[r][c]) {
                    seen[r][c] = true;
                    heap.add(new int[]{Math.max(cur[0], grid[r][c]), r, c});
                }
            }
        }
    }
}
''',
test=r'''
class SwimInRisingWaterTest {

    private final SwimInRisingWater solution = new SwimInRisingWater();

    @Test
    void examples() {
        assertEquals(3, solution.swimInWater(new int[][]{{0, 2}, {1, 3}}));
        assertEquals(16, solution.swimInWater(new int[][]{{0, 1, 2, 3, 4}, {24, 23, 22, 21, 5}, {12, 13, 14, 15, 16}, {11, 17, 18, 19, 20}, {10, 9, 8, 7, 6}}));
    }
}
''',
trace=r'''
function run(g) {
  const n = g.length, seen = new Set(['0,0']), heap = [[g[0][0], 0, 0]], done = {};
  A.step('A path costs as much as its highest cell. Always continue from the lowest frontier cell.', A.grid('elevations', g, { hl: { '0,0': 'cur' } }));
  while (true) {
    heap.sort((a, b) => a[0] - b[0]); const [t, r, c] = heap.shift();
    done[`${r},${c}`] = 'ok';
    if (r === n - 1 && c === n - 1) { A.step(`Reached the corner. The highest cell on the best path is ${t}, so the answer is ${t}.`, A.grid('elevations', g, { hl: done }), A.text('Result', t, 'ok')); return; }
    for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const a = r + dr, b = c + dc, k = `${a},${b}`; if (a >= 0 && a < n && b >= 0 && b < n && !seen.has(k)) { seen.add(k); heap.push([Math.max(t, g[a][b]), a, b]); } }
    A.step(`Swim to (${r},${c}); the water must be at least ${t}. Add its neighbours to the frontier.`, A.grid('elevations', g, { hl: { ...done, ...Object.fromEntries(heap.map(([, a, b]) => [`${a},${b}`, 'sel'])), [`${r},${c}`]: 'cur' } }));
  }
}
A.scenario('Spiral', '5 × 5 grid', () => run([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]));
'''),

P(num=332, slug="reconstruct-itinerary", title="Reconstruct Itinerary", diff="Hard", topic="Graph General", cls="ReconstructItinerary",
idea="Hierholzer's algorithm: take the smallest unused ticket each time; airports are added when they run out of tickets, giving the route in reverse.",
vname="Hierholzer with sorted destinations",
spec=r'''
Given airline `tickets[i] = [from, to]`, use **all** tickets exactly once to build an itinerary starting at `"JFK"`. If several are valid,
return the lexicographically smallest. At least one valid itinerary exists.

**Example**
```
[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]] → ["JFK","MUC","LHR","SFO","SJC"]
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]] → ["JFK","ATL","JFK","SFO","ATL","SFO"]
```

**Constraints**
* `1 <= tickets.length <= 300`
''',
approach=r'''
**Eulerian path.** Map each airport to a min-heap of destinations (`MyHashMap<String, PriorityQueue<String>>`). With an explicit stack,
keep flying the smallest unused ticket from the top airport; when an airport has no tickets left, pop it onto the front of the answer.
Dead ends are therefore placed last, which is why the greedy choice still uses every ticket.

* Time: **O(E log E)** — each ticket is pushed and popped from a heap once.
* Space: **O(E)** — the graph and the stack.
''',
tc="nlogn", sc="n",
java=r'''
public class ReconstructItinerary {

    public List<String> findItinerary(List<List<String>> tickets) {
        MyHashMap<String, PriorityQueue<String>> graph = new MyHashMap<>();
        for (List<String> t : tickets) graph.computeIfAbsent(t.get(0), k -> new PriorityQueue<>()).add(t.get(1));
        LinkedList<String> route = new LinkedList<>();
        Deque<String> stack = new ArrayDeque<>(List.of("JFK"));
        while (!stack.isEmpty()) {
            PriorityQueue<String> next = graph.get(stack.peek());
            if (next != null && !next.isEmpty()) {
                stack.push(next.poll());
            } else {
                route.addFirst(stack.pop());
            }
        }
        return route;
    }
}
''',
test=r'''
class ReconstructItineraryTest {

    private final ReconstructItinerary solution = new ReconstructItinerary();

    @Test
    void examples() {
        assertEquals(List.of("JFK", "MUC", "LHR", "SFO", "SJC"),
                solution.findItinerary(List.of(List.of("MUC", "LHR"), List.of("JFK", "MUC"), List.of("SFO", "SJC"), List.of("LHR", "SFO"))));
        assertEquals(List.of("JFK", "ATL", "JFK", "SFO", "ATL", "SFO"),
                solution.findItinerary(List.of(List.of("JFK", "SFO"), List.of("JFK", "ATL"), List.of("SFO", "ATL"), List.of("ATL", "JFK"), List.of("ATL", "SFO"))));
    }

    @Test
    void deadEndFirst() {
        assertEquals(List.of("JFK", "NRT", "JFK", "KUL"),
                solution.findItinerary(List.of(List.of("JFK", "KUL"), List.of("JFK", "NRT"), List.of("NRT", "JFK"))));
    }
}
''',
trace=r'''
function run(tickets) {
  const g = {}; tickets.forEach(([a, b]) => (g[a] = g[a] || []).push(b)); Object.values(g).forEach(l => l.sort());
  const airports = [...new Set(tickets.flat())], nodes = airports.map(a => ({ id: a, label: a }));
  const used = []; const stack = ['JFK'], route = [];
  A.step('Always fly the alphabetically smallest unused ticket. When an airport has no tickets left, it goes to the front of the route.', A.graph('tickets', nodes, tickets.map(([a, b]) => [a, b]), { directed: true, hl: { JFK: 'cur' } }), A.stack('stack', stack));
  while (stack.length) {
    const top = stack[stack.length - 1];
    if (g[top] && g[top].length) { const nx = g[top].shift(); used.push([top, nx]); stack.push(nx); A.step(`From ${top}, fly to ${nx}.`, A.graph('tickets', nodes, tickets.map(([a, b]) => [a, b, '', used.some(([x, y]) => x === a && y === b) ? 'ok' : '']), { directed: true, hl: { [nx]: 'cur' } }), A.stack('stack', stack), A.arr('route', route)); }
    else { route.unshift(stack.pop()); A.step(`${top} has no tickets left: put it at the front of the route.`, A.stack('stack', stack), A.arr('route', route, { hl: { 0: 'ok' } })); }
  }
  A.step(`Itinerary: ${route.join(' → ')}.`, A.text('Result', route.join(' → '), 'ok'));
}
A.scenario('Dead end first', 'JFK→KUL, JFK→NRT, NRT→JFK', () => run([['JFK', 'KUL'], ['JFK', 'NRT'], ['NRT', 'JFK']]));
'''),

P(num=621, slug="task-scheduler", title="Task Scheduler", diff="Medium", topic="Heap", cls="TaskScheduler",
idea="The most frequent task fixes a frame of (maxCount − 1) blocks of n + 1 slots; the others fill the gaps.",
vname="Counting formula",
spec=r'''
CPU tasks are letters; each takes one interval. The same task must be separated by at least `n` intervals (idle intervals allowed).
Return the minimum number of intervals to finish all tasks.

**Example**
```
tasks = [A,A,A,B,B,B], n = 2 → 8   (A B idle A B idle A B)
tasks = [A,C,A,B,D,B], n = 1 → 6
```

**Constraints**
* `1 <= tasks.length <= 10^4`; `0 <= n <= 100`
''',
approach=r'''
**Frame counting.** Let `maxCount` be the highest frequency and `tied` the number of tasks with that frequency. The busiest task needs
`(maxCount - 1)` full blocks of `n + 1` slots plus a final block of `tied` slots. If there are more tasks than that, no idle time is needed:
the answer is `max(tasks.length, (maxCount - 1) * (n + 1) + tied)`.

* Time: **O(N)** — one counting pass.
* Space: **O(1)** — 26 counters.
''',
java=r'''
public class TaskScheduler {

    public int leastInterval(char[] tasks, int n) {
        int[] count = new int[26];
        for (char t : tasks) count[t - 'A']++;
        int maxCount = 0, tied = 0;
        for (int c : count) {
            if (c > maxCount) { maxCount = c; tied = 1; }
            else if (c == maxCount) tied++;
        }
        return Math.max(tasks.length, (maxCount - 1) * (n + 1) + tied);
    }
}
''',
test=r'''
class TaskSchedulerTest {

    private final TaskScheduler solution = new TaskScheduler();

    @Test
    void examples() {
        assertEquals(8, solution.leastInterval("AAABBB".toCharArray(), 2));
        assertEquals(6, solution.leastInterval("ACABDB".toCharArray(), 1));
        assertEquals(10, solution.leastInterval("AAABBB".toCharArray(), 3));
        assertEquals(6, solution.leastInterval("AAABBB".toCharArray(), 0));
    }
}
''',
trace=r'''
function run(tasks, n) {
  const cnt = {}; [...tasks].forEach(t => (cnt[t] = (cnt[t] || 0) + 1));
  const maxc = Math.max(...Object.values(cnt)), tied = Object.values(cnt).filter(c => c === maxc).length;
  A.step(`The most frequent task appears ${maxc} times (${tied} task${tied > 1 ? 's' : ''} tie). It needs ${maxc - 1} gaps of ${n} slots between its runs.`, A.map('counts', cnt));
  const blocks = [];
  const top = Object.keys(cnt).filter(t => cnt[t] === maxc), rest = [...tasks].filter(t => !top.includes(t));
  for (let b = 0; b < maxc; b++) { const row = top.slice(); if (b < maxc - 1) while (row.length < n + 1) row.push(rest.length ? rest.shift() : 'idle'); blocks.push(row); }
  A.step(`Lay out ${maxc - 1} full blocks of ${n + 1} slots plus a last block with the ${tied} busiest task${tied > 1 ? 's' : ''}. Other tasks fill the gaps; leftover gaps are idle.`, A.grid('schedule', blocks.map(r => r.concat(new Array(n + 1 - r.length).fill('')))));
  const frame = (maxc - 1) * (n + 1) + tied, ans = Math.max(tasks.length, frame);
  A.step(`Frame size: (${maxc} − 1) × ${n + 1} + ${tied} = ${frame}. ${tasks.length > frame ? 'There are more tasks than slots, so no idling is needed.' : ''} Answer: ${ans}.`, A.text('Result', ans, 'ok'));
}
A.scenario('n = 2', 'tasks = AAABBB', () => run('AAABBB', 2));
A.scenario('Many kinds', 'tasks = AAABCDEFG, n = 2', () => run('AAABCDEFG', 2));
''',
variants=[dict(
name="Greedy simulation with a max-heap",
idea="Each round of n + 1 slots, run the most frequent remaining tasks first.",
approach=r'''
**Simulation.** Keep counts in a max-heap. Each round, pop up to `n + 1` tasks, run them, and push back the ones with work left. A round
that is not the last counts `n + 1` intervals.

* Time: **O(N log 26)** — one heap operation per executed task.
* Space: **O(1)** — at most 26 heap entries.
''',
java=r'''
public class TaskScheduler {

    public int leastInterval(char[] tasks, int n) {
        int[] count = new int[26];
        for (char t : tasks) count[t - 'A']++;
        PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.reverseOrder());
        for (int c : count) if (c > 0) heap.add(c);
        int time = 0;
        while (!heap.isEmpty()) {
            List<Integer> left = new ArrayList<>();
            int ran = 0;
            for (int i = 0; i <= n && !heap.isEmpty(); i++, ran++) {
                int c = heap.poll() - 1;
                if (c > 0) left.add(c);
            }
            heap.addAll(left);
            time += heap.isEmpty() ? ran : n + 1;
        }
        return time;
    }
}
''',
trace=r'''
function run(tasks, n) {
  const cnt = {}; [...tasks].forEach(t => (cnt[t] = (cnt[t] || 0) + 1));
  let time = 0, round = 0;
  while (Object.values(cnt).some(c => c > 0)) {
    const pick = Object.keys(cnt).filter(t => cnt[t] > 0).sort((a, b) => cnt[b] - cnt[a]).slice(0, n + 1);
    pick.forEach(t => cnt[t]--);
    const last = !Object.values(cnt).some(c => c > 0);
    time += last ? pick.length : n + 1; round++;
    A.step(`Round ${round}: run ${pick.join(' ')}${!last && pick.length < n + 1 ? ` and idle ${n + 1 - pick.length}` : ''}. Time: ${time}.`, A.map('remaining', cnt), A.vars({ time }));
  }
  A.step(`Total: ${time} intervals.`, A.text('Result', time, 'ok'));
}
A.scenario('n = 2', 'tasks = AAABBB', () => run('AAABBB', 2));
''')]),

P(num=1046, slug="last-stone-weight", title="Last Stone Weight", diff="Easy", topic="Heap", cls="LastStoneWeight",
idea="A max-heap always hands you the two heaviest stones to smash.",
vname="Max-heap simulation",
spec=r'''
Repeatedly smash the two heaviest stones `x <= y`: if equal, both vanish; otherwise a stone of weight `y - x` remains. Return the weight of
the last stone, or 0 if none remain.

**Example**
```
[2,7,4,1,8,1] → 1
```

**Constraints**
* `1 <= stones.length <= 30`
''',
approach=r'''
**Max-heap.** Pop the two largest; push their difference if non-zero. Stop when at most one stone is left.

* Time: **O(n log n)** — about n rounds of heap operations.
* Space: **O(n)** — the heap.
''',
tc="nlogn",
java=r'''
public class LastStoneWeight {

    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.reverseOrder());
        for (int s : stones) heap.add(s);
        while (heap.size() > 1) {
            int y = heap.poll(), x = heap.poll();
            if (y > x) heap.add(y - x);
        }
        return heap.isEmpty() ? 0 : heap.peek();
    }
}
''',
test=r'''
class LastStoneWeightTest {

    private final LastStoneWeight solution = new LastStoneWeight();

    @Test
    void examples() {
        assertEquals(1, solution.lastStoneWeight(new int[]{2, 7, 4, 1, 8, 1}));
        assertEquals(1, solution.lastStoneWeight(new int[]{1}));
        assertEquals(0, solution.lastStoneWeight(new int[]{3, 3}));
    }
}
''',
trace=r'''
function run(stones) {
  const h = stones.slice().sort((a, b) => b - a);
  A.step('Keep the stones in a max-heap.', A.arr('heap (largest first)', h));
  while (h.length > 1) { const y = h.shift(), x = h.shift(); if (y > x) h.push(y - x); h.sort((a, b) => b - a); A.step(`Smash ${y} and ${x}: ${y > x ? `a stone of ${y - x} remains` : 'both vanish'}.`, A.arr('heap (largest first)', h, { hl: y > x ? { [h.indexOf(y - x)]: 'ok' } : {} })); }
  A.step(`Last stone: ${h[0] || 0}.`, A.text('Result', h[0] || 0, 'ok'));
}
A.scenario('Six stones', 'stones = [2,7,4,1,8,1]', () => run([2, 7, 4, 1, 8, 1]));
'''),

P(num=703, slug="kth-largest-element-in-a-stream", title="Kth Largest Element in a Stream", diff="Easy", topic="Heap", cls="KthLargestInStream",
idea="A min-heap of size k keeps the k largest scores; its top is the k-th largest.",
vname="Min-heap of size k",
spec=r'''
Implement `KthLargest(k, nums)` and `int add(val)`, which adds `val` to the stream and returns the current `k`-th largest element.

**Example**
```
KthLargest(3, [4,5,8,2]); add(3) → 4; add(5) → 5; add(10) → 5; add(9) → 8; add(4) → 8
```

**Constraints**
* `1 <= k <= 10^4`; at least `k` elements exist when `add` returns.
''',
approach=r'''
**Bounded heap.** Keep only the `k` largest values in a min-heap; after each add, pop while the size exceeds `k`. The top is the answer.

* Time: **O(log k)** — per add.
* Space: **O(k)** — the heap.
''',
tc="log",
java=r'''
public class KthLargestInStream {

    private final int k;
    private final PriorityQueue<Integer> heap = new PriorityQueue<>();

    public KthLargestInStream(int k, int[] nums) {
        this.k = k;
        for (int x : nums) add(x);
    }

    public int add(int val) {
        heap.add(val);
        if (heap.size() > k) heap.poll();
        return heap.peek();
    }
}
''',
test=r'''
class KthLargestInStreamTest {

    @Test
    void example() {
        KthLargestInStream s = new KthLargestInStream(3, new int[]{4, 5, 8, 2});
        assertEquals(4, s.add(3));
        assertEquals(5, s.add(5));
        assertEquals(5, s.add(10));
        assertEquals(8, s.add(9));
        assertEquals(8, s.add(4));
    }
}
''',
trace=r'''
A.scenario('k = 3', 'start [4,5,8,2] · add 3, 5, 10, 9, 4', () => {
  const k = 3, h = [];
  const add = v => { h.push(v); h.sort((a, b) => a - b); const drop = h.length > k ? h.shift() : null; return drop; };
  [4, 5, 8, 2].forEach(add);
  A.step(`Keep only the ${k} largest values. The smallest of them (the heap top) is the ${k}rd largest.`, A.arr('min-heap', h, { hl: { 0: 'alt' } }));
  for (const v of [3, 5, 10, 9, 4]) { const d = add(v); A.step(`add(${v})${d !== null ? `: ${d} is pushed out` : ''}. The answer is ${h[0]}.`, A.arr('min-heap', h, { hl: { 0: 'ok' } }), A.text('kth largest', h[0], 'ok')); }
});
'''),

P(num=973, slug="k-closest-points-to-origin", title="K Closest Points to Origin", diff="Medium", topic="Heap", cls="KClosestPoints",
idea="Keep a max-heap of the k closest points seen so far; a closer point replaces the farthest one.",
vname="Max-heap of size k",
spec=r'''
Return the `k` points closest to the origin `(0, 0)` by Euclidean distance, in any order.

**Example**
```
points = [[1,3],[-2,2]], k = 1          → [[-2,2]]
points = [[3,3],[5,-1],[-2,4]], k = 2   → [[3,3],[-2,4]]
```

**Constraints**
* `1 <= k <= points.length <= 10^4`
''',
approach=r'''
**Bounded max-heap by squared distance.** Push each point; if the heap holds more than `k`, pop the farthest. Squared distances avoid
square roots and stay exact.

* Time: **O(n log k)** — n heap operations of size k.
* Space: **O(k)** — the heap.
''',
tc="nlogn",
java=r'''
public class KClosestPoints {

    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(dist(b), dist(a)));
        for (int[] p : points) {
            heap.add(p);
            if (heap.size() > k) heap.poll();
        }
        return heap.toArray(new int[0][]);
    }

    private static int dist(int[] p) {
        return p[0] * p[0] + p[1] * p[1];
    }
}
''',
test=r'''
class KClosestPointsTest {

    private final KClosestPoints solution = new KClosestPoints();

    private static Set<List<Integer>> set(int[][] pts) {
        Set<List<Integer>> s = new HashSet<>();
        for (int[] p : pts) s.add(List.of(p[0], p[1]));
        return s;
    }

    @Test
    void examples() {
        assertEquals(Set.of(List.of(-2, 2)), set(solution.kClosest(new int[][]{{1, 3}, {-2, 2}}, 1)));
        assertEquals(Set.of(List.of(3, 3), List.of(-2, 4)), set(solution.kClosest(new int[][]{{3, 3}, {5, -1}, {-2, 4}}, 2)));
    }
}
''',
trace=r'''
function run(pts, k) {
  const d = p => p[0] * p[0] + p[1] * p[1], heap = [];
  const nodes = pts.map((p, i) => ({ id: i, label: `${p}`, x: 160 + p[0] * 25, y: 160 - p[1] * 25 })).concat([{ id: 'O', label: 'O', x: 160, y: 160 }]);
  pts.forEach((p, i) => {
    heap.push(i); heap.sort((a, b) => d(pts[b]) - d(pts[a]));
    const drop = heap.length > k ? heap.shift() : null;
    A.step(`Add (${p}) at squared distance ${d(p)}.${drop !== null ? ` More than ${k} points: drop the farthest, (${pts[drop]}).` : ''}`, A.graph('points', nodes, heap.map(j => ['O', j, d(pts[j])])), A.arr('max-heap (farthest first)', heap.map(j => `(${pts[j]}):${d(pts[j])}`), { hl: { 0: 'alt' } }));
  });
  A.step(`The ${k} closest points remain.`, A.text('Result', heap.map(j => `[${pts[j]}]`).join(' '), 'ok'));
}
A.scenario('k = 2', '[[3,3],[5,-1],[-2,4],[1,1]]', () => run([[3, 3], [5, -1], [-2, 4], [1, 1]], 2));
'''),

P(num=355, slug="design-twitter", title="Design Twitter", diff="Medium", topic="Heap", cls="Twitter",
idea="Each user's tweets are a newest-first list; a news feed merges the lists of the user and their followees with a heap.",
vname="Hash maps + k-way merge",
spec=r'''
Design a simplified Twitter:
* `postTweet(userId, tweetId)`;
* `getNewsFeed(userId)`: the 10 most recent tweet ids posted by the user or anyone they follow, newest first;
* `follow(followerId, followeeId)` and `unfollow(followerId, followeeId)`.

**Example**
```
postTweet(1,5); getNewsFeed(1) → [5]; follow(1,2); postTweet(2,6);
getNewsFeed(1) → [6,5]; unfollow(1,2); getNewsFeed(1) → [5]
```

**Constraints**
* At most `3 * 10^4` calls.
''',
approach=r'''
**Own hash maps.** `MyHashMap<user, List<tweet>>` (tweets stored with a global timestamp) and `MyHashMap<user, MyHashSet<followee>>`.
`getNewsFeed` pushes the newest tweet of each relevant user into a max-heap by time, then pops up to 10 times, each time pushing that user's
next-older tweet.

* Time: **O(F log F)** — per feed, where F is the number of followees (posting and following are O(1)).
* Space: **O(T + E)** — all tweets and follow links.
''',
tc="nlogn", sc="n",
java=r'''
public class Twitter {

    private record Tweet(int id, int time) { }

    private final MyHashMap<Integer, List<Tweet>> tweets = new MyHashMap<>();
    private final MyHashMap<Integer, MyHashSet<Integer>> follows = new MyHashMap<>();
    private int clock;

    public void postTweet(int userId, int tweetId) {
        tweets.computeIfAbsent(userId, k -> new ArrayList<>()).add(new Tweet(tweetId, clock++));
    }

    public List<Integer> getNewsFeed(int userId) {
        // heap entries: {time, userId, index into that user's list}
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        List<Integer> users = new ArrayList<>(List.of(userId));
        MyHashSet<Integer> f = follows.get(userId);
        if (f != null) for (int u : f) if (u != userId) users.add(u);
        for (int u : users) {
            List<Tweet> list = tweets.get(u);
            if (list != null && !list.isEmpty()) heap.add(new int[]{list.getLast().time(), u, list.size() - 1});
        }
        List<Integer> feed = new ArrayList<>();
        while (feed.size() < 10 && !heap.isEmpty()) {
            int[] top = heap.poll();
            List<Tweet> list = tweets.get(top[1]);
            feed.add(list.get(top[2]).id());
            if (top[2] > 0) heap.add(new int[]{list.get(top[2] - 1).time(), top[1], top[2] - 1});
        }
        return feed;
    }

    public void follow(int followerId, int followeeId) {
        follows.computeIfAbsent(followerId, k -> new MyHashSet<>()).add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        MyHashSet<Integer> f = follows.get(followerId);
        if (f != null) f.remove(followeeId);
    }
}
''',
test=r'''
class TwitterTest {

    @Test
    void example() {
        Twitter t = new Twitter();
        t.postTweet(1, 5);
        assertEquals(List.of(5), t.getNewsFeed(1));
        t.follow(1, 2);
        t.postTweet(2, 6);
        assertEquals(List.of(6, 5), t.getNewsFeed(1));
        t.unfollow(1, 2);
        assertEquals(List.of(5), t.getNewsFeed(1));
    }

    @Test
    void onlyTenNewest() {
        Twitter t = new Twitter();
        for (int i = 0; i < 12; i++) t.postTweet(1, i);
        assertEquals(List.of(11, 10, 9, 8, 7, 6, 5, 4, 3, 2), t.getNewsFeed(1));
    }
}
''',
trace=r'''
A.scenario('Two users', 'post · follow · feed · unfollow', () => {
  let clock = 0; const tw = new Map(), fol = new Map();
  const post = (u, id) => { (tw.get(u) || tw.set(u, []).get(u)).push([id, clock++]); A.step(`User ${u} posts tweet ${id} at time ${clock - 1}.`, A.hashTable('tweets by user', new Map([...tw].map(([k, v]) => [k, v.map(x => x[0]).join(',')])))); };
  const feed = u => { const users = [u, ...(fol.get(u) || [])]; const all = users.flatMap(x => (tw.get(x) || []).map(t => t)); all.sort((a, b) => b[1] - a[1]); const r = all.slice(0, 10).map(t => t[0]); A.step(`getNewsFeed(${u}): merge the newest tweets of users ${users.join(', ')} with a heap: [${r}].`, A.hashTable('follows', new Map([...fol].map(([k, v]) => [k, [...v].join(',')]))), A.text('feed', JSON.stringify(r), 'ok')); };
  post(1, 5); feed(1);
  (fol.get(1) || fol.set(1, new Set()).get(1)).add(2); A.step('User 1 follows user 2.', A.hashTable('follows', new Map([[1, '2']])));
  post(2, 6); feed(1);
  fol.get(1).delete(2); A.step('User 1 unfollows user 2.', A.hashTable('follows', new Map([[1, '']])));
  feed(1);
});
'''),

P(num=763, slug="partition-labels", title="Partition Labels", diff="Medium", topic="Greedy", cls="PartitionLabels",
idea="A part must extend at least to the last occurrence of every letter it contains; cut as soon as that reach is met.",
vname="Last-occurrence greedy",
spec=r'''
Split `s` into as many parts as possible so that each letter appears in at most one part. Return the part sizes in order.

**Example**
```
"ababcbacadefegdehijhklij" → [9,7,8]
"eccbbbbdec"               → [10]
```

**Constraints**
* `1 <= s.length <= 500`; lowercase letters.
''',
approach=r'''
**Reach.** Record each letter's last index. Scan, extending `end = max(end, last[c])`; when `i == end`, the part is closed.

* Time: **O(n)** — two passes.
* Space: **O(1)** — 26 last indices.
''',
java=r'''
public class PartitionLabels {

    public List<Integer> partitionLabels(String s) {
        int[] last = new int[26];
        for (int i = 0; i < s.length(); i++) last[s.charAt(i) - 'a'] = i;
        List<Integer> sizes = new ArrayList<>();
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            end = Math.max(end, last[s.charAt(i) - 'a']);
            if (i == end) {
                sizes.add(end - start + 1);
                start = i + 1;
            }
        }
        return sizes;
    }
}
''',
test=r'''
class PartitionLabelsTest {

    private final PartitionLabels solution = new PartitionLabels();

    @Test
    void examples() {
        assertEquals(List.of(9, 7, 8), solution.partitionLabels("ababcbacadefegdehijhklij"));
        assertEquals(List.of(10), solution.partitionLabels("eccbbbbdec"));
        assertEquals(List.of(1, 1, 1), solution.partitionLabels("abc"));
    }
}
''',
trace=r'''
function run(s) {
  const last = {}; [...s].forEach((c, i) => (last[c] = i));
  const sizes = []; let start = 0, end = 0;
  A.step('Record the last position of every letter. A part must reach at least the last occurrence of each of its letters.', A.chars('s', s), A.map('last index', last));
  for (let i = 0; i < s.length; i++) {
    end = Math.max(end, last[s[i]]);
    if (i === end) { sizes.push(end - start + 1); A.step(`At ${i}, nothing in this part appears later. Cut: size ${end - start + 1}.`, A.chars('s', s, { range: [start, end], hl: Object.fromEntries([...Array(end - start + 1)].map((_, t) => [start + t, 'ok'])) }), A.arr('sizes', sizes)); start = i + 1; }
    else if (last[s[i]] === end && i > start) A.step(`'${s[i]}' appears again at ${last[s[i]]}, so this part must reach at least ${end}.`, A.chars('s', s, { range: [start, end], hl: { [i]: 'cur', [end]: 'alt' } }));
  }
}
A.scenario('Classic', 's = "ababcbacadefegdehijhklij"', () => run('ababcbacadefegdehijhklij'));
'''),

P(num=846, slug="hand-of-straights", title="Hand of Straights", diff="Medium", topic="Greedy", cls="HandOfStraights",
idea="The smallest remaining card must start a group, so greedily build groups from the smallest card up.",
vname="Sort + counts",
spec=r'''
Can the cards in `hand` be rearranged into groups of `groupSize` **consecutive** values?

**Example**
```
hand = [1,2,3,6,2,3,4,7,8], groupSize = 3 → true ([1,2,3],[2,3,4],[6,7,8])
hand = [1,2,3,4,5], groupSize = 4          → false
```

**Constraints**
* `1 <= hand.length <= 10^4`; `1 <= groupSize <= hand.length`
''',
approach=r'''
**Greedy from the smallest.** Count cards in a `MyHashMap` and sort the distinct values. For each value `v` (ascending) with count `c > 0`,
it must start `c` groups: every value `v+1 … v+groupSize-1` needs at least `c` copies, which are then used up.

* Time: **O(n log n)** — sorting dominates.
* Space: **O(n)** — counts and the sorted values.
''',
tc="nlogn", sc="n",
java=r'''
public class HandOfStraights {

    public boolean isNStraightHand(int[] hand, int groupSize) {
        if (hand.length % groupSize != 0) return false;
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int c : hand) count.merge(c, 1, Integer::sum);
        int[] values = hand.clone();
        Arrays.sort(values);
        for (int v : values) {
            int c = count.get(v);
            if (c == 0) continue;
            for (int x = v; x < v + groupSize; x++) {
                int have = count.getOrDefault(x, 0);
                if (have < c) return false;
                count.put(x, have - c);
            }
        }
        return true;
    }
}
''',
test=r'''
class HandOfStraightsTest {

    private final HandOfStraights solution = new HandOfStraights();

    @Test
    void examples() {
        assertTrue(solution.isNStraightHand(new int[]{1, 2, 3, 6, 2, 3, 4, 7, 8}, 3));
        assertFalse(solution.isNStraightHand(new int[]{1, 2, 3, 4, 5}, 4));
        assertTrue(solution.isNStraightHand(new int[]{8, 10, 12}, 1));
    }
}
''',
trace=r'''
function run(hand, k) {
  const cnt = new Map(); hand.forEach(c => cnt.set(c, (cnt.get(c) || 0) + 1));
  const vals = [...cnt.keys()].sort((a, b) => a - b), groups = [];
  A.step(`Count the cards. The smallest remaining card must start a group of ${k}.`, A.hashTable('counts', cnt));
  for (const v of vals) {
    const c = cnt.get(v); if (!c) continue;
    for (let x = v; x < v + k; x++) { const have = cnt.get(x) || 0; if (have < c) { A.step(`${v} must start ${c} group${c > 1 ? 's' : ''}, but only ${have} card${have === 1 ? '' : 's'} of ${x} remain. Impossible.`, A.hashTable('counts', cnt, { hl: x }), A.text('Result', 'false', 'bad')); return; } cnt.set(x, have - c); }
    for (let g = 0; g < c; g++) groups.push(`[${[...Array(k)].map((_, t) => v + t)}]`);
    A.step(`Start ${c} group${c > 1 ? 's' : ''} at ${v}: ${[...Array(k)].map((_, t) => v + t).join(', ')}.`, A.hashTable('counts', cnt), A.arr('groups', groups));
  }
  A.step('Every card is in a group.', A.text('Result', 'true', 'ok'));
}
A.scenario('Possible', 'hand = [1,2,3,6,2,3,4,7,8], groupSize = 3', () => run([1, 2, 3, 6, 2, 3, 4, 7, 8], 3));
A.scenario('Impossible', 'hand = [1,2,3,4,5], groupSize = 4', () => run([1, 2, 3, 4, 5], 4));
'''),
]
