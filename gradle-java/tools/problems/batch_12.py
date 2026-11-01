BS_TRACE_HELPERS = r'''
const bsView = (label, a, lo, hi, mid, extra = {}) => A.arr(label, a, { range: [lo, hi], ptr: [[lo, 'lo'], [hi, 'hi'], ...(mid >= 0 ? [[mid, 'mid']] : [])], hl: { ...(mid >= 0 ? { [mid]: 'cur' } : {}), ...extra } });
'''

PROBLEMS = [
P(num=23, slug="merge-k-sorted-lists", title="Merge k Sorted Lists", diff="Hard", topic="Divide & Conquer", cls="MergeKSortedLists",
idea="Merge the lists in pairs, round after round, like the upper levels of merge sort.",
vname="Pairwise divide and conquer", helpers=["ListNode"],
spec=r'''
You are given an array of `k` linked lists, each sorted ascending. Merge them into one sorted linked list and return its head.

**Example**
```
Input:  [[1,4,5],[1,3,4],[2,6]]
Output: 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

**Constraints**
* `0 <= k <= 10^4`; total nodes `N <= 10^4`
''',
approach=r'''
**Merge in rounds.** In each round merge list `i` with list `i + step` for `step = 1, 2, 4, …`. Each round halves the number of lists,
and every node takes part in one merge per round.

* Time: **O(N log k)** — log k rounds, each touching all N nodes.
* Space: **O(1)** — nodes are re-linked in place.
''',
tc="nlogn", sc="1",
java=r'''
public class MergeKSortedLists {

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        ListNode[] a = lists.clone();
        for (int step = 1; step < a.length; step *= 2) {
            for (int i = 0; i + step < a.length; i += 2 * step) {
                a[i] = merge(a[i], a[i + step]);
            }
        }
        return a[0];
    }

    private static ListNode merge(ListNode x, ListNode y) {
        ListNode dummy = new ListNode(0), tail = dummy;
        while (x != null && y != null) {
            if (x.val <= y.val) { tail.next = x; x = x.next; } else { tail.next = y; y = y.next; }
            tail = tail.next;
        }
        tail.next = x != null ? x : y;
        return dummy.next;
    }
}
''',
test=r'''
class MergeKSortedListsTest {

    private final MergeKSortedLists solution = new MergeKSortedLists();

    @Test
    void three() {
        ListNode[] lists = {ListNode.of(1, 4, 5), ListNode.of(1, 3, 4), ListNode.of(2, 6)};
        assertArrayEquals(new int[]{1, 1, 2, 3, 4, 4, 5, 6}, ListNode.toArray(solution.mergeKLists(lists)));
    }

    @Test
    void empty() {
        assertNull(solution.mergeKLists(new ListNode[]{}));
        assertNull(solution.mergeKLists(new ListNode[]{null}));
    }

    @Test
    void many() {
        ListNode[] lists = new ListNode[7];
        for (int i = 0; i < 7; i++) lists[i] = ListNode.of(i, i + 7, i + 14);
        int[] expected = new int[21];
        for (int i = 0; i < 21; i++) expected[i] = i;
        assertArrayEquals(expected, ListNode.toArray(solution.mergeKLists(lists)));
    }
}
''',
trace=r'''
function run(lists) {
  let a = lists.map(l => l.slice());
  const merge = (x, y) => { const m = []; let i = 0, j = 0; while (i < x.length && j < y.length) m.push(x[i] <= y[j] ? x[i++] : y[j++]); return m.concat(x.slice(i), y.slice(j)); };
  A.step(`${a.length} sorted lists. Merge them in pairs, round by round.`, ...a.map((l, i) => A.list(`list ${i}`, l)));
  for (let step = 1; step < a.length; step *= 2) {
    for (let i = 0; i + step < a.length; i += 2 * step) {
      const m = merge(a[i], a[i + step]);
      A.step(`Round with step ${step}: merge list ${i} and list ${i + step}.`, A.list(`list ${i}`, a[i], { hl: a[i].map((_, t) => [t, 'sel']) }), A.list(`list ${i + step}`, a[i + step], { hl: a[i + step].map((_, t) => [t, 'alt']) }), A.list('merged', m, { hl: m.map((_, t) => [t, 'ok']) }));
      a[i] = m; a[i + step] = [];
    }
  }
  A.step(`Done after ${Math.ceil(Math.log2(lists.length))} rounds.`, A.list('result', a[0], { hl: a[0].map((_, t) => [t, 'ok']) }));
}
A.scenario('Three lists', '[[1,4,5],[1,3,4],[2,6]]', () => run([[1, 4, 5], [1, 3, 4], [2, 6]]));
A.scenario('Four lists', '[[1,9],[2,5],[3,4],[0,8]]', () => run([[1, 9], [2, 5], [3, 4], [0, 8]]));
''',
variants=[dict(
name="Min-heap of list heads",
idea="A priority queue always hands out the smallest current head among the k lists.",
approach=r'''
**Priority queue.** Push every non-null head into a min-heap keyed by value. Pop the smallest, append it, and push its `next`.

* Time: **O(N log k)** — each of N nodes is pushed and popped from a heap of size k.
* Space: **O(k)** — the heap.
''',
tc="nlogn", sc="n",
java=r'''
public class MergeKSortedLists {

    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> heap = new PriorityQueue<>(Comparator.comparingInt(n -> n.val));
        for (ListNode l : lists) if (l != null) heap.add(l);
        ListNode dummy = new ListNode(0), tail = dummy;
        while (!heap.isEmpty()) {
            ListNode n = heap.poll();
            tail.next = n;
            tail = n;
            if (n.next != null) heap.add(n.next);
        }
        return dummy.next;
    }
}
''',
trace=r'''
function run(lists) {
  const idx = lists.map(() => 0), out = [];
  const heap = () => lists.map((l, i) => (idx[i] < l.length ? `${l[idx[i]]} (list ${i})` : null)).filter(Boolean).sort((a, b) => parseInt(a) - parseInt(b));
  A.step('Put the head of every list in a min-heap.', ...lists.map((l, i) => A.list(`list ${i}`, l)), A.arr('heap', heap()));
  while (true) {
    let best = -1; lists.forEach((l, i) => { if (idx[i] < l.length && (best < 0 || l[idx[i]] < lists[best][idx[best]])) best = i; });
    if (best < 0) break;
    out.push(lists[best][idx[best]]); idx[best]++;
    A.step(`Pop ${out[out.length - 1]} from list ${best} and push its successor${idx[best] < lists[best].length ? ` ${lists[best][idx[best]]}` : ' (none)'}.`, A.arr('heap', heap()), A.list('merged', out, { hl: { [out.length - 1]: 'ok' } }));
  }
}
A.scenario('Three lists', '[[1,4,5],[1,3,4],[2,6]]', () => run([[1, 4, 5], [1, 3, 4], [2, 6]]));
''')]),

P(num=53, slug="maximum-subarray", title="Maximum Subarray", diff="Medium", topic="Kadane's Algorithm", cls="MaximumSubarray",
idea="Kadane: the best subarray ending here either extends the previous one or starts fresh at this element.",
vname="Kadane's algorithm",
spec=r'''
Given an integer array `nums`, find the contiguous subarray (at least one element) with the largest sum, and return that sum.

**Example 1**
```
Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6   ([4,-1,2,1])
```

**Example 2**
```
Input:  nums = [-1]
Output: -1
```

**Constraints**
* `1 <= nums.length <= 10^5`; `-10^4 <= nums[i] <= 10^4`
''',
approach=r'''
**Kadane's algorithm.** `cur` = best sum of a subarray ending at `i` = `max(nums[i], cur + nums[i])`: extending only helps if `cur`
is positive. Track the maximum `cur` ever seen.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two numbers.
''',
java=r'''
public class MaximumSubarray {

    public int maxSubArray(int[] nums) {
        int cur = nums[0], best = nums[0];
        for (int i = 1; i < nums.length; i++) {
            cur = Math.max(nums[i], cur + nums[i]);
            best = Math.max(best, cur);
        }
        return best;
    }
}
''',
test=r'''
class MaximumSubarrayTest {

    private final MaximumSubarray solution = new MaximumSubarray();

    @Test
    void classic() {
        assertEquals(6, solution.maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}));
    }

    @Test
    void allNegative() {
        assertEquals(-1, solution.maxSubArray(new int[]{-3, -1, -2}));
    }

    @Test
    void wholeArray() {
        assertEquals(23, solution.maxSubArray(new int[]{5, 4, -1, 7, 8}));
    }
}
''',
trace=r'''
function run(a) {
  let cur = a[0], best = a[0], start = 0, bs = 0, be = 0;
  A.step('cur is the best sum of a subarray ending at the current index. Start with the first element.', A.arr('nums', a, { range: [0, 0] }), A.vars({ cur, best }));
  for (let i = 1; i < a.length; i++) {
    const prev = cur, fresh = a[i] > prev + a[i];
    if (fresh) { cur = a[i]; start = i; } else cur += a[i];
    const nb = cur > best;
    if (nb) { best = cur; bs = start; be = i; }
    A.step(fresh ? `The sum so far is ${prev}, which is negative, so ${a[i]} alone (${a[i]}) beats extending (${prev + a[i]}). Restart the subarray at index ${i}.${nb ? ' New best.' : ''}` : `Extend the subarray with ${a[i]}: cur = ${prev} + ${a[i]} = ${cur}.${nb ? ' New best.' : ''}`, A.arr('nums', a, { range: [start, i], hl: { [i]: fresh ? 'alt' : 'cur' } }), A.vars({ cur, best }));
  }
  A.step(`The best subarray is indices ${bs}..${be}, with sum ${best}.`, A.arr('nums', a, { range: [bs, be], hl: Object.fromEntries([...Array(be - bs + 1).keys()].map(t => [bs + t, 'ok'])) }), A.text('Result', best, 'ok'));
}
A.scenario('Classic', 'nums = [-2,1,-3,4,-1,2,1,-5,4]', () => run([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
A.scenario('Edge: all negative', 'nums = [-3,-1,-2]', () => run([-3, -1, -2]));
''',
variants=[dict(
name="Brute force over all starts",
idea="For each start, extend to every end, keeping a running sum.",
approach=r'''
**All subarrays.** For each start `i`, accumulate `sum` while extending `j` and keep the maximum.

* Time: **O(n²)** — about n²/2 subarrays.
* Space: **O(1)** — a running sum.
''',
java=r'''
public class MaximumSubarray {

    public int maxSubArray(int[] nums) {
        int best = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                best = Math.max(best, sum);
            }
        }
        return best;
    }
}
''',
trace=r'''
function run(a) {
  let best = -Infinity, checks = 0;
  for (let i = 0; i < a.length; i++) {
    let sum = 0, bj = i, bsum = -Infinity;
    for (let j = i; j < a.length; j++) { sum += a[j]; checks++; if (sum > bsum) { bsum = sum; bj = j; } }
    if (bsum > best) best = bsum;
    A.step(`Start ${i}: the best end is ${bj}, with sum ${bsum}. Overall best: ${best}.`, A.arr('nums', a, { range: [i, bj], hl: { [i]: 'cur' } }), A.vars({ best, subarraysChecked: checks }));
  }
  A.step(`${checks} subarrays checked. The answer is ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', 'nums = [-2,1,-3,4,-1,2,1,-5,4]', () => run([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
''')]),

P(num=918, slug="maximum-sum-circular-subarray", title="Maximum Sum Circular Subarray", diff="Medium", topic="Kadane's Algorithm", cls="MaximumCircularSubarray",
idea="A wrapping subarray is the total minus a minimum middle subarray; take the better of that and normal Kadane.",
vname="Max and min Kadane",
spec=r'''
`nums` is a **circular** array (the end connects to the start). Return the maximum possible sum of a non-empty subarray, where each
element may be used at most once.

**Example 1**
```
Input:  nums = [5,-3,5]
Output: 10   ([5,5], wrapping around)
```

**Example 2**
```
Input:  nums = [-3,-2,-3]
Output: -2
```

**Constraints**
* `1 <= n <= 3 * 10^4`; `-3 * 10^4 <= nums[i] <= 3 * 10^4`
''',
approach=r'''
**Two Kadanes in one pass.** The best subarray either does not wrap (normal Kadane maximum) or wraps, in which case it is
`total - (minimum subarray)`. If every number is negative, the minimum subarray is the whole array and the wrap formula would give an
empty subarray, so return the normal maximum.

* Time: **O(n)** — one pass.
* Space: **O(1)** — a few running sums.
''',
java=r'''
public class MaximumCircularSubarray {

    public int maxSubarraySumCircular(int[] nums) {
        int total = 0, curMax = 0, curMin = 0, best = nums[0], worst = nums[0];
        for (int x : nums) {
            curMax = Math.max(x, curMax + x);
            best = Math.max(best, curMax);
            curMin = Math.min(x, curMin + x);
            worst = Math.min(worst, curMin);
            total += x;
        }
        return best < 0 ? best : Math.max(best, total - worst);
    }
}
''',
test=r'''
class MaximumCircularSubarrayTest {

    private final MaximumCircularSubarray solution = new MaximumCircularSubarray();

    @ParameterizedTest
    @CsvSource(value = {"1,-2,3,-2:3", "5,-3,5:10", "-3,-2,-3:-2", "3,-1,2,-1:4", "-2:-2"}, delimiter = ':')
    void finds(String nums, int expected) {
        int[] a = Arrays.stream(nums.split(",")).mapToInt(Integer::parseInt).toArray();
        assertEquals(expected, solution.maxSubarraySumCircular(a));
    }
}
''',
trace=r'''
function run(a) {
  let total = 0, cmax = 0, cmin = 0, best = a[0], worst = a[0];
  A.step('Track the best subarray (normal Kadane) and the worst subarray at the same time. A wrapping answer equals total minus the worst middle part.', A.arr('nums', a), A.vars({ best, worst, total }));
  a.forEach((x, i) => {
    cmax = Math.max(x, cmax + x); best = Math.max(best, cmax);
    cmin = Math.min(x, cmin + x); worst = Math.min(worst, cmin);
    total += x;
    A.step(`Index ${i} (${x}): best ending here ${cmax}, worst ending here ${cmin}.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.vars({ best, worst, total }));
  });
  const wrap = total - worst, res = best < 0 ? best : Math.max(best, wrap);
  A.step(best < 0 ? `Every number is negative, so the answer is the single largest value: ${best}.` : `Without wrapping: ${best}. With wrapping: ${total} − (${worst}) = ${wrap}. The answer is ${res}.`, A.text('Result', res, 'ok'));
}
A.scenario('Wrapping wins', 'nums = [5,-3,5]', () => run([5, -3, 5]));
A.scenario('No wrap', 'nums = [1,-2,3,-2]', () => run([1, -2, 3, -2]));
A.scenario('Edge: all negative', 'nums = [-3,-2,-3]', () => run([-3, -2, -3]));
'''),

P(num=35, slug="search-insert-position", title="Search Insert Position", diff="Easy", topic="Binary Search", cls="SearchInsertPosition",
idea="Binary search for the first index whose value is at least the target.",
vname="Lower-bound binary search",
spec=r'''
Given a sorted array of **distinct** integers and a `target`, return the index of `target` if present, otherwise the index where it
would be inserted to keep the order. Run in O(log n).

**Example**
```
nums = [1,3,5,6]:  target 5 → 2,  target 2 → 1,  target 7 → 4
```

**Constraints**
* `1 <= nums.length <= 10^4`; sorted and distinct.
''',
approach=r'''
**Lower bound.** Search `[lo, hi)` with `hi = n`. If `nums[mid] < target`, the answer is right of `mid`; otherwise it is `mid` or
to its left. When `lo == hi`, that is the first index with `nums[i] >= target`.

* Time: **O(log n)** — the range halves each step.
* Space: **O(1)** — two indices.
''',
java=r'''
public class SearchInsertPosition {

    public int searchInsert(int[] nums, int target) {
        int lo = 0, hi = nums.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] < target) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
}
''',
test=r'''
class SearchInsertPositionTest {

    private final SearchInsertPosition solution = new SearchInsertPosition();

    @ParameterizedTest
    @CsvSource({"5,2", "2,1", "7,4", "0,0", "1,0", "6,3"})
    void finds(int target, int expected) {
        assertEquals(expected, solution.searchInsert(new int[]{1, 3, 5, 6}, target));
    }
}
''',
trace=BS_TRACE_HELPERS + r'''
function run(a, t) {
  let lo = 0, hi = a.length;
  A.step(`Find the first index whose value is at least ${t}. The search range is [lo, hi).`, A.arr('nums', a), A.vars({ target: t, lo, hi }));
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    const right = a[mid] < t;
    A.step(`mid = ${mid}: ${a[mid]} ${right ? `< ${t}, so the answer is to the right` : `≥ ${t}, so the answer is mid or to the left`}.`, bsView('nums', a, lo, Math.min(hi, a.length - 1), mid), A.vars({ target: t, lo, hi }));
    if (right) lo = mid + 1; else hi = mid;
  }
  A.step(lo < a.length && a[lo] === t ? `Found ${t} at index ${lo}.` : `${t} is not present; it would be inserted at index ${lo}.`, A.arr('nums', a, { ptr: [[Math.min(lo, a.length - 1), lo < a.length ? 'insert' : 'end']], hl: lo < a.length ? { [lo]: 'ok' } : {} }), A.text('Result', lo, 'ok'));
}
A.scenario('Present', 'nums = [1,3,5,6], target = 5', () => run([1, 3, 5, 6], 5));
A.scenario('Insert in the middle', 'nums = [1,3,5,6,8,10], target = 7', () => run([1, 3, 5, 6, 8, 10], 7));
A.scenario('Edge: past the end', 'nums = [1,3,5,6], target = 7', () => run([1, 3, 5, 6], 7));
'''),

P(num=74, slug="search-a-2d-matrix", title="Search a 2D Matrix", diff="Medium", topic="Binary Search", cls="Search2DMatrix",
idea="Rows are sorted and each row starts after the previous one ends, so the matrix is one sorted list in disguise.",
vname="Binary search on the flattened index",
spec=r'''
In an `m × n` matrix, each row is sorted ascending and the first value of each row is greater than the last value of the previous row.
Return `true` if `target` is in the matrix. Run in O(log(m·n)).

**Example**
```
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]:  target 3 → true,  target 13 → false
```

**Constraints**
* `1 <= m, n <= 100`
''',
approach=r'''
**One virtual array.** Index `k` in `[0, m·n)` maps to `matrix[k / n][k % n]`. Run an ordinary binary search on `k`.

* Time: **O(log(m·n))** — standard binary search over m·n cells.
* Space: **O(1)** — a few indices.
''',
tc="log",
java=r'''
public class Search2DMatrix {

    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length, lo = 0, hi = m * n - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            int v = matrix[mid / n][mid % n];
            if (v == target) return true;
            if (v < target) lo = mid + 1; else hi = mid - 1;
        }
        return false;
    }
}
''',
test=r'''
class Search2DMatrixTest {

    private final Search2DMatrix solution = new Search2DMatrix();
    private final int[][] matrix = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};

    @ParameterizedTest
    @CsvSource({"3,true", "13,false", "1,true", "60,true", "0,false", "61,false"})
    void searches(int target, boolean expected) {
        assertEquals(expected, solution.searchMatrix(matrix, target));
    }
}
''',
trace=r'''
function run(m, t) {
  const R = m.length, C = m[0].length; let lo = 0, hi = R * C - 1;
  const cell = k => `${Math.floor(k / C)},${k % C}`;
  const hl = (mid) => { const o = []; for (let k = 0; k < R * C; k++) o.push([cell(k), k === mid ? 'cur' : k < lo || k > hi ? 'dim' : 'sel']); return o; };
  A.step(`Read the rows one after another and the matrix is a single sorted list of ${R * C} values. Index k is cell (k ÷ ${C}, k mod ${C}).`, A.grid('matrix', m, { hl: hl(-1) }), A.vars({ target: t, lo, hi }));
  while (lo <= hi) {
    const mid = (lo + hi) >> 1, v = m[Math.floor(mid / C)][mid % C];
    if (v === t) { A.step(`k = ${mid} is cell (${cell(mid)}), holding ${v}. Found it.`, A.grid('matrix', m, { hl: [[cell(mid), 'ok']] }), A.text('Result', 'true', 'ok')); return; }
    A.step(`k = ${mid} is cell (${cell(mid)}), holding ${v}: ${v < t ? 'too small, so search right' : 'too big, so search left'}.`, A.grid('matrix', m, { hl: hl(mid) }), A.vars({ target: t, lo, hi, mid }));
    if (v < t) lo = mid + 1; else hi = mid - 1;
  }
  A.step(`The range is empty: ${t} is not in the matrix.`, A.grid('matrix', m, { hl: hl(-1) }), A.text('Result', 'false', 'bad'));
}
A.scenario('Present', 'target = 11', () => run([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 11));
A.scenario('Absent', 'target = 13', () => run([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13));
'''),

P(num=162, slug="find-peak-element", title="Find Peak Element", diff="Medium", topic="Binary Search", cls="FindPeakElement",
idea="Walk uphill: if the next element is larger, a peak lies to the right; otherwise mid is on a downslope or a peak.",
vname="Binary search uphill",
spec=r'''
A **peak** is an element strictly greater than its neighbours. Given `nums` (with `nums[-1] = nums[n] = -∞` and no two adjacent values
equal), return the index of **any** peak, in O(log n).

**Example**
```
Input:  nums = [1,2,1,3,5,6,4]
Output: 1 or 5
```

**Constraints**
* `1 <= nums.length <= 1000`; `nums[i] != nums[i + 1]`
''',
approach=r'''
**Follow the slope.** If `nums[mid] < nums[mid + 1]`, the values rise to the right and must eventually come down (the edge is −∞),
so a peak exists in `mid + 1 .. hi`. Otherwise a peak exists in `lo .. mid`. Stop when `lo == hi`.

* Time: **O(log n)** — the range halves each step.
* Space: **O(1)** — two indices.
''',
java=r'''
public class FindPeakElement {

    public int findPeakElement(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] < nums[mid + 1]) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
}
''',
test=r'''
class FindPeakElementTest {

    private final FindPeakElement solution = new FindPeakElement();

    private static boolean isPeak(int[] a, int i) {
        return (i == 0 || a[i] > a[i - 1]) && (i == a.length - 1 || a[i] > a[i + 1]);
    }

    @Test
    void examples() {
        int[] a = {1, 2, 3, 1};
        assertEquals(2, solution.findPeakElement(a));
        int[] b = {1, 2, 1, 3, 5, 6, 4};
        assertTrue(isPeak(b, solution.findPeakElement(b)));
    }

    @Test
    void edges() {
        assertEquals(0, solution.findPeakElement(new int[]{1}));
        assertEquals(0, solution.findPeakElement(new int[]{3, 2, 1}));
        assertEquals(2, solution.findPeakElement(new int[]{1, 2, 3}));
    }
}
''',
trace=BS_TRACE_HELPERS + r'''
function run(a) {
  let lo = 0, hi = a.length - 1;
  A.step('Both ends are treated as −∞, so walking uphill must reach a peak somewhere.', A.arr('nums', a));
  while (lo < hi) {
    const mid = (lo + hi) >> 1, up = a[mid] < a[mid + 1];
    A.step(`mid = ${mid}: ${a[mid]} ${up ? `< ${a[mid + 1]}, so the slope rises to the right and a peak lies there` : `> ${a[mid + 1]}, so mid is a peak or a peak lies to its left`}.`, bsView('nums', a, lo, hi, mid, { [mid + 1]: 'alt' }));
    if (up) lo = mid + 1; else hi = mid;
  }
  A.step(`lo meets hi at index ${lo}: ${a[lo]} is a peak.`, A.arr('nums', a, { hl: { [lo]: 'ok' } }), A.text('Result', lo, 'ok'));
}
A.scenario('Two peaks', 'nums = [1,2,1,3,5,6,4]', () => run([1, 2, 1, 3, 5, 6, 4]));
''',
variants=[dict(
name="Linear scan",
idea="Return the first index whose next value is smaller.",
approach=r'''
**Scan.** The first `i` with `nums[i] > nums[i + 1]` is a peak (everything before it rises). If none, the last index is a peak.

* Time: **O(n)** — a single scan.
* Space: **O(1)** — one index.
''',
java=r'''
public class FindPeakElement {

    public int findPeakElement(int[] nums) {
        for (int i = 0; i + 1 < nums.length; i++) {
            if (nums[i] > nums[i + 1]) return i;
        }
        return nums.length - 1;
    }
}
''',
trace=r'''
function run(a) {
  for (let i = 0; i + 1 < a.length; i++) {
    if (a[i] > a[i + 1]) { A.step(`${a[i]} > ${a[i + 1]}, and everything before it was rising, so index ${i} is a peak.`, A.arr('nums', a, { hl: { [i]: 'ok' } }), A.text('Result', i, 'ok')); return; }
    A.step(`${a[i]} < ${a[i + 1]}: still rising.`, A.arr('nums', a, { hl: { [i]: 'cur' } }));
  }
  A.step('Rising all the way, so the last index is a peak.', A.text('Result', a.length - 1, 'ok'));
}
A.scenario('Two peaks', 'nums = [1,2,1,3,5,6,4]', () => run([1, 2, 1, 3, 5, 6, 4]));
''')]),

P(num=33, slug="search-in-rotated-sorted-array", title="Search in Rotated Sorted Array", diff="Medium", topic="Binary Search", cls="SearchRotatedArray",
idea="One half around mid is always sorted; check whether the target lies inside that sorted half.",
vname="Binary search on the sorted half",
spec=r'''
A sorted array of **distinct** integers was rotated at an unknown pivot (e.g. `[0,1,2,4,5,6,7]` → `[4,5,6,7,0,1,2]`). Return the index
of `target`, or `-1`, in O(log n).

**Example**
```
nums = [4,5,6,7,0,1,2]:  target 0 → 4,  target 3 → -1
```

**Constraints**
* `1 <= nums.length <= 5000`; values are distinct.
''',
approach=r'''
**Pick the sorted half.** If `nums[lo] <= nums[mid]`, the left half `lo..mid` is sorted: go left if the target lies in
`[nums[lo], nums[mid])`, otherwise go right. Otherwise the right half `mid..hi` is sorted: go right if the target lies in
`(nums[mid], nums[hi]]`, otherwise go left.

* Time: **O(log n)** — the range halves each step.
* Space: **O(1)** — a few indices.
''',
java=r'''
public class SearchRotatedArray {

    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] == target) return mid;
            if (nums[lo] <= nums[mid]) {
                if (nums[lo] <= target && target < nums[mid]) hi = mid - 1; else lo = mid + 1;
            } else {
                if (nums[mid] < target && target <= nums[hi]) lo = mid + 1; else hi = mid - 1;
            }
        }
        return -1;
    }
}
''',
test=r'''
class SearchRotatedArrayTest {

    private final SearchRotatedArray solution = new SearchRotatedArray();

    @ParameterizedTest
    @CsvSource({"0,4", "3,-1", "4,0", "2,6", "7,3"})
    void searches(int target, int expected) {
        assertEquals(expected, solution.search(new int[]{4, 5, 6, 7, 0, 1, 2}, target));
    }

    @Test
    void single() {
        assertEquals(-1, solution.search(new int[]{1}, 0));
        assertEquals(0, solution.search(new int[]{1}, 1));
    }
}
''',
trace=BS_TRACE_HELPERS + r'''
function run(a, t) {
  let lo = 0, hi = a.length - 1;
  A.step(`The array was sorted and then rotated. Look for ${t}.`, A.arr('nums', a), A.vars({ target: t }));
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    if (a[mid] === t) { A.step(`nums[${mid}] = ${t}. Found it.`, A.arr('nums', a, { hl: { [mid]: 'ok' } }), A.text('Result', mid, 'ok')); return; }
    const leftSorted = a[lo] <= a[mid];
    const sorted = leftSorted ? [lo, mid] : [mid, hi];
    const inside = leftSorted ? a[lo] <= t && t < a[mid] : a[mid] < t && t <= a[hi];
    const sh = {}; for (let i = sorted[0]; i <= sorted[1]; i++) sh[i] = 'sel'; sh[mid] = 'cur';
    A.step(`mid = ${mid} (${a[mid]}). The ${leftSorted ? 'left' : 'right'} half ${a[sorted[0]]}..${a[sorted[1]]} is sorted (blue). ${t} is ${inside ? '' : 'not '}inside it, so go ${inside === leftSorted ? 'left' : 'right'}.`, bsView('nums', a, lo, hi, mid, sh), A.vars({ target: t, lo, hi }));
    if (inside === leftSorted) hi = mid - 1; else lo = mid + 1;
  }
  A.step(`${t} is not in the array.`, A.text('Result', -1, 'bad'));
}
A.scenario('Found after the pivot', 'nums = [4,5,6,7,0,1,2], target = 0', () => run([4, 5, 6, 7, 0, 1, 2], 0));
A.scenario('Absent', 'nums = [4,5,6,7,0,1,2], target = 3', () => run([4, 5, 6, 7, 0, 1, 2], 3));
'''),

P(num=34, slug="find-first-and-last-position-of-element-in-sorted-array", title="Find First and Last Position of Element in Sorted Array", diff="Medium", topic="Binary Search", cls="FirstAndLastPosition",
idea="Two lower-bound searches: the first index ≥ target, and the first index ≥ target + 1.",
vname="Two lower bounds",
spec=r'''
Given a sorted array `nums`, return the first and last index of `target` as `[first, last]`, or `[-1, -1]` if it is absent. Run in
O(log n).

**Example**
```
nums = [5,7,7,8,8,10]:  target 8 → [3,4],  target 6 → [-1,-1]
```

**Constraints**
* `0 <= nums.length <= 10^5`; sorted non-decreasing.
''',
approach=r'''
**Lower bound twice.** `lower(x)` is the first index whose value is `>= x`. Then `first = lower(target)`; if it is out of range or not
equal to the target, return `[-1, -1]`. Otherwise `last = lower(target + 1) - 1`.

* Time: **O(log n)** — two binary searches.
* Space: **O(1)** — a few indices.
''',
java=r'''
public class FirstAndLastPosition {

    public int[] searchRange(int[] nums, int target) {
        int first = lower(nums, target);
        if (first == nums.length || nums[first] != target) return new int[]{-1, -1};
        return new int[]{first, lower(nums, (long) target + 1) - 1};
    }

    private static int lower(int[] nums, long x) {
        int lo = 0, hi = nums.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] < x) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
}
''',
test=r'''
class FirstAndLastPositionTest {

    private final FirstAndLastPosition solution = new FirstAndLastPosition();

    @Test
    void present() {
        assertArrayEquals(new int[]{3, 4}, solution.searchRange(new int[]{5, 7, 7, 8, 8, 10}, 8));
    }

    @Test
    void absent() {
        assertArrayEquals(new int[]{-1, -1}, solution.searchRange(new int[]{5, 7, 7, 8, 8, 10}, 6));
        assertArrayEquals(new int[]{-1, -1}, solution.searchRange(new int[]{}, 0));
    }

    @Test
    void maxValue() {
        assertArrayEquals(new int[]{0, 1}, solution.searchRange(new int[]{2147483647, 2147483647}, 2147483647));
    }
}
''',
trace=BS_TRACE_HELPERS + r'''
function run(a, t) {
  const lower = (x, name) => {
    let lo = 0, hi = a.length;
    while (lo < hi) { const mid = (lo + hi) >> 1; A.step(`${name}: mid = ${mid}, value ${a[mid]} ${a[mid] < x ? `< ${x}, so go right` : `≥ ${x}, so go left`}.`, bsView('nums', a, lo, Math.min(hi, a.length - 1), mid)); if (a[mid] < x) lo = mid + 1; else hi = mid; }
    return lo;
  };
  A.step(`Find where ${t} starts, then where ${t + 1} would start.`, A.arr('nums', a));
  const first = lower(t, `first index ≥ ${t}`);
  if (first === a.length || a[first] !== t) { A.step(`${t} is not present.`, A.text('Result', '[-1, -1]', 'bad')); return; }
  const last = lower(t + 1, `first index ≥ ${t + 1}`) - 1;
  A.step(`${t} occupies indices ${first} to ${last}.`, A.arr('nums', a, { hl: Object.fromEntries([...Array(last - first + 1).keys()].map(k => [first + k, 'ok'])) }), A.text('Result', `[${first}, ${last}]`, 'ok'));
}
A.scenario('Present twice', 'nums = [5,7,7,8,8,10], target = 8', () => run([5, 7, 7, 8, 8, 10], 8));
A.scenario('Absent', 'nums = [5,7,7,8,8,10], target = 6', () => run([5, 7, 7, 8, 8, 10], 6));
'''),

P(num=153, slug="find-minimum-in-rotated-sorted-array", title="Find Minimum in Rotated Sorted Array", diff="Medium", topic="Binary Search", cls="FindMinimumRotated",
idea="Compare mid with the right end: if mid is bigger, the drop (and the minimum) is to its right.",
vname="Binary search against the right end",
spec=r'''
A sorted array of **unique** values was rotated between 1 and n times. Return its minimum element in O(log n).

**Example**
```
[3,4,5,1,2] → 1,  [4,5,6,7,0,1,2] → 0,  [11,13,15,17] → 11
```

**Constraints**
* `1 <= n <= 5000`; values are unique.
''',
approach=r'''
**Look for the drop.** If `nums[mid] > nums[hi]`, the rotation point is right of `mid`: `lo = mid + 1`. Otherwise `mid..hi` is sorted,
so the minimum is at `mid` or to its left: `hi = mid`.

* Time: **O(log n)** — the range halves each step.
* Space: **O(1)** — two indices.
''',
java=r'''
public class FindMinimumRotated {

    public int findMin(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] > nums[hi]) lo = mid + 1; else hi = mid;
        }
        return nums[lo];
    }
}
''',
test=r'''
class FindMinimumRotatedTest {

    private final FindMinimumRotated solution = new FindMinimumRotated();

    @Test
    void rotated() {
        assertEquals(1, solution.findMin(new int[]{3, 4, 5, 1, 2}));
        assertEquals(0, solution.findMin(new int[]{4, 5, 6, 7, 0, 1, 2}));
    }

    @Test
    void notRotated() {
        assertEquals(11, solution.findMin(new int[]{11, 13, 15, 17}));
    }

    @Test
    void single() {
        assertEquals(5, solution.findMin(new int[]{5}));
    }
}
''',
trace=BS_TRACE_HELPERS + r'''
function run(a) {
  let lo = 0, hi = a.length - 1;
  A.step('The minimum sits right after the drop. Compare mid with the right end to find which side holds the drop.', A.arr('nums', a));
  while (lo < hi) {
    const mid = (lo + hi) >> 1, right = a[mid] > a[hi];
    A.step(`mid = ${mid} (${a[mid]}) ${right ? '>' : '≤'} right end ${a[hi]}: ${right ? 'the drop is to the right of mid' : 'mid..hi is sorted, so the minimum is at mid or to its left'}.`, bsView('nums', a, lo, hi, mid, { [hi]: 'alt' }));
    if (right) lo = mid + 1; else hi = mid;
  }
  A.step(`The minimum is ${a[lo]}, at index ${lo}.`, A.arr('nums', a, { hl: { [lo]: 'ok' } }), A.text('Result', a[lo], 'ok'));
}
A.scenario('Rotated', 'nums = [4,5,6,7,0,1,2]', () => run([4, 5, 6, 7, 0, 1, 2]));
A.scenario('Edge: not rotated', 'nums = [11,13,15,17]', () => run([11, 13, 15, 17]));
'''),

P(num=4, slug="median-of-two-sorted-arrays", title="Median of Two Sorted Arrays", diff="Hard", topic="Binary Search", cls="MedianOfTwoSortedArrays",
idea="Binary-search a cut in the shorter array so that the left halves of both arrays hold exactly the smaller half of all values.",
vname="Binary search on the partition",
spec=r'''
Given two sorted arrays `nums1` (size `m`) and `nums2` (size `n`), return the **median** of all `m + n` values, in O(log(m + n)).

**Example 1**
```
Input:  nums1 = [1,3], nums2 = [2]
Output: 2.0
```

**Example 2**
```
Input:  nums1 = [1,2], nums2 = [3,4]
Output: 2.5
```

**Constraints**
* `0 <= m, n <= 1000`; `1 <= m + n <= 2000`
''',
approach=r'''
**Partition search.** Make `A` the shorter array. Choose `i` elements from `A` and `j = (m + n + 1) / 2 - i` from `B` for the left half.
The cut is right when `A[i-1] <= B[j]` and `B[j-1] <= A[i]` (missing neighbours count as ±∞). If `A[i-1]` is too big, move `i` left;
otherwise move it right. The median comes from the largest value on the left and the smallest on the right.

* Time: **O(log min(m, n))** — binary search over the shorter array.
* Space: **O(1)** — a few indices.
''',
tc="log",
java=r'''
public class MedianOfTwoSortedArrays {

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] a = nums1.length <= nums2.length ? nums1 : nums2;
        int[] b = a == nums1 ? nums2 : nums1;
        int m = a.length, n = b.length, half = (m + n + 1) / 2, lo = 0, hi = m;
        while (true) {
            int i = (lo + hi) >>> 1, j = half - i;
            int aLeft = i == 0 ? Integer.MIN_VALUE : a[i - 1];
            int aRight = i == m ? Integer.MAX_VALUE : a[i];
            int bLeft = j == 0 ? Integer.MIN_VALUE : b[j - 1];
            int bRight = j == n ? Integer.MAX_VALUE : b[j];
            if (aLeft <= bRight && bLeft <= aRight) {
                int leftMax = Math.max(aLeft, bLeft);
                if ((m + n) % 2 == 1) return leftMax;
                return (leftMax + (double) Math.min(aRight, bRight)) / 2;
            }
            if (aLeft > bRight) hi = i - 1; else lo = i + 1;
        }
    }
}
''',
test=r'''
class MedianOfTwoSortedArraysTest {

    private final MedianOfTwoSortedArrays solution = new MedianOfTwoSortedArrays();

    @Test
    void odd() {
        assertEquals(2.0, solution.findMedianSortedArrays(new int[]{1, 3}, new int[]{2}));
    }

    @Test
    void even() {
        assertEquals(2.5, solution.findMedianSortedArrays(new int[]{1, 2}, new int[]{3, 4}));
    }

    @Test
    void oneEmpty() {
        assertEquals(3.0, solution.findMedianSortedArrays(new int[]{}, new int[]{1, 3, 5}));
    }

    @Test
    void interleaved() {
        assertEquals(4.5, solution.findMedianSortedArrays(new int[]{1, 3, 5, 7}, new int[]{2, 4, 6, 8}));
    }
}
''',
trace=r'''
function run(x, y) {
  const [a, b] = x.length <= y.length ? [x, y] : [y, x];
  const m = a.length, n = b.length, half = (m + n + 1) >> 1; let lo = 0, hi = m;
  A.step(`Search for a cut in the shorter array A. The left side must hold ${half} of the ${m + n} values.`, A.arr('A (shorter)', a), A.arr('B', b));
  while (true) {
    const i = (lo + hi) >> 1, j = half - i;
    const al = i ? a[i - 1] : -Infinity, ar = i < m ? a[i] : Infinity, bl = j ? b[j - 1] : -Infinity, br = j < n ? b[j] : Infinity;
    const f = v => (v === Infinity ? '+∞' : v === -Infinity ? '−∞' : v);
    const ok = al <= br && bl <= ar;
    const ha = Object.fromEntries(a.map((_, k) => [k, k < i ? 'sel' : 'alt'])), hb = Object.fromEntries(b.map((_, k) => [k, k < j ? 'sel' : 'alt']));
    A.step(`Take ${i} from A and ${j} from B for the left side (blue). Check: ${f(al)} ≤ ${f(br)} and ${f(bl)} ≤ ${f(ar)}? ${ok ? 'Yes, the cut is correct.' : al > br ? `No: ${f(al)} is too big, so take fewer from A.` : `No: ${f(bl)} is too big, so take more from A.`}`, A.arr('A (shorter)', a, { hl: ha, ptr: [[Math.min(i, m - 1), i < m ? 'cut' : 'cut→']] }), A.arr('B', b, { hl: hb, ptr: [[Math.min(j, n - 1), j < n ? 'cut' : 'cut→']] }));
    if (ok) {
      const lm = Math.max(al, bl), med = (m + n) % 2 ? lm : (lm + Math.min(ar, br)) / 2;
      A.step((m + n) % 2 ? `The total count is odd, so the median is the largest value on the left: ${lm}.` : `The total count is even, so the median is (${lm} + ${Math.min(ar, br)}) / 2 = ${med}.`, A.text('Result', med, 'ok'));
      return;
    }
    if (al > br) hi = i - 1; else lo = i + 1;
  }
}
A.scenario('Even total', 'nums1 = [1,3,5,7], nums2 = [2,4,6,8,9,10]', () => run([1, 3, 5, 7], [2, 4, 6, 8, 9, 10]));
A.scenario('Odd total', 'nums1 = [1,3], nums2 = [2]', () => run([1, 3], [2]));
''',
variants=[dict(
name="Merge until the middle",
idea="Walk both arrays like a merge, stopping once the middle position is reached.",
approach=r'''
**Partial merge.** Advance two pointers, always taking the smaller head, until `(m + n) / 2 + 1` values have been taken; keep the last
two taken values to compute the median.

* Time: **O(m + n)** — about half of all values are visited.
* Space: **O(1)** — two pointers and two remembered values.
''',
java=r'''
public class MedianOfTwoSortedArrays {

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int total = nums1.length + nums2.length, i = 0, j = 0, prev = 0, cur = 0;
        for (int k = 0; k <= total / 2; k++) {
            prev = cur;
            if (j >= nums2.length || (i < nums1.length && nums1[i] <= nums2[j])) cur = nums1[i++];
            else cur = nums2[j++];
        }
        return total % 2 == 1 ? cur : (prev + (double) cur) / 2;
    }
}
''',
trace=r'''
function run(a, b) {
  const total = a.length + b.length; let i = 0, j = 0, prev = 0, cur = 0;
  for (let k = 0; k <= total >> 1; k++) {
    prev = cur;
    const fromA = j >= b.length || (i < a.length && a[i] <= b[j]);
    cur = fromA ? a[i++] : b[j++];
    A.step(`Merged position ${k}: take ${cur} from ${fromA ? 'nums1' : 'nums2'}.`, A.arr('nums1', a, { hl: Object.fromEntries([...Array(i).keys()].map(t => [t, 'ok'])) }), A.arr('nums2', b, { hl: Object.fromEntries([...Array(j).keys()].map(t => [t, 'ok'])) }), A.vars({ prev, cur }));
  }
  const med = total % 2 ? cur : (prev + cur) / 2;
  A.step(`The middle is reached. Median = ${med}.`, A.text('Result', med, 'ok'));
}
A.scenario('Even total', 'nums1 = [1,2], nums2 = [3,4]', () => run([1, 2], [3, 4]));
''')]),
]
