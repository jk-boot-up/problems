PROBLEMS = [
P(num=9, slug="palindrome-number", title="Palindrome Number", diff="Easy", topic="Math", cls="PalindromeNumber",
idea="Reverse only the lower half of the digits and compare it with the upper half; no overflow, no strings.",
vname="Reverse half the digits",
spec=r'''
Return `true` if the integer `x` reads the same forward and backward.

**Example**
```
121 → true,   -121 → false (reads 121-),   10 → false
```

**Constraints**
* `-2^31 <= x <= 2^31 - 1`

**Follow-up:** solve it without converting to a string.
''',
approach=r'''
**Half reversal.** Negative numbers and numbers ending in 0 (except 0) are not palindromes. Pop digits from `x` onto `rev` while
`x > rev`. Then `x == rev` (even length) or `x == rev / 10` (odd length, the middle digit sits in `rev`).

* Time: **O(log n)** — half of the digits are processed.
* Space: **O(1)** — two ints.
''',
tc="log",
java=r'''
public class PalindromeNumber {

    public boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;
        int rev = 0;
        while (x > rev) {
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return x == rev || x == rev / 10;
    }
}
''',
test=r'''
class PalindromeNumberTest {

    private final PalindromeNumber solution = new PalindromeNumber();

    @ParameterizedTest
    @CsvSource({"121,true", "-121,false", "10,false", "0,true", "1221,true", "12321,true", "2147483647,false"})
    void checks(int x, boolean expected) {
        assertEquals(expected, solution.isPalindrome(x));
    }
}
''',
trace=r'''
function run(x) {
  const orig = x;
  A.step('First, two quick checks: a negative number, or a number ending in 0 (other than 0 itself), can never be a palindrome.', A.chars('x', String(x)));
  if (x < 0 || (x % 10 === 0 && x !== 0)) { A.step(x < 0 ? 'A negative number has a minus sign on only one end, so it is not a palindrome.' : 'It ends in 0 but does not start with 0, so it is not a palindrome.', A.chars('x', String(x)), A.text('Result', 'false', 'bad')); return; }
  let rev = 0;
  A.step('Move digits from the end of x onto rev until rev has caught up with x.', A.chars('x', String(x)), A.vars({ x, rev }));
  while (x > rev) { const d = x % 10; rev = rev * 10 + d; x = Math.floor(x / 10); A.step(`Pop digit ${d}: x = ${x}, rev = ${rev}.`, A.chars('x', String(x)), A.chars('rev', String(rev), { hl: { [String(rev).length - 1]: 'ok' } }), A.vars({ x, rev })); }
  const ok = x === rev || x === Math.floor(rev / 10);
  A.step(x === rev ? `x and rev are both ${x}: an even-length palindrome.` : x === Math.floor(rev / 10) ? `Dropping the middle digit from rev gives ${Math.floor(rev / 10)}, which equals x: an odd-length palindrome.` : `${x} does not match ${rev}: not a palindrome.`, A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('Odd length', 'x = 12321', () => run(12321));
A.scenario('Not a palindrome', 'x = 1231', () => run(1231));
A.scenario('Edge: negative', 'x = -121', () => run(-121));
''',
variants=[dict(
name="Compare as a string",
idea="Convert to a string and compare characters from both ends.",
approach=r'''
**String two pointers.** `String.valueOf(x)`, then compare `s[i]` with `s[n-1-i]`.

* Time: **O(log n)** — the string has about log₁₀ n characters.
* Space: **O(log n)** — the string.
''',
tc="log", sc="log",
java=r'''
public class PalindromeNumber {

    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) return false;
        }
        return true;
    }
}
''',
trace=r'''
function run(x) {
  const s = String(x);
  for (let i = 0, j = s.length - 1; i < j; i++, j--) {
    const ok = s[i] === s[j];
    A.step(`'${s[i]}' vs '${s[j]}': ${ok ? 'match' : 'mismatch'}.`, A.chars('x as text', s, { hl: { [i]: ok ? 'ok' : 'bad', [j]: ok ? 'ok' : 'bad' } }));
    if (!ok) { A.step('Not a palindrome.', A.text('Result', 'false', 'bad')); return; }
  }
  A.step('All pairs matched.', A.text('Result', 'true', 'ok'));
}
A.scenario('Odd length', 'x = 12321', () => run(12321));
''')]),

P(num=66, slug="plus-one", title="Plus One", diff="Easy", topic="Math", cls="PlusOne",
idea="Add one from the right: 9s turn into 0s and carry; the first non-9 just increments.",
vname="Carry from the right",
spec=r'''
A large integer is given as an array of `digits` (most significant first, no leading zeros). Add one and return the resulting digits.

**Example**
```
[1,2,3] → [1,2,4],   [4,3,2,1] → [4,3,2,2],   [9] → [1,0]
```

**Constraints**
* `1 <= digits.length <= 100`; `0 <= digits[i] <= 9`
''',
approach=r'''
**Right-to-left.** From the last digit: if it is below 9, increment and return. Otherwise set it to 0 and continue left. If every digit
was 9, the answer is `1` followed by zeros.

* Time: **O(n)** — at most one pass.
* Space: **O(1)** — in place, except when a new leading digit is needed.
''',
java=r'''
public class PlusOne {

    public int[] plusOne(int[] digits) {
        int[] d = digits.clone();
        for (int i = d.length - 1; i >= 0; i--) {
            if (d[i] < 9) {
                d[i]++;
                return d;
            }
            d[i] = 0;
        }
        int[] out = new int[d.length + 1];
        out[0] = 1;
        return out;
    }
}
''',
test=r'''
class PlusOneTest {

    private final PlusOne solution = new PlusOne();

    @Test
    void simple() {
        assertArrayEquals(new int[]{1, 2, 4}, solution.plusOne(new int[]{1, 2, 3}));
    }

    @Test
    void carry() {
        assertArrayEquals(new int[]{1, 3, 0, 0}, solution.plusOne(new int[]{1, 2, 9, 9}));
    }

    @Test
    void allNines() {
        assertArrayEquals(new int[]{1, 0, 0}, solution.plusOne(new int[]{9, 9}));
    }
}
''',
trace=r'''
function run(digits) {
  const d = digits.slice();
  A.step('Add one starting from the last digit.', A.arr('digits', d));
  for (let i = d.length - 1; i >= 0; i--) {
    if (d[i] < 9) { d[i]++; A.step(`${d[i] - 1} + 1 = ${d[i]}. No carry, so we are done.`, A.arr('digits', d, { hl: { [i]: 'ok' } }), A.text('Result', JSON.stringify(d), 'ok')); return; }
    d[i] = 0; A.step('9 + 1 = 10: write 0 and carry 1 to the left.', A.arr('digits', d, { hl: { [i]: 'alt' } }));
  }
  const out = [1, ...d];
  A.step('Every digit was 9, so a new leading 1 is needed.', A.arr('digits', out, { hl: { 0: 'ok' } }), A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Carry', 'digits = [1,2,9,9]', () => run([1, 2, 9, 9]));
A.scenario('Edge: all nines', 'digits = [9,9,9]', () => run([9, 9, 9]));
'''),

P(num=172, slug="factorial-trailing-zeroes", title="Factorial Trailing Zeroes", diff="Medium", topic="Math", cls="FactorialTrailingZeroes",
idea="Each trailing zero needs a factor 10 = 2 × 5, and 5s are the scarce factor, so count the 5s in n!.",
vname="Count factors of five",
spec=r'''
Return the number of trailing zeroes in `n!`.

**Example**
```
3 → 0 (6),   5 → 1 (120),   0 → 0,   25 → 6
```

**Constraints**
* `0 <= n <= 10^4`

**Follow-up:** logarithmic time.
''',
approach=r'''
**Legendre's formula for 5.** Multiples of 5 contribute one factor of 5, multiples of 25 another, multiples of 125 another, and so on:
the answer is `n/5 + n/25 + n/125 + …`, computed by repeatedly dividing by 5.

* Time: **O(log n)** — about log₅ n divisions.
* Space: **O(1)** — a counter.
''',
tc="log",
java=r'''
public class FactorialTrailingZeroes {

    public int trailingZeroes(int n) {
        int count = 0;
        while (n > 0) {
            n /= 5;
            count += n;
        }
        return count;
    }
}
''',
test=r'''
class FactorialTrailingZeroesTest {

    private final FactorialTrailingZeroes solution = new FactorialTrailingZeroes();

    @ParameterizedTest
    @CsvSource({"3,0", "5,1", "0,0", "25,6", "100,24", "10000,2499"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.trailingZeroes(n));
    }
}
''',
trace=r'''
function run(n) {
  const nums = [...Array(n)].map((_, i) => i + 1);
  const fives = k => { let c = 0; while (k % 5 === 0) { c++; k /= 5; } return c; };
  A.step(`${n}! = 1 × 2 × … × ${n}. A trailing zero needs a factor 2 × 5; factors of 2 are plentiful, so count the 5s.`, A.arr('factors', nums, { noIdx: true, hl: Object.fromEntries(nums.map((v, i) => [i, fives(v) ? (fives(v) > 1 ? 'alt' : 'sel') : 'dim'])) }));
  let count = 0, m = n, p = 5;
  while (m > 0) { m = Math.floor(m / 5); count += m; A.step(`${n} ÷ ${p} = ${m} number${m === 1 ? '' : 's'} contribute a factor of 5 at this level. Total: ${count}.`, A.arr('factors', nums, { noIdx: true, hl: Object.fromEntries(nums.map((v, i) => [i, v % p === 0 ? 'ok' : 'dim'])) }), A.vars({ count })); p *= 5; }
  A.step(`${n}! ends with ${count} zero${count === 1 ? '' : 's'}.`, A.text('Result', count, 'ok'));
}
A.scenario('n = 25', '25 contributes two fives', () => run(25));
'''),

P(num=69, slug="sqrtx", title="Sqrt(x)", diff="Easy", topic="Math", cls="SqrtX",
idea="Newton's method: repeatedly average r with x / r; it converges quickly to the integer square root.",
vname="Newton's method",
spec=r'''
Given a non-negative integer `x`, return the square root of `x` rounded **down** to an integer, without using built-in power or square
root functions.

**Example**
```
4 → 2,   8 → 2 (2.828…)
```

**Constraints**
* `0 <= x <= 2^31 - 1`
''',
approach=r'''
**Integer Newton iteration.** Start with `r = x` and repeat `r = (r + x / r) / 2` while `r * r > x` (using `long`). The sequence only
decreases and stops at the floor of √x.

* Time: **O(log x)** — Newton's method roughly doubles the number of correct digits per step.
* Space: **O(1)** — one long.
''',
tc="log",
java=r'''
public class SqrtX {

    public int mySqrt(int x) {
        long r = x;
        while (r * r > x) {
            r = (r + x / r) / 2;
        }
        return (int) r;
    }
}
''',
test=r'''
class SqrtXTest {

    private final SqrtX solution = new SqrtX();

    @ParameterizedTest
    @CsvSource({"0,0", "1,1", "4,2", "8,2", "15,3", "16,4", "2147395599,46339", "2147483647,46340"})
    void roots(int x, int expected) {
        assertEquals(expected, solution.mySqrt(x));
    }
}
''',
trace=r'''
function run(x) {
  let r = x, step = 0;
  A.step(`Start with r = ${x}. Each step averages r and x / r, which pulls r toward √${x}.`, A.vars({ x, r, 'r²': r * r }));
  while (r * r > x) { const nr = Math.floor((r + Math.floor(x / r)) / 2); step++; A.step(`Step ${step}: (${r} + ${x} ÷ ${r}) / 2 = ${nr}. Then r² = ${nr * nr}.`, A.vars({ x, r: nr, 'r²': nr * nr })); r = nr; }
  A.step(`r² = ${r * r} ≤ ${x} < (r + 1)² = ${(r + 1) * (r + 1)}, so the answer is ${r}.`, A.text('Result', r, 'ok'));
}
A.scenario('x = 200', '√200 ≈ 14.14', () => run(200));
A.scenario('x = 8', '√8 ≈ 2.83', () => run(8));
''',
variants=[dict(
name="Binary search",
idea="Search for the largest m with m × m ≤ x.",
approach=r'''
**Binary search on the answer.** Search `[0, x]`; if `mid * mid <= x` (as `long`), the answer is at least `mid`.

* Time: **O(log x)** — the range halves each step.
* Space: **O(1)** — a few longs.
''',
tc="log",
java=r'''
public class SqrtX {

    public int mySqrt(int x) {
        long lo = 0, hi = x;
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2;
            if (mid * mid <= x) lo = mid; else hi = mid - 1;
        }
        return (int) lo;
    }
}
''',
trace=r'''
function run(x) {
  let lo = 0, hi = x;
  while (lo < hi) { const mid = Math.floor((lo + hi + 1) / 2), ok = mid * mid <= x; A.step(`mid = ${mid}: ${mid}² = ${mid * mid} ${ok ? '≤' : '>'} ${x}, so ${ok ? 'the answer is at least ' + mid : 'the answer is below ' + mid}.`, A.vars({ lo, hi, mid })); if (ok) lo = mid; else hi = mid - 1; }
  A.step(`The answer is ${lo}.`, A.text('Result', lo, 'ok'));
}
A.scenario('x = 200', '√200 ≈ 14.14', () => run(200));
''')]),

P(num=50, slug="powx-n", title="Pow(x, n)", diff="Medium", topic="Math", cls="PowXN",
idea="Square the base and halve the exponent: each set bit of n multiplies one squared power into the result.",
vname="Iterative binary exponentiation",
spec=r'''
Implement `pow(x, n)`: `x` raised to the integer power `n` (which may be negative).

**Example**
```
pow(2.0, 10) = 1024.0,   pow(2.1, 3) = 9.261,   pow(2.0, -2) = 0.25
```

**Constraints**
* `-100.0 < x < 100.0`; `-2^31 <= n <= 2^31 - 1`; the result fits in a double.
''',
approach=r'''
**Exponentiation by squaring.** Use `long e = n` (so `-Integer.MIN_VALUE` does not overflow); if negative, use `1/x` and `-e`.
While `e > 0`: if its lowest bit is set, multiply the result by the current base; square the base; shift `e` right.

* Time: **O(log n)** — one step per bit of n.
* Space: **O(1)** — a few variables.
''',
tc="log",
java=r'''
public class PowXN {

    public double myPow(double x, int n) {
        long e = n;
        if (e < 0) {
            x = 1 / x;
            e = -e;
        }
        double result = 1;
        while (e > 0) {
            if ((e & 1) == 1) result *= x;
            x *= x;
            e >>= 1;
        }
        return result;
    }
}
''',
test=r'''
class PowXNTest {

    private final PowXN solution = new PowXN();

    @Test
    void examples() {
        assertEquals(1024.0, solution.myPow(2.0, 10), 1e-9);
        assertEquals(9.261, solution.myPow(2.1, 3), 1e-9);
        assertEquals(0.25, solution.myPow(2.0, -2), 1e-12);
    }

    @Test
    void extremes() {
        assertEquals(1.0, solution.myPow(1.0, Integer.MIN_VALUE));
        assertEquals(0.0, solution.myPow(2.0, Integer.MIN_VALUE));
        assertEquals(1.0, solution.myPow(5.0, 0));
    }
}
''',
trace=r'''
function run(x, n) {
  let e = n, base = x, res = 1;
  const bits = e.toString(2).split('');
  A.step(`${x}^${n}: write ${n} in binary (${e.toString(2)}). Each 1-bit multiplies in one squared power of ${x}.`, A.arr('bits of n', bits, { noIdx: true }), A.vars({ result: res, base }));
  let k = 0;
  while (e > 0) {
    const on = e & 1;
    if (on) res *= base;
    A.step(`Bit ${k} is ${on}. ${on ? `Multiply result by base ${base}: result = ${res}.` : 'Skip.'} Then square the base: ${base} → ${base * base}.`, A.arr('bits of n', bits, { noIdx: true, hl: { [bits.length - 1 - k]: on ? 'ok' : 'dim' } }), A.vars({ result: res, base: base * base }));
    base *= base; e >>= 1; k++;
  }
  A.step(`${x}^${n} = ${res}, using ${k} squarings instead of ${n - 1} multiplications.`, A.text('Result', res, 'ok'));
}
A.scenario('2^10', 'x = 2, n = 10', () => run(2, 10));
A.scenario('3^13', 'x = 3, n = 13', () => run(3, 13));
''',
variants=[dict(
name="Recursive fast power",
idea="xⁿ = (x^(n/2))², times x when n is odd.",
approach=r'''
**Divide and conquer.** `pow(x, n) = half * half` (times `x` if `n` is odd), where `half = pow(x, n / 2)`.

* Time: **O(log n)** — the exponent halves each call.
* Space: **O(log n)** — the recursion depth.
''',
tc="log", sc="log",
java=r'''
public class PowXN {

    public double myPow(double x, int n) {
        long e = n;
        return e < 0 ? 1 / power(x, -e) : power(x, e);
    }

    private double power(double x, long e) {
        if (e == 0) return 1;
        double half = power(x, e / 2);
        return e % 2 == 0 ? half * half : half * half * x;
    }
}
''',
trace=r'''
function run(x, n) {
  const calls = [];
  const p = e => { calls.push(`pow(${x}, ${e})`); A.step(`Call pow(${x}, ${e}).`, A.stack('calls', calls)); if (e === 0) { calls.pop(); return 1; } const h = p(Math.floor(e / 2)); const r = e % 2 ? h * h * x : h * h; calls.pop(); A.step(`pow(${x}, ${e}) = ${h}²${e % 2 ? ` × ${x}` : ''} = ${r}.`, A.stack('calls', calls), A.vars({ result: r })); return r; };
  A.step(`Result: ${p(n)}.`, A.text('Result', Math.pow(x, n), 'ok'));
}
A.scenario('2^10', 'x = 2, n = 10', () => run(2, 10));
''')]),

P(num=149, slug="max-points-on-a-line", title="Max Points on a Line", diff="Hard", topic="Math", cls="MaxPointsOnALine",
idea="Fix each point and count the others by exact slope (a reduced fraction) in a hash map.",
vname="Slope counting per anchor",
spec=r'''
Given an array of distinct `points[i] = [x, y]`, return the maximum number of points that lie on the same straight line.

**Example**
```
[[1,1],[2,2],[3,3]] → 3
[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] → 4
```

**Constraints**
* `1 <= points.length <= 300`; `-10^4 <= x, y <= 10^4`; all points are distinct.
''',
approach=r'''
**Exact slopes.** For each anchor point `i`, compute `dx, dy` to every later point, divide both by `gcd(|dx|, |dy|)` and normalize the
sign (so `(1,2)` and `(-1,-2)` match, and vertical lines become `(0,1)`). Count slopes in a `MyHashMap`; the best line through `i`
has `1 + max count` points. Using fractions avoids floating-point errors.

* Time: **O(n² log C)** — n²/2 pairs, each with a gcd on coordinates up to C.
* Space: **O(n)** — the slope map for one anchor.
''',
tc="n2", sc="n",
java=r'''
public class MaxPointsOnALine {

    public int maxPoints(int[][] points) {
        int n = points.length, best = 1;
        for (int i = 0; i < n; i++) {
            MyHashMap<Long, Integer> slopes = new MyHashMap<>();
            for (int j = i + 1; j < n; j++) {
                int dx = points[j][0] - points[i][0], dy = points[j][1] - points[i][1];
                int g = gcd(Math.abs(dx), Math.abs(dy));
                dx /= g;
                dy /= g;
                if (dx < 0 || (dx == 0 && dy < 0)) {
                    dx = -dx;
                    dy = -dy;
                }
                long key = ((long) dx << 32) | (dy & 0xffffffffL);
                best = Math.max(best, 1 + slopes.merge(key, 1, Integer::sum));
            }
        }
        return best;
    }

    private static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
''',
test=r'''
class MaxPointsOnALineTest {

    private final MaxPointsOnALine solution = new MaxPointsOnALine();

    @Test
    void diagonal() {
        assertEquals(3, solution.maxPoints(new int[][]{{1, 1}, {2, 2}, {3, 3}}));
    }

    @Test
    void mixed() {
        assertEquals(4, solution.maxPoints(new int[][]{{1, 1}, {3, 2}, {5, 3}, {4, 1}, {2, 3}, {1, 4}}));
    }

    @Test
    void verticalAndSingle() {
        assertEquals(3, solution.maxPoints(new int[][]{{0, 0}, {0, 5}, {0, -3}, {1, 1}}));
        assertEquals(1, solution.maxPoints(new int[][]{{7, 7}}));
    }
}
''',
trace=r'''
function run(pts) {
  const gcd = (a, b) => (b ? gcd(b, a % b) : a);
  const nodes = pts.map(([x, y], i) => ({ id: i, label: `${x},${y}`, x: 40 + x * 55, y: 300 - y * 55 }));
  let best = 1, bestEdges = [];
  A.step('Fix one point at a time and group the others by the exact slope from it.', A.graph('points', nodes, []));
  for (let i = 0; i < pts.length; i++) {
    const m = new Map(), groups = new Map();
    for (let j = i + 1; j < pts.length; j++) {
      let dx = pts[j][0] - pts[i][0], dy = pts[j][1] - pts[i][1]; const g = gcd(Math.abs(dx), Math.abs(dy)); dx /= g; dy /= g;
      if (dx < 0 || (dx === 0 && dy < 0)) { dx = -dx; dy = -dy; }
      const key = `${dy}/${dx}`; m.set(key, (m.get(key) || 0) + 1); (groups.get(key) || groups.set(key, []).get(key)).push(j);
    }
    if (!m.size) continue;
    const [bk, bc] = [...m].sort((a, b) => b[1] - a[1])[0];
    if (bc + 1 > best) { best = bc + 1; bestEdges = groups.get(bk).map(j => [i, j, '', 'ok']); }
    A.step(`Anchor (${pts[i]}): the most common slope is ${bk}, shared by ${bc} other point${bc > 1 ? 's' : ''}, giving a line of ${bc + 1}. Best so far: ${best}.`, A.graph('points', nodes, groups.get(bk).map(j => [i, j, '', 'cur']), { hl: { [i]: 'cur', ...Object.fromEntries(groups.get(bk).map(j => [j, 'sel'])) } }), A.hashTable('slope → count', m, { hl: bk }));
  }
  A.step(`At most ${best} points lie on one line.`, A.graph('points', nodes, bestEdges), A.text('Result', best, 'ok'));
}
A.scenario('Six points', '[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]', () => run([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]));
'''),

P(num=70, slug="climbing-stairs", title="Climbing Stairs", diff="Easy", topic="1D DP", cls="ClimbingStairs",
idea="ways(n) = ways(n − 1) + ways(n − 2): the last move was either one step or two.",
vname="Two rolling variables",
spec=r'''
You climb a staircase of `n` steps, taking 1 or 2 steps at a time. In how many distinct ways can you reach the top?

**Example**
```
n = 2 → 2 (1+1, 2),   n = 3 → 3 (1+1+1, 1+2, 2+1)
```

**Constraints**
* `1 <= n <= 45`
''',
approach=r'''
**Fibonacci recurrence.** `ways(1) = 1`, `ways(2) = 2`, and `ways(i) = ways(i-1) + ways(i-2)`. Only the last two values are needed.

* Time: **O(n)** — one loop.
* Space: **O(1)** — two variables.
''',
java=r'''
public class ClimbingStairs {

    public int climbStairs(int n) {
        int a = 1, b = 1; // ways to reach step i-2 and i-1
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}
''',
test=r'''
class ClimbingStairsTest {

    private final ClimbingStairs solution = new ClimbingStairs();

    @ParameterizedTest
    @CsvSource({"1,1", "2,2", "3,3", "5,8", "45,1836311903"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.climbStairs(n));
    }
}
''',
trace=r'''
function run(n) {
  const ways = [1, 1];
  A.step('There is 1 way to stand on step 0 and 1 way to reach step 1. Each later step is reached from one or two steps below.', A.arr('ways', ways));
  for (let i = 2; i <= n; i++) { ways.push(ways[i - 1] + ways[i - 2]); A.step(`ways[${i}] = ways[${i - 1}] + ways[${i - 2}] = ${ways[i - 1]} + ${ways[i - 2]} = ${ways[i]}.`, A.arr('ways', ways, { hl: { [i]: 'ok', [i - 1]: 'sel', [i - 2]: 'sel' } })); }
  A.step(`There are ${ways[n]} ways to climb ${n} steps. Only the last two values were ever needed.`, A.text('Result', ways[n], 'ok'));
}
A.scenario('n = 6', 'six steps', () => run(6));
''',
variants=[dict(
name="Memoized recursion",
idea="Recurse on n − 1 and n − 2, caching each answer so it is computed only once.",
approach=r'''
**Top-down with a memo array.** `ways(n) = ways(n-1) + ways(n-2)`, storing results in `memo[n]`.

* Time: **O(n)** — each n is computed once.
* Space: **O(n)** — the memo array and the recursion stack.
''',
sc="n",
java=r'''
public class ClimbingStairs {

    public int climbStairs(int n) {
        return ways(n, new int[n + 1]);
    }

    private int ways(int n, int[] memo) {
        if (n <= 1) return 1;
        if (memo[n] == 0) memo[n] = ways(n - 1, memo) + ways(n - 2, memo);
        return memo[n];
    }
}
''',
trace=r'''
function run(n) {
  const memo = new Array(n + 1).fill(''), calls = [];
  const ways = k => { if (k <= 1) return 1; if (memo[k] !== '') { A.step(`ways(${k}) is cached: ${memo[k]}.`, A.arr('memo', memo, { hl: { [k]: 'alt' } }), A.stack('calls', calls)); return memo[k]; } calls.push(`ways(${k})`); const r = ways(k - 1) + ways(k - 2); memo[k] = r; calls.pop(); A.step(`ways(${k}) = ${r}. Store it.`, A.arr('memo', memo, { hl: { [k]: 'ok' } }), A.stack('calls', calls)); return r; };
  A.step(`Answer: ${ways(n)}.`, A.text('Result', memo[n], 'ok'));
}
A.scenario('n = 5', 'five steps', () => run(5));
''')]),

P(num=198, slug="house-robber", title="House Robber", diff="Medium", topic="1D DP", cls="HouseRobber",
idea="At each house: either rob it (plus the best up to two houses back) or skip it (keep the best up to the previous house).",
vname="Two rolling variables",
spec=r'''
Houses along a street hold `nums[i]` money. You cannot rob two **adjacent** houses. Return the maximum amount you can rob.

**Example**
```
[1,2,3,1] → 4 (1 + 3),   [2,7,9,3,1] → 12 (2 + 9 + 1)
```

**Constraints**
* `1 <= nums.length <= 100`; `0 <= nums[i] <= 400`
''',
approach=r'''
**DP.** `best(i) = max(best(i-1), best(i-2) + nums[i])`. Keep only `prev2` and `prev1`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two variables.
''',
java=r'''
public class HouseRobber {

    public int rob(int[] nums) {
        int prev2 = 0, prev1 = 0;
        for (int x : nums) {
            int cur = Math.max(prev1, prev2 + x);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}
''',
test=r'''
class HouseRobberTest {

    private final HouseRobber solution = new HouseRobber();

    @Test
    void examples() {
        assertEquals(4, solution.rob(new int[]{1, 2, 3, 1}));
        assertEquals(12, solution.rob(new int[]{2, 7, 9, 3, 1}));
    }

    @Test
    void skipTwo() {
        assertEquals(4, solution.rob(new int[]{2, 1, 1, 2}));
    }

    @Test
    void single() {
        assertEquals(5, solution.rob(new int[]{5}));
    }
}
''',
trace=r'''
function run(a) {
  const best = [];
  A.step('best[i] is the most money from houses 0..i. At each house, either skip it or rob it plus best[i − 2].', A.arr('houses', a), A.arr('best', best));
  a.forEach((x, i) => {
    const skip = i ? best[i - 1] : 0, take = (i > 1 ? best[i - 2] : 0) + x;
    best.push(Math.max(skip, take));
    A.step(`House ${i} (${x}): skip it for ${skip}, or rob it for ${i > 1 ? best[i - 2] : 0} + ${x} = ${take}. Best: ${best[i]}.`, A.arr('houses', a, { hl: { [i]: take >= skip ? 'ok' : 'dim' } }), A.arr('best', best, { hl: { [i]: 'cur', ...(i ? { [i - 1]: 'sel' } : {}), ...(i > 1 ? { [i - 2]: 'alt' } : {}) } }));
  });
  A.step(`The maximum is ${best[best.length - 1]}.`, A.text('Result', best[best.length - 1], 'ok'));
}
A.scenario('Five houses', 'nums = [2,7,9,3,1]', () => run([2, 7, 9, 3, 1]));
A.scenario('Skip two in a row', 'nums = [2,1,1,2]', () => run([2, 1, 1, 2]));
''',
variants=[dict(
name="DP table",
idea="Fill dp[i] = max(dp[i−1], dp[i−2] + nums[i]) in an array.",
approach=r'''
**Full table.** Same recurrence, but every `dp[i]` is stored.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the dp array.
''',
sc="n",
java=r'''
public class HouseRobber {

    public int rob(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n + 1]; // dp[i] = best using the first i houses
        dp[1] = nums[0];
        for (int i = 2; i <= n; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i - 1]);
        }
        return dp[n];
    }
}
''',
trace=r'''
function run(a) {
  const dp = [0, a[0]];
  for (let i = 2; i <= a.length; i++) { dp.push(Math.max(dp[i - 1], dp[i - 2] + a[i - 1])); A.step(`dp[${i}] = max(${dp[i - 1]}, ${dp[i - 2]} + ${a[i - 1]}) = ${dp[i]}.`, A.arr('dp', dp, { hl: { [i]: 'ok' } })); }
  A.step(`Answer: ${dp[a.length]}. The table needs O(n) space.`, A.text('Result', dp[a.length], 'ok'));
}
A.scenario('Five houses', 'nums = [2,7,9,3,1]', () => run([2, 7, 9, 3, 1]));
''')]),

P(num=139, slug="word-break", title="Word Break", diff="Medium", topic="1D DP", cls="WordBreak",
idea="ok[i] is true when the first i characters split into words: some earlier ok[j] plus a dictionary word s[j..i).",
vname="DP over prefixes",
spec=r'''
Return `true` if `s` can be split into a sequence of one or more words from `wordDict` (words may be reused).

**Example**
```
s = "leetcode", wordDict = ["leet","code"]            → true
s = "applepenapple", wordDict = ["apple","pen"]       → true
s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] → false
```

**Constraints**
* `1 <= s.length <= 300`; `1 <= wordDict.length <= 1000`; `1 <= wordDict[i].length <= 20`
''',
approach=r'''
**Prefix DP.** `ok[0] = true`. For each end `i`, look back at most `maxLen` characters: `ok[i]` is true if some `ok[j]` is true and
`s.substring(j, i)` is in the dictionary (a `MyHashSet`).

* Time: **O(n · L²)** — n ends × up to L starts × O(L) substring hashing (L = longest word).
* Space: **O(n + D)** — the dp array and the dictionary set.
''',
tc="n", sc="n",
java=r'''
public class WordBreak {

    public boolean wordBreak(String s, List<String> wordDict) {
        MyHashSet<String> words = new MyHashSet<>();
        int maxLen = 0;
        for (String w : wordDict) {
            words.add(w);
            maxLen = Math.max(maxLen, w.length());
        }
        boolean[] ok = new boolean[s.length() + 1];
        ok[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = i - 1; j >= Math.max(0, i - maxLen); j--) {
                if (ok[j] && words.contains(s.substring(j, i))) {
                    ok[i] = true;
                    break;
                }
            }
        }
        return ok[s.length()];
    }
}
''',
test=r'''
class WordBreakTest {

    private final WordBreak solution = new WordBreak();

    @Test
    void examples() {
        assertTrue(solution.wordBreak("leetcode", List.of("leet", "code")));
        assertTrue(solution.wordBreak("applepenapple", List.of("apple", "pen")));
        assertFalse(solution.wordBreak("catsandog", List.of("cats", "dog", "sand", "and", "cat")));
    }

    @Test
    void longRepeated() {
        assertFalse(solution.wordBreak("a".repeat(150) + "b", List.of("a", "aa", "aaa", "aaaa")));
    }
}
''',
trace=r'''
function run(s, dict) {
  const words = new Set(dict), ok = [true, ...new Array(s.length).fill(false)], from = [];
  A.step('ok[i] means the first i characters can be split into words. ok[0] is true: the empty prefix.', A.chars('s', s), A.arr('ok', ok.map(v => (v ? 'T' : 'F'))), A.hashTable('dictionary', words));
  for (let i = 1; i <= s.length; i++) {
    for (let j = i - 1; j >= 0; j--) if (ok[j] && words.has(s.slice(j, i))) { ok[i] = true; from[i] = j; break; }
    const hl = {}; if (ok[i]) for (let t = from[i]; t < i; t++) hl[t] = 'ok';
    A.step(ok[i] ? `ok[${i}] is true: ok[${from[i]}] holds and "${s.slice(from[i], i)}" is a word.` : `ok[${i}] is false: no word ends here after a valid split.`, A.chars('s', s, { hl, range: [0, i - 1] }), A.arr('ok', ok.map(v => (v ? 'T' : 'F')), { hl: { [i]: ok[i] ? 'ok' : 'bad', ...(ok[i] ? { [from[i]]: 'sel' } : {}) } }));
  }
  A.step(`ok[${s.length}] = ${ok[s.length]}.`, A.text('Result', String(ok[s.length]), ok[s.length] ? 'ok' : 'bad'));
}
A.scenario('Splits', 's = "applepenapple"', () => run('applepenapple', ['apple', 'pen']));
A.scenario('No split', 's = "catsandog"', () => run('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']));
'''),

P(num=322, slug="coin-change", title="Coin Change", diff="Medium", topic="1D DP", cls="CoinChange",
idea="dp[a] = 1 + the minimum of dp[a − coin] over all coins; build it up from amount 0.",
vname="Bottom-up DP",
spec=r'''
Given coin denominations `coins` (unlimited supply of each) and an `amount`, return the fewest coins that add up to `amount`, or `-1`
if it is impossible.

**Example**
```
coins = [1,2,5], amount = 11 → 3 (5 + 5 + 1)
coins = [2],     amount = 3  → -1
coins = [1],     amount = 0  → 0
```

**Constraints**
* `1 <= coins.length <= 12`; `1 <= coins[i] <= 2^31 - 1`; `0 <= amount <= 10^4`
''',
approach=r'''
**Unbounded knapsack.** `dp[0] = 0`, every other entry starts at "infinity" (`amount + 1`). For `a = 1..amount` and each coin `c <= a`,
`dp[a] = min(dp[a], dp[a - c] + 1)`.

* Time: **O(amount · coins)** — every amount tries every coin.
* Space: **O(amount)** — the dp array.
''',
tc="n2", sc="n",
java=r'''
public class CoinChange {

    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int a = 1; a <= amount; a++) {
            for (int c : coins) {
                if (c <= a) dp[a] = Math.min(dp[a], dp[a - c] + 1);
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
''',
test=r'''
class CoinChangeTest {

    private final CoinChange solution = new CoinChange();

    @Test
    void examples() {
        assertEquals(3, solution.coinChange(new int[]{1, 2, 5}, 11));
        assertEquals(-1, solution.coinChange(new int[]{2}, 3));
        assertEquals(0, solution.coinChange(new int[]{1}, 0));
    }

    @Test
    void greedyFails() {
        assertEquals(2, solution.coinChange(new int[]{1, 3, 4}, 6));
    }

    @Test
    void hugeCoin() {
        assertEquals(1, solution.coinChange(new int[]{2147483647, 1}, 1));
    }
}
''',
trace=r'''
function run(coins, amount) {
  const dp = [0, ...new Array(amount).fill('∞')];
  A.step(`dp[a] is the fewest coins making amount a. dp[0] = 0. Coins: ${coins.join(', ')}.`, A.arr('dp', dp));
  for (let a = 1; a <= amount; a++) {
    let best = Infinity, via = null;
    for (const c of coins) if (c <= a && dp[a - c] !== '∞' && dp[a - c] + 1 < best) { best = dp[a - c] + 1; via = c; }
    dp[a] = best === Infinity ? '∞' : best;
    A.step(via ? `dp[${a}]: the best last coin is ${via}, so 1 + dp[${a - via}] = ${best}.` : `dp[${a}]: no coin combination makes ${a}.`, A.arr('dp', dp, { hl: { [a]: via ? 'ok' : 'bad', ...(via ? { [a - via]: 'sel' } : {}) } }));
  }
  const r = dp[amount] === '∞' ? -1 : dp[amount];
  A.step(r < 0 ? `${amount} cannot be made.` : `${amount} needs ${r} coins.`, A.text('Result', r, r < 0 ? 'bad' : 'ok'));
}
A.scenario('Greedy would fail', 'coins = [1,3,4], amount = 6', () => run([1, 3, 4], 6));
A.scenario('Impossible', 'coins = [2], amount = 3', () => run([2], 3));
''',
variants=[dict(
name="Top-down memoized recursion",
idea="minCoins(a) = 1 + min over coins of minCoins(a − coin), with answers cached in an array.",
approach=r'''
**Memoized recursion.** `solve(a)`: 0 for `a == 0`, -1 for `a < 0`, otherwise try every coin; cache results in `memo[a]`.

* Time: **O(amount · coins)** — each amount is solved once, trying every coin.
* Space: **O(amount)** — the memo array and the recursion depth.
''',
tc="n2", sc="n",
java=r'''
public class CoinChange {

    private int[] memo;

    public int coinChange(int[] coins, int amount) {
        memo = new int[amount + 1];
        Arrays.fill(memo, Integer.MIN_VALUE);
        return solve(coins, amount);
    }

    private int solve(int[] coins, int a) {
        if (a == 0) return 0;
        if (memo[a] != Integer.MIN_VALUE) return memo[a];
        int best = Integer.MAX_VALUE;
        for (int c : coins) {
            if (c <= a) {
                int sub = solve(coins, a - c);
                if (sub >= 0) best = Math.min(best, sub + 1);
            }
        }
        return memo[a] = best == Integer.MAX_VALUE ? -1 : best;
    }
}
''',
trace=r'''
function run(coins, amount) {
  const memo = new Array(amount + 1).fill('');
  memo[0] = 0;
  const solve = a => { if (memo[a] !== '') return memo[a]; let best = Infinity; for (const c of coins) if (c <= a) { const s = solve(a - c); if (s >= 0) best = Math.min(best, s + 1); } memo[a] = best === Infinity ? -1 : best; A.step(`solve(${a}) = ${memo[a]}.`, A.arr('memo', memo, { hl: { [a]: 'ok' } })); return memo[a]; };
  A.step(`Answer: ${solve(amount)}.`, A.text('Result', memo[amount], 'ok'));
}
A.scenario('Greedy would fail', 'coins = [1,3,4], amount = 6', () => run([1, 3, 4], 6));
''')]),
]
