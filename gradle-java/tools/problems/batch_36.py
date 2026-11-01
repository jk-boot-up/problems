PROBLEMS = [
P(num=29, slug="divide-two-integers", title="Divide Two Integers", diff="Medium", topic="Bit Manipulation", cls="DivideTwoIntegers",
idea="Subtract the largest doubled divisor (divisor·2^k) that still fits, adding 2^k to the quotient each time.",
vname="Exponential subtraction",
spec=r'''
Divide two integers **without** using multiplication, division or mod. The quotient truncates toward zero. If the result overflows 32 bits,
return `2^31 - 1`.

**Example**
```
10 / 3 = 3,   7 / -3 = -2,   -2147483648 / -1 = 2147483647
```

**Constraints**
* `-2^31 <= dividend, divisor <= 2^31 - 1`; `divisor != 0`
''',
approach=r'''
**Doubling.** Work with negative numbers (they have the larger range). Repeatedly find the largest `divisor << k` that still fits in the
remaining dividend, subtract it and add `1 << k` to the quotient. Handle the single overflow case `MIN / -1` first.

* Time: **O(log² n)** — at most 31 outer rounds, each doubling up to 31 times.
* Space: **O(1)** — a few ints.
''',
tc="log",
java=r'''
public class DivideTwoIntegers {

    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) return Integer.MAX_VALUE;
        boolean negative = (dividend < 0) != (divisor < 0);
        int a = dividend > 0 ? -dividend : dividend, b = divisor > 0 ? -divisor : divisor; // both <= 0
        int quotient = 0;
        while (a <= b) {
            int chunk = b, multiple = 1;
            while (chunk >= (Integer.MIN_VALUE >> 1) && a <= chunk + chunk) {
                chunk += chunk;
                multiple += multiple;
            }
            a -= chunk;
            quotient += multiple;
        }
        return negative ? -quotient : quotient;
    }
}
''',
test=r'''
class DivideTwoIntegersTest {

    private final DivideTwoIntegers solution = new DivideTwoIntegers();

    @ParameterizedTest
    @CsvSource({"10,3,3", "7,-3,-2", "-2147483648,-1,2147483647", "-2147483648,1,-2147483648", "1,1,1", "0,5,0", "2147483647,2,1073741823"})
    void divides(int a, int b, int expected) {
        assertEquals(expected, solution.divide(a, b));
    }
}
''',
trace=r'''
function run(x, y) {
  let a = Math.abs(x), q = 0; const b = Math.abs(y);
  A.step(`Divide ${a} by ${b} using only subtraction and doubling.`, A.vars({ remaining: a, quotient: q }));
  while (a >= b) {
    let chunk = b, mult = 1; const ladder = [`${b}×1`];
    while (a >= chunk * 2) { chunk *= 2; mult *= 2; ladder.push(`${chunk / mult * mult}×${mult}`); }
    a -= chunk; q += mult;
    A.step(`Double ${b} until the next doubling would be too big: ${b} × ${mult} = ${chunk}. Subtract it; quotient += ${mult}.`, A.arr('doublings tried', ladder, { hl: { [ladder.length - 1]: 'ok' } }), A.vars({ remaining: a, quotient: q }));
  }
  const res = (x < 0) !== (y < 0) ? -q : q;
  A.step(`Remaining ${a} is less than ${b}. Apply the sign: ${res}.`, A.text('Result', res, 'ok'));
}
A.scenario('100 / 7', 'dividend = 100, divisor = 7', () => run(100, 7));
'''),

P(num=38, slug="count-and-say", title="Count and Say", diff="Medium", topic="Strings", cls="CountAndSay",
idea="Each term reads the previous one aloud: run-length encode it as (count, digit) pairs.",
vname="Run-length encoding",
spec=r'''
`countAndSay(1) = "1"`; `countAndSay(n)` describes `countAndSay(n-1)` by saying, for each run of equal digits, the run length followed by the
digit. Return the `n`-th term.

**Example**
```
1 → "1",   2 → "11",   3 → "21",   4 → "1211",   5 → "111221"
```

**Constraints**
* `1 <= n <= 30`
''',
approach=r'''
**Iterate.** Starting from `"1"`, build each next term by scanning runs and appending `count` then `digit`.

* Time: **O(L)** — L is the total length of all terms produced (it grows by about 30% per step).
* Space: **O(L)** — the current term.
''',
tc="exp", sc="exp",
java=r'''
public class CountAndSay {

    public String countAndSay(int n) {
        String s = "1";
        for (int k = 1; k < n; k++) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < s.length(); ) {
                int j = i;
                while (j < s.length() && s.charAt(j) == s.charAt(i)) j++;
                sb.append(j - i).append(s.charAt(i));
                i = j;
            }
            s = sb.toString();
        }
        return s;
    }
}
''',
test=r'''
class CountAndSayTest {

    private final CountAndSay solution = new CountAndSay();

    @ParameterizedTest
    @CsvSource({"1,1", "2,11", "3,21", "4,1211", "5,111221", "6,312211"})
    void terms(int n, String expected) {
        assertEquals(expected, solution.countAndSay(n));
    }
}
''',
trace=r'''
function run(n) {
  let s = '1';
  A.step('The first term is "1".', A.chars('term 1', s));
  for (let k = 2; k <= n; k++) {
    let out = '', i = 0; const runs = [];
    while (i < s.length) { let j = i; while (j < s.length && s[j] === s[i]) j++; runs.push(`${j - i}×${s[i]}`); out += (j - i) + s[i]; i = j; }
    A.step(`Read term ${k - 1} aloud: ${runs.map(r => r.replace('×', ' × ')).join(', ')} → "${out}".`, A.chars(`term ${k - 1}`, s), A.arr('runs', runs), A.chars(`term ${k}`, out, { hl: Object.fromEntries([...out].map((_, t) => [t, t % 2 ? 'sel' : 'alt'])) }));
    s = out;
  }
}
A.scenario('Up to term 6', 'n = 6', () => run(6));
'''),

P(num=59, slug="spiral-matrix-ii", title="Spiral Matrix II", diff="Medium", topic="Matrix", cls="SpiralMatrixII",
idea="Walk the four shrinking boundaries clockwise, writing 1, 2, 3, … as you go.",
vname="Shrinking boundaries",
spec=r'''
Generate an `n × n` matrix filled with `1 .. n²` in clockwise spiral order.

**Example**
```
n = 3 → [[1,2,3],[8,9,4],[7,6,5]]
```

**Constraints**
* `1 <= n <= 20`
''',
approach=r'''
**Boundaries.** Fill the top row left→right, right column top→bottom, bottom row right→left, left column bottom→top; shrink and repeat.

* Time: **O(n²)** — each cell once.
* Space: **O(1)** — apart from the output.
''',
tc="n2", sc="1",
java=r'''
public class SpiralMatrixII {

    public int[][] generateMatrix(int n) {
        int[][] m = new int[n][n];
        int top = 0, bottom = n - 1, left = 0, right = n - 1, v = 1;
        while (v <= n * n) {
            for (int c = left; c <= right; c++) m[top][c] = v++;
            top++;
            for (int r = top; r <= bottom; r++) m[r][right] = v++;
            right--;
            for (int c = right; c >= left; c--) m[bottom][c] = v++;
            bottom--;
            for (int r = bottom; r >= top; r--) m[r][left] = v++;
            left++;
        }
        return m;
    }
}
''',
test=r'''
class SpiralMatrixIITest {

    private final SpiralMatrixII solution = new SpiralMatrixII();

    @Test
    void examples() {
        assertArrayEquals(new int[][]{{1, 2, 3}, {8, 9, 4}, {7, 6, 5}}, solution.generateMatrix(3));
        assertArrayEquals(new int[][]{{1}}, solution.generateMatrix(1));
        assertArrayEquals(new int[][]{{1, 2, 3, 4}, {12, 13, 14, 5}, {11, 16, 15, 6}, {10, 9, 8, 7}}, solution.generateMatrix(4));
    }
}
''',
trace=r'''
function run(n) {
  const m = [...Array(n)].map(() => new Array(n).fill('')); let top = 0, bottom = n - 1, left = 0, right = n - 1, v = 1;
  const put = (r, c, dir) => { m[r][c] = v++; A.step(`Walk ${dir}: write ${m[r][c]}.`, A.grid('matrix', m, { hl: { [`${r},${c}`]: 'cur' } })); };
  while (v <= n * n) {
    for (let c = left; c <= right; c++) put(top, c, 'right'); top++;
    for (let r = top; r <= bottom; r++) put(r, right, 'down'); right--;
    for (let c = right; c >= left; c--) put(bottom, c, 'left'); bottom--;
    for (let r = bottom; r >= top; r--) put(r, left, 'up'); left++;
  }
  A.step('The spiral is complete.', A.grid('matrix', m));
}
A.scenario('n = 4', '4 × 4 spiral', () => run(4));
'''),

P(num=60, slug="permutation-sequence", title="Permutation Sequence", diff="Hard", topic="Math", cls="PermutationSequence",
idea="Factorials tell how many permutations start with each digit; pick digits one by one with k's factorial-base digits.",
vname="Factorial number system",
spec=r'''
The permutations of `1..n`, listed in lexicographic order, are numbered from 1. Return the `k`-th one as a string.

**Example**
```
n = 3, k = 3 → "213",   n = 4, k = 9 → "2314",   n = 3, k = 1 → "123"
```

**Constraints**
* `1 <= n <= 9`; `1 <= k <= n!`
''',
approach=r'''
**Skip whole blocks.** With `m` digits left, each choice of first digit starts a block of `(m-1)!` permutations. Using zero-based `k`, the
block index is `k / (m-1)!`: take that remaining digit, set `k %= (m-1)!`, and repeat.

* Time: **O(n²)** — n picks, each removing from a list of up to n digits.
* Space: **O(n)** — the remaining digits.
''',
tc="n2", sc="n",
java=r'''
public class PermutationSequence {

    public String getPermutation(int n, int k) {
        List<Integer> digits = new ArrayList<>();
        int[] fact = new int[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            digits.add(i);
            fact[i] = fact[i - 1] * i;
        }
        StringBuilder sb = new StringBuilder();
        k--;
        for (int m = n; m >= 1; m--) {
            int block = k / fact[m - 1];
            sb.append(digits.remove(block));
            k %= fact[m - 1];
        }
        return sb.toString();
    }
}
''',
test=r'''
class PermutationSequenceTest {

    private final PermutationSequence solution = new PermutationSequence();

    @ParameterizedTest
    @CsvSource({"3,3,213", "4,9,2314", "3,1,123", "3,6,321", "9,362880,987654321"})
    void finds(int n, int k, String expected) {
        assertEquals(expected, solution.getPermutation(n, k));
    }
}
''',
trace=r'''
function run(n, k) {
  const digits = [...Array(n)].map((_, i) => i + 1), fact = [1]; for (let i = 1; i <= n; i++) fact.push(fact[i - 1] * i);
  let kk = k - 1, out = '';
  A.step(`Use zero-based k = ${kk}. With m digits left, each possible first digit covers (m − 1)! permutations.`, A.arr('remaining digits', digits), A.vars({ k: kk }));
  for (let m = n; m >= 1; m--) {
    const block = Math.floor(kk / fact[m - 1]), d = digits[block];
    A.step(`${m} digits left: each block has ${fact[m - 1]} permutations. ${kk} ÷ ${fact[m - 1]} = ${block}, so take ${d}.`, A.arr('remaining digits', digits, { hl: { [block]: 'ok' } }), A.vars({ k: kk, output: out + d }));
    digits.splice(block, 1); out += d; kk %= fact[m - 1];
  }
  A.step(`The ${k}th permutation is ${out}.`, A.text('Result', out, 'ok'));
}
A.scenario('n = 4, k = 9', 'the 9th permutation of 1234', () => run(4, 9));
'''),

P(num=65, slug="valid-number", title="Valid Number", diff="Hard", topic="Strings", cls="ValidNumber",
idea="One pass tracking what has been seen (digits, a dot, an exponent) and rejecting anything out of place.",
vname="Single scan with flags",
spec=r'''
Return `true` if `s` is a valid number: an integer or decimal (optional sign, digits with at most one dot and at least one digit), optionally
followed by `e`/`E` and an integer exponent (optional sign, at least one digit).

**Example**
```
valid:   "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "53.5e93"
invalid: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "."
```

**Constraints**
* `1 <= s.length <= 20`
''',
approach=r'''
**Flags.** Scan once with `digits`, `dot` and `exp` flags. A sign is allowed only at the start or right after `e`. A dot is allowed once
and never after `e`. `e` needs digits before it and resets `digits` so that digits must follow. Anything else is invalid. Valid iff
`digits` at the end.

* Time: **O(n)** — one pass.
* Space: **O(1)** — three flags.
''',
java=r'''
public class ValidNumber {

    public boolean isNumber(String s) {
        boolean digits = false, dot = false, exp = false;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                digits = true;
            } else if (c == '+' || c == '-') {
                if (i > 0 && s.charAt(i - 1) != 'e' && s.charAt(i - 1) != 'E') return false;
            } else if (c == '.') {
                if (dot || exp) return false;
                dot = true;
            } else if (c == 'e' || c == 'E') {
                if (exp || !digits) return false;
                exp = true;
                digits = false;
            } else {
                return false;
            }
        }
        return digits;
    }
}
''',
test=r'''
class ValidNumberTest {

    private final ValidNumber solution = new ValidNumber();

    @ParameterizedTest
    @CsvSource({"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "53.5e93"})
    void valid(String s) {
        assertTrue(solution.isNumber(s));
    }

    @ParameterizedTest
    @CsvSource({"abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "."})
    void invalid(String s) {
        assertFalse(solution.isNumber(s));
    }
}
''',
trace=r'''
function run(s) {
  let digits = false, dot = false, exp = false;
  const view = (msg, i, c) => A.step(msg, A.chars('s', s, { hl: { [i]: c } }), A.vars({ digits, dot, exp }));
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (/\d/.test(c)) { digits = true; view(`'${c}' is a digit.`, i, 'ok'); }
    else if (c === '+' || c === '-') { if (i > 0 && !/[eE]/.test(s[i - 1])) { view(`A sign is only allowed at the start or right after e.`, i, 'bad'); A.step('Invalid.', A.text('Result', 'false', 'bad')); return; } view(`'${c}' is a sign in a valid place.`, i, 'sel'); }
    else if (c === '.') { if (dot || exp) { view(`A second dot, or a dot in the exponent, is not allowed.`, i, 'bad'); A.step('Invalid.', A.text('Result', 'false', 'bad')); return; } dot = true; view('The decimal point.', i, 'sel'); }
    else if (/[eE]/.test(c)) { if (exp || !digits) { view(`'${c}' needs digits before it and may appear only once.`, i, 'bad'); A.step('Invalid.', A.text('Result', 'false', 'bad')); return; } exp = true; digits = false; view('The exponent marker: digits must follow.', i, 'alt'); }
    else { view(`'${c}' cannot appear in a number.`, i, 'bad'); A.step('Invalid.', A.text('Result', 'false', 'bad')); return; }
  }
  A.step(digits ? 'The string ends with digits in the right places: valid.' : 'The string ended before the required digits.', A.text('Result', String(digits), digits ? 'ok' : 'bad'));
}
A.scenario('Valid', 's = "-12.5e+3"', () => run('-12.5e+3'));
A.scenario('Invalid', 's = "99e2.5"', () => run('99e2.5'));
'''),

P(num=81, slug="search-in-rotated-sorted-array-ii", title="Search in Rotated Sorted Array II", diff="Medium", topic="Binary Search", cls="SearchRotatedArrayII",
idea="Like the distinct version, but when lo, mid and hi are equal the sorted half is unknown, so shrink both ends.",
vname="Binary search with duplicate skipping",
spec=r'''
A sorted array, possibly with **duplicates**, was rotated. Return `true` if `target` is in it.

**Example**
```
nums = [2,5,6,0,0,1,2]: target 0 → true, target 3 → false
```

**Constraints**
* `1 <= nums.length <= 5000`

**Follow-up:** duplicates can make the worst case linear — why?
''',
approach=r'''
**Pick the sorted half when possible.** If `nums[lo] == nums[mid] == nums[hi]`, either half could hold the rotation, so just move `lo++`,
`hi--`. Otherwise one half is sorted; check whether the target lies inside it, exactly as in the distinct version.

* Time: **O(n)** — worst case with many duplicates; O(log n) when values are distinct.
* Space: **O(1)** — indices.
''',
tc="n",
java=r'''
public class SearchRotatedArrayII {

    public boolean search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] == target) return true;
            if (nums[lo] == nums[mid] && nums[mid] == nums[hi]) {
                lo++;
                hi--;
            } else if (nums[lo] <= nums[mid]) {
                if (nums[lo] <= target && target < nums[mid]) hi = mid - 1; else lo = mid + 1;
            } else {
                if (nums[mid] < target && target <= nums[hi]) lo = mid + 1; else hi = mid - 1;
            }
        }
        return false;
    }
}
''',
test=r'''
class SearchRotatedArrayIITest {

    private final SearchRotatedArrayII solution = new SearchRotatedArrayII();

    @Test
    void examples() {
        assertTrue(solution.search(new int[]{2, 5, 6, 0, 0, 1, 2}, 0));
        assertFalse(solution.search(new int[]{2, 5, 6, 0, 0, 1, 2}, 3));
        assertTrue(solution.search(new int[]{1, 0, 1, 1, 1}, 0));
    }
}
''',
trace=r'''
function run(a, t) {
  let lo = 0, hi = a.length - 1;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    if (a[mid] === t) { A.step(`nums[${mid}] = ${t}. Found.`, A.arr('nums', a, { hl: { [mid]: 'ok' } }), A.text('Result', 'true', 'ok')); return; }
    if (a[lo] === a[mid] && a[mid] === a[hi]) { A.step(`lo, mid and hi all hold ${a[mid]}: we cannot tell which half is sorted, so shrink both ends by one.`, A.arr('nums', a, { range: [lo, hi], hl: { [lo]: 'bad', [mid]: 'cur', [hi]: 'bad' } })); lo++; hi--; continue; }
    const leftSorted = a[lo] <= a[mid], inside = leftSorted ? a[lo] <= t && t < a[mid] : a[mid] < t && t <= a[hi];
    A.step(`The ${leftSorted ? 'left' : 'right'} half is sorted; ${t} is ${inside ? '' : 'not '}inside it, so go ${inside === leftSorted ? 'left' : 'right'}.`, A.arr('nums', a, { range: [lo, hi], hl: { [mid]: 'cur' } }));
    if (inside === leftSorted) hi = mid - 1; else lo = mid + 1;
  }
  A.step('Not found.', A.text('Result', 'false', 'bad'));
}
A.scenario('Ambiguous duplicates', 'nums = [1,0,1,1,1], target = 0', () => run([1, 0, 1, 1, 1], 0));
'''),

P(num=87, slug="scramble-string", title="Scramble String", diff="Hard", topic="Multidimensional DP", cls="ScrambleString",
idea="s2 is a scramble of s1 if some split of s1 matches s2's halves either in order or swapped, recursively.",
vname="Memoized recursion with pruning",
spec=r'''
A string is scrambled by splitting it into two non-empty parts, optionally swapping them, and scrambling each part recursively. Return
`true` if `s2` is a scrambled string of `s1`.

**Example**
```
"great", "rgeat" → true,   "abcde", "caebd" → false,   "a", "a" → true
```

**Constraints**
* `1 <= s1.length <= 30`; `s2.length == s1.length`
''',
approach=r'''
**Recursion + memo.** `scr(a, b)`: equal strings are true; different letter counts are false. Otherwise try every split length `k`:
(`a[..k]` ~ `b[..k]` and `a[k..]` ~ `b[k..]`) or (`a[..k]` ~ `b[n-k..]` and `a[k..]` ~ `b[..n-k]`). Memoize on `(a, b)` in a `MyHashMap`.

* Time: **O(n⁴)** — O(n³) distinct substring pairs, each trying O(n) splits.
* Space: **O(n³)** — the memo.
''',
tc="n2", sc="n2",
java=r'''
public class ScrambleString {

    private final MyHashMap<String, Boolean> memo = new MyHashMap<>();

    public boolean isScramble(String s1, String s2) {
        if (s1.equals(s2)) return true;
        String key = s1 + "#" + s2;
        Boolean cached = memo.get(key);
        if (cached != null) return cached;
        int n = s1.length();
        int[] count = new int[26];
        for (int i = 0; i < n; i++) {
            count[s1.charAt(i) - 'a']++;
            count[s2.charAt(i) - 'a']--;
        }
        boolean result = false;
        for (int c : count) {
            if (c != 0) {
                memo.put(key, false);
                return false;
            }
        }
        for (int k = 1; k < n && !result; k++) {
            result = (isScramble(s1.substring(0, k), s2.substring(0, k)) && isScramble(s1.substring(k), s2.substring(k)))
                    || (isScramble(s1.substring(0, k), s2.substring(n - k)) && isScramble(s1.substring(k), s2.substring(0, n - k)));
        }
        memo.put(key, result);
        return result;
    }
}
''',
test=r'''
class ScrambleStringTest {

    @ParameterizedTest
    @CsvSource({"great,rgeat,true", "abcde,caebd,false", "a,a,true", "abcdbdacbdac,bdacabcdbdac,true"})
    void checks(String a, String b, boolean expected) {
        assertEquals(expected, new ScrambleString().isScramble(a, b));
    }
}
''',
trace=r'''
function run(s1, s2) {
  const memo = new Map(); const calls = [];
  const same = (a, b) => [...a].sort().join('') === [...b].sort().join('');
  const scr = (a, b) => {
    if (a === b) return true;
    const key = a + '#' + b; if (memo.has(key)) return memo.get(key);
    if (!same(a, b)) { memo.set(key, false); return false; }
    const n = a.length; let r = false;
    for (let k = 1; k < n && !r; k++) {
      const keep = scr(a.slice(0, k), b.slice(0, k)) && scr(a.slice(k), b.slice(k));
      const swap = !keep && scr(a.slice(0, k), b.slice(n - k)) && scr(a.slice(k), b.slice(0, n - k));
      r = keep || swap;
      if (n === s1.length || r) calls.push(`"${a}" | split ${k}: ${keep ? 'halves match in order' : swap ? 'halves match swapped' : 'no match'}`);
      if (r && n === s1.length) A.step(`Split "${a}" after ${k} letters: "${a.slice(0, k)}" + "${a.slice(k)}". ${keep ? 'Both halves are scrambles of the matching halves of s2.' : 'Swapped, the halves match s2.'}`, A.chars('s1', s1, { range: [0, k - 1] }), A.chars('s2', s2, keep ? { range: [0, k - 1] } : { range: [n - k, n - 1] }), A.arr('decisions', calls.slice(-6)));
    }
    memo.set(key, r); return r;
  };
  A.step('Try every split of s1. Each half must be a scramble of the matching part of s2, either in order or swapped. Letter counts prune early.', A.chars('s1', s1), A.chars('s2', s2));
  const res = scr(s1, s2);
  A.step(res ? 's2 is a scramble of s1.' : 'No split works.', A.vars({ memoEntries: memo.size }), A.text('Result', String(res), res ? 'ok' : 'bad'));
}
A.scenario('great → rgeat', 's1 = "great", s2 = "rgeat"', () => run('great', 'rgeat'));
'''),

P(num=89, slug="gray-code", title="Gray Code", diff="Medium", topic="Bit Manipulation", cls="GrayCode",
idea="The i-th Gray code is i XOR (i >> 1); consecutive codes differ in exactly one bit.",
vname="Formula i ^ (i >> 1)",
spec=r'''
Return any `n`-bit Gray code sequence: `2^n` integers starting at 0, each appearing once, where consecutive values (and the last and first)
differ in exactly one bit.

**Example**
```
n = 2 → [0,1,3,2],   n = 1 → [0,1]
```

**Constraints**
* `1 <= n <= 16`
''',
approach=r'''
**Binary-reflected Gray code.** `g(i) = i ^ (i >> 1)`. Going from `i` to `i + 1` flips a run of low bits; the XOR with the shifted value
cancels all but one of those flips.

* Time: **O(2ⁿ)** — one formula per code.
* Space: **O(1)** — apart from the output.
''',
tc="exp", sc="1",
java=r'''
public class GrayCode {

    public List<Integer> grayCode(int n) {
        List<Integer> out = new ArrayList<>();
        for (int i = 0; i < (1 << n); i++) out.add(i ^ (i >> 1));
        return out;
    }
}
''',
test=r'''
class GrayCodeTest {

    private final GrayCode solution = new GrayCode();

    @Test
    void examples() {
        assertEquals(List.of(0, 1, 3, 2), solution.grayCode(2));
        assertEquals(List.of(0, 1), solution.grayCode(1));
    }

    @Test
    void oneBitApart() {
        List<Integer> g = solution.grayCode(10);
        assertEquals(1024, new HashSet<>(g).size());
        for (int i = 0; i < g.size(); i++) assertEquals(1, Integer.bitCount(g.get(i) ^ g.get((i + 1) % g.size())));
    }
}
''',
trace=r'''
function run(n) {
  const rows = [];
  for (let i = 0; i < 1 << n; i++) {
    const g = i ^ (i >> 1), bits = g.toString(2).padStart(n, '0'), prev = rows.length ? rows[rows.length - 1] : null;
    rows.push(bits.split(''));
    const changed = prev ? prev.findIndex((c, t) => c !== bits[t]) : -1;
    A.step(`i = ${i}: ${i} XOR ${i >> 1} = ${g} (${bits}).${prev ? ` Only bit ${n - 1 - changed} changed.` : ''}`, A.grid('Gray codes', rows, { hl: changed >= 0 ? { [`${rows.length - 1},${changed}`]: 'ok' } : {} }));
  }
}
A.scenario('n = 3', 'eight codes', () => run(3));
'''),

P(num=93, slug="restore-ip-addresses", title="Restore IP Addresses", diff="Medium", topic="Backtracking", cls="RestoreIPAddresses",
idea="Choose 1–3 digits for each of the four parts, rejecting parts above 255 or with leading zeros.",
vname="Backtracking over four parts",
spec=r'''
Return every valid IPv4 address that can be formed by inserting three dots into the digit string `s` (no reordering or removal). A valid part
is 0–255 with no leading zeros.

**Example**
```
"25525511135" → ["255.255.11.135","255.255.111.35"]
"0000"        → ["0.0.0.0"]
"101023"      → ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

**Constraints**
* `1 <= s.length <= 20`
''',
approach=r'''
**Backtracking.** At part `p` from index `i`, try lengths 1–3; skip if not enough digits remain for the other parts, if the part has a
leading zero, or if it exceeds 255. After four parts, accept if all digits were used.

* Time: **O(1)** — at most 3⁴ = 81 combinations.
* Space: **O(1)** — four parts of recursion.
''',
tc="1", sc="1",
java=r'''
public class RestoreIPAddresses {

    public List<String> restoreIpAddresses(String s) {
        List<String> out = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), out);
        return out;
    }

    private void backtrack(String s, int i, List<String> parts, List<String> out) {
        if (parts.size() == 4) {
            if (i == s.length()) out.add(String.join(".", parts));
            return;
        }
        for (int len = 1; len <= 3 && i + len <= s.length(); len++) {
            String part = s.substring(i, i + len);
            if ((part.length() > 1 && part.charAt(0) == '0') || Integer.parseInt(part) > 255) break;
            parts.add(part);
            backtrack(s, i + len, parts, out);
            parts.removeLast();
        }
    }
}
''',
test=r'''
class RestoreIPAddressesTest {

    private final RestoreIPAddresses solution = new RestoreIPAddresses();

    @Test
    void examples() {
        assertEquals(List.of("255.255.11.135", "255.255.111.35"), solution.restoreIpAddresses("25525511135"));
        assertEquals(List.of("0.0.0.0"), solution.restoreIpAddresses("0000"));
        assertEquals(List.of("1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"), solution.restoreIpAddresses("101023"));
    }
}
''',
trace=r'''
function run(s) {
  const out = [], parts = [];
  (function bt(i) {
    if (parts.length === 4) { if (i === s.length) { out.push(parts.join('.')); A.step(`All four parts used every digit: ${parts.join('.')}.`, A.arr('parts', parts, { hl: { 0: 'ok', 1: 'ok', 2: 'ok', 3: 'ok' } }), A.arr('addresses', out)); } return; }
    for (let len = 1; len <= 3 && i + len <= s.length; len++) {
      const p = s.slice(i, i + len);
      if ((p.length > 1 && p[0] === '0') || +p > 255) { A.step(`"${p}" is not a valid part (${p[0] === '0' ? 'leading zero' : 'above 255'}).`, A.chars('s', s, { range: [i, i + len - 1], hl: { [i]: 'bad' } }), A.arr('parts', parts)); break; }
      parts.push(p); bt(i + len); parts.pop();
    }
  })(0);
  A.step(`${out.length} valid address${out.length === 1 ? '' : 'es'}.`, A.arr('addresses', out));
}
A.scenario('Classic', 's = "25525511135"', () => run('25525511135'));
'''),

P(num=95, slug="unique-binary-search-trees-ii", title="Unique Binary Search Trees II", diff="Medium", topic="Backtracking", cls="UniqueBSTsII",
idea="For each root r, combine every left tree built from smaller values with every right tree built from larger ones.",
vname="Recursive generation",
spec=r'''
Return all structurally unique BSTs that store exactly the values `1..n`, in any order.

**Example**
```
n = 3 → 5 trees: [1,null,2,null,3], [1,null,3,2], [2,1,3], [3,1,null,null,2], [3,2,null,1]
```

**Constraints**
* `1 <= n <= 8`
''',
approach=r'''
**Divide by the root.** `build(lo, hi)` returns all BSTs of `lo..hi`: for each root `r`, pair every tree of `build(lo, r-1)` with every tree of
`build(r+1, hi)` (subtrees are shared between results, which is fine because they are never modified).

* Time: **O(n · Cₙ)** — Cₙ (the n-th Catalan number) trees, each assembled with O(n) work.
* Space: **O(n · Cₙ)** — the trees produced.
''',
tc="exp", sc="exp",
helpers=["TreeNode"],
java=r'''
public class UniqueBSTsII {

    public List<TreeNode> generateTrees(int n) {
        return build(1, n);
    }

    private List<TreeNode> build(int lo, int hi) {
        List<TreeNode> out = new ArrayList<>();
        if (lo > hi) {
            out.add(null);
            return out;
        }
        for (int r = lo; r <= hi; r++) {
            for (TreeNode left : build(lo, r - 1)) {
                for (TreeNode right : build(r + 1, hi)) out.add(new TreeNode(r, left, right));
            }
        }
        return out;
    }
}
''',
test=r'''
class UniqueBSTsIITest {

    private final UniqueBSTsII solution = new UniqueBSTsII();

    @Test
    void three() {
        Set<List<Integer>> shapes = new HashSet<>();
        for (TreeNode t : solution.generateTrees(3)) shapes.add(TreeNode.toList(t));
        assertEquals(Set.of(Arrays.asList(1, null, 2, null, 3), Arrays.asList(1, null, 3, 2), Arrays.asList(2, 1, 3),
                Arrays.asList(3, 1, null, null, 2), Arrays.asList(3, 2, null, 1)), shapes);
    }

    @Test
    void catalanCounts() {
        assertEquals(1, solution.generateTrees(1).size());
        assertEquals(14, solution.generateTrees(4).size());
    }
}
''',
trace=r'''
function run(n) {
  const build = (lo, hi) => { if (lo > hi) return [null]; const out = []; for (let r = lo; r <= hi; r++) for (const l of build(lo, r - 1)) for (const rt of build(r + 1, hi)) out.push({ val: r, left: l, right: rt }); return out; };
  const trees = build(1, n);
  let seq = 0; const copy = t => (t ? { val: t.val, id: seq++, left: copy(t.left), right: copy(t.right) } : null);
  A.step(`Every value 1..${n} takes a turn as the root; smaller values form the left subtree and larger ones the right.`, A.vars({ trees: trees.length }));
  trees.forEach((t, i) => A.step(`Tree ${i + 1} of ${trees.length}: root ${t.val}.`, A.tree(`tree ${i + 1}`, copy(t), { hl: { [seq - (function c(x) { return x ? 1 + c(x.left) + c(x.right) : 0; })(t)]: 'cur' } })));
}
A.scenario('n = 3', 'five trees', () => run(3));
'''),
]
