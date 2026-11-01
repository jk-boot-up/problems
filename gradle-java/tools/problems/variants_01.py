"""Simpler solution versions (v1, v2, ...) for problems in batches 01-03.
The solution written in the batch file is always the last, most efficient version."""

VARIANTS = {
88: dict(vname="Three pointers from the back", variants=[dict(
name="Copy and sort",
idea="Copy nums2 into the empty tail of nums1, then sort the whole array.",
approach=r'''
**Copy, then sort.** The last `n` slots of `nums1` are free, so copy `nums2` there and call `Arrays.sort`.
Simple and correct, but it ignores that both inputs are already sorted.

* Time: **O((m + n) log(m + n))** — the sort dominates.
* Space: **O(log(m + n))** — the recursion stack of the sort on primitives.
''',
java=r'''
public class MergeSortedArray {

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        System.arraycopy(nums2, 0, nums1, m, n);
        Arrays.sort(nums1);
    }
}
''',
tc="nlogn", sc="log",
trace=r'''
function run(a, m, b) {
  A.step('nums1 has free slots at the end. Copy nums2 into them.', A.arr('nums1', a, { hl: a.map((_, i) => [i, i >= m ? 'dim' : '']) }), A.arr('nums2', b));
  b.forEach((x, j) => { a[m + j] = x; A.step(`Copy ${x} into slot ${m + j}.`, A.arr('nums1', a, { hl: { [m + j]: 'sel' } }), A.arr('nums2', b, { hl: { [j]: 'cur' } })); });
  a.sort((x, y) => x - y);
  A.step('Sort the whole array. The sort does not use the fact that both halves were already sorted, so it costs O(n log n).', A.arr('nums1', a, { hl: a.map((_, i) => [i, 'ok']) }), A.text('Result', JSON.stringify(a), 'ok'));
}
A.scenario('Interleaved values', 'nums1 = [1,2,3,_,_,_], nums2 = [2,5,6]', () => run([1, 2, 3, 0, 0, 0], 3, [2, 5, 6]));
''')]),

169: dict(vname="Boyer–Moore voting", variants=[dict(
name="Hash map counting",
idea="Count every value in a hash map; return the first one whose count passes n / 2.",
approach=r'''
**Count occurrences.** Increment `count[x]` for each value; as soon as a count exceeds `n / 2`, that value is the answer.

* Time: **O(n)** — one pass with O(1) map updates.
* Space: **O(n)** — up to n distinct keys in the map.
''',
java=r'''
public class MajorityElement {

    public int majorityElement(int[] nums) {
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int x : nums) {
            if (count.merge(x, 1, Integer::sum) > nums.length / 2) {
                return x;
            }
        }
        throw new IllegalArgumentException("No majority element");
    }
}
''',
trace=r'''
function run(a) {
  const c = new Map();
  A.step(`Count each value. The majority must appear more than ${Math.floor(a.length / 2)} times.`, A.arr('nums', a), A.hashTable('count', c));
  for (let i = 0; i < a.length; i++) {
    c.set(a[i], (c.get(a[i]) || 0) + 1);
    const done = c.get(a[i]) > a.length / 2;
    A.step(`${a[i]} has now been seen ${c.get(a[i])} time${c.get(a[i]) > 1 ? 's' : ''}.${done ? ' That is more than half, so it is the answer.' : ''}`, A.arr('nums', a, { hl: { [i]: done ? 'ok' : 'cur' } }), A.hashTable('count', c));
    if (done) { A.step(`The majority element is ${a[i]}.`, A.text('Result', a[i], 'ok')); return; }
  }
}
A.scenario('Majority spread out', 'nums = [2,2,1,1,1,2,2]', () => run([2, 2, 1, 1, 1, 2, 2]));
'''), dict(
name="Sort and take the middle",
idea="After sorting, the majority value always covers the middle index.",
approach=r'''
**Sort.** A value that fills more than half of the array must cover index `n / 2` once sorted.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's recursion stack.
''',
java=r'''
public class MajorityElement {

    public int majorityElement(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        return sorted[sorted.length / 2];
    }
}
''',
tc="nlogn", sc="log",
trace=r'''
function run(a) {
  const s = a.slice().sort((x, y) => x - y), mid = Math.floor(s.length / 2);
  A.step('Sort the values. Equal values end up next to each other.', A.arr('nums', a), A.arr('sorted', s));
  A.step(`The majority fills more than half of the array, so whatever its position, it covers the middle index ${mid}.`, A.arr('sorted', s, { ptr: [[mid, 'mid']], hl: s.map((v, i) => [i, v === s[mid] ? 'sel' : 'dim']).concat([[mid, 'ok']]) }));
  A.step(`The majority element is ${s[mid]}.`, A.text('Result', s[mid], 'ok'));
}
A.scenario('Majority spread out', 'nums = [2,2,1,1,1,2,2]', () => run([2, 2, 1, 1, 1, 2, 2]));
A.scenario('Majority is small', 'nums = [1,3,1,1,2]', () => run([1, 3, 1, 1, 2]));
''')]),

189: dict(vname="Triple reversal", variants=[dict(
name="Extra array",
idea="Write each value straight to its final index (i + k) % n in a copy, then copy back.",
approach=r'''
**Copy to the target positions.** Value at `i` belongs at `(i + k) % n`. Fill a new array, then copy it back into `nums`.

* Time: **O(n)** — two linear passes.
* Space: **O(n)** — the temporary array.
''',
java=r'''
public class RotateArray {

    public void rotate(int[] nums, int k) {
        int n = nums.length;
        int[] rotated = new int[n];
        for (int i = 0; i < n; i++) {
            rotated[(i + k) % n] = nums[i];
        }
        System.arraycopy(rotated, 0, nums, 0, n);
    }
}
''',
trace=r'''
function run(a, k) {
  const n = a.length, out = new Array(n).fill('');
  A.step(`Each value at index i moves to index (i + ${k}) mod ${n}. Build the result in a separate array.`, A.arr('nums', a), A.arr('rotated', out));
  a.forEach((x, i) => { out[(i + k) % n] = x; A.step(`nums[${i}] = ${x} goes to index (${i} + ${k}) mod ${n} = ${(i + k) % n}.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.arr('rotated', out, { hl: { [(i + k) % n]: 'ok' } })); });
  A.step('Copy the result back into nums. It works, but needs a second array of size n.', A.arr('nums', out, { hl: out.map((_, i) => [i, 'ok']) }), A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Rotate by 3', 'nums = [1..7], k = 3', () => run([1, 2, 3, 4, 5, 6, 7], 3));
''')]),

121: dict(vname="One pass, running minimum", variants=[dict(
name="Brute force",
idea="Try every buy day with every later sell day and keep the best difference.",
approach=r'''
**All pairs.** For every `i < j`, compute `prices[j] - prices[i]` and keep the maximum.

* Time: **O(n²)** — about n²/2 pairs.
* Space: **O(1)** — a running best.
''',
java=r'''
public class BestTimeToBuyAndSellStock {

    public int maxProfit(int[] prices) {
        int best = 0;
        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                best = Math.max(best, prices[j] - prices[i]);
            }
        }
        return best;
    }
}
''',
trace=r'''
function run(p) {
  let best = 0, pairs = 0;
  A.step('Try every buy day i with every later sell day j.', A.arr('prices', p), A.vars({ best, pairsChecked: pairs }));
  for (let i = 0; i < p.length; i++) for (let j = i + 1; j < p.length; j++) {
    pairs++;
    const pr = p[j] - p[i], nb = pr > best;
    if (nb) best = pr;
    A.step(`Buy at ${p[i]}, sell at ${p[j]}: profit ${pr}.${nb ? ' New best.' : ''}`, A.arr('prices', p, { ptr: [[i, 'buy'], [j, 'sell']], hl: { [i]: 'sel', [j]: nb ? 'ok' : 'cur' } }), A.vars({ best, pairsChecked: pairs }));
  }
  A.step(`Checked ${pairs} pairs. That count grows with the square of the number of days. The best profit is ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Small market', 'prices = [7,1,5,3,6]', () => run([7, 1, 5, 3, 6]));
''')]),

45: dict(vname="Greedy windows", variants=[dict(
name="Dynamic programming",
idea="jumps[i] = fewest jumps to reach i; relax every index reachable from i.",
approach=r'''
**DP over positions.** `dp[0] = 0`, every other entry starts at infinity. For each `i`, for each `j` in `i+1 … i+nums[i]`,
set `dp[j] = min(dp[j], dp[i] + 1)`.

* Time: **O(n²)** — each index may relax up to n later indices.
* Space: **O(n)** — the dp array.
''',
java=r'''
public class JumpGameII {

    public int jump(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= Math.min(n - 1, i + nums[i]); j++) {
                dp[j] = Math.min(dp[j], dp[i] + 1);
            }
        }
        return dp[n - 1];
    }
}
''',
trace=r'''
function run(a) {
  const n = a.length, dp = new Array(n).fill('∞');
  dp[0] = 0;
  A.step('dp[i] is the fewest jumps needed to reach index i. Index 0 needs none.', A.arr('nums', a), A.arr('dp', dp, { hl: { 0: 'ok' } }));
  for (let i = 0; i < n; i++) {
    const upd = [];
    for (let j = i + 1; j <= Math.min(n - 1, i + a[i]); j++) if (dp[j] === '∞' || dp[i] + 1 < dp[j]) { dp[j] = dp[i] + 1; upd.push([j, 'ok']); }
    if (i + a[i] > i) A.step(`From index ${i} (${dp[i]} jumps) we reach indices ${i + 1} to ${Math.min(n - 1, i + a[i])} in ${dp[i] + 1} jumps.${upd.length ? '' : ' Nothing improves.'}`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.arr('dp', dp, { hl: upd.concat([[i, 'cur']]) }));
  }
  A.step(`dp[${n - 1}] = ${dp[n - 1]}.`, A.arr('dp', dp, { hl: { [n - 1]: 'ok' } }), A.text('Result', dp[n - 1], 'ok'));
}
A.scenario('Two jumps', 'nums = [2,3,1,1,4]', () => run([2, 3, 1, 1, 4]));
''')]),

274: dict(vname="Counting buckets", variants=[dict(
name="Sort descending",
idea="Sort citations high to low; h grows while the (h+1)-th paper still has more than h citations.",
approach=r'''
**Sort.** Sort ascending and scan from the top: the paper at rank `h + 1` (counting from the most cited) must have at least
`h + 1` citations for the h-index to reach `h + 1`.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's recursion stack.
''',
java=r'''
public class HIndex {

    public int hIndex(int[] citations) {
        int[] c = citations.clone();
        Arrays.sort(c);
        int n = c.length, h = 0;
        while (h < n && c[n - 1 - h] > h) {
            h++;
        }
        return h;
    }
}
''',
tc="nlogn", sc="log",
trace=r'''
function run(c) {
  const s = c.slice().sort((x, y) => y - x);
  let h = 0;
  A.step('Sort the citations from most to least cited.', A.arr('citations', c), A.arr('sorted (desc)', s));
  while (h < s.length && s[h] > h) { A.step(`Paper #${h + 1} has ${s[h]} citations, at least ${h + 1}. So h can be ${h + 1}.`, A.arr('sorted (desc)', s, { hl: s.map((_, t) => [t, t <= h ? 'ok' : '']) }), A.vars({ h: h + 1 })); h++; }
  A.step(h < s.length ? `Paper #${h + 1} has only ${s[h]} citations, fewer than ${h + 1}. Stop: the h-index is ${h}.` : `Every paper qualifies, so the h-index is ${h}.`, A.arr('sorted (desc)', s, { hl: s.map((_, t) => [t, t < h ? 'ok' : 'bad']) }), A.text('Result', h, 'ok'));
}
A.scenario('Mixed citations', 'citations = [3,0,6,1,5]', () => run([3, 0, 6, 1, 5]));
''')]),

238: dict(vname="Output array + running suffix", variants=[dict(
name="Prefix and suffix arrays",
idea="Precompute products to the left and to the right of every index, then multiply them.",
approach=r'''
**Two helper arrays.** `left[i]` = product of `nums[0..i-1]`, `right[i]` = product of `nums[i+1..n-1]`;
`answer[i] = left[i] * right[i]`.

* Time: **O(n)** — three linear passes.
* Space: **O(n)** — two extra arrays besides the output.
''',
java=r'''
public class ProductExceptSelf {

    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] left = new int[n], right = new int[n], answer = new int[n];
        left[0] = 1;
        for (int i = 1; i < n; i++) left[i] = left[i - 1] * nums[i - 1];
        right[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) right[i] = right[i + 1] * nums[i + 1];
        for (int i = 0; i < n; i++) answer[i] = left[i] * right[i];
        return answer;
    }
}
''',
trace=r'''
function run(a) {
  const n = a.length, L = new Array(n).fill(''), R = new Array(n).fill(''), ans = new Array(n).fill('');
  L[0] = 1;
  for (let i = 1; i < n; i++) L[i] = L[i - 1] * a[i - 1];
  A.step('left[i] is the product of everything before i.', A.arr('nums', a), A.arr('left', L, { hl: L.map((_, i) => [i, 'sel']) }));
  R[n - 1] = 1;
  for (let i = n - 2; i >= 0; i--) R[i] = R[i + 1] * a[i + 1];
  A.step('right[i] is the product of everything after i.', A.arr('nums', a), A.arr('left', L), A.arr('right', R, { hl: R.map((_, i) => [i, 'alt']) }));
  for (let i = 0; i < n; i++) { ans[i] = L[i] * R[i]; A.step(`answer[${i}] = left ${L[i]} × right ${R[i]} = ${ans[i]}.`, A.arr('left', L, { hl: { [i]: 'sel' } }), A.arr('right', R, { hl: { [i]: 'alt' } }), A.arr('answer', ans, { hl: { [i]: 'ok' } })); }
  A.step('Correct, but the two helper arrays cost O(n) extra space. The next version avoids them.', A.text('Result', JSON.stringify(ans), 'ok'));
}
A.scenario('Plain values', 'nums = [1,2,3,4]', () => run([1, 2, 3, 4]));
''')]),

134: dict(vname="Greedy single pass", variants=[dict(
name="Simulate every start",
idea="Try each station as the start and drive around until the tank runs dry.",
approach=r'''
**Brute force.** For every start `s`, drive `n` legs, adding `gas` and subtracting `cost`. If the tank never drops below zero,
`s` works.

* Time: **O(n²)** — n starts × up to n legs.
* Space: **O(1)** — a tank counter.
''',
java=r'''
public class GasStation {

    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        for (int start = 0; start < n; start++) {
            int tank = 0, legs = 0;
            while (legs < n) {
                int i = (start + legs) % n;
                tank += gas[i] - cost[i];
                if (tank < 0) break;
                legs++;
            }
            if (legs == n) return start;
        }
        return -1;
    }
}
''',
trace=r'''
function run(gas, cost) {
  const n = gas.length, d = gas.map((g, i) => g - cost[i]);
  A.step('Net fuel per station is gas minus cost. Try each station as the start.', A.arr('gas − cost', d));
  for (let s = 0; s < n; s++) {
    let tank = 0, legs = 0;
    const hl = [];
    while (legs < n) { const i = (s + legs) % n; tank += d[i]; if (tank < 0) { hl.push([i, 'bad']); break; } hl.push([i, 'ok']); legs++; }
    A.step(legs === n ? `Starting at ${s}, the tank never runs dry. Answer: ${s}.` : `Starting at ${s}, the tank runs dry after ${legs + 1} leg${legs ? 's' : ''}.`, A.arr('gas − cost', d, { ptr: [[s, 'start']], hl }), A.vars({ start: s, tank }));
    if (legs === n) { A.step(`Station ${s} works, but we may have re-driven many legs to find it: O(n²) in the worst case.`, A.text('Result', s, 'ok')); return; }
  }
  A.step('No start works.', A.text('Result', -1, 'bad'));
}
A.scenario('Start in the middle', 'gas = [1,2,3,4,5], cost = [3,4,5,1,2]', () => run([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]));
''')]),

42: dict(vname="Two pointers", variants=[dict(
name="Prefix / suffix maximum arrays",
idea="Precompute the tallest wall to the left and to the right of every bar.",
approach=r'''
**Precomputed maxima.** `leftMax[i]` = tallest bar in `0..i`, `rightMax[i]` = tallest in `i..n-1`.
Water at `i` = `min(leftMax[i], rightMax[i]) - height[i]`.

* Time: **O(n)** — three linear passes.
* Space: **O(n)** — two arrays of maxima.
''',
java=r'''
public class TrappingRainWater {

    public int trap(int[] height) {
        int n = height.length;
        int[] leftMax = new int[n], rightMax = new int[n];
        for (int i = 0; i < n; i++) leftMax[i] = Math.max(i > 0 ? leftMax[i - 1] : 0, height[i]);
        for (int i = n - 1; i >= 0; i--) rightMax[i] = Math.max(i < n - 1 ? rightMax[i + 1] : 0, height[i]);
        int water = 0;
        for (int i = 0; i < n; i++) water += Math.min(leftMax[i], rightMax[i]) - height[i];
        return water;
    }
}
''',
trace=r'''
function run(h) {
  const n = h.length, L = [], R = new Array(n);
  h.forEach((v, i) => (L[i] = Math.max(i ? L[i - 1] : 0, v)));
  A.step('leftMax[i]: the tallest bar from the left edge up to i.', A.arr('height', h), A.arr('leftMax', L, { hl: L.map((_, i) => [i, 'sel']) }));
  for (let i = n - 1; i >= 0; i--) R[i] = Math.max(i < n - 1 ? R[i + 1] : 0, h[i]);
  A.step('rightMax[i]: the tallest bar from i to the right edge.', A.arr('height', h), A.arr('leftMax', L), A.arr('rightMax', R, { hl: R.map((_, i) => [i, 'alt']) }));
  let water = 0; const W = [];
  for (let i = 0; i < n; i++) { const w = Math.min(L[i], R[i]) - h[i]; W.push(w); water += w; A.step(`Index ${i}: min(${L[i]}, ${R[i]}) − ${h[i]} = ${w}. Total ${water}.`, A.arr('height', h, { hl: { [i]: 'cur' } }), A.arr('water', W, { hl: { [i]: w ? 'sel' : 'dim' } }), A.vars({ water })); }
  A.step(`Total trapped water: ${water}. The two helper arrays cost O(n) space.`, A.text('Result', water, 'ok'));
}
A.scenario('Basin', 'height = [4,2,0,3,2,5]', () => run([4, 2, 0, 3, 2, 5]));
''')]),

151: dict(vname="Manual right-to-left scan", variants=[dict(
name="Split, reverse, join",
idea="Let the library split on runs of spaces, reverse the list, and join with single spaces.",
approach=r'''
**Library calls.** `s.trim().split("\\s+")` gives the words; reverse the list; `String.join(" ", words)`.
Short and clear, though it allocates an intermediate array.

* Time: **O(n)** — splitting, reversing and joining are linear.
* Space: **O(n)** — the array of words.
''',
java=r'''
public class ReverseWords {

    public String reverseWords(String s) {
        List<String> words = Arrays.asList(s.trim().split("\\s+"));
        Collections.reverse(words);
        return String.join(" ", words);
    }
}
''',
trace=r'''
function run(s) {
  const words = s.trim().split(/\s+/);
  A.step('Trim the ends and split on runs of spaces.', A.chars('s', [...s].map(c => (c === ' ' ? '␣' : c)).join('')), A.arr('words', words, { hl: words.map((_, i) => [i, 'sel']) }));
  const r = words.slice().reverse();
  A.step('Reverse the list of words.', A.arr('reversed', r, { hl: r.map((_, i) => [i, 'alt']) }));
  A.step(`Join with single spaces: "${r.join(' ')}".`, A.text('Result', `"${r.join(' ')}"`, 'ok'));
}
A.scenario('Extra spaces', 's = "  hello  world "', () => run('  hello  world '));
''')]),

28: dict(vname="KMP", variants=[dict(
name="Brute force",
idea="Try every start position and compare the needle character by character.",
approach=r'''
**Check every alignment.** For each start `i` from 0 to `n - m`, compare `needle` with `haystack[i..i+m-1]`.

* Time: **O(n·m)** — each of about n alignments may compare up to m characters.
* Space: **O(1)** — a couple of indices.
''',
java=r'''
public class StrStr {

    public int strStr(String haystack, String needle) {
        int n = haystack.length(), m = needle.length();
        for (int i = 0; i + m <= n; i++) {
            int j = 0;
            while (j < m && haystack.charAt(i + j) == needle.charAt(j)) {
                j++;
            }
            if (j == m) {
                return i;
            }
        }
        return -1;
    }
}
''',
tc="n2",
trace=r'''
function run(h, nd) {
  let comps = 0;
  for (let i = 0; i + nd.length <= h.length; i++) {
    let j = 0;
    while (j < nd.length && h[i + j] === nd[j]) { j++; comps++; }
    if (j < nd.length) comps++;
    const hl = []; for (let t = 0; t < j; t++) hl.push([i + t, 'ok']); if (j < nd.length) hl.push([i + j, 'bad']);
    A.step(j === nd.length ? `Start ${i}: all ${nd.length} characters match.` : `Start ${i}: mismatch after ${j} matching character${j === 1 ? '' : 's'}. Slide the needle by one.`, A.chars('haystack', h, { hl, ptr: [[i, 'start']] }), A.chars('needle', nd), A.vars({ comparisons: comps }));
    if (j === nd.length) { A.step(`The needle starts at ${i}. That took ${comps} character comparisons; KMP avoids re-checking characters.`, A.text('Result', i, 'ok')); return; }
  }
  A.step('No alignment matches.', A.text('Result', -1, 'bad'));
}
A.scenario('Repeated letters', 'haystack = "aaaab", needle = "aab"', () => run('aaaab', 'aab'));
''')]),

167: dict(vname="Two pointers", variants=[dict(
name="Binary search for the partner",
idea="For each value, binary-search the rest of the sorted array for target minus that value.",
approach=r'''
**Binary search.** For every `i`, search `numbers[i+1..n-1]` for `target - numbers[i]`.

* Time: **O(n log n)** — n binary searches.
* Space: **O(1)** — a few indices.
''',
java=r'''
public class TwoSumII {

    public int[] twoSum(int[] numbers, int target) {
        for (int i = 0; i < numbers.length; i++) {
            int want = target - numbers[i], lo = i + 1, hi = numbers.length - 1;
            while (lo <= hi) {
                int mid = (lo + hi) >>> 1;
                if (numbers[mid] == want) return new int[]{i + 1, mid + 1};
                if (numbers[mid] < want) lo = mid + 1; else hi = mid - 1;
            }
        }
        throw new IllegalArgumentException("No solution");
    }
}
''',
trace=r'''
function run(a, target) {
  for (let i = 0; i < a.length; i++) {
    const want = target - a[i];
    let lo = i + 1, hi = a.length - 1;
    A.step(`Fix ${a[i]}. Its partner must be ${want}. Binary-search indices ${lo} to ${hi}.`, A.arr('numbers', a, { range: [lo, hi], hl: { [i]: 'alt' } }), A.vars({ target, want }));
    while (lo <= hi) {
      const mid = (lo + hi) >> 1;
      if (a[mid] === want) { A.step(`numbers[${mid}] = ${want}. Found the pair: [${i + 1}, ${mid + 1}].`, A.arr('numbers', a, { hl: { [i]: 'ok', [mid]: 'ok' } }), A.text('Result', `[${i + 1}, ${mid + 1}]`, 'ok')); return; }
      A.step(`numbers[${mid}] = ${a[mid]} is ${a[mid] < want ? 'too small, so search right' : 'too big, so search left'}.`, A.arr('numbers', a, { range: [lo, hi], ptr: [[mid, 'mid']], hl: { [i]: 'alt', [mid]: 'cur' } }), A.vars({ target, want }));
      if (a[mid] < want) lo = mid + 1; else hi = mid - 1;
    }
  }
}
A.scenario('Pair in the middle', 'numbers = [1,3,4,6,8,11], target = 10', () => run([1, 3, 4, 6, 8, 11], 10));
''')]),

11: dict(vname="Two pointers", variants=[dict(
name="Brute force",
idea="Measure every pair of lines.",
approach=r'''
**All pairs.** For every `i < j`, the area is `min(h[i], h[j]) * (j - i)`; keep the maximum.

* Time: **O(n²)** — about n²/2 pairs.
* Space: **O(1)** — the best area.
''',
java=r'''
public class ContainerWithMostWater {

    public int maxArea(int[] height) {
        int best = 0;
        for (int i = 0; i < height.length; i++) {
            for (int j = i + 1; j < height.length; j++) {
                best = Math.max(best, Math.min(height[i], height[j]) * (j - i));
            }
        }
        return best;
    }
}
''',
trace=r'''
function run(h) {
  let best = 0, pairs = 0;
  A.step('Measure every pair of lines.', A.arr('height', h), A.vars({ best }));
  for (let i = 0; i < h.length; i++) for (let j = i + 1; j < h.length; j++) {
    pairs++;
    const area = Math.min(h[i], h[j]) * (j - i), nb = area > best;
    if (nb) best = area;
    A.step(`Lines ${i} and ${j}: min(${h[i]}, ${h[j]}) × ${j - i} = ${area}.${nb ? ' New best.' : ''}`, A.arr('height', h, { range: [i, j], hl: { [i]: 'cur', [j]: nb ? 'ok' : 'cur' } }), A.vars({ best, pairsChecked: pairs }));
  }
  A.step(`Best area ${best} after ${pairs} pairs; the pair count grows quadratically.`, A.text('Result', best, 'ok'));
}
A.scenario('Small input', 'height = [1,8,6,2,7]', () => run([1, 8, 6, 2, 7]));
''')]),

15: dict(vname="Sort + two pointers", variants=[dict(
name="Hash set per fixed number",
idea="Fix nums[i]; scan the rest with a hash set looking for the value that completes the triplet.",
approach=r'''
**Hashing.** Sort (so triplets come out in a canonical order), then for each `i` scan `j > i` with a set of seen values:
if `-(nums[i] + nums[j])` was seen, record the triplet. A `Set<List<Integer>>` removes duplicates.

* Time: **O(n²)** — n fixed values × a linear scan.
* Space: **O(n)** — the seen set (plus the output).
''',
java=r'''
public class ThreeSum {

    public List<List<Integer>> threeSum(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        MyHashSet<List<Integer>> found = new MyHashSet<>();
        for (int i = 0; i < a.length - 2; i++) {
            MyHashSet<Integer> seen = new MyHashSet<>();
            for (int j = i + 1; j < a.length; j++) {
                int need = -a[i] - a[j];
                if (seen.contains(need)) {
                    found.add(List.of(a[i], need, a[j]));
                }
                seen.add(a[j]);
            }
        }
        List<List<Integer>> out = new ArrayList<>();
        for (List<Integer> triplet : found) out.add(triplet);
        return out;
    }
}
''',
trace=r'''
function run(orig) {
  const a = orig.slice().sort((x, y) => x - y), found = new Set();
  A.step('Sort, then for each fixed value scan the rest with a set of values seen so far.', A.arr('sorted', a));
  for (let i = 0; i < a.length - 2; i++) {
    const seen = new Set();
    for (let j = i + 1; j < a.length; j++) {
      const need = -a[i] - a[j], hit = seen.has(need);
      if (hit) found.add(`[${a[i]},${need},${a[j]}]`);
      A.step(`Fixed ${a[i]}, current ${a[j]}: we need ${need}. ${hit ? 'It was seen, so record the triplet.' : 'Not seen yet.'}`, A.arr('sorted', a, { hl: { [i]: 'alt', [j]: hit ? 'ok' : 'cur' } }), A.hashTable('seen', seen), A.arr('triplets', [...found]));
      seen.add(a[j]);
    }
  }
  A.step(`The set removed duplicates. ${found.size} unique triplet${found.size === 1 ? '' : 's'}.`, A.arr('triplets', [...found], { hl: [...found].map((_, t) => [t, 'ok']) }));
}
A.scenario('Small input', 'nums = [-1,0,1,2,-1]', () => run([-1, 0, 1, 2, -1]));
''')]),

209: dict(vname="Sliding window", variants=[dict(
name="Prefix sums + binary search",
idea="With prefix sums, for each start binary-search the first end whose window sum reaches the target.",
approach=r'''
**Prefix sums.** `pre[i]` = sum of the first `i` values (increasing, since all values are positive). For each `i`,
binary-search the smallest `j` with `pre[j] - pre[i] >= target`; the window length is `j - i`.

* Time: **O(n log n)** — n binary searches.
* Space: **O(n)** — the prefix-sum array.
''',
java=r'''
public class MinimumSizeSubarraySum {

    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int[] pre = new int[n + 1];
        for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + nums[i];
        int best = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int lo = i + 1, hi = n;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (pre[mid] - pre[i] >= target) hi = mid; else lo = mid + 1;
            }
            if (pre[lo] - pre[i] >= target) best = Math.min(best, lo - i);
        }
        return best == Integer.MAX_VALUE ? 0 : best;
    }
}
''',
trace=r'''
function run(target, a) {
  const n = a.length, pre = [0];
  a.forEach(x => pre.push(pre[pre.length - 1] + x));
  A.step('Build prefix sums: pre[j] − pre[i] is the sum of nums[i..j−1]. They only increase, so we can binary-search them.', A.arr('nums', a), A.arr('pre', pre));
  let best = Infinity;
  for (let i = 0; i < n; i++) {
    let lo = i + 1, hi = n;
    while (lo < hi) { const mid = (lo + hi) >> 1; if (pre[mid] - pre[i] >= target) hi = mid; else lo = mid + 1; }
    const ok = pre[lo] - pre[i] >= target;
    if (ok) best = Math.min(best, lo - i);
    A.step(ok ? `Starting at ${i}, the first end that reaches ${target} is ${lo}, a window of length ${lo - i}.` : `Starting at ${i}, no window reaches ${target}.`, A.arr('pre', pre, { hl: { [i]: 'sel', [lo]: ok ? 'ok' : 'bad' } }), A.arr('nums', a, { range: ok ? [i, lo - 1] : [i, n - 1] }), A.vars({ best: best === Infinity ? '∞' : best }));
  }
  A.step(`Minimal length: ${best === Infinity ? 0 : best}.`, A.text('Result', best === Infinity ? 0 : best, 'ok'));
}
A.scenario('Classic', 'target = 7, nums = [2,3,1,2,4,3]', () => run(7, [2, 3, 1, 2, 4, 3]));
''')]),
}
