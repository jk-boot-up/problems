PROBLEMS = [
P(num=1047, slug="remove-all-adjacent-duplicates-in-string", title="Remove All Adjacent Duplicates In String", diff="Easy", topic="Stack", cls="RemoveAdjacentDuplicates",
idea="Use the result as a stack: a letter equal to the top cancels it, otherwise it is pushed.",
vname="Stack via StringBuilder",
spec=r'''
Repeatedly remove two adjacent equal letters from `s` until no such pair remains. Return the final string (it is unique).

**Example**
```
"abbaca" → "ca",   "azxxzy" → "ay"
```

**Constraints**
* `1 <= s.length <= 10^5`
''',
approach=r'''
**Stack.** For each letter: if it equals the last kept letter, delete that letter; otherwise append it.

* Time: **O(n)** — O(1) per letter.
* Space: **O(n)** — the builder.
''',
sc="n",
java=r'''
public class RemoveAdjacentDuplicates {

    public String removeDuplicates(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            int last = sb.length() - 1;
            if (last >= 0 && sb.charAt(last) == c) sb.deleteCharAt(last);
            else sb.append(c);
        }
        return sb.toString();
    }
}
''',
test=r'''
class RemoveAdjacentDuplicatesTest {

    private final RemoveAdjacentDuplicates solution = new RemoveAdjacentDuplicates();

    @ParameterizedTest
    @CsvSource({"abbaca,ca", "azxxzy,ay", "aa,''", "abc,abc"})
    void removes(String s, String expected) {
        assertEquals(expected, solution.removeDuplicates(s));
    }
}
''',
trace=r'''
function run(s) {
  const st = [];
  [...s].forEach((c, i) => { const hit = st.length && st[st.length - 1] === c; if (hit) st.pop(); else st.push(c); A.step(hit ? `'${c}' matches the top: both vanish.` : `Push '${c}'.`, A.chars('s', s, { hl: { [i]: hit ? 'bad' : 'cur' } }), A.stack('kept', st)); });
  A.step(`Result: "${st.join('')}".`, A.text('Result', st.join(''), 'ok'));
}
A.scenario('Chain reaction', 's = "azxxzy"', () => run('azxxzy'));
'''),

P(num=1009, slug="complement-of-base-10-integer", title="Complement of Base 10 Integer", diff="Easy", topic="Bit Manipulation", cls="ComplementOfBase10",
idea="XOR n with a mask of 1s as long as n's binary representation.",
vname="All-ones mask",
spec=r'''
The complement flips every bit of a number's binary representation (without leading zeros). Return the complement of `n`.

**Example**
```
5 (101) → 2 (010),   7 (111) → 0,   10 (1010) → 5 (0101),   0 → 1
```

**Constraints**
* `0 <= n < 10^9`
''',
approach=r'''
**Mask.** Build `mask = 1, 11, 111, …` until it covers `n`; the answer is `n ^ mask` (for `n = 0`, the mask is `1`).

* Time: **O(log n)** — one step per bit.
* Space: **O(1)** — one mask.
''',
tc="log",
java=r'''
public class ComplementOfBase10 {

    public int bitwiseComplement(int n) {
        int mask = 1;
        while (mask < n) mask = (mask << 1) | 1;
        return n ^ mask;
    }
}
''',
test=r'''
class ComplementOfBase10Test {

    private final ComplementOfBase10 solution = new ComplementOfBase10();

    @ParameterizedTest
    @CsvSource({"5,2", "7,0", "10,5", "0,1", "1,0"})
    void complements(int n, int expected) {
        assertEquals(expected, solution.bitwiseComplement(n));
    }
}
''',
trace=r'''
function run(n) {
  let mask = 1;
  while (mask < n) mask = (mask << 1) | 1;
  const w = Math.max(1, n.toString(2).length), b = v => v.toString(2).padStart(w, '0').split('');
  A.step(`${n} in binary is ${n.toString(2)}. Build a mask of ${w} ones: ${mask.toString(2)}.`, A.arr('n', b(n), { noIdx: true }), A.arr('mask', b(mask), { noIdx: true, hl: Object.fromEntries(b(mask).map((_, i) => [i, 'alt'])) }));
  A.step(`XOR flips every bit: ${b(n ^ mask).join('')} = ${n ^ mask}.`, A.arr('n XOR mask', b(n ^ mask), { noIdx: true, hl: Object.fromEntries(b(n ^ mask).map((c, i) => [i, c === '1' ? 'ok' : 'dim'])) }), A.text('Result', n ^ mask, 'ok'));
}
A.scenario('n = 10', '1010 → 0101', () => run(10));
'''),

P(num=1189, slug="maximum-number-of-balloons", title="Maximum Number of Balloons", diff="Easy", topic="Arrays & Hashing", cls="MaximumBalloons",
idea="Count letters; the answer is limited by the scarcest letter of 'balloon' (l and o are needed twice).",
vname="Letter counts",
spec=r'''
Using each character of `text` at most once, how many times can you form the word `"balloon"`?

**Example**
```
"nlaebolko" → 1,   "loonbalxballpoon" → 2,   "leetcode" → 0
```

**Constraints**
* `1 <= text.length <= 10^4`
''',
approach=r'''
**Bottleneck.** Count letters; the answer is `min(b, a, l/2, o/2, n)`.

* Time: **O(n)** — one counting pass.
* Space: **O(1)** — 26 counters.
''',
java=r'''
public class MaximumBalloons {

    public int maxNumberOfBalloons(String text) {
        int[] c = new int[26];
        for (char ch : text.toCharArray()) c[ch - 'a']++;
        return Math.min(Math.min(c['b' - 'a'], c['a' - 'a']), Math.min(Math.min(c['l' - 'a'] / 2, c['o' - 'a'] / 2), c['n' - 'a']));
    }
}
''',
test=r'''
class MaximumBalloonsTest {

    private final MaximumBalloons solution = new MaximumBalloons();

    @ParameterizedTest
    @CsvSource({"nlaebolko,1", "loonbalxballpoon,2", "leetcode,0"})
    void counts(String text, int expected) {
        assertEquals(expected, solution.maxNumberOfBalloons(text));
    }
}
''',
trace=r'''
function run(text) {
  const c = {}; for (const ch of text) c[ch] = (c[ch] || 0) + 1;
  const need = { b: 1, a: 1, l: 2, o: 2, n: 1 }, per = Object.fromEntries(Object.keys(need).map(k => [k, Math.floor((c[k] || 0) / need[k])]));
  A.step('"balloon" needs b, a, n once and l, o twice.', A.chars('text', text), A.map('letter counts', Object.fromEntries(Object.keys(need).map(k => [k, c[k] || 0]))));
  const ans = Math.min(...Object.values(per)), worst = Object.keys(per).find(k => per[k] === ans);
  A.step(`Balloons each letter allows: ${Object.entries(per).map(([k, v]) => `${k}: ${v}`).join(', ')}. '${worst}' is the bottleneck: ${ans}.`, A.map('balloons per letter', per), A.text('Result', ans, 'ok'));
}
A.scenario('Two balloons', 'text = "loonbalxballpoon"', () => run('loonbalxballpoon'));
'''),

P(num=1260, slug="shift-2d-grid", title="Shift 2D Grid", diff="Easy", topic="Matrix", cls="Shift2DGrid",
idea="Treat the grid as one flat list of m·n cells and rotate it right by k.",
vname="Flat index rotation",
spec=r'''
One shift moves every element one place right in row-major order, with the last element wrapping to the top-left. Return the grid after `k`
shifts.

**Example**
```
grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1 → [[9,1,2],[3,4,5],[6,7,8]]
```

**Constraints**
* `1 <= m, n <= 50`; `0 <= k <= 100`
''',
approach=r'''
**Index arithmetic.** Cell number `i` (row-major) moves to `(i + k) mod (m·n)`.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the output grid.
''',
tc="n2", sc="n2",
java=r'''
public class Shift2DGrid {

    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length, total = m * n;
        Integer[] flat = new Integer[total];
        for (int i = 0; i < total; i++) flat[(i + k) % total] = grid[i / n][i % n];
        List<List<Integer>> out = new ArrayList<>();
        for (int r = 0; r < m; r++) out.add(new ArrayList<>(Arrays.asList(flat).subList(r * n, r * n + n)));
        return out;
    }
}
''',
test=r'''
class Shift2DGridTest {

    private final Shift2DGrid solution = new Shift2DGrid();

    @Test
    void examples() {
        assertEquals(List.of(List.of(9, 1, 2), List.of(3, 4, 5), List.of(6, 7, 8)), solution.shiftGrid(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 1));
        assertEquals(List.of(List.of(1, 2, 3), List.of(4, 5, 6), List.of(7, 8, 9)), solution.shiftGrid(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 9));
    }
}
''',
trace=r'''
function run(g, k) {
  const m = g.length, n = g[0].length, t = m * n, out = [...Array(m)].map(() => new Array(n).fill(''));
  A.step(`Read the grid row by row as one list of ${t} cells. Each cell moves ${k} places forward, wrapping around.`, A.grid('grid', g), A.grid('shifted', out));
  for (let i = 0; i < t; i++) { const j = (i + k) % t; out[Math.floor(j / n)][j % n] = g[Math.floor(i / n)][i % n]; A.step(`Cell #${i} (${g[Math.floor(i / n)][i % n]}) moves to #${j}.`, A.grid('grid', g, { hl: { [`${Math.floor(i / n)},${i % n}`]: 'cur' } }), A.grid('shifted', out, { hl: { [`${Math.floor(j / n)},${j % n}`]: 'ok' } })); }
}
A.scenario('k = 2', '3 × 3 grid', () => run([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2));
'''),

P(num=1295, slug="find-numbers-with-even-number-of-digits", title="Find Numbers with Even Number of Digits", diff="Easy", topic="Math", cls="EvenNumberOfDigits",
idea="Count each number's digits by repeated division by 10.",
vname="Digit counting",
spec=r'''
Return how many numbers in `nums` have an even number of digits.

**Example**
```
[12,345,2,6,7896] → 2,   [555,901,482,1771] → 1
```

**Constraints**
* `1 <= nums[i] <= 10^5`
''',
approach=r'''
**Divide by 10.** Count digits for each number and check parity.

* Time: **O(n log M)** — M is the largest value.
* Space: **O(1)** — counters.
''',
java=r'''
public class EvenNumberOfDigits {

    public int findNumbers(int[] nums) {
        int count = 0;
        for (int x : nums) {
            int digits = 0;
            for (int v = x; v > 0; v /= 10) digits++;
            if (digits % 2 == 0) count++;
        }
        return count;
    }
}
''',
test=r'''
class EvenNumberOfDigitsTest {

    private final EvenNumberOfDigits solution = new EvenNumberOfDigits();

    @Test
    void examples() {
        assertEquals(2, solution.findNumbers(new int[]{12, 345, 2, 6, 7896}));
        assertEquals(1, solution.findNumbers(new int[]{555, 901, 482, 1771}));
        assertEquals(1, solution.findNumbers(new int[]{100000}));
    }
}
''',
trace=r'''
function run(a) {
  let count = 0;
  a.forEach((x, i) => { const d = String(x).length, even = d % 2 === 0; if (even) count++; A.step(`${x} has ${d} digit${d > 1 ? 's' : ''}: ${even ? 'even' : 'odd'}. Count ${count}.`, A.arr('nums', a, { hl: { [i]: even ? 'ok' : 'dim' } })); });
  A.step(`${count} numbers have an even number of digits.`, A.text('Result', count, 'ok'));
}
A.scenario('Classic', 'nums = [12,345,2,6,7896]', () => run([12, 345, 2, 6, 7896]));
'''),

P(num=1299, slug="replace-elements-with-greatest-element-on-right-side", title="Replace Elements with Greatest Element on Right Side", diff="Easy", topic="Arrays & Hashing", cls="ReplaceWithGreatestOnRight",
idea="Walk from the right, carrying the maximum seen so far.",
vname="Right-to-left running maximum",
spec=r'''
Replace every element with the greatest element to its right, and the last element with `-1`.

**Example**
```
[17,18,5,4,6,1] → [18,6,6,6,1,-1],   [400] → [-1]
```

**Constraints**
* `1 <= arr.length <= 10^4`
''',
approach=r'''
**Suffix maximum.** Start with `max = -1`; going right to left, store `max` in the slot, then update `max` with the old value.

* Time: **O(n)** — one pass.
* Space: **O(1)** — apart from the output.
''',
java=r'''
public class ReplaceWithGreatestOnRight {

    public int[] replaceElements(int[] arr) {
        int[] out = new int[arr.length];
        int max = -1;
        for (int i = arr.length - 1; i >= 0; i--) {
            out[i] = max;
            max = Math.max(max, arr[i]);
        }
        return out;
    }
}
''',
test=r'''
class ReplaceWithGreatestOnRightTest {

    private final ReplaceWithGreatestOnRight solution = new ReplaceWithGreatestOnRight();

    @Test
    void examples() {
        assertArrayEquals(new int[]{18, 6, 6, 6, 1, -1}, solution.replaceElements(new int[]{17, 18, 5, 4, 6, 1}));
        assertArrayEquals(new int[]{-1}, solution.replaceElements(new int[]{400}));
    }
}
''',
trace=r'''
function run(a) {
  const out = new Array(a.length).fill(''); let max = -1;
  for (let i = a.length - 1; i >= 0; i--) { out[i] = max; A.step(`Index ${i}: the greatest value to its right is ${max}. Then the running maximum becomes ${Math.max(max, a[i])}.`, A.arr('arr', a, { hl: { [i]: 'cur' } }), A.arr('result', out, { hl: { [i]: 'ok' } })); max = Math.max(max, a[i]); }
}
A.scenario('Classic', 'arr = [17,18,5,4,6,1]', () => run([17, 18, 5, 4, 6, 1]));
'''),

P(num=1342, slug="number-of-steps-to-reduce-a-number-to-zero", title="Number of Steps to Reduce a Number to Zero", diff="Easy", topic="Bit Manipulation", cls="StepsToZero",
idea="Each 1 bit costs a subtraction, and every bit except the top one costs a halving.",
vname="Simulation",
spec=r'''
Repeatedly halve `num` if it is even, or subtract 1 if it is odd, until it is 0. Return the number of steps.

**Example**
```
14 → 6,   8 → 4,   123 → 12
```

**Constraints**
* `0 <= num <= 10^6`
''',
approach=r'''
**Simulate.** At most about 2·log₂(num) steps. (Equivalently: bit length − 1 + number of 1 bits.)

* Time: **O(log n)** — number of bits.
* Space: **O(1)** — a counter.
''',
tc="log",
java=r'''
public class StepsToZero {

    public int numberOfSteps(int num) {
        int steps = 0;
        while (num > 0) {
            num = num % 2 == 0 ? num / 2 : num - 1;
            steps++;
        }
        return steps;
    }
}
''',
test=r'''
class StepsToZeroTest {

    private final StepsToZero solution = new StepsToZero();

    @ParameterizedTest
    @CsvSource({"14,6", "8,4", "123,12", "0,0"})
    void steps(int num, int expected) {
        assertEquals(expected, solution.numberOfSteps(num));
    }
}
''',
trace=r'''
function run(n) {
  let steps = 0;
  while (n > 0) { const even = n % 2 === 0, nx = even ? n / 2 : n - 1; steps++; A.step(`${n} is ${even ? 'even: halve it' : 'odd: subtract 1'} → ${nx}.`, A.vars({ num: nx, steps }), A.arr('binary', nx.toString(2).split(''), { noIdx: true })); n = nx; }
  A.step(`${steps} steps.`, A.text('Result', steps, 'ok'));
}
A.scenario('num = 14', '14 → 0', () => run(14));
'''),

P(num=1365, slug="how-many-numbers-are-smaller-than-the-current-number", title="How Many Numbers Are Smaller Than the Current Number", diff="Easy", topic="Arrays & Hashing", cls="SmallerThanCurrent",
idea="Values are small (0–100): count them, then prefix-sum the counts.",
vname="Counting sort prefix sums",
spec=r'''
For each `nums[i]`, return how many other values in `nums` are strictly smaller.

**Example**
```
[8,1,2,2,3] → [4,0,1,1,3],   [6,5,4,8] → [2,1,0,3],   [7,7,7,7] → [0,0,0,0]
```

**Constraints**
* `2 <= nums.length <= 500`; `0 <= nums[i] <= 100`
''',
approach=r'''
**Counting.** `count[v]` holds how many times `v` appears; turn it into "how many values are less than v" with a running sum.

* Time: **O(n + R)** — R = 101 possible values.
* Space: **O(R)** — the count array.
''',
java=r'''
public class SmallerThanCurrent {

    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] less = new int[102];
        for (int x : nums) less[x + 1]++;
        for (int v = 1; v < less.length; v++) less[v] += less[v - 1];
        int[] out = new int[nums.length];
        for (int i = 0; i < nums.length; i++) out[i] = less[nums[i]];
        return out;
    }
}
''',
test=r'''
class SmallerThanCurrentTest {

    private final SmallerThanCurrent solution = new SmallerThanCurrent();

    @Test
    void examples() {
        assertArrayEquals(new int[]{4, 0, 1, 1, 3}, solution.smallerNumbersThanCurrent(new int[]{8, 1, 2, 2, 3}));
        assertArrayEquals(new int[]{2, 1, 0, 3}, solution.smallerNumbersThanCurrent(new int[]{6, 5, 4, 8}));
        assertArrayEquals(new int[]{0, 0, 0, 0}, solution.smallerNumbersThanCurrent(new int[]{7, 7, 7, 7}));
    }
}
''',
trace=r'''
function run(a) {
  const mx = Math.max(...a), cnt = new Array(mx + 1).fill(0); a.forEach(x => cnt[x]++);
  A.step('Count how many times each value appears.', A.arr('nums', a), A.arr('count (index = value)', cnt));
  const less = []; let run = 0; cnt.forEach((c, v) => { less.push(run); run += c; });
  A.step('Running total: less[v] = how many values are below v.', A.arr('less (index = value)', less));
  const out = a.map(x => less[x]);
  A.step(`Look up each number: [${out}].`, A.arr('nums', a), A.arr('answer', out, { hl: Object.fromEntries(out.map((_, i) => [i, 'ok'])) }));
}
A.scenario('Classic', 'nums = [8,1,2,2,3]', () => run([8, 1, 2, 2, 3]));
'''),

P(num=1480, slug="running-sum-of-1d-array", title="Running Sum of 1d Array", diff="Easy", topic="Prefix Sum", cls="RunningSum",
idea="Each prefix sum is the previous prefix sum plus the current value.",
vname="Prefix sums",
spec=r'''
Return the running sum: `runningSum[i] = nums[0] + … + nums[i]`.

**Example**
```
[1,2,3,4] → [1,3,6,10],   [1,1,1,1,1] → [1,2,3,4,5]
```

**Constraints**
* `1 <= nums.length <= 1000`
''',
approach=r'''
**One pass.** `out[i] = out[i-1] + nums[i]`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — apart from the output.
''',
java=r'''
public class RunningSum {

    public int[] runningSum(int[] nums) {
        int[] out = nums.clone();
        for (int i = 1; i < out.length; i++) out[i] += out[i - 1];
        return out;
    }
}
''',
test=r'''
class RunningSumTest {

    private final RunningSum solution = new RunningSum();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 3, 6, 10}, solution.runningSum(new int[]{1, 2, 3, 4}));
        assertArrayEquals(new int[]{3, 4, 6, 16, 17}, solution.runningSum(new int[]{3, 1, 2, 10, 1}));
    }
}
''',
trace=r'''
function run(a) {
  const out = [a[0]];
  A.step(`The first running sum is just ${a[0]}.`, A.arr('nums', a), A.arr('running sum', out));
  for (let i = 1; i < a.length; i++) { out.push(out[i - 1] + a[i]); A.step(`${out[i - 1]} + ${a[i]} = ${out[i]}.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.arr('running sum', out, { hl: { [i]: 'ok', [i - 1]: 'sel' } })); }
}
A.scenario('Classic', 'nums = [3,1,2,10,1]', () => run([3, 1, 2, 10, 1]));
'''),

P(num=1512, slug="number-of-good-pairs", title="Number of Good Pairs", diff="Easy", topic="Arrays & Hashing", cls="NumberOfGoodPairs",
idea="Each new copy of a value pairs with every earlier copy of it.",
vname="Running counts",
spec=r'''
A pair `(i, j)` is good if `nums[i] == nums[j]` and `i < j`. Return the number of good pairs.

**Example**
```
[1,2,3,1,1,3] → 4,   [1,1,1,1] → 6,   [1,2,3] → 0
```

**Constraints**
* `1 <= nums.length <= 100`; `1 <= nums[i] <= 100`
''',
approach=r'''
**Count as you go.** When a value appears for the k-th time, it forms `k - 1` new pairs; add the current count before incrementing it.

* Time: **O(n)** — one pass.
* Space: **O(1)** — 101 counters.
''',
java=r'''
public class NumberOfGoodPairs {

    public int numIdenticalPairs(int[] nums) {
        int[] seen = new int[101];
        int pairs = 0;
        for (int x : nums) pairs += seen[x]++;
        return pairs;
    }
}
''',
test=r'''
class NumberOfGoodPairsTest {

    private final NumberOfGoodPairs solution = new NumberOfGoodPairs();

    @Test
    void examples() {
        assertEquals(4, solution.numIdenticalPairs(new int[]{1, 2, 3, 1, 1, 3}));
        assertEquals(6, solution.numIdenticalPairs(new int[]{1, 1, 1, 1}));
        assertEquals(0, solution.numIdenticalPairs(new int[]{1, 2, 3}));
    }
}
''',
trace=r'''
function run(a) {
  const seen = {}; let pairs = 0;
  a.forEach((x, i) => { const before = seen[x] || 0; pairs += before; seen[x] = before + 1; A.step(`${x} has appeared ${before} time${before === 1 ? '' : 's'} before: ${before} new pair${before === 1 ? '' : 's'}. Total ${pairs}.`, A.arr('nums', a, { hl: { [i]: before ? 'ok' : 'cur', ...Object.fromEntries(a.slice(0, i).map((v, t) => [t, v === x ? 'sel' : ''])) } }), A.map('seen so far', seen)); });
  A.step(`${pairs} good pairs.`, A.text('Result', pairs, 'ok'));
}
A.scenario('Classic', 'nums = [1,2,3,1,1,3]', () => run([1, 2, 3, 1, 1, 3]));
'''),
]
