PROBLEMS = [
P(num=217, slug="contains-duplicate", title="Contains Duplicate", diff="Easy", topic="Arrays & Hashing", cls="ContainsDuplicate",
idea="Add values to a hash set; the first value that is already there is a duplicate.",
vname="Hash set",
spec=r'''
Return `true` if any value appears **at least twice** in `nums`, and `false` if every element is distinct.

**Example**
```
[1,2,3,1] → true,   [1,2,3,4] → false,   [1,1,1,3,3,4,3,2,4,2] → true
```

**Constraints**
* `1 <= nums.length <= 10^5`; `-10^9 <= nums[i] <= 10^9`
''',
approach=r'''
**Seen set.** `MyHashSet.add` returns `false` when the value is already present: that is a duplicate.

* Time: **O(n)** — one pass with O(1) average set operations.
* Space: **O(n)** — the set.
''',
java=r'''
public class ContainsDuplicate {

    public boolean containsDuplicate(int[] nums) {
        MyHashSet<Integer> seen = new MyHashSet<>();
        for (int x : nums) {
            if (!seen.add(x)) return true;
        }
        return false;
    }
}
''',
test=r'''
class ContainsDuplicateTest {

    private final ContainsDuplicate solution = new ContainsDuplicate();

    @Test
    void examples() {
        assertTrue(solution.containsDuplicate(new int[]{1, 2, 3, 1}));
        assertFalse(solution.containsDuplicate(new int[]{1, 2, 3, 4}));
        assertTrue(solution.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}));
    }

    @Test
    void single() {
        assertFalse(solution.containsDuplicate(new int[]{7}));
    }
}
''',
trace=r'''
function run(a) {
  const seen = new Set();
  A.step('Put each value in a hash set. A value that is already there is a duplicate.', A.arr('nums', a), A.hashTable('seen', seen));
  for (let i = 0; i < a.length; i++) {
    if (seen.has(a[i])) { A.step(`${a[i]} is already in the set. Duplicate found.`, A.arr('nums', a, { hl: { [i]: 'bad', [a.indexOf(a[i])]: 'bad' } }), A.hashTable('seen', seen, { hl: a[i] }), A.text('Result', 'true', 'ok')); return; }
    seen.add(a[i]);
    A.step(`${a[i]} is new. Add it.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.hashTable('seen', seen, { hl: a[i] }));
  }
  A.step('Every value was new, so there is no duplicate.', A.text('Result', 'false', 'bad'));
}
A.scenario('Has a duplicate', 'nums = [1,2,3,1]', () => run([1, 2, 3, 1]));
A.scenario('All distinct', 'nums = [1,2,3,4]', () => run([1, 2, 3, 4]));
''',
variants=[dict(
name="Sort and compare neighbours",
idea="After sorting, equal values are adjacent.",
approach=r'''
**Sort.** Sort a copy and check whether any two neighbours are equal.

* Time: **O(n log n)** — sorting.
* Space: **O(n)** — the sorted copy.
''',
tc="nlogn",
java=r'''
public class ContainsDuplicate {

    public boolean containsDuplicate(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        for (int i = 1; i < a.length; i++) {
            if (a[i] == a[i - 1]) return true;
        }
        return false;
    }
}
''',
trace=r'''
function run(a) {
  const s = a.slice().sort((x, y) => x - y);
  A.step('Sort the values.', A.arr('nums', a), A.arr('sorted', s));
  for (let i = 1; i < s.length; i++) {
    if (s[i] === s[i - 1]) { A.step(`Neighbours ${s[i - 1]} and ${s[i]} are equal.`, A.arr('sorted', s, { hl: { [i - 1]: 'bad', [i]: 'bad' } }), A.text('Result', 'true', 'ok')); return; }
    A.step(`${s[i - 1]} ≠ ${s[i]}.`, A.arr('sorted', s, { hl: { [i - 1]: 'sel', [i]: 'cur' } }));
  }
  A.step('No equal neighbours.', A.text('Result', 'false', 'bad'));
}
A.scenario('Has a duplicate', 'nums = [1,2,3,1]', () => run([1, 2, 3, 1]));
''')]),

P(num=347, slug="top-k-frequent-elements", title="Top K Frequent Elements", diff="Medium", topic="Arrays & Hashing", cls="TopKFrequent",
idea="Count with a hash map, then drop each value into a bucket indexed by its count and read buckets from the top.",
vname="Counting + bucket sort",
spec=r'''
Return the `k` most frequent elements of `nums`, in any order. The answer is guaranteed to be unique.

**Example**
```
nums = [1,1,1,2,2,3], k = 2 → [1,2]
nums = [1], k = 1            → [1]
```

**Constraints**
* `1 <= nums.length <= 10^5`; `1 <= k <=` number of distinct values

**Follow-up:** better than O(n log n).
''',
approach=r'''
**Bucket sort by frequency.** Count each value in a `MyHashMap`. A count is at most `n`, so put each value into `bucket[count]`.
Walk the buckets from `n` down to 1, collecting values until `k` are found.

* Time: **O(n)** — counting and bucketing are linear.
* Space: **O(n)** — the map and the buckets.
''',
java=r'''
public class TopKFrequent {

    public int[] topKFrequent(int[] nums, int k) {
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int x : nums) count.merge(x, 1, Integer::sum);
        List<List<Integer>> bucket = new ArrayList<>();
        for (int i = 0; i <= nums.length; i++) bucket.add(new ArrayList<>());
        for (MyHashMap.Entry<Integer, Integer> e : count.entries()) bucket.get(e.getValue()).add(e.getKey());
        int[] out = new int[k];
        int filled = 0;
        for (int f = nums.length; f > 0 && filled < k; f--) {
            for (int v : bucket.get(f)) {
                if (filled < k) out[filled++] = v;
            }
        }
        return out;
    }
}
''',
test=r'''
class TopKFrequentTest {

    private final TopKFrequent solution = new TopKFrequent();

    private static Set<Integer> set(int[] a) {
        Set<Integer> s = new HashSet<>();
        for (int x : a) s.add(x);
        return s;
    }

    @Test
    void examples() {
        assertEquals(Set.of(1, 2), set(solution.topKFrequent(new int[]{1, 1, 1, 2, 2, 3}, 2)));
        assertEquals(Set.of(1), set(solution.topKFrequent(new int[]{1}, 1)));
    }

    @Test
    void negatives() {
        assertEquals(Set.of(-1, 2), set(solution.topKFrequent(new int[]{4, -1, -1, 2, -1, 2, 3}, 2)));
    }
}
''',
trace=r'''
function run(a, k) {
  const cnt = new Map();
  a.forEach(x => cnt.set(x, (cnt.get(x) || 0) + 1));
  A.step('Count every value in a hash map.', A.arr('nums', a), A.hashTable('count', cnt));
  const bucket = [...Array(a.length + 1)].map(() => []);
  for (const [v, c] of cnt) bucket[c].push(v);
  A.step('Put each value into the bucket matching its count. Counts never exceed n, so there are n + 1 buckets.', A.arr('bucket[count]', bucket.map(b => (b.length ? b.join(',') : ''))));
  const out = [];
  for (let f = a.length; f > 0 && out.length < k; f--) if (bucket[f].length) { for (const v of bucket[f]) if (out.length < k) out.push(v); A.step(`Bucket ${f} holds ${bucket[f].join(', ')}. Take ${out.length < k ? 'them' : 'what we need'}.`, A.arr('bucket[count]', bucket.map(b => (b.length ? b.join(',') : '')), { hl: { [f]: 'ok' } }), A.arr('top k', out)); }
  A.step(`The ${k} most frequent: [${out}].`, A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('k = 2', 'nums = [1,1,1,2,2,3]', () => run([1, 1, 1, 2, 2, 3], 2));
''',
variants=[dict(
name="Counting + min-heap of size k",
idea="Keep the k most frequent values in a min-heap ordered by count.",
approach=r'''
**Heap.** Count with `MyHashMap`, then push `(value, count)` into a min-heap by count, popping whenever it holds more than `k`.

* Time: **O(n log k)** — each distinct value enters a heap of size k.
* Space: **O(n)** — the map (plus the heap).
''',
tc="nlogn",
java=r'''
public class TopKFrequent {

    public int[] topKFrequent(int[] nums, int k) {
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int x : nums) count.merge(x, 1, Integer::sum);
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(e -> e[1]));
        for (MyHashMap.Entry<Integer, Integer> e : count.entries()) {
            heap.add(new int[]{e.getKey(), e.getValue()});
            if (heap.size() > k) heap.poll();
        }
        int[] out = new int[k];
        for (int i = 0; i < k; i++) out[i] = heap.poll()[0];
        return out;
    }
}
''',
trace=r'''
function run(a, k) {
  const cnt = new Map(); a.forEach(x => cnt.set(x, (cnt.get(x) || 0) + 1));
  const heap = [];
  for (const [v, c] of cnt) { heap.push([v, c]); heap.sort((p, q) => p[1] - q[1]); let drop = null; if (heap.length > k) drop = heap.shift(); A.step(`Push ${v} (count ${c}).${drop ? ` Too many: drop ${drop[0]} (count ${drop[1]}).` : ''}`, A.arr('min-heap (value:count)', heap.map(([x, y]) => `${x}:${y}`), { hl: { 0: 'alt' } })); }
  A.step(`The heap holds the top ${k}.`, A.text('Result', JSON.stringify(heap.map(h => h[0])), 'ok'));
}
A.scenario('k = 2', 'nums = [1,1,1,2,2,3]', () => run([1, 1, 1, 2, 2, 3], 2));
''')]),

P(num=206, slug="reverse-linked-list", title="Reverse Linked List", diff="Easy", topic="Linked List", cls="ReverseLinkedList",
idea="Walk the list once, turning each next pointer around to point at the previous node.",
vname="Iterative pointer reversal", helpers=["ListNode"],
spec=r'''
Reverse a singly linked list and return the new head.

**Example**
```
1 → 2 → 3 → 4 → 5   becomes   5 → 4 → 3 → 2 → 1
```

**Constraints**
* `0 <= n <= 5000`

**Follow-up:** do it both iteratively and recursively.
''',
approach=r'''
**Three pointers.** Keep `prev` (already reversed part) and `cur`. Save `cur.next`, point `cur.next` at `prev`, then move both forward.

* Time: **O(n)** — each node once.
* Space: **O(1)** — three pointers.
''',
java=r'''
public class ReverseLinkedList {

    public ListNode reverseList(ListNode head) {
        ListNode prev = null, cur = head;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }
}
''',
test=r'''
class ReverseLinkedListTest {

    private final ReverseLinkedList solution = new ReverseLinkedList();

    @Test
    void five() {
        assertArrayEquals(new int[]{5, 4, 3, 2, 1}, ListNode.toArray(solution.reverseList(ListNode.of(1, 2, 3, 4, 5))));
    }

    @Test
    void emptyAndSingle() {
        assertNull(solution.reverseList(null));
        assertArrayEquals(new int[]{1}, ListNode.toArray(solution.reverseList(ListNode.of(1))));
    }
}
''',
trace=r'''
function run(vals) {
  const done = [], rest = vals.slice();
  A.step('prev is the reversed part (empty at first); cur walks the rest. Each step turns one arrow around.', A.list('reversed (prev)', done), A.list('remaining (cur)', rest));
  while (rest.length) {
    const v = rest.shift(); done.unshift(v);
    A.step(`Point ${v}'s next at ${done[1] ?? 'null'}; ${v} becomes the new head of the reversed part.`, A.list('reversed (prev)', done, { hl: { 0: 'ok' } }), A.list('remaining (cur)', rest, { hl: { 0: 'cur' } }));
  }
  A.step(`Reversed: ${done.join(' → ')}.`, A.text('Result', done.join(' → '), 'ok'));
}
A.scenario('Five nodes', '1→2→3→4→5', () => run([1, 2, 3, 4, 5]));
''',
variants=[dict(
name="Recursive",
idea="Reverse the rest of the list, then hook the current node onto its end.",
approach=r'''
**Recursion.** `reverse(head)`: reverse `head.next`, then `head.next.next = head` and `head.next = null`.

* Time: **O(n)** — one call per node.
* Space: **O(n)** — the recursion stack.
''',
sc="n",
java=r'''
public class ReverseLinkedList {

    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode newHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }
}
''',
trace=r'''
function run(vals) {
  const calls = [];
  const rec = i => { calls.push(`reverse(${vals[i]})`); A.step(`Call reverse starting at ${vals[i]}.`, A.stack('calls', calls)); if (i === vals.length - 1) { calls.pop(); A.step(`${vals[i]} is the last node: it is the new head.`, A.stack('calls', calls)); return [vals[i]]; } const r = rec(i + 1); r.push(vals[i]); calls.pop(); A.step(`Hook ${vals[i]} onto the end of the reversed rest.`, A.list('reversed so far', r, { hl: { [r.length - 1]: 'ok' } }), A.stack('calls', calls)); return r; };
  rec(0);
}
A.scenario('Four nodes', '1→2→3→4', () => run([1, 2, 3, 4]));
''')]),

P(num=704, slug="binary-search", title="Binary Search", diff="Easy", topic="Binary Search", cls="BinarySearch",
idea="Compare with the middle value and discard the half that cannot contain the target.",
vname="Classic binary search",
spec=r'''
Given a sorted array of **distinct** integers and a `target`, return its index or `-1`, in O(log n).

**Example**
```
nums = [-1,0,3,5,9,12]:  target 9 → 4,  target 2 → -1
```

**Constraints**
* `1 <= nums.length <= 10^4`; sorted ascending and distinct.
''',
approach=r'''
**Closed interval.** Keep `[lo, hi]`; compare `nums[mid]` with the target and move `lo = mid + 1` or `hi = mid - 1`. Use
`(lo + hi) >>> 1` so the sum cannot overflow.

* Time: **O(log n)** — the range halves each step.
* Space: **O(1)** — three indices.
''',
java=r'''
public class BinarySearch {

    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) lo = mid + 1; else hi = mid - 1;
        }
        return -1;
    }
}
''',
test=r'''
class BinarySearchTest {

    private final BinarySearch solution = new BinarySearch();

    @ParameterizedTest
    @CsvSource({"9,4", "2,-1", "-1,0", "12,5", "13,-1"})
    void searches(int target, int expected) {
        assertEquals(expected, solution.search(new int[]{-1, 0, 3, 5, 9, 12}, target));
    }
}
''',
trace=r'''
function run(a, t) {
  let lo = 0, hi = a.length - 1;
  A.step(`Look for ${t} in the sorted array.`, A.arr('nums', a, { range: [lo, hi] }));
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    if (a[mid] === t) { A.step(`nums[${mid}] = ${t}. Found.`, A.arr('nums', a, { hl: { [mid]: 'ok' } }), A.text('Result', mid, 'ok')); return; }
    A.step(`mid = ${mid}: ${a[mid]} is ${a[mid] < t ? 'smaller, so discard the left half' : 'larger, so discard the right half'}.`, A.arr('nums', a, { range: [lo, hi], ptr: [[lo, 'lo'], [hi, 'hi'], [mid, 'mid']], hl: { [mid]: 'cur' } }));
    if (a[mid] < t) lo = mid + 1; else hi = mid - 1;
  }
  A.step('The range is empty, so the target is not present.', A.text('Result', -1, 'bad'));
}
A.scenario('Found', 'target = 9', () => run([-1, 0, 3, 5, 9, 12], 9));
A.scenario('Missing', 'target = 2', () => run([-1, 0, 3, 5, 9, 12], 2));
'''),

P(num=283, slug="move-zeroes", title="Move Zeroes", diff="Easy", topic="Two Pointers", cls="MoveZeroes",
idea="Swap each non-zero value forward to the write pointer; zeros drift to the back.",
vname="Swap with write pointer",
spec=r'''
Move all `0`s in `nums` to the end **in place**, keeping the relative order of the non-zero values.

**Example**
```
[0,1,0,3,12] → [1,3,12,0,0]
```

**Constraints**
* `1 <= nums.length <= 10^4`
''',
approach=r'''
**Read/write pointers.** `k` is where the next non-zero belongs. For each non-zero `nums[i]`, swap it with `nums[k]` and advance `k`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — in place.
''',
java=r'''
public class MoveZeroes {

    public void moveZeroes(int[] nums) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int t = nums[k];
                nums[k++] = nums[i];
                nums[i] = t;
            }
        }
    }
}
''',
test=r'''
class MoveZeroesTest {

    private final MoveZeroes solution = new MoveZeroes();

    @Test
    void example() {
        int[] a = {0, 1, 0, 3, 12};
        solution.moveZeroes(a);
        assertArrayEquals(new int[]{1, 3, 12, 0, 0}, a);
    }

    @Test
    void noZeros() {
        int[] a = {1, 2};
        solution.moveZeroes(a);
        assertArrayEquals(new int[]{1, 2}, a);
    }
}
''',
trace=r'''
function run(a) {
  let k = 0;
  A.step('k marks where the next non-zero value goes.', A.arr('nums', a, { ptr: [[0, 'i,k']] }));
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== 0) { [a[k], a[i]] = [a[i], a[k]]; A.step(`${a[k]} is non-zero: swap it to index ${k}.`, A.arr('nums', a, { ptr: [[i, 'i'], [k + 1 < a.length ? k + 1 : k, 'k']], hl: { [k]: 'ok', [i]: i !== k ? 'alt' : 'ok' } })); k++; }
    else A.step(`Index ${i} is 0. Leave it; it will be swapped back later.`, A.arr('nums', a, { ptr: [[i, 'i'], [k, 'k']], hl: { [i]: 'dim' } }));
  }
  A.step('All non-zero values are at the front in their original order.', A.arr('nums', a, { hl: a.map((v, i) => [i, v ? 'ok' : 'dim']) }));
}
A.scenario('Classic', 'nums = [0,1,0,3,12]', () => run([0, 1, 0, 3, 12]));
'''),

P(num=344, slug="reverse-string", title="Reverse String", diff="Easy", topic="Two Pointers", cls="ReverseString",
idea="Swap the outermost pair and move both pointers inward.",
vname="Two pointers",
spec=r'''
Reverse an array of characters `s` **in place** with O(1) extra memory.

**Example**
```
["h","e","l","l","o"] → ["o","l","l","e","h"]
```

**Constraints**
* `1 <= s.length <= 10^5`
''',
approach=r'''
**Swap ends.** `l = 0`, `r = n - 1`; swap and move inward until they meet.

* Time: **O(n)** — n/2 swaps.
* Space: **O(1)** — one temporary.
''',
java=r'''
public class ReverseString {

    public void reverseString(char[] s) {
        for (int l = 0, r = s.length - 1; l < r; l++, r--) {
            char t = s[l];
            s[l] = s[r];
            s[r] = t;
        }
    }
}
''',
test=r'''
class ReverseStringTest {

    private final ReverseString solution = new ReverseString();

    @Test
    void hello() {
        char[] s = "hello".toCharArray();
        solution.reverseString(s);
        assertArrayEquals("olleh".toCharArray(), s);
    }

    @Test
    void even() {
        char[] s = "Hannah".toCharArray();
        solution.reverseString(s);
        assertArrayEquals("hannaH".toCharArray(), s);
    }
}
''',
trace=r'''
function run(str) {
  const s = [...str];
  for (let l = 0, r = s.length - 1; l < r; l++, r--) { [s[l], s[r]] = [s[r], s[l]]; A.step(`Swap positions ${l} and ${r}.`, A.arr('s', s, { ptr: [[l, 'l'], [r, 'r']], hl: { [l]: 'ok', [r]: 'ok' } })); }
  A.step(`Reversed: "${s.join('')}".`, A.text('Result', s.join(''), 'ok'));
}
A.scenario('hello', 's = "hello"', () => run('hello'));
'''),

P(num=268, slug="missing-number", title="Missing Number", diff="Easy", topic="Bit Manipulation", cls="MissingNumber",
idea="XOR every index and every value; all present numbers cancel, leaving the missing one.",
vname="XOR indices and values",
spec=r'''
`nums` contains `n` distinct numbers from the range `[0, n]`. Return the one number in the range that is missing.

**Example**
```
[3,0,1] → 2,   [0,1] → 2,   [9,6,4,2,3,5,7,0,1] → 8
```

**Constraints**
* `1 <= n <= 10^4`

**Follow-up:** O(1) extra space and O(n) time.
''',
approach=r'''
**XOR.** Start with `x = n` and XOR in every index `i` and every value `nums[i]`. Each present number appears twice and cancels;
the missing one appears once.

* Time: **O(n)** — one pass.
* Space: **O(1)** — one accumulator.
''',
java=r'''
public class MissingNumber {

    public int missingNumber(int[] nums) {
        int x = nums.length;
        for (int i = 0; i < nums.length; i++) x ^= i ^ nums[i];
        return x;
    }
}
''',
test=r'''
class MissingNumberTest {

    private final MissingNumber solution = new MissingNumber();

    @Test
    void examples() {
        assertEquals(2, solution.missingNumber(new int[]{3, 0, 1}));
        assertEquals(2, solution.missingNumber(new int[]{0, 1}));
        assertEquals(8, solution.missingNumber(new int[]{9, 6, 4, 2, 3, 5, 7, 0, 1}));
    }

    @Test
    void zeroMissing() {
        assertEquals(0, solution.missingNumber(new int[]{1}));
    }
}
''',
trace=r'''
function run(a) {
  let x = a.length;
  A.step(`XOR together every number 0..${a.length} and every value in the array. Numbers that appear in both cancel out.`, A.arr('nums', a), A.vars({ acc: x }));
  a.forEach((v, i) => { x ^= i ^ v; A.step(`XOR in index ${i} and value ${v}: acc = ${x}.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.vars({ acc: x })); });
  A.step(`Everything cancelled except ${x}: that number is missing.`, A.text('Result', x, 'ok'));
}
A.scenario('Missing 2', 'nums = [3,0,1]', () => run([3, 0, 1]));
''',
variants=[dict(
name="Gauss sum",
idea="The expected sum 0 + 1 + … + n minus the actual sum is the missing number.",
approach=r'''
**Arithmetic.** `n(n + 1)/2 - sum(nums)`.

* Time: **O(n)** — one pass to sum.
* Space: **O(1)** — one total.
''',
java=r'''
public class MissingNumber {

    public int missingNumber(int[] nums) {
        int n = nums.length, sum = n * (n + 1) / 2;
        for (int x : nums) sum -= x;
        return sum;
    }
}
''',
trace=r'''
function run(a) {
  const n = a.length, exp = n * (n + 1) / 2, act = a.reduce((s, v) => s + v, 0);
  A.step(`0 + 1 + … + ${n} = ${exp}.`, A.arr('nums', a), A.vars({ expected: exp }));
  A.step(`The values add up to ${act}. The difference ${exp} − ${act} = ${exp - act} is missing.`, A.vars({ expected: exp, actual: act }), A.text('Result', exp - act, 'ok'));
}
A.scenario('Missing 2', 'nums = [3,0,1]', () => run([3, 0, 1]));
''')]),

P(num=287, slug="find-the-duplicate-number", title="Find the Duplicate Number", diff="Medium", topic="Two Pointers", cls="FindDuplicate",
idea="Treat i → nums[i] as a linked list; the duplicate is where the cycle begins (Floyd).",
vname="Floyd cycle detection",
spec=r'''
`nums` has `n + 1` integers, each in `[1, n]`. Exactly one value is repeated (possibly many times). Return it without modifying the
array and using O(1) extra space.

**Example**
```
[1,3,4,2,2] → 2,   [3,1,3,4,2] → 3,   [3,3,3,3,3] → 3
```

**Constraints**
* `1 <= n <= 10^5`
''',
approach=r'''
**Cycle entrance.** Follow `x → nums[x]` from 0. Two indices point to the duplicate value, so the path forms a cycle whose entrance
is the duplicate. Phase 1: slow (1 step) and fast (2 steps) meet inside the cycle. Phase 2: restart one pointer at 0 and move both one
step at a time; they meet at the entrance.

* Time: **O(n)** — both phases are linear.
* Space: **O(1)** — two indices.
''',
java=r'''
public class FindDuplicate {

    public int findDuplicate(int[] nums) {
        int slow = nums[0], fast = nums[nums[0]];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        slow = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
}
''',
test=r'''
class FindDuplicateTest {

    private final FindDuplicate solution = new FindDuplicate();

    @Test
    void examples() {
        assertEquals(2, solution.findDuplicate(new int[]{1, 3, 4, 2, 2}));
        assertEquals(3, solution.findDuplicate(new int[]{3, 1, 3, 4, 2}));
        assertEquals(3, solution.findDuplicate(new int[]{3, 3, 3, 3, 3}));
    }
}
''',
trace=r'''
function run(a) {
  const nodes = a.map((_, i) => ({ id: i, label: i })), edges = a.map((v, i) => [i, v]);
  let slow = a[0], fast = a[a[0]];
  A.step('Draw an arrow from each index i to nums[i]. Two arrows point at the duplicate value, which creates a cycle.', A.graph('i → nums[i]', nodes, edges, { directed: true }), A.arr('nums', a));
  while (slow !== fast) { slow = a[slow]; fast = a[a[fast]]; A.step(`Phase 1: slow → ${slow}, fast → ${fast}.`, A.graph('i → nums[i]', nodes, edges, { directed: true, hl: { [slow]: 'cur', [fast]: 'alt' } })); }
  A.step(`They meet at ${slow}, inside the cycle. Phase 2: restart slow at 0; move both one step at a time.`, A.graph('i → nums[i]', nodes, edges, { directed: true, hl: { [slow]: 'sel' } }));
  slow = 0;
  while (slow !== fast) { slow = a[slow]; fast = a[fast]; A.step(`slow → ${slow}, fast → ${fast}.`, A.graph('i → nums[i]', nodes, edges, { directed: true, hl: { [slow]: 'cur', [fast]: 'alt' } })); }
  A.step(`They meet at ${slow}, the entrance of the cycle: the duplicate.`, A.graph('i → nums[i]', nodes, edges, { directed: true, hl: { [slow]: 'ok' } }), A.text('Result', slow, 'ok'));
}
A.scenario('Classic', 'nums = [1,3,4,2,2]', () => run([1, 3, 4, 2, 2]));
A.scenario('Another', 'nums = [3,1,3,4,2]', () => run([3, 1, 3, 4, 2]));
''',
variants=[dict(
name="Seen set",
idea="Remember every value; the first one seen twice is the duplicate.",
approach=r'''
**`MyHashSet`.** Simple, but uses O(n) memory, which the problem forbids.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the set.
''',
java=r'''
public class FindDuplicate {

    public int findDuplicate(int[] nums) {
        MyHashSet<Integer> seen = new MyHashSet<>();
        for (int x : nums) {
            if (!seen.add(x)) return x;
        }
        throw new IllegalArgumentException("No duplicate");
    }
}
''',
trace=r'''
function run(a) {
  const s = new Set();
  for (let i = 0; i < a.length; i++) { if (s.has(a[i])) { A.step(`${a[i]} was seen before: duplicate.`, A.arr('nums', a, { hl: { [i]: 'bad' } }), A.hashTable('seen', s, { hl: a[i] }), A.text('Result', a[i], 'ok')); return; } s.add(a[i]); A.step(`Remember ${a[i]}.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.hashTable('seen', s)); }
}
A.scenario('Classic', 'nums = [1,3,4,2,2]', () => run([1, 3, 4, 2, 2]));
''')]),

P(num=41, slug="first-missing-positive", title="First Missing Positive", diff="Hard", topic="Arrays & Hashing", cls="FirstMissingPositive",
idea="Use the array itself as a hash table: put every value v in 1..n at index v − 1, then find the first misplaced slot.",
vname="Cyclic placement",
spec=r'''
Return the smallest **positive** integer that does not appear in the unsorted array `nums`, in O(n) time and O(1) extra space.

**Example**
```
[1,2,0] → 3,   [3,4,-1,1] → 2,   [7,8,9,11,12] → 1
```

**Constraints**
* `1 <= nums.length <= 10^5`
''',
approach=r'''
**Place each value at its own index.** The answer is in `1..n+1`. For every slot, while `nums[i]` is in `1..n` and not already at
index `nums[i] - 1`, swap it there. Afterwards the first index `i` with `nums[i] != i + 1` gives the answer `i + 1`; if none, `n + 1`.

* Time: **O(n)** — every swap puts one value in its final place.
* Space: **O(1)** — the array is reused.
''',
java=r'''
public class FirstMissingPositive {

    public int firstMissingPositive(int[] nums) {
        int[] a = nums.clone();
        int n = a.length;
        for (int i = 0; i < n; i++) {
            while (a[i] >= 1 && a[i] <= n && a[a[i] - 1] != a[i]) {
                int j = a[i] - 1, t = a[j];
                a[j] = a[i];
                a[i] = t;
            }
        }
        for (int i = 0; i < n; i++) {
            if (a[i] != i + 1) return i + 1;
        }
        return n + 1;
    }
}
''',
test=r'''
class FirstMissingPositiveTest {

    private final FirstMissingPositive solution = new FirstMissingPositive();

    @Test
    void examples() {
        assertEquals(3, solution.firstMissingPositive(new int[]{1, 2, 0}));
        assertEquals(2, solution.firstMissingPositive(new int[]{3, 4, -1, 1}));
        assertEquals(1, solution.firstMissingPositive(new int[]{7, 8, 9, 11, 12}));
    }

    @Test
    void duplicatesAndFull() {
        assertEquals(2, solution.firstMissingPositive(new int[]{1, 1}));
        assertEquals(4, solution.firstMissingPositive(new int[]{3, 1, 2}));
    }
}
''',
trace=r'''
function run(nums) {
  const a = nums.slice(), n = a.length;
  A.step(`The answer is between 1 and ${n + 1}. Try to put each value v at index v − 1.`, A.arr('nums', a));
  for (let i = 0; i < n; i++) while (a[i] >= 1 && a[i] <= n && a[a[i] - 1] !== a[i]) { const j = a[i] - 1; [a[i], a[j]] = [a[j], a[i]]; A.step(`Send ${a[j]} to its home index ${j}.`, A.arr('nums', a, { hl: { [j]: 'ok', [i]: 'cur' } })); }
  const hl = a.map((v, i) => [i, v === i + 1 ? 'ok' : 'bad']);
  for (let i = 0; i < n; i++) if (a[i] !== i + 1) { A.step(`Index ${i} should hold ${i + 1} but holds ${a[i]}. So ${i + 1} is missing.`, A.arr('nums', a, { hl }), A.text('Result', i + 1, 'ok')); return; }
  A.step(`Every slot holds its own number, so the answer is ${n + 1}.`, A.arr('nums', a, { hl }), A.text('Result', n + 1, 'ok'));
}
A.scenario('Missing 2', 'nums = [3,4,-1,1]', () => run([3, 4, -1, 1]));
A.scenario('All large', 'nums = [7,8,9,11,12]', () => run([7, 8, 9, 11, 12]));
'''),

P(num=31, slug="next-permutation", title="Next Permutation", diff="Medium", topic="Two Pointers", cls="NextPermutation",
idea="Find the rightmost ascent, swap its left value with the next larger value to its right, then reverse the tail.",
vname="Pivot, swap, reverse",
spec=r'''
Rearrange `nums` **in place** into the next lexicographically greater permutation. If it is the largest permutation, rearrange it
into the smallest (ascending) one.

**Example**
```
[1,2,3] → [1,3,2],   [3,2,1] → [1,2,3],   [1,1,5] → [1,5,1]
```

**Constraints**
* `1 <= nums.length <= 100`
''',
approach=r'''
**Three steps.** (1) From the right, find the first `i` with `nums[i] < nums[i+1]` (the pivot); the tail after it is non-increasing.
(2) If found, swap `nums[i]` with the rightmost value in the tail that is larger than it. (3) Reverse the tail, making it ascending.

* Time: **O(n)** — at most three linear scans.
* Space: **O(1)** — in place.
''',
java=r'''
public class NextPermutation {

    public void nextPermutation(int[] nums) {
        int i = nums.length - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) i--;
        if (i >= 0) {
            int j = nums.length - 1;
            while (nums[j] <= nums[i]) j--;
            swap(nums, i, j);
        }
        for (int l = i + 1, r = nums.length - 1; l < r; l++, r--) swap(nums, l, r);
    }

    private static void swap(int[] a, int i, int j) {
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
}
''',
test=r'''
class NextPermutationTest {

    private final NextPermutation solution = new NextPermutation();

    private int[] next(int... a) {
        solution.nextPermutation(a);
        return a;
    }

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 3, 2}, next(1, 2, 3));
        assertArrayEquals(new int[]{1, 2, 3}, next(3, 2, 1));
        assertArrayEquals(new int[]{1, 5, 1}, next(1, 1, 5));
    }

    @Test
    void middle() {
        assertArrayEquals(new int[]{1, 3, 1, 2}, next(1, 2, 3, 1));
    }
}
''',
trace=r'''
function run(a) {
  let i = a.length - 2;
  A.step('From the right, find the first value that is smaller than its right neighbour: the pivot.', A.arr('nums', a));
  while (i >= 0 && a[i] >= a[i + 1]) i--;
  if (i < 0) { a.reverse(); A.step('The whole array is non-increasing: this is the largest permutation. Reverse it to get the smallest.', A.arr('nums', a, { hl: a.map((_, t) => [t, 'ok']) })); return; }
  A.step(`The pivot is ${a[i]} at index ${i}. Everything to its right is non-increasing.`, A.arr('nums', a, { hl: { [i]: 'cur', ...Object.fromEntries(a.slice(i + 1).map((_, t) => [i + 1 + t, 'sel'])) } }));
  let j = a.length - 1; while (a[j] <= a[i]) j--;
  [a[i], a[j]] = [a[j], a[i]];
  A.step(`Swap the pivot with ${a[i]}, the smallest value to its right that is larger than it.`, A.arr('nums', a, { hl: { [i]: 'ok', [j]: 'alt' } }));
  const tail = a.splice(i + 1).reverse(); a.push(...tail);
  A.step('Reverse the tail so it is ascending, the smallest possible order.', A.arr('nums', a, { hl: Object.fromEntries(tail.map((_, t) => [i + 1 + t, 'ok'])) }), A.text('Result', JSON.stringify(a), 'ok'));
}
A.scenario('Middle case', 'nums = [1,2,3,1]', () => run([1, 2, 3, 1]));
A.scenario('Edge: largest', 'nums = [3,2,1]', () => run([3, 2, 1]));
'''),
]
