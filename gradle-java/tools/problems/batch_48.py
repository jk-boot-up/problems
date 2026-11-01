PROBLEMS = [
P(num=1438, slug="longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit", title="Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit", diff="Medium", topic="Sliding Window", cls="LongestSubarrayWithinLimit",
idea="Slide a window while two monotonic deques report its current max and min in O(1).",
vname="Window with max/min deques",
spec=r'''
Return the length of the longest non-empty subarray in which the absolute difference between **any** two elements is at most `limit`
(equivalently, `max - min <= limit`).

**Example**
```
nums = [8,2,4,7],         limit = 4 → 2   ([2,4] or [4,7])
nums = [10,1,2,4,7,2],    limit = 5 → 4   ([2,4,7,2])
nums = [4,2,2,2,4,4,2,2], limit = 0 → 3
```

**Constraints**
* `1 <= nums.length <= 10^5`
''',
approach=r'''
**Two deques.** `maxQ` holds values in decreasing order and `minQ` in increasing order, so their fronts are the window's max and min. Add
`nums[hi]` to both (dropping smaller / larger values from the back). While `max - min > limit`, move `lo` right, removing `nums[lo]` from a
deque front if it is there.

* Time: **O(n)** — every value enters and leaves each deque once.
* Space: **O(n)** — the deques.
''',
tc="n", sc="n",
java=r'''
public class LongestSubarrayWithinLimit {

    public int longestSubarray(int[] nums, int limit) {
        Deque<Integer> maxQ = new ArrayDeque<>(), minQ = new ArrayDeque<>();
        int lo = 0, best = 0;
        for (int hi = 0; hi < nums.length; hi++) {
            int v = nums[hi];
            while (!maxQ.isEmpty() && maxQ.peekLast() < v) maxQ.pollLast();
            while (!minQ.isEmpty() && minQ.peekLast() > v) minQ.pollLast();
            maxQ.addLast(v);
            minQ.addLast(v);
            while (maxQ.peekFirst() - minQ.peekFirst() > limit) {
                if (maxQ.peekFirst() == nums[lo]) maxQ.pollFirst();
                if (minQ.peekFirst() == nums[lo]) minQ.pollFirst();
                lo++;
            }
            best = Math.max(best, hi - lo + 1);
        }
        return best;
    }
}
''',
test=r'''
class LongestSubarrayWithinLimitTest {

    private final LongestSubarrayWithinLimit solution = new LongestSubarrayWithinLimit();

    @Test
    void examples() {
        assertEquals(2, solution.longestSubarray(new int[]{8, 2, 4, 7}, 4));
        assertEquals(4, solution.longestSubarray(new int[]{10, 1, 2, 4, 7, 2}, 5));
        assertEquals(3, solution.longestSubarray(new int[]{4, 2, 2, 2, 4, 4, 2, 2}, 0));
        assertEquals(1, solution.longestSubarray(new int[]{5}, 0));
    }
}
''',
trace=r'''
function run(nums, limit) {
  const mx = [], mn = []; let lo = 0, best = 0;
  A.step(`Grow a window to the right; the max deque and min deque give its spread instantly. Keep max − min ≤ ${limit}.`, A.arr('nums', nums));
  for (let hi = 0; hi < nums.length; hi++) {
    const v = nums[hi];
    while (mx.length && mx[mx.length - 1] < v) mx.pop(); while (mn.length && mn[mn.length - 1] > v) mn.pop();
    mx.push(v); mn.push(v);
    let shrunk = 0;
    while (mx[0] - mn[0] > limit) { if (mx[0] === nums[lo]) mx.shift(); if (mn[0] === nums[lo]) mn.shift(); lo++; shrunk++; }
    best = Math.max(best, hi - lo + 1);
    A.step(`Add ${v}.${shrunk ? ` The spread was too large: drop ${shrunk} from the left.` : ''} Window max ${mx[0]}, min ${mn[0]}, length ${hi - lo + 1}.`, A.arr('nums', nums, { range: [lo, hi], hl: { [hi]: 'cur' } }), A.arr('max deque', mx), A.arr('min deque', mn), A.vars({ best }));
  }
  A.step(`Longest window: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Example', '[10,1,2,4,7,2], limit 5', () => run([10, 1, 2, 4, 7, 2], 5));
'''),

P(num=1462, slug="course-schedule-iv", title="Course Schedule IV", diff="Medium", topic="Graph", cls="CourseScheduleIV",
idea="With at most 100 courses, precompute every reachable pair with Floyd–Warshall style closure.",
vname="Transitive closure",
spec=r'''
There are `numCourses` courses. `prerequisites[i] = [a, b]` means `a` must be taken before `b`. Prerequisites are transitive. For each
query `[u, v]`, return whether `u` is a (direct or indirect) prerequisite of `v`.

**Example**
```
numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]] → [false,true]
numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]] → [true,true]
```

**Constraints**
* `2 <= numCourses <= 100`, no cycles, up to `10^4` queries
''',
approach=r'''
**Closure.** `reach[a][b]` starts true for direct prerequisites. For every middle course `k`, if `a` reaches `k` and `k` reaches `b`, then `a`
reaches `b`. After all `k`, each query is a lookup.

* Time: **O(n³ + q)**.
* Space: **O(n²)**.
''',
tc="exp", sc="n2",
java=r'''
public class CourseScheduleIV {

    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        boolean[][] reach = new boolean[numCourses][numCourses];
        for (int[] p : prerequisites) reach[p[0]][p[1]] = true;
        for (int k = 0; k < numCourses; k++)
            for (int a = 0; a < numCourses; a++)
                if (reach[a][k])
                    for (int b = 0; b < numCourses; b++) if (reach[k][b]) reach[a][b] = true;
        List<Boolean> out = new ArrayList<>(queries.length);
        for (int[] q : queries) out.add(reach[q[0]][q[1]]);
        return out;
    }
}
''',
test=r'''
class CourseScheduleIVTest {

    private final CourseScheduleIV solution = new CourseScheduleIV();

    @Test
    void examples() {
        assertEquals(List.of(false, true), solution.checkIfPrerequisite(2, new int[][]{{1, 0}}, new int[][]{{0, 1}, {1, 0}}));
        assertEquals(List.of(false, false), solution.checkIfPrerequisite(2, new int[][]{}, new int[][]{{1, 0}, {0, 1}}));
        assertEquals(List.of(true, true), solution.checkIfPrerequisite(3, new int[][]{{1, 2}, {1, 0}, {2, 0}}, new int[][]{{1, 0}, {1, 2}}));
        assertEquals(List.of(true, false), solution.checkIfPrerequisite(4, new int[][]{{0, 1}, {1, 2}, {2, 3}}, new int[][]{{0, 3}, {3, 0}}));
    }
}
''',
trace=r'''
function run(n, pre, queries) {
  const R = Array.from({ length: n }, () => new Array(n).fill(0)); pre.forEach(([a, b]) => (R[a][b] = 1));
  const nodes = [...Array(n).keys()].map(i => ({ id: i })), view = hl => A.grid('reach[a][b]', R, { hl });
  A.step('Direct prerequisites. reach[a][b] = 1 means a comes before b.', A.graph('courses', nodes, pre, { directed: true }), view({}));
  for (let k = 0; k < n; k++) {
    const added = {};
    for (let a = 0; a < n; a++) if (R[a][k]) for (let b = 0; b < n; b++) if (R[k][b] && !R[a][b]) { R[a][b] = 1; added[`${a},${b}`] = 'ok'; }
    A.step(`Through course ${k}: if a reaches ${k} and ${k} reaches b, then a reaches b. ${Object.keys(added).length ? `New: ${Object.keys(added).map(s => s.replace(',', '→')).join(', ')}.` : 'Nothing new.'}`, view(added));
  }
  const ans = queries.map(([u, v]) => !!R[u][v]);
  A.step(`Answer the queries by lookup: [${ans}].`, view(Object.fromEntries(queries.map(([u, v]) => [`${u},${v}`, R[u][v] ? 'ok' : 'bad']))), A.text('Result', `[${ans}]`, 'ok'));
}
A.scenario('Chain', '0 → 1 → 2 → 3', () => run(4, [[0, 1], [1, 2], [2, 3]], [[0, 3], [3, 0]]));
'''),

P(num=1470, slug="shuffle-the-array", title="Shuffle the Array", diff="Easy", topic="Array", cls="ShuffleTheArray",
idea="Element i of the first half and element i of the second half go to positions 2i and 2i + 1.",
vname="Interleave halves",
spec=r'''
Given `nums = [x1,…,xn,y1,…,yn]`, return `[x1,y1,x2,y2,…,xn,yn]`.

**Example**
```
nums = [2,5,1,3,4,7], n = 3 → [2,3,5,4,1,7]
```

**Constraints**
* `1 <= n <= 500`
''',
approach=r'''
**Direct placement.** `out[2i] = nums[i]` and `out[2i + 1] = nums[n + i]`.

* Time: **O(n)**.
* Space: **O(n)** — the output.
''',
tc="n", sc="n",
java=r'''
public class ShuffleTheArray {

    public int[] shuffle(int[] nums, int n) {
        int[] out = new int[2 * n];
        for (int i = 0; i < n; i++) {
            out[2 * i] = nums[i];
            out[2 * i + 1] = nums[n + i];
        }
        return out;
    }
}
''',
test=r'''
class ShuffleTheArrayTest {

    private final ShuffleTheArray solution = new ShuffleTheArray();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 3, 5, 4, 1, 7}, solution.shuffle(new int[]{2, 5, 1, 3, 4, 7}, 3));
        assertArrayEquals(new int[]{1, 4, 2, 3, 3, 2, 4, 1}, solution.shuffle(new int[]{1, 2, 3, 4, 4, 3, 2, 1}, 4));
        assertArrayEquals(new int[]{1, 2}, solution.shuffle(new int[]{1, 2}, 1));
    }
}
''',
trace=r'''
function run(nums) {
  const n = nums.length / 2, out = new Array(2 * n).fill('·');
  A.step(`First half x, second half y. Interleave them.`, A.arr('nums', nums, { hl: Object.fromEntries(nums.map((_, i) => [i, i < n ? 'cur' : 'alt'])) }));
  for (let i = 0; i < n; i++) { out[2 * i] = nums[i]; out[2 * i + 1] = nums[n + i]; A.step(`x${i + 1} = ${nums[i]} → position ${2 * i}; y${i + 1} = ${nums[n + i]} → position ${2 * i + 1}.`, A.arr('nums', nums, { hl: { [i]: 'cur', [n + i]: 'alt' } }), A.arr('result', out, { hl: { [2 * i]: 'cur', [2 * i + 1]: 'alt' } })); }
  A.step(`Result: [${out}].`, A.arr('result', out));
}
A.scenario('Example', '[2,5,1,3,4,7]', () => run([2, 5, 1, 3, 4, 7]));
'''),

P(num=1475, slug="final-prices-with-a-special-discount-in-a-shop", title="Final Prices With a Special Discount in a Shop", diff="Easy", topic="Monotonic Stack", cls="FinalPrices",
idea="Each item's discount is the next item to its right that costs no more; a monotonic stack finds all of them in one pass.",
vname="Next smaller-or-equal with a stack",
spec=r'''
Item `i` costs `prices[i]`. Its discount is `prices[j]` for the **first** `j > i` with `prices[j] <= prices[i]` (no discount if none).
Return the final prices.

**Example**
```
[8,4,6,2,3] → [4,2,4,2,3]
[1,2,3,4,5] → [1,2,3,4,5]
[10,1,1,6]  → [9,0,1,6]
```

**Constraints**
* `1 <= prices.length <= 500`
''',
approach=r'''
**Pending items.** Keep a stack of indices still waiting for their discount (their prices increase up the stack). When a new price is `<=`
the price on top, that top item gets this discount: pop it and subtract. Then push the new index.

* Time: **O(n)**.
* Space: **O(n)**.
''',
tc="n", sc="n",
java=r'''
public class FinalPrices {

    public int[] finalPrices(int[] prices) {
        int[] out = prices.clone();
        Deque<Integer> stack = new ArrayDeque<>();
        for (int j = 0; j < prices.length; j++) {
            while (!stack.isEmpty() && prices[stack.peek()] >= prices[j]) out[stack.pop()] -= prices[j];
            stack.push(j);
        }
        return out;
    }
}
''',
test=r'''
class FinalPricesTest {

    private final FinalPrices solution = new FinalPrices();

    @Test
    void examples() {
        assertArrayEquals(new int[]{4, 2, 4, 2, 3}, solution.finalPrices(new int[]{8, 4, 6, 2, 3}));
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, solution.finalPrices(new int[]{1, 2, 3, 4, 5}));
        assertArrayEquals(new int[]{9, 0, 1, 6}, solution.finalPrices(new int[]{10, 1, 1, 6}));
    }
}
''',
trace=r'''
function run(prices) {
  const out = prices.slice(), st = [];
  A.step('Walk the prices. The stack holds items still waiting for a cheaper-or-equal item to their right.', A.arr('prices', prices), A.stack('waiting (index)', st));
  prices.forEach((p, j) => {
    const got = [];
    while (st.length && prices[st[st.length - 1]] >= p) { const i = st.pop(); out[i] -= p; got.push(i); }
    st.push(j);
    A.step(got.length ? `${p} is ≤ the waiting price${got.length > 1 ? 's' : ''} at ${got.join(', ')}: they get ${p} off.` : `${p}: nobody waiting is ≥ it. It starts waiting.`, A.arr('prices', prices, { hl: { [j]: 'cur', ...Object.fromEntries(got.map(i => [i, 'ok'])) } }), A.arr('final', out, { hl: Object.fromEntries(got.map(i => [i, 'ok'])) }), A.stack('waiting (index)', st));
  });
  A.step(`Items still waiting pay full price. Final: [${out}].`, A.arr('final', out));
}
A.scenario('Example', '[8,4,6,2,3]', () => run([8, 4, 6, 2, 3]));
'''),

P(num=1491, slug="average-salary-excluding-the-minimum-and-maximum-salary", title="Average Salary Excluding the Minimum and Maximum Salary", diff="Easy", topic="Array", cls="AverageSalary",
idea="One pass for the sum, the minimum and the maximum.",
vname="Single pass",
spec=r'''
Given unique salaries, return the average excluding the minimum and the maximum salary.

**Example**
```
[4000,3000,1000,2000] → 2500.0
[1000,2000,3000]      → 2000.0
```

**Constraints**
* `3 <= salary.length <= 100`
''',
approach=r'''
**Sum, min, max.** Add everything, then subtract the smallest and largest and divide by `n - 2`.

* Time: **O(n)**.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class AverageSalary {

    public double average(int[] salary) {
        long sum = 0;
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int s : salary) {
            sum += s;
            min = Math.min(min, s);
            max = Math.max(max, s);
        }
        return (double) (sum - min - max) / (salary.length - 2);
    }
}
''',
test=r'''
class AverageSalaryTest {

    private final AverageSalary solution = new AverageSalary();

    @Test
    void examples() {
        assertEquals(2500.0, solution.average(new int[]{4000, 3000, 1000, 2000}), 1e-9);
        assertEquals(2000.0, solution.average(new int[]{1000, 2000, 3000}), 1e-9);
        assertEquals(3500.0, solution.average(new int[]{6000, 5000, 4000, 3000, 2000, 1000}), 1e-9);
    }
}
''',
trace=r'''
function run(s) {
  let sum = 0, min = Infinity, max = -Infinity;
  A.step('One pass: keep the sum, the smallest and the largest salary.', A.arr('salary', s));
  s.forEach((v, i) => { sum += v; min = Math.min(min, v); max = Math.max(max, v); A.step(`Add ${v}.`, A.arr('salary', s, { hl: { [i]: 'cur' } }), A.vars({ sum, min, max })); });
  const avg = (sum - min - max) / (s.length - 2);
  A.step(`(${sum} − ${min} − ${max}) / ${s.length - 2} = ${avg}.`, A.arr('salary', s, { hl: { [s.indexOf(min)]: 'bad', [s.indexOf(max)]: 'bad' } }), A.text('Result', avg, 'ok'));
}
A.scenario('Example', '[4000,3000,1000,2000]', () => run([4000, 3000, 1000, 2000]));
'''),

P(num=1498, slug="number-of-subsequences-that-satisfy-the-given-sum-condition", title="Number of Subsequences That Satisfy the Given Sum Condition", diff="Medium", topic="Two Pointers", cls="NumSubseqSumCondition",
idea="After sorting, only the min and max matter; fixing the min, any subset of elements up to the farthest valid max works.",
vname="Sort, two pointers, powers of two",
spec=r'''
Count the non-empty subsequences of `nums` whose `min + max <= target`. Return the count modulo `10^9 + 7`.

**Example**
```
nums = [3,5,6,7],     target = 9  → 4    ([3], [3,5], [3,5,6], [3,6])
nums = [3,3,6,8],     target = 10 → 6
nums = [2,3,3,4,6,7], target = 12 → 61
```

**Constraints**
* `1 <= nums.length <= 10^5`, `1 <= nums[i], target <= 10^6`
''',
approach=r'''
**Fix the minimum.** A subsequence's min and max do not depend on order, so sort. With `lo` as the minimum, move `hi` left until
`nums[lo] + nums[hi] <= target`. Then every subset of `nums[lo+1..hi]` combined with `nums[lo]` is valid: `2^(hi - lo)` of them. If the
pair fails, `nums[hi]` is too big for every later minimum too, so drop it. Precompute powers of two mod `10^9 + 7`.

* Time: **O(n log n)** — sorting.
* Space: **O(n)** — the powers.
''',
tc="nlogn", sc="n",
java=r'''
public class NumSubseqSumCondition {

    private static final int MOD = 1_000_000_007;

    public int numSubseq(int[] nums, int target) {
        int[] a = nums.clone();
        Arrays.sort(a);
        int n = a.length;
        int[] pow = new int[n];
        pow[0] = 1;
        for (int i = 1; i < n; i++) pow[i] = pow[i - 1] * 2 % MOD;
        int lo = 0, hi = n - 1;
        long count = 0;
        while (lo <= hi) {
            if (a[lo] + a[hi] <= target) count = (count + pow[hi - lo++]) % MOD;
            else hi--;
        }
        return (int) count;
    }
}
''',
test=r'''
class NumSubseqSumConditionTest {

    private final NumSubseqSumCondition solution = new NumSubseqSumCondition();

    @Test
    void examples() {
        assertEquals(4, solution.numSubseq(new int[]{3, 5, 6, 7}, 9));
        assertEquals(6, solution.numSubseq(new int[]{3, 3, 6, 8}, 10));
        assertEquals(61, solution.numSubseq(new int[]{2, 3, 3, 4, 6, 7}, 12));
        assertEquals(0, solution.numSubseq(new int[]{5}, 9));
    }

    @Test
    void largeIsReducedModulo() {
        int[] ones = new int[100];
        Arrays.fill(ones, 1);
        long expected = 1;
        for (int i = 0; i < 100; i++) expected = expected * 2 % 1_000_000_007;
        assertEquals((expected - 1 + 1_000_000_007) % 1_000_000_007, solution.numSubseq(ones, 2));
    }
}
''',
trace=r'''
function run(nums, target) {
  const a = nums.slice().sort((x, y) => x - y); let lo = 0, hi = a.length - 1, count = 0;
  A.step('Sort: only the smallest and largest element of a subsequence matter.', A.arr('sorted', a), A.vars({ target }));
  while (lo <= hi) {
    if (a[lo] + a[hi] <= target) { const w = 2 ** (hi - lo); count += w; A.step(`${a[lo]} + ${a[hi]} ≤ ${target}. With ${a[lo]} as the minimum, any subset of the ${hi - lo} element${hi - lo === 1 ? '' : 's'} after it up to index ${hi} works: 2^${hi - lo} = ${w}.`, A.arr('sorted', a, { range: [lo, hi], ptr: { [lo]: 'lo', [hi]: 'hi' } }), A.vars({ count })); lo++; }
    else { A.step(`${a[lo]} + ${a[hi]} > ${target}: ${a[hi]} is too big for this and every larger minimum. Drop it.`, A.arr('sorted', a, { range: [lo, hi], hl: { [hi]: 'bad' }, ptr: { [lo]: 'lo', [hi]: 'hi' } }), A.vars({ count })); hi--; }
  }
  A.step(`${count} valid subsequences.`, A.text('Result', count, 'ok'));
}
A.scenario('Example', '[3,5,6,7], target 9', () => run([3, 5, 6, 7], 9));
A.scenario('Bigger', '[2,3,3,4,6,7], target 12', () => run([2, 3, 3, 4, 6, 7], 12));
'''),

P(num=1514, slug="path-with-maximum-probability", title="Path with Maximum Probability", diff="Medium", topic="Shortest Path", cls="MaxProbabilityPath",
idea="Dijkstra works for products of probabilities in [0, 1]: a path can only get less likely as it grows.",
vname="Dijkstra with a max-heap",
spec=r'''
An undirected graph has `n` nodes; edge `edges[i]` succeeds with probability `succProb[i]`. Return the highest probability of a path from
`start` to `end` (the product of its edges), or 0 if there is none.

**Example**
```
n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2 → 0.25
n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2 → 0.3
```

**Constraints**
* `2 <= n <= 10^4`, up to `2 * 10^4` edges, `0 <= succProb[i] <= 1`
''',
approach=r'''
**Dijkstra, maximising.** Multiplying by a probability never increases a value, just as adding a non-negative weight never decreases a
distance. So the node with the highest known probability is final when it is popped from a max-heap. Relax each neighbour with
`best[u] * p`; skip stale heap entries.

* Time: **O((V + E) log V)**.
* Space: **O(V + E)** — adjacency and heap.
''',
tc="nlogn", sc="n",
java=r'''
public class MaxProbabilityPath {

    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        int m = edges.length;
        int[] head = new int[n], next = new int[2 * m], to = new int[2 * m];
        double[] prob = new double[2 * m];
        Arrays.fill(head, -1);
        for (int i = 0; i < m; i++)
            for (int side = 0; side < 2; side++) {
                int e = 2 * i + side, u = edges[i][side], v = edges[i][1 - side];
                to[e] = v;
                prob[e] = succProb[i];
                next[e] = head[u];
                head[u] = e;
            }
        double[] best = new double[n];
        best[start] = 1;
        PriorityQueue<double[]> heap = new PriorityQueue<>((a, b) -> Double.compare(b[0], a[0]));
        heap.add(new double[]{1, start});
        while (!heap.isEmpty()) {
            double[] top = heap.poll();
            int u = (int) top[1];
            if (top[0] < best[u]) continue;
            if (u == end) return top[0];
            for (int e = head[u]; e != -1; e = next[e]) {
                double p = top[0] * prob[e];
                if (p > best[to[e]]) {
                    best[to[e]] = p;
                    heap.add(new double[]{p, to[e]});
                }
            }
        }
        return 0;
    }
}
''',
test=r'''
class MaxProbabilityPathTest {

    private final MaxProbabilityPath solution = new MaxProbabilityPath();

    @Test
    void examples() {
        int[][] e = {{0, 1}, {1, 2}, {0, 2}};
        assertEquals(0.25, solution.maxProbability(3, e, new double[]{0.5, 0.5, 0.2}, 0, 2), 1e-9);
        assertEquals(0.3, solution.maxProbability(3, e, new double[]{0.5, 0.5, 0.3}, 0, 2), 1e-9);
        assertEquals(0.0, solution.maxProbability(3, new int[][]{{0, 1}}, new double[]{0.5}, 0, 2), 1e-9);
        assertEquals(0.72, solution.maxProbability(4, new int[][]{{0, 1}, {1, 3}, {0, 2}, {2, 3}}, new double[]{0.9, 0.8, 0.95, 0.7}, 0, 3), 1e-9);
    }
}
''',
trace=r'''
function run(n, edges, probs, s, t) {
  const nodes = [...Array(n).keys()].map(i => ({ id: i })), E = edges.map(([a, b], i) => [a, b, probs[i]]), best = new Array(n).fill(0), done = new Set();
  best[s] = 1;
  A.step(`Start at ${s} with probability 1. Always expand the most likely unfinished node.`, A.graph('graph', nodes, E, { hl: { [s]: 'cur' } }), A.arr('best', best));
  while (true) {
    let u = -1; for (let i = 0; i < n; i++) if (!done.has(i) && best[i] > 0 && (u < 0 || best[i] > best[u])) u = i;
    if (u < 0) { A.step(`${t} cannot be reached.`, A.text('Result', 0, 'bad')); return; }
    done.add(u);
    if (u === t) { A.step(`${t} is the most likely node left, so its probability ${+best[t].toFixed(4)} is final.`, A.graph('graph', nodes, E, { hl: { ...Object.fromEntries([...done].map(d => [d, 'dim'])), [t]: 'ok' } }), A.text('Result', +best[t].toFixed(4), 'ok')); return; }
    const upd = [];
    E.forEach(([a, b, p]) => { const v = a === u ? b : b === u ? a : -1; if (v >= 0 && !done.has(v) && best[u] * p > best[v]) { best[v] = best[u] * p; upd.push(v); } });
    A.step(`Finalise ${u} (${+best[u].toFixed(4)}). ${upd.length ? `Improve ${upd.map(v => `${v} to ${+best[v].toFixed(4)}`).join(', ')}.` : 'No improvements.'}`, A.graph('graph', nodes, E, { hl: { ...Object.fromEntries([...done].map(d => [d, 'dim'])), [u]: 'cur', ...Object.fromEntries(upd.map(v => [v, 'ok'])) } }), A.arr('best', best.map(x => +x.toFixed(4))));
  }
}
A.scenario('Two routes', 'start 0, end 2', () => run(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2));
A.scenario('Four nodes', 'start 0, end 3', () => run(4, [[0, 1], [1, 3], [0, 2], [2, 3]], [0.9, 0.8, 0.95, 0.7], 0, 3));
'''),

P(num=1523, slug="count-odd-numbers-in-an-interval-range", title="Count Odd Numbers in an Interval Range", diff="Easy", topic="Math", cls="CountOddsInRange",
idea="There are (x + 1) / 2 odd numbers in [0, x]; subtract the count below low.",
vname="Prefix count formula",
spec=r'''
Return how many odd numbers lie in `[low, high]` (inclusive).

**Example**
```
low = 3, high = 7  → 3   (3, 5, 7)
low = 8, high = 10 → 1   (9)
```

**Constraints**
* `0 <= low <= high <= 10^9`
''',
approach=r'''
**Prefix counts.** The odd numbers in `[0, x]` number `(x + 1) / 2` (integer division), and those in `[0, low - 1]` number `low / 2`. The
difference is the answer.

* Time: **O(1)**.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class CountOddsInRange {

    public int countOdds(int low, int high) {
        return (high + 1) / 2 - low / 2;
    }
}
''',
test=r'''
class CountOddsInRangeTest {

    private final CountOddsInRange solution = new CountOddsInRange();

    @ParameterizedTest
    @CsvSource({"3,7,3", "8,10,1", "0,0,0", "1,1,1", "2,2,0", "0,1000000000,500000000", "999999999,1000000000,1"})
    void count(int low, int high, int expected) {
        assertEquals(expected, solution.countOdds(low, high));
    }
}
''',
trace=r'''
function run(low, high) {
  const nums = []; for (let x = low; x <= high; x++) nums.push(x);
  A.step(`Count the odd numbers from ${low} to ${high}.`, A.arr('range', nums, { noIdx: true, hl: Object.fromEntries(nums.map((x, i) => [i, x % 2 ? 'ok' : 'dim'])) }));
  A.step(`Odd numbers in [0, ${high}]: (${high} + 1) / 2 = ${Math.floor((high + 1) / 2)}.`, A.vars({ upTo: Math.floor((high + 1) / 2) }));
  A.step(`Odd numbers in [0, ${low - 1 < 0 ? '−1' : low - 1}]: ${low} / 2 = ${Math.floor(low / 2)}.`, A.vars({ upTo: Math.floor((high + 1) / 2), below: Math.floor(low / 2) }));
  const r = Math.floor((high + 1) / 2) - Math.floor(low / 2);
  A.step(`Difference: ${r}.`, A.text('Result', r, 'ok'));
}
A.scenario('Odd ends', 'low 3, high 7', () => run(3, 7));
A.scenario('Even ends', 'low 8, high 10', () => run(8, 10));
'''),

P(num=1539, slug="kth-missing-positive-number", title="Kth Missing Positive Number", diff="Easy", topic="Binary Search", cls="KthMissingPositive",
idea="arr[i] − (i + 1) counts the positives missing before arr[i]; binary search where that count reaches k.",
vname="Binary search on missing counts",
spec=r'''
Given a strictly increasing array of positive integers and `k`, return the `k`-th positive integer missing from the array.

**Example**
```
arr = [2,3,4,7,11], k = 5 → 9    (missing: 1,5,6,8,9,…)
arr = [1,2,3,4],    k = 2 → 6
```

**Constraints**
* `1 <= arr.length <= 1000`, `1 <= arr[i], k <= 1000`
''',
approach=r'''
**Missing counter.** Before `arr[i]` there are `arr[i] - (i + 1)` missing positives, and this count never decreases. Binary search for the
first index `lo` whose count is at least `k`. Exactly `lo` array values are below the answer, so the answer is `lo + k`.

* Time: **O(log n)**.
* Space: **O(1)**.
''',
tc="log", sc="1",
java=r'''
public class KthMissingPositive {

    public int findKthPositive(int[] arr, int k) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] - mid - 1 < k) lo = mid + 1;
            else hi = mid;
        }
        return lo + k;
    }
}
''',
test=r'''
class KthMissingPositiveTest {

    private final KthMissingPositive solution = new KthMissingPositive();

    @Test
    void examples() {
        assertEquals(9, solution.findKthPositive(new int[]{2, 3, 4, 7, 11}, 5));
        assertEquals(6, solution.findKthPositive(new int[]{1, 2, 3, 4}, 2));
        assertEquals(1, solution.findKthPositive(new int[]{5}, 1));
        assertEquals(6, solution.findKthPositive(new int[]{5}, 5));
    }
}
''',
trace=r'''
function run(arr, k) {
  const miss = arr.map((v, i) => v - i - 1); let lo = 0, hi = arr.length;
  A.step(`missing[i] = arr[i] − (i + 1): how many positives are missing before arr[i]. Find where it reaches ${k}.`, A.arr('arr', arr), A.arr('missing before', miss));
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    A.step(`mid = ${mid}: ${miss[mid]} missing before ${arr[mid]}, ${miss[mid] < k ? `fewer than ${k}, go right` : `at least ${k}, go left`}.`, A.arr('missing before', miss, { range: [lo, hi - 1], ptr: { [mid]: 'mid' } }), A.vars({ lo, hi }));
    if (miss[mid] < k) lo = mid + 1; else hi = mid;
  }
  A.step(`${lo} array value${lo === 1 ? ' is' : 's are'} below the answer, so it is ${lo} + ${k} = ${lo + k}.`, A.text('Result', lo + k, 'ok'));
}
A.scenario('Example', '[2,3,4,7,11], k = 5', () => run([2, 3, 4, 7, 11], 5));
'''),

P(num=1544, slug="make-the-string-great", title="Make The String Great", diff="Easy", topic="Stack", cls="MakeStringGreat",
idea="Use the output as a stack; drop the top whenever the next letter is the same letter in the other case.",
vname="Stack of letters",
spec=r'''
A string is **good** if no two adjacent characters are the same letter in different cases (like `"aA"`). Repeatedly remove such adjacent
pairs and return the resulting string (possibly empty).

**Example**
```
"leEeetcode" → "leetcode"
"abBAcC"     → ""
"s"          → "s"
```

**Constraints**
* `1 <= s.length <= 100`, English letters
''',
approach=r'''
**Stack.** Read characters left to right. If the next one and the top of the stack differ exactly by the case offset (`|a - b| == 32`),
pop; otherwise push. Removing a pair can expose a new pair, which the stack handles automatically.

* Time: **O(n)**.
* Space: **O(n)**.
''',
tc="n", sc="n",
java=r'''
public class MakeStringGreat {

    public String makeGood(String s) {
        StringBuilder stack = new StringBuilder();
        for (char c : s.toCharArray()) {
            int n = stack.length();
            if (n > 0 && Math.abs(stack.charAt(n - 1) - c) == 'a' - 'A') stack.setLength(n - 1);
            else stack.append(c);
        }
        return stack.toString();
    }
}
''',
test=r'''
class MakeStringGreatTest {

    private final MakeStringGreat solution = new MakeStringGreat();

    @Test
    void examples() {
        assertEquals("leetcode", solution.makeGood("leEeetcode"));
        assertEquals("", solution.makeGood("abBAcC"));
        assertEquals("s", solution.makeGood("s"));
        assertEquals("aa", solution.makeGood("aa"));
        assertEquals("", solution.makeGood("PpXxPxXp"));
    }
}
''',
trace=r'''
function run(s) {
  const st = [];
  A.step('Push letters; a letter that is the other-case twin of the top cancels it.', A.chars('s', s), A.stack('stack', st));
  [...s].forEach((c, i) => {
    const top = st[st.length - 1];
    if (top !== undefined && top !== c && top.toLowerCase() === c.toLowerCase()) { st.pop(); A.step(`'${c}' and '${top}' are the same letter in different cases: remove both.`, A.chars('s', s, { hl: { [i]: 'bad' } }), A.stack('stack', st)); }
    else { st.push(c); A.step(`Push '${c}'.`, A.chars('s', s, { hl: { [i]: 'cur' } }), A.stack('stack', st)); }
  });
  A.step(`Result: "${st.join('')}".`, A.text('Result', `"${st.join('')}"`, 'ok'));
}
A.scenario('Cascade', '"abBAcC"', () => run('abBAcC'));
A.scenario('One pair', '"leEeetcode"', () => run('leEeetcode'));
'''),
]
