PROBLEMS = [
P(num=389, slug="find-the-difference", title="Find the Difference", diff="Easy", topic="Bit Manipulation", cls="FindTheDifference",
idea="XOR every character of both strings; all pairs cancel and the added letter remains.",
vname="XOR of characters",
spec=r'''
`t` is `s` shuffled with one extra letter added. Return that letter.

**Example**
```
s = "abcd", t = "abcde" → 'e',   s = "", t = "y" → 'y'
```

**Constraints**
* `0 <= s.length <= 1000`; `t.length == s.length + 1`
''',
approach=r'''
**XOR.** Every letter of `s` appears in `t` too and cancels; the extra letter survives.

* Time: **O(n)** — one pass over each string.
* Space: **O(1)** — one accumulator.
''',
java=r'''
public class FindTheDifference {

    public char findTheDifference(String s, String t) {
        int x = 0;
        for (char c : s.toCharArray()) x ^= c;
        for (char c : t.toCharArray()) x ^= c;
        return (char) x;
    }
}
''',
test=r'''
class FindTheDifferenceTest {

    private final FindTheDifference solution = new FindTheDifference();

    @Test
    void examples() {
        assertEquals('e', solution.findTheDifference("abcd", "abcde"));
        assertEquals('y', solution.findTheDifference("", "y"));
        assertEquals('a', solution.findTheDifference("a", "aa"));
    }
}
''',
trace=r'''
function run(s, t) {
  let x = 0;
  [...s + t].forEach((c, i) => { x ^= c.charCodeAt(0); A.step(`XOR '${c}' (${c.charCodeAt(0)}): accumulator ${x}${x >= 97 && x <= 122 ? ` ('${String.fromCharCode(x)}')` : ''}.`, A.chars('s + t', s + t, { hl: { [i]: 'cur' } }), A.vars({ acc: x })); });
  A.step(`Pairs cancelled; '${String.fromCharCode(x)}' is the extra letter.`, A.text('Result', String.fromCharCode(x), 'ok'));
}
A.scenario('Extra e', 's = "abc", t = "cbae"', () => run('abc', 'cbae'));
'''),

P(num=448, slug="find-all-numbers-disappeared-in-an-array", title="Find All Numbers Disappeared in an Array", diff="Easy", topic="Arrays & Hashing", cls="FindDisappearedNumbers",
idea="Mark value v as seen by making nums[v−1] negative; indices left positive are the missing numbers.",
vname="Sign marking in place",
spec=r'''
`nums` has `n` values in `[1, n]`. Return every number in `[1, n]` that does not appear.

**Example**
```
[4,3,2,7,8,2,3,1] → [5,6],   [1,1] → [2]
```

**Constraints**
* `1 <= n <= 10^5`

**Follow-up:** no extra space (the output does not count).
''',
approach=r'''
**Signs as flags.** For each value `v = |nums[i]|`, make `nums[v-1]` negative. Afterwards, index `i` still positive means `i + 1` never
appeared. (We work on a copy so the input is untouched.)

* Time: **O(n)** — two passes.
* Space: **O(1)** — apart from the copy and output.
''',
java=r'''
public class FindDisappearedNumbers {

    public List<Integer> findDisappearedNumbers(int[] nums) {
        int[] a = nums.clone();
        for (int x : a) {
            int i = Math.abs(x) - 1;
            if (a[i] > 0) a[i] = -a[i];
        }
        List<Integer> out = new ArrayList<>();
        for (int i = 0; i < a.length; i++) {
            if (a[i] > 0) out.add(i + 1);
        }
        return out;
    }
}
''',
test=r'''
class FindDisappearedNumbersTest {

    private final FindDisappearedNumbers solution = new FindDisappearedNumbers();

    @Test
    void examples() {
        assertEquals(List.of(5, 6), solution.findDisappearedNumbers(new int[]{4, 3, 2, 7, 8, 2, 3, 1}));
        assertEquals(List.of(2), solution.findDisappearedNumbers(new int[]{1, 1}));
    }
}
''',
trace=r'''
function run(nums) {
  const a = nums.slice();
  A.step('Use the sign of each slot as a "seen" flag: value v marks slot v − 1 by making it negative.', A.arr('nums', a));
  a.forEach((_, k) => { const v = Math.abs(a[k]), i = v - 1; const was = a[i] < 0; if (!was) a[i] = -a[i]; A.step(`Value ${v}: ${was ? `slot ${i} is already marked` : `mark slot ${i}`}.`, A.arr('nums', a, { hl: { [k]: 'cur', [i]: 'alt' } })); });
  const out = a.map((v, i) => (v > 0 ? i + 1 : null)).filter(Boolean);
  A.step(`Slots still positive belong to missing numbers: [${out}].`, A.arr('nums', a, { hl: Object.fromEntries(a.map((v, i) => [i, v > 0 ? 'ok' : 'dim'])) }), A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Two missing', 'nums = [4,3,2,7,8,2,3,1]', () => run([4, 3, 2, 7, 8, 2, 3, 1]));
'''),

P(num=442, slug="find-all-duplicates-in-an-array", title="Find All Duplicates in an Array", diff="Medium", topic="Arrays & Hashing", cls="FindAllDuplicates",
idea="Flip the sign at index v−1 when you see v; finding it already negative means v is a duplicate.",
vname="Sign marking in place",
spec=r'''
`nums` has `n` values in `[1, n]`, each appearing once or twice. Return all values that appear twice, in O(n) time and O(1) extra space.

**Example**
```
[4,3,2,7,8,2,3,1] → [2,3],   [1,1,2] → [1],   [1] → []
```

**Constraints**
* `1 <= n <= 10^5`
''',
approach=r'''
**Signs as flags.** For each `v = |nums[i]|`: if `nums[v-1]` is already negative, `v` has been seen: record it; otherwise negate it.

* Time: **O(n)** — one pass.
* Space: **O(1)** — apart from the copy and output.
''',
java=r'''
public class FindAllDuplicates {

    public List<Integer> findDuplicates(int[] nums) {
        int[] a = nums.clone();
        List<Integer> out = new ArrayList<>();
        for (int x : a) {
            int i = Math.abs(x) - 1;
            if (a[i] < 0) out.add(i + 1);
            else a[i] = -a[i];
        }
        return out;
    }
}
''',
test=r'''
class FindAllDuplicatesTest {

    private final FindAllDuplicates solution = new FindAllDuplicates();

    @Test
    void examples() {
        assertEquals(List.of(2, 3), solution.findDuplicates(new int[]{4, 3, 2, 7, 8, 2, 3, 1}));
        assertEquals(List.of(1), solution.findDuplicates(new int[]{1, 1, 2}));
        assertEquals(List.of(), solution.findDuplicates(new int[]{1}));
    }
}
''',
trace=r'''
function run(nums) {
  const a = nums.slice(), out = [];
  a.forEach((_, k) => { const v = Math.abs(a[k]), i = v - 1; if (a[i] < 0) { out.push(v); A.step(`${v}: slot ${i} is already negative, so ${v} is a duplicate.`, A.arr('nums', a, { hl: { [k]: 'cur', [i]: 'bad' } }), A.arr('duplicates', out)); } else { a[i] = -a[i]; A.step(`${v}: mark slot ${i}.`, A.arr('nums', a, { hl: { [k]: 'cur', [i]: 'alt' } }), A.arr('duplicates', out)); } });
  A.step(`Duplicates: [${out}].`, A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Classic', 'nums = [4,3,2,7,8,2,3,1]', () => run([4, 3, 2, 7, 8, 2, 3, 1]));
'''),

P(num=485, slug="max-consecutive-ones", title="Max Consecutive Ones", diff="Easy", topic="Arrays & Hashing", cls="MaxConsecutiveOnes",
idea="Count the current run of 1s, reset on 0, and remember the longest run.",
vname="Running count",
spec=r'''
Return the maximum number of consecutive `1`s in a binary array.

**Example**
```
[1,1,0,1,1,1] → 3,   [1,0,1,1,0,1] → 2
```

**Constraints**
* `1 <= n <= 10^5`
''',
approach=r'''
**One pass.** `run = x == 1 ? run + 1 : 0`; track the maximum.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two counters.
''',
java=r'''
public class MaxConsecutiveOnes {

    public int findMaxConsecutiveOnes(int[] nums) {
        int run = 0, best = 0;
        for (int x : nums) {
            run = x == 1 ? run + 1 : 0;
            best = Math.max(best, run);
        }
        return best;
    }
}
''',
test=r'''
class MaxConsecutiveOnesTest {

    private final MaxConsecutiveOnes solution = new MaxConsecutiveOnes();

    @Test
    void examples() {
        assertEquals(3, solution.findMaxConsecutiveOnes(new int[]{1, 1, 0, 1, 1, 1}));
        assertEquals(2, solution.findMaxConsecutiveOnes(new int[]{1, 0, 1, 1, 0, 1}));
        assertEquals(0, solution.findMaxConsecutiveOnes(new int[]{0}));
    }
}
''',
trace=r'''
function run(a) {
  let run = 0, best = 0;
  a.forEach((x, i) => { run = x ? run + 1 : 0; best = Math.max(best, run); A.step(x ? `1: the run grows to ${run}. Best ${best}.` : '0: the run resets.', A.arr('nums', a, { hl: { [i]: x ? 'ok' : 'bad' }, range: run ? [i - run + 1, i] : undefined }), A.vars({ run, best })); });
  A.step(`Longest run: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', 'nums = [1,1,0,1,1,1]', () => run([1, 1, 0, 1, 1, 1]));
'''),

P(num=496, slug="next-greater-element-i", title="Next Greater Element I", diff="Easy", topic="Stack", cls="NextGreaterElementI",
idea="A decreasing stack over nums2 finds every element's next greater value; a hash map answers the queries from nums1.",
vname="Monotonic stack + hash map",
spec=r'''
`nums1` is a subset of `nums2` (all values distinct). For each `x` in `nums1`, find the first value to the right of `x` in `nums2` that is
greater than `x`, or `-1`.

**Example**
```
nums1 = [4,1,2], nums2 = [1,3,4,2] → [-1,3,-1]
nums1 = [2,4],   nums2 = [1,2,3,4] → [3,-1]
```

**Constraints**
* `1 <= nums1.length <= nums2.length <= 1000`
''',
approach=r'''
**One stack pass.** Scan `nums2`; while the current value is larger than the stack top, the top's next greater value is the current one:
record it in a `MyHashMap`. Then answer `nums1` from the map (default -1).

* Time: **O(m + n)** — each value is pushed and popped once.
* Space: **O(n)** — the stack and map.
''',
java=r'''
public class NextGreaterElementI {

    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        MyHashMap<Integer, Integer> next = new MyHashMap<>();
        Deque<Integer> stack = new ArrayDeque<>();
        for (int x : nums2) {
            while (!stack.isEmpty() && stack.peek() < x) next.put(stack.pop(), x);
            stack.push(x);
        }
        int[] out = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) out[i] = next.getOrDefault(nums1[i], -1);
        return out;
    }
}
''',
test=r'''
class NextGreaterElementITest {

    private final NextGreaterElementI solution = new NextGreaterElementI();

    @Test
    void examples() {
        assertArrayEquals(new int[]{-1, 3, -1}, solution.nextGreaterElement(new int[]{4, 1, 2}, new int[]{1, 3, 4, 2}));
        assertArrayEquals(new int[]{3, -1}, solution.nextGreaterElement(new int[]{2, 4}, new int[]{1, 2, 3, 4}));
    }
}
''',
trace=r'''
function run(n1, n2) {
  const st = [], next = new Map();
  n2.forEach((x, i) => { const res = []; while (st.length && st[st.length - 1] < x) { const t = st.pop(); next.set(t, x); res.push(t); } st.push(x); A.step(res.length ? `${x} is the next greater value for ${res.join(', ')}.` : `${x}: nothing on the stack is smaller.`, A.arr('nums2', n2, { hl: { [i]: 'cur' } }), A.stack('waiting', st), A.hashTable('next greater', next)); });
  const out = n1.map(x => (next.has(x) ? next.get(x) : -1));
  A.step(`Answer each query from the map: [${out}].`, A.arr('nums1', n1), A.arr('answer', out), A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Classic', 'nums1 = [4,1,2], nums2 = [1,3,4,2]', () => run([4, 1, 2], [1, 3, 4, 2]));
'''),

P(num=503, slug="next-greater-element-ii", title="Next Greater Element II", diff="Medium", topic="Stack", cls="NextGreaterElementII",
idea="Scan the circular array twice with a stack of indices; the second pass resolves elements that wrap around.",
vname="Monotonic stack over two passes",
spec=r'''
`nums` is **circular**. For each element, return the first greater value found by moving right (wrapping around), or `-1`.

**Example**
```
[1,2,1] → [2,-1,2],   [1,2,3,4,3] → [2,3,4,-1,4]
```

**Constraints**
* `1 <= n <= 10^4`
''',
approach=r'''
**Virtual doubled array.** Iterate `i` from 0 to `2n - 1` using `nums[i % n]`; pop smaller indices from the stack and set their answer.
Only push indices during the first pass.

* Time: **O(n)** — each index is pushed and popped once.
* Space: **O(n)** — the stack.
''',
java=r'''
public class NextGreaterElementII {

    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] out = new int[n];
        Arrays.fill(out, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < 2 * n; i++) {
            int x = nums[i % n];
            while (!stack.isEmpty() && nums[stack.peek()] < x) out[stack.pop()] = x;
            if (i < n) stack.push(i);
        }
        return out;
    }
}
''',
test=r'''
class NextGreaterElementIITest {

    private final NextGreaterElementII solution = new NextGreaterElementII();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, -1, 2}, solution.nextGreaterElements(new int[]{1, 2, 1}));
        assertArrayEquals(new int[]{2, 3, 4, -1, 4}, solution.nextGreaterElements(new int[]{1, 2, 3, 4, 3}));
    }
}
''',
trace=r'''
function run(a) {
  const n = a.length, out = new Array(n).fill(-1), st = [];
  for (let i = 0; i < 2 * n; i++) {
    const x = a[i % n], res = [];
    while (st.length && a[st[st.length - 1]] < x) { const j = st.pop(); out[j] = x; res.push(j); }
    if (i < n) st.push(i);
    A.step(`${i < n ? 'First' : 'Second (wrap-around)'} pass, value ${x}: ${res.length ? `answers index${res.length > 1 ? 'es' : ''} ${res.join(', ')}` : 'resolves nothing'}.`, A.arr('nums', a, { hl: { [i % n]: 'cur', ...Object.fromEntries(res.map(j => [j, 'ok'])) } }), A.stack('waiting indices', st), A.arr('answer', out));
  }
}
A.scenario('Circular', 'nums = [1,2,3,4,3]', () => run([1, 2, 3, 4, 3]));
'''),

P(num=556, slug="next-greater-element-iii", title="Next Greater Element III", diff="Medium", topic="Math", cls="NextGreaterElementIII",
idea="Apply next permutation to the digits; return -1 if there is none or it overflows 32 bits.",
vname="Next permutation of digits",
spec=r'''
Return the smallest integer greater than `n` that uses exactly the same digits, or `-1` if none exists or it exceeds 32 bits.

**Example**
```
12 → 21,   21 → -1,   2147483486 → -1
```

**Constraints**
* `1 <= n <= 2^31 - 1`
''',
approach=r'''
**Next permutation.** Find the rightmost digit smaller than its right neighbour, swap it with the smallest larger digit to its right,
reverse the tail. Parse as `long` and check the 32-bit limit.

* Time: **O(d)** — d ≤ 10 digits.
* Space: **O(d)** — the digit array.
''',
tc="1", sc="1",
java=r'''
public class NextGreaterElementIII {

    public int nextGreaterElement(int n) {
        char[] d = String.valueOf(n).toCharArray();
        int i = d.length - 2;
        while (i >= 0 && d[i] >= d[i + 1]) i--;
        if (i < 0) return -1;
        int j = d.length - 1;
        while (d[j] <= d[i]) j--;
        char t = d[i];
        d[i] = d[j];
        d[j] = t;
        for (int l = i + 1, r = d.length - 1; l < r; l++, r--) {
            t = d[l];
            d[l] = d[r];
            d[r] = t;
        }
        long value = Long.parseLong(new String(d));
        return value > Integer.MAX_VALUE ? -1 : (int) value;
    }
}
''',
test=r'''
class NextGreaterElementIIITest {

    private final NextGreaterElementIII solution = new NextGreaterElementIII();

    @ParameterizedTest
    @CsvSource({"12,21", "21,-1", "2147483486,-1", "230241,230412", "1999999999,-1"})
    void next(int n, int expected) {
        assertEquals(expected, solution.nextGreaterElement(n));
    }
}
''',
trace=r'''
function run(n) {
  const d = String(n).split('');
  let i = d.length - 2; while (i >= 0 && d[i] >= d[i + 1]) i--;
  A.step('From the right, find the first digit smaller than its right neighbour.', A.arr('digits', d, i >= 0 ? { hl: { [i]: 'cur' } } : {}));
  if (i < 0) { A.step('The digits never increase from right to left, so no larger arrangement exists.', A.text('Result', -1, 'bad')); return; }
  let j = d.length - 1; while (d[j] <= d[i]) j--;
  [d[i], d[j]] = [d[j], d[i]];
  A.step(`Swap it with ${d[i]}, the smallest larger digit to its right.`, A.arr('digits', d, { hl: { [i]: 'ok', [j]: 'alt' } }));
  const tail = d.splice(i + 1).reverse(); d.push(...tail);
  const v = +d.join('');
  A.step(`Reverse the tail to make it as small as possible: ${v}.${v > 2147483647 ? ' That exceeds 32 bits, so -1.' : ''}`, A.arr('digits', d, { hl: Object.fromEntries(tail.map((_, t) => [i + 1 + t, 'sel'])) }), A.text('Result', v > 2147483647 ? -1 : v, 'ok'));
}
A.scenario('230241', 'n = 230241', () => run(230241));
'''),

P(num=557, slug="reverse-words-in-a-string-iii", title="Reverse Words in a String III", diff="Easy", topic="Two Pointers", cls="ReverseWordsIII",
idea="Find each word's boundaries and reverse its characters in place.",
vname="Reverse each word",
spec=r'''
Reverse the characters of every word in `s` while keeping the word order and the single spaces.

**Example**
```
"Let's take LeetCode contest" → "s'teL ekat edoCteeL tsetnoc"
```

**Constraints**
* `1 <= s.length <= 5 * 10^4`; words are separated by single spaces.
''',
approach=r'''
**Two pointers per word.** Scan for each word's start and end, and swap characters inward.

* Time: **O(n)** — each character is swapped once.
* Space: **O(n)** — the character array.
''',
sc="n",
java=r'''
public class ReverseWordsIII {

    public String reverseWords(String s) {
        char[] a = s.toCharArray();
        for (int start = 0; start < a.length; ) {
            int end = start;
            while (end < a.length && a[end] != ' ') end++;
            for (int l = start, r = end - 1; l < r; l++, r--) {
                char t = a[l];
                a[l] = a[r];
                a[r] = t;
            }
            start = end + 1;
        }
        return new String(a);
    }
}
''',
test=r'''
class ReverseWordsIIITest {

    private final ReverseWordsIII solution = new ReverseWordsIII();

    @Test
    void examples() {
        assertEquals("s'teL ekat edoCteeL tsetnoc", solution.reverseWords("Let's take LeetCode contest"));
        assertEquals("rM gniD", solution.reverseWords("Mr Ding"));
    }
}
''',
trace=r'''
function run(s) {
  const a = [...s];
  for (let st = 0; st < a.length;) { let e = st; while (e < a.length && a[e] !== ' ') e++; const w = a.slice(st, e).join(''); a.splice(st, e - st, ...a.slice(st, e).reverse()); A.step(`Reverse "${w}" in place.`, A.chars('s', a.join('').replace(/ /g, '␣'), { range: [st, e - 1] })); st = e + 1; }
  A.step(`Result: "${a.join('')}".`, A.text('Result', a.join(''), 'ok'));
}
A.scenario('Three words', 's = "Mr Ding here"', () => run('Mr Ding here'));
'''),

P(num=561, slug="array-partition", title="Array Partition", diff="Easy", topic="Greedy", cls="ArrayPartition",
idea="Sort and pair neighbours; the sum of every other element (the smaller of each pair) is maximal.",
vname="Sort and take every other",
spec=r'''
Group `2n` integers into `n` pairs to maximize the sum of `min(a, b)` over all pairs. Return that sum.

**Example**
```
[1,4,3,2] → 4 ((1,2), (3,4)),   [6,2,6,5,1,2] → 9
```

**Constraints**
* `1 <= n <= 10^4`
''',
approach=r'''
**Pair neighbours after sorting.** The smallest element is a minimum anyway, so pair it with the next smallest to waste as little as possible;
repeat. The answer is the sum of elements at even indices of the sorted array.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's stack.
''',
tc="nlogn", sc="log",
java=r'''
public class ArrayPartition {

    public int arrayPairSum(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        int sum = 0;
        for (int i = 0; i < a.length; i += 2) sum += a[i];
        return sum;
    }
}
''',
test=r'''
class ArrayPartitionTest {

    private final ArrayPartition solution = new ArrayPartition();

    @Test
    void examples() {
        assertEquals(4, solution.arrayPairSum(new int[]{1, 4, 3, 2}));
        assertEquals(9, solution.arrayPairSum(new int[]{6, 2, 6, 5, 1, 2}));
    }
}
''',
trace=r'''
function run(nums) {
  const a = nums.slice().sort((x, y) => x - y); let sum = 0;
  A.step('Sort, then pair neighbours. The smaller of each pair is at an even index.', A.arr('sorted', a));
  for (let i = 0; i < a.length; i += 2) { sum += a[i]; A.step(`Pair (${a[i]}, ${a[i + 1]}): add the minimum ${a[i]}. Sum ${sum}.`, A.arr('sorted', a, { hl: { [i]: 'ok', [i + 1]: 'dim' } }), A.vars({ sum })); }
  A.step(`Maximum sum of minimums: ${sum}.`, A.text('Result', sum, 'ok'));
}
A.scenario('Six numbers', 'nums = [6,2,6,5,1,2]', () => run([6, 2, 6, 5, 1, 2]));
'''),

P(num=566, slug="reshape-the-matrix", title="Reshape the Matrix", diff="Easy", topic="Matrix", cls="ReshapeMatrix",
idea="Read cells in row-major order and write them in the same order into an r × c matrix.",
vname="Row-major index mapping",
spec=r'''
Reshape an `m × n` matrix into `r × c`, filling row by row in the original row-major order. If `r × c != m × n`, return the original matrix.

**Example**
```
mat = [[1,2],[3,4]], r = 1, c = 4 → [[1,2,3,4]]
mat = [[1,2],[3,4]], r = 2, c = 4 → [[1,2],[3,4]]
```

**Constraints**
* `1 <= m, n <= 100`
''',
approach=r'''
**Flat index.** Cell number `k` lives at `(k / n, k % n)` in the input and at `(k / c, k % c)` in the output.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the new matrix.
''',
tc="n2", sc="n2",
java=r'''
public class ReshapeMatrix {

    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length, n = mat[0].length;
        if (m * n != r * c) return mat;
        int[][] out = new int[r][c];
        for (int k = 0; k < m * n; k++) out[k / c][k % c] = mat[k / n][k % n];
        return out;
    }
}
''',
test=r'''
class ReshapeMatrixTest {

    private final ReshapeMatrix solution = new ReshapeMatrix();

    @Test
    void examples() {
        assertArrayEquals(new int[][]{{1, 2, 3, 4}}, solution.matrixReshape(new int[][]{{1, 2}, {3, 4}}, 1, 4));
        assertArrayEquals(new int[][]{{1, 2}, {3, 4}}, solution.matrixReshape(new int[][]{{1, 2}, {3, 4}}, 2, 4));
        assertArrayEquals(new int[][]{{1}, {2}, {3}, {4}}, solution.matrixReshape(new int[][]{{1, 2}, {3, 4}}, 4, 1));
    }
}
''',
trace=r'''
function run(mat, r, c) {
  const m = mat.length, n = mat[0].length, out = [...Array(r)].map(() => new Array(c).fill(''));
  A.step(`Read the ${m} × ${n} matrix row by row and refill a ${r} × ${c} matrix in the same order.`, A.grid('input', mat), A.grid('output', out));
  for (let k = 0; k < m * n; k++) { out[Math.floor(k / c)][k % c] = mat[Math.floor(k / n)][k % n]; A.step(`Cell #${k} (${mat[Math.floor(k / n)][k % n]}) goes from (${Math.floor(k / n)},${k % n}) to (${Math.floor(k / c)},${k % c}).`, A.grid('input', mat, { hl: { [`${Math.floor(k / n)},${k % n}`]: 'cur' } }), A.grid('output', out, { hl: { [`${Math.floor(k / c)},${k % c}`]: 'ok' } })); }
}
A.scenario('2 × 3 → 3 × 2', 'mat = [[1,2,3],[4,5,6]]', () => run([[1, 2, 3], [4, 5, 6]], 3, 2));
'''),
]
