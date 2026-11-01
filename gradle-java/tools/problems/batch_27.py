PROBLEMS = [
P(num=1004, slug="max-consecutive-ones-iii", title="Max Consecutive Ones III", diff="Medium", topic="Sliding Window", cls="MaxConsecutiveOnesIII",
idea="Keep a window with at most k zeros (the zeros you would flip); shrink from the left when it has too many.",
vname="Sliding window with a zero budget",
spec=r'''
Given a binary array and an integer `k`, return the longest run of `1`s you can get by flipping at most `k` zeros.

**Example**
```
nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 → 6
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3 → 10
```

**Constraints**
* `1 <= nums.length <= 10^5`; `0 <= k <= nums.length`
''',
approach=r'''
**Window with ≤ k zeros.** Extend the right edge; count zeros inside. While the count exceeds `k`, move the left edge past a zero. The window
length is a candidate answer.

* Time: **O(n)** — each index enters and leaves once.
* Space: **O(1)** — a counter.
''',
java=r'''
public class MaxConsecutiveOnesIII {

    public int longestOnes(int[] nums, int k) {
        int left = 0, zeros = 0, best = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > k) {
                if (nums[left++] == 0) zeros--;
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
''',
test=r'''
class MaxConsecutiveOnesIIITest {

    private final MaxConsecutiveOnesIII solution = new MaxConsecutiveOnesIII();

    @Test
    void examples() {
        assertEquals(6, solution.longestOnes(new int[]{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0}, 2));
        assertEquals(10, solution.longestOnes(new int[]{0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1}, 3));
        assertEquals(0, solution.longestOnes(new int[]{0, 0}, 0));
    }
}
''',
trace=r'''
function run(a, k) {
  let left = 0, zeros = 0, best = 0;
  A.step(`The window may hold at most ${k} zeros: those are the ones we would flip.`, A.arr('nums', a), A.vars({ zeros, best }));
  for (let r = 0; r < a.length; r++) {
    if (!a[r]) zeros++;
    let shrank = false;
    while (zeros > k) { if (!a[left++]) zeros--; shrank = true; }
    best = Math.max(best, r - left + 1);
    A.step(`Add ${a[r]}.${shrank ? ` Too many zeros: move the left edge to ${left}.` : ''} Window length ${r - left + 1}, best ${best}.`, A.arr('nums', a, { range: [left, r], hl: Object.fromEntries(a.map((v, i) => [i, i >= left && i <= r && !v ? 'alt' : ''])) }), A.vars({ zeros, best }));
  }
  A.step(`Longest run after flipping: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('k = 2', 'nums = [1,1,1,0,0,0,1,1,1,1,0]', () => run([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2));
'''),

P(num=1493, slug="longest-subarray-of-1s-after-deleting-one-element", title="Longest Subarray of 1's After Deleting One Element", diff="Medium", topic="Sliding Window", cls="LongestSubarrayAfterDeleting",
idea="A window with at most one zero; its length minus one (the deleted element) is a candidate.",
vname="Sliding window with one zero",
spec=r'''
Delete exactly one element from a binary array. Return the length of the longest non-empty subarray of only `1`s in the result (0 if none).

**Example**
```
[1,1,0,1] → 3,   [0,1,1,1,0,1,1,0,1] → 5,   [1,1,1] → 2
```

**Constraints**
* `1 <= nums.length <= 10^5`
''',
approach=r'''
**At most one zero.** Same as Max Consecutive Ones III with `k = 1`, but one element must be deleted, so the answer is the window length
minus 1 (this also covers an all-ones array).

* Time: **O(n)** — one pass.
* Space: **O(1)** — a counter.
''',
java=r'''
public class LongestSubarrayAfterDeleting {

    public int longestSubarray(int[] nums) {
        int left = 0, zeros = 0, best = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > 1) {
                if (nums[left++] == 0) zeros--;
            }
            best = Math.max(best, right - left);
        }
        return best;
    }
}
''',
test=r'''
class LongestSubarrayAfterDeletingTest {

    private final LongestSubarrayAfterDeleting solution = new LongestSubarrayAfterDeleting();

    @Test
    void examples() {
        assertEquals(3, solution.longestSubarray(new int[]{1, 1, 0, 1}));
        assertEquals(5, solution.longestSubarray(new int[]{0, 1, 1, 1, 0, 1, 1, 0, 1}));
        assertEquals(2, solution.longestSubarray(new int[]{1, 1, 1}));
    }
}
''',
trace=r'''
function run(a) {
  let left = 0, zeros = 0, best = 0;
  for (let r = 0; r < a.length; r++) {
    if (!a[r]) zeros++;
    while (zeros > 1) { if (!a[left++]) zeros--; }
    best = Math.max(best, r - left);
    A.step(`Window ${left}..${r} has ${zeros} zero${zeros === 1 ? '' : 's'}; deleting one element leaves ${r - left} ones. Best ${best}.`, A.arr('nums', a, { range: [left, r], hl: Object.fromEntries(a.map((v, i) => [i, i >= left && i <= r && !v ? 'bad' : ''])) }), A.vars({ best }));
  }
  A.step(`Answer: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', 'nums = [0,1,1,1,0,1,1,0,1]', () => run([0, 1, 1, 1, 0, 1, 1, 0, 1]));
'''),

P(num=1732, slug="find-the-highest-altitude", title="Find the Highest Altitude", diff="Easy", topic="Prefix Sum", cls="HighestAltitude",
idea="Altitudes are running sums of the gains; return the largest running sum (starting at 0).",
vname="Running sum",
spec=r'''
A biker starts at altitude 0; `gain[i]` is the change from point `i` to point `i + 1`. Return the highest altitude reached.

**Example**
```
[-5,1,5,0,-7] → 1,   [-4,-3,-2,-1,4,3,2] → 0
```

**Constraints**
* `1 <= n <= 100`
''',
approach=r'''
**Prefix sum.** Track the running altitude and its maximum, starting from 0.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two numbers.
''',
java=r'''
public class HighestAltitude {

    public int largestAltitude(int[] gain) {
        int altitude = 0, best = 0;
        for (int g : gain) {
            altitude += g;
            best = Math.max(best, altitude);
        }
        return best;
    }
}
''',
test=r'''
class HighestAltitudeTest {

    private final HighestAltitude solution = new HighestAltitude();

    @Test
    void examples() {
        assertEquals(1, solution.largestAltitude(new int[]{-5, 1, 5, 0, -7}));
        assertEquals(0, solution.largestAltitude(new int[]{-4, -3, -2, -1, 4, 3, 2}));
    }
}
''',
trace=r'''
function run(g) {
  const alt = [0];
  g.forEach((x, i) => { alt.push(alt[i] + x); A.step(`Gain ${x}: altitude ${alt[i + 1]}.`, A.arr('gain', g, { hl: { [i]: 'cur' } }), A.arr('altitude', alt, { hl: { [i + 1]: 'ok' } })); });
  A.step(`Highest altitude: ${Math.max(...alt)}.`, A.arr('altitude', alt, { hl: { [alt.indexOf(Math.max(...alt))]: 'ok' } }), A.text('Result', Math.max(...alt), 'ok'));
}
A.scenario('Classic', 'gain = [-5,1,5,0,-7]', () => run([-5, 1, 5, 0, -7]));
'''),

P(num=724, slug="find-pivot-index", title="Find Pivot Index", diff="Easy", topic="Prefix Sum", cls="FindPivotIndex",
idea="The pivot is where the sum to its left equals total − left − nums[i].",
vname="Total minus running left sum",
spec=r'''
Return the leftmost index where the sum of the elements to its left equals the sum of the elements to its right (an empty side sums to 0),
or `-1`.

**Example**
```
[1,7,3,6,5,6] → 3,   [1,2,3] → -1,   [2,1,-1] → 0
```

**Constraints**
* `1 <= nums.length <= 10^4`
''',
approach=r'''
**One total, one running sum.** The right side's sum is `total - left - nums[i]`; check it equals `left`, then add `nums[i]` to `left`.

* Time: **O(n)** — two passes.
* Space: **O(1)** — two sums.
''',
java=r'''
public class FindPivotIndex {

    public int pivotIndex(int[] nums) {
        int total = 0, left = 0;
        for (int x : nums) total += x;
        for (int i = 0; i < nums.length; i++) {
            if (left == total - left - nums[i]) return i;
            left += nums[i];
        }
        return -1;
    }
}
''',
test=r'''
class FindPivotIndexTest {

    private final FindPivotIndex solution = new FindPivotIndex();

    @Test
    void examples() {
        assertEquals(3, solution.pivotIndex(new int[]{1, 7, 3, 6, 5, 6}));
        assertEquals(-1, solution.pivotIndex(new int[]{1, 2, 3}));
        assertEquals(0, solution.pivotIndex(new int[]{2, 1, -1}));
    }
}
''',
trace=r'''
function run(a) {
  const total = a.reduce((s, x) => s + x, 0); let left = 0;
  A.step(`The total is ${total}. At each index, right = total − left − nums[i].`, A.arr('nums', a), A.vars({ total }));
  for (let i = 0; i < a.length; i++) {
    const right = total - left - a[i];
    if (left === right) { A.step(`Index ${i}: left ${left} = right ${right}. Pivot found.`, A.arr('nums', a, { hl: { [i]: 'ok', ...Object.fromEntries(a.map((_, t) => [t, t < i ? 'sel' : t > i ? 'alt' : 'ok'])) } }), A.text('Result', i, 'ok')); return; }
    A.step(`Index ${i}: left ${left}, right ${right}. Not equal.`, A.arr('nums', a, { hl: Object.fromEntries(a.map((_, t) => [t, t < i ? 'sel' : t > i ? 'alt' : 'cur'])) }), A.vars({ left, right }));
    left += a[i];
  }
  A.step('No pivot.', A.text('Result', -1, 'bad'));
}
A.scenario('Classic', 'nums = [1,7,3,6,5,6]', () => run([1, 7, 3, 6, 5, 6]));
'''),

P(num=2215, slug="find-the-difference-of-two-arrays", title="Find the Difference of Two Arrays", diff="Easy", topic="Arrays & Hashing", cls="DifferenceOfTwoArrays",
idea="Put each array in a hash set; keep the distinct values missing from the other set.",
vname="Two hash sets",
spec=r'''
Return `[a, b]` where `a` holds the distinct values of `nums1` not in `nums2`, and `b` the distinct values of `nums2` not in `nums1`
(any order).

**Example**
```
nums1 = [1,2,3], nums2 = [2,4,6] → [[1,3],[4,6]]
```

**Constraints**
* `1 <= nums1.length, nums2.length <= 1000`
''',
approach=r'''
**Sets.** Build `MyHashSet`s of both arrays, then collect each set's values that the other lacks.

* Time: **O(m + n)** — linear set operations.
* Space: **O(m + n)** — the sets.
''',
java=r'''
public class DifferenceOfTwoArrays {

    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        MyHashSet<Integer> a = new MyHashSet<>(), b = new MyHashSet<>();
        for (int x : nums1) a.add(x);
        for (int x : nums2) b.add(x);
        List<Integer> onlyA = new ArrayList<>(), onlyB = new ArrayList<>();
        for (int x : a) if (!b.contains(x)) onlyA.add(x);
        for (int x : b) if (!a.contains(x)) onlyB.add(x);
        return List.of(onlyA, onlyB);
    }
}
''',
test=r'''
class DifferenceOfTwoArraysTest {

    private final DifferenceOfTwoArrays solution = new DifferenceOfTwoArrays();

    @Test
    void examples() {
        List<List<Integer>> r = solution.findDifference(new int[]{1, 2, 3}, new int[]{2, 4, 6});
        assertEquals(Set.of(1, 3), new HashSet<>(r.get(0)));
        assertEquals(Set.of(4, 6), new HashSet<>(r.get(1)));
        List<List<Integer>> s = solution.findDifference(new int[]{1, 2, 3, 3}, new int[]{1, 1, 2, 2});
        assertEquals(List.of(3), s.get(0));
        assertEquals(List.of(), s.get(1));
    }
}
''',
trace=r'''
function run(x, y) {
  const a = new Set(x), b = new Set(y);
  A.step('Put both arrays into hash sets (duplicates collapse).', A.hashTable('set 1', a), A.hashTable('set 2', b));
  const oa = [...a].filter(v => !b.has(v)), ob = [...b].filter(v => !a.has(v));
  A.step(`Values only in nums1: [${oa}]. Values only in nums2: [${ob}].`, A.arr('nums1', x, { hl: Object.fromEntries(x.map((v, i) => [i, b.has(v) ? 'dim' : 'ok'])) }), A.arr('nums2', y, { hl: Object.fromEntries(y.map((v, i) => [i, a.has(v) ? 'dim' : 'ok'])) }), A.text('Result', JSON.stringify([oa, ob]), 'ok'));
}
A.scenario('Classic', 'nums1 = [1,2,3], nums2 = [2,4,6]', () => run([1, 2, 3], [2, 4, 6]));
'''),

P(num=1207, slug="unique-number-of-occurrences", title="Unique Number of Occurrences", diff="Easy", topic="Arrays & Hashing", cls="UniqueOccurrences",
idea="Count each value, then check that no two values share the same count.",
vname="Counts + set of counts",
spec=r'''
Return `true` if the number of occurrences of each value in `arr` is unique.

**Example**
```
[1,2,2,1,1,3] → true (counts 3, 2, 1),   [1,2] → false
```

**Constraints**
* `1 <= arr.length <= 1000`
''',
approach=r'''
**Two hash structures.** Count with `MyHashMap`; add every count to a `MyHashSet`; a failed add means two values share a count.

* Time: **O(n)** — linear.
* Space: **O(n)** — map and set.
''',
java=r'''
public class UniqueOccurrences {

    public boolean uniqueOccurrences(int[] arr) {
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int x : arr) count.merge(x, 1, Integer::sum);
        MyHashSet<Integer> seen = new MyHashSet<>();
        for (int c : count.values()) {
            if (!seen.add(c)) return false;
        }
        return true;
    }
}
''',
test=r'''
class UniqueOccurrencesTest {

    private final UniqueOccurrences solution = new UniqueOccurrences();

    @Test
    void examples() {
        assertTrue(solution.uniqueOccurrences(new int[]{1, 2, 2, 1, 1, 3}));
        assertFalse(solution.uniqueOccurrences(new int[]{1, 2}));
        assertTrue(solution.uniqueOccurrences(new int[]{-3, 0, 1, -3, 1, 1, 1, -3, 10, 0}));
    }
}
''',
trace=r'''
function run(a) {
  const cnt = new Map(); a.forEach(x => cnt.set(x, (cnt.get(x) || 0) + 1));
  A.step('Count each value.', A.arr('arr', a), A.hashTable('value → count', cnt));
  const seen = new Set();
  for (const [v, c] of cnt) { if (seen.has(c)) { A.step(`${v} also appears ${c} time${c > 1 ? 's' : ''}: counts are not unique.`, A.hashTable('counts seen', seen, { hl: c }), A.text('Result', 'false', 'bad')); return; } seen.add(c); A.step(`${v} appears ${c} time${c > 1 ? 's' : ''}: a new count.`, A.hashTable('counts seen', seen, { hl: c })); }
  A.step('All counts are different.', A.text('Result', 'true', 'ok'));
}
A.scenario('Unique counts', 'arr = [1,2,2,1,1,3]', () => run([1, 2, 2, 1, 1, 3]));
A.scenario('Repeated count', 'arr = [1,2]', () => run([1, 2]));
'''),

P(num=1657, slug="determine-if-two-strings-are-close", title="Determine if Two Strings Are Close", diff="Medium", topic="Arrays & Hashing", cls="CloseStrings",
idea="Swaps and letter-relabelling preserve the set of letters and the multiset of counts; those two must match.",
vname="Letter set + sorted counts",
spec=r'''
Two strings are **close** if one can become the other using (1) swaps of any two characters and (2) transforming every occurrence of one
existing letter into another existing letter and vice versa. Return `true` if `word1` and `word2` are close.

**Example**
```
"abc", "bca" → true,   "a", "aa" → false,   "cabbba", "abbccc" → true
```

**Constraints**
* `1 <= length <= 10^5`; lowercase letters.
''',
approach=r'''
**Invariants.** Swaps keep counts per letter; relabelling permutes counts among existing letters. So the strings are close iff they use the
same set of letters and their sorted count lists are equal.

* Time: **O(n)** — counting (sorting 26 counts is constant).
* Space: **O(1)** — two arrays of 26.
''',
java=r'''
public class CloseStrings {

    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()) return false;
        int[] a = new int[26], b = new int[26];
        for (char c : word1.toCharArray()) a[c - 'a']++;
        for (char c : word2.toCharArray()) b[c - 'a']++;
        for (int i = 0; i < 26; i++) {
            if ((a[i] == 0) != (b[i] == 0)) return false;
        }
        Arrays.sort(a);
        Arrays.sort(b);
        return Arrays.equals(a, b);
    }
}
''',
test=r'''
class CloseStringsTest {

    private final CloseStrings solution = new CloseStrings();

    @ParameterizedTest
    @CsvSource({"abc,bca,true", "a,aa,false", "cabbba,abbccc,true", "uau,ssx,false"})
    void checks(String a, String b, boolean expected) {
        assertEquals(expected, solution.closeStrings(a, b));
    }
}
''',
trace=r'''
function run(a, b) {
  const cnt = s => { const m = {}; [...s].forEach(c => (m[c] = (m[c] || 0) + 1)); return m; };
  const ca = cnt(a), cb = cnt(b);
  A.step('Count the letters of both words.', A.map('word1 counts', ca), A.map('word2 counts', cb));
  const sameSet = Object.keys(ca).sort().join('') === Object.keys(cb).sort().join('');
  A.step(sameSet ? 'Both words use the same set of letters.' : 'The letter sets differ, and relabelling can only swap existing letters.', A.text('letters', `${Object.keys(ca).sort().join('')} vs ${Object.keys(cb).sort().join('')}`, sameSet ? 'ok' : 'bad'));
  if (!sameSet) { A.step('Not close.', A.text('Result', 'false', 'bad')); return; }
  const sa = Object.values(ca).sort((x, y) => x - y), sb = Object.values(cb).sort((x, y) => x - y), ok = sa.join() === sb.join();
  A.step(`Sorted counts: [${sa}] vs [${sb}]. ${ok ? 'Equal, so relabelling can match them.' : 'Different.'}`, A.arr('word1 counts sorted', sa), A.arr('word2 counts sorted', sb), A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('Close', 'word1 = "cabbba", word2 = "abbccc"', () => run('cabbba', 'abbccc'));
'''),

P(num=2352, slug="equal-row-and-column-pairs", title="Equal Row and Column Pairs", diff="Medium", topic="Arrays & Hashing", cls="EqualRowColumnPairs",
idea="Count each row (as a key) in a hash map, then look up every column.",
vname="Hash rows, look up columns",
spec=r'''
Given an `n × n` grid, return the number of pairs `(r, c)` such that row `r` and column `c` contain the same values in the same order.

**Example**
```
[[3,2,1],[1,7,6],[2,7,7]]                 → 1
[[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]] → 3
```

**Constraints**
* `1 <= n <= 200`
''',
approach=r'''
**Row keys.** Turn each row into a `List<Integer>` and count it in a `MyHashMap`. For each column, build the same kind of key and add the
number of equal rows.

* Time: **O(n²)** — every cell is read twice; hashing a key costs O(n), n times per side.
* Space: **O(n²)** — the stored row keys.
''',
tc="n2", sc="n2",
java=r'''
public class EqualRowColumnPairs {

    public int equalPairs(int[][] grid) {
        int n = grid.length, pairs = 0;
        MyHashMap<List<Integer>, Integer> rows = new MyHashMap<>();
        for (int[] row : grid) {
            List<Integer> key = new ArrayList<>();
            for (int v : row) key.add(v);
            rows.merge(key, 1, Integer::sum);
        }
        for (int c = 0; c < n; c++) {
            List<Integer> key = new ArrayList<>();
            for (int r = 0; r < n; r++) key.add(grid[r][c]);
            pairs += rows.getOrDefault(key, 0);
        }
        return pairs;
    }
}
''',
test=r'''
class EqualRowColumnPairsTest {

    private final EqualRowColumnPairs solution = new EqualRowColumnPairs();

    @Test
    void examples() {
        assertEquals(1, solution.equalPairs(new int[][]{{3, 2, 1}, {1, 7, 6}, {2, 7, 7}}));
        assertEquals(3, solution.equalPairs(new int[][]{{3, 1, 2, 2}, {1, 4, 4, 5}, {2, 4, 2, 2}, {2, 4, 2, 2}}));
    }
}
''',
trace=r'''
function run(g) {
  const n = g.length, rows = new Map(); g.forEach(r => rows.set(r.join(','), (rows.get(r.join(',')) || 0) + 1));
  A.step('Count every row in a hash map, using the row itself as the key.', A.grid('grid', g), A.hashTable('row → count', rows));
  let pairs = 0;
  for (let c = 0; c < n; c++) {
    const key = g.map(r => r[c]).join(','), hit = rows.get(key) || 0; pairs += hit;
    A.step(`Column ${c} reads [${key}]: it matches ${hit} row${hit === 1 ? '' : 's'}.`, A.grid('grid', g, { hl: Object.fromEntries(g.flatMap((r, i) => r.map((_, j) => [`${i},${j}`, j === c ? 'cur' : r.join(',') === key ? 'ok' : '']))) }), A.hashTable('row → count', rows, { hl: key }), A.vars({ pairs }));
  }
  A.step(`${pairs} equal row/column pairs.`, A.text('Result', pairs, 'ok'));
}
A.scenario('Three pairs', '4 × 4 grid', () => run([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]));
'''),

P(num=2390, slug="removing-stars-from-a-string", title="Removing Stars From a String", diff="Medium", topic="Stack", cls="RemovingStars",
idea="Treat the result as a stack: letters push, each star pops the closest letter on its left.",
vname="Stack via StringBuilder",
spec=r'''
Each `*` in `s` removes itself and the closest non-star character to its left. Return the string after all stars are processed (the input
always allows this).

**Example**
```
"leet**cod*e" → "lecoe",   "erase*****" → ""
```

**Constraints**
* `1 <= s.length <= 10^5`
''',
approach=r'''
**Stack.** Append letters to a `StringBuilder`; for a star, delete its last character.

* Time: **O(n)** — O(1) per character.
* Space: **O(n)** — the builder.
''',
sc="n",
java=r'''
public class RemovingStars {

    public String removeStars(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c == '*') sb.deleteCharAt(sb.length() - 1);
            else sb.append(c);
        }
        return sb.toString();
    }
}
''',
test=r'''
class RemovingStarsTest {

    private final RemovingStars solution = new RemovingStars();

    @ParameterizedTest
    @CsvSource({"leet**cod*e,lecoe", "erase*****,''", "abc,abc"})
    void removes(String s, String expected) {
        assertEquals(expected, solution.removeStars(s));
    }
}
''',
trace=r'''
function run(s) {
  const st = [];
  [...s].forEach((c, i) => { if (c === '*') { const g = st.pop(); A.step(`'*' removes '${g}'.`, A.chars('s', s, { hl: { [i]: 'bad' } }), A.stack('result', st)); } else { st.push(c); A.step(`Push '${c}'.`, A.chars('s', s, { hl: { [i]: 'cur' } }), A.stack('result', st)); } });
  A.step(`Result: "${st.join('')}".`, A.text('Result', st.join(''), 'ok'));
}
A.scenario('Classic', 's = "leet**cod*e"', () => run('leet**cod*e'));
'''),

P(num=735, slug="asteroid-collision", title="Asteroid Collision", diff="Medium", topic="Stack", cls="AsteroidCollision",
idea="A stack of surviving asteroids; a left-moving one collides with right-moving ones on top until it dies or none remain.",
vname="Stack of survivors",
spec=r'''
Each asteroid's size is `|a|` and its direction is its sign (`+` right, `-` left); all move at the same speed. When two meet, the smaller
explodes; equal sizes both explode. Return the asteroids left after all collisions.

**Example**
```
[5,10,-5] → [5,10],   [8,-8] → [],   [10,2,-5] → [10],   [-2,-1,1,2] → [-2,-1,1,2]
```

**Constraints**
* `2 <= n <= 10^4`; `a != 0`
''',
approach=r'''
**Stack.** Right-movers just push. A left-mover fights the right-movers on top of the stack: it destroys smaller ones, dies against larger
ones, and both vanish on a tie. If it survives, push it.

* Time: **O(n)** — each asteroid is pushed and popped at most once.
* Space: **O(n)** — the stack.
''',
java=r'''
public class AsteroidCollision {

    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (int a : asteroids) {
            boolean alive = true;
            while (alive && a < 0 && !stack.isEmpty() && stack.peek() > 0) {
                int top = stack.peek();
                if (top < -a) stack.pop();
                else {
                    alive = false;
                    if (top == -a) stack.pop();
                }
            }
            if (alive) stack.push(a);
        }
        int[] out = new int[stack.size()];
        for (int i = out.length - 1; i >= 0; i--) out[i] = stack.pop();
        return out;
    }
}
''',
test=r'''
class AsteroidCollisionTest {

    private final AsteroidCollision solution = new AsteroidCollision();

    @Test
    void examples() {
        assertArrayEquals(new int[]{5, 10}, solution.asteroidCollision(new int[]{5, 10, -5}));
        assertArrayEquals(new int[]{}, solution.asteroidCollision(new int[]{8, -8}));
        assertArrayEquals(new int[]{10}, solution.asteroidCollision(new int[]{10, 2, -5}));
        assertArrayEquals(new int[]{-2, -1, 1, 2}, solution.asteroidCollision(new int[]{-2, -1, 1, 2}));
    }
}
''',
trace=r'''
function run(a) {
  const st = [];
  a.forEach((x, i) => {
    let alive = true;
    while (alive && x < 0 && st.length && st[st.length - 1] > 0) {
      const top = st[st.length - 1];
      if (top < -x) { st.pop(); A.step(`${x} hits ${top}: ${top} is smaller and explodes.`, A.arr('asteroids', a, { hl: { [i]: 'cur' } }), A.stack('survivors', st)); }
      else { alive = false; if (top === -x) { st.pop(); A.step(`${x} hits ${top}: equal sizes, both explode.`, A.arr('asteroids', a, { hl: { [i]: 'bad' } }), A.stack('survivors', st)); } else A.step(`${x} hits ${top}: ${x} is smaller and explodes.`, A.arr('asteroids', a, { hl: { [i]: 'bad' } }), A.stack('survivors', st)); }
    }
    if (alive) { st.push(x); A.step(`${x} ${x > 0 ? 'moves right' : 'meets nothing'}: it survives for now.`, A.arr('asteroids', a, { hl: { [i]: 'ok' } }), A.stack('survivors', st)); }
  });
  A.step(`Survivors: [${st}].`, A.text('Result', JSON.stringify(st), 'ok'));
}
A.scenario('Chain collision', 'asteroids = [10,2,-5]', () => run([10, 2, -5]));
A.scenario('Mixed', 'asteroids = [5,10,-5,-15,3]', () => run([5, 10, -5, -15, 3]));
'''),
]
