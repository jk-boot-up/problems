PROBLEMS = [
P(num=215, slug="kth-largest-element-in-an-array", title="Kth Largest Element in an Array", diff="Medium", topic="Heap", cls="KthLargest",
idea="Quickselect: partition around a pivot and recurse only into the side that holds the k-th largest.",
vname="Quickselect",
spec=r'''
Return the `k`-th largest element of `nums` (in sorted order, not the k-th distinct value). Can you solve it without sorting?

**Example**
```
nums = [3,2,1,5,6,4], k = 2        → 5
nums = [3,2,3,1,2,4,5,5,6], k = 4  → 4
```

**Constraints**
* `1 <= k <= nums.length <= 10^5`; `-10^4 <= nums[i] <= 10^4`
''',
approach=r'''
**Quickselect with a random pivot.** The k-th largest is at index `n - k` in sorted order. Partition the range around a random pivot
(three-way, so many duplicates stay fast); if the target index falls in the "equal" block, done; otherwise continue in the left or
right part only.

* Time: **O(n)** — on average, since each round keeps about half of the range (worst case O(n²)).
* Space: **O(1)** — partitioning is in place and the loop is iterative.
''',
java=r'''
public class KthLargest {

    private final Random random = new Random(42);

    public int findKthLargest(int[] nums, int k) {
        int[] a = nums.clone();
        int target = a.length - k, lo = 0, hi = a.length - 1;
        while (true) {
            int pivot = a[lo + random.nextInt(hi - lo + 1)];
            int lt = lo, i = lo, gt = hi; // a[lo..lt-1] < pivot, a[lt..i-1] == pivot, a[gt+1..hi] > pivot
            while (i <= gt) {
                if (a[i] < pivot) swap(a, lt++, i++);
                else if (a[i] > pivot) swap(a, i, gt--);
                else i++;
            }
            if (target < lt) hi = lt - 1;
            else if (target > gt) lo = gt + 1;
            else return pivot;
        }
    }

    private static void swap(int[] a, int i, int j) {
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
}
''',
test=r'''
class KthLargestTest {

    private final KthLargest solution = new KthLargest();

    @Test
    void examples() {
        assertEquals(5, solution.findKthLargest(new int[]{3, 2, 1, 5, 6, 4}, 2));
        assertEquals(4, solution.findKthLargest(new int[]{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4));
    }

    @Test
    void duplicates() {
        assertEquals(1, solution.findKthLargest(new int[]{1, 1, 1, 1}, 3));
    }

    @Test
    void randomAgainstSort() {
        Random rnd = new Random(3);
        int[] a = rnd.ints(2000, -100, 100).toArray();
        int[] s = a.clone();
        Arrays.sort(s);
        for (int k : new int[]{1, 7, 1000, 2000}) assertEquals(s[s.length - k], solution.findKthLargest(a, k));
    }
}
''',
trace=r'''
function run(nums, k) {
  const a = nums.slice(), target = a.length - k; let lo = 0, hi = a.length - 1, round = 0;
  A.step(`The ${k}th largest value sits at index ${target} once sorted. Partition around a pivot and keep only the side containing index ${target}.`, A.arr('nums', a, { ptr: [[target, 'target']] }));
  const pivots = [5, 3, 2, 4, 1, 6];
  while (true) {
    const pivot = a.slice(lo, hi + 1).includes(pivots[round % pivots.length]) ? pivots[round % pivots.length] : a[lo]; round++;
    let lt = lo, i = lo, gt = hi;
    while (i <= gt) { if (a[i] < pivot) { [a[lt], a[i]] = [a[i], a[lt]]; lt++; i++; } else if (a[i] > pivot) { [a[i], a[gt]] = [a[gt], a[i]]; gt--; } else i++; }
    const hl = {}; for (let t = lo; t <= hi; t++) hl[t] = t < lt ? 'sel' : t > gt ? 'alt' : 'cur';
    A.step(`Pivot ${pivot}: smaller values to the left (blue), equal in the middle (orange), larger to the right (purple).`, A.arr('nums', a, { range: [lo, hi], ptr: [[target, 'target']], hl }));
    if (target < lt) { hi = lt - 1; A.step(`Index ${target} is in the smaller part. Discard everything else.`, A.arr('nums', a, { range: [lo, hi], ptr: [[target, 'target']] })); }
    else if (target > gt) { lo = gt + 1; A.step(`Index ${target} is in the larger part. Discard everything else.`, A.arr('nums', a, { range: [lo, hi], ptr: [[target, 'target']] })); }
    else { A.step(`Index ${target} falls in the pivot's block, so the ${k}th largest is ${pivot}.`, A.arr('nums', a, { hl: { [target]: 'ok' } }), A.text('Result', pivot, 'ok')); return; }
  }
}
A.scenario('k = 2', 'nums = [3,2,1,5,6,4]', () => run([3, 2, 1, 5, 6, 4], 2));
A.scenario('With duplicates', 'nums = [3,2,3,1,2,4,5,5,6], k = 4', () => run([3, 2, 3, 1, 2, 4, 5, 5, 6], 4));
''',
variants=[dict(
name="Sort",
idea="Sort and read index n − k.",
approach=r'''
**Sort.** `Arrays.sort` then return `nums[n - k]`.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's recursion stack (on a copy).
''',
tc="nlogn", sc="log",
java=r'''
public class KthLargest {

    public int findKthLargest(int[] nums, int k) {
        int[] a = nums.clone();
        Arrays.sort(a);
        return a[a.length - k];
    }
}
''',
trace=r'''
function run(nums, k) {
  const s = nums.slice().sort((x, y) => x - y);
  A.step('Sort everything.', A.arr('nums', nums), A.arr('sorted', s));
  A.step(`The ${k}th largest is at index ${s.length - k}: ${s[s.length - k]}. Sorting did far more work than needed.`, A.arr('sorted', s, { hl: { [s.length - k]: 'ok' } }), A.text('Result', s[s.length - k], 'ok'));
}
A.scenario('k = 2', 'nums = [3,2,1,5,6,4]', () => run([3, 2, 1, 5, 6, 4], 2));
'''), dict(
name="Min-heap of size k",
idea="Keep the k largest values seen so far in a min-heap; its top is the k-th largest.",
approach=r'''
**Bounded heap.** Push each value; when the heap holds more than `k` values, pop the smallest. At the end the heap's minimum is the
k-th largest.

* Time: **O(n log k)** — n pushes on a heap of size k.
* Space: **O(k)** — the heap.
''',
tc="nlogn", sc="n",
java=r'''
public class KthLargest {

    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int x : nums) {
            heap.add(x);
            if (heap.size() > k) heap.poll();
        }
        return heap.peek();
    }
}
''',
trace=r'''
function run(nums, k) {
  const heap = [];
  nums.forEach((x, i) => {
    heap.push(x); heap.sort((a, b) => a - b);
    let dropped = null; if (heap.length > k) dropped = heap.shift();
    A.step(`Add ${x}.${dropped !== null ? ` The heap has more than ${k} values, so drop the smallest, ${dropped}.` : ''}`, A.arr('nums', nums, { hl: { [i]: 'cur' } }), A.arr(`min-heap (keeps the ${k} largest)`, heap, { hl: { 0: 'alt' } }));
  });
  A.step(`The top of the heap, ${heap[0]}, is the ${k}th largest.`, A.text('Result', heap[0], 'ok'));
}
A.scenario('k = 2', 'nums = [3,2,1,5,6,4]', () => run([3, 2, 1, 5, 6, 4], 2));
''')]),

P(num=502, slug="ipo", title="IPO", diff="Hard", topic="Heap", cls="IPO",
idea="Unlock every project you can afford, then always take the most profitable unlocked one.",
vname="Sort by capital + max-heap of profits",
spec=r'''
You have initial capital `w` and may finish at most `k` distinct projects. Project `i` needs at least `capital[i]` to start and adds
`profits[i]` to your capital when finished. Return the maximum capital after at most `k` projects.

**Example**
```
Input:  k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4   (do project 0 → w = 1, then project 2 → w = 4)
```

**Constraints**
* `1 <= k <= 10^5`; `0 <= w <= 10^9`; `1 <= n <= 10^5`
''',
approach=r'''
**Greedy with two structures.** Sort projects by required capital. Repeat `k` times: push the profits of every project whose capital
requirement is now within `w` into a max-heap; if the heap is empty, stop; otherwise add the largest profit to `w`.

* Time: **O(n log n)** — sorting plus heap operations (k ≤ n relevant pops).
* Space: **O(n)** — the sorted index and the heap.
''',
tc="nlogn", sc="n",
java=r'''
public class IPO {

    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, Comparator.comparingInt(i -> capital[i]));
        PriorityQueue<Integer> best = new PriorityQueue<>(Comparator.reverseOrder());
        int next = 0;
        for (int round = 0; round < k; round++) {
            while (next < n && capital[order[next]] <= w) best.add(profits[order[next++]]);
            if (best.isEmpty()) break;
            w += best.poll();
        }
        return w;
    }
}
''',
test=r'''
class IPOTest {

    private final IPO solution = new IPO();

    @Test
    void example1() {
        assertEquals(4, solution.findMaximizedCapital(2, 0, new int[]{1, 2, 3}, new int[]{0, 1, 1}));
    }

    @Test
    void example2() {
        assertEquals(6, solution.findMaximizedCapital(3, 0, new int[]{1, 2, 3}, new int[]{0, 1, 2}));
    }

    @Test
    void cannotStart() {
        assertEquals(0, solution.findMaximizedCapital(1, 0, new int[]{1, 2, 3}, new int[]{1, 1, 2}));
    }
}
''',
trace=r'''
function run(k, w, profits, capital) {
  const order = profits.map((_, i) => i).sort((a, b) => capital[a] - capital[b]), heap = []; let next = 0;
  const lab = order.map(i => `need ${capital[i]} → +${profits[i]}`);
  A.step(`Sort the projects by the capital they need. We start with ${w}.`, A.arr('projects by capital', lab), A.vars({ capital: w, roundsLeft: k }));
  for (let r = 0; r < k; r++) {
    while (next < order.length && capital[order[next]] <= w) heap.push(profits[order[next++]]);
    heap.sort((a, b) => b - a);
    if (!heap.length) { A.step(`No affordable project remains with capital ${w}. Stop.`, A.arr('projects by capital', lab, { hl: Object.fromEntries(order.map((_, t) => [t, t < next ? 'dim' : 'bad'])) }), A.vars({ capital: w })); break; }
    const p = heap.shift(); w += p;
    A.step(`Round ${r + 1}: every project needing at most ${w - p} is unlocked. The best unlocked profit is ${p}; take it. Capital is now ${w}.`, A.arr('projects by capital', lab, { hl: Object.fromEntries(order.map((_, t) => [t, t < next ? 'sel' : ''])) }), A.arr('max-heap of profits', heap), A.vars({ capital: w }));
  }
  A.step(`Final capital: ${w}.`, A.text('Result', w, 'ok'));
}
A.scenario('Classic', 'k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]', () => run(2, 0, [1, 2, 3], [0, 1, 1]));
A.scenario('Unlock as you grow', 'k = 3, w = 1, profits = [2,5,3,10], capital = [0,3,1,6]', () => run(3, 1, [2, 5, 3, 10], [0, 3, 1, 6]));
'''),

P(num=373, slug="find-k-pairs-with-smallest-sums", title="Find K Pairs with Smallest Sums", diff="Medium", topic="Heap", cls="KSmallestPairs",
idea="Treat each nums1[i] as a sorted row of pairs; a heap merges the rows, always expanding the smallest pair.",
vname="Min-heap over row heads",
spec=r'''
Given two sorted arrays `nums1` and `nums2` and an integer `k`, return the `k` pairs `[u, v]` (u from nums1, v from nums2) with the
smallest sums.

**Example**
```
Input:  nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
```

**Constraints**
* `1 <= nums1.length, nums2.length <= 10^5`; `1 <= k <= 10^4`; `k <= nums1.length * nums2.length`
''',
approach=r'''
**K-way merge.** Row `i` is the pairs `(nums1[i], nums2[0..])`, already sorted by sum. Seed a min-heap with `(i, 0)` for the first
`min(k, n1)` rows. Pop the smallest, record it, and push `(i, j + 1)` from the same row.

* Time: **O(k log k)** — k pops and pushes on a heap of size at most k.
* Space: **O(k)** — the heap (plus the output).
''',
tc="nlogn", sc="n",
java=r'''
public class KSmallestPairs {

    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(p -> nums1[p[0]] + nums2[p[1]]));
        for (int i = 0; i < Math.min(k, nums1.length); i++) heap.add(new int[]{i, 0});
        List<List<Integer>> out = new ArrayList<>();
        while (out.size() < k && !heap.isEmpty()) {
            int[] p = heap.poll();
            out.add(List.of(nums1[p[0]], nums2[p[1]]));
            if (p[1] + 1 < nums2.length) heap.add(new int[]{p[0], p[1] + 1});
        }
        return out;
    }
}
''',
test=r'''
class KSmallestPairsTest {

    private final KSmallestPairs solution = new KSmallestPairs();

    @Test
    void example1() {
        assertEquals(List.of(List.of(1, 2), List.of(1, 4), List.of(1, 6)), solution.kSmallestPairs(new int[]{1, 7, 11}, new int[]{2, 4, 6}, 3));
    }

    @Test
    void sumsOnly() {
        List<List<Integer>> out = solution.kSmallestPairs(new int[]{1, 1, 2}, new int[]{1, 2, 3}, 2);
        assertEquals(List.of(2, 2), out.stream().map(p -> p.get(0) + p.get(1)).toList());
    }

    @Test
    void allPairs() {
        assertEquals(4, solution.kSmallestPairs(new int[]{1, 2}, new int[]{3, 4}, 4).size());
    }
}
''',
trace=r'''
function run(a, b, k) {
  const grid = a.map(x => b.map(y => x + y)), heap = [], out = [], done = {};
  for (let i = 0; i < Math.min(k, a.length); i++) heap.push([i, 0]);
  const view = (msg, cur) => A.step(msg, A.grid('sums (rows: nums1, columns: nums2)', grid, { hl: Object.entries(done).concat(heap.map(([i, j]) => [`${i},${j}`, 'sel'])).concat(cur ? [[cur, 'cur']] : []) }), A.arr('heap', heap.slice().sort((p, q) => grid[p[0]][p[1]] - grid[q[0]][q[1]]).map(([i, j]) => `${a[i]}+${b[j]}`)), A.arr('result', out));
  view('Each row is sorted. The heap starts with the first pair of every row (blue).');
  while (out.length < k && heap.length) {
    heap.sort((p, q) => grid[p[0]][p[1]] - grid[q[0]][q[1]]);
    const [i, j] = heap.shift(); out.push(`[${a[i]},${b[j]}]`); done[`${i},${j}`] = 'ok';
    if (j + 1 < b.length) heap.push([i, j + 1]);
    view(`Pop the smallest sum ${a[i]} + ${b[j]} = ${grid[i][j]}. Push the next pair in its row.`, `${i},${j}`);
  }
}
A.scenario('k = 3', 'nums1 = [1,7,11], nums2 = [2,4,6]', () => run([1, 7, 11], [2, 4, 6], 3));
A.scenario('k = 5', 'nums1 = [1,2,4], nums2 = [1,3,5]', () => run([1, 2, 4], [1, 3, 5], 5));
'''),

P(num=295, slug="find-median-from-data-stream", title="Find Median from Data Stream", diff="Hard", topic="Heap", cls="MedianFinder",
idea="Keep the smaller half in a max-heap and the larger half in a min-heap; the median sits on their tops.",
vname="Two heaps",
spec=r'''
Implement `MedianFinder`:
* `addNum(int num)`: add a number from the stream;
* `double findMedian()`: the median of all numbers so far (the mean of the two middle values for an even count).

**Example**
```
addNum(1), addNum(2) → findMedian() = 1.5; addNum(3) → findMedian() = 2.0
```

**Constraints**
* `-10^5 <= num <= 10^5`; up to `5 * 10^4` calls; `findMedian` is called on a non-empty stream.
''',
approach=r'''
**Balanced halves.** `low` is a max-heap holding the smaller half; `high` a min-heap holding the larger half, with `low` allowed one
extra element. To add: push into `low`, move `low`'s top to `high` (keeps every value in `low` ≤ every value in `high`), and if `high`
grew bigger than `low`, move its top back.

* Time: **O(log n)** — per add (a few heap operations); findMedian is O(1).
* Space: **O(n)** — both heaps together hold every number.
''',
tc="log", sc="n",
java=r'''
public class MedianFinder {

    private final PriorityQueue<Integer> low = new PriorityQueue<>(Comparator.reverseOrder());
    private final PriorityQueue<Integer> high = new PriorityQueue<>();

    public void addNum(int num) {
        low.add(num);
        high.add(low.poll());
        if (high.size() > low.size()) low.add(high.poll());
    }

    public double findMedian() {
        return low.size() > high.size() ? low.peek() : (low.peek() + (double) high.peek()) / 2;
    }
}
''',
test=r'''
class MedianFinderTest {

    @Test
    void example() {
        MedianFinder m = new MedianFinder();
        m.addNum(1);
        m.addNum(2);
        assertEquals(1.5, m.findMedian());
        m.addNum(3);
        assertEquals(2.0, m.findMedian());
    }

    @Test
    void unsortedStream() {
        MedianFinder m = new MedianFinder();
        int[] stream = {5, 15, 1, 3, 8, 7, 9, 10};
        double[] expected = {5, 10, 5, 4, 5, 6, 7, 7.5};
        for (int i = 0; i < stream.length; i++) {
            m.addNum(stream[i]);
            assertEquals(expected[i], m.findMedian());
        }
    }
}
''',
trace=r'''
A.scenario('Stream 5, 15, 1, 3, 8, 7', 'addNum each and read the median', () => {
  const low = [], high = [];
  const view = (msg) => A.step(msg, A.arr('low: max-heap (smaller half)', low.slice().sort((a, b) => b - a), { hl: { 0: 'sel' } }), A.arr('high: min-heap (larger half)', high.slice().sort((a, b) => a - b), { hl: { 0: 'alt' } }));
  view('The smaller half lives in a max-heap and the larger half in a min-heap. The median is at their tops.');
  for (const x of [5, 15, 1, 3, 8, 7]) {
    low.push(x); low.sort((a, b) => b - a); const moved = low.shift(); high.push(moved); high.sort((a, b) => a - b);
    let back = null; if (high.length > low.length) { back = high.shift(); low.push(back); }
    const med = low.length > high.length ? Math.max(...low) : (Math.max(...low) + Math.min(...high)) / 2;
    view(`addNum(${x}): pass the largest of the low half (${moved}) up to high${back !== null ? `, then move ${back} back so low stays at least as big` : ''}. Median = ${med}.`);
  }
});
''',
variants=[dict(
name="Sorted list with binary insertion",
idea="Keep every number in a sorted list; the median is in the middle.",
approach=r'''
**Insertion sort, one value at a time.** Binary-search the insertion point and insert into an `ArrayList`.

* Time: **O(n)** — per add, because inserting shifts the elements after the position; findMedian is O(1).
* Space: **O(n)** — the list.
''',
tc="n", sc="n",
java=r'''
public class MedianFinder {

    private final List<Integer> sorted = new ArrayList<>();

    public void addNum(int num) {
        int lo = 0, hi = sorted.size();
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (sorted.get(mid) < num) lo = mid + 1; else hi = mid;
        }
        sorted.add(lo, num);
    }

    public double findMedian() {
        int n = sorted.size();
        return n % 2 == 1 ? sorted.get(n / 2) : (sorted.get(n / 2 - 1) + (double) sorted.get(n / 2)) / 2;
    }
}
''',
trace=r'''
A.scenario('Stream 5, 15, 1, 3, 8, 7', 'addNum each and read the median', () => {
  const s = [];
  for (const x of [5, 15, 1, 3, 8, 7]) {
    let lo = 0; while (lo < s.length && s[lo] < x) lo++;
    s.splice(lo, 0, x);
    const n = s.length, med = n % 2 ? s[n >> 1] : (s[n / 2 - 1] + s[n / 2]) / 2;
    A.step(`Insert ${x} at index ${lo}; ${s.length - lo - 1} value${s.length - lo - 1 === 1 ? '' : 's'} shift right. Median = ${med}.`, A.arr('sorted', s, { hl: { [lo]: 'ok', ...(n % 2 ? { [n >> 1]: 'alt' } : { [n / 2 - 1]: 'alt', [n / 2]: 'alt' }) } }));
  }
});
''')]),

P(num=67, slug="add-binary", title="Add Binary", diff="Easy", topic="Bit Manipulation", cls="AddBinary",
idea="Add digit by digit from the right with a carry, exactly like on paper.",
vname="Right-to-left with carry",
spec=r'''
Given two binary strings `a` and `b`, return their sum as a binary string.

**Example**
```
a = "11",   b = "1"    → "100"
a = "1010", b = "1011" → "10101"
```

**Constraints**
* `1 <= a.length, b.length <= 10^4`; no leading zeros except "0" itself.
''',
approach=r'''
**Schoolbook addition.** Walk both strings from the end; `sum = carry + bitA + bitB`; append `sum % 2`, carry `sum / 2`. Reverse at the end.

* Time: **O(max(m, n))** — one step per digit.
* Space: **O(max(m, n))** — the result builder.
''',
tc="n", sc="n",
java=r'''
public class AddBinary {

    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1, j = b.length() - 1, carry = 0;
        while (i >= 0 || j >= 0 || carry > 0) {
            int sum = carry;
            if (i >= 0) sum += a.charAt(i--) - '0';
            if (j >= 0) sum += b.charAt(j--) - '0';
            sb.append(sum % 2);
            carry = sum / 2;
        }
        return sb.reverse().toString();
    }
}
''',
test=r'''
class AddBinaryTest {

    private final AddBinary solution = new AddBinary();

    @ParameterizedTest
    @CsvSource({"11,1,100", "1010,1011,10101", "0,0,0", "1111,1111,11110"})
    void adds(String a, String b, String expected) {
        assertEquals(expected, solution.addBinary(a, b));
    }
}
''',
trace=r'''
function run(a, b) {
  const w = Math.max(a.length, b.length) + 1, A2 = a.padStart(w, ' '), B2 = b.padStart(w, ' ');
  const out = new Array(w).fill(''); let carry = 0;
  const g = () => [[...A2].map(c => c.trim()), [...B2].map(c => c.trim()), out.slice()];
  A.step('Line the numbers up on the right and add column by column, carrying into the next column.', A.grid('a / b / sum', g()), A.vars({ carry }));
  for (let c = w - 1; c >= 0; c--) {
    const x = A2[c] === '1' ? 1 : 0, y = B2[c] === '1' ? 1 : 0;
    if (A2[c] === ' ' && B2[c] === ' ' && !carry) break;
    const s = x + y + carry; out[c] = String(s % 2);
    A.step(`Column ${w - 1 - c}: ${x} + ${y}${carry ? ' + carry 1' : ''} = ${s}. Write ${s % 2}${s >= 2 ? ', carry 1' : ''}.`, A.grid('a / b / sum', g(), { hl: { [`0,${c}`]: 'cur', [`1,${c}`]: 'cur', [`2,${c}`]: 'ok' } }), A.vars({ carry: s >> 1 }));
    carry = s >> 1;
  }
  A.step(`Sum: ${out.join('')}.`, A.text('Result', out.join(''), 'ok'));
}
A.scenario('1010 + 1011', 'a = "1010", b = "1011"', () => run('1010', '1011'));
A.scenario('Carry out', 'a = "11", b = "1"', () => run('11', '1'));
'''),

P(num=190, slug="reverse-bits", title="Reverse Bits", diff="Easy", topic="Bit Manipulation", cls="ReverseBits",
idea="Shift bits out of n from the right and into the result from the left, 32 times.",
vname="Bit-by-bit shifting",
spec=r'''
Reverse the bits of a 32-bit **unsigned** integer (in Java it arrives in an `int`, so the top bit may be the sign bit).

**Example**
```
Input:  00000010100101000001111010011100   (43261596)
Output: 00111001011110000010100101000000   (964176192)
```

**Constraints**
* The input is a 32-bit binary value.

**Follow-up:** if called many times, how would you optimize it?
''',
approach=r'''
**Shift and build.** 32 times: shift `result` left, add `n & 1`, then shift `n` right with `>>>` (unsigned).

* Time: **O(1)** — always 32 iterations.
* Space: **O(1)** — one int.
''',
java=r'''
public class ReverseBits {

    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result = (result << 1) | (n & 1);
            n >>>= 1;
        }
        return result;
    }
}
''',
test=r'''
class ReverseBitsTest {

    private final ReverseBits solution = new ReverseBits();

    @Test
    void example1() {
        assertEquals(964176192, solution.reverseBits(43261596));
    }

    @Test
    void highBit() {
        assertEquals(-1073741825, solution.reverseBits(0b11111111111111111111111111111101));
    }

    @Test
    void one() {
        assertEquals(Integer.MIN_VALUE, solution.reverseBits(1));
    }
}
''',
trace=r'''
function run(n) {
  const bits = n.toString(2).padStart(32, '0').split(''), res = new Array(32).fill('');
  A.step('Take bits off the right end of n and push them onto the right end of the result. After 32 moves, the order is reversed.', A.arr('n', bits, { noIdx: true }), A.arr('result', res, { noIdx: true }));
  for (let i = 0; i < 32; i++) {
    res[i] = bits[31 - i];
    if (i < 6 || i > 28) A.step(`Step ${i + 1}: bit ${i} of n (${bits[31 - i]}) becomes bit ${31 - i} of the result.`, A.arr('n', bits, { noIdx: true, hl: { [31 - i]: 'cur' } }), A.arr('result', res, { noIdx: true, hl: { [i]: 'ok' } }));
    else if (i === 6) A.step('… the same for the middle bits …', A.arr('result', res, { noIdx: true }));
  }
  A.step(`Result: ${parseInt(res.join(''), 2)}.`, A.arr('result', res, { noIdx: true, hl: res.map((_, i) => [i, 'ok']) }), A.text('Result', parseInt(res.join(''), 2), 'ok'));
}
A.scenario('43261596', 'n = 43261596', () => run(43261596));
''',
variants=[dict(
name="Swap halves (divide and conquer)",
idea="Swap the two 16-bit halves, then the bytes in each half, then the nibbles, pairs and single bits.",
approach=r'''
**Masks.** Five mask-and-shift steps swap blocks of 16, 8, 4, 2 and 1 bits. After all five, every bit has moved to its mirror position.

* Time: **O(1)** — five constant steps.
* Space: **O(1)** — one int.
''',
java=r'''
public class ReverseBits {

    public int reverseBits(int n) {
        n = (n >>> 16) | (n << 16);
        n = ((n & 0xff00ff00) >>> 8) | ((n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >>> 4) | ((n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >>> 2) | ((n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >>> 1) | ((n & 0x55555555) << 1);
        return n;
    }
}
''',
trace=r'''
function run(n) {
  let b = n.toString(2).padStart(32, '0').split('');
  A.step('Swap ever smaller blocks: halves, bytes, nibbles, pairs, then single bits.', A.arr('bits', b, { noIdx: true }));
  for (const size of [16, 8, 4, 2, 1]) {
    const nb = []; for (let i = 0; i < 32; i += 2 * size) nb.push(...b.slice(i + size, i + 2 * size), ...b.slice(i, i + size));
    b = nb;
    A.step(`Swap neighbouring blocks of ${size} bit${size > 1 ? 's' : ''}.`, A.arr('bits', b, { noIdx: true, hl: Object.fromEntries(b.map((_, i) => [i, Math.floor(i / size) % 2 ? 'alt' : 'sel'])) }));
  }
  A.step(`Result: ${parseInt(b.join(''), 2)}.`, A.text('Result', parseInt(b.join(''), 2), 'ok'));
}
A.scenario('43261596', 'n = 43261596', () => run(43261596));
''')]),

P(num=191, slug="number-of-1-bits", title="Number of 1 Bits", diff="Easy", topic="Bit Manipulation", cls="NumberOf1Bits",
idea="n & (n − 1) clears the lowest set bit, so count how many times you can do that before n is 0.",
vname="Clear lowest set bit",
spec=r'''
Return the number of set bits (`1`s) in the binary representation of a positive integer `n` (its Hamming weight).

**Example**
```
n = 11 (1011)            → 3
n = 128 (10000000)       → 1
n = 2147483645           → 30
```

**Constraints**
* `1 <= n <= 2^31 - 1`
''',
approach=r'''
**Brian Kernighan's trick.** `n & (n - 1)` turns off the lowest 1-bit. Loop until `n == 0`, counting iterations.

* Time: **O(k)** — k is the number of set bits (at most 32).
* Space: **O(1)** — a counter.
''',
tc="1",
java=r'''
public class NumberOf1Bits {

    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n &= n - 1;
            count++;
        }
        return count;
    }
}
''',
test=r'''
class NumberOf1BitsTest {

    private final NumberOf1Bits solution = new NumberOf1Bits();

    @ParameterizedTest
    @CsvSource({"11,3", "128,1", "2147483645,30", "1,1"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.hammingWeight(n));
    }
}
''',
trace=r'''
function run(n) {
  let count = 0;
  const show = x => x.toString(2).padStart(8, '0').split('');
  A.step(`n = ${n}. Each n & (n − 1) clears the lowest 1-bit.`, A.arr('n', show(n), { noIdx: true, hl: Object.fromEntries(show(n).map((c, i) => [i, c === '1' ? 'sel' : ''])) }), A.vars({ count }));
  while (n) {
    const low = n & -n, pos = 7 - Math.log2(low);
    A.step(`The lowest 1-bit is the one worth ${low}. Clear it with n & (n − 1).`, A.arr('n', show(n), { noIdx: true, hl: { [pos]: 'bad' } }), A.vars({ count }));
    n &= n - 1; count++;
    A.step(`n is now ${n}; count = ${count}.`, A.arr('n', show(n), { noIdx: true }), A.vars({ count }));
  }
  A.step(`n is 0, so there were ${count} set bits.`, A.text('Result', count, 'ok'));
}
A.scenario('n = 11', '1011', () => run(11));
''',
variants=[dict(
name="Check all 32 bits",
idea="Test each of the 32 bits with a shift and a mask.",
approach=r'''
**Bit loop.** For `i = 0..31`, add `(n >>> i) & 1`.

* Time: **O(1)** — always 32 iterations.
* Space: **O(1)** — a counter.
''',
java=r'''
public class NumberOf1Bits {

    public int hammingWeight(int n) {
        int count = 0;
        for (int i = 0; i < 32; i++) count += (n >>> i) & 1;
        return count;
    }
}
''',
trace=r'''
function run(n) {
  const b = n.toString(2).padStart(8, '0').split(''); let count = 0;
  for (let i = 7; i >= 0; i--) { count += +b[i]; A.step(`Bit ${7 - i}: ${b[i]}. Count = ${count}.`, A.arr('n (low 8 bits)', b, { noIdx: true, hl: { [i]: b[i] === '1' ? 'ok' : 'dim' } })); }
  A.step(`${count} set bits (the remaining 24 bits are 0 and are checked the same way).`, A.text('Result', count, 'ok'));
}
A.scenario('n = 11', '1011', () => run(11));
''')]),

P(num=136, slug="single-number", title="Single Number", diff="Easy", topic="Bit Manipulation", cls="SingleNumber",
idea="x ^ x = 0 and x ^ 0 = x, so XOR-ing everything cancels the pairs and leaves the single value.",
vname="XOR everything",
spec=r'''
Every element of a non-empty array appears **twice** except one. Find that one, in linear time and constant extra space.

**Example**
```
[2,2,1] → 1,   [4,1,2,1,2] → 4,   [1] → 1
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`
''',
approach=r'''
**XOR.** XOR is commutative and associative, `x ^ x = 0` and `x ^ 0 = x`; XOR all values and the pairs vanish.

* Time: **O(n)** — one pass.
* Space: **O(1)** — one accumulator.
''',
java=r'''
public class SingleNumber {

    public int singleNumber(int[] nums) {
        int x = 0;
        for (int v : nums) x ^= v;
        return x;
    }
}
''',
test=r'''
class SingleNumberTest {

    private final SingleNumber solution = new SingleNumber();

    @Test
    void examples() {
        assertEquals(1, solution.singleNumber(new int[]{2, 2, 1}));
        assertEquals(4, solution.singleNumber(new int[]{4, 1, 2, 1, 2}));
        assertEquals(1, solution.singleNumber(new int[]{1}));
    }

    @Test
    void negatives() {
        assertEquals(-5, solution.singleNumber(new int[]{-1, -5, -1}));
    }
}
''',
trace=r'''
function run(a) {
  let x = 0;
  const bits = v => (v >>> 0).toString(2).padStart(4, '0').slice(-4).split('');
  A.step('XOR every value into an accumulator. Equal pairs cancel to 0.', A.arr('nums', a), A.arr('acc (bits)', bits(x), { noIdx: true }));
  a.forEach((v, i) => { const before = x; x ^= v; A.step(`${before} XOR ${v} = ${x}.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.arr(`${v} (bits)`, bits(v), { noIdx: true }), A.arr('acc (bits)', bits(x), { noIdx: true, hl: Object.fromEntries(bits(x).map((c, t) => [t, c === '1' ? 'sel' : ''])) })); });
  A.step(`Every pair cancelled. ${x} is left over.`, A.text('Result', x, 'ok'));
}
A.scenario('Five values', 'nums = [4,1,2,1,2]', () => run([4, 1, 2, 1, 2]));
''',
variants=[dict(
name="Hash set toggling",
idea="Add a value when first seen and remove it when seen again; one value remains.",
approach=r'''
**`MyHashSet`.** `add` returns false for the second copy, so remove it then. The set ends with the single value.

* Time: **O(n)** — one pass of O(1) average set operations.
* Space: **O(n)** — up to n/2 values in the set.
''',
java=r'''
public class SingleNumber {

    public int singleNumber(int[] nums) {
        MyHashSet<Integer> seen = new MyHashSet<>();
        for (int v : nums) {
            if (!seen.add(v)) seen.remove(v);
        }
        return seen.iterator().next();
    }
}
''',
trace=r'''
function run(a) {
  const s = new Set();
  a.forEach((v, i) => { const had = s.has(v); if (had) s.delete(v); else s.add(v); A.step(had ? `${v} seen again: remove it.` : `${v} seen for the first time: add it.`, A.arr('nums', a, { hl: { [i]: had ? 'bad' : 'cur' } }), A.hashTable('set', s)); });
  A.step(`One value remains: ${[...s][0]}. This used O(n) extra space.`, A.text('Result', [...s][0], 'ok'));
}
A.scenario('Five values', 'nums = [4,1,2,1,2]', () => run([4, 1, 2, 1, 2]));
''')]),

P(num=137, slug="single-number-ii", title="Single Number II", diff="Medium", topic="Bit Manipulation", cls="SingleNumberII",
idea="Track, per bit, how many times it has been seen modulo 3 using two masks: ones and twos.",
vname="Ones/twos bit counters",
spec=r'''
Every element appears **three times** except one, which appears exactly once. Find it in linear time and constant extra space.

**Example**
```
[2,2,3,2] → 3,   [0,1,0,1,0,1,99] → 99
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`
''',
approach=r'''
**A mod-3 counter for every bit.** `ones` holds bits seen 1 (mod 3) times, `twos` bits seen 2 times. For each `x`:
`ones = (ones ^ x) & ~twos`, then `twos = (twos ^ x) & ~ones`. A bit seen three times is cleared from both, so `ones` ends as the answer.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two ints.
''',
java=r'''
public class SingleNumberII {

    public int singleNumber(int[] nums) {
        int ones = 0, twos = 0;
        for (int x : nums) {
            ones = (ones ^ x) & ~twos;
            twos = (twos ^ x) & ~ones;
        }
        return ones;
    }
}
''',
test=r'''
class SingleNumberIITest {

    private final SingleNumberII solution = new SingleNumberII();

    @Test
    void examples() {
        assertEquals(3, solution.singleNumber(new int[]{2, 2, 3, 2}));
        assertEquals(99, solution.singleNumber(new int[]{0, 1, 0, 1, 0, 1, 99}));
    }

    @Test
    void negative() {
        assertEquals(-4, solution.singleNumber(new int[]{-2, -2, 1, 1, -4, 1, -2}));
    }
}
''',
trace=r'''
function run(a) {
  let ones = 0, twos = 0;
  const b = v => (v >>> 0).toString(2).padStart(4, '0').slice(-4).split('');
  A.step('ones holds bits seen once (mod 3); twos holds bits seen twice. A third sighting clears a bit from both.', A.arr('nums', a), A.arr('ones', b(ones), { noIdx: true }), A.arr('twos', b(twos), { noIdx: true }));
  a.forEach((x, i) => {
    ones = (ones ^ x) & ~twos; twos = (twos ^ x) & ~ones;
    A.step(`Add ${x}: ones = ${ones}, twos = ${twos}.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.arr(`${x} (bits)`, b(x), { noIdx: true }), A.arr('ones', b(ones), { noIdx: true, hl: Object.fromEntries(b(ones).map((c, t) => [t, c === '1' ? 'ok' : ''])) }), A.arr('twos', b(twos), { noIdx: true, hl: Object.fromEntries(b(twos).map((c, t) => [t, c === '1' ? 'sel' : ''])) }));
  });
  A.step(`Bits seen three times have cancelled out. ones = ${ones} is the single number.`, A.text('Result', ones, 'ok'));
}
A.scenario('Four values', 'nums = [2,2,3,2]', () => run([2, 2, 3, 2]));
''',
variants=[dict(
name="Count each bit position",
idea="For each of the 32 bits, count how many numbers have it set; counts not divisible by 3 belong to the single number.",
approach=r'''
**Per-bit sums.** For `bit = 0..31`, sum `(x >> bit) & 1` over all numbers; if the sum mod 3 is 1, set that bit in the answer.

* Time: **O(32·n)** — 32 passes, which is O(n).
* Space: **O(1)** — counters.
''',
java=r'''
public class SingleNumberII {

    public int singleNumber(int[] nums) {
        int result = 0;
        for (int bit = 0; bit < 32; bit++) {
            int count = 0;
            for (int x : nums) count += (x >> bit) & 1;
            if (count % 3 != 0) result |= 1 << bit;
        }
        return result;
    }
}
''',
trace=r'''
function run(a) {
  let res = 0;
  for (let bit = 0; bit < 4; bit++) {
    const cnt = a.reduce((s, x) => s + ((x >> bit) & 1), 0);
    if (cnt % 3) res |= 1 << bit;
    A.step(`Bit ${bit}: set in ${cnt} numbers. ${cnt} mod 3 = ${cnt % 3}, so the answer ${cnt % 3 ? 'has' : 'does not have'} this bit.`, A.arr('nums', a, { hl: Object.fromEntries(a.map((x, i) => [i, (x >> bit) & 1 ? 'sel' : ''])) }), A.vars({ result: res }));
  }
  A.step(`Result: ${res} (higher bits work the same way).`, A.text('Result', res, 'ok'));
}
A.scenario('Four values', 'nums = [2,2,3,2]', () => run([2, 2, 3, 2]));
''')]),

P(num=201, slug="bitwise-and-of-numbers-range", title="Bitwise AND of Numbers Range", diff="Medium", topic="Bit Manipulation", cls="RangeBitwiseAnd",
idea="Only the common binary prefix of left and right survives; every lower bit flips somewhere in the range.",
vname="Common prefix by shifting",
spec=r'''
Return the bitwise AND of all integers in the inclusive range `[left, right]`.

**Example**
```
[5, 7] → 4,   [0, 0] → 0,   [1, 2147483647] → 0
```

**Constraints**
* `0 <= left <= right <= 2^31 - 1`
''',
approach=r'''
**Shift until equal.** While `left != right`, shift both right and count the shifts. The remaining value is the common prefix; shift it
back left. Any bit below the prefix is 0 for at least one number in the range.

* Time: **O(1)** — at most 31 shifts.
* Space: **O(1)** — a shift counter.
''',
java=r'''
public class RangeBitwiseAnd {

    public int rangeBitwiseAnd(int left, int right) {
        int shift = 0;
        while (left != right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        return left << shift;
    }
}
''',
test=r'''
class RangeBitwiseAndTest {

    private final RangeBitwiseAnd solution = new RangeBitwiseAnd();

    @ParameterizedTest
    @CsvSource({"5,7,4", "0,0,0", "1,2147483647,0", "12,15,12", "6,6,6"})
    void ands(int left, int right, int expected) {
        assertEquals(expected, solution.rangeBitwiseAnd(left, right));
    }
}
''',
trace=r'''
function run(l, r) {
  const b = v => v.toString(2).padStart(5, '0').split('');
  const L0 = l; let shift = 0;
  A.step(`AND of every number from ${l} to ${r}. Only the shared high prefix of ${l} and ${r} survives.`, A.arr(`${l}`, b(l), { noIdx: true }), A.arr(`${r}`, b(r), { noIdx: true }));
  while (l !== r) { l >>= 1; r >>= 1; shift++; A.step(`They differ, so drop the lowest bit of both (${shift} dropped).`, A.arr('left', b(l), { noIdx: true }), A.arr('right', b(r), { noIdx: true })); }
  const res = l << shift;
  A.step(`They match: the common prefix is ${l.toString(2)}. Shift it back by ${shift}: ${res}.`, A.arr('result', b(res), { noIdx: true, hl: Object.fromEntries([...Array(5 - shift).keys()].map(i => [i, 'ok'])) }), A.text('Result', res, 'ok'));
}
A.scenario('[5, 7]', 'left = 5, right = 7', () => run(5, 7));
A.scenario('[12, 15]', 'left = 12, right = 15', () => run(12, 15));
'''),
]
