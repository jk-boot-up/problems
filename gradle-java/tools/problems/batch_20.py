PROBLEMS = [
P(num=328, slug="odd-even-linked-list", title="Odd Even Linked List", diff="Medium", topic="Linked List", cls="OddEvenLinkedList",
idea="Build the odd-position chain and the even-position chain in one pass, then attach evens after odds.",
vname="Two interleaved chains", helpers=["ListNode"],
spec=r'''
Group all nodes at **odd positions** (1st, 3rd, …) first, followed by nodes at even positions, keeping relative order within each group.
Use O(1) extra space and O(n) time.

**Example**
```
1 → 2 → 3 → 4 → 5        becomes 1 → 3 → 5 → 2 → 4
2 → 1 → 3 → 5 → 6 → 4 → 7 becomes 2 → 3 → 6 → 7 → 1 → 5 → 4
```

**Constraints**
* `0 <= n <= 10^4`
''',
approach=r'''
**Leapfrog.** `odd` and `even` walk two steps at a time, each skipping over the other's nodes: `odd.next = even.next`,
`even.next = odd.next`. Finally link the odd tail to the saved even head.

* Time: **O(n)** — one pass.
* Space: **O(1)** — pointers only.
''',
java=r'''
public class OddEvenLinkedList {

    public ListNode oddEvenList(ListNode head) {
        if (head == null) return null;
        ListNode odd = head, even = head.next, evenHead = even;
        while (even != null && even.next != null) {
            odd.next = even.next;
            odd = odd.next;
            even.next = odd.next;
            even = even.next;
        }
        odd.next = evenHead;
        return head;
    }
}
''',
test=r'''
class OddEvenLinkedListTest {

    private final OddEvenLinkedList solution = new OddEvenLinkedList();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 3, 5, 2, 4}, ListNode.toArray(solution.oddEvenList(ListNode.of(1, 2, 3, 4, 5))));
        assertArrayEquals(new int[]{2, 3, 6, 7, 1, 5, 4}, ListNode.toArray(solution.oddEvenList(ListNode.of(2, 1, 3, 5, 6, 4, 7))));
        assertNull(solution.oddEvenList(null));
    }
}
''',
trace=r'''
function run(vals) {
  const odd = [], even = [];
  A.step('Walk the list once, sending positions 1, 3, 5, … to the odd chain and 2, 4, … to the even chain.', A.list('list', vals));
  vals.forEach((v, i) => { (i % 2 ? even : odd).push(v); A.step(`Position ${i + 1} (${v}) joins the ${i % 2 ? 'even' : 'odd'} chain.`, A.list('list', vals, { hl: { [i]: i % 2 ? 'alt' : 'sel' } }), A.list('odd', odd), A.list('even', even)); });
  const out = odd.concat(even);
  A.step('Link the end of the odd chain to the head of the even chain.', A.list('result', out, { hl: out.map((_, i) => [i, i < odd.length ? 'sel' : 'alt']) }));
}
A.scenario('Five nodes', '1→2→3→4→5', () => run([1, 2, 3, 4, 5]));
'''),

P(num=229, slug="majority-element-ii", title="Majority Element II", diff="Medium", topic="Arrays & Hashing", cls="MajorityElementII",
idea="At most two values can exceed n/3; extended Boyer–Moore keeps two candidates, then a second pass verifies them.",
vname="Two-candidate voting",
spec=r'''
Return all values that appear **more than ⌊n/3⌋ times** in `nums`, in any order.

**Example**
```
[3,2,3] → [3],   [1] → [1],   [1,2] → [1,2]
```

**Constraints**
* `1 <= nums.length <= 5 * 10^4`

**Follow-up:** O(n) time and O(1) space.
''',
approach=r'''
**Boyer–Moore with two slots.** A matching value adds a vote to its slot; an empty slot adopts the value; otherwise both slots lose a vote
(three distinct values cancel). Survivors are only candidates, so count them in a second pass.

* Time: **O(n)** — two passes.
* Space: **O(1)** — two candidates and two counters.
''',
java=r'''
public class MajorityElementII {

    public List<Integer> majorityElement(int[] nums) {
        int c1 = 0, c2 = 1, n1 = 0, n2 = 0;
        for (int x : nums) {
            if (x == c1) n1++;
            else if (x == c2) n2++;
            else if (n1 == 0) { c1 = x; n1 = 1; }
            else if (n2 == 0) { c2 = x; n2 = 1; }
            else { n1--; n2--; }
        }
        n1 = 0;
        n2 = 0;
        for (int x : nums) {
            if (x == c1) n1++;
            else if (x == c2) n2++;
        }
        List<Integer> out = new ArrayList<>();
        if (n1 > nums.length / 3) out.add(c1);
        if (n2 > nums.length / 3) out.add(c2);
        return out;
    }
}
''',
test=r'''
class MajorityElementIITest {

    private final MajorityElementII solution = new MajorityElementII();

    @Test
    void examples() {
        assertEquals(List.of(3), solution.majorityElement(new int[]{3, 2, 3}));
        assertEquals(List.of(1), solution.majorityElement(new int[]{1}));
        assertEquals(Set.of(1, 2), new HashSet<>(solution.majorityElement(new int[]{1, 2})));
    }

    @Test
    void zeros() {
        assertEquals(List.of(0), solution.majorityElement(new int[]{0, 0, 0}));
    }
}
''',
trace=r'''
function run(a) {
  let c1 = null, c2 = null, n1 = 0, n2 = 0;
  A.step('Keep two candidates. Three different values cancel each other out, so a value above n/3 must survive.', A.arr('nums', a), A.vars({ c1: '-', n1, c2: '-', n2 }));
  a.forEach((x, i) => {
    let msg;
    if (x === c1) { n1++; msg = `${x} votes for candidate 1.`; }
    else if (x === c2) { n2++; msg = `${x} votes for candidate 2.`; }
    else if (!n1) { c1 = x; n1 = 1; msg = `Slot 1 is empty: ${x} becomes candidate 1.`; }
    else if (!n2) { c2 = x; n2 = 1; msg = `Slot 2 is empty: ${x} becomes candidate 2.`; }
    else { n1--; n2--; msg = `${x} matches neither: all three cancel, so both counts drop.`; }
    A.step(msg, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.vars({ c1: c1 ?? '-', n1, c2: c2 ?? '-', n2 }));
  });
  const res = [c1, c2].filter((c, k) => c !== null && (k === 0 || c !== c1) && a.filter(x => x === c).length > Math.floor(a.length / 3));
  A.step(`Second pass: count the candidates. Those above ${Math.floor(a.length / 3)}: [${res}].`, A.arr('nums', a, { hl: Object.fromEntries(a.map((x, i) => [i, res.includes(x) ? 'ok' : 'dim'])) }), A.text('Result', JSON.stringify(res), 'ok'));
}
A.scenario('Two winners', 'nums = [1,1,1,3,3,2,2,2]', () => run([1, 1, 1, 3, 3, 2, 2, 2]));
'''),

P(num=239, slug="sliding-window-maximum", title="Sliding Window Maximum", diff="Hard", topic="Sliding Window", cls="SlidingWindowMaximum",
idea="A deque keeps indices of decreasing values; the front is always the window maximum.",
vname="Monotonic deque",
spec=r'''
A window of size `k` slides over `nums` from left to right. Return the maximum of each window position.

**Example**
```
nums = [1,3,-1,-3,5,3,6,7], k = 3 → [3,3,5,5,6,7]
```

**Constraints**
* `1 <= k <= nums.length <= 10^5`
''',
approach=r'''
**Decreasing deque.** Before pushing index `i`, pop smaller values from the back: they can never be a maximum again. Pop the front
when it falls out of the window. Once the first window is complete, the front holds the maximum.

* Time: **O(n)** — each index enters and leaves the deque once.
* Space: **O(k)** — the deque.
''',
java=r'''
public class SlidingWindowMaximum {

    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] out = new int[nums.length - k + 1];
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < nums.length; i++) {
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
            dq.addLast(i);
            if (dq.peekFirst() <= i - k) dq.pollFirst();
            if (i >= k - 1) out[i - k + 1] = nums[dq.peekFirst()];
        }
        return out;
    }
}
''',
test=r'''
class SlidingWindowMaximumTest {

    private final SlidingWindowMaximum solution = new SlidingWindowMaximum();

    @Test
    void example() {
        assertArrayEquals(new int[]{3, 3, 5, 5, 6, 7}, solution.maxSlidingWindow(new int[]{1, 3, -1, -3, 5, 3, 6, 7}, 3));
    }

    @Test
    void kOne() {
        assertArrayEquals(new int[]{1}, solution.maxSlidingWindow(new int[]{1}, 1));
    }

    @Test
    void decreasing() {
        assertArrayEquals(new int[]{5, 4, 3}, solution.maxSlidingWindow(new int[]{5, 4, 3, 2, 1}, 3));
    }
}
''',
trace=r'''
function run(a, k) {
  const dq = [], out = [];
  A.step(`Window size ${k}. The deque holds indices whose values decrease from front to back.`, A.arr('nums', a), A.arr('deque (values)', []));
  for (let i = 0; i < a.length; i++) {
    const popped = []; while (dq.length && a[dq[dq.length - 1]] <= a[i]) popped.push(a[dq.pop()]);
    dq.push(i);
    let expired = null; if (dq[0] <= i - k) expired = a[dq.shift()];
    if (i >= k - 1) out.push(a[dq[0]]);
    A.step(`Add ${a[i]}.${popped.length ? ` It beats ${popped.join(', ')}, which can never be a maximum again.` : ''}${expired !== null ? ` ${expired} slid out of the window.` : ''}${i >= k - 1 ? ` Window max: ${a[dq[0]]}.` : ''}`, A.arr('nums', a, { range: [Math.max(0, i - k + 1), i], hl: { [dq[0]]: 'ok', [i]: 'cur' } }), A.arr('deque (values)', dq.map(j => a[j]), { hl: { 0: 'ok' } }), A.arr('maxima', out));
  }
}
A.scenario('Classic', 'nums = [1,3,-1,-3,5,3,6,7], k = 3', () => run([1, 3, -1, -3, 5, 3, 6, 7], 3));
'''),

P(num=240, slug="search-a-2d-matrix-ii", title="Search a 2D Matrix II", diff="Medium", topic="Binary Search", cls="Search2DMatrixII",
idea="Start at the top-right corner: moving left decreases, moving down increases, so each step discards a row or a column.",
vname="Staircase from the top-right",
spec=r'''
Each row of the `m × n` matrix is sorted left to right and each column top to bottom. Return `true` if `target` is in the matrix.

**Example**
```
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target 5 → true,  target 20 → false
```

**Constraints**
* `1 <= m, n <= 300`
''',
approach=r'''
**Staircase search.** At `(r, c)` starting from the top-right: if the value is larger than the target, the whole column below is larger
too, so `c--`; if smaller, the whole row to the left is smaller, so `r++`.

* Time: **O(m + n)** — each step removes a row or a column.
* Space: **O(1)** — two indices.
''',
tc="n",
java=r'''
public class Search2DMatrixII {

    public boolean searchMatrix(int[][] matrix, int target) {
        int r = 0, c = matrix[0].length - 1;
        while (r < matrix.length && c >= 0) {
            int v = matrix[r][c];
            if (v == target) return true;
            if (v > target) c--; else r++;
        }
        return false;
    }
}
''',
test=r'''
class Search2DMatrixIITest {

    private final Search2DMatrixII solution = new Search2DMatrixII();
    private final int[][] m = {{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};

    @ParameterizedTest
    @CsvSource({"5,true", "20,false", "30,true", "1,true", "0,false"})
    void searches(int target, boolean expected) {
        assertEquals(expected, solution.searchMatrix(m, target));
    }
}
''',
trace=r'''
function run(m, t) {
  let r = 0, c = m[0].length - 1; const gone = {};
  A.step(`Start at the top-right corner. Look for ${t}.`, A.grid('matrix', m, { hl: { [`${r},${c}`]: 'cur' } }));
  while (r < m.length && c >= 0) {
    const v = m[r][c];
    if (v === t) { A.step(`Found ${t} at (${r},${c}).`, A.grid('matrix', m, { hl: { ...gone, [`${r},${c}`]: 'ok' } }), A.text('Result', 'true', 'ok')); return; }
    if (v > t) { for (let x = r; x < m.length; x++) gone[`${x},${c}`] = 'dim'; A.step(`${v} > ${t}: everything below in this column is even larger. Discard the column and move left.`, A.grid('matrix', m, { hl: { ...gone, [`${r},${c}`]: 'bad' } })); c--; }
    else { for (let y = 0; y <= c; y++) gone[`${r},${y}`] = 'dim'; A.step(`${v} < ${t}: everything to the left in this row is even smaller. Discard the row and move down.`, A.grid('matrix', m, { hl: { ...gone, [`${r},${c}`]: 'bad' } })); r++; }
  }
  A.step(`Fell off the matrix: ${t} is not present.`, A.text('Result', 'false', 'bad'));
}
const M = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]];
A.scenario('Present', 'target = 14', () => run(M, 14));
A.scenario('Absent', 'target = 20', () => run(M, 20));
'''),

P(num=279, slug="perfect-squares", title="Perfect Squares", diff="Medium", topic="1D DP", cls="PerfectSquares",
idea="dp[n] = 1 + min over squares s ≤ n of dp[n − s]: the last square used, plus the best way to make the rest.",
vname="DP over amounts",
spec=r'''
Return the least number of perfect squares (`1, 4, 9, 16, …`) that sum to `n`.

**Example**
```
12 → 3 (4 + 4 + 4),   13 → 2 (4 + 9)
```

**Constraints**
* `1 <= n <= 10^4`
''',
approach=r'''
**Coin change with square coins.** `dp[0] = 0`; for each `i`, try every square `j² <= i`: `dp[i] = min(dp[i], dp[i - j²] + 1)`.

* Time: **O(n·√n)** — √n squares for each amount.
* Space: **O(n)** — the dp array.
''',
tc="n2", sc="n",
java=r'''
public class PerfectSquares {

    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            dp[i] = Integer.MAX_VALUE;
            for (int j = 1; j * j <= i; j++) dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
        }
        return dp[n];
    }
}
''',
test=r'''
class PerfectSquaresTest {

    private final PerfectSquares solution = new PerfectSquares();

    @ParameterizedTest
    @CsvSource({"12,3", "13,2", "1,1", "16,1", "7,4"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.numSquares(n));
    }
}
''',
trace=r'''
function run(n) {
  const dp = [0];
  A.step('dp[i] is the fewest squares adding up to i. dp[0] = 0.', A.arr('dp', dp));
  for (let i = 1; i <= n; i++) {
    let best = Infinity, via = 0;
    for (let j = 1; j * j <= i; j++) if (dp[i - j * j] + 1 < best) { best = dp[i - j * j] + 1; via = j * j; }
    dp.push(best);
    A.step(`dp[${i}]: the best last square is ${via}, so 1 + dp[${i - via}] = ${best}.`, A.arr('dp', dp, { hl: { [i]: 'ok', [i - via]: 'sel' } }));
  }
  A.step(`${n} needs ${dp[n]} square${dp[n] > 1 ? 's' : ''}.`, A.text('Result', dp[n], 'ok'));
}
A.scenario('n = 12', '4 + 4 + 4', () => run(12));
'''),

P(num=309, slug="best-time-to-buy-and-sell-stock-with-cooldown", title="Best Time to Buy and Sell Stock with Cooldown", diff="Medium", topic="1D DP", cls="StockWithCooldown",
idea="Three states per day: holding a share, just sold (cooling down), or resting free to buy.",
vname="Three-state machine",
spec=r'''
You may trade as many times as you like, holding at most one share, but after selling you must wait one day (cooldown) before buying
again. Return the maximum profit.

**Example**
```
[1,2,3,0,2] → 3   (buy, sell, cooldown, buy, sell)
[1]         → 0
```

**Constraints**
* `1 <= prices.length <= 5000`
''',
approach=r'''
**State machine.** `hold = max(hold, rest - p)` (buy only from rest), `sold = hold + p` (sell today), `rest = max(rest, prevSold)`
(yesterday's sale finishes its cooldown). Use the previous day's values for all three.

* Time: **O(n)** — one pass.
* Space: **O(1)** — three numbers.
''',
java=r'''
public class StockWithCooldown {

    public int maxProfit(int[] prices) {
        int hold = Integer.MIN_VALUE, sold = 0, rest = 0;
        for (int p : prices) {
            int prevSold = sold;
            sold = hold + p;
            hold = Math.max(hold, rest - p);
            rest = Math.max(rest, prevSold);
        }
        return Math.max(sold, rest);
    }
}
''',
test=r'''
class StockWithCooldownTest {

    private final StockWithCooldown solution = new StockWithCooldown();

    @Test
    void examples() {
        assertEquals(3, solution.maxProfit(new int[]{1, 2, 3, 0, 2}));
        assertEquals(0, solution.maxProfit(new int[]{1}));
        assertEquals(3, solution.maxProfit(new int[]{2, 1, 4}));
    }
}
''',
trace=r'''
function run(p) {
  let hold = -Infinity, sold = 0, rest = 0;
  const f = v => (v === -Infinity ? '−∞' : v);
  A.step('Three running balances: holding a share, just sold (cooling down), or resting and free to buy.', A.arr('prices', p), A.vars({ hold: '−∞', sold, rest }));
  p.forEach((x, i) => {
    const ps = sold; sold = hold + x; hold = Math.max(hold, rest - x); rest = Math.max(rest, ps);
    A.step(`Day ${i} (${x}): sell from hold → ${f(sold)}; buy from rest → hold ${f(hold)}; yesterday's sale finishes cooling → rest ${rest}.`, A.arr('prices', p, { hl: { [i]: 'cur' } }), A.vars({ hold: f(hold), sold: f(sold), rest }));
  });
  A.step(`Best profit: ${Math.max(sold, rest)}.`, A.text('Result', Math.max(sold, rest), 'ok'));
}
A.scenario('Classic', 'prices = [1,2,3,0,2]', () => run([1, 2, 3, 0, 2]));
'''),

P(num=714, slug="best-time-to-buy-and-sell-stock-with-transaction-fee", title="Best Time to Buy and Sell Stock with Transaction Fee", diff="Medium", topic="1D DP", cls="StockWithFee",
idea="Two states: holding or not; selling pays the fee.",
vname="Two-state machine",
spec=r'''
You may trade as many times as you like, holding at most one share, and every sale costs `fee`. Return the maximum profit.

**Example**
```
prices = [1,3,2,8,4,9], fee = 2 → 8   ((8 − 1 − 2) + (9 − 4 − 2))
```

**Constraints**
* `1 <= prices.length <= 5 * 10^4`
''',
approach=r'''
**DP.** `cash = max(cash, hold + p - fee)` (sell today) and `hold = max(hold, cash - p)` (buy today).

* Time: **O(n)** — one pass.
* Space: **O(1)** — two numbers.
''',
java=r'''
public class StockWithFee {

    public int maxProfit(int[] prices, int fee) {
        int cash = 0, hold = -prices[0];
        for (int p : prices) {
            cash = Math.max(cash, hold + p - fee);
            hold = Math.max(hold, cash - p);
        }
        return cash;
    }
}
''',
test=r'''
class StockWithFeeTest {

    private final StockWithFee solution = new StockWithFee();

    @Test
    void examples() {
        assertEquals(8, solution.maxProfit(new int[]{1, 3, 2, 8, 4, 9}, 2));
        assertEquals(6, solution.maxProfit(new int[]{1, 3, 7, 5, 10, 3}, 3));
    }
}
''',
trace=r'''
function run(p, fee) {
  let cash = 0, hold = -p[0];
  A.step(`cash: best balance with no share. hold: best balance while holding one. Every sale pays ${fee}.`, A.arr('prices', p), A.vars({ cash, hold }));
  p.forEach((x, i) => { const sell = hold + x - fee; cash = Math.max(cash, sell); hold = Math.max(hold, cash - x); A.step(`Day ${i} (${x}): selling now would leave ${sell}, so cash = ${cash}. Buying now would leave ${cash - x}, so hold = ${hold}.`, A.arr('prices', p, { hl: { [i]: 'cur' } }), A.vars({ cash, hold })); });
  A.step(`Best profit: ${cash}.`, A.text('Result', cash, 'ok'));
}
A.scenario('Classic', 'prices = [1,3,2,8,4,9], fee = 2', () => run([1, 3, 2, 8, 4, 9], 2));
'''),

P(num=312, slug="burst-balloons", title="Burst Balloons", diff="Hard", topic="Multidimensional DP", cls="BurstBalloons",
idea="Think about the LAST balloon burst in an interval: its neighbours are then the interval's fixed boundaries.",
vname="Interval DP on the last balloon",
spec=r'''
Bursting balloon `i` earns `nums[left] * nums[i] * nums[right]`, where `left` and `right` are its current neighbours (out of range counts
as 1). Burst all balloons to collect the maximum total.

**Example**
```
[3,1,5,8] → 167   (3·1·5 + 3·5·8 + 1·3·8 + 1·8·1)
[1,5]     → 10
```

**Constraints**
* `1 <= n <= 300`; `0 <= nums[i] <= 100`
''',
approach=r'''
**Interval DP.** Pad with 1s: `a = [1, nums…, 1]`. `dp[l][r]` = best coins from bursting everything strictly between `l` and `r`. If `k`
is the last one burst there, its neighbours are `a[l]` and `a[r]`: `dp[l][r] = max(dp[l][k] + a[l]·a[k]·a[r] + dp[k][r])`. Fill by
increasing gap.

* Time: **O(n³)** — n² intervals × n choices of k.
* Space: **O(n²)** — the table.
''',
tc="n2", sc="n2",
java=r'''
public class BurstBalloons {

    public int maxCoins(int[] nums) {
        int n = nums.length + 2;
        int[] a = new int[n];
        a[0] = a[n - 1] = 1;
        System.arraycopy(nums, 0, a, 1, nums.length);
        int[][] dp = new int[n][n];
        for (int gap = 2; gap < n; gap++) {
            for (int l = 0; l + gap < n; l++) {
                int r = l + gap;
                for (int k = l + 1; k < r; k++) {
                    dp[l][r] = Math.max(dp[l][r], dp[l][k] + a[l] * a[k] * a[r] + dp[k][r]);
                }
            }
        }
        return dp[0][n - 1];
    }
}
''',
test=r'''
class BurstBalloonsTest {

    private final BurstBalloons solution = new BurstBalloons();

    @Test
    void examples() {
        assertEquals(167, solution.maxCoins(new int[]{3, 1, 5, 8}));
        assertEquals(10, solution.maxCoins(new int[]{1, 5}));
        assertEquals(7, solution.maxCoins(new int[]{7}));
    }
}
''',
trace=r'''
function run(nums) {
  const a = [1, ...nums, 1], n = a.length, dp = [...Array(n)].map(() => new Array(n).fill(0));
  const show = () => A.grid('dp[l][r] (best between l and r)', dp.map((r, i) => r.map((v, j) => (j > i + 1 ? v : ''))));
  A.step(`Pad with 1s: [${a}]. dp[l][r] is the best score for bursting everything strictly between l and r.`, A.arr('padded', a), show());
  for (let gap = 2; gap < n; gap++) for (let l = 0; l + gap < n; l++) {
    const r = l + gap; let bk = -1;
    for (let k = l + 1; k < r; k++) { const v = dp[l][k] + a[l] * a[k] * a[r] + dp[k][r]; if (v > dp[l][r]) { dp[l][r] = v; bk = k; } }
    A.step(`Between ${l} and ${r}: bursting ${a[bk]} last (with neighbours ${a[l]} and ${a[r]}) is best: ${dp[l][r]}.`, A.arr('padded', a, { range: [l, r], hl: { [bk]: 'ok', [l]: 'sel', [r]: 'sel' } }), A.grid('dp[l][r] (best between l and r)', dp.map((rw, i) => rw.map((v, j) => (j > i + 1 ? v : ''))), { hl: { [`${l},${r}`]: 'cur' } }));
  }
  A.step(`Maximum coins: ${dp[0][n - 1]}.`, A.text('Result', dp[0][n - 1], 'ok'));
}
A.scenario('Classic', 'nums = [3,1,5,8]', () => run([3, 1, 5, 8]));
'''),

P(num=329, slug="longest-increasing-path-in-a-matrix", title="Longest Increasing Path in a Matrix", diff="Hard", topic="Graph General", cls="LongestIncreasingPath",
idea="DFS from each cell with memoization: the longest path from a cell is 1 + the best path from a larger neighbour.",
vname="Memoized DFS",
spec=r'''
Return the length of the longest strictly increasing path in an integer matrix, moving up, down, left or right.

**Example**
```
[[9,9,4],[6,6,8],[2,1,1]] → 4   (1 → 2 → 6 → 9)
```

**Constraints**
* `1 <= m, n <= 200`
''',
approach=r'''
**Memo DFS.** `len(r, c) = 1 + max(len(neighbour))` over neighbours with a larger value. Strictly increasing paths cannot cycle, so the
memo is safe; each cell is computed once.

* Time: **O(m·n)** — each cell computed once, four neighbours each.
* Space: **O(m·n)** — the memo and the recursion depth.
''',
tc="n2", sc="n2",
java=r'''
public class LongestIncreasingPath {

    private static final int[][] DIRS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int longestIncreasingPath(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length, best = 0;
        int[][] memo = new int[m][n];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) best = Math.max(best, dfs(matrix, r, c, memo));
        }
        return best;
    }

    private int dfs(int[][] g, int r, int c, int[][] memo) {
        if (memo[r][c] != 0) return memo[r][c];
        int best = 1;
        for (int[] d : DIRS) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < g.length && nc >= 0 && nc < g[0].length && g[nr][nc] > g[r][c]) {
                best = Math.max(best, 1 + dfs(g, nr, nc, memo));
            }
        }
        return memo[r][c] = best;
    }
}
''',
test=r'''
class LongestIncreasingPathTest {

    private final LongestIncreasingPath solution = new LongestIncreasingPath();

    @Test
    void examples() {
        assertEquals(4, solution.longestIncreasingPath(new int[][]{{9, 9, 4}, {6, 6, 8}, {2, 1, 1}}));
        assertEquals(4, solution.longestIncreasingPath(new int[][]{{3, 4, 5}, {3, 2, 6}, {2, 2, 1}}));
        assertEquals(1, solution.longestIncreasingPath(new int[][]{{1}}));
    }
}
''',
trace=r'''
function run(g) {
  const m = g.length, n = g[0].length, memo = g.map(r => r.map(() => ''));
  const dfs = (r, c) => {
    if (memo[r][c] !== '') return memo[r][c];
    let best = 1;
    for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const a = r + dr, b = c + dc; if (a >= 0 && a < m && b >= 0 && b < n && g[a][b] > g[r][c]) best = Math.max(best, 1 + dfs(a, b)); }
    memo[r][c] = best;
    A.step(`From (${r},${c}) = ${g[r][c]}, the longest increasing path has ${best} cell${best > 1 ? 's' : ''}. Remember it.`, A.grid('matrix', g, { hl: { [`${r},${c}`]: 'cur' } }), A.grid('memo (longest path from here)', memo, { hl: { [`${r},${c}`]: 'ok' } }));
    return best;
  };
  let best = 0; for (let r = 0; r < m; r++) for (let c = 0; c < n; c++) best = Math.max(best, dfs(r, c));
  A.step(`The longest increasing path has ${best} cells. Each cell was computed only once.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', '[[9,9,4],[6,6,8],[2,1,1]]', () => run([[9, 9, 4], [6, 6, 8], [2, 1, 1]]));
'''),

P(num=213, slug="house-robber-ii", title="House Robber II", diff="Medium", topic="1D DP", cls="HouseRobberII",
idea="The houses form a circle, so the first and last can't both be robbed: solve the line twice, without each end.",
vname="Two linear passes",
spec=r'''
Same as House Robber, but the houses are arranged in a **circle**: the first and last houses are neighbours. Return the maximum amount.

**Example**
```
[2,3,2] → 3,   [1,2,3,1] → 4,   [1,2,3] → 3
```

**Constraints**
* `1 <= nums.length <= 100`
''',
approach=r'''
**Break the circle.** Either the first house is skipped (rob from `1..n-1`) or the last is (rob from `0..n-2`). Run the linear
House Robber on both ranges and take the larger. A single house is a special case.

* Time: **O(n)** — two linear passes.
* Space: **O(1)** — two variables per pass.
''',
java=r'''
public class HouseRobberII {

    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        return Math.max(robLine(nums, 0, n - 2), robLine(nums, 1, n - 1));
    }

    private static int robLine(int[] nums, int lo, int hi) {
        int prev2 = 0, prev1 = 0;
        for (int i = lo; i <= hi; i++) {
            int cur = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}
''',
test=r'''
class HouseRobberIITest {

    private final HouseRobberII solution = new HouseRobberII();

    @Test
    void examples() {
        assertEquals(3, solution.rob(new int[]{2, 3, 2}));
        assertEquals(4, solution.rob(new int[]{1, 2, 3, 1}));
        assertEquals(3, solution.rob(new int[]{1, 2, 3}));
        assertEquals(5, solution.rob(new int[]{5}));
    }
}
''',
trace=r'''
function run(a) {
  const line = (lo, hi) => { let p2 = 0, p1 = 0; for (let i = lo; i <= hi; i++) { const c = Math.max(p1, p2 + a[i]); p2 = p1; p1 = c; } return p1; };
  A.step('In a circle the first and last houses are neighbours. So either skip the first house or skip the last one.', A.arr('houses', a, { hl: { 0: 'alt', [a.length - 1]: 'alt' } }));
  const x = line(0, a.length - 2);
  A.step(`Without the last house, the linear robber gets ${x}.`, A.arr('houses', a, { range: [0, a.length - 2] }), A.vars({ withoutLast: x }));
  const y = line(1, a.length - 1);
  A.step(`Without the first house, the linear robber gets ${y}.`, A.arr('houses', a, { range: [1, a.length - 1] }), A.vars({ withoutLast: x, withoutFirst: y }));
  A.step(`The answer is the better of the two: ${Math.max(x, y)}.`, A.text('Result', Math.max(x, y), 'ok'));
}
A.scenario('Four houses', 'nums = [1,2,3,1]', () => run([1, 2, 3, 1]));
A.scenario('Ends conflict', 'nums = [2,3,2]', () => run([2, 3, 2]));
'''),
]
