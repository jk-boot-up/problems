PROBLEMS = [
P(num=746, slug="min-cost-climbing-stairs", title="Min Cost Climbing Stairs", diff="Easy", topic="1D DP", cls="MinCostClimbingStairs",
idea="Reaching step i costs the cheaper of coming from i−1 or i−2, plus what you pay to leave that step.",
vname="Two rolling values",
spec=r'''
`cost[i]` is the price of stepping off stair `i`; from there you climb 1 or 2 stairs. You may start at stair 0 or 1. Return the minimum cost
to reach the top (just past the last stair).

**Example**
```
[10,15,20] → 15,   [1,100,1,1,1,100,1,1,100,1] → 6
```

**Constraints**
* `2 <= cost.length <= 1000`
''',
approach=r'''
**DP.** `reach(i) = min(reach(i-1) + cost[i-1], reach(i-2) + cost[i-2])` with `reach(0) = reach(1) = 0`; answer `reach(n)`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two values.
''',
java=r'''
public class MinCostClimbingStairs {

    public int minCostClimbingStairs(int[] cost) {
        int a = 0, b = 0; // cheapest cost to stand on step i-2 and i-1
        for (int i = 2; i <= cost.length; i++) {
            int c = Math.min(b + cost[i - 1], a + cost[i - 2]);
            a = b;
            b = c;
        }
        return b;
    }
}
''',
test=r'''
class MinCostClimbingStairsTest {

    private final MinCostClimbingStairs solution = new MinCostClimbingStairs();

    @Test
    void examples() {
        assertEquals(15, solution.minCostClimbingStairs(new int[]{10, 15, 20}));
        assertEquals(6, solution.minCostClimbingStairs(new int[]{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}));
    }
}
''',
trace=r'''
function run(cost) {
  const reach = [0, 0];
  A.step('Standing on step 0 or 1 is free. reach[i] is the cheapest way to stand on step i.', A.arr('cost', cost), A.arr('reach', reach));
  for (let i = 2; i <= cost.length; i++) {
    const one = reach[i - 1] + cost[i - 1], two = reach[i - 2] + cost[i - 2]; reach.push(Math.min(one, two));
    A.step(`Step ${i}${i === cost.length ? ' (the top)' : ''}: from step ${i - 1} costs ${one}, from step ${i - 2} costs ${two}. Take ${reach[i]}.`, A.arr('cost', cost, { hl: { [i - 1]: one <= two ? 'ok' : 'dim', [i - 2]: two < one ? 'ok' : 'dim' } }), A.arr('reach', reach, { hl: { [i]: 'cur' } }));
  }
  A.step(`Minimum cost: ${reach[cost.length]}.`, A.text('Result', reach[cost.length], 'ok'));
}
A.scenario('Three steps', 'cost = [10,15,20]', () => run([10, 15, 20]));
'''),

P(num=790, slug="domino-and-tromino-tiling", title="Domino and Tromino Tiling", diff="Medium", topic="1D DP", cls="DominoTrominoTiling",
idea="Counting tilings of a 2×n board satisfies f(n) = 2·f(n−1) + f(n−3).",
vname="Linear recurrence",
spec=r'''
Count the ways to tile a `2 × n` board with `2 × 1` dominoes and L-shaped trominoes (both may be rotated). Return the count modulo
`10^9 + 7`.

**Example**
```
n = 3 → 5,   n = 1 → 1
```

**Constraints**
* `1 <= n <= 1000`
''',
approach=r'''
**Recurrence.** Tracking full and half-filled boards leads to `f(n) = 2·f(n-1) + f(n-3)` with `f(0) = 1, f(1) = 1, f(2) = 2`. Compute it
iteratively modulo `10^9 + 7` using `long`.

* Time: **O(n)** — one loop.
* Space: **O(n)** — the table (three values would also do).
''',
sc="n",
java=r'''
public class DominoTrominoTiling {

    public int numTilings(int n) {
        final long MOD = 1_000_000_007L;
        long[] f = new long[Math.max(3, n + 1)];
        f[0] = 1;
        f[1] = 1;
        f[2] = 2;
        for (int i = 3; i <= n; i++) f[i] = (2 * f[i - 1] + f[i - 3]) % MOD;
        return (int) f[n];
    }
}
''',
test=r'''
class DominoTrominoTilingTest {

    private final DominoTrominoTiling solution = new DominoTrominoTiling();

    @ParameterizedTest
    @CsvSource({"1,1", "2,2", "3,5", "4,11", "5,24", "30,312342182"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.numTilings(n));
    }
}
''',
trace=r'''
function run(n) {
  const f = [1, 1, 2];
  A.step('f(n) counts tilings of a 2 × n board. f(0) = 1 (empty board), f(1) = 1, f(2) = 2.', A.arr('f', f));
  for (let i = 3; i <= n; i++) { f.push(2 * f[i - 1] + f[i - 3]); A.step(`f(${i}) = 2 × f(${i - 1}) + f(${i - 3}) = 2 × ${f[i - 1]} + ${f[i - 3]} = ${f[i]}.`, A.arr('f', f, { hl: { [i]: 'ok', [i - 1]: 'sel', [i - 3]: 'alt' } })); }
  A.step(`${f[n]} tilings for n = ${n}.`, A.text('Result', f[n], 'ok'));
}
A.scenario('n = 6', 'board 2 × 6', () => run(6));
'''),

P(num=1318, slug="minimum-flips-to-make-a-or-b-equal-to-c", title="Minimum Flips to Make a OR b Equal to c", diff="Medium", topic="Bit Manipulation", cls="MinimumFlips",
idea="Bit by bit: if c's bit is 1, need one 1 among a and b; if it is 0, every 1 in a and b must be flipped.",
vname="Per-bit counting",
spec=r'''
Return the minimum number of single-bit flips in `a` and `b` so that `a | b == c`.

**Example**
```
a = 2, b = 6, c = 5 → 3,   a = 4, b = 2, c = 7 → 1,   a = 1, b = 2, c = 3 → 0
```

**Constraints**
* `1 <= a, b, c <= 10^9`
''',
approach=r'''
**Independent bits.** For each of 31 bits: if `c`'s bit is 1 and both `a`, `b` bits are 0, one flip; if `c`'s bit is 0, flip every 1 bit in `a`
and `b` there.

* Time: **O(1)** — 31 bits.
* Space: **O(1)** — a counter.
''',
java=r'''
public class MinimumFlips {

    public int minFlips(int a, int b, int c) {
        int flips = 0;
        for (int i = 0; i < 31; i++) {
            int x = a >> i & 1, y = b >> i & 1, z = c >> i & 1;
            if (z == 1) flips += (x | y) == 0 ? 1 : 0;
            else flips += x + y;
        }
        return flips;
    }
}
''',
test=r'''
class MinimumFlipsTest {

    private final MinimumFlips solution = new MinimumFlips();

    @ParameterizedTest
    @CsvSource({"2,6,5,3", "4,2,7,1", "1,2,3,0"})
    void flips(int a, int b, int c, int expected) {
        assertEquals(expected, solution.minFlips(a, b, c));
    }
}
''',
trace=r'''
function run(a, b, c) {
  const W = 4, bits = v => v.toString(2).padStart(W, '0').split('');
  let flips = 0; const g = [bits(a), bits(b), bits(c)];
  A.step('Compare bit by bit. Rows: a, b, c.', A.grid('bits (high → low)', g));
  for (let i = 0; i < W; i++) {
    const x = (a >> i) & 1, y = (b >> i) & 1, z = (c >> i) & 1, col = W - 1 - i;
    const need = z ? ((x | y) ? 0 : 1) : x + y; flips += need;
    A.step(`Bit ${i}: a = ${x}, b = ${y}, c = ${z}. ${z ? ((x | y) ? 'Already has a 1.' : 'Need one 1: 1 flip.') : `Both must be 0: ${x + y} flip${x + y === 1 ? '' : 's'}.`} Total ${flips}.`, A.grid('bits (high → low)', g, { hl: { [`0,${col}`]: 'cur', [`1,${col}`]: 'cur', [`2,${col}`]: need ? 'bad' : 'ok' } }), A.vars({ flips }));
  }
  A.step(`${flips} flips.`, A.text('Result', flips, 'ok'));
}
A.scenario('a = 2, b = 6, c = 5', 'three flips', () => run(2, 6, 5));
'''),

P(num=1268, slug="search-suggestions-system", title="Search Suggestions System", diff="Medium", topic="Binary Search", cls="SearchSuggestions",
idea="Sort the products; for each typed prefix, binary-search where it would start and take up to three matches from there.",
vname="Sort + binary search per prefix",
spec=r'''
As each character of `searchWord` is typed, suggest up to three products that start with the typed prefix, in lexicographic order.
Return the list of suggestions after each character.

**Example**
```
products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
→ [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
```

**Constraints**
* `1 <= products.length <= 1000`
''',
approach=r'''
**Lower bound.** Sort products. Products sharing a prefix are contiguous, so binary-search the first product `>= prefix` and take up to three
that start with the prefix.

* Time: **O(n log n + L·(log n + 3))** — sorting plus a search per prefix (string comparisons cost O(L)).
* Space: **O(n)** — the sorted copy.
''',
tc="nlogn", sc="n",
java=r'''
public class SearchSuggestions {

    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        String[] sorted = products.clone();
        Arrays.sort(sorted);
        List<List<String>> out = new ArrayList<>();
        for (int len = 1; len <= searchWord.length(); len++) {
            String prefix = searchWord.substring(0, len);
            int lo = 0, hi = sorted.length;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (sorted[mid].compareTo(prefix) < 0) lo = mid + 1; else hi = mid;
            }
            List<String> picks = new ArrayList<>();
            for (int i = lo; i < sorted.length && picks.size() < 3 && sorted[i].startsWith(prefix); i++) picks.add(sorted[i]);
            out.add(picks);
        }
        return out;
    }
}
''',
test=r'''
class SearchSuggestionsTest {

    private final SearchSuggestions solution = new SearchSuggestions();

    @Test
    void example() {
        List<String> top = List.of("mobile", "moneypot", "monitor"), mouse = List.of("mouse", "mousepad");
        assertEquals(List.of(top, top, mouse, mouse, mouse),
                solution.suggestedProducts(new String[]{"mobile", "mouse", "moneypot", "monitor", "mousepad"}, "mouse"));
    }

    @Test
    void noMatches() {
        assertEquals(List.of(List.of("havana"), List.of("havana"), List.of("havana"), List.of("havana"), List.of("havana"), List.of("havana")),
                solution.suggestedProducts(new String[]{"havana"}, "havana"));
        assertEquals(List.of(List.of(), List.of()), solution.suggestedProducts(new String[]{"abc"}, "xy"));
    }
}
''',
trace=r'''
function run(products, word) {
  const s = products.slice().sort();
  A.step('Sort the products. Products sharing a prefix sit next to each other.', A.arr('sorted products', s));
  for (let len = 1; len <= word.length; len++) {
    const pre = word.slice(0, len); let lo = 0; while (lo < s.length && s[lo] < pre) lo++;
    const picks = []; for (let i = lo; i < s.length && picks.length < 3 && s[i].startsWith(pre); i++) picks.push(i);
    A.step(`Typed "${pre}": binary search lands at index ${lo}; take up to three products starting with "${pre}".`, A.arr('sorted products', s, { hl: Object.fromEntries(s.map((p, i) => [i, picks.includes(i) ? 'ok' : p.startsWith(pre) ? 'sel' : 'dim'])) }), A.arr('suggestions', picks.map(i => s[i])));
  }
}
A.scenario('mouse', 'searchWord = "mouse"', () => run(['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse'));
'''),

P(num=901, slug="online-stock-span", title="Online Stock Span", diff="Medium", topic="Stack", cls="StockSpanner",
idea="A stack of (price, span) pairs; a new price absorbs every smaller-or-equal price on top, adding their spans.",
vname="Monotonic stack with spans",
spec=r'''
Implement `StockSpanner.next(price)`: return today's **span**, the number of consecutive days (ending today, going backward) with a price
at most today's price.

**Example**
```
next(100)=1, next(80)=1, next(60)=1, next(70)=2, next(60)=1, next(75)=4, next(85)=6
```

**Constraints**
* At most `10^4` calls.
''',
approach=r'''
**Collapse smaller days.** Keep a decreasing stack of `(price, span)`. For a new price, pop every entry with price `<=` it and add its span to
today's span; push the result.

* Time: **O(1)** — amortized per call (each day is pushed and popped once).
* Space: **O(n)** — the stack.
''',
tc="1", sc="n",
java=r'''
public class StockSpanner {

    private final Deque<int[]> stack = new ArrayDeque<>(); // {price, span}

    public int next(int price) {
        int span = 1;
        while (!stack.isEmpty() && stack.peek()[0] <= price) span += stack.pop()[1];
        stack.push(new int[]{price, span});
        return span;
    }
}
''',
test=r'''
class StockSpannerTest {

    @Test
    void example() {
        StockSpanner s = new StockSpanner();
        int[] prices = {100, 80, 60, 70, 60, 75, 85};
        int[] spans = {1, 1, 1, 2, 1, 4, 6};
        for (int i = 0; i < prices.length; i++) assertEquals(spans[i], s.next(prices[i]));
    }
}
''',
trace=r'''
A.scenario('Seven days', 'prices 100, 80, 60, 70, 60, 75, 85', () => {
  const st = [];
  for (const p of [100, 80, 60, 70, 60, 75, 85]) {
    let span = 1; const eaten = [];
    while (st.length && st[st.length - 1][0] <= p) { const [q, s] = st.pop(); span += s; eaten.push(`${q}(${s})`); }
    st.push([p, span]);
    A.step(`next(${p}): ${eaten.length ? `absorb ${eaten.join(', ')} from the stack, ` : ''}span = ${span}.`, A.stack('stack (price, span)', st.map(([q, s]) => `${q} | ${s}`)), A.text('span', span, 'ok'));
  }
});
'''),

P(num=509, slug="fibonacci-number", title="Fibonacci Number", diff="Easy", topic="1D DP", cls="FibonacciNumber",
idea="Each Fibonacci number is the sum of the previous two; keep two rolling values.",
vname="Two rolling values",
spec=r'''
`F(0) = 0`, `F(1) = 1`, `F(n) = F(n-1) + F(n-2)`. Return `F(n)`.

**Example**
```
n = 2 → 1,   n = 3 → 2,   n = 4 → 3
```

**Constraints**
* `0 <= n <= 30`
''',
approach=r'''
**Bottom-up.** Shift `(a, b)` forward `n` times.

* Time: **O(n)** — one loop.
* Space: **O(1)** — two ints.
''',
java=r'''
public class FibonacciNumber {

    public int fib(int n) {
        int a = 0, b = 1;
        for (int i = 0; i < n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return a;
    }
}
''',
test=r'''
class FibonacciNumberTest {

    private final FibonacciNumber solution = new FibonacciNumber();

    @ParameterizedTest
    @CsvSource({"0,0", "1,1", "2,1", "3,2", "4,3", "30,832040"})
    void values(int n, int expected) {
        assertEquals(expected, solution.fib(n));
    }
}
''',
trace=r'''
function run(n) {
  const f = [0, 1];
  for (let i = 2; i <= n; i++) { f.push(f[i - 1] + f[i - 2]); A.step(`F(${i}) = ${f[i - 1]} + ${f[i - 2]} = ${f[i]}.`, A.arr('F', f, { hl: { [i]: 'ok', [i - 1]: 'sel', [i - 2]: 'sel' } })); }
  A.step(`F(${n}) = ${f[n]}.`, A.text('Result', f[n], 'ok'));
}
A.scenario('n = 8', 'F(8)', () => run(8));
''',
variants=[dict(
name="Naive recursion",
idea="F(n) = F(n−1) + F(n−2) computed directly, re-solving the same subproblems many times.",
approach=r'''
**Plain recursion.** Mirrors the definition but recomputes overlapping subproblems.

* Time: **O(2ⁿ)** — the call tree roughly doubles at each level.
* Space: **O(n)** — the recursion depth.
''',
tc="exp", sc="n",
java=r'''
public class FibonacciNumber {

    public int fib(int n) {
        return n < 2 ? n : fib(n - 1) + fib(n - 2);
    }
}
''',
trace=r'''
function run(n) {
  let calls = 0; const counts = new Array(n + 1).fill(0);
  const f = k => { calls++; counts[k]++; return k < 2 ? k : f(k - 1) + f(k - 2); };
  const r = f(n);
  A.step(`Computing F(${n}) this way made ${calls} calls. The count of calls for each k shows the repeated work.`, A.arr('times F(k) was computed', counts, { hl: Object.fromEntries(counts.map((c, i) => [i, c > 1 ? 'bad' : 'ok'])) }), A.vars({ calls }));
  A.step(`F(${n}) = ${r}, but the call count grows exponentially with n.`, A.text('Result', r, 'ok'));
}
A.scenario('n = 8', 'F(8)', () => run(8));
''')]),

P(num=412, slug="fizz-buzz", title="Fizz Buzz", diff="Easy", topic="Math", cls="FizzBuzz",
idea="Check divisibility by 15 first, then by 3 and by 5.",
vname="Direct checks",
spec=r'''
Return a list of `1..n` as strings where multiples of 3 are `"Fizz"`, multiples of 5 `"Buzz"`, multiples of both `"FizzBuzz"`.

**Example**
```
n = 5 → ["1","2","Fizz","4","Buzz"]
```

**Constraints**
* `1 <= n <= 10^4`
''',
approach=r'''
**Build the label.** Append `"Fizz"` if divisible by 3 and `"Buzz"` if divisible by 5; if nothing was appended, use the number.

* Time: **O(n)** — one pass.
* Space: **O(1)** — apart from the output.
''',
sc="1",
java=r'''
public class FizzBuzz {

    public List<String> fizzBuzz(int n) {
        List<String> out = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            String s = (i % 3 == 0 ? "Fizz" : "") + (i % 5 == 0 ? "Buzz" : "");
            out.add(s.isEmpty() ? String.valueOf(i) : s);
        }
        return out;
    }
}
''',
test=r'''
class FizzBuzzTest {

    private final FizzBuzz solution = new FizzBuzz();

    @Test
    void fifteen() {
        assertEquals(List.of("1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"), solution.fizzBuzz(15));
    }
}
''',
trace=r'''
function run(n) {
  const out = [];
  for (let i = 1; i <= n; i++) { const s = (i % 3 ? '' : 'Fizz') + (i % 5 ? '' : 'Buzz') || String(i); out.push(s); A.step(`${i}: ${s === String(i) ? 'not divisible by 3 or 5' : `${i % 3 ? '' : 'divisible by 3'}${!(i % 3) && !(i % 5) ? ' and ' : ''}${i % 5 ? '' : 'divisible by 5'}`} → "${s}".`, A.arr('output', out, { hl: { [i - 1]: s === String(i) ? 'dim' : 'ok' }, noIdx: true })); }
}
A.scenario('n = 15', '1 to 15', () => run(15));
'''),

P(num=387, slug="first-unique-character-in-a-string", title="First Unique Character in a String", diff="Easy", topic="Arrays & Hashing", cls="FirstUniqueCharacter",
idea="Count every letter, then return the first index whose letter has count 1.",
vname="Counting array",
spec=r'''
Return the index of the first character of `s` that does not repeat, or `-1`.

**Example**
```
"leetcode" → 0,   "loveleetcode" → 2,   "aabb" → -1
```

**Constraints**
* `1 <= s.length <= 10^5`; lowercase letters.
''',
approach=r'''
**Two passes.** Count letters in an `int[26]`, then scan for the first letter with count 1.

* Time: **O(n)** — two passes.
* Space: **O(1)** — 26 counters.
''',
java=r'''
public class FirstUniqueCharacter {

    public int firstUniqChar(String s) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) count[c - 'a']++;
        for (int i = 0; i < s.length(); i++) {
            if (count[s.charAt(i) - 'a'] == 1) return i;
        }
        return -1;
    }
}
''',
test=r'''
class FirstUniqueCharacterTest {

    private final FirstUniqueCharacter solution = new FirstUniqueCharacter();

    @ParameterizedTest
    @CsvSource({"leetcode,0", "loveleetcode,2", "aabb,-1"})
    void finds(String s, int expected) {
        assertEquals(expected, solution.firstUniqChar(s));
    }
}
''',
trace=r'''
function run(s) {
  const cnt = {}; [...s].forEach(c => (cnt[c] = (cnt[c] || 0) + 1));
  A.step('Count every letter.', A.chars('s', s), A.map('counts', cnt));
  for (let i = 0; i < s.length; i++) {
    if (cnt[s[i]] === 1) { A.step(`'${s[i]}' at index ${i} appears once: the first unique character.`, A.chars('s', s, { hl: { [i]: 'ok' } }), A.text('Result', i, 'ok')); return; }
    A.step(`'${s[i]}' appears ${cnt[s[i]]} times.`, A.chars('s', s, { hl: { [i]: 'bad' } }));
  }
  A.step('Every character repeats.', A.text('Result', -1, 'bad'));
}
A.scenario('loveleetcode', 's = "loveleetcode"', () => run('loveleetcode'));
'''),

P(num=349, slug="intersection-of-two-arrays", title="Intersection of Two Arrays", diff="Easy", topic="Arrays & Hashing", cls="IntersectionOfTwoArrays",
idea="Put one array in a hash set; collect the other's values that are in it, each once.",
vname="Hash sets",
spec=r'''
Return the distinct values present in both `nums1` and `nums2`, in any order.

**Example**
```
[1,2,2,1], [2,2] → [2],   [4,9,5], [9,4,9,8,4] → [9,4]
```

**Constraints**
* `1 <= length <= 1000`
''',
approach=r'''
**Set membership.** Load `nums1` into a `MyHashSet`. For each value of `nums2`, if `remove` succeeds, it is common and reported once.

* Time: **O(m + n)** — linear set operations.
* Space: **O(m)** — the set.
''',
java=r'''
public class IntersectionOfTwoArrays {

    public int[] intersection(int[] nums1, int[] nums2) {
        MyHashSet<Integer> set = new MyHashSet<>();
        for (int x : nums1) set.add(x);
        List<Integer> out = new ArrayList<>();
        for (int x : nums2) {
            if (set.remove(x)) out.add(x);
        }
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
}
''',
test=r'''
class IntersectionOfTwoArraysTest {

    private final IntersectionOfTwoArrays solution = new IntersectionOfTwoArrays();

    private static Set<Integer> set(int[] a) {
        Set<Integer> s = new HashSet<>();
        for (int x : a) s.add(x);
        return s;
    }

    @Test
    void examples() {
        assertArrayEquals(new int[]{2}, solution.intersection(new int[]{1, 2, 2, 1}, new int[]{2, 2}));
        assertEquals(Set.of(4, 9), set(solution.intersection(new int[]{4, 9, 5}, new int[]{9, 4, 9, 8, 4})));
    }
}
''',
trace=r'''
function run(a, b) {
  const s = new Set(a), out = [];
  A.step('Put nums1 into a hash set.', A.arr('nums1', a), A.hashTable('set', s));
  b.forEach((x, i) => { const hit = s.delete(x); if (hit) out.push(x); A.step(hit ? `${x} is in the set: report it and remove it so it is not reported twice.` : `${x} is ${out.includes(x) ? 'already reported' : 'not in nums1'}.`, A.arr('nums2', b, { hl: { [i]: hit ? 'ok' : 'dim' } }), A.hashTable('set', s), A.arr('result', out)); });
}
A.scenario('Repeated values', 'nums1 = [4,9,5], nums2 = [9,4,9,8,4]', () => run([4, 9, 5], [9, 4, 9, 8, 4]));
'''),

P(num=350, slug="intersection-of-two-arrays-ii", title="Intersection of Two Arrays II", diff="Easy", topic="Arrays & Hashing", cls="IntersectionOfTwoArraysII",
idea="Count nums1 in a hash map; each value of nums2 that still has a count left is matched once.",
vname="Hash map counts",
spec=r'''
Return the intersection of `nums1` and `nums2`, where each value appears as many times as it shows in **both** arrays, in any order.

**Example**
```
[1,2,2,1], [2,2] → [2,2],   [4,9,5], [9,4,9,8,4] → [4,9]
```

**Constraints**
* `1 <= length <= 1000`
''',
approach=r'''
**Counting.** Count `nums1` in a `MyHashMap`. For each value of `nums2` with a positive count, output it and decrement the count.

* Time: **O(m + n)** — linear map operations.
* Space: **O(m)** — the map.
''',
java=r'''
public class IntersectionOfTwoArraysII {

    public int[] intersect(int[] nums1, int[] nums2) {
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int x : nums1) count.merge(x, 1, Integer::sum);
        List<Integer> out = new ArrayList<>();
        for (int x : nums2) {
            int c = count.getOrDefault(x, 0);
            if (c > 0) {
                out.add(x);
                count.put(x, c - 1);
            }
        }
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
}
''',
test=r'''
class IntersectionOfTwoArraysIITest {

    private final IntersectionOfTwoArraysII solution = new IntersectionOfTwoArraysII();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 2}, solution.intersect(new int[]{1, 2, 2, 1}, new int[]{2, 2}));
        int[] r = solution.intersect(new int[]{4, 9, 5}, new int[]{9, 4, 9, 8, 4});
        Arrays.sort(r);
        assertArrayEquals(new int[]{4, 9}, r);
    }
}
''',
trace=r'''
function run(a, b) {
  const cnt = new Map(); a.forEach(x => cnt.set(x, (cnt.get(x) || 0) + 1)); const out = [];
  A.step('Count the values of nums1.', A.arr('nums1', a), A.hashTable('counts', cnt));
  b.forEach((x, i) => { const c = cnt.get(x) || 0; if (c) { cnt.set(x, c - 1); out.push(x); } A.step(c ? `${x} still has ${c} copy${c > 1 ? 'ies' : ''} in nums1: match one.` : `No copy of ${x} left in nums1.`, A.arr('nums2', b, { hl: { [i]: c ? 'ok' : 'dim' } }), A.hashTable('counts', cnt, { hl: x }), A.arr('result', out)); });
}
A.scenario('Repeats', 'nums1 = [1,2,2,1], nums2 = [2,2]', () => run([1, 2, 2, 1], [2, 2]));
'''),
]
