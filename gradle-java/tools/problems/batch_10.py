GRAPH_NODE = r'''
    /** Undirected graph node. */
    public static class Node {
        public int val;
        public List<Node> neighbors = new ArrayList<>();

        public Node(int val) { this.val = val; }
    }
'''

CLONE_TEST = r'''
class CloneGraphTest {

    private final CloneGraph solution = new CloneGraph();

    private static CloneGraph.Node build(int[][] adj) {
        if (adj.length == 0) return null;
        CloneGraph.Node[] nodes = new CloneGraph.Node[adj.length];
        for (int i = 0; i < adj.length; i++) nodes[i] = new CloneGraph.Node(i + 1);
        for (int i = 0; i < adj.length; i++) for (int j : adj[i]) nodes[i].neighbors.add(nodes[j - 1]);
        return nodes[0];
    }

    /** Collects nodes by value and checks the clone shares no node with the original. */
    private static Map<Integer, CloneGraph.Node> nodes(CloneGraph.Node start) {
        Map<Integer, CloneGraph.Node> seen = new TreeMap<>();
        Deque<CloneGraph.Node> stack = new ArrayDeque<>(List.of(start));
        while (!stack.isEmpty()) {
            CloneGraph.Node n = stack.pop();
            if (seen.putIfAbsent(n.val, n) == null) stack.addAll(n.neighbors);
        }
        return seen;
    }

    @Test
    void square() {
        int[][] adj = {{2, 4}, {1, 3}, {2, 4}, {1, 3}};
        CloneGraph.Node original = build(adj), copy = solution.cloneGraph(original);
        Map<Integer, CloneGraph.Node> a = nodes(original), b = nodes(copy);
        assertEquals(a.keySet(), b.keySet());
        for (int v : a.keySet()) {
            assertNotSame(a.get(v), b.get(v));
            assertEquals(a.get(v).neighbors.stream().map(x -> x.val).toList(), b.get(v).neighbors.stream().map(x -> x.val).toList());
            for (CloneGraph.Node nb : b.get(v).neighbors) assertSame(b.get(nb.val), nb);
        }
    }

    @Test
    void singleNodeAndEmpty() {
        assertEquals(1, solution.cloneGraph(new CloneGraph.Node(1)).val);
        assertNull(solution.cloneGraph(null));
    }
}
'''

