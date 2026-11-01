PROBLEMS = [
P(num=678, slug="valid-parenthesis-string", title="Valid Parenthesis String", diff="Medium", topic="Greedy", cls="ValidParenthesisString",
idea="Track the range [lo, hi] of possible open-bracket counts; '*' widens the range.",
vname="Range of open counts",
spec=r'''
`s` contains `(`, `)` and `*`, where `*` can be `(`, `)` or empty. Return `true` if some choice makes `s` a valid parentheses string.

**Example**
```
"()" → true,   "(*)" → true,   "(*))" → true,   ")(" → false
```

**Constraints**
* `1 <= s.length <= 100`
''',
approach=r'''
**Interval of open counts.** `lo` is the fewest open brackets possible, `hi` the most. `(` raises both, `)` lowers both, `*` lowers `lo` and
raises `hi`. If `hi < 0`, too many `)` appear: fail. Clamp `lo` at 0. At the end, valid iff `lo == 0`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two counters.
''',
java=r'''
public class ValidParenthesisString {

    public boolean checkValidString(String s) {
        int lo = 0, hi = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') { lo++; hi++; }
            else if (c == ')') { lo--; hi--; }
            else { lo--; hi++; }
            if (hi < 0) return false;
            lo = Math.max(lo, 0);
        }
        return lo == 0;
    }
}
''',
test=r'''
class ValidParenthesisStringTest {

    private final ValidParenthesisString solution = new ValidParenthesisString();

    @ParameterizedTest
    @CsvSource({"'()',true", "'(*)',true", "'(*))',true", "')(',false", "'((*',false", "'*',true"})
    void checks(String s, boolean expected) {
        assertEquals(expected, solution.checkValidString(s));
    }
}
''',
trace=r'''
function run(s) {
  let lo = 0, hi = 0;
  A.step('lo and hi bound how many brackets might still be open. A star can be "(", ")" or nothing, so it widens the range.', A.chars('s', s), A.vars({ lo, hi }));
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (c === '(') { lo++; hi++; } else if (c === ')') { lo--; hi--; } else { lo--; hi++; }
    if (hi < 0) { A.step(`Too many ')' even if every star were '(': invalid.`, A.chars('s', s, { hl: { [i]: 'bad' } }), A.vars({ lo, hi }), A.text('Result', 'false', 'bad')); return; }
    lo = Math.max(lo, 0);
    A.step(`'${c}': open count is now between ${lo} and ${hi}.`, A.chars('s', s, { hl: { [i]: 'cur' } }), A.vars({ lo, hi }));
  }
  A.step(lo === 0 ? 'Zero open brackets is possible, so the string can be valid.' : `At least ${lo} brackets stay open: invalid.`, A.text('Result', String(lo === 0), lo === 0 ? 'ok' : 'bad'));
}
A.scenario('Valid', 's = "(*))"', () => run('(*))'));
A.scenario('Invalid', 's = "((*"', () => run('((*'));
'''),

P(num=435, slug="non-overlapping-intervals", title="Non-overlapping Intervals", diff="Medium", topic="Intervals", cls="NonOverlappingIntervals",
idea="Keep intervals that end earliest; every interval overlapping the last kept one must be removed.",
vname="Greedy by end",
spec=r'''
Return the minimum number of intervals to remove so the rest do not overlap (touching at an endpoint is fine).

**Example**
```
[[1,2],[2,3],[3,4],[1,3]] → 1
[[1,2],[1,2],[1,2]]       → 2
[[1,2],[2,3]]             → 0
```

**Constraints**
* `1 <= intervals.length <= 10^5`
''',
approach=r'''
**Activity selection.** Sort by end. Keep an interval when it starts at or after the last kept end; otherwise remove it. Ending earliest
leaves the most room for the rest.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's stack.
''',
tc="nlogn", sc="log",
java=r'''
public class NonOverlappingIntervals {

    public int eraseOverlapIntervals(int[][] intervals) {
        int[][] a = intervals.clone();
        Arrays.sort(a, Comparator.comparingInt(x -> x[1]));
        int removed = 0, end = Integer.MIN_VALUE;
        for (int[] iv : a) {
            if (iv[0] >= end) end = iv[1];
            else removed++;
        }
        return removed;
    }
}
''',
test=r'''
class NonOverlappingIntervalsTest {

    private final NonOverlappingIntervals solution = new NonOverlappingIntervals();

    @Test
    void examples() {
        assertEquals(1, solution.eraseOverlapIntervals(new int[][]{{1, 2}, {2, 3}, {3, 4}, {1, 3}}));
        assertEquals(2, solution.eraseOverlapIntervals(new int[][]{{1, 2}, {1, 2}, {1, 2}}));
        assertEquals(0, solution.eraseOverlapIntervals(new int[][]{{1, 2}, {2, 3}}));
    }
}
''',
trace=r'''
function run(iv) {
  const a = iv.map(x => x.slice()).sort((x, y) => x[1] - y[1]); let end = -Infinity, removed = 0;
  const lab = a.map(x => `[${x}]`), hl = {};
  A.step('Sort by end time and keep whatever ends first.', A.arr('intervals by end', lab));
  a.forEach((x, i) => {
    if (x[0] >= end) { end = x[1]; hl[i] = 'ok'; A.step(`[${x}] starts at or after ${end === x[1] ? 'the last kept end' : end}: keep it. New end: ${end}.`, A.arr('intervals by end', lab, { hl })); }
    else { removed++; hl[i] = 'bad'; A.step(`[${x}] overlaps the last kept interval: remove it.`, A.arr('intervals by end', lab, { hl }), A.vars({ removed })); }
  });
  A.step(`Remove ${removed}.`, A.text('Result', removed, 'ok'));
}
A.scenario('Classic', '[[1,2],[2,3],[3,4],[1,3]]', () => run([[1, 2], [2, 3], [3, 4], [1, 3]]));
'''),

P(num=7, slug="reverse-integer", title="Reverse Integer", diff="Medium", topic="Math", cls="ReverseInteger",
idea="Pop digits from the end and push them onto the result, checking for 32-bit overflow before each push.",
vname="Digit popping with overflow check",
spec=r'''
Reverse the digits of a signed 32-bit integer `x`. If the result overflows the 32-bit range, return 0. Assume no 64-bit integers are
available.

**Example**
```
123 → 321,   -123 → -321,   120 → 21,   1534236469 → 0
```

**Constraints**
* `-2^31 <= x <= 2^31 - 1`
''',
approach=r'''
**Check before multiplying.** `rev * 10 + d` overflows exactly when `rev > MAX/10` (or equals it with `d > 7`), and symmetrically for the
minimum. Java's `%` keeps the sign, so negative numbers work digit by digit.

* Time: **O(log x)** — one step per digit.
* Space: **O(1)** — one int.
''',
tc="log",
java=r'''
public class ReverseInteger {

    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int d = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE / 10 || (rev == Integer.MAX_VALUE / 10 && d > 7)) return 0;
            if (rev < Integer.MIN_VALUE / 10 || (rev == Integer.MIN_VALUE / 10 && d < -8)) return 0;
            rev = rev * 10 + d;
        }
        return rev;
    }
}
''',
test=r'''
class ReverseIntegerTest {

    private final ReverseInteger solution = new ReverseInteger();

    @ParameterizedTest
    @CsvSource({"123,321", "-123,-321", "120,21", "0,0", "1534236469,0", "-2147483648,0", "1463847412,2147483641"})
    void reverses(int x, int expected) {
        assertEquals(expected, solution.reverse(x));
    }
}
''',
trace=r'''
function run(x) {
  let rev = 0;
  A.step(`Pop the last digit of x and push it onto rev, checking first that rev × 10 + digit still fits in 32 bits.`, A.vars({ x, rev }));
  while (x !== 0) {
    const d = x % 10; x = Math.trunc(x / 10);
    if (rev > 214748364 || (rev === 214748364 && d > 7) || rev < -214748364 || (rev === -214748364 && d < -8)) { A.step(`Pushing ${d} would overflow 32 bits, so the answer is 0.`, A.vars({ x, rev }), A.text('Result', 0, 'bad')); return; }
    rev = rev * 10 + d;
    A.step(`Pop ${d}: rev = ${rev}.`, A.vars({ x, rev }));
  }
  A.step(`Reversed: ${rev}.`, A.text('Result', rev, 'ok'));
}
A.scenario('Negative', 'x = -123', () => run(-123));
A.scenario('Overflow', 'x = 1534236469', () => run(1534236469));
'''),

P(num=8, slug="string-to-integer-atoi", title="String to Integer (atoi)", diff="Medium", topic="Strings", cls="StringToInteger",
idea="Skip spaces, read an optional sign, then digits, clamping to the 32-bit range as soon as it would overflow.",
vname="Single pass with clamping",
spec=r'''
Convert a string to a 32-bit signed integer:
1. skip leading spaces; 2. read an optional `+` or `-`; 3. read digits until a non-digit (ignore the rest);
4. if no digits were read the result is 0; 5. clamp to `[-2^31, 2^31 - 1]`.

**Example**
```
"42" → 42,   "   -042" → -42,   "1337c0d3" → 1337,   "0-1" → 0,   "words and 987" → 0
```

**Constraints**
* `0 <= s.length <= 200`
''',
approach=r'''
**Careful scanning.** Accumulate digits; before `result * 10 + d`, check `result > (MAX - d) / 10` and clamp according to the sign.

* Time: **O(n)** — one pass.
* Space: **O(1)** — a few variables.
''',
java=r'''
public class StringToInteger {

    public int myAtoi(String s) {
        int i = 0, n = s.length(), sign = 1, result = 0;
        while (i < n && s.charAt(i) == ' ') i++;
        if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) sign = s.charAt(i++) == '-' ? -1 : 1;
        while (i < n && Character.isDigit(s.charAt(i))) {
            int d = s.charAt(i++) - '0';
            if (result > (Integer.MAX_VALUE - d) / 10) return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            result = result * 10 + d;
        }
        return sign * result;
    }
}
''',
test=r'''
class StringToIntegerTest {

    private final StringToInteger solution = new StringToInteger();

    @ParameterizedTest
    @CsvSource({"42,42", "'   -042',-42", "1337c0d3,1337", "0-1,0", "words and 987,0", "-91283472332,-2147483648", "2147483648,2147483647", "'',0"})
    void converts(String s, int expected) {
        assertEquals(expected, solution.myAtoi(s));
    }
}
''',
trace=r'''
function run(s) {
  let i = 0, sign = 1, res = 0;
  const shown = [...s].map(c => (c === ' ' ? '␣' : c));
  while (i < s.length && s[i] === ' ') i++;
  A.step(`Skip ${i} leading space${i === 1 ? '' : 's'}.`, A.arr('s', shown, { hl: Object.fromEntries([...Array(i)].map((_, t) => [t, 'dim'])) }));
  if (s[i] === '+' || s[i] === '-') { sign = s[i] === '-' ? -1 : 1; A.step(`Read the sign '${s[i]}'.`, A.arr('s', shown, { hl: { [i]: 'alt' } })); i++; }
  while (i < s.length && /[0-9]/.test(s[i])) {
    const d = +s[i];
    if (res > (2147483647 - d) / 10) { const c = sign > 0 ? 2147483647 : -2147483648; A.step(`Adding ${d} would overflow, so clamp to ${c}.`, A.arr('s', shown, { hl: { [i]: 'bad' } }), A.text('Result', c, 'ok')); return; }
    res = res * 10 + d;
    A.step(`Digit ${d}: value ${res}.`, A.arr('s', shown, { hl: { [i]: 'ok' } }), A.vars({ value: res, sign }));
    i++;
  }
  A.step(i < s.length ? `'${s[i]}' is not a digit: stop reading.` : 'End of string.', A.arr('s', shown, i < s.length ? { hl: { [i]: 'bad' } } : {}), A.text('Result', sign * res, 'ok'));
}
A.scenario('Spaces and sign', 's = "   -042"', () => run('   -042'));
A.scenario('Trailing letters', 's = "1337c0d3"', () => run('1337c0d3'));
'''),

P(num=16, slug="3sum-closest", title="3Sum Closest", diff="Medium", topic="Two Pointers", cls="ThreeSumClosest",
idea="Sort, fix one number, and move two pointers toward the target sum, remembering the closest sum seen.",
vname="Sort + two pointers",
spec=r'''
Find three numbers in `nums` whose sum is closest to `target` and return that sum. Exactly one answer exists.

**Example**
```
nums = [-1,2,1,-4], target = 1 → 2   (-1 + 2 + 1)
nums = [0,0,0], target = 1     → 0
```

**Constraints**
* `3 <= nums.length <= 500`
''',
approach=r'''
**Two pointers per fixed element.** Sort. For each `i`, move `l` and `r` inward: if the sum is below the target, `l++`; above, `r--`;
equal, return immediately. Track the sum with the smallest distance.

* Time: **O(n²)** — n fixed values × a linear scan.
* Space: **O(log n)** — sorting.
''',
tc="n2", sc="log",
java=r'''
public class ThreeSumClosest {

    public int threeSumClosest(int[] nums, int target) {
        int[] a = nums.clone();
        Arrays.sort(a);
        int best = a[0] + a[1] + a[2];
        for (int i = 0; i < a.length - 2; i++) {
            int l = i + 1, r = a.length - 1;
            while (l < r) {
                int sum = a[i] + a[l] + a[r];
                if (Math.abs(sum - target) < Math.abs(best - target)) best = sum;
                if (sum < target) l++;
                else if (sum > target) r--;
                else return sum;
            }
        }
        return best;
    }
}
''',
test=r'''
class ThreeSumClosestTest {

    private final ThreeSumClosest solution = new ThreeSumClosest();

    @Test
    void examples() {
        assertEquals(2, solution.threeSumClosest(new int[]{-1, 2, 1, -4}, 1));
        assertEquals(0, solution.threeSumClosest(new int[]{0, 0, 0}, 1));
        assertEquals(3, solution.threeSumClosest(new int[]{1, 1, 1, 0}, 100));
    }
}
''',
trace=r'''
function run(nums, t) {
  const a = nums.slice().sort((x, y) => x - y); let best = a[0] + a[1] + a[2];
  A.step(`Sort, then for each fixed number move two pointers toward ${t}.`, A.arr('sorted', a), A.vars({ target: t, best }));
  for (let i = 0; i < a.length - 2; i++) {
    let l = i + 1, r = a.length - 1;
    while (l < r) {
      const s = a[i] + a[l] + a[r];
      if (Math.abs(s - t) < Math.abs(best - t)) best = s;
      A.step(`${a[i]} + ${a[l]} + ${a[r]} = ${s}${s === best ? ' (closest so far)' : ''}. ${s < t ? 'Too small: move l right.' : s > t ? 'Too big: move r left.' : 'Exactly the target.'}`, A.arr('sorted', a, { ptr: [[i, 'i'], [l, 'l'], [r, 'r']], hl: { [i]: 'alt', [l]: 'cur', [r]: 'cur' } }), A.vars({ target: t, best }));
      if (s === t) { A.step('Exact match.', A.text('Result', s, 'ok')); return; }
      if (s < t) l++; else r--;
    }
  }
  A.step(`Closest sum: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', 'nums = [-1,2,1,-4], target = 1', () => run([-1, 2, 1, -4], 1));
'''),

P(num=18, slug="4sum", title="4Sum", diff="Medium", topic="Two Pointers", cls="FourSum",
idea="Fix two numbers with nested loops (skipping duplicates), then find the remaining pair with two pointers.",
vname="Sort + two loops + two pointers",
spec=r'''
Return all unique quadruplets `[a, b, c, d]` from `nums` (distinct indices) whose sum equals `target`, in any order.

**Example**
```
nums = [1,0,-1,0,-2,2], target = 0 → [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
nums = [2,2,2,2,2], target = 8      → [[2,2,2,2]]
```

**Constraints**
* `1 <= nums.length <= 200`; `-10^9 <= nums[i], target <= 10^9`
''',
approach=r'''
**Extend 3Sum.** Sort. Loop `i`, then `j > i` (skipping equal neighbours), then two pointers on the rest. Sums use `long`, since four
values near 10⁹ overflow an `int`.

* Time: **O(n³)** — n² pairs × a linear scan.
* Space: **O(log n)** — sorting (plus the output).
''',
tc="n2", sc="log",
java=r'''
public class FourSum {

    public List<List<Integer>> fourSum(int[] nums, int target) {
        int[] a = nums.clone();
        Arrays.sort(a);
        List<List<Integer>> out = new ArrayList<>();
        int n = a.length;
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && a[i] == a[i - 1]) continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && a[j] == a[j - 1]) continue;
                int l = j + 1, r = n - 1;
                while (l < r) {
                    long sum = (long) a[i] + a[j] + a[l] + a[r];
                    if (sum < target) l++;
                    else if (sum > target) r--;
                    else {
                        out.add(List.of(a[i], a[j], a[l], a[r]));
                        while (l < r && a[l] == a[l + 1]) l++;
                        while (l < r && a[r] == a[r - 1]) r--;
                        l++;
                        r--;
                    }
                }
            }
        }
        return out;
    }
}
''',
test=r'''
class FourSumTest {

    private final FourSum solution = new FourSum();

    @Test
    void examples() {
        assertEquals(List.of(List.of(-2, -1, 1, 2), List.of(-2, 0, 0, 2), List.of(-1, 0, 0, 1)), solution.fourSum(new int[]{1, 0, -1, 0, -2, 2}, 0));
        assertEquals(List.of(List.of(2, 2, 2, 2)), solution.fourSum(new int[]{2, 2, 2, 2, 2}, 8));
    }

    @Test
    void overflow() {
        assertEquals(List.of(), solution.fourSum(new int[]{1000000000, 1000000000, 1000000000, 1000000000}, -294967296));
    }
}
''',
trace=r'''
function run(nums, t) {
  const a = nums.slice().sort((x, y) => x - y), n = a.length, out = [];
  A.step('Sort. Fix the first two numbers with two loops; find the last two with two pointers.', A.arr('sorted', a), A.vars({ target: t }));
  for (let i = 0; i < n - 3; i++) { if (i && a[i] === a[i - 1]) continue; for (let j = i + 1; j < n - 2; j++) { if (j > i + 1 && a[j] === a[j - 1]) continue;
    let l = j + 1, r = n - 1;
    while (l < r) { const s = a[i] + a[j] + a[l] + a[r]; if (s === t) { out.push(`[${a[i]},${a[j]},${a[l]},${a[r]}]`); A.step(`${a[i]} + ${a[j]} + ${a[l]} + ${a[r]} = ${t}. Record it.`, A.arr('sorted', a, { ptr: [[i, 'i'], [j, 'j'], [l, 'l'], [r, 'r']], hl: { [i]: 'ok', [j]: 'ok', [l]: 'ok', [r]: 'ok' } }), A.arr('quadruplets', out)); while (l < r && a[l] === a[l + 1]) l++; while (l < r && a[r] === a[r - 1]) r--; l++; r--; } else if (s < t) l++; else r--; }
  } }
  A.step(`${out.length} unique quadruplets.`, A.arr('quadruplets', out));
}
A.scenario('Classic', 'nums = [1,0,-1,0,-2,2], target = 0', () => run([1, 0, -1, 0, -2, 2], 0));
'''),

P(num=43, slug="multiply-strings", title="Multiply Strings", diff="Medium", topic="Math", cls="MultiplyStrings",
idea="Digit i of num1 times digit j of num2 lands at positions i + j and i + j + 1 of the product.",
vname="Grade-school multiplication",
spec=r'''
Multiply two non-negative integers given as strings and return the product as a string, without converting the inputs to integers.

**Example**
```
"2" × "3" = "6",   "123" × "456" = "56088"
```

**Constraints**
* `1 <= num1.length, num2.length <= 200`; no leading zeros except "0".
''',
approach=r'''
**Position array.** The product has at most `m + n` digits. For every pair of digits, add their product at `i + j + 1` and carry into
`i + j`. Finally skip leading zeros.

* Time: **O(m·n)** — every digit pair.
* Space: **O(m + n)** — the result digits.
''',
tc="n2", sc="n",
java=r'''
public class MultiplyStrings {

    public String multiply(String num1, String num2) {
        int m = num1.length(), n = num2.length();
        int[] pos = new int[m + n];
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int sum = (num1.charAt(i) - '0') * (num2.charAt(j) - '0') + pos[i + j + 1];
                pos[i + j + 1] = sum % 10;
                pos[i + j] += sum / 10;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int d : pos) if (!(sb.isEmpty() && d == 0)) sb.append(d);
        return sb.isEmpty() ? "0" : sb.toString();
    }
}
''',
test=r'''
class MultiplyStringsTest {

    private final MultiplyStrings solution = new MultiplyStrings();

    @ParameterizedTest
    @CsvSource({"2,3,6", "123,456,56088", "0,52,0", "999,999,998001"})
    void multiplies(String a, String b, String expected) {
        assertEquals(expected, solution.multiply(a, b));
    }
}
''',
trace=r'''
function run(a, b) {
  const m = a.length, n = b.length, pos = new Array(m + n).fill(0);
  A.step(`The product has at most ${m + n} digits. Digit i of "${a}" times digit j of "${b}" lands at positions i + j and i + j + 1.`, A.chars('num1', a), A.chars('num2', b), A.arr('product digits', pos));
  for (let i = m - 1; i >= 0; i--) for (let j = n - 1; j >= 0; j--) {
    const s = +a[i] * +b[j] + pos[i + j + 1]; pos[i + j + 1] = s % 10; pos[i + j] += Math.floor(s / 10);
    A.step(`${a[i]} × ${b[j]} = ${+a[i] * +b[j]}: write ${s % 10} at position ${i + j + 1}, carry ${Math.floor(s / 10)} to ${i + j}.`, A.chars('num1', a, { hl: { [i]: 'cur' } }), A.chars('num2', b, { hl: { [j]: 'cur' } }), A.arr('product digits', pos, { hl: { [i + j + 1]: 'ok', [i + j]: 'sel' } }));
  }
  const r = pos.join('').replace(/^0+/, '') || '0';
  A.step(`Drop leading zeros: ${r}.`, A.text('Result', r, 'ok'));
}
A.scenario('123 × 45', 'num1 = "123", num2 = "45"', () => run('123', '45'));
'''),

P(num=706, slug="design-hashmap", title="Design HashMap", diff="Easy", topic="Design", cls="DesignHashMap",
idea="An array of buckets indexed by a hash of the key; colliding keys share a bucket's linked list; grow when it gets crowded.",
vname="Separate chaining with resizing",
spec=r'''
Design a hash map **without** any built-in hash table library:
* `put(key, value)`: insert or update;
* `get(key)`: the value, or `-1` if the key is absent;
* `remove(key)`.

**Example**
```
put(1,1); put(2,2); get(1) → 1; get(3) → -1; put(2,1); get(2) → 1; remove(2); get(2) → -1
```

**Constraints**
* `0 <= key, value <= 10^6`; at most `10^4` calls.
''',
approach=r'''
**Buckets + chaining.** Keys are spread with `h ^ (h >>> 16)` and masked to a power-of-two bucket count. Each bucket holds a singly linked
list of `(key, value)` nodes. When the number of entries exceeds 75% of the bucket count, double the array and re-insert every node, which
keeps chains short.

* Time: **O(1)** — average per operation.
* Space: **O(n)** — one node per key plus the bucket array.
''',
tc="1", sc="n",
java=r'''
public class DesignHashMap {

    private static final class Node {
        final int key;
        int value;
        Node next;

        Node(int key, int value, Node next) {
            this.key = key;
            this.value = value;
            this.next = next;
        }
    }

    private Node[] buckets = new Node[16];
    private int size;

    private int index(int key, int capacity) {
        int h = Integer.hashCode(key);
        return (h ^ (h >>> 16)) & (capacity - 1);
    }

    public void put(int key, int value) {
        int i = index(key, buckets.length);
        for (Node n = buckets[i]; n != null; n = n.next) {
            if (n.key == key) {
                n.value = value;
                return;
            }
        }
        buckets[i] = new Node(key, value, buckets[i]);
        if (++size > buckets.length * 3 / 4) resize();
    }

    public int get(int key) {
        for (Node n = buckets[index(key, buckets.length)]; n != null; n = n.next) {
            if (n.key == key) return n.value;
        }
        return -1;
    }

    public void remove(int key) {
        int i = index(key, buckets.length);
        for (Node prev = null, n = buckets[i]; n != null; prev = n, n = n.next) {
            if (n.key == key) {
                if (prev == null) buckets[i] = n.next; else prev.next = n.next;
                size--;
                return;
            }
        }
    }

    private void resize() {
        Node[] old = buckets;
        buckets = new Node[old.length * 2];
        for (Node head : old) {
            for (Node n = head; n != null; ) {
                Node next = n.next;
                int i = index(n.key, buckets.length);
                n.next = buckets[i];
                buckets[i] = n;
                n = next;
            }
        }
    }
}
''',
test=r'''
class DesignHashMapTest {

    @Test
    void example() {
        DesignHashMap m = new DesignHashMap();
        m.put(1, 1);
        m.put(2, 2);
        assertEquals(1, m.get(1));
        assertEquals(-1, m.get(3));
        m.put(2, 1);
        assertEquals(1, m.get(2));
        m.remove(2);
        assertEquals(-1, m.get(2));
    }

    @Test
    void manyKeysAndCollisions() {
        DesignHashMap m = new DesignHashMap();
        for (int k = 0; k < 5000; k++) m.put(k * 16, k);
        for (int k = 0; k < 5000; k++) assertEquals(k, m.get(k * 16));
        for (int k = 0; k < 5000; k += 2) m.remove(k * 16);
        assertEquals(-1, m.get(0));
        assertEquals(1, m.get(16));
    }
}
''',
trace=r'''
A.scenario('Collisions and growth', 'put 1, 9, 17, 2 · get 9 · remove 9 · then grow', () => {
  const m = new Map();
  const view = (msg, hl) => A.step(msg, A.hashTable('buckets', m, { capacity: 8, hl }));
  view('An array of 8 buckets. A key goes to bucket (hash ^ hash >>> 16) & 7, which for small ints is key mod 8.');
  for (const [k, v] of [[1, 10], [9, 90], [17, 170], [2, 20]]) { m.set(k, v); view(`put(${k}, ${v}): bucket ${k & 7}.${[1, 9, 17].includes(k) && k !== 1 ? ' That bucket already holds a key, so the new node is chained in front.' : ''}`, k); }
  view('get(9): go to bucket 1 and walk its chain until key 9 is found: 90.', 9);
  m.delete(9); view('remove(9): unlink its node from bucket 1’s chain.');
  for (const k of [3, 4, 5, 6]) m.set(k, k * 10);
  view('More than 75% of 8 buckets are used (7 entries > 6), so the array doubles to 16 buckets and every key is re-bucketed.');
});
'''),

P(num=232, slug="implement-queue-using-stacks", title="Implement Queue using Stacks", diff="Easy", topic="Design", cls="MyQueue",
idea="Push onto an inbox stack; pop from an outbox stack, refilling it (which reverses the order) only when it is empty.",
vname="Two stacks, lazy transfer",
spec=r'''
Implement a FIFO queue (`push`, `pop`, `peek`, `empty`) using only two stacks (push to top, pop/peek from top, size, isEmpty).

**Example**
```
push(1); push(2); peek() → 1; pop() → 1; empty() → false
```

**Constraints**
* At most 100 calls; `pop`/`peek` are only called on a non-empty queue.

**Follow-up:** amortized O(1) per operation.
''',
approach=r'''
**Inbox / outbox.** `push` goes onto `in`. `pop`/`peek` read from `out`; if `out` is empty, move everything from `in` to `out`, which reverses
it so the oldest element is on top. Each element moves at most once.

* Time: **O(1)** — amortized per operation.
* Space: **O(n)** — the two stacks.
''',
tc="1", sc="n",
java=r'''
public class MyQueue {

    private final Deque<Integer> in = new ArrayDeque<>(), out = new ArrayDeque<>();

    public void push(int x) {
        in.push(x);
    }

    public int pop() {
        peek();
        return out.pop();
    }

    public int peek() {
        if (out.isEmpty()) {
            while (!in.isEmpty()) out.push(in.pop());
        }
        return out.peek();
    }

    public boolean empty() {
        return in.isEmpty() && out.isEmpty();
    }
}
''',
test=r'''
class MyQueueTest {

    @Test
    void example() {
        MyQueue q = new MyQueue();
        q.push(1);
        q.push(2);
        assertEquals(1, q.peek());
        assertEquals(1, q.pop());
        assertFalse(q.empty());
        q.push(3);
        assertEquals(2, q.pop());
        assertEquals(3, q.pop());
        assertTrue(q.empty());
    }
}
''',
trace=r'''
A.scenario('Push and pop', 'push 1, 2, 3 · pop · push 4 · pop, pop, pop', () => {
  const inS = [], outS = [];
  const view = msg => A.step(msg, A.stack('in (push here)', inS), A.stack('out (pop here)', outS));
  const pop = () => { if (!outS.length) { while (inS.length) outS.push(inS.pop()); view('out is empty: move everything from in to out. That reverses the order, so the oldest is on top.'); } const v = outS.pop(); view(`pop() → ${v}.`); };
  for (const x of [1, 2, 3]) { inS.push(x); view(`push(${x}) onto in.`); }
  pop(); inS.push(4); view('push(4) onto in. out still has older items, so no transfer is needed.');
  pop(); pop(); pop();
});
'''),

P(num=225, slug="implement-stack-using-queues", title="Implement Stack using Queues", diff="Easy", topic="Design", cls="MyStack",
idea="After adding a new element to the queue, rotate the older ones behind it so the newest is always at the front.",
vname="One queue with rotation",
spec=r'''
Implement a LIFO stack (`push`, `pop`, `top`, `empty`) using only queue operations (add to back, remove/peek from front, size, isEmpty).

**Example**
```
push(1); push(2); top() → 2; pop() → 2; empty() → false
```

**Constraints**
* At most 100 calls; `pop`/`top` are only called on a non-empty stack.
''',
approach=r'''
**Rotate on push.** Add `x` at the back, then move the `size - 1` older elements from the front to the back. Now `x` is at the front, so
`pop` and `top` are plain queue operations.

* Time: **O(n)** — per push; pop/top are O(1).
* Space: **O(n)** — the queue.
''',
tc="n", sc="n",
java=r'''
public class MyStack {

    private final Deque<Integer> queue = new ArrayDeque<>();

    public void push(int x) {
        queue.addLast(x);
        for (int i = 1; i < queue.size(); i++) queue.addLast(queue.pollFirst());
    }

    public int pop() {
        return queue.pollFirst();
    }

    public int top() {
        return queue.peekFirst();
    }

    public boolean empty() {
        return queue.isEmpty();
    }
}
''',
test=r'''
class MyStackTest {

    @Test
    void example() {
        MyStack s = new MyStack();
        s.push(1);
        s.push(2);
        assertEquals(2, s.top());
        assertEquals(2, s.pop());
        assertFalse(s.empty());
        s.push(3);
        assertEquals(3, s.pop());
        assertEquals(1, s.pop());
        assertTrue(s.empty());
    }
}
''',
trace=r'''
A.scenario('Push and pop', 'push 1, 2, 3 · pop · top', () => {
  const q = [];
  const view = msg => A.step(msg, A.arr('queue (front → back)', q, { hl: { 0: 'ok' } }));
  for (const x of [1, 2, 3]) { q.push(x); view(`push(${x}): add it at the back.`); for (let i = 1; i < q.length; i++) q.push(q.shift()); view(`Rotate the ${q.length - 1} older element${q.length > 2 ? 's' : ''} behind it: ${x} is now at the front.`); }
  const v = q.shift(); view(`pop() → ${v}, taken from the front.`);
  view(`top() → ${q[0]}.`);
});
'''),
]
