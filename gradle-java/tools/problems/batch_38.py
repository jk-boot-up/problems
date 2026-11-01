PROBLEMS = [
P(num=166, slug="fraction-to-recurring-decimal", title="Fraction to Recurring Decimal", diff="Medium", topic="Hash Map", cls="FractionToDecimal",
idea="Long division repeats exactly when a remainder repeats; remember where each remainder first appeared.",
vname="Long division with a remainder map",
spec=r'''
Given two integers `numerator` and `denominator`, return the fraction as a string. If the fractional part repeats, wrap the repeating
part in parentheses.

**Example**
```
1 / 2    → "0.5"
2 / 1    → "2"
4 / 333  → "0.(012)"
1 / 6    → "0.1(6)"
-50 / 8  → "-6.25"
```

**Constraints**
* `-2^31 <= numerator, denominator <= 2^31 - 1`, `denominator != 0`
''',
approach=r'''
**Long division.** Work with `long` absolute values (so `-2^31` does not overflow) and add the sign first. After the integer part, keep
multiplying the remainder by 10 to produce the next digit. Store each remainder with the position of the digit it produces. When a
remainder comes back, the digits from that position onward repeat forever: insert `(` there and close with `)`.

* Time: **O(d)** — `d` is the denominator; there are fewer than `d` distinct remainders.
* Space: **O(d)** — the remainder map.
''',
tc="n", sc="n",
java=r'''
public class FractionToDecimal {

    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        StringBuilder sb = new StringBuilder();
        if ((numerator < 0) ^ (denominator < 0)) sb.append('-');
        long n = Math.abs((long) numerator), d = Math.abs((long) denominator);
        sb.append(n / d);
        long r = n % d;
        if (r == 0) return sb.toString();
        sb.append('.');
        MyHashMap<Long, Integer> seenAt = new MyHashMap<>();
        while (r != 0) {
            Integer at = seenAt.get(r);
            if (at != null) {
                sb.insert((int) at, '(');
                sb.append(')');
                break;
            }
            seenAt.put(r, sb.length());
            r *= 10;
            sb.append(r / d);
            r %= d;
        }
        return sb.toString();
    }
}
''',
test=r'''
class FractionToDecimalTest {

    private final FractionToDecimal solution = new FractionToDecimal();

    @Test
    void examples() {
        assertEquals("0.5", solution.fractionToDecimal(1, 2));
        assertEquals("2", solution.fractionToDecimal(2, 1));
        assertEquals("0.(012)", solution.fractionToDecimal(4, 333));
        assertEquals("0.1(6)", solution.fractionToDecimal(1, 6));
        assertEquals("-6.25", solution.fractionToDecimal(-50, 8));
        assertEquals("0", solution.fractionToDecimal(0, -5));
    }

    @Test
    void extremes() {
        assertEquals("0.0000000004656612873077392578125", solution.fractionToDecimal(-1, Integer.MIN_VALUE));
        assertEquals("2147483648", solution.fractionToDecimal(Integer.MIN_VALUE, -1));
    }
}
''',
trace=r'''
function run(num, den) {
  let s = String(Math.floor(num / den)), r = num % den;
  A.step(`Long division of ${num} by ${den}. Each remainder decides every digit after it, so a repeated remainder means repeating digits.`, A.vars({ numerator: num, denominator: den }));
  A.step(`Integer part: ${num} ÷ ${den} = ${s}, remainder ${r}.`, A.vars({ remainder: r }), A.text('Result so far', s));
  if (r === 0) { A.step('The remainder is 0, so the division is exact.', A.text('Result', s, 'ok')); return; }
  s += '.'; const seen = new Map();
  while (r !== 0 && !seen.has(r)) {
    seen.set(r, s.length); const old = r; r *= 10; const q = Math.floor(r / den); s += q;
    A.step(`Remainder ${old} is new; it produces the digit at position ${seen.get(old)}. ${r} ÷ ${den} = ${q}, next remainder ${r % den}.`, A.hashTable('remainder → position', seen, { hl: old }), A.text('Result so far', s));
    r %= den;
  }
  if (r === 0) { A.step('The remainder reached 0: the decimal ends here.', A.text('Result', s, 'ok')); return; }
  const at = seen.get(r); s = s.slice(0, at) + '(' + s.slice(at) + ')';
  A.step(`Remainder ${r} was seen before at position ${at}. Everything from there repeats, so wrap it in parentheses.`, A.hashTable('remainder → position', seen, { hl: r }), A.text('Result', s, 'ok'));
}
A.scenario('Repeating tail', '1 / 6', () => run(1, 6));
A.scenario('Pure repeat', '4 / 333', () => run(4, 333));
A.scenario('Terminating', '1 / 8', () => run(1, 8));
'''),

P(num=168, slug="excel-sheet-column-title", title="Excel Sheet Column Title", diff="Easy", topic="Math", cls="ExcelColumnTitle",
idea="Base 26 with digits 1..26 instead of 0..25, so subtract one before each step.",
vname="Bijective base-26",
spec=r'''
Given a positive integer `columnNumber`, return its column title as it appears in a spreadsheet: `1 → A`, `26 → Z`, `27 → AA`,
`28 → AB`, …

**Example**
```
1   → "A"
28  → "AB"
701 → "ZY"
```

**Constraints**
* `1 <= columnNumber <= 2^31 - 1`
''',
approach=r'''
**Shift then divide.** Titles are base 26 with no zero digit. Subtract 1 so the last letter becomes `(n - 1) % 26` (0 → `A`, 25 → `Z`),
then continue with `(n - 1) / 26`. Letters come out last-first, so reverse at the end.

* Time: **O(log₂₆ n)** — one letter per step.
* Space: **O(1)** — at most 7 letters.
''',
tc="log", sc="1",
java=r'''
public class ExcelColumnTitle {

    public String convertToTitle(int columnNumber) {
        StringBuilder sb = new StringBuilder();
        while (columnNumber > 0) {
            columnNumber--;
            sb.append((char) ('A' + columnNumber % 26));
            columnNumber /= 26;
        }
        return sb.reverse().toString();
    }
}
''',
test=r'''
class ExcelColumnTitleTest {

    private final ExcelColumnTitle solution = new ExcelColumnTitle();

    @ParameterizedTest
    @CsvSource({"1,A", "26,Z", "27,AA", "28,AB", "52,AZ", "701,ZY", "702,ZZ", "703,AAA", "2147483647,FXSHRXW"})
    void titles(int n, String expected) {
        assertEquals(expected, solution.convertToTitle(n));
    }
}
''',
trace=r'''
function run(n) {
  A.step(`Convert ${n}. There is no zero letter, so each round first subtracts 1, then takes the remainder mod 26.`, A.vars({ n }));
  let out = '';
  while (n > 0) {
    const m = n - 1, ch = String.fromCharCode(65 + (m % 26));
    out = ch + out;
    A.step(`${n} − 1 = ${m}; ${m} mod 26 = ${m % 26} → '${ch}'. Continue with ${m} ÷ 26 = ${Math.floor(m / 26)}.`, A.vars({ n, 'n - 1': m, letter: ch }), A.chars('title', out, { hl: { 0: 'cur' } }));
    n = Math.floor(m / 26);
  }
  A.step(`Nothing left. The title is ${out}.`, A.text('Result', out, 'ok'));
}
A.scenario('Two letters', '28', () => run(28));
A.scenario('Z boundary', '701', () => run(701));
'''),

P(num=171, slug="excel-sheet-column-number", title="Excel Sheet Column Number", diff="Easy", topic="Math", cls="ExcelColumnNumber",
idea="Read the title like a base-26 number whose digits are A = 1 … Z = 26.",
vname="Horner's rule in base 26",
spec=r'''
Given a column title as shown in a spreadsheet, return its column number (`A → 1`, `Z → 26`, `AA → 27`, …).

**Example**
```
"A"  → 1
"AB" → 28
"ZY" → 701
```

**Constraints**
* `1 <= columnTitle.length <= 7`, upper-case letters, value at most `2^31 - 1`
''',
approach=r'''
**Horner's rule.** Scan left to right: `result = result * 26 + (letter - 'A' + 1)`.

* Time: **O(n)** — one step per letter.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class ExcelColumnNumber {

    public int titleToNumber(String columnTitle) {
        int result = 0;
        for (int i = 0; i < columnTitle.length(); i++) result = result * 26 + (columnTitle.charAt(i) - 'A' + 1);
        return result;
    }
}
''',
test=r'''
class ExcelColumnNumberTest {

    private final ExcelColumnNumber solution = new ExcelColumnNumber();

    @ParameterizedTest
    @CsvSource({"A,1", "Z,26", "AA,27", "AB,28", "ZY,701", "AAA,703", "FXSHRXW,2147483647"})
    void numbers(String title, int expected) {
        assertEquals(expected, solution.titleToNumber(title));
    }
}
''',
trace=r'''
function run(t) {
  A.step(`Read "${t}" as a base-26 number where A = 1 and Z = 26.`, A.chars('title', t), A.vars({ result: 0 }));
  let r = 0;
  for (let i = 0; i < t.length; i++) {
    const d = t.charCodeAt(i) - 64, prev = r; r = r * 26 + d;
    A.step(`'${t[i]}' = ${d}. result = ${prev} × 26 + ${d} = ${r}.`, A.chars('title', t, { hl: { [i]: 'cur' } }), A.vars({ result: r }));
  }
  A.step(`"${t}" is column ${r}.`, A.text('Result', r, 'ok'));
}
A.scenario('Two letters', '"AB"', () => run('AB'));
A.scenario('Three letters', '"AAA"', () => run('AAA'));
'''),

P(num=179, slug="largest-number", title="Largest Number", diff="Medium", topic="Sorting", cls="LargestNumber",
idea="Put a before b exactly when the string a+b beats b+a.",
vname="Sort by concatenation order",
spec=r'''
Given non-negative integers `nums`, arrange them so they form the largest possible number, and return it as a string.

**Example**
```
[10,2]          → "210"
[3,30,34,5,9]   → "9534330"
[0,0]           → "0"
```

**Constraints**
* `1 <= nums.length <= 100`, `0 <= nums[i] <= 10^9`
''',
approach=r'''
**Custom order.** Compare two numbers by trying both orders: `a` goes first if `a + b > b + a` as strings. This order is transitive, so a
normal sort produces the best arrangement. If the biggest piece is `"0"`, every piece is zero: return `"0"`, not `"00"`.

* Time: **O(n log n · L)** — sorting with comparisons of length `L` (at most 20 characters).
* Space: **O(n · L)** — the strings.
''',
tc="nlogn", sc="n",
java=r'''
public class LargestNumber {

    public String largestNumber(int[] nums) {
        String[] parts = new String[nums.length];
        for (int i = 0; i < nums.length; i++) parts[i] = String.valueOf(nums[i]);
        Arrays.sort(parts, (a, b) -> (b + a).compareTo(a + b));
        if (parts[0].equals("0")) return "0";
        return String.join("", parts);
    }
}
''',
test=r'''
class LargestNumberTest {

    private final LargestNumber solution = new LargestNumber();

    @Test
    void examples() {
        assertEquals("210", solution.largestNumber(new int[]{10, 2}));
        assertEquals("9534330", solution.largestNumber(new int[]{3, 30, 34, 5, 9}));
        assertEquals("0", solution.largestNumber(new int[]{0, 0}));
        assertEquals("1", solution.largestNumber(new int[]{1}));
        assertEquals("43243432", solution.largestNumber(new int[]{432, 43243}));
    }
}
''',
trace=r'''
function run(nums) {
  const a = nums.map(String);
  A.step('Turn the numbers into strings. Instead of comparing values, compare the two ways of gluing a pair together.', A.arr('pieces', a));
  for (let i = 1; i < a.length; i++) {
    let j = i;
    while (j > 0 && a[j] + a[j - 1] > a[j - 1] + a[j]) {
      A.step(`"${a[j]}${a[j - 1]}" > "${a[j - 1]}${a[j]}", so ${a[j]} should come before ${a[j - 1]}: swap.`, A.arr('pieces', a, { hl: { [j - 1]: 'bad', [j]: 'cur' } }));
      [a[j], a[j - 1]] = [a[j - 1], a[j]]; j--;
    }
    if (j > 0) A.step(`"${a[j - 1]}${a[j]}" ≥ "${a[j]}${a[j - 1]}": ${a[j]} stays after ${a[j - 1]}.`, A.arr('pieces', a, { hl: { [j - 1]: 'ok', [j]: 'cur' } }));
  }
  const res = a[0] === '0' ? '0' : a.join('');
  A.step(`Sorted in concatenation order. Joined: ${res}.`, A.arr('pieces', a, { hl: Object.fromEntries(a.map((_, i) => [i, 'ok'])) }), A.text('Result', res, 'ok'));
}
A.scenario('Classic', '[3,30,34,5,9]', () => run([3, 30, 34, 5, 9]));
A.scenario('Prefix trap', '[10,2]', () => run([10, 2]));
'''),

P(num=187, slug="repeated-dna-sequences", title="Repeated DNA Sequences", diff="Medium", topic="Hash Map", cls="RepeatedDNA",
idea="Encode each 10-letter window as a 20-bit integer and roll it forward one letter at a time.",
vname="Rolling 2-bit encoding",
spec=r'''
A DNA string uses the letters `A`, `C`, `G`, `T`. Return every 10-letter substring that occurs **more than once**, each reported once.

**Example**
```
"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" → ["AAAAACCCCC","CCCCCAAAAA"]
"AAAAAAAAAAAAA"                    → ["AAAAAAAAAA"]
```

**Constraints**
* `1 <= s.length <= 10^5`
''',
approach=r'''
**Two bits per letter.** Map `A,C,G,T` to `0..3`. A window of 10 letters fits in 20 bits. Sliding right, shift the code left by 2, add the
new letter, and mask to 20 bits, all in O(1). Keep a set of codes seen once and a set of codes already reported.

* Time: **O(n)** — constant work per position.
* Space: **O(n)** — the two integer sets.
''',
tc="n", sc="n",
java=r'''
public class RepeatedDNA {

    public List<String> findRepeatedDnaSequences(String s) {
        int[] code = new int[128];
        code['C'] = 1;
        code['G'] = 2;
        code['T'] = 3;
        int mask = (1 << 20) - 1, h = 0;
        MyHashSet<Integer> seen = new MyHashSet<>(), reported = new MyHashSet<>();
        List<String> out = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            h = ((h << 2) | code[s.charAt(i)]) & mask;
            if (i >= 9 && !seen.add(h) && reported.add(h)) out.add(s.substring(i - 9, i + 1));
        }
        return out;
    }
}
''',
test=r'''
class RepeatedDNATest {

    private final RepeatedDNA solution = new RepeatedDNA();

    @Test
    void examples() {
        assertEquals(List.of("AAAAACCCCC", "CCCCCAAAAA"), solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"));
        assertEquals(List.of("AAAAAAAAAA"), solution.findRepeatedDnaSequences("AAAAAAAAAAAAA"));
        assertEquals(List.of(), solution.findRepeatedDnaSequences("ACGT"));
        assertEquals(List.of(), solution.findRepeatedDnaSequences("ACGTACGTAC"));
    }
}
''',
trace=r'''
function run(s) {
  const code = { A: 0, C: 1, G: 2, T: 3 }, mask = (1 << 20) - 1, seen = new Set(), rep = new Set(), out = [];
  A.step('Each letter becomes 2 bits (A=00, C=01, G=10, T=11). A 10-letter window is a 20-bit number.', A.chars('dna', s), A.vars(code, 'Codes'));
  let h = 0;
  for (let i = 0; i < s.length; i++) {
    h = ((h << 2) | code[s[i]]) & mask;
    if (i < 9) continue;
    const w = s.slice(i - 9, i + 1), range = [i - 9, i];
    if (!seen.has(h)) { seen.add(h); A.step(`Window "${w}" → code ${h}. First time: remember it.`, A.chars('dna', s, { range }), A.vars({ code: h, seen: seen.size })); }
    else if (!rep.has(h)) { rep.add(h); out.push(w); A.step(`Window "${w}" → code ${h} was seen before. Report it.`, A.chars('dna', s, { range, hl: Object.fromEntries(Array.from({ length: 10 }, (_, k) => [i - 9 + k, 'ok'])) }), A.arr('repeated', out, { hl: { [out.length - 1]: 'ok' } })); }
    else A.step(`Window "${w}" was already reported; skip it.`, A.chars('dna', s, { range }), A.arr('repeated', out));
  }
  A.step(`Done: ${out.length} repeated sequence${out.length === 1 ? '' : 's'}.`, A.arr('repeated', out, { hl: Object.fromEntries(out.map((_, i) => [i, 'ok'])) }));
}
A.scenario('All A', '"AAAAAAAAAAAAA"', () => run('AAAAAAAAAAAAA'));
A.scenario('Two repeats', '"AAAAACCCCCAAAAACCCCCC"', () => run('AAAAACCCCCAAAAACCCCCC'));
''',
variants=[dict(
name="Set of substrings",
idea="Slice every 10-letter window and remember it in a set of strings.",
approach=r'''
**Substring set.** For each start, take the 10-letter substring. Adding it to `seen` fails for a repeat; report it the first time that
happens.

* Time: **O(n · L)** — `L = 10` characters copied and hashed per window.
* Space: **O(n · L)** — the stored substrings.
''',
tc="n", sc="n",
java=r'''
public class RepeatedDNA {

    public List<String> findRepeatedDnaSequences(String s) {
        MyHashSet<String> seen = new MyHashSet<>(), reported = new MyHashSet<>();
        List<String> out = new ArrayList<>();
        for (int i = 0; i + 10 <= s.length(); i++) {
            String w = s.substring(i, i + 10);
            if (!seen.add(w) && reported.add(w)) out.add(w);
        }
        return out;
    }
}
''',
trace=r'''
function run(s) {
  const seen = new Set(), rep = new Set(), out = [];
  A.step('Slide a 10-letter window and keep every window in a set.', A.chars('dna', s));
  for (let i = 0; i + 10 <= s.length; i++) {
    const w = s.slice(i, i + 10), range = [i, i + 9];
    if (!seen.has(w)) { seen.add(w); A.step(`"${w}" is new.`, A.chars('dna', s, { range }), A.vars({ 'distinct windows': seen.size })); }
    else if (!rep.has(w)) { rep.add(w); out.push(w); A.step(`"${w}" is already in the set: report it.`, A.chars('dna', s, { range }), A.arr('repeated', out, { hl: { [out.length - 1]: 'ok' } })); }
    else A.step(`"${w}" was reported already.`, A.chars('dna', s, { range }), A.arr('repeated', out));
  }
  A.step(`Done: ${out.length} repeated sequence${out.length === 1 ? '' : 's'}.`, A.arr('repeated', out));
}
A.scenario('All A', '"AAAAAAAAAAAAA"', () => run('AAAAAAAAAAAAA'));
''')]),

P(num=204, slug="count-primes", title="Count Primes", diff="Medium", topic="Math", cls="CountPrimes",
idea="Cross out multiples of each prime, starting at its square; whatever survives is prime.",
vname="Sieve of Eratosthenes",
spec=r'''
Return the number of prime numbers **strictly less than** `n`.

**Example**
```
10 → 4    (2, 3, 5, 7)
0  → 0
1  → 0
```

**Constraints**
* `0 <= n <= 5 * 10^6`
''',
approach=r'''
**Sieve.** Walk `i` upward. If `i` is not crossed out, it is prime: count it and cross out `i·i, i·i + i, …` (smaller multiples were
crossed out by smaller primes already). Use `long` for `i·i` so large `i` does not overflow.

* Time: **O(n log log n)** — the classic sieve bound.
* Space: **O(n)** — one flag per number.
''',
tc="n", sc="n",
java=r'''
public class CountPrimes {

    public int countPrimes(int n) {
        boolean[] composite = new boolean[Math.max(n, 2)];
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (composite[i]) continue;
            count++;
            for (long j = (long) i * i; j < n; j += i) composite[(int) j] = true;
        }
        return count;
    }
}
''',
test=r'''
class CountPrimesTest {

    private final CountPrimes solution = new CountPrimes();

    @ParameterizedTest
    @CsvSource({"0,0", "1,0", "2,0", "3,1", "10,4", "11,4", "12,5", "100,25", "10000,1229"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.countPrimes(n));
    }
}
''',
trace=r'''
function run(n) {
  const nums = Array.from({ length: n }, (_, i) => i), comp = new Array(n).fill(false), hl = { 0: 'dim', 1: 'dim' };
  A.step(`Find the primes below ${n}. 0 and 1 are not prime.`, A.arr('numbers', nums, { hl }));
  let count = 0, said = false;
  for (let i = 2; i < n; i++) {
    if (comp[i]) continue;
    count++; hl[i] = 'ok';
    const crossed = [];
    for (let j = i * i; j < n; j += i) if (!comp[j]) { comp[j] = true; crossed.push(j); hl[j] = 'bad'; }
    if (crossed.length) A.step(`${i} survived, so it is prime. Cross out its multiples from ${i}² = ${i * i}: ${crossed.join(', ')}.`, A.arr('numbers', nums, { hl, ptr: { [i]: 'p' } }), A.vars({ primes: count }));
    else if (i * i >= n && !said) { said = true; A.step(`${i}² ≥ ${n}: no more crossing out is needed. Every number still standing is prime.`, A.arr('numbers', nums, { hl, ptr: { [i]: 'p' } }), A.vars({ primes: count })); }
  }
  A.step(`${count} primes below ${n}.`, A.arr('numbers', nums, { hl }), A.text('Result', count, 'ok'));
}
A.scenario('Below 30', 'n = 30', () => run(30));
A.scenario('Below 10', 'n = 10', () => run(10));
''',
variants=[dict(
name="Trial division",
idea="Test each number for a divisor up to its square root.",
approach=r'''
**Trial division.** For each `x < n`, try divisors `2..√x`. Simple, but every number pays for its own test.

* Time: **O(n√n)** — up to `√x` divisions for each `x`.
* Space: **O(1)**.
''',
tc="n2", sc="1",
java=r'''
public class CountPrimes {

    public int countPrimes(int n) {
        int count = 0;
        for (int x = 2; x < n; x++) if (isPrime(x)) count++;
        return count;
    }

    private boolean isPrime(int x) {
        for (int d = 2; (long) d * d <= x; d++) if (x % d == 0) return false;
        return true;
    }
}
''',
trace=r'''
function run(n) {
  const nums = Array.from({ length: n }, (_, i) => i), hl = { 0: 'dim', 1: 'dim' };
  A.step(`Test every number below ${n} on its own.`, A.arr('numbers', nums, { hl }));
  let count = 0;
  for (let x = 2; x < n; x++) {
    let d = 2; while (d * d <= x && x % d) d++;
    const prime = d * d > x; if (prime) count++; hl[x] = prime ? 'ok' : 'bad';
    A.step(prime ? `${x}: no divisor up to √${x}, so it is prime.` : `${x} is divisible by ${d}.`, A.arr('numbers', nums, { hl, ptr: { [x]: 'x' } }), A.vars({ primes: count }));
  }
  A.step(`${count} primes below ${n}.`, A.text('Result', count, 'ok'));
}
A.scenario('Below 10', 'n = 10', () => run(10));
''')]),

P(num=216, slug="combination-sum-iii", title="Combination Sum III", diff="Medium", topic="Backtracking", cls="CombinationSumIII",
idea="Pick digits in increasing order and stop a branch as soon as the sum or the count overshoots.",
vname="Backtracking over digits 1–9",
spec=r'''
Find all combinations of `k` **distinct** digits from `1` to `9` that add up to `n`. Return each combination once, in any order.

**Example**
```
k = 3, n = 7 → [[1,2,4]]
k = 3, n = 9 → [[1,2,6],[1,3,5],[2,3,4]]
k = 4, n = 1 → []
```

**Constraints**
* `2 <= k <= 9`, `1 <= n <= 60`
''',
approach=r'''
**Increasing choices.** Choosing digits in increasing order makes each combination appear once. From `start`, try each digit `d` no larger
than the remaining sum, recurse with `d + 1`, then undo. Record the path when it has `k` digits and the remainder is 0.

* Time: **O(C(9, k) · k)** — at most `C(9, k)` complete paths, each copied once.
* Space: **O(k)** — the recursion depth and path.
''',
tc="1", sc="1",
java=r'''
public class CombinationSumIII {

    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> out = new ArrayList<>();
        dfs(1, k, n, new ArrayList<>(), out);
        return out;
    }

    private void dfs(int start, int k, int left, List<Integer> path, List<List<Integer>> out) {
        if (path.size() == k) {
            if (left == 0) out.add(new ArrayList<>(path));
            return;
        }
        for (int d = start; d <= 9 && d <= left; d++) {
            path.add(d);
            dfs(d + 1, k, left - d, path, out);
            path.remove(path.size() - 1);
        }
    }
}
''',
test=r'''
class CombinationSumIIITest {

    private final CombinationSumIII solution = new CombinationSumIII();

    @Test
    void examples() {
        assertEquals(List.of(List.of(1, 2, 4)), solution.combinationSum3(3, 7));
        assertEquals(List.of(List.of(1, 2, 6), List.of(1, 3, 5), List.of(2, 3, 4)), solution.combinationSum3(3, 9));
        assertEquals(List.of(), solution.combinationSum3(4, 1));
        assertEquals(List.of(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9)), solution.combinationSum3(9, 45));
    }
}
''',
trace=r'''
function run(k, n) {
  const out = [], path = [];
  A.step(`Pick ${k} distinct digits from 1–9 that sum to ${n}. Digits go in increasing order, so no combination is built twice.`, A.vars({ k, n }));
  (function dfs(start, left) {
    if (path.length === k) {
      if (left === 0) { out.push(path.slice()); A.step(`[${path}] has ${k} digits and sums to ${n}: record it.`, A.stack('path', path), A.arr('found', out.map(c => `[${c}]`), { hl: { [out.length - 1]: 'ok' } })); }
      else A.step(`[${path}] has ${k} digits but ${left} is still missing. Back up.`, A.stack('path', path), A.vars({ left }));
      return;
    }
    for (let d = start; d <= 9 && d <= left; d++) { path.push(d); dfs(d + 1, left - d); path.pop(); }
  })(1, n);
  A.step(`Search finished: ${out.length} combination${out.length === 1 ? '' : 's'}.`, A.arr('found', out.map(c => `[${c}]`)));
}
A.scenario('One answer', 'k = 3, n = 7', () => run(3, 7));
A.scenario('Three answers', 'k = 3, n = 9', () => run(3, 9));
'''),

P(num=218, slug="the-skyline-problem", title="The Skyline Problem", diff="Hard", topic="Heap", cls="Skyline",
idea="Sweep the x-coordinates; a max-heap of active buildings gives the current height, and every change is a key point.",
vname="Sweep line with a max-heap",
spec=r'''
Each building is `[left, right, height]`, sorted by `left`. Return the **skyline**: the key points `[x, height]` where the outline's height
changes, sorted by `x`. The last point always has height 0. No two consecutive points may have the same height.

**Example**
```
[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
  → [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
[[0,2,3],[2,5,3]] → [[0,3],[5,0]]
```

**Constraints**
* `1 <= buildings.length <= 10^4`, `0 <= left < right <= 2^31 - 1`, `1 <= height <= 2^31 - 1`
''',
approach=r'''
**Sweep.** The height can only change at a building edge. Visit the distinct edge x-coordinates in order. Push every building that starts
at or before `x` into a max-heap keyed by height, then pop buildings from the top whose `right <= x` (lazy removal: buried finished
buildings are removed once they reach the top). The heap top is the height just right of `x`; record `[x, h]` if it differs from the
last recorded height.

* Time: **O(n log n)** — sorting edges and heap operations.
* Space: **O(n)** — the heap and edge list.
''',
tc="nlogn", sc="n",
java=r'''
public class Skyline {

    public List<List<Integer>> getSkyline(int[][] buildings) {
        int m = buildings.length;
        int[] xs = new int[2 * m];
        for (int i = 0; i < m; i++) {
            xs[2 * i] = buildings[i][0];
            xs[2 * i + 1] = buildings[i][1];
        }
        Arrays.sort(xs);
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        List<List<Integer>> out = new ArrayList<>();
        int next = 0;
        for (int k = 0; k < xs.length; k++) {
            int x = xs[k];
            if (k > 0 && x == xs[k - 1]) continue;
            while (next < m && buildings[next][0] <= x) {
                heap.add(new int[]{buildings[next][2], buildings[next][1]});
                next++;
            }
            while (!heap.isEmpty() && heap.peek()[1] <= x) heap.poll();
            int h = heap.isEmpty() ? 0 : heap.peek()[0];
            if (out.isEmpty() || out.get(out.size() - 1).get(1) != h) out.add(List.of(x, h));
        }
        return out;
    }
}
''',
test=r'''
class SkylineTest {

    private final Skyline solution = new Skyline();

    @Test
    void examples() {
        assertEquals(List.of(List.of(2, 10), List.of(3, 15), List.of(7, 12), List.of(12, 0), List.of(15, 10), List.of(20, 8), List.of(24, 0)),
                solution.getSkyline(new int[][]{{2, 9, 10}, {3, 7, 15}, {5, 12, 12}, {15, 20, 10}, {19, 24, 8}}));
        assertEquals(List.of(List.of(0, 3), List.of(5, 0)), solution.getSkyline(new int[][]{{0, 2, 3}, {2, 5, 3}}));
    }

    @Test
    void nested() {
        assertEquals(List.of(List.of(1, 5), List.of(10, 0)), solution.getSkyline(new int[][]{{1, 10, 5}, {2, 3, 4}}));
        assertEquals(List.of(List.of(1, 3), List.of(2, 0)), solution.getSkyline(new int[][]{{1, 2, 1}, {1, 2, 2}, {1, 2, 3}}));
    }
}
''',
trace=r'''
function run(bs) {
  const xs = [...new Set(bs.flatMap(b => [b[0], b[1]]))].sort((a, b) => a - b), out = []; let heap = [], next = 0;
  A.step('The outline can only change at a building edge. Sweep those x-coordinates from left to right.', A.grid('buildings [left, right, height]', bs), A.arr('edges', xs));
  xs.forEach((x, k) => {
    const added = [];
    while (next < bs.length && bs[next][0] <= x) { heap.push([bs[next][2], bs[next][1]]); added.push(bs[next][2]); next++; }
    heap.sort((a, b) => b[0] - a[0]);
    const gone = [];
    while (heap.length && heap[0][1] <= x) gone.push(heap.shift()[0]);
    const h = heap.length ? heap[0][0] : 0, changed = !out.length || out[out.length - 1][1] !== h;
    if (changed) out.push([x, h]);
    const what = [added.length ? `add height ${added.join(', ')}` : '', gone.length ? `drop finished ${gone.join(', ')}` : ''].filter(Boolean).join('; ');
    A.step(`x = ${x}: ${what || 'nothing new'}. Tallest active: ${h}. ${changed ? `Height changed → key point [${x}, ${h}].` : 'Same height, no key point.'}`,
      A.arr('edges', xs, { hl: { [k]: 'cur' } }), A.stack('heap (height, right)', heap.map(e => `${e[0]} (→${e[1]})`)), A.arr('skyline', out.map(p => `[${p}]`), { hl: changed ? { [out.length - 1]: 'ok' } : {} }));
  });
  A.step(`Skyline complete: ${out.length} key points.`, A.arr('skyline', out.map(p => `[${p}]`)));
}
A.scenario('Classic city', '5 buildings', () => run([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]));
A.scenario('Touching equal heights', '[[0,2,3],[2,5,3]]', () => run([[0, 2, 3], [2, 5, 3]]));
''',
variants=[dict(
name="Height at every edge",
idea="For each edge x, scan all buildings to find the tallest one covering x.",
approach=r'''
**Brute force.** The height just right of `x` is the tallest building with `left <= x < right`. Compute it for every distinct edge by
scanning all buildings, and keep the points where it changes.

* Time: **O(n²)** — `2n` edges, each scanning `n` buildings.
* Space: **O(n)** — the edge list.
''',
tc="n2", sc="n",
java=r'''
public class Skyline {

    public List<List<Integer>> getSkyline(int[][] buildings) {
        int[] xs = new int[2 * buildings.length];
        for (int i = 0; i < buildings.length; i++) {
            xs[2 * i] = buildings[i][0];
            xs[2 * i + 1] = buildings[i][1];
        }
        Arrays.sort(xs);
        List<List<Integer>> out = new ArrayList<>();
        for (int k = 0; k < xs.length; k++) {
            int x = xs[k];
            if (k > 0 && x == xs[k - 1]) continue;
            int h = 0;
            for (int[] b : buildings) if (b[0] <= x && x < b[1]) h = Math.max(h, b[2]);
            if (out.isEmpty() || out.get(out.size() - 1).get(1) != h) out.add(List.of(x, h));
        }
        return out;
    }
}
''',
trace=r'''
function run(bs) {
  const xs = [...new Set(bs.flatMap(b => [b[0], b[1]]))].sort((a, b) => a - b), out = [];
  A.step('Check the height just right of every building edge.', A.grid('buildings [left, right, height]', bs), A.arr('edges', xs));
  xs.forEach((x, k) => {
    const cover = bs.filter(b => b[0] <= x && x < b[1]), h = Math.max(0, ...cover.map(b => b[2])), changed = !out.length || out[out.length - 1][1] !== h;
    if (changed) out.push([x, h]);
    A.step(`x = ${x}: covered by ${cover.length ? cover.map(b => b[2]).join(', ') : 'nothing'} → height ${h}. ${changed ? 'New key point.' : 'No change.'}`, A.arr('edges', xs, { hl: { [k]: 'cur' } }), A.arr('skyline', out.map(p => `[${p}]`), { hl: changed ? { [out.length - 1]: 'ok' } : {} }));
  });
  A.step(`Skyline complete: ${out.length} key points.`, A.arr('skyline', out.map(p => `[${p}]`)));
}
A.scenario('Classic city', '5 buildings', () => run([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]));
''')]),

P(num=220, slug="contains-duplicate-iii", title="Contains Duplicate III", diff="Hard", topic="Sliding Window", cls="ContainsDuplicateIII",
idea="Buckets of width valueDiff + 1: two close values share a bucket or sit in neighbouring buckets.",
vname="Buckets over a sliding window",
spec=r'''
Given `nums`, `indexDiff` and `valueDiff`, return `true` if there are two indices `i != j` with `|i - j| <= indexDiff` and
`|nums[i] - nums[j]| <= valueDiff`.

**Example**
```
nums = [1,2,3,1],     indexDiff = 3, valueDiff = 0 → true
nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3 → false
```

**Constraints**
* `2 <= nums.length <= 10^5`, `-10^9 <= nums[i] <= 10^9`, `1 <= indexDiff <= nums.length`, `0 <= valueDiff <= 10^9`
''',
approach=r'''
**Buckets.** Let `w = valueDiff + 1` and put value `v` in bucket `floorDiv(v, w)`. Two values in the same bucket differ by at most
`valueDiff`; values in buckets two or more apart differ by more. So for each new value, check its own bucket and the two neighbours. Keep
only the last `indexDiff` values in the map (one per bucket suffices, since a second one would already have returned `true`). Use `long`
to avoid overflow.

* Time: **O(n)** — constant work per element.
* Space: **O(min(n, k))** — at most `indexDiff` buckets.
''',
tc="n", sc="n",
java=r'''
public class ContainsDuplicateIII {

    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        long w = (long) valueDiff + 1;
        MyHashMap<Long, Long> buckets = new MyHashMap<>();
        for (int i = 0; i < nums.length; i++) {
            long v = nums[i], id = Math.floorDiv(v, w);
            if (buckets.containsKey(id)) return true;
            Long lo = buckets.get(id - 1), hi = buckets.get(id + 1);
            if (lo != null && v - lo <= valueDiff) return true;
            if (hi != null && hi - v <= valueDiff) return true;
            buckets.put(id, v);
            if (i >= indexDiff) buckets.remove(Math.floorDiv((long) nums[i - indexDiff], w));
        }
        return false;
    }
}
''',
test=r'''
class ContainsDuplicateIIITest {

    private final ContainsDuplicateIII solution = new ContainsDuplicateIII();

    @Test
    void examples() {
        assertTrue(solution.containsNearbyAlmostDuplicate(new int[]{1, 2, 3, 1}, 3, 0));
        assertFalse(solution.containsNearbyAlmostDuplicate(new int[]{1, 5, 9, 1, 5, 9}, 2, 3));
        assertTrue(solution.containsNearbyAlmostDuplicate(new int[]{1, 0, 1, 1}, 1, 2));
    }

    @Test
    void negativesAndExtremes() {
        assertFalse(solution.containsNearbyAlmostDuplicate(new int[]{-3, 3}, 2, 4));
        assertTrue(solution.containsNearbyAlmostDuplicate(new int[]{-3, 3}, 2, 6));
        assertFalse(solution.containsNearbyAlmostDuplicate(new int[]{Integer.MIN_VALUE, Integer.MAX_VALUE}, 1, Integer.MAX_VALUE));
        assertTrue(solution.containsNearbyAlmostDuplicate(new int[]{-1, -1}, 1, 0));
    }

    @Test
    void windowLimit() {
        assertFalse(solution.containsNearbyAlmostDuplicate(new int[]{1, 2, 3, 1}, 2, 0));
        assertTrue(solution.containsNearbyAlmostDuplicate(new int[]{8, 7, 15, 1, 6, 1, 9, 15}, 1, 3));
    }
}
''',
trace=r'''
function run(nums, k, t) {
  const w = t + 1, b = new Map(), fd = v => Math.floor(v / w);
  A.step(`Bucket width ${w}: values in one bucket differ by at most ${t}. Keep only the last ${k} values.`, A.arr('nums', nums), A.vars({ indexDiff: k, valueDiff: t, width: w }));
  for (let i = 0; i < nums.length; i++) {
    const v = nums[i], id = fd(v), lo = b.get(id - 1), hi = b.get(id + 1);
    const win = { range: [Math.max(0, i - k), i], hl: { [i]: 'cur' } };
    if (b.has(id)) { A.step(`${v} goes to bucket ${id}, which already holds ${b.get(id)}. They differ by at most ${t}: true.`, A.arr('nums', nums, win), A.hashTable('bucket → value', b, { hl: id }), A.text('Result', 'true', 'ok')); return; }
    if (lo !== undefined && v - lo <= t) { A.step(`Neighbour bucket ${id - 1} holds ${lo}; ${v} − ${lo} ≤ ${t}: true.`, A.arr('nums', nums, win), A.hashTable('bucket → value', b, { hl: id - 1 }), A.text('Result', 'true', 'ok')); return; }
    if (hi !== undefined && hi - v <= t) { A.step(`Neighbour bucket ${id + 1} holds ${hi}; ${hi} − ${v} ≤ ${t}: true.`, A.arr('nums', nums, win), A.hashTable('bucket → value', b, { hl: id + 1 }), A.text('Result', 'true', 'ok')); return; }
    b.set(id, v);
    let note = '';
    if (i >= k) { const old = nums[i - k]; b.delete(fd(old)); note = ` ${old} leaves the window.`; }
    A.step(`${v} → bucket ${id}; no close value nearby. Store it.${note}`, A.arr('nums', nums, win), A.hashTable('bucket → value', b, { hl: id }));
  }
  A.step('No pair is close enough in both index and value.', A.text('Result', 'false', 'bad'));
}
A.scenario('Equal values', '[1,2,3,1], 3, 0', () => run([1, 2, 3, 1], 3, 0));
A.scenario('Never close', '[1,5,9,1,5,9], 2, 3', () => run([1, 5, 9, 1, 5, 9], 2, 3));
''',
variants=[dict(
name="Check every nearby pair",
idea="For each index, compare it with the next indexDiff elements.",
approach=r'''
**Brute force.** For each `i`, compare `nums[i]` with `nums[i+1..i+indexDiff]` using `long` differences.

* Time: **O(n · k)** — `k = indexDiff` comparisons per element.
* Space: **O(1)**.
''',
tc="n2", sc="1",
java=r'''
public class ContainsDuplicateIII {

    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        for (int i = 0; i < nums.length; i++)
            for (int j = i + 1; j < nums.length && j - i <= indexDiff; j++)
                if (Math.abs((long) nums[i] - nums[j]) <= valueDiff) return true;
        return false;
    }
}
''',
trace=r'''
function run(nums, k, t) {
  A.step(`Compare every pair at most ${k} apart.`, A.arr('nums', nums), A.vars({ indexDiff: k, valueDiff: t }));
  for (let i = 0; i < nums.length; i++) for (let j = i + 1; j < nums.length && j - i <= k; j++) {
    const d = Math.abs(nums[i] - nums[j]);
    if (d <= t) { A.step(`|${nums[i]} − ${nums[j]}| = ${d} ≤ ${t}: true.`, A.arr('nums', nums, { hl: { [i]: 'ok', [j]: 'ok' } }), A.text('Result', 'true', 'ok')); return; }
    A.step(`|${nums[i]} − ${nums[j]}| = ${d} > ${t}.`, A.arr('nums', nums, { hl: { [i]: 'cur', [j]: 'bad' } }));
  }
  A.step('No pair qualifies.', A.text('Result', 'false', 'bad'));
}
A.scenario('Equal values', '[1,2,3,1], 3, 0', () => run([1, 2, 3, 1], 3, 0));
'''), dict(
name="Ordered window with TreeSet",
idea="Keep the last indexDiff values sorted and ask for the smallest one at least nums[i] − valueDiff.",
approach=r'''
**Balanced BST window.** Hold the last `indexDiff` values in a `TreeSet`. For the new value `v`, `ceiling(v - valueDiff)` is the smallest
candidate that is not too small; if it is also at most `v + valueDiff`, return `true`.

* Time: **O(n log k)** — one ordered lookup, insert and delete per element.
* Space: **O(k)** — the window.
''',
tc="nlogn", sc="n",
java=r'''
public class ContainsDuplicateIII {

    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        TreeSet<Long> window = new TreeSet<>();
        for (int i = 0; i < nums.length; i++) {
            long v = nums[i];
            Long c = window.ceiling(v - valueDiff);
            if (c != null && c <= v + valueDiff) return true;
            window.add(v);
            if (i >= indexDiff) window.remove((long) nums[i - indexDiff]);
        }
        return false;
    }
}
''',
trace=r'''
function run(nums, k, t) {
  const win = [];
  A.step(`Keep the last ${k} values sorted. For each value v, look for the smallest one ≥ v − ${t}.`, A.arr('nums', nums), A.vars({ indexDiff: k, valueDiff: t }));
  for (let i = 0; i < nums.length; i++) {
    const v = nums[i], c = win.find(x => x >= v - t);
    if (c !== undefined && c <= v + t) { A.step(`ceiling(${v - t}) = ${c}, and ${c} ≤ ${v + t}: true.`, A.arr('nums', nums, { hl: { [i]: 'ok' } }), A.arr('sorted window', win, { hl: { [win.indexOf(c)]: 'ok' } }), A.text('Result', 'true', 'ok')); return; }
    win.push(v); win.sort((a, b) => a - b);
    if (i >= k) win.splice(win.indexOf(nums[i - k]), 1);
    A.step(`${c === undefined ? `Nothing ≥ ${v - t}` : `ceiling ${c} > ${v + t}`}. Add ${v}${i >= k ? `, drop ${nums[i - k]}` : ''}.`, A.arr('nums', nums, { hl: { [i]: 'cur' } }), A.arr('sorted window', win));
  }
  A.step('No pair qualifies.', A.text('Result', 'false', 'bad'));
}
A.scenario('Never close', '[1,5,9,1,5,9], 2, 3', () => run([1, 5, 9, 1, 5, 9], 2, 3));
''')]),

P(num=223, slug="rectangle-area", title="Rectangle Area", diff="Medium", topic="Math", cls="RectangleArea",
idea="Add both areas and subtract the overlap, whose sides are clamped at zero.",
vname="Inclusion–exclusion",
spec=r'''
Two axis-aligned rectangles are given by their bottom-left `(ax1, ay1)`, `(bx1, by1)` and top-right `(ax2, ay2)`, `(bx2, by2)` corners.
Return the total area they cover.

**Example**
```
ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2 → 45
ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2 → 16
```

**Constraints**
* `-10^4 <= all coordinates <= 10^4`
''',
approach=r'''
**Inclusion–exclusion.** The overlap is a rectangle from `max` of the left/bottom edges to `min` of the right/top edges. Its width and
height are clamped at 0 when the rectangles do not meet. Answer: `areaA + areaB - overlap`.

* Time: **O(1)**.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class RectangleArea {

    public int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        int a = (ax2 - ax1) * (ay2 - ay1);
        int b = (bx2 - bx1) * (by2 - by1);
        int w = Math.max(0, Math.min(ax2, bx2) - Math.max(ax1, bx1));
        int h = Math.max(0, Math.min(ay2, by2) - Math.max(ay1, by1));
        return a + b - w * h;
    }
}
''',
test=r'''
class RectangleAreaTest {

    private final RectangleArea solution = new RectangleArea();

    @Test
    void examples() {
        assertEquals(45, solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2));
        assertEquals(16, solution.computeArea(-2, -2, 2, 2, -2, -2, 2, 2));
        assertEquals(2, solution.computeArea(0, 0, 1, 1, 2, 2, 3, 3));
        assertEquals(2, solution.computeArea(0, 0, 1, 1, 1, 0, 2, 1));
    }
}
''',
trace=r'''
function run(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) {
  const a = (ax2 - ax1) * (ay2 - ay1), b = (bx2 - bx1) * (by2 - by1);
  A.step(`Rectangle A spans x ${ax1}..${ax2}, y ${ay1}..${ay2}. Rectangle B spans x ${bx1}..${bx2}, y ${by1}..${by2}.`, A.vars({ A: `(${ax1},${ay1})–(${ax2},${ay2})`, B: `(${bx1},${by1})–(${bx2},${by2})` }));
  A.step(`Area A = ${ax2 - ax1} × ${ay2 - ay1} = ${a}. Area B = ${bx2 - bx1} × ${by2 - by1} = ${b}.`, A.vars({ areaA: a, areaB: b }));
  const w = Math.max(0, Math.min(ax2, bx2) - Math.max(ax1, bx1)), h = Math.max(0, Math.min(ay2, by2) - Math.max(ay1, by1));
  A.step(`Overlap width = min(${ax2}, ${bx2}) − max(${ax1}, ${bx1}) → ${w}; height = min(${ay2}, ${by2}) − max(${ay1}, ${by1}) → ${h}. Overlap area ${w * h}.`, A.vars({ overlapW: w, overlapH: h, overlap: w * h }));
  A.step(`Counted twice, so subtract it once: ${a} + ${b} − ${w * h} = ${a + b - w * h}.`, A.text('Result', a + b - w * h, 'ok'));
}
A.scenario('Partial overlap', 'A(-3,0,3,4), B(0,-1,9,2)', () => run(-3, 0, 3, 4, 0, -1, 9, 2));
A.scenario('Disjoint', 'A(0,0,1,1), B(2,2,3,3)', () => run(0, 0, 1, 1, 2, 2, 3, 3));
'''),
]