PROBLEMS = [
P(num=133, slug="clone-graph", title="Clone Graph", diff="Medium", topic="Graph General", cls="CloneGraph",
idea="Map every original node to its copy the first time you see it; the map also stops cycles from looping forever.",
vname="BFS with a clone map",
spec=r'''
Given a reference to a node in a connected undirected graph, return a **deep copy** of the graph. Each node has an integer `val`
(1..n, unique) and a list of `neighbors`.

**Example**
```
Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]   (a square 1-2-3-4)
Output: an identical but separate graph
```

**Constraints**
* `0 <= n <= 100`; no repeated edges or self-loops; the graph is connected.
''',
approach=r'''
**BFS + `MyHashMap<original, copy>`.** Copy the start node and enqueue it. For each dequeued node, look at its neighbours: create a copy
the first time a neighbour is seen (and enqueue it), then add the neighbour's copy to the current copy's neighbour list.

* Time: **O(V + E)** — each node and edge is processed once.
* Space: **O(V)** — the map and the queue.
''',
tc="n", sc="n",
java=r'''
public class CloneGraph {
''' + GRAPH_NODE + r'''
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        MyHashMap<Node, Node> copyOf = new MyHashMap<>();
        copyOf.put(node, new Node(node.val));
        Deque<Node> queue = new ArrayDeque<>(List.of(node));
        while (!queue.isEmpty()) {
            Node cur = queue.poll();
            for (Node nb : cur.neighbors) {
                if (!copyOf.containsKey(nb)) {
                    copyOf.put(nb, new Node(nb.val));
                    queue.add(nb);
                }
                copyOf.get(cur).neighbors.add(copyOf.get(nb));
            }
        }
        return copyOf.get(node);
    }
}
''',
test=CLONE_TEST,
trace=r'''
function run(adj) {
  const N = adj.length, nodes = adj.map((_, i) => ({ id: i + 1, label: i + 1 }));
  const edges = []; adj.forEach((ns, i) => ns.forEach(j => i + 1 < j && edges.push([i + 1, j])));
  const copy = new Map(), copyEdges = [], q = [1];
  copy.set(1, "1'");
  const view = (cur, msg) => A.step(msg, A.graph('original', nodes, edges, { hl: Object.fromEntries([...copy.keys()].map(k => [k, k === cur ? 'cur' : 'ok'])) }), A.graph('copy', [...copy.keys()].map(k => ({ id: k, label: k + "'" })), copyEdges.map(([a, b]) => [a, b])), A.hashTable('original → copy', copy), A.arr('queue', q));
  view(1, "Copy node 1 and put it in the map. The map tells us whether a node has already been copied.");
  while (q.length) {
    const cur = q.shift();
    for (const nb of adj[cur - 1]) {
      const fresh = !copy.has(nb);
      if (fresh) { copy.set(nb, nb + "'"); q.push(nb); }
      if (!copyEdges.some(([a, b]) => (a === nb && b === cur))) copyEdges.push([cur, nb]);
      view(cur, fresh ? `Neighbour ${nb} of ${cur} has no copy yet: create ${nb}' and queue it. Link ${cur}' to ${nb}'.` : `Neighbour ${nb} already has a copy (found in the map). Just link ${cur}' to ${nb}'.`);
    }
  }
  A.step('The queue is empty. Every node and edge has been copied exactly once.', A.graph('copy', [...copy.keys()].map(k => ({ id: k, label: k + "'" })), copyEdges, { hl: Object.fromEntries([...copy.keys()].map(k => [k, 'ok'])) }));
}
A.scenario('Square graph', 'adjList = [[2,4],[1,3],[2,4],[1,3]]', () => run([[2, 4], [1, 3], [2, 4], [1, 3]]));
''',
variants=[dict(
name="Recursive DFS with a clone map",
idea="clone(node) returns the existing copy if there is one, otherwise copies the node and clones its neighbours.",
approach=r'''
**DFS + memo map.** Register the copy in the map **before** recursing into neighbours; that is what stops cycles.

* Time: **O(V + E)** — each node is copied once and each edge followed once.
* Space: **O(V)** — the map plus the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class CloneGraph {
''' + GRAPH_NODE + r'''
    private final MyHashMap<Node, Node> copyOf = new MyHashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) return null;
        Node existing = copyOf.get(node);
        if (existing != null) return existing;
        Node copy = new Node(node.val);
        copyOf.put(node, copy);
        for (Node nb : node.neighbors) copy.neighbors.add(cloneGraph(nb));
        return copy;
    }
}
''',
trace=r'''
function run(adj) {
  const nodes = adj.map((_, i) => ({ id: i + 1, label: i + 1 })), edges = [];
  adj.forEach((ns, i) => ns.forEach(j => i + 1 < j && edges.push([i + 1, j])));
  const copy = new Map(), stack = [];
  (function clone(v) {
    if (copy.has(v)) { A.step(`${v} is already in the map. Reuse ${v}' instead of recursing again.`, A.graph('original', nodes, edges, { hl: Object.fromEntries([...copy.keys()].map(k => [k, k === v ? 'alt' : 'ok'])) }), A.stack('call stack', stack)); return; }
    copy.set(v, v + "'"); stack.push(`clone(${v})`);
    A.step(`clone(${v}): create ${v}' and store it in the map before visiting the neighbours.`, A.graph('original', nodes, edges, { hl: Object.fromEntries([...copy.keys()].map(k => [k, k === v ? 'cur' : 'ok'])) }), A.hashTable('original → copy', copy), A.stack('call stack', stack));
    adj[v - 1].forEach(clone);
    stack.pop();
  })(1);
  A.step('All nodes are cloned.', A.hashTable('original → copy', copy));
}
A.scenario('Square graph', 'adjList = [[2,4],[1,3],[2,4],[1,3]]', () => run([[2, 4], [1, 3], [2, 4], [1, 3]]));
''')]),

P(num=399, slug="evaluate-division", title="Evaluate Division", diff="Medium", topic="Graph General", cls="EvaluateDivision",
idea="Each equation a / b = k is an edge a → b with weight k (and b → a with 1/k); a query is a path product.",
vname="Weighted graph + DFS",
spec=r'''
You are given equations `Ai / Bi = values[i]` between variables (strings). For each query `Cj / Dj`, return its value, or `-1.0` if it
cannot be determined. Variables that never appear in an equation are unknown (even `x / x` gives `-1.0`). There are no contradictions
or divisions by zero.

**Example**
```
Input:  equations = [["a","b"],["b","c"]], values = [2.0,3.0]
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.0, 0.5, -1.0, 1.0, -1.0]
```

**Constraints**
* `1 <= equations.length, queries.length <= 20`; `0 < values[i] <= 20`
''',
approach=r'''
**Graph search.** Build `MyHashMap<String, MyHashMap<String, Double>>` with an edge `a → b` of weight `k` and `b → a` of weight
`1/k`. For each query, DFS from `C` to `D` multiplying weights along the path, with a `MyHashSet` of visited variables.

* Time: **O(Q·(V + E))** — one graph search per query.
* Space: **O(V + E)** — the adjacency maps.
''',
tc="n2", sc="n",
java=r'''
public class EvaluateDivision {

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        MyHashMap<String, MyHashMap<String, Double>> graph = new MyHashMap<>();
        for (int i = 0; i < values.length; i++) {
            String a = equations.get(i).get(0), b = equations.get(i).get(1);
            graph.computeIfAbsent(a, k -> new MyHashMap<>()).put(b, values[i]);
            graph.computeIfAbsent(b, k -> new MyHashMap<>()).put(a, 1.0 / values[i]);
        }
        double[] out = new double[queries.size()];
        for (int i = 0; i < out.length; i++) {
            String c = queries.get(i).get(0), d = queries.get(i).get(1);
            out[i] = graph.containsKey(c) && graph.containsKey(d) ? dfs(graph, c, d, new MyHashSet<>()) : -1.0;
        }
        return out;
    }

    private double dfs(MyHashMap<String, MyHashMap<String, Double>> graph, String cur, String target, MyHashSet<String> seen) {
        if (cur.equals(target)) return 1.0;
        seen.add(cur);
        for (MyHashMap.Entry<String, Double> e : graph.get(cur).entries()) {
            if (seen.contains(e.getKey())) continue;
            double rest = dfs(graph, e.getKey(), target, seen);
            if (rest >= 0) return e.getValue() * rest;
        }
        return -1.0;
    }
}
''',
test=r'''
class EvaluateDivisionTest {

    private final EvaluateDivision solution = new EvaluateDivision();

    @Test
    void example() {
        double[] out = solution.calcEquation(
                List.of(List.of("a", "b"), List.of("b", "c")), new double[]{2.0, 3.0},
                List.of(List.of("a", "c"), List.of("b", "a"), List.of("a", "e"), List.of("a", "a"), List.of("x", "x")));
        assertArrayEquals(new double[]{6.0, 0.5, -1.0, 1.0, -1.0}, out, 1e-9);
    }

    @Test
    void disconnectedComponents() {
        double[] out = solution.calcEquation(
                List.of(List.of("a", "b"), List.of("c", "d")), new double[]{1.5, 2.5},
                List.of(List.of("a", "d"), List.of("d", "c")));
        assertArrayEquals(new double[]{-1.0, 0.4}, out, 1e-9);
    }
}
''',
trace=r'''
function run(eqs, vals, queries) {
  const vars = [...new Set(eqs.flat())], nodes = vars.map(v => ({ id: v, label: v }));
  const edges = eqs.map(([a, b], i) => [a, b, `×${vals[i]}`]);
  const g = new Map(); eqs.forEach(([a, b], i) => { (g.get(a) || g.set(a, new Map()).get(a)).set(b, vals[i]); (g.get(b) || g.set(b, new Map()).get(b)).set(a, 1 / vals[i]); });
  A.step('Each equation a / b = k becomes an edge a → b with weight k, and b → a with weight 1/k.', A.graph('variables', nodes, edges, { directed: true }));
  const out = [];
  for (const [c, d] of queries) {
    if (!g.has(c) || !g.has(d)) { out.push(-1); A.step(`${c} / ${d}: ${!g.has(c) ? c : d} never appears in an equation, so the answer is -1.`, A.graph('variables', nodes, edges, { directed: true }), A.arr('answers', out)); continue; }
    const seen = new Set(), path = [];
    const dfs = (cur, prod) => { if (cur === d) return prod; seen.add(cur); for (const [nx, w] of g.get(cur)) if (!seen.has(nx)) { path.push([cur, nx, w]); const r = dfs(nx, prod * w); if (r >= 0) return r; path.pop(); } return -1; };
    const r = dfs(c, 1); out.push(+r.toFixed(4));
    const hl = { [c]: 'cur', [d]: 'ok' }; path.forEach(([a, b]) => { hl[a] = hl[a] || 'sel'; hl[b] = hl[b] || 'sel'; });
    A.step(r < 0 ? `${c} / ${d}: no path connects them, so the answer is -1.` : `${c} / ${d}: follow the path ${[c, ...path.map(p => p[1])].join(' → ')} and multiply the weights: ${path.map(p => +p[2].toFixed(4)).join(' × ') || '1'} = ${+r.toFixed(4)}.`, A.graph('variables', nodes, edges.map(e => { const on = path.some(([a, b]) => (a === e[0] && b === e[1]) || (a === e[1] && b === e[0])); return [...e.slice(0, 3), on ? 'ok' : '']; }), { directed: true, hl }), A.arr('answers', out, { hl: { [out.length - 1]: r < 0 ? 'bad' : 'ok' } }));
  }
}
A.scenario('Chain a → b → c', 'a/b = 2, b/c = 3', () => run([['a', 'b'], ['b', 'c']], [2, 3], [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a']]));
''',
variants=[dict(
name="Weighted union-find",
idea="Keep each variable's ratio to its group root; two variables in the same group divide via their ratios.",
approach=r'''
**Union-find with weights.** `parent[x]` and `weight[x] = x / parent[x]`. `find` compresses paths and multiplies weights so each
variable stores its ratio to the root. For `a / b = k`, join the roots so the ratios stay consistent. A query `c / d` is
`weight[c] / weight[d]` when both share a root. Both maps are `MyHashMap`s.

* Time: **O((E + Q)·α(V))** — almost constant per operation thanks to path compression.
* Space: **O(V)** — the parent and weight maps.
''',
tc="n", sc="n",
java=r'''
public class EvaluateDivision {

    private final MyHashMap<String, String> parent = new MyHashMap<>();
    private final MyHashMap<String, Double> weight = new MyHashMap<>(); // x / parent(x)

    private String find(String x) {
        String p = parent.get(x);
        if (!p.equals(x)) {
            String root = find(p);
            weight.put(x, weight.get(x) * weight.get(p));
            parent.put(x, root);
        }
        return parent.get(x);
    }

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        for (int i = 0; i < values.length; i++) {
            String a = equations.get(i).get(0), b = equations.get(i).get(1);
            for (String v : List.of(a, b)) {
                if (!parent.containsKey(v)) { parent.put(v, v); weight.put(v, 1.0); }
            }
            String ra = find(a), rb = find(b);
            if (!ra.equals(rb)) {
                parent.put(ra, rb);
                weight.put(ra, values[i] * weight.get(b) / weight.get(a));
            }
        }
        double[] out = new double[queries.size()];
        for (int i = 0; i < out.length; i++) {
            String c = queries.get(i).get(0), d = queries.get(i).get(1);
            if (!parent.containsKey(c) || !parent.containsKey(d) || !find(c).equals(find(d))) out[i] = -1.0;
            else out[i] = weight.get(c) / weight.get(d);
        }
        return out;
    }
}
''',
trace=r'''
function run(eqs, vals, queries) {
  const par = new Map(), w = new Map();
  const find = x => { const p = par.get(x); if (p !== x) { const r = find(p); w.set(x, w.get(x) * w.get(p)); par.set(x, r); } return par.get(x); };
  const show = () => A.hashTable('parent (ratio to parent)', new Map([...par].map(([k, v]) => [k, `${v} ×${+w.get(k).toFixed(3)}`])));
  eqs.forEach(([a, b], i) => {
    [a, b].forEach(v => { if (!par.has(v)) { par.set(v, v); w.set(v, 1); } });
    const ra = find(a), rb = find(b);
    if (ra !== rb) { par.set(ra, rb); w.set(ra, vals[i] * w.get(b) / w.get(a)); }
    A.step(`${a} / ${b} = ${vals[i]}: join ${ra}'s group under ${rb}, with a ratio that keeps both equations true.`, show());
  });
  const out = queries.map(([c, d]) => (!par.has(c) || !par.has(d) || find(c) !== find(d) ? -1 : +(w.get(c) / w.get(d)).toFixed(4)));
  A.step('Each query divides the two variables’ ratios to their shared root.', show(), A.arr('answers', out));
}
A.scenario('Chain a → b → c', 'a/b = 2, b/c = 3', () => run([['a', 'b'], ['b', 'c']], [2, 3], [['a', 'c'], ['b', 'a'], ['a', 'e']]));
''')]),

P(num=207, slug="course-schedule", title="Course Schedule", diff="Medium", topic="Graph General", cls="CourseSchedule",
idea="Courses can all be finished exactly when the prerequisite graph has no cycle; peel off courses with no remaining prerequisites.",
vname="Kahn's topological sort",
spec=r'''
There are `numCourses` courses `0..numCourses-1`. `prerequisites[i] = [a, b]` means you must take `b` before `a`. Return `true` if
it is possible to finish all courses.

**Example 1**
```
Input:  numCourses = 2, prerequisites = [[1,0]]
Output: true
```

**Example 2**
```
Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false   (a cycle)
```

**Constraints**
* `1 <= numCourses <= 2000`; `0 <= prerequisites.length <= 5000`; pairs are unique.
''',
approach=r'''
**Kahn's algorithm.** Count each course's unmet prerequisites (in-degree). Queue every course with in-degree 0; when a course is
taken, decrement its dependants and queue any that reach 0. All courses are taken iff there is no cycle.

* Time: **O(V + E)** — each course and edge is processed once.
* Space: **O(V + E)** — the adjacency lists and the queue.
''',
tc="n", sc="n",
java=r'''
public class CourseSchedule {

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> next = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) next.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] p : prerequisites) {
            next.get(p[1]).add(p[0]);
            indegree[p[0]]++;
        }
        Deque<Integer> queue = new ArrayDeque<>();
        for (int c = 0; c < numCourses; c++) if (indegree[c] == 0) queue.add(c);
        int taken = 0;
        while (!queue.isEmpty()) {
            int c = queue.poll();
            taken++;
            for (int d : next.get(c)) {
                if (--indegree[d] == 0) queue.add(d);
            }
        }
        return taken == numCourses;
    }
}
''',
test=r'''
class CourseScheduleTest {

    private final CourseSchedule solution = new CourseSchedule();

    @Test
    void possible() {
        assertTrue(solution.canFinish(2, new int[][]{{1, 0}}));
        assertTrue(solution.canFinish(4, new int[][]{{1, 0}, {2, 0}, {3, 1}, {3, 2}}));
    }

    @Test
    void cycle() {
        assertFalse(solution.canFinish(2, new int[][]{{1, 0}, {0, 1}}));
        assertFalse(solution.canFinish(3, new int[][]{{0, 1}, {1, 2}, {2, 0}}));
    }

    @Test
    void noPrerequisites() {
        assertTrue(solution.canFinish(3, new int[][]{}));
    }
}
''',
trace=r'''
function run(n, pre) {
  const nodes = [...Array(n).keys()].map(i => ({ id: i, label: i })), edges = pre.map(([a, b]) => [b, a]);
  const indeg = new Array(n).fill(0), next = [...Array(n)].map(() => []);
  pre.forEach(([a, b]) => { next[b].push(a); indeg[a]++; });
  const q = [], done = {}; for (let i = 0; i < n; i++) if (!indeg[i]) q.push(i);
  A.step('An arrow b → a means b must come before a. In-degree counts each course’s unmet prerequisites.', A.graph('courses', nodes, edges, { directed: true }), A.arr('in-degree', indeg), A.arr('ready queue', q));
  let taken = 0;
  while (q.length) {
    const c = q.shift(); taken++; done[c] = 'ok';
    const freed = [];
    next[c].forEach(d => { if (--indeg[d] === 0) { q.push(d); freed.push(d); } });
    A.step(`Take course ${c}. ${next[c].length ? `Its dependants ${next[c].join(', ')} each lose a prerequisite${freed.length ? `; ${freed.join(', ')} ${freed.length > 1 ? 'are' : 'is'} now ready` : ''}.` : 'Nothing depends on it.'}`, A.graph('courses', nodes, edges.map(e => [...e, '', done[e[0]] ? 'ok' : '']), { directed: true, hl: { ...done, [c]: 'cur' } }), A.arr('in-degree', indeg), A.arr('ready queue', q), A.vars({ taken }));
  }
  const ok = taken === n;
  A.step(ok ? 'Every course was taken, so the schedule works.' : `Only ${taken} of ${n} courses could be taken. The rest are stuck in a cycle.`, A.graph('courses', nodes, edges, { directed: true, hl: Object.fromEntries(nodes.map(x => [x.id, done[x.id] ? 'ok' : 'bad'])) }), A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('Diamond (possible)', 'n = 4, [[1,0],[2,0],[3,1],[3,2]]', () => run(4, [[1, 0], [2, 0], [3, 1], [3, 2]]));
A.scenario('Cycle (impossible)', 'n = 4, [[1,0],[2,1],[3,2],[1,3]]', () => run(4, [[1, 0], [2, 1], [3, 2], [1, 3]]));
''',
variants=[dict(
name="DFS cycle detection",
idea="Colour courses white, grey (on the current DFS path) and black (done); reaching a grey course means a cycle.",
approach=r'''
**Three-colour DFS.** Start a DFS from every unvisited course. Mark it grey on entry and black on exit. An edge into a grey course
closes a cycle.

* Time: **O(V + E)** — each course and edge is explored once.
* Space: **O(V + E)** — the adjacency lists and the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class CourseSchedule {

    private List<List<Integer>> next;
    private int[] state; // 0 = unvisited, 1 = on the current path, 2 = done

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        next = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) next.add(new ArrayList<>());
        for (int[] p : prerequisites) next.get(p[1]).add(p[0]);
        state = new int[numCourses];
        for (int c = 0; c < numCourses; c++) {
            if (hasCycle(c)) return false;
        }
        return true;
    }

    private boolean hasCycle(int c) {
        if (state[c] == 1) return true;
        if (state[c] == 2) return false;
        state[c] = 1;
        for (int d : next.get(c)) {
            if (hasCycle(d)) return true;
        }
        state[c] = 2;
        return false;
    }
}
''',
trace=r'''
function run(n, pre) {
  const nodes = [...Array(n).keys()].map(i => ({ id: i, label: i })), edges = pre.map(([a, b]) => [b, a]);
  const next = [...Array(n)].map(() => []); pre.forEach(([a, b]) => next[b].push(a));
  const st = new Array(n).fill(0), cls = () => Object.fromEntries(st.map((s, i) => [i, s === 1 ? 'cur' : s === 2 ? 'ok' : '']));
  let cyc = false;
  const dfs = c => {
    if (st[c] === 1) { cyc = true; A.step(`Reached ${c}, which is still on the current path (orange). That is a cycle.`, A.graph('courses', nodes, edges, { directed: true, hl: { ...cls(), [c]: 'bad' } })); return true; }
    if (st[c] === 2) return false;
    st[c] = 1; A.step(`Enter ${c}: mark it as on the current path.`, A.graph('courses', nodes, edges, { directed: true, hl: cls() }));
    for (const d of next[c]) if (dfs(d)) return true;
    st[c] = 2; A.step(`Leave ${c}: everything after it is cycle-free, so mark it done.`, A.graph('courses', nodes, edges, { directed: true, hl: cls() }));
    return false;
  };
  for (let c = 0; c < n && !cyc; c++) dfs(c);
  A.step(cyc ? 'There is a cycle, so the courses cannot all be finished.' : 'No cycle, so all courses can be finished.', A.text('Result', String(!cyc), cyc ? 'bad' : 'ok'));
}
A.scenario('Cycle (impossible)', 'n = 4, [[1,0],[2,1],[3,2],[1,3]]', () => run(4, [[1, 0], [2, 1], [3, 2], [1, 3]]));
''')]),

P(num=210, slug="course-schedule-ii", title="Course Schedule II", diff="Medium", topic="Graph General", cls="CourseScheduleII",
idea="Kahn's algorithm produces a valid order directly: the order in which courses become ready.",
vname="Kahn's topological sort",
spec=r'''
Same setup as Course Schedule: `prerequisites[i] = [a, b]` means `b` before `a`. Return **an ordering** of all courses that respects
every prerequisite, or an empty array if impossible. Any valid order is accepted.

**Example 1**
```
Input:  numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
```

**Example 2**
```
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
```

**Constraints**
* `1 <= numCourses <= 2000`; pairs are unique.
''',
approach=r'''
**Kahn's algorithm, recording the order.** Repeatedly take a course with in-degree 0, append it to the answer, and decrement its
dependants. If fewer than `numCourses` were taken, there is a cycle: return `[]`.

* Time: **O(V + E)** — each course and edge is processed once.
* Space: **O(V + E)** — adjacency lists, in-degrees, the queue.
''',
tc="n", sc="n",
java=r'''
public class CourseScheduleII {

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> next = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) next.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] p : prerequisites) {
            next.get(p[1]).add(p[0]);
            indegree[p[0]]++;
        }
        Deque<Integer> queue = new ArrayDeque<>();
        for (int c = 0; c < numCourses; c++) if (indegree[c] == 0) queue.add(c);
        int[] order = new int[numCourses];
        int taken = 0;
        while (!queue.isEmpty()) {
            int c = queue.poll();
            order[taken++] = c;
            for (int d : next.get(c)) {
                if (--indegree[d] == 0) queue.add(d);
            }
        }
        return taken == numCourses ? order : new int[0];
    }
}
''',
test=r'''
class CourseScheduleIITest {

    private final CourseScheduleII solution = new CourseScheduleII();

    private static void assertValid(int n, int[][] pre, int[] order) {
        assertEquals(n, order.length);
        int[] pos = new int[n];
        for (int i = 0; i < n; i++) pos[order[i]] = i;
        for (int[] p : pre) assertTrue(pos[p[1]] < pos[p[0]], "prerequisite order violated");
    }

    @Test
    void diamond() {
        int[][] pre = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};
        assertValid(4, pre, solution.findOrder(4, pre));
    }

    @Test
    void cycle() {
        assertArrayEquals(new int[0], solution.findOrder(2, new int[][]{{1, 0}, {0, 1}}));
    }

    @Test
    void single() {
        assertArrayEquals(new int[]{0}, solution.findOrder(1, new int[][]{}));
    }
}
''',
trace=r'''
function run(n, pre) {
  const nodes = [...Array(n).keys()].map(i => ({ id: i, label: i })), edges = pre.map(([a, b]) => [b, a]);
  const indeg = new Array(n).fill(0), next = [...Array(n)].map(() => []);
  pre.forEach(([a, b]) => { next[b].push(a); indeg[a]++; });
  const q = [], order = [], done = {}; for (let i = 0; i < n; i++) if (!indeg[i]) q.push(i);
  A.step('Courses with no prerequisites are ready. The order in which courses become ready is a valid schedule.', A.graph('courses', nodes, edges, { directed: true }), A.arr('in-degree', indeg), A.arr('ready', q));
  while (q.length) {
    const c = q.shift(); order.push(c); done[c] = 'ok';
    next[c].forEach(d => { if (--indeg[d] === 0) q.push(d); });
    A.step(`Take ${c}; its dependants lose a prerequisite.`, A.graph('courses', nodes, edges, { directed: true, hl: { ...done, [c]: 'cur' } }), A.arr('in-degree', indeg), A.arr('ready', q), A.arr('order', order, { hl: { [order.length - 1]: 'ok' } }));
  }
  A.step(order.length === n ? `Order: [${order}].` : 'A cycle blocks some courses, so the answer is [].', A.text('Result', JSON.stringify(order.length === n ? order : []), order.length === n ? 'ok' : 'bad'));
}
A.scenario('Diamond', 'n = 4, [[1,0],[2,0],[3,1],[3,2]]', () => run(4, [[1, 0], [2, 0], [3, 1], [3, 2]]));
A.scenario('Six courses', 'n = 6, [[2,0],[2,1],[3,2],[4,2],[5,3],[5,4]]', () => run(6, [[2, 0], [2, 1], [3, 2], [4, 2], [5, 3], [5, 4]]));
'''),

P(num=909, slug="snakes-and-ladders", title="Snakes and Ladders", diff="Medium", topic="Graph BFS", cls="SnakesAndLadders",
idea="Each square is a node with edges to the next six squares (after following a snake or ladder); BFS finds the fewest rolls.",
vname="BFS over squares",
spec=r'''
An `n × n` board is numbered `1..n²` in a **boustrophedon** pattern starting at the bottom-left (row direction alternates). From
square `cur`, a die roll moves you to any of `cur+1 .. min(cur+6, n²)`. If that square has `board[r][c] != -1`, you must take the
snake or ladder to that square (only one per move). Return the fewest rolls to reach `n²`, or `-1`.

**Example**
```
Input:  board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],
                 [-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
```

**Constraints**
* `2 <= n <= 20`; squares 1 and n² have no snake or ladder.
''',
approach=r'''
**BFS.** Convert a square number to `(row, col)`: `row = n - 1 - (s - 1) / n`, `col = (s - 1) % n`, mirrored on every other row.
BFS from square 1; neighbours are the next six squares after following any snake or ladder. The first time `n²` is dequeued gives the
minimum number of rolls.

* Time: **O(n²)** — each square is visited once with six edges.
* Space: **O(n²)** — the distance array.
''',
tc="n2", sc="n2",
java=r'''
public class SnakesAndLadders {

    public int snakesAndLadders(int[][] board) {
        int n = board.length, target = n * n;
        int[] dist = new int[target + 1];
        Arrays.fill(dist, -1);
        dist[1] = 0;
        Deque<Integer> queue = new ArrayDeque<>(List.of(1));
        while (!queue.isEmpty()) {
            int s = queue.poll();
            if (s == target) return dist[s];
            for (int next = s + 1; next <= Math.min(s + 6, target); next++) {
                int r = n - 1 - (next - 1) / n, c = (next - 1) % n;
                if ((n - 1 - r) % 2 == 1) c = n - 1 - c;
                int dest = board[r][c] == -1 ? next : board[r][c];
                if (dist[dest] == -1) {
                    dist[dest] = dist[s] + 1;
                    queue.add(dest);
                }
            }
        }
        return -1;
    }
}
''',
test=r'''
class SnakesAndLaddersTest {

    private final SnakesAndLadders solution = new SnakesAndLadders();

    @Test
    void example() {
        int[][] board = {
            {-1, -1, -1, -1, -1, -1}, {-1, -1, -1, -1, -1, -1}, {-1, -1, -1, -1, -1, -1},
            {-1, 35, -1, -1, 13, -1}, {-1, -1, -1, -1, -1, -1}, {-1, 15, -1, -1, -1, -1}};
        assertEquals(4, solution.snakesAndLadders(board));
    }

    @Test
    void small() {
        assertEquals(1, solution.snakesAndLadders(new int[][]{{-1, -1}, {-1, 3}}));
    }

    @Test
    void plainBoard() {
        assertEquals(2, solution.snakesAndLadders(new int[][]{{-1, -1, -1}, {-1, -1, -1}, {-1, -1, -1}}));
    }
}
''',
trace=r'''
function run(board) {
  const n = board.length, T = n * n, pos = s => { const r = n - 1 - Math.floor((s - 1) / n); let c = (s - 1) % n; if ((n - 1 - r) % 2) c = n - 1 - c; return [r, c]; };
  const label = board.map(r => r.slice());
  for (let s = 1; s <= T; s++) { const [r, c] = pos(s); label[r][c] = board[r][c] === -1 ? s : `${s}→${board[r][c]}`; }
  const dist = new Array(T + 1).fill(-1); dist[1] = 0; let q = [1];
  const hl = () => { const o = []; for (let s = 1; s <= T; s++) if (dist[s] >= 0) { const [r, c] = pos(s); o.push([`${r},${c}`, dist[s] === 0 ? 'cur' : 'ok']); } return o; };
  A.step('Squares are numbered from the bottom-left, snaking back and forth. "a→b" marks a snake or ladder. Breadth-first search from square 1.', A.grid('board', label, { hl: hl() }));
  while (q.length) {
    const nq = [];
    for (const s of q) for (let nx = s + 1; nx <= Math.min(s + 6, T); nx++) { const [r, c] = pos(nx); const d = board[r][c] === -1 ? nx : board[r][c]; if (dist[d] === -1) { dist[d] = dist[s] + 1; nq.push(d); } }
    if (!nq.length) break;
    const rolls = dist[nq[0]];
    A.step(`After ${rolls} roll${rolls > 1 ? 's' : ''} we can stand on squares ${nq.sort((a, b) => a - b).join(', ')}.${dist[T] >= 0 ? ` That includes square ${T}.` : ''}`, A.grid('board', label, { hl: hl() }), A.vars({ rolls }));
    if (dist[T] >= 0) break;
    q = nq;
  }
  A.step(dist[T] >= 0 ? `The minimum number of rolls is ${dist[T]}.` : 'The last square is unreachable.', A.text('Result', dist[T], dist[T] >= 0 ? 'ok' : 'bad'));
}
A.scenario('4 × 4 board', 'a ladder 2 → 15 and a snake 14 → 3', () => run([[-1, -1, -1, -1], [-1, 3, -1, -1], [-1, -1, -1, -1], [-1, 15, -1, -1]]));
'''),

P(num=433, slug="minimum-genetic-mutation", title="Minimum Genetic Mutation", diff="Medium", topic="Graph BFS", cls="MinimumGeneticMutation",
idea="Genes are nodes; one-letter changes that land in the bank are edges; BFS gives the fewest mutations.",
vname="BFS over gene strings",
spec=r'''
A gene is an 8-character string over `A, C, G, T`. A mutation changes one character, and every intermediate gene must be in `bank`.
Return the minimum number of mutations from `startGene` to `endGene`, or `-1` if impossible. `startGene` may not be in the bank.

**Example**
```
Input:  startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
```

**Constraints**
* `0 <= bank.length <= 10`; all strings have length 8.
''',
approach=r'''
**BFS.** Put the bank in a `MyHashSet`. From each gene, try all `8 × 3` single-letter changes; any change that is in the bank and not
yet visited joins the next level.

* Time: **O(B·L·4)** — each bank gene is expanded once, trying 4 letters at each of L = 8 positions.
* Space: **O(B)** — the bank set and the queue.
''',
tc="n", sc="n",
java=r'''
public class MinimumGeneticMutation {

    public int minMutation(String startGene, String endGene, String[] bank) {
        MyHashSet<String> valid = new MyHashSet<>();
        for (String g : bank) valid.add(g);
        if (!valid.contains(endGene)) return -1;
        MyHashSet<String> seen = new MyHashSet<>();
        seen.add(startGene);
        Deque<String> queue = new ArrayDeque<>(List.of(startGene));
        for (int steps = 0; !queue.isEmpty(); steps++) {
            for (int size = queue.size(); size > 0; size--) {
                String g = queue.poll();
                if (g.equals(endGene)) return steps;
                char[] chars = g.toCharArray();
                for (int i = 0; i < chars.length; i++) {
                    char original = chars[i];
                    for (char c : "ACGT".toCharArray()) {
                        chars[i] = c;
                        String next = new String(chars);
                        if (valid.contains(next) && seen.add(next)) queue.add(next);
                    }
                    chars[i] = original;
                }
            }
        }
        return -1;
    }
}
''',
test=r'''
class MinimumGeneticMutationTest {

    private final MinimumGeneticMutation solution = new MinimumGeneticMutation();

    @Test
    void one() {
        assertEquals(1, solution.minMutation("AACCGGTT", "AACCGGTA", new String[]{"AACCGGTA"}));
    }

    @Test
    void two() {
        assertEquals(2, solution.minMutation("AACCGGTT", "AAACGGTA", new String[]{"AACCGGTA", "AACCGCTA", "AAACGGTA"}));
    }

    @Test
    void impossible() {
        assertEquals(-1, solution.minMutation("AAAAAAAA", "CCCCCCCC", new String[]{"AAAAAAAC", "CCCCCCCC"}));
        assertEquals(-1, solution.minMutation("AACCGGTT", "AACCGGTA", new String[]{}));
    }
}
''',
trace=r'''
function run(start, end, bank) {
  const valid = new Set(bank), seen = new Set([start]);
  const nodes = [start, ...bank.filter(b => b !== start)].map(g => ({ id: g, label: g.slice(0, 4) + '…' }));
  const diff1 = (a, b) => [...a].filter((c, i) => c !== b[i]).length === 1;
  const all = [start, ...bank];
  const edges = []; all.forEach((a, i) => all.forEach((b, j) => i < j && diff1(a, b) && edges.push([a, b])));
  A.step('Genes are nodes; genes one letter apart are connected. Only genes in the bank may be used.', A.graph('mutation graph', nodes, edges, { hl: { [start]: 'cur', [end]: 'alt' } }), A.hashTable('bank (MyHashSet)', valid));
  let q = [start], steps = 0;
  while (q.length) {
    if (q.includes(end)) { A.step(`Reached ${end} after ${steps} mutation${steps === 1 ? '' : 's'}.`, A.graph('mutation graph', nodes, edges, { hl: Object.fromEntries([...seen].map(g => [g, g === end ? 'ok' : 'sel'])) }), A.text('Result', steps, 'ok')); return; }
    const nq = [];
    for (const g of q) for (let i = 0; i < 8; i++) for (const c of 'ACGT') { const nx = g.slice(0, i) + c + g.slice(i + 1); if (valid.has(nx) && !seen.has(nx)) { seen.add(nx); nq.push(nx); } }
    steps++;
    A.step(nq.length ? `Mutation ${steps}: one letter away, in the bank and unseen: ${nq.join(', ')}.` : 'No new genes can be reached.', A.graph('mutation graph', nodes, edges, { hl: Object.fromEntries([...seen].map(g => [g, nq.includes(g) ? 'cur' : 'sel'])) }), A.arr('level', nq));
    q = nq;
  }
  A.step('The target cannot be reached.', A.text('Result', -1, 'bad'));
}
A.scenario('Two mutations', 'AACCGGTT → AAACGGTA', () => run('AACCGGTT', 'AAACGGTA', ['AACCGGTA', 'AACCGCTA', 'AAACGGTA']));
'''),

P(num=127, slug="word-ladder", title="Word Ladder", diff="Hard", topic="Graph BFS", cls="WordLadder",
idea="Search outward from both ends at once; the frontiers meet in the middle after far fewer expansions.",
vname="Bidirectional BFS",
spec=r'''
A **transformation sequence** from `beginWord` to `endWord` changes one letter at a time, and every word after the first must be in
`wordList`. Return the number of words in the **shortest** such sequence, or `0` if none exists.

**Example 1**
```
Input:  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5   (hit → hot → dot → dog → cog)
```

**Example 2**
```
Input:  same, but without "cog"
Output: 0
```

**Constraints**
* `1 <= beginWord.length <= 10`; `1 <= wordList.length <= 5000`; lowercase letters.
''',
approach=r'''
**Bidirectional BFS.** Keep two frontier sets, from the start and from the end, in `MyHashSet`s. Always expand the **smaller**
frontier by trying every one-letter change; if a change lands in the other frontier, the ladders meet. Expanding the smaller side
keeps the number of generated words low.

* Time: **O(N·L·26)** — each word is expanded at most once, trying 26 letters at each of L positions.
* Space: **O(N)** — the word set and the frontiers.
''',
tc="n", sc="n",
java=r'''
public class WordLadder {

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        MyHashSet<String> words = new MyHashSet<>();
        for (String w : wordList) words.add(w);
        if (!words.contains(endWord)) return 0;
        MyHashSet<String> front = new MyHashSet<>(), back = new MyHashSet<>();
        front.add(beginWord);
        back.add(endWord);
        words.remove(beginWord);
        words.remove(endWord);
        for (int length = 2; !front.isEmpty(); length++) {
            if (front.size() > back.size()) {
                MyHashSet<String> t = front; front = back; back = t;
            }
            MyHashSet<String> next = new MyHashSet<>();
            for (String w : front) {
                char[] chars = w.toCharArray();
                for (int i = 0; i < chars.length; i++) {
                    char original = chars[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        chars[i] = c;
                        String candidate = new String(chars);
                        if (back.contains(candidate)) return length;
                        if (words.remove(candidate)) next.add(candidate);
                    }
                    chars[i] = original;
                }
            }
            front = next;
        }
        return 0;
    }
}
''',
test=r'''
class WordLadderTest {

    private final WordLadder solution = new WordLadder();

    @Test
    void reachable() {
        assertEquals(5, solution.ladderLength("hit", "cog", List.of("hot", "dot", "dog", "lot", "log", "cog")));
    }

    @Test
    void endMissing() {
        assertEquals(0, solution.ladderLength("hit", "cog", List.of("hot", "dot", "dog", "lot", "log")));
    }

    @Test
    void oneStep() {
        assertEquals(2, solution.ladderLength("a", "c", List.of("a", "b", "c")));
    }
}
''',
trace=r'''
function run(begin, end, list) {
  const all = [begin, ...list.filter(w => w !== begin)], nodes = all.map(w => ({ id: w, label: w }));
  const d1 = (a, b) => [...a].filter((c, i) => c !== b[i]).length === 1;
  const edges = []; all.forEach((a, i) => all.forEach((b, j) => i < j && d1(a, b) && edges.push([a, b])));
  const words = new Set(list); words.delete(begin); words.delete(end);
  let front = new Set([begin]), back = new Set([end]); const fromStart = new Set([begin]), fromEnd = new Set([end]);
  const hl = () => Object.fromEntries([...fromStart].map(w => [w, 'sel']).concat([...fromEnd].map(w => [w, 'alt'])));
  A.step('Search from both ends at once: blue grows from the start, purple from the end.', A.graph('word graph', nodes, edges, { hl: hl() }));
  for (let len = 2; front.size; len++) {
    let swapped = false;
    if (front.size > back.size) { [front, back] = [back, front]; swapped = true; }
    const startSide = fromStart.has([...front][0]);
    const next = new Set();
    for (const w of front) for (let i = 0; i < w.length; i++) for (let c = 97; c < 123; c++) {
      const cand = w.slice(0, i) + String.fromCharCode(c) + w.slice(i + 1);
      if (back.has(cand)) { A.step(`${w} is one letter from ${cand}, which the other search already reached. The searches meet. The ladder has ${len} words.`, A.graph('word graph', nodes, edges, { hl: { ...hl(), [w]: 'ok', [cand]: 'ok' } }), A.text('Result', len, 'ok')); return; }
      if (words.has(cand)) { words.delete(cand); next.add(cand); (startSide ? fromStart : fromEnd).add(cand); }
    }
    A.step(`Expand the smaller frontier, from the ${startSide ? 'start' : 'end'} side${swapped ? ' (swapped)' : ''}: it reaches ${[...next].join(', ') || 'nothing new'}.`, A.graph('word graph', nodes, edges, { hl: hl() }));
    front = next;
  }
  A.step('The frontiers never met, so the answer is 0.', A.text('Result', 0, 'bad'));
}
A.scenario('hit → cog', 'wordList = [hot,dot,dog,lot,log,cog]', () => run('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']));
''',
variants=[dict(
name="One-directional BFS",
idea="BFS from the begin word, one level per transformation, until the end word appears.",
approach=r'''
**Plain BFS.** Level by level, generate every one-letter change of every word in the queue; keep those in the word set (removing
them to mark as visited).

* Time: **O(N·L·26)** — each word is dequeued once.
* Space: **O(N)** — the word set and the queue.
''',
tc="n", sc="n",
java=r'''
public class WordLadder {

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        MyHashSet<String> words = new MyHashSet<>();
        for (String w : wordList) words.add(w);
        if (!words.contains(endWord)) return 0;
        Deque<String> queue = new ArrayDeque<>(List.of(beginWord));
        for (int length = 1; !queue.isEmpty(); length++) {
            for (int size = queue.size(); size > 0; size--) {
                String w = queue.poll();
                if (w.equals(endWord)) return length;
                char[] chars = w.toCharArray();
                for (int i = 0; i < chars.length; i++) {
                    char original = chars[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        chars[i] = c;
                        String candidate = new String(chars);
                        if (words.remove(candidate)) queue.add(candidate);
                    }
                    chars[i] = original;
                }
            }
        }
        return 0;
    }
}
''',
trace=r'''
function run(begin, end, list) {
  const all = [begin, ...list.filter(w => w !== begin)], nodes = all.map(w => ({ id: w, label: w }));
  const d1 = (a, b) => [...a].filter((c, i) => c !== b[i]).length === 1;
  const edges = []; all.forEach((a, i) => all.forEach((b, j) => i < j && d1(a, b) && edges.push([a, b])));
  const words = new Set(list), seen = { [begin]: 'cur' }; let q = [begin];
  for (let len = 1; q.length; len++) {
    if (q.includes(end)) { A.step(`Reached ${end}: the ladder has ${len} words.`, A.graph('word graph', nodes, edges, { hl: { ...seen, [end]: 'ok' } }), A.text('Result', len, 'ok')); return; }
    const nq = [];
    for (const w of q) for (let i = 0; i < w.length; i++) for (let c = 97; c < 123; c++) { const cand = w.slice(0, i) + String.fromCharCode(c) + w.slice(i + 1); if (words.has(cand)) { words.delete(cand); nq.push(cand); seen[cand] = 'sel'; } }
    A.step(`Level ${len + 1}: ${nq.join(', ') || 'nothing new'}.`, A.graph('word graph', nodes, edges, { hl: seen }));
    q = nq;
  }
  A.step('Not reachable.', A.text('Result', 0, 'bad'));
}
A.scenario('hit → cog', 'wordList = [hot,dot,dog,lot,log,cog]', () => run('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']));
''')]),

P(num=208, slug="implement-trie-prefix-tree", title="Implement Trie (Prefix Tree)", diff="Medium", topic="Trie", cls="Trie",
idea="Each node has 26 child slots; a word is a path from the root, with an end-of-word flag on its last node.",
vname="Array-of-children trie",
spec=r'''
Implement a **trie** (prefix tree) of lowercase words:
* `insert(word)`
* `search(word)`: `true` if `word` was inserted
* `startsWith(prefix)`: `true` if some inserted word starts with `prefix`

**Example**
```
insert("apple"); search("apple") → true; search("app") → false;
startsWith("app") → true; insert("app"); search("app") → true
```

**Constraints**
* `1 <= word.length, prefix.length <= 2000`; at most `3 * 10^4` calls.
''',
approach=r'''
**Fixed child arrays.** Each node holds `Node[26] children` and a boolean `end`. `insert` walks the letters, creating missing nodes,
and marks the last node. `search` and `startsWith` walk the same path; `search` also needs `end`.

* Time: **O(L)** — per operation, L being the word length.
* Space: **O(total letters)** — at most one node per inserted letter.
''',
tc="n", sc="n",
java=r'''
public class Trie {

    private static final class Node {
        final Node[] children = new Node[26];
        boolean end;
    }

    private final Node root = new Node();

    public void insert(String word) {
        Node n = root;
        for (char c : word.toCharArray()) {
            int i = c - 'a';
            if (n.children[i] == null) n.children[i] = new Node();
            n = n.children[i];
        }
        n.end = true;
    }

    public boolean search(String word) {
        Node n = walk(word);
        return n != null && n.end;
    }

    public boolean startsWith(String prefix) {
        return walk(prefix) != null;
    }

    private Node walk(String s) {
        Node n = root;
        for (char c : s.toCharArray()) {
            n = n.children[c - 'a'];
            if (n == null) return null;
        }
        return n;
    }
}
''',
test=r'''
class TrieTest {

    @Test
    void example() {
        Trie t = new Trie();
        t.insert("apple");
        assertTrue(t.search("apple"));
        assertFalse(t.search("app"));
        assertTrue(t.startsWith("app"));
        t.insert("app");
        assertTrue(t.search("app"));
        assertFalse(t.startsWith("b"));
    }
}
''',
trace=r'''
A.scenario('apple, app, apt', 'insert apple, app, apt · search · startsWith', () => {
  let seq = 0; const root = { val: '•', left: null, right: null, id: seq++, kids: {} };
  const draw = () => { const nodes = [], edges = []; (function walk(n) { nodes.push({ id: n.id, label: n.val + (n.end ? '✓' : '') }); Object.keys(n.kids).sort().forEach(k => { edges.push([n.id, n.kids[k].id, '']); walk(n.kids[k]); }); })(root); return { nodes, edges }; };
  const place = () => { const pos = {}; let x = 0; (function walk(n, d) { const ks = Object.keys(n.kids).sort(); if (!ks.length) { pos[n.id] = [40 + x * 58, 30 + d * 62]; x++; return; } ks.forEach(k => walk(n.kids[k], d + 1)); const xs = ks.map(k => pos[n.kids[k].id][0]); pos[n.id] = [(Math.min(...xs) + Math.max(...xs)) / 2, 30 + d * 62]; })(root, 0); return pos; };
  const view = (hl, msg, extra) => { const { nodes, edges } = draw(), pos = place(); A.step(msg, A.graph('trie', nodes.map(n => ({ ...n, x: pos[n.id][0], y: pos[n.id][1] })), edges, { hl, directed: true }), ...(extra || [])); };
  view({}, 'An empty trie is just the root.');
  for (const w of ['apple', 'app', 'apt']) {
    let n = root; const path = {};
    for (const c of w) { const fresh = !n.kids[c]; if (fresh) n.kids[c] = { val: c, id: seq++, kids: {} }; n = n.kids[c]; path[n.id] = fresh ? 'ok' : 'sel'; }
    n.end = true;
    view(path, `insert("${w}"): follow existing letters (blue) and create new nodes (green). Mark the last node as the end of a word (✓).`);
  }
  const walk = s => { let n = root; const p = {}; for (const c of s) { n = n.kids[c]; if (!n) return [null, p]; p[n.id] = 'cur'; } return [n, p]; };
  for (const [op, s] of [['search', 'app'], ['search', 'ap'], ['startsWith', 'ap'], ['search', 'bat']]) {
    const [n, p] = walk(s);
    const r = op === 'search' ? !!(n && n.end) : !!n;
    view(p, `${op}("${s}"): ${!n ? 'the path breaks off, so false' : op === 'search' ? (n.end ? 'the path exists and ends at a ✓ node, so true' : 'the path exists but its last node has no ✓, so false') : 'the path exists, so true'}.`, [A.text('Result', String(r), r ? 'ok' : 'bad')]);
  }
});
'''),

P(num=211, slug="design-add-and-search-words-data-structure", title="Design Add and Search Words Data Structure", diff="Medium", topic="Trie", cls="WordDictionary",
idea="A trie handles exact letters directly; a '.' wildcard branches into every existing child.",
vname="Trie with wildcard DFS",
spec=r'''
Design `WordDictionary`:
* `addWord(word)`: add a lowercase word;
* `search(word)`: `true` if any added word matches, where `.` matches **any one letter**.

**Example**
```
addWord("bad"); addWord("dad"); addWord("mad");
search("pad") → false; search("bad") → true; search(".ad") → true; search("b..") → true
```

**Constraints**
* `1 <= word.length <= 25`; at most 2 dots per search; at most `10^4` calls.
''',
approach=r'''
**Trie + DFS.** Insert as in a normal trie. `search(i, node)`: for a letter follow that child; for `.` try every non-null child
recursively. Succeed at the end only if the node marks a word end.

* Time: **O(L)** — per add; search is O(26^d · L) with d dots (here at most 2).
* Space: **O(total letters)** — the trie nodes.
''',
tc="n", sc="n",
java=r'''
public class WordDictionary {

    private static final class Node {
        final Node[] children = new Node[26];
        boolean end;
    }

    private final Node root = new Node();

    public void addWord(String word) {
        Node n = root;
        for (char c : word.toCharArray()) {
            int i = c - 'a';
            if (n.children[i] == null) n.children[i] = new Node();
            n = n.children[i];
        }
        n.end = true;
    }

    public boolean search(String word) {
        return search(word, 0, root);
    }

    private boolean search(String word, int i, Node n) {
        if (i == word.length()) return n.end;
        char c = word.charAt(i);
        if (c == '.') {
            for (Node child : n.children) {
                if (child != null && search(word, i + 1, child)) return true;
            }
            return false;
        }
        Node child = n.children[c - 'a'];
        return child != null && search(word, i + 1, child);
    }
}
''',
test=r'''
class WordDictionaryTest {

    @Test
    void example() {
        WordDictionary d = new WordDictionary();
        d.addWord("bad");
        d.addWord("dad");
        d.addWord("mad");
        assertFalse(d.search("pad"));
        assertTrue(d.search("bad"));
        assertTrue(d.search(".ad"));
        assertTrue(d.search("b.."));
        assertFalse(d.search("b."));
        assertFalse(d.search("...."));
    }
}
''',
trace=r'''
A.scenario('bad, dad, mad', 'addWord bad, dad, mad · search .ad, b.., pad', () => {
  let seq = 0; const root = { val: '•', id: seq++, kids: {} };
  const draw = () => { const nodes = [], edges = [], pos = {}; let x = 0; (function walk(n, d) { nodes.push(n); const ks = Object.keys(n.kids).sort(); ks.forEach(k => { edges.push([n.id, n.kids[k].id, '']); walk(n.kids[k], d + 1); }); if (!ks.length) { pos[n.id] = [40 + x * 58, 30 + d * 62]; x++; } else { const xs = ks.map(k => pos[n.kids[k].id][0]); pos[n.id] = [(Math.min(...xs) + Math.max(...xs)) / 2, 30 + d * 62]; } })(root, 0); return [nodes.map(n => ({ id: n.id, label: n.val + (n.end ? '✓' : ''), x: pos[n.id][0], y: pos[n.id][1] })), edges]; };
  const view = (hl, msg, ex = []) => { const [nodes, edges] = draw(); A.step(msg, A.graph('trie', nodes, edges, { hl, directed: true }), ...ex); };
  for (const w of ['bad', 'dad', 'mad']) { let n = root; for (const c of w) { if (!n.kids[c]) n.kids[c] = { val: c, id: seq++, kids: {} }; n = n.kids[c]; } n.end = true; }
  view({}, 'The trie after adding bad, dad and mad.');
  for (const q of ['.ad', 'b..', 'pad']) {
    const tried = {};
    const dfs = (i, n) => { if (i === q.length) return !!n.end; const c = q[i]; const kids = c === '.' ? Object.values(n.kids) : n.kids[c] ? [n.kids[c]] : []; for (const k of kids) { tried[k.id] = 'sel'; if (dfs(i + 1, k)) { tried[k.id] = 'ok'; return true; } tried[k.id] = 'bad'; } return false; };
    const r = dfs(0, root);
    view(tried, `search("${q}"): ${q.includes('.') ? 'a dot tries every child at that level. ' : ''}${r ? 'A full path to a ✓ node exists (green).' : 'Every branch fails (red), so false.'}`, [A.text('Result', String(r), r ? 'ok' : 'bad')]);
  }
});
'''),

P(num=212, slug="word-search-ii", title="Word Search II", diff="Hard", topic="Trie", cls="WordSearchII",
idea="Put all words in a trie and DFS the board once; the trie prunes any path that is not a prefix of some word.",
vname="Trie + backtracking",
spec=r'''
Given an `m × n` board of letters and a list of `words`, return all words that can be formed by a path of **adjacent** cells
(horizontally or vertically). A cell may be used at most once per word. Return the words in any order.

**Example**
```
Input:  board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

**Constraints**
* `1 <= m, n <= 12`; `1 <= words.length <= 3 * 10^4`; `1 <= words[i].length <= 10`
''',
approach=r'''
**Shared trie.** Build a trie of all words, storing the full word at its end node. DFS from every cell, following the trie child for
the cell's letter; mark cells as used (`'#'`) during the path. When a node holds a word, record it and clear it (no duplicates).
Prune leaf nodes once they are exhausted.

* Time: **O(m·n·3^L)** — from each cell, a path of length up to L branches into at most 3 new directions per step.
* Space: **O(total letters)** — the trie (plus O(L) recursion).
''',
tc="exp", sc="n",
java=r'''
public class WordSearchII {

    private static final class Node {
        final Node[] children = new Node[26];
        String word;
    }

    public List<String> findWords(char[][] board, String[] words) {
        Node root = new Node();
        for (String w : words) {
            Node n = root;
            for (char c : w.toCharArray()) {
                if (n.children[c - 'a'] == null) n.children[c - 'a'] = new Node();
                n = n.children[c - 'a'];
            }
            n.word = w;
        }
        List<String> found = new ArrayList<>();
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) dfs(board, r, c, root, found);
        }
        return found;
    }

    private void dfs(char[][] board, int r, int c, Node parent, List<String> found) {
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length) return;
        char ch = board[r][c];
        if (ch == '#' || parent.children[ch - 'a'] == null) return;
        Node node = parent.children[ch - 'a'];
        if (node.word != null) {
            found.add(node.word);
            node.word = null;
        }
        board[r][c] = '#';
        dfs(board, r + 1, c, node, found);
        dfs(board, r - 1, c, node, found);
        dfs(board, r, c + 1, node, found);
        dfs(board, r, c - 1, node, found);
        board[r][c] = ch;
    }
}
''',
test=r'''
class WordSearchIITest {

    private final WordSearchII solution = new WordSearchII();

    private static char[][] board(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    @Test
    void example() {
        List<String> found = solution.findWords(board("oaan", "etae", "ihkr", "iflv"), new String[]{"oath", "pea", "eat", "rain"});
        assertEquals(Set.of("oath", "eat"), new HashSet<>(found));
        assertEquals(2, found.size());
    }

    @Test
    void cellUsedOnce() {
        assertEquals(List.of(), solution.findWords(board("ab", "cd"), new String[]{"abcb"}));
    }

    @Test
    void duplicatesReportedOnce() {
        assertEquals(List.of("aa"), solution.findWords(board("aa"), new String[]{"aa"}));
    }
}
''',
trace=r'''
function run(rows, words) {
  const b = rows.map(r => [...r]), m = b.length, n = b[0].length, found = [];
  const root = {}; words.forEach(w => { let t = root; for (const c of w) t = t[c] = t[c] || {}; t.$ = w; });
  A.step(`Put all the words (${words.join(', ')}) in one trie, then DFS the board, following only trie paths.`, A.grid('board', b), A.arr('words', words));
  for (let r = 0; r < m; r++) for (let c = 0; c < n; c++) {
    if (!root[b[r][c]]) continue;
    const path = [];
    const dfs = (x, y, node) => {
      if (x < 0 || y < 0 || x >= m || y >= n || b[x][y] === '#' || !node[b[x][y]]) return;
      const ch = b[x][y], nx = node[ch]; path.push([x, y]);
      if (nx.$) { found.push(nx.$); A.step(`Path ${path.map(([i, j]) => rows[i][j]).join('')} spells "${nx.$}". Record it.`, A.grid('board', rows.map(rw => [...rw]), { hl: path.map(([i, j]) => [`${i},${j}`, 'ok']) }), A.arr('found', found, { hl: { [found.length - 1]: 'ok' } })); delete nx.$; }
      b[x][y] = '#';
      dfs(x + 1, y, nx); dfs(x - 1, y, nx); dfs(x, y + 1, nx); dfs(x, y - 1, nx);
      b[x][y] = ch; path.pop();
    };
    A.step(`Start at (${r},${c}) = '${b[r][c]}', which begins a trie path.`, A.grid('board', b, { hl: { [`${r},${c}`]: 'cur' } }), A.arr('found', found));
    dfs(r, c, root);
  }
  A.step(`Found: ${found.join(', ') || 'none'}. Paths that are not a prefix of any word were cut off immediately.`, A.text('Result', JSON.stringify(found), 'ok'));
}
A.scenario('Classic', 'words = [oath, pea, eat, rain]', () => run(['oaan', 'etae', 'ihkr', 'iflv'], ['oath', 'pea', 'eat', 'rain']));
''',
variants=[dict(
name="Separate DFS for every word",
idea="Run the single-word search (Word Search I) for each word independently.",
approach=r'''
**One search per word.** For each word, try every cell as a start and backtrack along matching letters.

* Time: **O(W·m·n·3^L)** — the board is searched again for every one of the W words.
* Space: **O(L)** — the recursion depth.
''',
tc="exp", sc="n",
java=r'''
public class WordSearchII {

    public List<String> findWords(char[][] board, String[] words) {
        List<String> found = new ArrayList<>();
        for (String w : words) {
            if (exists(board, w) && !found.contains(w)) found.add(w);
        }
        return found;
    }

    private boolean exists(char[][] board, String word) {
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                if (dfs(board, r, c, word, 0)) return true;
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, int r, int c, String word, int i) {
        if (i == word.length()) return true;
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length || board[r][c] != word.charAt(i)) return false;
        char ch = board[r][c];
        board[r][c] = '#';
        boolean ok = dfs(board, r + 1, c, word, i + 1) || dfs(board, r - 1, c, word, i + 1)
                || dfs(board, r, c + 1, word, i + 1) || dfs(board, r, c - 1, word, i + 1);
        board[r][c] = ch;
        return ok;
    }
}
''',
trace=r'''
function run(rows, words) {
  const b = rows.map(r => [...r]), m = b.length, n = b[0].length, found = [];
  for (const w of words) {
    let path = null;
    const dfs = (x, y, i, p) => { if (i === w.length) { path = p.slice(); return true; } if (x < 0 || y < 0 || x >= m || y >= n || b[x][y] !== w[i]) return false; const ch = b[x][y]; b[x][y] = '#'; p.push([x, y]); const ok = dfs(x + 1, y, i + 1, p) || dfs(x - 1, y, i + 1, p) || dfs(x, y + 1, i + 1, p) || dfs(x, y - 1, i + 1, p); p.pop(); b[x][y] = ch; return ok; };
    for (let r = 0; r < m && !path; r++) for (let c = 0; c < n && !path; c++) dfs(r, c, 0, []);
    if (path) found.push(w);
    A.step(path ? `Search the whole board for "${w}": found.` : `Search the whole board for "${w}": not found.`, A.grid('board', b, { hl: (path || []).map(([i, j]) => [`${i},${j}`, 'ok']) }), A.arr('found', found));
  }
  A.step('Each word needed its own full board search.', A.text('Result', JSON.stringify(found), 'ok'));
}
A.scenario('Classic', 'words = [oath, pea, eat, rain]', () => run(['oaan', 'etae', 'ihkr', 'iflv'], ['oath', 'pea', 'eat', 'rain']));
''')]),
]
