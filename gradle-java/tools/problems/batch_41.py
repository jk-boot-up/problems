PROBLEMS = [
P(num=318, slug="maximum-product-of-word-lengths", title="Maximum Product of Word Lengths", diff="Medium", topic="Bit Manipulation", cls="MaxProductWordLengths",
idea="A 26-bit mask per word turns 'no common letters' into a single AND.",
vname="Letter bitmasks",
spec=r'''
Return the maximum value of `length(a) * length(b)` over two words of `words` that share **no** letters. Return 0 if no such pair exists.

**Example**
```
["abcw","baz","foo","bar","xtfn","abcdef"] → 16   ("abcw", "xtfn")
["a","ab","abc","d","cd","bcd","abcd"]     → 4    ("ab", "cd")
["a","aa","aaa","aaaa"]                    → 0
```

**Constraints**
* `2 <= words.length <= 1000`, lower-case words of length at most 1000
''',
approach=r'''
**Masks.** Bit `c` of `mask[i]` is set when word `i` contains letter `c`. Two words share no letter exactly when `mask[i] & mask[j] == 0`.
Compare every pair in O(1).

* Time: **O(L + n²)** — `L` letters to build the masks, then all pairs.
* Space: **O(n)** — one mask per word.
''',
tc="n2", sc="n",
java=r'''
public class MaxProductWordLengths {

    public int maxProduct(String[] words) {
        int n = words.length;
        int[] mask = new int[n];
        for (int i = 0; i < n; i++) for (char c : words[i].toCharArray()) mask[i] |= 1 << (c - 'a');
        int best = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                if ((mask[i] & mask[j]) == 0) best = Math.max(best, words[i].length() * words[j].length());
        return best;
    }
}
''',
test=r'''
class MaxProductWordLengthsTest {

    private final MaxProductWordLengths solution = new MaxProductWordLengths();

    @Test
    void examples() {
        assertEquals(16, solution.maxProduct(new String[]{"abcw", "baz", "foo", "bar", "xtfn", "abcdef"}));
        assertEquals(4, solution.maxProduct(new String[]{"a", "ab", "abc", "d", "cd", "bcd", "abcd"}));
        assertEquals(0, solution.maxProduct(new String[]{"a", "aa", "aaa", "aaaa"}));
    }
}
''',
trace=r'''
function run(words) {
  const mask = words.map(w => [...w].reduce((m, c) => m | (1 << (c.charCodeAt(0) - 97)), 0));
  const bits = m => [...'abcdefghijklmnopqrstuvwxyz'].filter((_, i) => m & (1 << i)).join('');
  A.step('Turn each word into a set of letters stored as bits.', A.arr('words', words), A.arr('letters in mask', mask.map(bits)));
  let best = 0, pair = null;
  for (let i = 0; i < words.length; i++) for (let j = i + 1; j < words.length; j++) {
    if (mask[i] & mask[j]) continue;
    const p = words[i].length * words[j].length, better = p > best;
    if (better) { best = p; pair = [i, j]; }
    A.step(`"${words[i]}" & "${words[j]}" = 0: no shared letter. Product ${words[i].length} × ${words[j].length} = ${p}${better ? ', the best so far' : ''}.`, A.arr('words', words, { hl: { [i]: better ? 'ok' : 'cur', [j]: better ? 'ok' : 'cur' } }), A.vars({ best }));
  }
  A.step(pair ? `Best pair: "${words[pair[0]]}" and "${words[pair[1]]}", product ${best}.` : 'Every pair shares a letter.', A.text('Result', best, best ? 'ok' : 'bad'));
}
A.scenario('Classic', '["abcw","baz","foo","bar","xtfn","abcdef"]', () => run(['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef']));
A.scenario('Small words', '["a","ab","abc","d","cd","bcd"]', () => run(['a', 'ab', 'abc', 'd', 'cd', 'bcd']));
'''),

P(num=319, slug="bulb-switcher", title="Bulb Switcher", diff="Medium", topic="Math", cls="BulbSwitcher",
idea="Bulb i is toggled once per divisor; only perfect squares have an odd number of divisors.",
vname="Count perfect squares",
spec=r'''
There are `n` bulbs, all off. In round `i` (for `i = 1..n`) you toggle every `i`-th bulb. Return how many bulbs are on after `n` rounds.

**Example**
```
n = 3 → 1
n = 0 → 0
n = 1 → 1
```

**Constraints**
* `0 <= n <= 10^9`
''',
approach=r'''
**Divisors pair up.** Bulb `k` is toggled in every round `d` that divides `k`. Divisors come in pairs `d` and `k / d`, except when
`d = √k`. So bulb `k` ends on exactly when `k` is a perfect square, and there are `⌊√n⌋` of those up to `n`.

* Time: **O(1)**.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class BulbSwitcher {

    public int bulbSwitch(int n) {
        int r = (int) Math.sqrt(n);
        while ((long) r * r > n) r--;
        while ((long) (r + 1) * (r + 1) <= n) r++;
        return r;
    }
}
''',
test=r'''
class BulbSwitcherTest {

    private final BulbSwitcher solution = new BulbSwitcher();

    @ParameterizedTest
    @CsvSource({"0,0", "1,1", "3,1", "4,2", "10,3", "99,9", "100,10", "1000000000,31622"})
    void bulbs(int n, int expected) {
        assertEquals(expected, solution.bulbSwitch(n));
    }

    @Test
    void matchesSimulation() {
        for (int n = 0; n <= 60; n++) {
            boolean[] on = new boolean[n + 1];
            for (int i = 1; i <= n; i++) for (int k = i; k <= n; k += i) on[k] = !on[k];
            int c = 0;
            for (int k = 1; k <= n; k++) if (on[k]) c++;
            assertEquals(c, solution.bulbSwitch(n));
        }
    }
}
''',
trace=r'''
function run(n) {
  const on = new Array(n).fill(false), view = () => A.arr('bulbs 1..n', on.map(b => (b ? 'on' : 'off')), { noIdx: true, hl: Object.fromEntries(on.map((b, i) => [i, b ? 'ok' : 'dim'])) });
  A.step(`${n} bulbs start off.`, view());
  for (let r = 1; r <= n; r++) {
    for (let k = r; k <= n; k += r) on[k - 1] = !on[k - 1];
    if (r <= 4 || r === n) A.step(`Round ${r}: toggle every ${r === 1 ? '' : r + '-th '}bulb${r === 1 ? '' : ''}.`, view(), A.vars({ round: r, on: on.filter(Boolean).length }));
  }
  const sq = on.map((b, i) => (b ? i + 1 : 0)).filter(Boolean);
  A.step(`The bulbs left on are ${sq.join(', ')}: the perfect squares, whose divisors cannot all pair up.`, view());
  A.step(`⌊√${n}⌋ = ${Math.floor(Math.sqrt(n))}.`, A.text('Result', Math.floor(Math.sqrt(n)), 'ok'));
}
A.scenario('Ten bulbs', 'n = 10', () => run(10));
'''),

P(num=326, slug="power-of-three", title="Power of Three", diff="Easy", topic="Math", cls="PowerOfThree",
idea="3^19 is the largest power of three in an int, and its only divisors are smaller powers of three.",
vname="Divisor of 3^19",
spec=r'''
Return `true` if `n` is a power of three (`n == 3^x` for some integer `x >= 0`).

**Example**
```
27 → true
0  → false
-1 → false
45 → false
```

**Constraints**
* `-2^31 <= n <= 2^31 - 1`
''',
approach=r'''
**One modulo.** `3^19 = 1162261467` is the biggest power of three that fits in an `int`. Since 3 is prime, the positive divisors of
`3^19` are exactly `3^0 … 3^19`. So `n` is a power of three iff `n > 0` and `1162261467 % n == 0`.

* Time: **O(1)**.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class PowerOfThree {

    public boolean isPowerOfThree(int n) {
        return n > 0 && 1162261467 % n == 0;
    }
}
''',
test=r'''
class PowerOfThreeTest {

    private final PowerOfThree solution = new PowerOfThree();

    @ParameterizedTest
    @CsvSource({"1,true", "3,true", "27,true", "1162261467,true", "0,false", "-1,false", "-27,false", "45,false", "6,false", "2147483647,false"})
    void check(int n, boolean expected) {
        assertEquals(expected, solution.isPowerOfThree(n));
    }
}
''',
trace=r'''
function run(n) {
  const BIG = 1162261467;
  A.step(`Is ${n} a power of three? The largest power of three in an int is 3^19 = ${BIG}.`, A.vars({ n, '3^19': BIG }));
  if (n <= 0) { A.step(`${n} is not positive, so it is not a power of three.`, A.text('Result', 'false', 'bad')); return; }
  A.step('3 is prime, so the only numbers dividing 3^19 evenly are 3^0, 3^1, …, 3^19.', A.arr('powers of 3', [1, 3, 9, 27, 81, 243, '…', BIG]));
  const r = BIG % n;
  A.step(`${BIG} mod ${n} = ${r}.`, A.vars({ remainder: r }));
  A.step(r === 0 ? `${n} divides 3^19, so it is a power of three.` : `${n} does not divide 3^19, so it has some other factor.`, A.text('Result', String(r === 0), r === 0 ? 'ok' : 'bad'));
}
A.scenario('Power', 'n = 27', () => run(27));
A.scenario('Not a power', 'n = 45', () => run(45));
''',
variants=[dict(
name="Repeated division",
idea="Divide by 3 while it divides evenly; a power of three ends at 1.",
approach=r'''
**Loop.** For positive `n`, divide by 3 while `n % 3 == 0`, then check `n == 1`.

* Time: **O(log n)** — at most 19 divisions.
* Space: **O(1)**.
''',
tc="log", sc="1",
java=r'''
public class PowerOfThree {

    public boolean isPowerOfThree(int n) {
        if (n <= 0) return false;
        while (n % 3 == 0) n /= 3;
        return n == 1;
    }
}
''',
trace=r'''
function run(n) {
  A.step(`Start with ${n}.`, A.vars({ n }));
  let m = n;
  while (m > 0 && m % 3 === 0) { A.step(`${m} is divisible by 3 → ${m / 3}.`, A.vars({ n: m / 3 })); m /= 3; }
  A.step(`${m} is not divisible by 3.`, A.vars({ n: m }));
  A.step(m === 1 ? 'We reached 1: a power of three.' : `We stopped at ${m}, not 1.`, A.text('Result', String(m === 1), m === 1 ? 'ok' : 'bad'));
}
A.scenario('Power', 'n = 27', () => run(27));
''')]),

P(num=341, slug="flatten-nested-list-iterator", title="Flatten Nested List Iterator", diff="Medium", topic="Stack", cls="NestedIterator",
idea="Keep a stack of iterators; dive into lists lazily and only stop when an integer is on top.",
vname="Lazy stack of iterators",
spec=r'''
A nested list holds integers or other nested lists. Implement an iterator over all of its integers, in order.

* `NestedIterator(List<NestedInteger> nestedList)`
* `int next()`, `boolean hasNext()`

`NestedInteger` (provided in this project) has `isInteger()`, `getInteger()` and `getList()`.

**Example**
```
[[1,1],2,[1,1]] → 1,1,2,1,1
[1,[4,[6]]]     → 1,4,6
[[],[[]]]       → (nothing)
```

**Constraints**
* Up to 500 elements; integers in `[-10^6, 10^6]`
''',
approach=r'''
**Stack of iterators.** Push an iterator over the top-level list. `hasNext` does the real work: while no integer is ready, look at the top
iterator. If it is exhausted, pop it; if its next item is a list, push that list's iterator; if it is an integer, keep it ready. Empty
lists simply get popped. `next` returns the ready integer.

* Time: **O(1)** amortised — each item and each list is visited once over the whole iteration.
* Space: **O(d)** — one iterator per nesting level.
''',
tc="1", sc="n",
java=r'''
interface NestedInteger {

    boolean isInteger();

    Integer getInteger();

    List<NestedInteger> getList();

    static NestedInteger of(int value) {
        return new NestedInteger() {
            public boolean isInteger() { return true; }
            public Integer getInteger() { return value; }
            public List<NestedInteger> getList() { return null; }
        };
    }

    static NestedInteger list(NestedInteger... items) {
        List<NestedInteger> l = List.of(items);
        return new NestedInteger() {
            public boolean isInteger() { return false; }
            public Integer getInteger() { return null; }
            public List<NestedInteger> getList() { return l; }
        };
    }
}

public class NestedIterator implements Iterator<Integer> {

    private final Deque<Iterator<NestedInteger>> stack = new ArrayDeque<>();
    private Integer ready;

    public NestedIterator(List<NestedInteger> nestedList) {
        stack.push(nestedList.iterator());
    }

    @Override
    public boolean hasNext() {
        while (ready == null && !stack.isEmpty()) {
            Iterator<NestedInteger> top = stack.peek();
            if (!top.hasNext()) {
                stack.pop();
                continue;
            }
            NestedInteger item = top.next();
            if (item.isInteger()) ready = item.getInteger();
            else stack.push(item.getList().iterator());
        }
        return ready != null;
    }

    @Override
    public Integer next() {
        if (!hasNext()) throw new NoSuchElementException();
        Integer v = ready;
        ready = null;
        return v;
    }
}
''',
test=r'''
class NestedIteratorTest {

    private static NestedInteger i(int v) { return NestedInteger.of(v); }

    private static NestedInteger l(NestedInteger... items) { return NestedInteger.list(items); }

    private List<Integer> drain(List<NestedInteger> input) {
        NestedIterator it = new NestedIterator(input);
        List<Integer> out = new ArrayList<>();
        while (it.hasNext()) out.add(it.next());
        return out;
    }

    @Test
    void examples() {
        assertEquals(List.of(1, 1, 2, 1, 1), drain(List.of(l(i(1), i(1)), i(2), l(i(1), i(1)))));
        assertEquals(List.of(1, 4, 6), drain(List.of(i(1), l(i(4), l(i(6))))));
        assertEquals(List.of(), drain(List.of(l(), l(l()))));
        assertEquals(List.of(0, -3), drain(List.of(l(l(l(i(0)))), l(), i(-3))));
    }
}
''',
trace=r'''
function run(data) {
  const show = x => (Array.isArray(x) ? `[${x.map(show).join(',')}]` : String(x));
  const stack = [{ list: data, i: 0 }], out = [];
  const view = () => A.stack('iterator stack (list · position)', stack.map(f => `${show(f.list)} · ${f.i}`));
  A.step(`Start with one iterator over ${show(data)}.`, view());
  while (stack.length) {
    const top = stack[stack.length - 1];
    if (top.i >= top.list.length) { stack.pop(); A.step(`${show(top.list)} is used up: pop its iterator.`, view(), A.arr('output', out)); continue; }
    const item = top.list[top.i++];
    if (Array.isArray(item)) { stack.push({ list: item, i: 0 }); A.step(`Next item is the list ${show(item)}: push an iterator into it.`, view(), A.arr('output', out)); }
    else { out.push(item); A.step(`Next item is the integer ${item}: hasNext() is true and next() returns it.`, view(), A.arr('output', out, { hl: { [out.length - 1]: 'ok' } })); }
  }
  A.step(`The stack is empty, so hasNext() is false. Output: ${out.join(', ') || 'nothing'}.`, A.arr('output', out));
}
A.scenario('Deep nesting', '[1,[4,[6]]]', () => run([1, [4, [6]]]));
A.scenario('Empty lists', '[[],[[]],3]', () => run([[], [[]], 3]));
''',
variants=[dict(
name="Flatten up front",
idea="Recursively copy every integer into a plain list in the constructor, then iterate over it.",
approach=r'''
**Eager flattening.** A recursive walk appends integers to a list; `next` and `hasNext` are an index into it. Simple, but it does all the
work and stores every integer before the first `next`.

* Time: **O(N)** — in the constructor, then O(1) per call.
* Space: **O(N)** — the flattened copy.
''',
tc="1", sc="n",
java=r'''
interface NestedInteger {

    boolean isInteger();

    Integer getInteger();

    List<NestedInteger> getList();

    static NestedInteger of(int value) {
        return new NestedInteger() {
            public boolean isInteger() { return true; }
            public Integer getInteger() { return value; }
            public List<NestedInteger> getList() { return null; }
        };
    }

    static NestedInteger list(NestedInteger... items) {
        List<NestedInteger> l = List.of(items);
        return new NestedInteger() {
            public boolean isInteger() { return false; }
            public Integer getInteger() { return null; }
            public List<NestedInteger> getList() { return l; }
        };
    }
}

public class NestedIterator implements Iterator<Integer> {

    private final List<Integer> flat = new ArrayList<>();
    private int pos;

    public NestedIterator(List<NestedInteger> nestedList) {
        flatten(nestedList);
    }

    private void flatten(List<NestedInteger> list) {
        for (NestedInteger item : list) {
            if (item.isInteger()) flat.add(item.getInteger());
            else flatten(item.getList());
        }
    }

    @Override
    public boolean hasNext() {
        return pos < flat.size();
    }

    @Override
    public Integer next() {
        if (!hasNext()) throw new NoSuchElementException();
        return flat.get(pos++);
    }
}
''',
trace=r'''
function run(data) {
  const show = x => (Array.isArray(x) ? `[${x.map(show).join(',')}]` : String(x)), flat = [];
  A.step(`The constructor walks ${show(data)} recursively.`, A.text('Input', show(data)));
  (function walk(l, depth) { l.forEach(x => { if (Array.isArray(x)) walk(x, depth + 1); else { flat.push(x); A.step(`Found ${x} at depth ${depth}: append it.`, A.arr('flattened', flat, { hl: { [flat.length - 1]: 'ok' } })); } }); })(data, 0);
  A.step('Iteration is now just an index moving over this list.', A.arr('flattened', flat, { ptr: { 0: 'pos' } }));
}
A.scenario('Deep nesting', '[1,[4,[6]]]', () => run([1, [4, [6]]]));
''')]),

P(num=342, slug="power-of-four", title="Power of Four", diff="Easy", topic="Bit Manipulation", cls="PowerOfFour",
idea="A power of four is a power of two whose single 1-bit sits at an even position.",
vname="Single bit at an even position",
spec=r'''
Return `true` if `n` is a power of four.

**Example**
```
16 → true
5  → false
1  → true
```

**Constraints**
* `-2^31 <= n <= 2^31 - 1`
''',
approach=r'''
**Two bit tests.** `n > 0 && (n & (n - 1)) == 0` checks for a single 1-bit. Powers of four have it at bit 0, 2, 4, …, so it must also
overlap the mask `0x55555555` (binary `…0101`).

* Time: **O(1)**.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class PowerOfFour {

    public boolean isPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && (n & 0x55555555) != 0;
    }
}
''',
test=r'''
class PowerOfFourTest {

    private final PowerOfFour solution = new PowerOfFour();

    @ParameterizedTest
    @CsvSource({"1,true", "4,true", "16,true", "1073741824,true", "2,false", "8,false", "5,false", "0,false", "-4,false", "-2147483648,false"})
    void check(int n, boolean expected) {
        assertEquals(expected, solution.isPowerOfFour(n));
    }
}
''',
trace=r'''
function run(n) {
  const bits = v => (v >>> 0).toString(2).padStart(8, '0').slice(-8);
  A.step(`Is ${n} a power of four? Look at its bits.`, A.chars(`${n}`, bits(n)));
  const single = n > 0 && (n & (n - 1)) === 0;
  A.step(single ? 'Exactly one bit is set, so it is a power of two.' : 'It is not a power of two, so it cannot be a power of four.', A.chars(`${n}`, bits(n)), A.vars({ 'n & (n − 1)': n > 0 ? n & (n - 1) : '—' }));
  const even = (n & 0x55555555) !== 0;
  A.step(`The mask 0x55555555 has 1s at even positions (…01010101). ${n} & mask = ${n & 0x55555555}.`, A.chars('mask (low byte)', bits(0x55)), A.chars(`${n}`, bits(n), { hl: Object.fromEntries([...bits(n)].map((b, i) => [i, b === '1' ? (((7 - i) % 2 === 0) ? 'ok' : 'bad') : ''])) }));
  const ans = single && even;
  A.step(ans ? 'The bit is at an even position: a power of four.' : single ? 'The bit is at an odd position: a power of two but not of four.' : 'Not a power of four.', A.text('Result', String(ans), ans ? 'ok' : 'bad'));
}
A.scenario('Power of four', 'n = 16', () => run(16));
A.scenario('Only a power of two', 'n = 8', () => run(8));
'''),

P(num=343, slug="integer-break", title="Integer Break", diff="Medium", topic="Math", cls="IntegerBreak",
idea="Break into as many 3s as possible, using a 4 (= 2 + 2) instead of 3 + 1 at the end.",
vname="Greedy threes",
spec=r'''
Break a positive integer `n` into the sum of **at least two** positive integers and maximise their product. Return that product.

**Example**
```
n = 2  → 1   (1 + 1)
n = 10 → 36  (3 + 3 + 4)
```

**Constraints**
* `2 <= n <= 58`
''',
approach=r'''
**Threes.** Any part `p >= 5` is better split (`2(p - 2) > p`), and `4 = 2 + 2` gives the same product, so parts are 2s and 3s. Three 2s
(product 8) lose to two 3s (product 9), so use as many 3s as possible, finishing with 2, 4 or nothing. `n = 2` and `n = 3` must still
split, giving `n - 1`.

* Time: **O(n)** — at most `n / 3` multiplications.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class IntegerBreak {

    public int integerBreak(int n) {
        if (n <= 3) return n - 1;
        int product = 1;
        while (n > 4) {
            product *= 3;
            n -= 3;
        }
        return product * n;
    }
}
''',
test=r'''
class IntegerBreakTest {

    private final IntegerBreak solution = new IntegerBreak();

    @ParameterizedTest
    @CsvSource({"2,1", "3,2", "4,4", "5,6", "6,9", "7,12", "8,18", "10,36", "58,1549681956"})
    void products(int n, int expected) {
        assertEquals(expected, solution.integerBreak(n));
    }
}
''',
trace=r'''
function run(n) {
  A.step(`Split ${n} into parts with the largest product. Parts of 5 or more are worth splitting, and 3s beat 2s.`, A.vars({ n }));
  if (n <= 3) { A.step(`${n} must still be split into at least two parts: ${n - 1}.`, A.text('Result', n - 1, 'ok')); return; }
  const parts = []; let m = n, p = 1;
  while (m > 4) { parts.push(3); p *= 3; m -= 3; A.step(`Take a 3. ${m} left; product so far ${p}.`, A.arr('parts', parts, { hl: { [parts.length - 1]: 'cur' } }), A.vars({ left: m, product: p })); }
  parts.push(m); p *= m;
  A.step(`${m} is left. ${m === 4 ? 'Keep it as 4 (2 + 2 gives 4 too, better than 3 + 1).' : `Use it as a final ${m}.`}`, A.arr('parts', parts, { hl: { [parts.length - 1]: 'ok' } }));
  A.step(`${parts.join(' × ')} = ${p}.`, A.text('Result', p, 'ok'));
}
A.scenario('Ten', 'n = 10', () => run(10));
A.scenario('Eleven', 'n = 11', () => run(11));
''',
variants=[dict(
name="Dynamic programming",
idea="best[i] is the largest product for i; the first part j combines with either i − j itself or its best split.",
approach=r'''
**DP.** `best[i] = max over j in 1..i-1 of j * max(i - j, best[i - j])`: after taking a first part `j`, either keep the rest whole or
break it further.

* Time: **O(n²)** — `n` values, each trying `n` first parts.
* Space: **O(n)** — the table.
''',
tc="n2", sc="n",
java=r'''
public class IntegerBreak {

    public int integerBreak(int n) {
        int[] best = new int[n + 1];
        best[1] = 1;
        for (int i = 2; i <= n; i++)
            for (int j = 1; j < i; j++) best[i] = Math.max(best[i], j * Math.max(i - j, best[i - j]));
        return best[n];
    }
}
''',
trace=r'''
function run(n) {
  const best = new Array(n + 1).fill(0); best[1] = 1;
  A.step('best[i] = the biggest product for i, using at least two parts.', A.arr('best', best));
  for (let i = 2; i <= n; i++) {
    let arg = 1;
    for (let j = 1; j < i; j++) { const v = j * Math.max(i - j, best[i - j]); if (v > best[i]) { best[i] = v; arg = j; } }
    A.step(`best[${i}] = ${best[i]}: first part ${arg}, then ${i - arg >= best[i - arg] ? `${i - arg} whole` : `the best split of ${i - arg}`}.`, A.arr('best', best, { hl: { [i]: 'ok', [i - arg]: 'cur' } }));
  }
  A.step(`Answer: best[${n}] = ${best[n]}.`, A.text('Result', best[n], 'ok'));
}
A.scenario('Ten', 'n = 10', () => run(10));
''')]),

P(num=367, slug="valid-perfect-square", title="Valid Perfect Square", diff="Easy", topic="Binary Search", cls="ValidPerfectSquare",
idea="Binary search for an integer whose square is exactly num.",
vname="Binary search on the root",
spec=r'''
Return `true` if `num` is a perfect square, without using a built-in square root.

**Example**
```
16 → true
14 → false
```

**Constraints**
* `1 <= num <= 2^31 - 1`
''',
approach=r'''
**Search the root.** The root, if any, is between 1 and 46340 (`46341² > 2^31`). Binary search on that range, squaring `mid` as a
`long` and comparing with `num`.

* Time: **O(log n)**.
* Space: **O(1)**.
''',
tc="log", sc="1",
java=r'''
public class ValidPerfectSquare {

    public boolean isPerfectSquare(int num) {
        long lo = 1, hi = Math.min(num, 46340);
        while (lo <= hi) {
            long mid = (lo + hi) >>> 1, sq = mid * mid;
            if (sq == num) return true;
            if (sq < num) lo = mid + 1;
            else hi = mid - 1;
        }
        return false;
    }
}
''',
test=r'''
class ValidPerfectSquareTest {

    private final ValidPerfectSquare solution = new ValidPerfectSquare();

    @ParameterizedTest
    @CsvSource({"1,true", "4,true", "16,true", "2147395600,true", "2,false", "14,false", "2147483647,false", "808201,true"})
    void check(int num, boolean expected) {
        assertEquals(expected, solution.isPerfectSquare(num));
    }
}
''',
trace=r'''
function run(num) {
  let lo = 1, hi = Math.min(num, 46340);
  A.step(`Look for an integer whose square is ${num}, between ${lo} and ${hi}.`, A.vars({ num, lo, hi }));
  while (lo <= hi) {
    const mid = Math.floor((lo + hi) / 2), sq = mid * mid;
    if (sq === num) { A.step(`${mid}² = ${sq}: found it.`, A.vars({ lo, hi, mid, 'mid²': sq }), A.text('Result', 'true', 'ok')); return; }
    A.step(`${mid}² = ${sq} is ${sq < num ? 'too small: search above' : 'too big: search below'} ${mid}.`, A.vars({ lo, hi, mid, 'mid²': sq }));
    if (sq < num) lo = mid + 1; else hi = mid - 1;
  }
  A.step(`The range is empty: no integer squares to ${num}.`, A.text('Result', 'false', 'bad'));
}
A.scenario('Square', 'num = 144', () => run(144));
A.scenario('Not a square', 'num = 14', () => run(14));
'''),

P(num=376, slug="wiggle-subsequence", title="Wiggle Subsequence", diff="Medium", topic="Greedy", cls="WiggleSubsequence",
idea="Track the longest wiggle ending with a rise and the longest ending with a fall.",
vname="Up/down greedy",
spec=r'''
A **wiggle sequence** has differences that strictly alternate between positive and negative (a single element, or two different
elements, also count). Return the length of the longest wiggle **subsequence** of `nums`.

**Example**
```
[1,7,4,9,2,5]               → 6
[1,17,5,10,13,15,10,5,16,8] → 7
[1,2,3,4,5,6,7,8,9]         → 2
```

**Constraints**
* `1 <= nums.length <= 1000`
''',
approach=r'''
**Two counters.** `up` is the longest wiggle so far ending with a rise, `down` the longest ending with a fall. A rise extends a sequence
that last fell: `up = down + 1`; a fall sets `down = up + 1`; equal neighbours change nothing. This is the same as counting the turning
points of the sequence.

* Time: **O(n)** — one pass.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class WiggleSubsequence {

    public int wiggleMaxLength(int[] nums) {
        int up = 1, down = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) up = down + 1;
            else if (nums[i] < nums[i - 1]) down = up + 1;
        }
        return Math.max(up, down);
    }
}
''',
test=r'''
class WiggleSubsequenceTest {

    private final WiggleSubsequence solution = new WiggleSubsequence();

    @Test
    void examples() {
        assertEquals(6, solution.wiggleMaxLength(new int[]{1, 7, 4, 9, 2, 5}));
        assertEquals(7, solution.wiggleMaxLength(new int[]{1, 17, 5, 10, 13, 15, 10, 5, 16, 8}));
        assertEquals(2, solution.wiggleMaxLength(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9}));
        assertEquals(1, solution.wiggleMaxLength(new int[]{0, 0}));
        assertEquals(1, solution.wiggleMaxLength(new int[]{5}));
        assertEquals(3, solution.wiggleMaxLength(new int[]{3, 3, 3, 2, 5}));
    }
}
''',
trace=r'''
function run(nums) {
  let up = 1, down = 1;
  A.step('up / down: the longest wiggle so far ending with a rise / with a fall. A single number counts as 1.', A.arr('nums', nums, { hl: { 0: 'cur' } }), A.vars({ up, down }));
  for (let i = 1; i < nums.length; i++) {
    let say;
    if (nums[i] > nums[i - 1]) { up = down + 1; say = `${nums[i - 1]} → ${nums[i]} rises: extend a sequence that fell. up = down + 1 = ${up}.`; }
    else if (nums[i] < nums[i - 1]) { down = up + 1; say = `${nums[i - 1]} → ${nums[i]} falls: extend a sequence that rose. down = up + 1 = ${down}.`; }
    else say = `${nums[i]} equals the previous value: nothing changes.`;
    A.step(say, A.arr('nums', nums, { hl: { [i - 1]: 'dim', [i]: 'cur' } }), A.vars({ up, down }));
  }
  A.step(`Longest wiggle: max(${up}, ${down}) = ${Math.max(up, down)}.`, A.text('Result', Math.max(up, down), 'ok'));
}
A.scenario('Full wiggle', '[1,7,4,9,2,5]', () => run([1, 7, 4, 9, 2, 5]));
A.scenario('Runs and ties', '[1,17,5,10,13,15,10,5,16,8]', () => run([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]));
'''),

P(num=377, slug="combination-sum-iv", title="Combination Sum IV", diff="Medium", topic="Dynamic Programming", cls="CombinationSumIV",
idea="Order matters, so ways(t) sums ways(t − x) over every choice x of the last number.",
vname="DP over the target",
spec=r'''
Given distinct positive integers `nums` and a `target`, return the number of **ordered** sequences of numbers from `nums` (repeats allowed)
that add up to `target`. The answer fits in a 32-bit integer.

**Example**
```
nums = [1,2,3], target = 4 → 7
   (1,1,1,1) (1,1,2) (1,2,1) (1,3) (2,1,1) (2,2) (3,1)
nums = [9], target = 3 → 0
```

**Constraints**
* `1 <= nums.length <= 200`, `1 <= nums[i], target <= 1000`
''',
approach=r'''
**Last element.** `ways[0] = 1` (the empty sequence). For `t = 1..target`, every sequence summing to `t` ends in some `x`, so
`ways[t] = Σ ways[t - x]` over `x <= t`. Some unused intermediate values can overflow an `int`; Java's wrap-around arithmetic is exact
modulo `2^32`, so the guaranteed-small final answer is still correct.

* Time: **O(target · n)**.
* Space: **O(target)**.
''',
tc="n2", sc="n",
java=r'''
public class CombinationSumIV {

    public int combinationSum4(int[] nums, int target) {
        int[] ways = new int[target + 1];
        ways[0] = 1;
        for (int t = 1; t <= target; t++)
            for (int x : nums) if (x <= t) ways[t] += ways[t - x];
        return ways[target];
    }
}
''',
test=r'''
class CombinationSumIVTest {

    private final CombinationSumIV solution = new CombinationSumIV();

    @Test
    void examples() {
        assertEquals(7, solution.combinationSum4(new int[]{1, 2, 3}, 4));
        assertEquals(0, solution.combinationSum4(new int[]{9}, 3));
        assertEquals(1, solution.combinationSum4(new int[]{1}, 1));
        assertEquals(181997601, solution.combinationSum4(new int[]{1, 2, 3}, 32));
        assertEquals(1132436852, solution.combinationSum4(new int[]{2, 1, 3}, 35));
    }
}
''',
trace=r'''
function run(nums, target) {
  const w = new Array(target + 1).fill(0); w[0] = 1;
  A.step('ways[0] = 1: the empty sequence. Every longer sequence is a shorter one plus a last number.', A.arr('nums', nums), A.arr('ways', w, { hl: { 0: 'ok' } }));
  for (let t = 1; t <= target; t++) {
    const used = nums.filter(x => x <= t), hl = { [t]: 'ok' };
    used.forEach(x => { w[t] += w[t - x]; hl[t - x] = 'cur'; });
    A.step(`ways[${t}] = ${used.length ? used.map(x => `ways[${t - x}]`).join(' + ') : '0'} = ${w[t]}.`, A.arr('ways', w, { hl }));
  }
  A.step(`${w[target]} ordered sequences add up to ${target}.`, A.text('Result', w[target], 'ok'));
}
A.scenario('Example', '[1,2,3], target 4', () => run([1, 2, 3], 4));
A.scenario('Unreachable', '[9], target 3', () => run([9], 3));
'''),

P(num=378, slug="kth-smallest-element-in-a-sorted-matrix", title="Kth Smallest Element in a Sorted Matrix", diff="Medium", topic="Binary Search", cls="KthSmallestInMatrix",
idea="Binary search on the value; count entries ≤ mid with a staircase walk from the bottom-left corner.",
vname="Binary search on value",
spec=r'''
In an `n × n` matrix where every row and every column is sorted ascending, return the `k`-th smallest element (counting duplicates).

**Example**
```
matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8 → 13
matrix = [[-5]], k = 1 → -5
```

**Constraints**
* `1 <= n <= 300`, `-10^9 <= matrix[i][j] <= 10^9`, `1 <= k <= n²`
''',
approach=r'''
**Search values, not positions.** The answer lies in `[matrix[0][0], matrix[n-1][n-1]]`. For a guess `mid`, count entries `<= mid`:
start at the bottom-left; if the entry is `<= mid`, the whole column above it is too (add `row + 1`, move right), otherwise move up. If
the count is less than `k`, the answer is bigger; otherwise it is `mid` or smaller. The range always ends on a value in the matrix. Use
`long` so `lo + hi` cannot overflow.

* Time: **O(n log R)** — `R` is the value range; each count is O(n).
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class KthSmallestInMatrix {

    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        long lo = matrix[0][0], hi = matrix[n - 1][n - 1];
        while (lo < hi) {
            long mid = Math.floorDiv(lo + hi, 2);
            if (countAtMost(matrix, mid) < k) lo = mid + 1;
            else hi = mid;
        }
        return (int) lo;
    }

    private int countAtMost(int[][] m, long x) {
        int n = m.length, row = n - 1, col = 0, count = 0;
        while (row >= 0 && col < n) {
            if (m[row][col] <= x) {
                count += row + 1;
                col++;
            } else row--;
        }
        return count;
    }
}
''',
test=r'''
class KthSmallestInMatrixTest {

    private final KthSmallestInMatrix solution = new KthSmallestInMatrix();

    @Test
    void examples() {
        assertEquals(13, solution.kthSmallest(new int[][]{{1, 5, 9}, {10, 11, 13}, {12, 13, 15}}, 8));
        assertEquals(-5, solution.kthSmallest(new int[][]{{-5}}, 1));
        assertEquals(1, solution.kthSmallest(new int[][]{{1, 2}, {1, 3}}, 2));
        assertEquals(1, solution.kthSmallest(new int[][]{{1, 5, 9}, {10, 11, 13}, {12, 13, 15}}, 1));
        assertEquals(15, solution.kthSmallest(new int[][]{{1, 5, 9}, {10, 11, 13}, {12, 13, 15}}, 9));
    }

    @Test
    void extremes() {
        assertEquals(-1_000_000_000, solution.kthSmallest(new int[][]{{-1_000_000_000, 1_000_000_000}, {1_000_000_000, 1_000_000_000}}, 1));
        assertEquals(1_000_000_000, solution.kthSmallest(new int[][]{{-1_000_000_000, 1_000_000_000}, {1_000_000_000, 1_000_000_000}}, 2));
    }
}
''',
trace=r'''
function run(m, k) {
  const n = m.length; let lo = m[0][0], hi = m[n - 1][n - 1];
  A.step(`The ${k}th smallest value lies between ${lo} and ${hi}. Binary search on the value.`, A.grid('matrix', m), A.vars({ k, lo, hi }));
  while (lo < hi) {
    const mid = Math.floor((lo + hi) / 2), hl = {};
    let r = n - 1, c = 0, cnt = 0;
    while (r >= 0 && c < n) { if (m[r][c] <= mid) { for (let i = 0; i <= r; i++) hl[`${i},${c}`] = 'ok'; cnt += r + 1; c++; } else { hl[`${r},${c}`] = 'bad'; r--; } }
    A.step(`mid = ${mid}: the staircase from the bottom-left counts ${cnt} entries ≤ ${mid}. ${cnt < k ? `Fewer than ${k}, so the answer is bigger.` : `At least ${k}, so the answer is ${mid} or smaller.`}`, A.grid('matrix', m, { hl }), A.vars({ lo, hi, mid, count: cnt }));
    if (cnt < k) lo = mid + 1; else hi = mid;
  }
  A.step(`lo = hi = ${lo}: the ${k}th smallest element.`, A.text('Result', lo, 'ok'));
}
A.scenario('Example', 'k = 8', () => run([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8));
''',
variants=[dict(
name="Min-heap over rows",
idea="Merge the sorted rows with a heap and pop k times.",
approach=r'''
**k-way merge.** Push the first element of each row. Pop the smallest `k` times; after each pop, push the next element of the same row.
The `k`-th pop is the answer.

* Time: **O(k log n)** — `k` pops from a heap of at most `n` entries.
* Space: **O(n)** — the heap.
''',
tc="nlogn", sc="n",
java=r'''
public class KthSmallestInMatrix {

    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(matrix[a[0]][a[1]], matrix[b[0]][b[1]]));
        for (int r = 0; r < n; r++) heap.add(new int[]{r, 0});
        int[] cur = null;
        for (int i = 0; i < k; i++) {
            cur = heap.poll();
            if (cur[1] + 1 < n) heap.add(new int[]{cur[0], cur[1] + 1});
        }
        return matrix[cur[0]][cur[1]];
    }
}
''',
trace=r'''
function run(m, k) {
  const n = m.length, heap = m.map((_, r) => [r, 0]), popped = {};
  const view = () => A.stack('heap (value @ row,col)', heap.slice().sort((a, b) => m[a[0]][a[1]] - m[b[0]][b[1]]).map(([r, c]) => `${m[r][c]} @ ${r},${c}`));
  A.step('Each row is sorted. Start the heap with the first element of every row.', A.grid('matrix', m), view());
  let last;
  for (let i = 1; i <= k; i++) {
    heap.sort((a, b) => m[a[0]][a[1]] - m[b[0]][b[1]]); last = heap.shift(); popped[`${last[0]},${last[1]}`] = i === k ? 'ok' : 'dim';
    if (last[1] + 1 < n) heap.push([last[0], last[1] + 1]);
    A.step(`Pop #${i}: ${m[last[0]][last[1]]}. Push the next element of row ${last[0]}.`, A.grid('matrix', m, { hl: popped }), view());
  }
  A.step(`The ${k}th pop is ${m[last[0]][last[1]]}.`, A.text('Result', m[last[0]][last[1]], 'ok'));
}
A.scenario('Example', 'k = 8', () => run([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8));
''')]),
]
