PROBLEMS = [
P(num=274, slug="h-index", title="H-Index", diff="Medium", topic="Array / String", cls="HIndex",
idea="Count papers by citation (capped at n), then walk down from n until at least h papers have h or more citations.",
spec=r'''
`citations[i]` is the number of citations of a researcher's `i`-th paper. Return the researcher's **h-index**: the largest
`h` such that at least `h` papers each have at least `h` citations.

**Example 1**
```
Input:  citations = [3,0,6,1,5]
Output: 3   (three papers have ≥ 3 citations)
```

**Example 2**
```
Input:  citations = [1,3,1]
Output: 1
```

**Constraints**
* `1 <= n <= 5000`
* `0 <= citations[i] <= 1000`
''',
approach=r'''
**Counting sort.** The answer is at most `n`, so put every paper into a bucket `min(c, n)`. Walk `h` from `n` down to 0,
keeping a running total of papers with at least `h` citations. The first `h` where that total reaches `h` is the answer.

* Time: **O(n)** — one pass to fill buckets, one pass down them.
* Space: **O(n)** — the bucket array of size n + 1.
''',
java=r'''
public class HIndex {

    public int hIndex(int[] citations) {
        int n = citations.length;
        int[] buckets = new int[n + 1];
        for (int c : citations) {
            buckets[Math.min(c, n)]++;
        }
        int papers = 0;
        for (int h = n; h >= 0; h--) {
            papers += buckets[h];
            if (papers >= h) {
                return h;
            }
        }
        return 0;
    }
}
''',
test=r'''
class HIndexTest {

    private final HIndex solution = new HIndex();

    @Test
    void example1() {
        assertEquals(3, solution.hIndex(new int[]{3, 0, 6, 1, 5}));
    }

    @Test
    void example2() {
        assertEquals(1, solution.hIndex(new int[]{1, 3, 1}));
    }

    @Test
    void noCitations() {
        assertEquals(0, solution.hIndex(new int[]{0, 0}));
    }

    @Test
    void allHighlyCited() {
        assertEquals(3, solution.hIndex(new int[]{100, 100, 100}));
    }
}
''',
trace=r'''
function run(c) {
  const n = c.length, b = new Array(n + 1).fill(0);
  A.step(`The h-index can be at most ${n}, the number of papers. Make buckets 0 to ${n}; a paper with more than ${n} citations goes in bucket ${n}.`, A.arr('citations', c), A.arr('buckets', b));
  c.forEach((x, i) => { b[Math.min(x, n)]++; A.step(`Paper ${i} has ${x} citations, so it goes in bucket ${Math.min(x, n)}.`, A.arr('citations', c, { hl: { [i]: 'cur' } }), A.arr('buckets', b, { hl: { [Math.min(x, n)]: 'sel' } })); });
  let papers = 0;
  for (let h = n; h >= 0; h--) {
    papers += b[h];
    const ok = papers >= h;
    A.step(`h = ${h}: ${papers} paper${papers === 1 ? '' : 's'} have at least ${h} citations. ${ok ? `That is enough, so the h-index is ${h}.` : `We need ${h}, so try a smaller h.`}`, A.arr('buckets', b, { ptr: [[h, 'h']], hl: b.map((_, t) => [t, t >= h ? (ok ? 'ok' : 'sel') : 'dim']) }), A.vars({ h, papers }));
    if (ok) { A.step(`The answer is ${h}.`, A.arr('citations', c, { hl: c.map((x, t) => [t, x >= h ? 'ok' : 'dim']) }), A.text('Result', h, 'ok')); return; }
  }
}
A.scenario('Mixed citations', 'citations = [3,0,6,1,5]', () => run([3, 0, 6, 1, 5]));
A.scenario('Small counts', 'citations = [1,3,1]', () => run([1, 3, 1]));
A.scenario('Edge: no citations', 'citations = [0,0]', () => run([0, 0]));
'''),

P(num=380, slug="insert-delete-getrandom-o1", title="Insert Delete GetRandom O(1)", diff="Medium", topic="Array / String", cls="RandomizedSet",
idea="An array gives O(1) random picks; a value→index map gives O(1) lookups; delete by swapping with the last element.",
spec=r'''
Implement `RandomizedSet`:
* `boolean insert(int val)`: inserts `val` if absent. Returns `true` if it was inserted.
* `boolean remove(int val)`: removes `val` if present. Returns `true` if it was removed.
* `int getRandom()`: returns a random element (the set is non-empty when called); each element must be equally likely.

Every operation must run in **average O(1)** time.

**Example**
```
insert(1) → true, remove(2) → false, insert(2) → true, getRandom() → 1 or 2,
remove(1) → true, insert(2) → false, getRandom() → 2
```

**Constraints**
* `-2^31 <= val <= 2^31 - 1`
* At most `2 * 10^5` calls in total.
''',
approach=r'''
**ArrayList + hash map.** We use our own `MyHashMap` (bucket array + chaining). The list stores values so `getRandom` picks a random index. The map stores each value's index.
To remove `val`, move the **last** value into `val`'s slot, update that value's index, and drop the last slot. Nothing shifts.

* Time: **O(1)** — average per operation (hash map + array end operations).
* Space: **O(n)** — the list and the map each hold every stored value.
''',
java=r'''
public class RandomizedSet {

    private final List<Integer> values = new ArrayList<>();
    private final MyHashMap<Integer, Integer> indexOf = new MyHashMap<>();
    private final Random random;

    public RandomizedSet() {
        this(new Random());
    }

    RandomizedSet(Random random) {
        this.random = random;
    }

    public boolean insert(int val) {
        if (indexOf.containsKey(val)) {
            return false;
        }
        indexOf.put(val, values.size());
        values.add(val);
        return true;
    }

    public boolean remove(int val) {
        Integer idx = indexOf.remove(val);
        if (idx == null) {
            return false;
        }
        int last = values.removeLast();
        if (idx < values.size()) {
            values.set(idx, last);
            indexOf.put(last, idx);
        }
        return true;
    }

    public int getRandom() {
        return values.get(random.nextInt(values.size()));
    }
}
''',
test=r'''
class RandomizedSetTest {

    @Test
    void exampleSequence() {
        RandomizedSet set = new RandomizedSet();
        assertTrue(set.insert(1));
        assertFalse(set.remove(2));
        assertTrue(set.insert(2));
        assertTrue(Set.of(1, 2).contains(set.getRandom()));
        assertTrue(set.remove(1));
        assertFalse(set.insert(2));
        assertEquals(2, set.getRandom());
    }

    @Test
    void removeMiddleKeepsOthers() {
        RandomizedSet set = new RandomizedSet(new Random(1));
        for (int i = 0; i < 5; i++) set.insert(i);
        assertTrue(set.remove(2));
        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < 200; i++) seen.add(set.getRandom());
        assertEquals(Set.of(0, 1, 3, 4), seen);
    }
}
''',
trace=r'''
const vals = [], idx = new Map();
const view = (hl = {}) => [A.arr('values (ArrayList)', vals, { hl }), A.hashTable('indexOf (MyHashMap)', idx)];
A.step('We keep values in an array for random access, and a map from each value to its index for constant-time lookups.', view());
function insert(v) {
  if (idx.has(v)) { A.step(`insert(${v}): ${v} is already in the map, so return false.`, view({ [idx.get(v)]: 'bad' })); return; }
  idx.set(v, vals.length); vals.push(v);
  A.step(`insert(${v}): append it at index ${vals.length - 1} and record that index in the map. Return true.`, view({ [vals.length - 1]: 'ok' }));
}
function remove(v) {
  if (!idx.has(v)) { A.step(`remove(${v}): ${v} is not in the map, so return false.`, view()); return; }
  const i = idx.get(v), last = vals[vals.length - 1];
  A.step(`remove(${v}): it sits at index ${i}. Instead of shifting, move the last value ${last} into that slot.`, view({ [i]: 'bad', [vals.length - 1]: 'sel' }));
  vals[i] = last; idx.set(last, i); vals.pop(); idx.delete(v);
  A.step(`Drop the last slot, update ${last}'s index to ${i}, and delete ${v} from the map. Return true. Nothing had to shift.`, view(i < vals.length ? { [i]: 'ok' } : {}));
}
A.scenario('Insert, remove, random', 'insert 10, 20, 30, 40 · remove 20 · getRandom', () => {
  [10, 20, 30, 40].forEach(insert); insert(20); remove(20); remove(99);
  A.step(`getRandom(): pick a random index between 0 and ${vals.length - 1}. Each of the ${vals.length} values is equally likely.`, view({ 1: 'cur' }), A.text('Picked', vals[1], 'ok'));
});
A.scenario('Remove the last element', 'insert 1, 2 · remove 2', () => { insert(1); insert(2); remove(2); });
'''),

P(num=238, slug="product-of-array-except-self", title="Product of Array Except Self", diff="Medium", topic="Array / String", cls="ProductExceptSelf",
idea="answer[i] = (product of everything left of i) × (product of everything right of i), built in two passes.",
spec=r'''
Given an integer array `nums`, return an array `answer` where `answer[i]` equals the product of every element of `nums`
**except** `nums[i]`. Do it in O(n) time **without using division**. Every prefix/suffix product fits in a 32-bit integer.

**Example 1**
```
Input:  nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2**
```
Input:  nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints**
* `2 <= nums.length <= 10^5`
* `-30 <= nums[i] <= 30`

**Follow-up:** O(1) extra space (the output array does not count).
''',
approach=r'''
**Prefix and suffix products.** First pass, left to right: `answer[i]` = product of all values before `i`.
Second pass, right to left: keep a running `suffix` product and multiply it into `answer[i]`.

* Time: **O(n)** — two linear passes.
* Space: **O(1)** — besides the output, only the running suffix product.
''',
java=r'''
public class ProductExceptSelf {

    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        answer[0] = 1;
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= suffix;
            suffix *= nums[i];
        }
        return answer;
    }
}
''',
test=r'''
class ProductExceptSelfTest {

    private final ProductExceptSelf solution = new ProductExceptSelf();

    @Test
    void example1() {
        assertArrayEquals(new int[]{24, 12, 8, 6}, solution.productExceptSelf(new int[]{1, 2, 3, 4}));
    }

    @Test
    void withZero() {
        assertArrayEquals(new int[]{0, 0, 9, 0, 0}, solution.productExceptSelf(new int[]{-1, 1, 0, -3, 3}));
    }

    @Test
    void twoElements() {
        assertArrayEquals(new int[]{3, 2}, solution.productExceptSelf(new int[]{2, 3}));
    }
}
''',
trace=r'''
function run(a) {
  const n = a.length, ans = new Array(n).fill('');
  ans[0] = 1;
  A.step('Pass 1, left to right: answer[i] holds the product of everything to the left of i. Nothing is left of index 0, so it starts at 1.', A.arr('nums', a), A.arr('answer', ans, { hl: { 0: 'ok' } }));
  for (let i = 1; i < n; i++) {
    ans[i] = ans[i - 1] * a[i - 1];
    A.step(`answer[${i}] = answer[${i - 1}] × nums[${i - 1}] = ${ans[i - 1]} × ${a[i - 1]} = ${ans[i]}.`, A.arr('nums', a, { hl: a.map((_, t) => [t, t < i ? 'sel' : '']) }), A.arr('answer', ans, { hl: { [i]: 'cur' } }));
  }
  let suf = 1;
  A.step('Pass 2, right to left: multiply in the product of everything to the right, kept in suffix.', A.arr('nums', a), A.arr('answer', ans), A.vars({ suffix: suf }));
  for (let i = n - 1; i >= 0; i--) {
    const before = ans[i]; ans[i] *= suf;
    A.step(`answer[${i}] = ${before} × suffix ${suf} = ${ans[i]}. Then suffix becomes ${suf} × ${a[i]} = ${suf * a[i]}.`, A.arr('nums', a, { hl: a.map((_, t) => [t, t > i ? 'alt' : t === i ? 'cur' : '']) }), A.arr('answer', ans, { hl: { [i]: 'ok' } }), A.vars({ suffix: suf * a[i] }));
    suf *= a[i];
  }
  A.step('Each answer is the left product times the right product, and we never divided.', A.arr('answer', ans, { hl: ans.map((_, t) => [t, 'ok']) }), A.text('Result', JSON.stringify(ans), 'ok'));
}
A.scenario('Plain values', 'nums = [1,2,3,4]', () => run([1, 2, 3, 4]));
A.scenario('Edge: contains a zero', 'nums = [-1,1,0,-3,3]', () => run([-1, 1, 0, -3, 3]));
'''),

P(num=134, slug="gas-station", title="Gas Station", diff="Medium", topic="Array / String", cls="GasStation",
idea="If total gas ≥ total cost a solution exists; whenever the tank goes negative, the start must be after this station.",
spec=r'''
There are `n` gas stations on a circular route. Station `i` gives `gas[i]` fuel, and driving from station `i` to `i + 1`
costs `cost[i]`. Starting with an empty tank, return the index of the station from which you can drive all the way around
once, or `-1` if impossible. If a solution exists it is unique.

**Example 1**
```
Input:  gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
```

**Example 2**
```
Input:  gas = [2,3,4], cost = [3,4,3]
Output: -1
```

**Constraints**
* `1 <= n <= 10^5`
* `0 <= gas[i], cost[i] <= 10^4`
''',
approach=r'''
**Greedy single pass.** Track `total = Σ(gas - cost)`; if it is negative, no start works. Also track the current `tank`
from a candidate `start`. If `tank` drops below 0 at station `i`, no station between `start` and `i` can be the start
(each would arrive at `i` with even less fuel), so set `start = i + 1` and reset the tank.

* Time: **O(n)** — one pass around the stations.
* Space: **O(1)** — three running numbers.
''',
java=r'''
public class GasStation {

    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total = 0, tank = 0, start = 0;
        for (int i = 0; i < gas.length; i++) {
            int diff = gas[i] - cost[i];
            total += diff;
            tank += diff;
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        return total >= 0 ? start : -1;
    }
}
''',
test=r'''
class GasStationTest {

    private final GasStation solution = new GasStation();

    @Test
    void example1() {
        assertEquals(3, solution.canCompleteCircuit(new int[]{1, 2, 3, 4, 5}, new int[]{3, 4, 5, 1, 2}));
    }

    @Test
    void impossible() {
        assertEquals(-1, solution.canCompleteCircuit(new int[]{2, 3, 4}, new int[]{3, 4, 3}));
    }

    @Test
    void singleStation() {
        assertEquals(0, solution.canCompleteCircuit(new int[]{5}, new int[]{4}));
    }
}
''',
trace=r'''
function run(gas, cost) {
  const n = gas.length, diff = gas.map((g, i) => g - cost[i]);
  let total = 0, tank = 0, start = 0;
  A.step('For each station, gas minus cost is the net fuel gained by leaving it. We look for a start where the tank never goes negative.', A.arr('gas', gas), A.arr('cost', cost), A.arr('gas − cost', diff), A.vars({ start, tank, total }));
  for (let i = 0; i < n; i++) {
    total += diff[i]; tank += diff[i];
    const hl = diff.map((_, t) => [t, t < start ? 'dim' : t === i ? (tank < 0 ? 'bad' : 'cur') : t > start - 1 && t < i ? 'sel' : '']);
    if (tank < 0) {
      A.step(`At station ${i} the tank drops to ${tank}. No station from ${start} to ${i} can be the start, so try station ${i + 1} next with an empty tank.`, A.arr('gas − cost', diff, { ptr: [[start, 'start'], [i, 'i']], hl }), A.vars({ start: i + 1, tank: 0, total }));
      start = i + 1; tank = 0;
    } else A.step(`Station ${i} adds ${diff[i]}, so the tank holds ${tank}. Keep going.`, A.arr('gas − cost', diff, { ptr: [[start, 'start'], [i, 'i']], hl }), A.vars({ start, tank, total }));
  }
  if (total >= 0) A.step(`Total net fuel is ${total}, which is not negative, so a full loop is possible. It starts at station ${start}.`, A.arr('gas − cost', diff, { hl: { [start]: 'ok' }, ptr: [[start, 'start']] }), A.text('Result', start, 'ok'));
  else A.step(`Total net fuel is ${total}. The route needs more fuel than all the stations provide, so the answer is -1.`, A.arr('gas − cost', diff), A.text('Result', -1, 'bad'));
}
A.scenario('Start in the middle', 'gas = [1,2,3,4,5], cost = [3,4,5,1,2]', () => run([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]));
A.scenario('Edge: impossible', 'gas = [2,3,4], cost = [3,4,3]', () => run([2, 3, 4], [3, 4, 3]));
'''),

P(num=135, slug="candy", title="Candy", diff="Hard", topic="Array / String", cls="Candy",
idea="Satisfy left neighbours in one pass and right neighbours in a second pass, taking the max at each child.",
spec=r'''
`n` children stand in a line; `ratings[i]` is child `i`'s rating. Give out candies so that:
* every child gets at least one candy, and
* a child with a higher rating than a neighbour gets more candies than that neighbour.

Return the minimum total number of candies.

**Example 1**
```
Input:  ratings = [1,0,2]
Output: 5   (2, 1, 2)
```

**Example 2**
```
Input:  ratings = [1,2,2]
Output: 4   (1, 2, 1)
```

**Constraints**
* `1 <= n <= 2 * 10^4`
* `0 <= ratings[i] <= 2 * 10^4`
''',
approach=r'''
**Two passes.** Start everyone at 1. Left to right: if `ratings[i] > ratings[i-1]`, set `candy[i] = candy[i-1] + 1`.
Right to left: if `ratings[i] > ratings[i+1]`, set `candy[i] = max(candy[i], candy[i+1] + 1)`. Both rules now hold with the
fewest candies.

* Time: **O(n)** — two passes.
* Space: **O(n)** — the candy array.
''',
java=r'''
public class Candy {

    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] candies = new int[n];
        Arrays.fill(candies, 1);
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);
            }
        }
        return Arrays.stream(candies).sum();
    }
}
''',
test=r'''
class CandyTest {

    private final Candy solution = new Candy();

    @Test
    void valley() {
        assertEquals(5, solution.candy(new int[]{1, 0, 2}));
    }

    @Test
    void equalNeighbours() {
        assertEquals(4, solution.candy(new int[]{1, 2, 2}));
    }

    @Test
    void decreasing() {
        assertEquals(6, solution.candy(new int[]{3, 2, 1}));
    }

    @Test
    void single() {
        assertEquals(1, solution.candy(new int[]{7}));
    }
}
''',
trace=r'''
function run(r) {
  const n = r.length, c = new Array(n).fill(1);
  A.step('Every child starts with one candy.', A.arr('ratings', r), A.arr('candies', c));
  for (let i = 1; i < n; i++) {
    if (r[i] > r[i - 1]) { c[i] = c[i - 1] + 1; A.step(`Left pass: rating ${r[i]} beats its left neighbour's ${r[i - 1]}, so child ${i} gets ${c[i]}, one more than the left neighbour.`, A.arr('ratings', r, { hl: { [i - 1]: 'sel', [i]: 'cur' } }), A.arr('candies', c, { hl: { [i]: 'ok' } })); }
    else A.step(`Left pass: rating ${r[i]} is not higher than ${r[i - 1]}, so no change.`, A.arr('ratings', r, { hl: { [i - 1]: 'sel', [i]: 'dim' } }), A.arr('candies', c));
  }
  for (let i = n - 2; i >= 0; i--) {
    if (r[i] > r[i + 1]) { const old = c[i]; c[i] = Math.max(c[i], c[i + 1] + 1); A.step(`Right pass: rating ${r[i]} beats its right neighbour's ${r[i + 1]}, so child ${i} needs at least ${c[i + 1] + 1}. ${old === c[i] ? 'It already has enough.' : `Raise it to ${c[i]}.`}`, A.arr('ratings', r, { hl: { [i + 1]: 'sel', [i]: 'cur' } }), A.arr('candies', c, { hl: { [i]: 'ok' } })); }
    else A.step(`Right pass: rating ${r[i]} is not higher than ${r[i + 1]}, so no change.`, A.arr('ratings', r, { hl: { [i + 1]: 'sel', [i]: 'dim' } }), A.arr('candies', c));
  }
  const sum = c.reduce((x, y) => x + y, 0);
  A.step(`Both rules hold. Total candies: ${sum}.`, A.arr('ratings', r), A.arr('candies', c, { hl: c.map((_, t) => [t, 'ok']) }), A.text('Result', sum, 'ok'));
}
A.scenario('Mountain', 'ratings = [1,3,4,5,2]', () => run([1, 3, 4, 5, 2]));
A.scenario('Valley', 'ratings = [1,0,2]', () => run([1, 0, 2]));
A.scenario('Edge: equal ratings', 'ratings = [1,2,2]', () => run([1, 2, 2]));
'''),

P(num=42, slug="trapping-rain-water", title="Trapping Rain Water", diff="Hard", topic="Array / String", cls="TrappingRainWater",
idea="Water above a bar is limited by the lower of the tallest walls on each side; two pointers always move the lower side.",
spec=r'''
`height[i]` is the height of a bar of width 1. After it rains, how many units of water are trapped between the bars?

**Example 1**
```
Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

**Example 2**
```
Input:  height = [4,2,0,3,2,5]
Output: 9
```

**Constraints**
* `1 <= n <= 2 * 10^4`
* `0 <= height[i] <= 10^5`
''',
approach=r'''
**Two pointers.** Water at `i` is `min(maxLeft, maxRight) - height[i]`. Keep `l` and `r` at the ends with running `leftMax` and
`rightMax`. If `leftMax < rightMax`, the left side is the bottleneck for `l`, so its water is exactly `leftMax - height[l]`.
Add it and move `l` right. Otherwise do the same on the right.

* Time: **O(n)** — each bar is visited once.
* Space: **O(1)** — two pointers and two maxima.
''',
java=r'''
public class TrappingRainWater {

    public int trap(int[] height) {
        int l = 0, r = height.length - 1, leftMax = 0, rightMax = 0, water = 0;
        while (l < r) {
            leftMax = Math.max(leftMax, height[l]);
            rightMax = Math.max(rightMax, height[r]);
            if (leftMax < rightMax) {
                water += leftMax - height[l++];
            } else {
                water += rightMax - height[r--];
            }
        }
        return water;
    }
}
''',
test=r'''
class TrappingRainWaterTest {

    private final TrappingRainWater solution = new TrappingRainWater();

    @Test
    void example1() {
        assertEquals(6, solution.trap(new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}));
    }

    @Test
    void example2() {
        assertEquals(9, solution.trap(new int[]{4, 2, 0, 3, 2, 5}));
    }

    @Test
    void noWalls() {
        assertEquals(0, solution.trap(new int[]{1, 2, 3}));
    }
}
''',
trace=r'''
function run(h) {
  const n = h.length, W = new Array(n).fill(0), H = Math.max(...h);
  let l = 0, r = n - 1, lm = 0, rm = 0, water = 0;
  const pic = () => { const g = []; for (let y = H; y >= 1; y--) g.push(h.map(() => '')); return g; };
  const ghl = (cur) => { const o = []; for (let y = H; y >= 1; y--) h.forEach((v, x) => { if (v >= y) o.push([`${H - y},${x}`, x === cur ? 'bar,cur' : 'bar']); else if (v + W[x] >= y) o.push([`${H - y},${x}`, x === cur ? 'water,cur' : 'water']); }); return o; };
  A.step('Bars are grey and trapped water is blue. Two pointers start at the ends, each with the tallest wall seen on its side.', A.grid('elevation map', pic(), { hl: ghl(-1) }), A.arr('height', h, { ptr: [[l, 'l'], [r, 'r']] }), A.vars({ leftMax: lm, rightMax: rm, water }));
  while (l < r) {
    lm = Math.max(lm, h[l]); rm = Math.max(rm, h[r]);
    if (lm < rm) {
      const w = lm - h[l]; W[l] = w; water += w;
      A.step(`leftMax ${lm} is lower than rightMax ${rm}, so the left side limits index ${l}. Water there is ${lm} − ${h[l]} = ${w}.`, A.grid('elevation map', pic(), { hl: ghl(l) }), A.arr('height', h, { ptr: [[l, 'l'], [r, 'r']], hl: { [l]: 'cur' } }), A.vars({ leftMax: lm, rightMax: rm, water }));
      l++;
    } else {
      const w = rm - h[r]; W[r] = w; water += w;
      A.step(`rightMax ${rm} is not higher than leftMax ${lm}, so the right side limits index ${r}. Water there is ${rm} − ${h[r]} = ${w}.`, A.grid('elevation map', pic(), { hl: ghl(r) }), A.arr('height', h, { ptr: [[l, 'l'], [r, 'r']], hl: { [r]: 'cur' } }), A.vars({ leftMax: lm, rightMax: rm, water }));
      r--;
    }
  }
  A.step(`The pointers met. Total trapped water: ${water}.`, A.grid('elevation map', pic(), { hl: ghl(-1) }), A.text('Result', water, 'ok'));
}
A.scenario('Basin', 'height = [4,2,0,3,2,5]', () => run([4, 2, 0, 3, 2, 5]));
A.scenario('Many pools', 'height = [0,1,0,2,1,0,1,3,2,1,2,1]', () => run([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));
A.scenario('Edge: staircase holds nothing', 'height = [1,2,3]', () => run([1, 2, 3]));
'''),

P(num=13, slug="roman-to-integer", title="Roman to Integer", diff="Easy", topic="Array / String", cls="RomanToInteger",
idea="Add each symbol's value, but subtract it when a larger symbol follows (IV, IX, XL, ...).",
spec=r'''
Roman numerals use `I=1, V=5, X=10, L=50, C=100, D=500, M=1000`. Symbols are usually written largest to smallest,
except for six subtractive pairs: `IV=4, IX=9, XL=40, XC=90, CD=400, CM=900`. Convert a valid Roman numeral `s` to an integer.

**Example 1**
```
Input:  s = "LVIII"
Output: 58
```

**Example 2**
```
Input:  s = "MCMXCIV"
Output: 1994   (M + CM + XC + IV)
```

**Constraints**
* `1 <= s.length <= 15`
* `s` is a valid Roman numeral in the range `[1, 3999]`.
''',
approach=r'''
**Look one ahead.** For each symbol, if the next symbol is larger, this one is subtracted; otherwise it is added.

* Time: **O(n)** — one pass over the string.
* Space: **O(1)** — a fixed symbol table.
''',
java=r'''
public class RomanToInteger {

    private static int value(char c) {
        return switch (c) {
            case 'I' -> 1;
            case 'V' -> 5;
            case 'X' -> 10;
            case 'L' -> 50;
            case 'C' -> 100;
            case 'D' -> 500;
            case 'M' -> 1000;
            default -> throw new IllegalArgumentException("Not a Roman symbol: " + c);
        };
    }

    public int romanToInt(String s) {
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            int v = value(s.charAt(i));
            if (i + 1 < s.length() && v < value(s.charAt(i + 1))) {
                total -= v;
            } else {
                total += v;
            }
        }
        return total;
    }
}
''',
test=r'''
class RomanToIntegerTest {

    private final RomanToInteger solution = new RomanToInteger();

    @ParameterizedTest
    @CsvSource({"III,3", "LVIII,58", "MCMXCIV,1994", "IV,4", "MMMCMXCIX,3999"})
    void converts(String roman, int expected) {
        assertEquals(expected, solution.romanToInt(roman));
    }
}
''',
trace=r'''
const V = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
function run(s) {
  let total = 0;
  A.step('Read left to right. A symbol is subtracted when the next symbol is larger; otherwise it is added.', A.chars('s', s), A.vars({ total }));
  for (let i = 0; i < s.length; i++) {
    const v = V[s[i]], nx = i + 1 < s.length ? V[s[i + 1]] : 0;
    if (v < nx) { total -= v; A.step(`${s[i]} (${v}) is followed by the larger ${s[i + 1]} (${nx}), so subtract ${v}. Total is ${total}.`, A.chars('s', s, { hl: { [i]: 'bad', [i + 1]: 'sel' } }), A.vars({ total })); }
    else { total += v; A.step(`${s[i]} (${v}) is not followed by anything larger, so add ${v}. Total is ${total}.`, A.chars('s', s, { hl: { [i]: 'ok' } }), A.vars({ total })); }
  }
  A.step(`${s} equals ${total}.`, A.chars('s', s), A.text('Result', total, 'ok'));
}
A.scenario('With subtractive pairs', 's = "MCMXCIV"', () => run('MCMXCIV'));
A.scenario('Additive only', 's = "LVIII"', () => run('LVIII'));
'''),

P(num=12, slug="integer-to-roman", title="Integer to Roman", diff="Medium", topic="Array / String", cls="IntegerToRoman",
idea="Greedy: repeatedly take the largest value (including the six subtractive pairs) that still fits.",
spec=r'''
Convert an integer `num` (1 to 3999) to a Roman numeral. Use the standard symbols `I, V, X, L, C, D, M` and the
subtractive forms `IV, IX, XL, XC, CD, CM`. `I`, `X`, `C` and `M` may repeat up to three times in a row; `V`, `L` and `D` never repeat.

**Example 1**
```
Input:  num = 3749
Output: "MMMDCCXLIX"
```

**Example 2**
```
Input:  num = 58
Output: "LVIII"
```

**Constraints**
* `1 <= num <= 3999`
''',
approach=r'''
**Greedy table.** Use a table of 13 values in descending order: `1000 M, 900 CM, 500 D, 400 CD, 100 C, 90 XC, 50 L, 40 XL, 10 X, 9 IX, 5 V, 4 IV, 1 I`.
While `num` is at least the current value, append its symbol and subtract.

* Time: **O(1)** — the output is at most 15 symbols, because num ≤ 3999.
* Space: **O(1)** — the fixed table and the output builder.
''',
java=r'''
public class IntegerToRoman {

    private static final int[] VALUES = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    private static final String[] SYMBOLS = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    public String intToRoman(int num) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < VALUES.length && num > 0; i++) {
            while (num >= VALUES[i]) {
                sb.append(SYMBOLS[i]);
                num -= VALUES[i];
            }
        }
        return sb.toString();
    }
}
''',
test=r'''
class IntegerToRomanTest {

    private final IntegerToRoman solution = new IntegerToRoman();

    @ParameterizedTest
    @CsvSource({"3749,MMMDCCXLIX", "58,LVIII", "1994,MCMXCIV", "4,IV", "3999,MMMCMXCIX", "1,I"})
    void converts(int num, String expected) {
        assertEquals(expected, solution.intToRoman(num));
    }
}
''',
trace=r'''
const VAL = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1], SYM = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
function run(num) {
  let out = '';
  A.step(`Convert ${num}. Walk the value table from largest to smallest and take each value as many times as it fits.`, A.arr('values', VAL, { noIdx: true }), A.vars({ num, roman: '""' }));
  for (let i = 0; i < VAL.length && num > 0; i++) {
    if (num < VAL[i]) continue;
    while (num >= VAL[i]) {
      num -= VAL[i]; out += SYM[i];
      A.step(`${VAL[i]} fits, so append ${SYM[i]}. ${num} is left.`, A.arr('values', VAL, { noIdx: true, hl: VAL.map((_, t) => [t, t === i ? 'cur' : t < i ? 'dim' : '']) }), A.chars('roman', out, { hl: { [out.length - 1]: 'ok' } }), A.vars({ num }));
    }
  }
  A.step(`Done: ${out}.`, A.chars('roman', out, { hl: [...out].map((_, t) => [t, 'ok']) }), A.text('Result', out, 'ok'));
}
A.scenario('3749', 'num = 3749', () => run(3749));
A.scenario('1994', 'num = 1994', () => run(1994));
'''),

P(num=58, slug="length-of-last-word", title="Length of Last Word", diff="Easy", topic="Array / String", cls="LengthOfLastWord",
idea="Scan from the end: skip trailing spaces, then count letters until the next space.",
spec=r'''
Given a string `s` of words and spaces, return the length of the **last** word. A word is a maximal run of non-space characters.

**Example 1**
```
Input:  s = "Hello World"
Output: 5
```

**Example 2**
```
Input:  s = "   fly me   to   the moon  "
Output: 4
```

**Constraints**
* `1 <= s.length <= 10^4`
* `s` has only English letters and spaces, and at least one word.
''',
approach=r'''
**Backward scan.** Start at the end, skip spaces, then count characters until a space or the start of the string.

* Time: **O(n)** — at worst we scan the whole string once.
* Space: **O(1)** — an index and a counter.
''',
java=r'''
public class LengthOfLastWord {

    public int lengthOfLastWord(String s) {
        int i = s.length() - 1;
        while (i >= 0 && s.charAt(i) == ' ') {
            i--;
        }
        int length = 0;
        while (i >= 0 && s.charAt(i) != ' ') {
            length++;
            i--;
        }
        return length;
    }
}
''',
test=r'''
class LengthOfLastWordTest {

    private final LengthOfLastWord solution = new LengthOfLastWord();

    @Test
    void simple() {
        assertEquals(5, solution.lengthOfLastWord("Hello World"));
    }

    @Test
    void trailingSpaces() {
        assertEquals(4, solution.lengthOfLastWord("   fly me   to   the moon  "));
    }

    @Test
    void singleWord() {
        assertEquals(5, solution.lengthOfLastWord("luffy"));
    }
}
''',
trace=r'''
function run(s) {
  let i = s.length - 1, len = 0;
  const shown = [...s].map(c => (c === ' ' ? '␣' : c));
  A.step('Start at the last character and walk backwards.', A.arr('s', shown, { ptr: [[i, 'i']] }), A.vars({ length: len }));
  while (i >= 0 && s[i] === ' ') { A.step(`Index ${i} is a trailing space, so skip it.`, A.arr('s', shown, { ptr: [[i, 'i']], hl: { [i]: 'dim' } }), A.vars({ length: len })); i--; }
  const hl = [];
  while (i >= 0 && s[i] !== ' ') { len++; hl.push([i, 'ok']); A.step(`'${s[i]}' is a letter of the last word. Length is now ${len}.`, A.arr('s', shown, { ptr: [[i, 'i']], hl: hl.slice() }), A.vars({ length: len })); i--; }
  A.step(i >= 0 ? `Index ${i} is a space, so the last word has ended. Its length is ${len}.` : `We reached the start of the string. The last word has length ${len}.`, A.arr('s', shown, { hl }), A.text('Result', len, 'ok'));
}
A.scenario('Trailing spaces', 's = "fly to the moon  "', () => run('fly to the moon  '));
A.scenario('Simple', 's = "Hello World"', () => run('Hello World'));
'''),

P(num=14, slug="longest-common-prefix", title="Longest Common Prefix", diff="Easy", topic="Array / String", cls="LongestCommonPrefix",
idea="Compare column by column: the prefix grows until some string ends or differs in that column.",
spec=r'''
Return the longest common prefix shared by all strings in `strs`, or `""` if there is none.

**Example 1**
```
Input:  strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2**
```
Input:  strs = ["dog","racecar","car"]
Output: ""
```

**Constraints**
* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`, lowercase English letters
''',
approach=r'''
**Vertical scan.** For column `c = 0, 1, …`, check that every string has a character at `c` equal to `strs[0].charAt(c)`.
Stop at the first mismatch or end of a string; the prefix is `strs[0].substring(0, c)`.

* Time: **O(S)** — S is the total number of characters; each is compared at most once.
* Space: **O(1)** — apart from the returned substring.
''',
java=r'''
public class LongestCommonPrefix {

    public String longestCommonPrefix(String[] strs) {
        String first = strs[0];
        for (int c = 0; c < first.length(); c++) {
            char ch = first.charAt(c);
            for (int i = 1; i < strs.length; i++) {
                if (c >= strs[i].length() || strs[i].charAt(c) != ch) {
                    return first.substring(0, c);
                }
            }
        }
        return first;
    }
}
''',
test=r'''
class LongestCommonPrefixTest {

    private final LongestCommonPrefix solution = new LongestCommonPrefix();

    @Test
    void sharedPrefix() {
        assertEquals("fl", solution.longestCommonPrefix(new String[]{"flower", "flow", "flight"}));
    }

    @Test
    void noPrefix() {
        assertEquals("", solution.longestCommonPrefix(new String[]{"dog", "racecar", "car"}));
    }

    @Test
    void singleString() {
        assertEquals("alone", solution.longestCommonPrefix(new String[]{"alone"}));
    }

    @Test
    void oneIsPrefixOfOther() {
        assertEquals("ab", solution.longestCommonPrefix(new String[]{"abc", "ab"}));
    }
}
''',
trace=r'''
function run(strs) {
  const w = Math.max(...strs.map(s => s.length));
  const m = strs.map(s => [...s.padEnd(w, ' ')].map(c => (c === ' ' ? '' : c)));
  const hl = (c, bad) => { const o = []; strs.forEach((s, r) => { for (let x = 0; x < c; x++) o.push([`${r},${x}`, 'ok']); if (c < w) o.push([`${r},${c}`, bad && bad.includes(r) ? 'bad' : 'cur']); }); return o; };
  A.step('Line the strings up and compare them one column at a time.', A.grid('strings', m), A.vars({ prefix: '""' }));
  for (let c = 0; c < strs[0].length; c++) {
    const ch = strs[0][c], bad = strs.map((s, r) => (c >= s.length || s[c] !== ch ? r : -1)).filter(r => r >= 0);
    if (bad.length) {
      A.step(`Column ${c}: ${c >= strs[bad[0]].length ? `"${strs[bad[0]]}" has already ended` : `"${strs[bad[0]]}" has '${strs[bad[0]][c]}' instead of '${ch}'`}. Stop here.`, A.grid('strings', m, { hl: hl(c, bad) }), A.vars({ prefix: `"${strs[0].slice(0, c)}"` }));
      A.step(`The longest common prefix is "${strs[0].slice(0, c)}".`, A.grid('strings', m, { hl: hl(c, []).filter(([k]) => +k.split(',')[1] < c) }), A.text('Result', `"${strs[0].slice(0, c)}"`, 'ok'));
      return;
    }
    A.step(`Column ${c}: every string has '${ch}'. The prefix grows to "${strs[0].slice(0, c + 1)}".`, A.grid('strings', m, { hl: hl(c) }), A.vars({ prefix: `"${strs[0].slice(0, c + 1)}"` }));
  }
  A.step(`The first string is used up, so it is the prefix: "${strs[0]}".`, A.grid('strings', m), A.text('Result', `"${strs[0]}"`, 'ok'));
}
A.scenario('Shared prefix', 'strs = ["flower","flow","flight"]', () => run(['flower', 'flow', 'flight']));
A.scenario('Edge: no common prefix', 'strs = ["dog","racecar","car"]', () => run(['dog', 'racecar', 'car']));
'''),
]
