PROBLEMS = [
P(num=1838, slug="frequency-of-the-most-frequent-element", title="Frequency of the Most Frequent Element", diff="Medium", topic="Sliding Window", cls="MostFrequentAfterIncrements",
idea="Sort; a window can all be raised to its largest value if largest × length − window sum ≤ k.",
vname="Sort + sliding window",
spec=r'''
In one operation you may increase any element by 1. With at most `k` operations, return the largest possible frequency of a single value.

**Example**
```
nums = [1,2,4],    k = 5 → 3   (raise 1 and 2 to 4)
nums = [1,4,8,13], k = 5 → 2
nums = [3,9,6],    k = 2 → 1
```

**Constraints**
* `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`, `1 <= k <= 10^5`
''',
approach=r'''
**Raise to the right end.** Only increases are allowed, so the target value should be an existing element and the elements raised to it
should be the closest smaller ones. After sorting, a window `[lo, hi]` can be made all equal to `nums[hi]` at a cost of
`nums[hi] · len - sum`. Grow `hi`; shrink `lo` while the cost exceeds `k`. Use `long` for the product.

* Time: **O(n log n)** — sorting.
* Space: **O(1)** — besides sorting.
''',
tc="nlogn", sc="1",
java=r'''
public class MostFrequentAfterIncrements {

    public int maxFrequency(int[] nums, int k) {
        int[] a = nums.clone();
        Arrays.sort(a);
        long sum = 0;
        int lo = 0, best = 0;
        for (int hi = 0; hi < a.length; hi++) {
            sum += a[hi];
            while ((long) a[hi] * (hi - lo + 1) - sum > k) sum -= a[lo++];
            best = Math.max(best, hi - lo + 1);
        }
        return best;
    }
}
''',
test=r'''
class MostFrequentAfterIncrementsTest {

    private final MostFrequentAfterIncrements solution = new MostFrequentAfterIncrements();

    @Test
    void examples() {
        assertEquals(3, solution.maxFrequency(new int[]{1, 2, 4}, 5));
        assertEquals(2, solution.maxFrequency(new int[]{1, 4, 8, 13}, 5));
        assertEquals(1, solution.maxFrequency(new int[]{3, 9, 6}, 2));
        assertEquals(4, solution.maxFrequency(new int[]{7, 7, 7, 7}, 1));
    }
}
''',
trace=r'''
function run(nums, k) {
  const a = nums.slice().sort((x, y) => x - y); let sum = 0, lo = 0, best = 0;
  A.step(`Sort. Try to raise a window of numbers up to its right end, spending at most ${k}.`, A.arr('sorted', a), A.vars({ k }));
  for (let hi = 0; hi < a.length; hi++) {
    sum += a[hi]; let dropped = 0;
    while (a[hi] * (hi - lo + 1) - sum > k) { sum -= a[lo++]; dropped++; }
    const cost = a[hi] * (hi - lo + 1) - sum; best = Math.max(best, hi - lo + 1);
    A.step(`Target ${a[hi]}: ${dropped ? `drop ${dropped} from the left; ` : ''}raising the window costs ${a[hi]} × ${hi - lo + 1} − ${sum} = ${cost}.`, A.arr('sorted', a, { range: [lo, hi], hl: { [hi]: 'cur' } }), A.vars({ cost, best }));
  }
  A.step(`Best frequency: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('All three', '[1,2,4], k = 5', () => run([1, 2, 4], 5));
A.scenario('Window slides', '[1,4,8,13], k = 5', () => run([1, 4, 8, 13], 5));
'''),

P(num=1929, slug="concatenation-of-array", title="Concatenation of Array", diff="Easy", topic="Array", cls="ConcatenationOfArray",
idea="Write each element twice: at i and at i + n.",
vname="Write both copies",
spec=r'''
Return `ans` of length `2n` with `ans[i] = ans[i + n] = nums[i]`.

**Example**
```
[1,2,1]   → [1,2,1,1,2,1]
[1,3,2,1] → [1,3,2,1,1,3,2,1]
```

**Constraints**
* `1 <= n <= 1000`
''',
approach=r'''
**Two writes per element.** Fill `ans[i]` and `ans[i + n]` in one loop.

* Time: **O(n)**.
* Space: **O(n)** — the output.
''',
tc="n", sc="n",
java=r'''
public class ConcatenationOfArray {

    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[2 * n];
        for (int i = 0; i < n; i++) ans[i] = ans[i + n] = nums[i];
        return ans;
    }
}
''',
test=r'''
class ConcatenationOfArrayTest {

    private final ConcatenationOfArray solution = new ConcatenationOfArray();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 2, 1, 1, 2, 1}, solution.getConcatenation(new int[]{1, 2, 1}));
        assertArrayEquals(new int[]{1, 3, 2, 1, 1, 3, 2, 1}, solution.getConcatenation(new int[]{1, 3, 2, 1}));
        assertArrayEquals(new int[]{9, 9}, solution.getConcatenation(new int[]{9}));
    }
}
''',
trace=r'''
function run(nums) {
  const n = nums.length, ans = new Array(2 * n).fill('·');
  A.step(`The answer has ${2 * n} slots.`, A.arr('nums', nums), A.arr('ans', ans));
  nums.forEach((v, i) => { ans[i] = ans[i + n] = v; A.step(`nums[${i}] = ${v} goes to positions ${i} and ${i + n}.`, A.arr('nums', nums, { hl: { [i]: 'cur' } }), A.arr('ans', ans, { hl: { [i]: 'ok', [i + n]: 'ok' } })); });
  A.step(`ans = [${ans}].`, A.arr('ans', ans));
}
A.scenario('Example', '[1,2,1]', () => run([1, 2, 1]));
'''),

P(num=1971, slug="find-if-path-exists-in-graph", title="Find if Path Exists in Graph", diff="Easy", topic="Union Find", cls="FindIfPathExists",
idea="Union the endpoints of every edge; a path exists iff source and destination end up in the same set.",
vname="Union–find",
spec=r'''
Given an undirected graph with `n` nodes and a list of edges, return whether there is a path from `source` to `destination`.

**Example**
```
n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2 → true
n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5 → false
```

**Constraints**
* `1 <= n <= 2 * 10^5`, up to `2 * 10^5` edges
''',
approach=r'''
**Disjoint sets.** Start with every node in its own set. For each edge, merge the two endpoints' sets (union by size, with path halving in
`find`). Afterwards, compare the roots of `source` and `destination`.

* Time: **O((n + E) · α(n))** — practically linear.
* Space: **O(n)**.
''',
tc="n", sc="n",
java=r'''
public class FindIfPathExists {

    private int[] parent, size;

    public boolean validPath(int n, int[][] edges, int source, int destination) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        for (int[] e : edges) union(e[0], e[1]);
        return find(source) == find(destination);
    }

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return;
        if (size[ra] < size[rb]) {
            int t = ra;
            ra = rb;
            rb = t;
        }
        parent[rb] = ra;
        size[ra] += size[rb];
    }
}
''',
test=r'''
class FindIfPathExistsTest {

    private final FindIfPathExists solution = new FindIfPathExists();

    @Test
    void examples() {
        assertTrue(solution.validPath(3, new int[][]{{0, 1}, {1, 2}, {2, 0}}, 0, 2));
        assertFalse(solution.validPath(6, new int[][]{{0, 1}, {0, 2}, {3, 5}, {5, 4}, {4, 3}}, 0, 5));
        assertTrue(solution.validPath(1, new int[][]{}, 0, 0));
        assertTrue(solution.validPath(5, new int[][]{{0, 4}, {4, 3}, {3, 1}}, 0, 1));
    }
}
''',
trace=r'''
function run(n, edges, s, d) {
  const parent = [...Array(n).keys()], find = x => { while (parent[x] !== x) x = parent[x]; return x; };
  const nodes = parent.map(i => ({ id: i })), colour = () => { const roots = [...new Set(parent.map((_, i) => find(i)))]; return Object.fromEntries(parent.map((_, i) => [i, ['cur', 'alt', 'ok', 'bad', 'sel'][roots.indexOf(find(i)) % 5]])); };
  A.step('Every node starts in its own set.', A.graph('graph', nodes, []), A.arr('parent', parent));
  edges.forEach(([a, b], i) => { const ra = find(a), rb = find(b); if (ra !== rb) parent[rb] = ra; A.step(ra === rb ? `Edge ${a}–${b}: already in the same set.` : `Edge ${a}–${b}: merge their sets.`, A.graph('graph', nodes, edges.slice(0, i + 1), { hl: colour() }), A.arr('parent', parent)); });
  const ok = find(s) === find(d);
  A.step(`${s} has root ${find(s)}, ${d} has root ${find(d)}: ${ok ? 'same set, so a path exists' : 'different sets, so no path'}.`, A.graph('graph', nodes, edges, { hl: { [s]: ok ? 'ok' : 'bad', [d]: ok ? 'ok' : 'bad' } }), A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('Two components', '0 → 5', () => run(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5));
A.scenario('Triangle', '0 → 2', () => run(3, [[0, 1], [1, 2], [2, 0]], 0, 2));
'''),

P(num=2108, slug="find-first-palindromic-string-in-the-array", title="Find First Palindromic String in the Array", diff="Easy", topic="Two Pointers", cls="FirstPalindrome",
idea="Check each word with two pointers moving inward; return the first that passes.",
vname="Two-pointer check per word",
spec=r'''
Return the first string in `words` that is a palindrome, or `""` if there is none.

**Example**
```
["abc","car","ada","racecar","cool"] → "ada"
["notapalindrome","racecar"]         → "racecar"
["def","ghi"]                        → ""
```

**Constraints**
* `1 <= words.length <= 100`, `1 <= words[i].length <= 100`
''',
approach=r'''
**Scan.** For each word, compare characters from both ends moving inward; stop at the first mismatch. Return the first word with none.

* Time: **O(total length)**.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class FirstPalindrome {

    public String firstPalindrome(String[] words) {
        for (String w : words) if (isPalindrome(w)) return w;
        return "";
    }

    private boolean isPalindrome(String w) {
        for (int i = 0, j = w.length() - 1; i < j; i++, j--) if (w.charAt(i) != w.charAt(j)) return false;
        return true;
    }
}
''',
test=r'''
class FirstPalindromeTest {

    private final FirstPalindrome solution = new FirstPalindrome();

    @Test
    void examples() {
        assertEquals("ada", solution.firstPalindrome(new String[]{"abc", "car", "ada", "racecar", "cool"}));
        assertEquals("racecar", solution.firstPalindrome(new String[]{"notapalindrome", "racecar"}));
        assertEquals("", solution.firstPalindrome(new String[]{"def", "ghi"}));
        assertEquals("a", solution.firstPalindrome(new String[]{"ab", "a"}));
    }
}
''',
trace=r'''
function run(words) {
  A.step('Check the words in order.', A.arr('words', words));
  for (let k = 0; k < words.length; k++) {
    const w = words[k]; let i = 0, j = w.length - 1;
    while (i < j && w[i] === w[j]) { i++; j--; }
    const ok = i >= j;
    A.step(ok ? `"${w}" reads the same both ways.` : `"${w}": '${w[i]}' ≠ '${w[j]}'. Not a palindrome.`, A.arr('words', words, { hl: { [k]: ok ? 'ok' : 'bad' } }), A.chars(w, w, { hl: ok ? {} : { [i]: 'bad', [j]: 'bad' } }));
    if (ok) { A.step(`The first palindrome is "${w}".`, A.text('Result', w, 'ok')); return; }
  }
  A.step('No palindrome found.', A.text('Result', '""', 'bad'));
}
A.scenario('Example', '["abc","car","ada","racecar","cool"]', () => run(['abc', 'car', 'ada', 'racecar', 'cool']));
'''),

P(num=1029, slug="two-city-scheduling", title="Two City Scheduling", diff="Medium", topic="Greedy", cls="TwoCityScheduling",
idea="Sort people by how much cheaper city A is for them; send the first half to A and the rest to B.",
vname="Sort by cost difference",
spec=r'''
`2n` people are interviewing; `costs[i] = [aCost, bCost]` is the cost of flying person `i` to city A or B. Exactly `n` people must go to
each city. Return the minimum total cost.

**Example**
```
[[10,20],[30,200],[400,50],[30,20]] → 110   (A: 10, 30; B: 50, 20)
```

**Constraints**
* `2 <= costs.length <= 100`, even
''',
approach=r'''
**Relative cost.** Imagine everyone flies to B first; sending person `i` to A instead changes the total by `aCost - bCost`. Choose the `n`
people with the smallest (most negative) changes. Sorting by `aCost - bCost` does exactly that.

* Time: **O(n log n)**.
* Space: **O(n)** — the sorted copy.
''',
tc="nlogn", sc="n",
java=r'''
public class TwoCityScheduling {

    public int twoCitySchedCost(int[][] costs) {
        int[][] c = costs.clone();
        Arrays.sort(c, (x, y) -> Integer.compare(x[0] - x[1], y[0] - y[1]));
        int n = c.length / 2, total = 0;
        for (int i = 0; i < c.length; i++) total += i < n ? c[i][0] : c[i][1];
        return total;
    }
}
''',
test=r'''
class TwoCitySchedulingTest {

    private final TwoCityScheduling solution = new TwoCityScheduling();

    @Test
    void examples() {
        assertEquals(110, solution.twoCitySchedCost(new int[][]{{10, 20}, {30, 200}, {400, 50}, {30, 20}}));
        assertEquals(1859, solution.twoCitySchedCost(new int[][]{{259, 770}, {448, 54}, {926, 667}, {184, 139}, {840, 118}, {577, 469}}));
        assertEquals(3086, solution.twoCitySchedCost(new int[][]{{515, 563}, {451, 713}, {537, 709}, {343, 819}, {855, 779}, {457, 60}, {650, 359}, {631, 42}}));
    }
}
''',
trace=r'''
function run(costs) {
  const c = costs.slice().sort((x, y) => (x[0] - x[1]) - (y[0] - y[1])), n = c.length / 2; let total = 0;
  A.step('Sending a person to A instead of B changes the cost by a − b. Sort by that difference.', A.arr('people [a, b]', costs.map(x => `[${x}]`)), A.arr('sorted by a − b', c.map(x => x[0] - x[1])));
  c.forEach((x, i) => { const a = i < n; total += a ? x[0] : x[1]; A.step(`[${x}] (a − b = ${x[0] - x[1]}) goes to ${a ? 'A' : 'B'} for ${a ? x[0] : x[1]}.`, A.arr('sorted people', c.map(y => `[${y}]`), { hl: { [i]: a ? 'cur' : 'alt' } }), A.vars({ total })); });
  A.step(`Minimum total: ${total}.`, A.text('Result', total, 'ok'));
}
A.scenario('Example', '[[10,20],[30,200],[400,50],[30,20]]', () => run([[10, 20], [30, 200], [400, 50], [30, 20]]));
'''),

P(num=1094, slug="car-pooling", title="Car Pooling", diff="Medium", topic="Prefix Sum", cls="CarPooling",
idea="Record passenger changes at each pick-up and drop-off point, then sweep the road keeping a running load.",
vname="Difference array sweep",
spec=r'''
A car with `capacity` empty seats drives east only. `trips[i] = [passengers, from, to]` picks up passengers at `from` and drops them at
`to`. Return whether every trip can be served.

**Example**
```
trips = [[2,1,5],[3,3,7]], capacity = 4 → false
trips = [[2,1,5],[3,3,7]], capacity = 5 → true
```

**Constraints**
* `1 <= trips.length <= 1000`, `0 <= from < to <= 1000`
''',
approach=r'''
**Difference array.** Add `passengers` at `from` and subtract at `to` (they leave before anyone boards there). Sweep positions `0..1000`
keeping a running sum; if it ever exceeds `capacity`, return `false`.

* Time: **O(n + L)** — `L = 1001` positions.
* Space: **O(L)**.
''',
tc="n", sc="1",
java=r'''
public class CarPooling {

    public boolean carPooling(int[][] trips, int capacity) {
        int[] change = new int[1001];
        for (int[] t : trips) {
            change[t[1]] += t[0];
            change[t[2]] -= t[0];
        }
        int load = 0;
        for (int c : change) if ((load += c) > capacity) return false;
        return true;
    }
}
''',
test=r'''
class CarPoolingTest {

    private final CarPooling solution = new CarPooling();

    @Test
    void examples() {
        assertFalse(solution.carPooling(new int[][]{{2, 1, 5}, {3, 3, 7}}, 4));
        assertTrue(solution.carPooling(new int[][]{{2, 1, 5}, {3, 3, 7}}, 5));
        assertTrue(solution.carPooling(new int[][]{{2, 1, 5}, {3, 5, 7}}, 3));
        assertTrue(solution.carPooling(new int[][]{{3, 2, 7}, {3, 7, 9}, {8, 3, 9}}, 11));
    }
}
''',
trace=r'''
function run(trips, cap) {
  const L = Math.max(...trips.map(t => t[2])) + 1, ch = new Array(L).fill(0);
  trips.forEach(([p, f, t]) => { ch[f] += p; ch[t] -= p; });
  A.step(`Mark +passengers at each pick-up and −passengers at each drop-off.`, A.grid('trips [n, from, to]', trips), A.arr('change at position', ch));
  let load = 0; const loads = [];
  for (let x = 0; x < L; x++) {
    load += ch[x]; loads.push(load);
    if (ch[x]) A.step(`Position ${x}: ${ch[x] > 0 ? '+' : ''}${ch[x]} → ${load} on board${load > cap ? `, more than ${cap} seats!` : '.'}`, A.arr('load', loads, { hl: { [x]: load > cap ? 'bad' : 'ok' } }), A.vars({ capacity: cap }));
    if (load > cap) { A.step('The car is over capacity.', A.text('Result', 'false', 'bad')); return; }
  }
  A.step('The load never exceeded the capacity.', A.text('Result', 'true', 'ok'));
}
A.scenario('Too full', 'capacity 4', () => run([[2, 1, 5], [3, 3, 7]], 4));
A.scenario('Fits', 'capacity 5', () => run([[2, 1, 5], [3, 3, 7]], 5));
'''),

P(num=1110, slug="delete-nodes-and-return-forest", title="Delete Nodes And Return Forest", diff="Medium", topic="Binary Tree DFS", cls="DeleteNodesForest",
idea="Post-order: when a node is deleted, its surviving children become new roots.",
vname="Post-order with a delete set", helpers=["TreeNode"],
spec=r'''
Delete every node whose value is in `to_delete`. The remaining nodes form a forest; return the roots of its trees, in any order.

**Example**
```
root = [1,2,3,4,5,6,7], to_delete = [3,5] → [[1,2,null,4],[6],[7]]
root = [1,2,4,null,3],  to_delete = [3]   → [[1,2,4]]
```

**Constraints**
* `1 <= n <= 1000`, distinct values
''',
approach=r'''
**Children first.** Put `to_delete` in a `MyHashSet`. Recurse with a flag saying whether the node's parent was deleted (or it is the root).
A kept node with that flag set is a new root. Process children before deciding, and return `null` for a deleted node so its parent
unlinks it.

* Time: **O(n + d)**.
* Space: **O(h + d)** — recursion and the set.
''',
tc="n", sc="n",
java=r'''
public class DeleteNodesForest {

    public List<TreeNode> delNodes(TreeNode root, int[] toDelete) {
        MyHashSet<Integer> del = new MyHashSet<>();
        for (int v : toDelete) del.add(v);
        List<TreeNode> roots = new ArrayList<>();
        walk(root, true, del, roots);
        return roots;
    }

    private TreeNode walk(TreeNode node, boolean parentGone, MyHashSet<Integer> del, List<TreeNode> roots) {
        if (node == null) return null;
        boolean gone = del.contains(node.val);
        if (parentGone && !gone) roots.add(node);
        node.left = walk(node.left, gone, del, roots);
        node.right = walk(node.right, gone, del, roots);
        return gone ? null : node;
    }
}
''',
test=r'''
class DeleteNodesForestTest {

    private final DeleteNodesForest solution = new DeleteNodesForest();

    private Set<String> shapes(List<TreeNode> roots) {
        Set<String> out = new TreeSet<>();
        for (TreeNode r : roots) out.add(TreeNode.toList(r).toString());
        return out;
    }

    @Test
    void examples() {
        assertEquals(new TreeSet<>(List.of("[1, 2, null, 4]", "[6]", "[7]")), shapes(solution.delNodes(TreeNode.of(1, 2, 3, 4, 5, 6, 7), new int[]{3, 5})));
        assertEquals(new TreeSet<>(List.of("[1, 2, 4]")), shapes(solution.delNodes(TreeNode.of(1, 2, 4, null, 3), new int[]{3})));
        assertEquals(new TreeSet<>(List.of("[2]", "[3]")), shapes(solution.delNodes(TreeNode.of(1, 2, 3), new int[]{1})));
    }
}
''',
trace=r'''
function run(arr, del) {
  const root = A.mkTree(arr), D = new Set(del), roots = [], hl = {};
  A.step(`Delete ${del.join(', ')}. A kept node whose parent is deleted (or the root) starts a new tree.`, A.tree('tree', root));
  (function mark(n) { if (!n) return; if (D.has(n.val)) hl[n.id] = 'bad'; mark(n.left); mark(n.right); })(root);
  A.step('Nodes to delete are red.', A.tree('tree', root, { hl }));
  (function walk(n, parentGone) {
    if (!n) return null;
    const gone = D.has(n.val);
    if (parentGone && !gone) { roots.push(n.val); hl[n.id] = 'ok'; A.step(`${n.val} stays and has no parent left: it is a new root.`, A.tree('tree', root, { hl }), A.arr('roots', roots, { hl: { [roots.length - 1]: 'ok' } })); }
    n.left = walk(n.left, gone); n.right = walk(n.right, gone);
    return gone ? null : n;
  })(root, true);
  A.step(`The forest has ${roots.length} tree${roots.length === 1 ? '' : 's'}, rooted at ${roots.join(', ')}.`, A.arr('roots', roots));
}
A.scenario('Example', '[1,2,3,4,5,6,7], delete 3 and 5', () => run([1, 2, 3, 4, 5, 6, 7], [3, 5]));
'''),

P(num=1155, slug="number-of-dice-rolls-with-target-sum", title="Number of Dice Rolls With Target Sum", diff="Medium", topic="Dynamic Programming", cls="DiceRollsTargetSum",
idea="ways[d][s] adds up ways[d − 1][s − f] over every face f of the last die.",
vname="DP over dice and sums",
spec=r'''
Roll `n` dice with `k` faces each (`1..k`). Return the number of ordered outcomes whose faces sum to `target`, modulo `10^9 + 7`.

**Example**
```
n = 1, k = 6, target = 3   → 1
n = 2, k = 6, target = 7   → 6
n = 30, k = 30, target = 500 → 222616187
```

**Constraints**
* `1 <= n, k <= 30`, `1 <= target <= 1000`
''',
approach=r'''
**Last die.** With one fewer die, every sum `s - f` for a face `f` extends to `s`. Keep one row `ways[s]` for the dice so far and build the
next row from it. Reduce modulo `10^9 + 7` as you add.

* Time: **O(n · target · k)**.
* Space: **O(target)** — two rows.
''',
tc="n2", sc="n",
java=r'''
public class DiceRollsTargetSum {

    private static final int MOD = 1_000_000_007;

    public int numRollsToTarget(int n, int k, int target) {
        int[] ways = new int[target + 1];
        ways[0] = 1;
        for (int d = 1; d <= n; d++) {
            int[] next = new int[target + 1];
            for (int s = 1; s <= target; s++)
                for (int f = 1; f <= k && f <= s; f++) next[s] = (next[s] + ways[s - f]) % MOD;
            ways = next;
        }
        return ways[target];
    }
}
''',
test=r'''
class DiceRollsTargetSumTest {

    private final DiceRollsTargetSum solution = new DiceRollsTargetSum();

    @ParameterizedTest
    @CsvSource({"1,6,3,1", "2,6,7,6", "30,30,500,222616187", "2,6,13,0", "3,2,4,3"})
    void ways(int n, int k, int target, int expected) {
        assertEquals(expected, solution.numRollsToTarget(n, k, target));
    }
}
''',
trace=r'''
function run(n, k, target) {
  let ways = new Array(target + 1).fill(0); ways[0] = 1; const rows = [ways.slice()];
  A.step(`With 0 dice, only sum 0 is possible (1 way). Each die adds a face from 1 to ${k}.`, A.grid('ways[dice][sum]', rows));
  for (let d = 1; d <= n; d++) {
    const next = new Array(target + 1).fill(0);
    for (let s = 1; s <= target; s++) for (let f = 1; f <= k && f <= s; f++) next[s] += ways[s - f];
    ways = next; rows.push(ways.slice());
    A.step(`${d} ${d === 1 ? 'die' : 'dice'}: ways[s] adds up the previous row at s − 1 … s − ${k}.`, A.grid('ways[dice][sum]', rows, { hl: Object.fromEntries(ways.map((v, s) => [`${d},${s}`, v ? 'cur' : ''])) }));
  }
  A.step(`${ways[target]} way${ways[target] === 1 ? '' : 's'} to roll ${target} with ${n} dice.`, A.grid('ways[dice][sum]', rows, { hl: { [`${n},${target}`]: 'ok' } }), A.text('Result', ways[target], 'ok'));
}
A.scenario('Two dice', 'n = 2, k = 6, target 7', () => run(2, 6, 7));
'''),

P(num=1209, slug="remove-all-adjacent-duplicates-in-string-ii", title="Remove All Adjacent Duplicates in String II", diff="Medium", topic="Stack", cls="RemoveAdjacentDuplicatesII",
idea="Keep a stack of (letter, run length); when a run reaches k, pop it.",
vname="Stack of runs",
spec=r'''
Repeatedly remove `k` adjacent equal letters from `s` until no such group remains. Return the final string.

**Example**
```
s = "abcd",                 k = 2 → "abcd"
s = "deeedbbcccbdaa",       k = 3 → "aa"
s = "pbbcggttciiippooaais", k = 2 → "ps"
```

**Constraints**
* `1 <= s.length <= 10^5`, `2 <= k <= 10^4`
''',
approach=r'''
**Runs on a stack.** Push each letter: if it matches the top run, increase that run's count, else push a new run of 1. When a count hits
`k`, pop the run; the runs on either side can now merge naturally on the next push. Rebuild the string from the remaining runs.

* Time: **O(n)**.
* Space: **O(n)**.
''',
tc="n", sc="n",
java=r'''
public class RemoveAdjacentDuplicatesII {

    public String removeDuplicates(String s, int k) {
        char[] letter = new char[s.length()];
        int[] count = new int[s.length()];
        int top = -1;
        for (char c : s.toCharArray()) {
            if (top >= 0 && letter[top] == c) {
                if (++count[top] == k) top--;
            } else {
                letter[++top] = c;
                count[top] = 1;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= top; i++) sb.repeat(letter[i], count[i]);
        return sb.toString();
    }
}
''',
test=r'''
class RemoveAdjacentDuplicatesIITest {

    private final RemoveAdjacentDuplicatesII solution = new RemoveAdjacentDuplicatesII();

    @ParameterizedTest
    @CsvSource({"abcd,2,abcd", "deeedbbcccbdaa,3,aa", "pbbcggttciiippooaais,2,ps", "aaaa,2,''", "aaaaa,3,aa"})
    void removes(String s, int k, String expected) {
        assertEquals(expected, solution.removeDuplicates(s, k));
    }
}
''',
trace=r'''
function run(s, k) {
  const st = [];
  A.step(`Keep runs of equal letters on a stack. A run of ${k} disappears.`, A.chars('s', s), A.stack('runs', st));
  [...s].forEach((c, i) => {
    let say;
    if (st.length && st[st.length - 1][0] === c) { st[st.length - 1][1]++; if (st[st.length - 1][1] === k) { st.pop(); say = `'${c}' completes a run of ${k}: remove it.`; } else say = `'${c}' extends the run to ${st[st.length - 1][1]}.`; }
    else { st.push([c, 1]); say = `'${c}' starts a new run.`; }
    A.step(say, A.chars('s', s, { hl: { [i]: say.includes('remove') ? 'bad' : 'cur' } }), A.stack('runs', st.map(([ch, n]) => `${ch} × ${n}`)));
  });
  const out = st.map(([c, n]) => c.repeat(n)).join('');
  A.step(`What remains: "${out}".`, A.text('Result', `"${out}"`, 'ok'));
}
A.scenario('Cascade', '"deeedbbcccbdaa", k = 3', () => run('deeedbbcccbdaa', 3));
'''),

P(num=1249, slug="minimum-remove-to-make-valid-parentheses", title="Minimum Remove to Make Valid Parentheses", diff="Medium", topic="Stack", cls="MinRemoveToMakeValid",
idea="Unmatched ')' are found left to right; '(' still open at the end are unmatched too; delete exactly those.",
vname="Stack of open indices",
spec=r'''
Remove the minimum number of parentheses from `s` (letters stay) so that the result is valid. Return any valid result.

**Example**
```
"lee(t(c)o)de)" → "lee(t(c)o)de"
"a)b(c)d"       → "ab(c)d"
"))(("          → ""
```

**Constraints**
* `1 <= s.length <= 10^5`
''',
approach=r'''
**Mark the unmatched.** Scan left to right with a stack of indices of `'('`. A `')'` with an empty stack has no partner: mark it. Otherwise
pop its partner. Any `'('` left on the stack never closes: mark those. Each marked character must go and removing them suffices, so it is
minimal.

* Time: **O(n)**.
* Space: **O(n)**.
''',
tc="n", sc="n",
java=r'''
public class MinRemoveToMakeValid {

    public String minRemoveToMakeValid(String s) {
        boolean[] remove = new boolean[s.length()];
        Deque<Integer> open = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') open.push(i);
            else if (c == ')') {
                if (open.isEmpty()) remove[i] = true;
                else open.pop();
            }
        }
        for (int i : open) remove[i] = true;
        StringBuilder sb = new StringBuilder(s.length());
        for (int i = 0; i < s.length(); i++) if (!remove[i]) sb.append(s.charAt(i));
        return sb.toString();
    }
}
''',
test=r'''
class MinRemoveToMakeValidTest {

    private final MinRemoveToMakeValid solution = new MinRemoveToMakeValid();

    @ParameterizedTest
    @CsvSource({"lee(t(c)o)de),lee(t(c)o)de", "a)b(c)d,ab(c)d", "))((,''", "(a(b(c)d),a(b(c)d)", "abc,abc", "()),()"})
    void removes(String s, String expected) {
        assertEquals(expected, solution.minRemoveToMakeValid(s));
    }
}
''',
trace=r'''
function run(s) {
  const open = [], rm = {};
  A.step("Scan left to right. Remember each '(' until a ')' closes it.", A.chars('s', s), A.stack('open (index)', open));
  [...s].forEach((c, i) => {
    if (c === '(') { open.push(i); A.step(`'(' at ${i}: wait for its partner.`, A.chars('s', s, { hl: { ...rm, [i]: 'cur' } }), A.stack('open (index)', open)); }
    else if (c === ')') { if (!open.length) { rm[i] = 'bad'; A.step(`')' at ${i} has nothing to close: remove it.`, A.chars('s', s, { hl: rm }), A.stack('open (index)', open)); } else { const j = open.pop(); A.step(`')' at ${i} closes '(' at ${j}.`, A.chars('s', s, { hl: { ...rm, [i]: 'ok', [j]: 'ok' } }), A.stack('open (index)', open)); } }
  });
  open.forEach(i => (rm[i] = 'bad'));
  if (open.length) A.step(`'(' at ${open.join(', ')} never closed: remove ${open.length === 1 ? 'it' : 'them'}.`, A.chars('s', s, { hl: rm }));
  const out = [...s].filter((_, i) => !rm[i]).join('');
  A.step(`Result: "${out}".`, A.text('Result', `"${out}"`, 'ok'));
}
A.scenario('Extra close', '"lee(t(c)o)de)"', () => run('lee(t(c)o)de)'));
A.scenario('Extra open', '"(a(b(c)d)"', () => run('(a(b(c)d)'));
'''),
]
