PROBLEMS = [
P(num=282, slug="expression-add-operators", title="Expression Add Operators", diff="Hard", topic="Backtracking", cls="ExpressionAddOperators",
idea="Backtrack over where numbers end and which operator joins them; remember the last term so * can undo it.",
vname="Backtracking with the last operand",
spec=r'''
Given a digit string `num` and an integer `target`, insert `+`, `-` or `*` between digits (or nothing, to join digits into one number) and
return every expression that evaluates to `target`. Numbers must not have leading zeros (`"05"` is not allowed, `"0"` is).

**Example**
```
num = "123", target = 6   → ["1*2*3","1+2+3"]
num = "232", target = 8   → ["2*3+2","2+3*2"]
num = "105", target = 5   → ["1*0+5","10-5"]
num = "3456237490", target = 9191 → []
```

**Constraints**
* `1 <= num.length <= 10`, `-2^31 <= target <= 2^31 - 1`
''',
approach=r'''
**Track the last term.** Choose the next number `cur = num[pos..i]`, then try each operator. For `+` and `-` the value changes by `±cur` and
the last term becomes `±cur`. For `*`, multiplication binds tighter, so undo the last term and apply it multiplied:
`value - last + last * cur`, with the new last term `last * cur`. Stop extending a number that starts with `0`. Use `long`.

* Time: **O(4ⁿ · n)** — up to 4 choices between digits, and building each expression.
* Space: **O(n)** — recursion depth and the expression buffer.
''',
tc="exp", sc="n",
java=r'''
public class ExpressionAddOperators {

    public List<String> addOperators(String num, int target) {
        List<String> out = new ArrayList<>();
        dfs(num, target, 0, 0, 0, new StringBuilder(), out);
        return out;
    }

    private void dfs(String num, long target, int pos, long value, long last, StringBuilder expr, List<String> out) {
        if (pos == num.length()) {
            if (value == target) out.add(expr.toString());
            return;
        }
        int len = expr.length();
        for (int i = pos; i < num.length(); i++) {
            if (i > pos && num.charAt(pos) == '0') break;
            long cur = Long.parseLong(num.substring(pos, i + 1));
            if (pos == 0) {
                dfs(num, target, i + 1, cur, cur, expr.append(cur), out);
                expr.setLength(len);
                continue;
            }
            dfs(num, target, i + 1, value + cur, cur, expr.append('+').append(cur), out);
            expr.setLength(len);
            dfs(num, target, i + 1, value - cur, -cur, expr.append('-').append(cur), out);
            expr.setLength(len);
            dfs(num, target, i + 1, value - last + last * cur, last * cur, expr.append('*').append(cur), out);
            expr.setLength(len);
        }
    }
}
''',
test=r'''
class ExpressionAddOperatorsTest {

    private final ExpressionAddOperators solution = new ExpressionAddOperators();

    private List<String> sorted(List<String> l) {
        List<String> c = new ArrayList<>(l);
        Collections.sort(c);
        return c;
    }

    @Test
    void examples() {
        assertEquals(List.of("1*2*3", "1+2+3"), sorted(solution.addOperators("123", 6)));
        assertEquals(List.of("2*3+2", "2+3*2"), sorted(solution.addOperators("232", 8)));
        assertEquals(List.of("1*0+5", "10-5"), sorted(solution.addOperators("105", 5)));
        assertEquals(List.of("0*0", "0+0", "0-0"), sorted(solution.addOperators("00", 0)));
        assertEquals(List.of(), solution.addOperators("3456237490", 9191));
    }

    @Test
    void bigNumberWithoutOverflow() {
        assertEquals(List.of("2147483647"), solution.addOperators("2147483647", Integer.MAX_VALUE));
    }
}
''',
trace=r'''
function run(num, target) {
  const out = []; let tried = 0;
  A.step(`Place +, −, × or nothing between the digits of "${num}" to reach ${target}. 'last' is the most recent term, so × can replace it.`, A.chars('digits', num), A.vars({ target }));
  (function dfs(pos, value, last, expr) {
    if (pos === num.length) {
      tried++;
      const ok = value === target; if (ok) out.push(expr);
      if (ok || tried <= 6) A.step(`${expr} = ${value}${ok ? ` hits the target. Record it.` : ', not the target.'}`, A.text('Expression', expr, ok ? 'ok' : 'bad'), A.vars({ value, last }), A.arr('found', out, ok ? { hl: { [out.length - 1]: 'ok' } } : {}));
      return;
    }
    for (let i = pos; i < num.length; i++) {
      if (i > pos && num[pos] === '0') break;
      const cur = +num.slice(pos, i + 1);
      if (pos === 0) { dfs(i + 1, cur, cur, String(cur)); continue; }
      dfs(i + 1, value + cur, cur, `${expr}+${cur}`);
      dfs(i + 1, value - cur, -cur, `${expr}-${cur}`);
      dfs(i + 1, value - last + last * cur, last * cur, `${expr}*${cur}`);
    }
  })(0, 0, 0, '');
  A.step(`Checked ${tried} complete expressions; ${out.length} reach ${target}.`, A.arr('found', out, { hl: Object.fromEntries(out.map((_, i) => [i, 'ok'])) }));
}
A.scenario('Two answers', '"123", target 6', () => run('123', 6));
A.scenario('Zero digit', '"105", target 5', () => run('105', 5));
'''),

P(num=284, slug="peeking-iterator", title="Peeking Iterator", diff="Medium", topic="Design", cls="PeekingIterator",
idea="Read one element ahead and keep it in a field; peek returns it, next hands it over and reads the next one.",
vname="Cache the next element",
spec=r'''
Wrap an `Iterator<Integer>` in a `PeekingIterator` that also supports `peek()`, which returns the next element **without** advancing.

* `PeekingIterator(Iterator<Integer> it)`
* `Integer next()`, `boolean hasNext()`, `Integer peek()`

**Example**
```
iterator over [1,2,3]
next() → 1, peek() → 2, next() → 2, next() → 3, hasNext() → false
```

**Constraints**
* `1 <= length <= 1000`; `next` and `peek` are only called when an element remains
''',
approach=r'''
**One element of look-ahead.** In the constructor, pull the first element (if any) into `ahead`. `peek` returns `ahead`. `next` returns
`ahead` and refills it from the inner iterator. A separate flag, not `null`, records whether `ahead` is valid.

* Time: **O(1)** — per call.
* Space: **O(1)** — one cached element.
''',
tc="1", sc="1",
java=r'''
public class PeekingIterator implements Iterator<Integer> {

    private final Iterator<Integer> inner;
    private Integer ahead;
    private boolean hasAhead;

    public PeekingIterator(Iterator<Integer> iterator) {
        inner = iterator;
        advance();
    }

    private void advance() {
        hasAhead = inner.hasNext();
        ahead = hasAhead ? inner.next() : null;
    }

    public Integer peek() {
        return ahead;
    }

    @Override
    public Integer next() {
        if (!hasAhead) throw new NoSuchElementException();
        Integer v = ahead;
        advance();
        return v;
    }

    @Override
    public boolean hasNext() {
        return hasAhead;
    }
}
''',
test=r'''
class PeekingIteratorTest {

    @Test
    void example() {
        PeekingIterator it = new PeekingIterator(List.of(1, 2, 3).iterator());
        assertEquals(1, it.next());
        assertEquals(2, it.peek());
        assertEquals(2, it.peek());
        assertEquals(2, it.next());
        assertEquals(3, it.next());
        assertFalse(it.hasNext());
        assertThrows(NoSuchElementException.class, it::next);
    }

    @Test
    void peekFirstAndEmpty() {
        PeekingIterator it = new PeekingIterator(List.of(7).iterator());
        assertTrue(it.hasNext());
        assertEquals(7, it.peek());
        assertEquals(7, it.next());
        assertFalse(it.hasNext());
        assertFalse(new PeekingIterator(new ArrayList<Integer>().iterator()).hasNext());
    }
}
''',
trace=r'''
function run(vals, ops) {
  let pos = 0, ahead = vals[0], has = vals.length > 0; pos = has ? 1 : 0;
  const view = () => A.arr('inner iterator', vals, { hl: Object.fromEntries(vals.map((_, i) => [i, i < pos - (has ? 1 : 0) ? 'dim' : i === pos - 1 && has ? 'cur' : ''])) });
  A.step(`The constructor reads one element ahead: ahead = ${ahead}.`, view(), A.vars({ ahead, hasAhead: has }));
  ops.forEach(op => {
    if (op === 'peek') A.step(`peek() returns the cached ${ahead} and does not move.`, view(), A.vars({ ahead, hasAhead: has }), A.text('Returned', ahead, 'ok'));
    else if (op === 'next') { const v = ahead; has = pos < vals.length; ahead = has ? vals[pos] : null; pos++; A.step(`next() hands over ${v} and reads the next one: ahead = ${ahead === null ? 'none' : ahead}.`, view(), A.vars({ ahead: ahead === null ? '—' : ahead, hasAhead: has }), A.text('Returned', v, 'ok')); }
    else A.step(`hasNext() is ${has}: ${has ? 'an element is cached' : 'nothing is cached'}.`, view(), A.vars({ hasAhead: has }), A.text('Returned', String(has), has ? 'ok' : 'bad'));
  });
}
A.scenario('Example', '[1,2,3]', () => run([1, 2, 3], ['next', 'peek', 'next', 'next', 'hasNext']));
'''),

P(num=292, slug="nim-game", title="Nim Game", diff="Easy", topic="Math", cls="NimGame",
idea="Multiples of 4 are losing positions: whatever you take, your opponent can make the total 4.",
vname="Multiples of four lose",
spec=r'''
There is a heap of `n` stones. Players alternate removing 1, 2 or 3 stones; whoever takes the last stone wins. You move first and both
players play optimally. Return `true` if you can win.

**Example**
```
n = 4 → false
n = 1 → true
n = 5 → true
```

**Constraints**
* `1 <= n <= 2^31 - 1`
''',
approach=r'''
**Pattern.** With 1–3 stones you take them all. With 4, every move leaves 1–3 for your opponent. In general, if `n % 4 != 0` take
`n % 4` stones to leave a multiple of 4; from a multiple of 4, whatever `k` you take, the opponent takes `4 - k`.

* Time: **O(1)**.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class NimGame {

    public boolean canWinNim(int n) {
        return n % 4 != 0;
    }
}
''',
test=r'''
class NimGameTest {

    private final NimGame solution = new NimGame();

    @ParameterizedTest
    @CsvSource({"1,true", "2,true", "3,true", "4,false", "5,true", "8,false", "2147483647,true", "2147483644,false"})
    void wins(int n, boolean expected) {
        assertEquals(expected, solution.canWinNim(n));
    }

    @Test
    void matchesGameTree() {
        boolean[] win = new boolean[60];
        for (int n = 1; n < 60; n++) for (int k = 1; k <= 3 && k <= n; k++) if (!win[n - k]) win[n] = true;
        for (int n = 1; n < 60; n++) assertEquals(win[n], solution.canWinNim(n));
    }
}
''',
trace=r'''
function run(n) {
  const N = Math.max(n, 12), win = [false], hl = { 0: 'bad' };
  A.step('0 stones on your turn means the opponent took the last one: a loss. Build up from there.', A.arr('can win?', ['L'], { hl }));
  for (let i = 1; i <= N; i++) {
    win[i] = [1, 2, 3].some(k => k <= i && !win[i - k]); hl[i] = win[i] ? 'ok' : 'bad';
    if (i <= 5 || i % 4 === 0) A.step(win[i] ? `${i} stones: take ${[1, 2, 3].find(k => k <= i && !win[i - k])} to leave ${i - [1, 2, 3].find(k => k <= i && !win[i - k])}, a losing spot for them. Win.` : `${i} stones: every move leaves ${i - 3}–${i - 1}, all winning for them. Loss.`, A.arr('can win?', win.map(w => (w ? 'W' : 'L')), { hl }));
  }
  A.step(`The losses are exactly the multiples of 4. ${n} % 4 = ${n % 4}, so you ${n % 4 ? 'win' : 'lose'}.`, A.text('Result', String(n % 4 !== 0), n % 4 ? 'ok' : 'bad'));
}
A.scenario('Losing start', 'n = 8', () => run(8));
A.scenario('Winning start', 'n = 7', () => run(7));
'''),

P(num=299, slug="bulls-and-cows", title="Bulls and Cows", diff="Medium", topic="Hash Map", cls="BullsAndCows",
idea="Count exact matches; for the rest, a signed digit tally tells you when a digit has a partner on the other side.",
vname="One pass with a signed tally",
spec=r'''
Given a `secret` and a `guess` of the same length (digits only), return the hint `"xAyB"`: `x` **bulls** (right digit, right position)
and `y` **cows** (digits in the guess that are in the secret but in the wrong position, each secret digit used at most once).

**Example**
```
secret = "1807", guess = "7810" → "1A3B"
secret = "1123", guess = "0111" → "1A1B"
```

**Constraints**
* `1 <= length <= 1000`
''',
approach=r'''
**Signed counts.** For each position that is not a bull, add 1 for the secret digit and subtract 1 for the guess digit. If the secret
digit's tally was negative, an earlier guess digit was waiting for it: a cow. If the guess digit's tally was positive, an earlier secret
digit was waiting: a cow.

* Time: **O(n)** — one pass.
* Space: **O(1)** — ten counters.
''',
tc="n", sc="1",
java=r'''
public class BullsAndCows {

    public String getHint(String secret, String guess) {
        int bulls = 0, cows = 0;
        int[] tally = new int[10];
        for (int i = 0; i < secret.length(); i++) {
            int s = secret.charAt(i) - '0', g = guess.charAt(i) - '0';
            if (s == g) {
                bulls++;
                continue;
            }
            if (tally[s]++ < 0) cows++;
            if (tally[g]-- > 0) cows++;
        }
        return bulls + "A" + cows + "B";
    }
}
''',
test=r'''
class BullsAndCowsTest {

    private final BullsAndCows solution = new BullsAndCows();

    @ParameterizedTest
    @CsvSource({"1807,7810,1A3B", "1123,0111,1A1B", "1,0,0A0B", "1,1,1A0B", "1122,2211,0A4B", "1122,1222,3A0B"})
    void hints(String secret, String guess, String expected) {
        assertEquals(expected, solution.getHint(secret, guess));
    }
}
''',
trace=r'''
function run(secret, guess) {
  const t = new Array(10).fill(0); let bulls = 0, cows = 0;
  A.step('Walk both strings together. Exact matches are bulls; other digits go into a signed tally (+ for secret, − for guess).', A.chars('secret', secret), A.chars('guess', guess));
  for (let i = 0; i < secret.length; i++) {
    const s = +secret[i], g = +guess[i];
    if (s === g) { bulls++; A.step(`Position ${i}: both ${s}. Bull.`, A.chars('secret', secret, { hl: { [i]: 'ok' } }), A.chars('guess', guess, { hl: { [i]: 'ok' } }), A.vars({ bulls, cows })); continue; }
    const notes = [];
    if (t[s]++ < 0) { cows++; notes.push(`a guess ${s} was waiting → cow`); }
    if (t[g]-- > 0) { cows++; notes.push(`a secret ${g} was waiting → cow`); }
    A.step(`Position ${i}: secret ${s}, guess ${g}. ${notes.length ? notes.join('; ') : 'No partner yet; remember both'}.`, A.chars('secret', secret, { hl: { [i]: 'cur' } }), A.chars('guess', guess, { hl: { [i]: 'cur' } }), A.arr('tally by digit', t), A.vars({ bulls, cows }));
  }
  A.step(`Hint: ${bulls}A${cows}B.`, A.text('Result', `${bulls}A${cows}B`, 'ok'));
}
A.scenario('Classic', '1807 vs 7810', () => run('1807', '7810'));
A.scenario('Repeated digits', '1123 vs 0111', () => run('1123', '0111'));
'''),

P(num=301, slug="remove-invalid-parentheses", title="Remove Invalid Parentheses", diff="Hard", topic="Backtracking", cls="RemoveInvalidParentheses",
idea="First count exactly how many '(' and ')' must go, then only explore removals of that many.",
vname="DFS with counted removals",
spec=r'''
Remove the **minimum** number of parentheses to make the string valid. Return every distinct valid result, in any order. Letters stay.

**Example**
```
"()())()"  → ["(())()","()()()"]
"(a)())()" → ["(a())()","(a)()()"]
")("       → [""]
```

**Constraints**
* `1 <= s.length <= 25`; `s` has letters and parentheses, at most 20 parentheses
''',
approach=r'''
**Count, then prune.** One scan finds `open` (unmatched `(`) and `close` (unmatched `)`): exactly the minimum removals. Recurse, removing
one bracket at a time from `start` onward, only while the matching budget lasts. In a run of equal characters, only remove the first:
removing any of them yields the same string, so this avoids duplicate answers. When both budgets are 0, keep the string if it is valid.

* Time: **O(2ⁿ · n)** — subsets of removable brackets, each checked in linear time.
* Space: **O(n²)** — recursion depth times the copied strings.
''',
tc="exp", sc="n2",
java=r'''
public class RemoveInvalidParentheses {

    public List<String> removeInvalidParentheses(String s) {
        int open = 0, close = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') open++;
            else if (c == ')') {
                if (open > 0) open--;
                else close++;
            }
        }
        List<String> out = new ArrayList<>();
        dfs(s, 0, open, close, out);
        return out;
    }

    private void dfs(String s, int start, int open, int close, List<String> out) {
        if (open == 0 && close == 0) {
            if (valid(s)) out.add(s);
            return;
        }
        for (int i = start; i < s.length(); i++) {
            if (open + close > s.length() - i) return;
            char c = s.charAt(i);
            if (i > start && c == s.charAt(i - 1)) continue;
            String t = s.substring(0, i) + s.substring(i + 1);
            if (c == '(' && open > 0) dfs(t, i, open - 1, close, out);
            if (c == ')' && close > 0) dfs(t, i, open, close - 1, out);
        }
    }

    private boolean valid(String s) {
        int depth = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') depth++;
            else if (c == ')' && --depth < 0) return false;
        }
        return depth == 0;
    }
}
''',
test=r'''
class RemoveInvalidParenthesesTest {

    private final RemoveInvalidParentheses solution = new RemoveInvalidParentheses();

    private List<String> sorted(List<String> l) {
        List<String> c = new ArrayList<>(l);
        Collections.sort(c);
        return c;
    }

    @Test
    void examples() {
        assertEquals(List.of("(())()", "()()()"), sorted(solution.removeInvalidParentheses("()())()")));
        assertEquals(List.of("(a())()", "(a)()()"), sorted(solution.removeInvalidParentheses("(a)())()")));
        assertEquals(List.of(""), solution.removeInvalidParentheses(")("));
        assertEquals(List.of("x"), solution.removeInvalidParentheses("x("));
        assertEquals(List.of("()"), solution.removeInvalidParentheses("()"));
        assertEquals(List.of("(())"), sorted(solution.removeInvalidParentheses("((())")));
    }
}
''',
trace=r'''
function valid(s) { let d = 0; for (const c of s) { if (c === '(') d++; else if (c === ')' && --d < 0) return false; } return d === 0; }
function run(s) {
  let open = 0, close = 0; for (const c of s) { if (c === '(') open++; else if (c === ')') { if (open) open--; else close++; } }
  A.step(`One scan: ${open} unmatched '(' and ${close} unmatched ')'. That is exactly how many must go.`, A.chars('s', s), A.vars({ removeOpen: open, removeClose: close }));
  const out = [];
  (function dfs(t, start, o, c) {
    if (!o && !c) { const ok = valid(t); if (ok) out.push(t); A.step(`Budget used up: "${t}" is ${ok ? 'valid. Keep it.' : 'still invalid. Drop it.'}`, A.chars('candidate', t || ' '), A.arr('answers', out, ok ? { hl: { [out.length - 1]: 'ok' } } : {})); return; }
    for (let i = start; i < t.length; i++) {
      if (o + c > t.length - i) return;
      const ch = t[i]; if (i > start && ch === t[i - 1]) continue;
      if ((ch === '(' && o) || (ch === ')' && c)) {
        A.step(`Remove '${ch}' at index ${i} from "${t}".`, A.chars('candidate', t, { hl: { [i]: 'bad' } }), A.vars({ removeOpen: o, removeClose: c }));
        dfs(t.slice(0, i) + t.slice(i + 1), i, o - (ch === '('), c - (ch === ')'));
      }
    }
  })(s, 0, open, close);
  A.step(`${out.length} distinct answer${out.length === 1 ? '' : 's'}, each with the minimum removals.`, A.arr('answers', out, { hl: Object.fromEntries(out.map((_, i) => [i, 'ok'])) }));
}
A.scenario('Classic', '"()())()"', () => run('()())()'));
A.scenario('Both kinds', '")("', () => run(')('));
''',
variants=[dict(
name="BFS by number of removals",
idea="Level k of a BFS holds every string with k characters removed; the first level with a valid string is the answer.",
approach=r'''
**Breadth-first.** Start from `s`. Check every string on the current level; if any are valid, return those. Otherwise build the next level
by deleting one parenthesis from each string, using a `MyHashSet` so each string is generated once.

* Time: **O(2ⁿ · n)** — in the worst case many subsets are explored, each checked in linear time.
* Space: **O(2ⁿ · n)** — the levels and the visited set.
''',
tc="exp", sc="exp",
java=r'''
public class RemoveInvalidParentheses {

    public List<String> removeInvalidParentheses(String s) {
        MyHashSet<String> seen = new MyHashSet<>();
        List<String> level = new ArrayList<>(List.of(s));
        seen.add(s);
        while (true) {
            List<String> out = new ArrayList<>();
            for (String t : level) if (valid(t)) out.add(t);
            if (!out.isEmpty()) return out;
            List<String> next = new ArrayList<>();
            for (String t : level)
                for (int i = 0; i < t.length(); i++) {
                    char c = t.charAt(i);
                    if (c != '(' && c != ')') continue;
                    String u = t.substring(0, i) + t.substring(i + 1);
                    if (seen.add(u)) next.add(u);
                }
            level = next;
        }
    }

    private boolean valid(String s) {
        int depth = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') depth++;
            else if (c == ')' && --depth < 0) return false;
        }
        return depth == 0;
    }
}
''',
trace=r'''
function valid(s) { let d = 0; for (const c of s) { if (c === '(') d++; else if (c === ')' && --d < 0) return false; } return d === 0; }
function run(s) {
  const seen = new Set([s]); let level = [s], k = 0;
  A.step('Level 0 is the string itself.', A.arr('level 0', level));
  while (true) {
    const out = level.filter(valid);
    if (out.length) { A.step(`Level ${k} has ${out.length} valid string${out.length > 1 ? 's' : ''}. Stop: ${k} removal${k === 1 ? '' : 's'} is the minimum.`, A.arr(`level ${k}`, level, { hl: Object.fromEntries(level.map((t, i) => [i, valid(t) ? 'ok' : 'dim'])) })); A.step('These are the answers.', A.arr('answers', out)); return; }
    A.step(`No valid string on level ${k}. Delete one more parenthesis from each.`, A.arr(`level ${k}`, level, { hl: Object.fromEntries(level.map((_, i) => [i, 'bad'])) }));
    const next = [];
    level.forEach(t => { for (let i = 0; i < t.length; i++) { if (t[i] !== '(' && t[i] !== ')') continue; const u = t.slice(0, i) + t.slice(i + 1); if (!seen.has(u)) { seen.add(u); next.push(u); } } });
    level = next; k++;
  }
}
A.scenario('Classic', '"()())()"', () => run('()())()'));
''')]),

P(num=303, slug="range-sum-query-immutable", title="Range Sum Query - Immutable", diff="Easy", topic="Prefix Sum", cls="NumArray",
idea="Precompute prefix sums once; any range sum is the difference of two prefixes.",
vname="Prefix sums",
spec=r'''
Implement `NumArray`:

* `NumArray(int[] nums)`
* `int sumRange(int left, int right)` — the sum of `nums[left..right]` inclusive.

**Example**
```
nums = [-2,0,3,-5,2,-1]
sumRange(0,2) → 1, sumRange(2,5) → -1, sumRange(0,5) → -3
```

**Constraints**
* `1 <= nums.length <= 10^4`, up to `10^4` queries
''',
approach=r'''
**Prefix sums.** Store `prefix[i] = nums[0] + … + nums[i-1]` with `prefix[0] = 0`. Then
`sumRange(l, r) = prefix[r + 1] - prefix[l]`.

* Time: **O(1)** — per query, after O(n) setup.
* Space: **O(n)** — the prefix array.
''',
tc="1", sc="n",
java=r'''
public class NumArray {

    private final int[] prefix;

    public NumArray(int[] nums) {
        prefix = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) prefix[i + 1] = prefix[i] + nums[i];
    }

    public int sumRange(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }
}
''',
test=r'''
class NumArrayTest {

    @Test
    void example() {
        NumArray a = new NumArray(new int[]{-2, 0, 3, -5, 2, -1});
        assertEquals(1, a.sumRange(0, 2));
        assertEquals(-1, a.sumRange(2, 5));
        assertEquals(-3, a.sumRange(0, 5));
        assertEquals(3, a.sumRange(2, 2));
    }
}
''',
trace=r'''
function run(nums, qs) {
  const p = [0]; nums.forEach(v => p.push(p[p.length - 1] + v));
  A.step('Build prefix sums once: prefix[i] is the sum of the first i numbers.', A.arr('nums', nums), A.arr('prefix', p));
  qs.forEach(([l, r]) => A.step(`sumRange(${l}, ${r}) = prefix[${r + 1}] − prefix[${l}] = ${p[r + 1]} − ${p[l]} = ${p[r + 1] - p[l]}.`, A.arr('nums', nums, { range: [l, r] }), A.arr('prefix', p, { hl: { [r + 1]: 'ok', [l]: 'bad' } })));
  A.step('Each query costs two lookups, however long the range.', A.vars({ queries: qs.length }));
}
A.scenario('Example', '[-2,0,3,-5,2,-1]', () => run([-2, 0, 3, -5, 2, -1], [[0, 2], [2, 5], [0, 5]]));
'''),

P(num=304, slug="range-sum-query-2d-immutable", title="Range Sum Query 2D - Immutable", diff="Medium", topic="Prefix Sum", cls="NumMatrix",
idea="2-D prefix sums: a rectangle is one big prefix minus two strips plus the corner counted twice.",
vname="2-D prefix sums",
spec=r'''
Implement `NumMatrix`:

* `NumMatrix(int[][] matrix)`
* `int sumRegion(int row1, int col1, int row2, int col2)` — the sum of the rectangle with corners `(row1, col1)` and `(row2, col2)`,
  inclusive, in O(1).

**Example**
```
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
sumRegion(2,1,4,3) → 8, sumRegion(1,1,2,2) → 11, sumRegion(1,2,2,4) → 12
```

**Constraints**
* `1 <= m, n <= 200`, up to `10^4` queries
''',
approach=r'''
**Inclusion–exclusion.** `P[r][c]` is the sum of the top-left `r × c` block, built as
`P[r][c] = M[r-1][c-1] + P[r-1][c] + P[r][c-1] - P[r-1][c-1]`. A query is
`P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]`.

* Time: **O(1)** — per query, after O(mn) setup.
* Space: **O(mn)** — the prefix table.
''',
tc="1", sc="n2",
java=r'''
public class NumMatrix {

    private final int[][] prefix;

    public NumMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        prefix = new int[m + 1][n + 1];
        for (int r = 1; r <= m; r++)
            for (int c = 1; c <= n; c++)
                prefix[r][c] = matrix[r - 1][c - 1] + prefix[r - 1][c] + prefix[r][c - 1] - prefix[r - 1][c - 1];
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        return prefix[row2 + 1][col2 + 1] - prefix[row1][col2 + 1] - prefix[row2 + 1][col1] + prefix[row1][col1];
    }
}
''',
test=r'''
class NumMatrixTest {

    @Test
    void example() {
        NumMatrix m = new NumMatrix(new int[][]{{3, 0, 1, 4, 2}, {5, 6, 3, 2, 1}, {1, 2, 0, 1, 5}, {4, 1, 0, 1, 7}, {1, 0, 3, 0, 5}});
        assertEquals(8, m.sumRegion(2, 1, 4, 3));
        assertEquals(11, m.sumRegion(1, 1, 2, 2));
        assertEquals(12, m.sumRegion(1, 2, 2, 4));
        assertEquals(3, m.sumRegion(0, 0, 0, 0));
        assertEquals(58, m.sumRegion(0, 0, 4, 4));
    }
}
''',
trace=r'''
function run(M, q) {
  const m = M.length, n = M[0].length, P = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
  for (let r = 1; r <= m; r++) for (let c = 1; c <= n; c++) P[r][c] = M[r - 1][c - 1] + P[r - 1][c] + P[r][c - 1] - P[r - 1][c - 1];
  A.step('P[r][c] holds the sum of the top-left r × c block (with an extra zero row and column).', A.grid('matrix', M), A.grid('prefix P', P));
  const [r1, c1, r2, c2] = q, hl = {};
  for (let r = r1; r <= r2; r++) for (let c = c1; c <= c2; c++) hl[`${r},${c}`] = 'cur';
  A.step(`Query rows ${r1}–${r2}, columns ${c1}–${c2}.`, A.grid('matrix', M, { hl }));
  A.step(`Start from P[${r2 + 1}][${c2 + 1}] = ${P[r2 + 1][c2 + 1]}; subtract the strip above, P[${r1}][${c2 + 1}] = ${P[r1][c2 + 1]}, and the strip to the left, P[${r2 + 1}][${c1}] = ${P[r2 + 1][c1]}.`, A.grid('prefix P', P, { hl: { [`${r2 + 1},${c2 + 1}`]: 'ok', [`${r1},${c2 + 1}`]: 'bad', [`${r2 + 1},${c1}`]: 'bad', [`${r1},${c1}`]: 'alt' } }));
  const s = P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1];
  A.step(`The top-left corner P[${r1}][${c1}] = ${P[r1][c1]} was subtracted twice; add it back. Sum = ${s}.`, A.text('Result', s, 'ok'));
}
A.scenario('Example', 'sumRegion(2,1,4,3)', () => run([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]], [2, 1, 4, 3]));
'''),

P(num=307, slug="range-sum-query-mutable", title="Range Sum Query - Mutable", diff="Medium", topic="Fenwick Tree", cls="NumArray",
idea="A Fenwick tree stores partial sums over power-of-two blocks, so both update and prefix sum take log n steps.",
vname="Fenwick (binary indexed) tree",
spec=r'''
Implement `NumArray` supporting both updates and range sums:

* `NumArray(int[] nums)`
* `void update(int index, int val)` — set `nums[index] = val`.
* `int sumRange(int left, int right)` — the sum of `nums[left..right]`.

**Example**
```
nums = [1,3,5]
sumRange(0,2) → 9, update(1,2), sumRange(0,2) → 8
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`, up to `3 * 10^4` calls
''',
approach=r'''
**Fenwick tree.** Slot `i` (1-based) stores the sum of the `i & -i` elements ending at `i`. A prefix sum walks `i -= i & -i`, collecting
at most `log n` slots; an update by `delta` walks `i += i & -i`, touching every slot that covers that index. A range sum is the difference
of two prefix sums. Keep a copy of the values to turn `update` into a delta.

* Time: **O(log n)** — per update or query.
* Space: **O(n)** — the tree.
''',
tc="log", sc="n",
java=r'''
public class NumArray {

    private final int[] values, tree;

    public NumArray(int[] nums) {
        values = nums.clone();
        tree = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) add(i + 1, nums[i]);
    }

    private void add(int i, int delta) {
        for (; i < tree.length; i += i & -i) tree[i] += delta;
    }

    private int prefix(int i) {
        int s = 0;
        for (; i > 0; i -= i & -i) s += tree[i];
        return s;
    }

    public void update(int index, int val) {
        add(index + 1, val - values[index]);
        values[index] = val;
    }

    public int sumRange(int left, int right) {
        return prefix(right + 1) - prefix(left);
    }
}
''',
test=r'''
class NumArrayTest {

    @Test
    void example() {
        NumArray a = new NumArray(new int[]{1, 3, 5});
        assertEquals(9, a.sumRange(0, 2));
        a.update(1, 2);
        assertEquals(8, a.sumRange(0, 2));
        assertEquals(2, a.sumRange(1, 1));
    }

    @Test
    void matchesBruteForce() {
        Random rnd = new Random(7);
        int[] ref = new int[50];
        for (int i = 0; i < ref.length; i++) ref[i] = rnd.nextInt(201) - 100;
        NumArray a = new NumArray(ref);
        for (int step = 0; step < 2000; step++) {
            if (rnd.nextBoolean()) {
                int i = rnd.nextInt(ref.length), v = rnd.nextInt(201) - 100;
                ref[i] = v;
                a.update(i, v);
            } else {
                int l = rnd.nextInt(ref.length), r = l + rnd.nextInt(ref.length - l), s = 0;
                for (int i = l; i <= r; i++) s += ref[i];
                assertEquals(s, a.sumRange(l, r));
            }
        }
    }
}
''',
trace=r'''
function run(nums) {
  const n = nums.length, t = new Array(n + 1).fill(0), lab = Array.from({ length: n + 1 }, (_, i) => (i ? `${i - (i & -i) + 1}..${i}` : '—'));
  const add = (i, d) => { const touched = []; for (; i <= n; i += i & -i) { t[i] += d; touched.push(i); } return touched; };
  nums.forEach((v, i) => add(i + 1, v));
  A.step('Slot i holds the sum of the (i & −i) elements ending at i. The labels show which positions each slot covers (1-based).', A.arr('nums (1-based)', [0, ...nums]), A.arr('tree', t), A.arr('covers', lab));
  const prefix = i => { let s = 0; const used = []; for (; i > 0; i -= i & -i) { s += t[i]; used.push(i); } return [s, used]; };
  let [s, used] = prefix(n);
  A.step(`Sum of all ${n}: add slots ${used.join(', ')} (strip the lowest bit each time) = ${s}.`, A.arr('tree', t, { hl: Object.fromEntries(used.map(i => [i, 'ok'])) }), A.vars({ sum: s }));
  const idx = 2, val = nums[idx] + 4, touched = add(idx + 1, val - nums[idx]); nums[idx] = val;
  A.step(`update(${idx}, ${val}): add +4 to slots ${touched.join(', ')} (add the lowest bit each time). Only these cover position ${idx + 1}.`, A.arr('nums (1-based)', [0, ...nums], { hl: { [idx + 1]: 'cur' } }), A.arr('tree', t, { hl: Object.fromEntries(touched.map(i => [i, 'cur'])) }));
  const [a, ua] = prefix(5), [b, ub] = prefix(1);
  A.step(`sumRange(1, 4) = prefix(5) − prefix(1) = (${ua.map(i => t[i]).join(' + ')}) − ${ub.map(i => t[i]).join(' + ')} = ${a - b}.`, A.arr('tree', t, { hl: Object.fromEntries([...ua.map(i => [i, 'ok']), ...ub.map(i => [i, 'bad'])]) }), A.text('Result', a - b, 'ok'));
}
A.scenario('Eight values', '[2,1,5,3,4,2,6,1]', () => run([2, 1, 5, 3, 4, 2, 6, 1]));
''',
variants=[dict(
name="Plain array, sum on demand",
idea="Updates are a single assignment; a range sum loops over the range.",
approach=r'''
**Direct.** Store the array. `update` assigns one cell; `sumRange` adds up `right - left + 1` cells.

* Time: **O(n)** — per query (updates are O(1)).
* Space: **O(n)** — the array copy.
''',
tc="n", sc="n",
java=r'''
public class NumArray {

    private final int[] values;

    public NumArray(int[] nums) {
        values = nums.clone();
    }

    public void update(int index, int val) {
        values[index] = val;
    }

    public int sumRange(int left, int right) {
        int s = 0;
        for (int i = left; i <= right; i++) s += values[i];
        return s;
    }
}
''',
trace=r'''
function run(nums) {
  A.step('Keep the numbers as they are.', A.arr('nums', nums));
  let s = 0; for (let i = 0; i < nums.length; i++) s += nums[i];
  A.step(`sumRange(0, ${nums.length - 1}) loops over every cell: ${s}.`, A.arr('nums', nums, { range: [0, nums.length - 1] }), A.vars({ sum: s }));
  nums[1] = 2;
  A.step('update(1, 2) is a single write.', A.arr('nums', nums, { hl: { 1: 'cur' } }));
  s = nums.reduce((a, b) => a + b, 0);
  A.step(`sumRange again loops over every cell: ${s}. Many large queries make this slow.`, A.arr('nums', nums, { range: [0, nums.length - 1] }), A.text('Result', s, 'ok'));
}
A.scenario('Example', '[1,3,5]', () => run([1, 3, 5]));
''')]),

P(num=313, slug="super-ugly-number", title="Super Ugly Number", diff="Medium", topic="Dynamic Programming", cls="SuperUglyNumber",
idea="The three-pointer merge from Ugly Number II, with one pointer per prime.",
vname="One pointer per prime",
spec=r'''
A **super ugly number** is a positive integer whose prime factors all appear in the array `primes`. Return the `n`-th super ugly number
(1 is the first). The answer fits in a 32-bit signed integer.

**Example**
```
n = 12, primes = [2,7,13,19] → 32
   (1,2,4,7,8,13,14,16,19,26,28,32)
n = 1,  primes = [2,3,5]     → 1
```

**Constraints**
* `1 <= n <= 10^5`, `1 <= primes.length <= 100`, primes are distinct and sorted
''',
approach=r'''
**k-way merge.** Every super ugly number is a smaller one times some prime. Keep a pointer `idx[j]` per prime: the smallest number not
yet multiplied by `primes[j]`. The next number is the smallest candidate `ugly[idx[j]] * primes[j]`; advance every pointer that produced
it to skip duplicates. Candidates can exceed 32 bits, so use `long`.

* Time: **O(n · k)** — `k` candidates per number.
* Space: **O(n + k)** — the sequence and pointers.
''',
tc="n2", sc="n",
java=r'''
public class SuperUglyNumber {

    public int nthSuperUglyNumber(int n, int[] primes) {
        long[] ugly = new long[n];
        ugly[0] = 1;
        int[] idx = new int[primes.length];
        for (int i = 1; i < n; i++) {
            long next = Long.MAX_VALUE;
            for (int j = 0; j < primes.length; j++) next = Math.min(next, ugly[idx[j]] * primes[j]);
            ugly[i] = next;
            for (int j = 0; j < primes.length; j++) if (ugly[idx[j]] * primes[j] == next) idx[j]++;
        }
        return (int) ugly[n - 1];
    }
}
''',
test=r'''
class SuperUglyNumberTest {

    private final SuperUglyNumber solution = new SuperUglyNumber();

    @Test
    void examples() {
        assertEquals(32, solution.nthSuperUglyNumber(12, new int[]{2, 7, 13, 19}));
        assertEquals(1, solution.nthSuperUglyNumber(1, new int[]{2, 3, 5}));
        assertEquals(12, solution.nthSuperUglyNumber(10, new int[]{2, 3, 5}));
        assertEquals(1024, solution.nthSuperUglyNumber(11, new int[]{2}));
    }
}
''',
trace=r'''
function run(n, primes) {
  const u = [1], idx = primes.map(() => 0);
  A.step(`Primes [${primes}]. Each prime has a pointer to the smallest number it has not multiplied yet.`, A.arr('ugly', u), A.arr('pointer per prime', idx));
  for (let i = 1; i < n; i++) {
    const cand = primes.map((p, j) => u[idx[j]] * p), next = Math.min(...cand);
    u.push(next);
    const moved = primes.filter((p, j) => cand[j] === next);
    primes.forEach((p, j) => { if (cand[j] === next) idx[j]++; });
    A.step(`Candidates ${cand.join(', ')}. Take ${next}; advance the pointer of ${moved.join(' and ')}.`, A.arr('ugly', u, { hl: { [i]: 'ok' } }), A.arr('candidates', cand, { hl: Object.fromEntries(cand.map((c, j) => [j, c === next ? 'ok' : ''])) }));
  }
  A.step(`The ${n}th super ugly number is ${u[n - 1]}.`, A.text('Result', u[n - 1], 'ok'));
}
A.scenario('Example', 'n = 12, primes = [2,7,13,19]', () => run(12, [2, 7, 13, 19]));
'''),

P(num=315, slug="count-of-smaller-numbers-after-self", title="Count of Smaller Numbers After Self", diff="Hard", topic="Divide and Conquer", cls="CountSmaller",
idea="During merge sort, every right-half element that is placed before a left-half element is smaller and lies after it.",
vname="Merge sort counting inversions",
spec=r'''
For each `nums[i]`, count how many elements to its **right** are strictly smaller. Return the counts.

**Example**
```
[5,2,6,1] → [2,1,1,0]
[-1]      → [0]
[-1,-1]   → [0,0]
```

**Constraints**
* `1 <= nums.length <= 10^5`, `-10^4 <= nums[i] <= 10^4`
''',
approach=r'''
**Merge sort on indices.** Sort an index array by value. When merging two sorted halves, an element taken from the left half has
exactly `j - (mid + 1)` right-half elements already placed before it, and those are smaller (ties go left first, so only strictly
smaller ones count) and originally to its right. Add that to its count.

* Time: **O(n log n)** — merge sort.
* Space: **O(n)** — the index and buffer arrays.
''',
tc="nlogn", sc="n",
java=r'''
public class CountSmaller {

    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        int[] idx = new int[n], count = new int[n], buf = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        sort(nums, idx, buf, count, 0, n - 1);
        List<Integer> out = new ArrayList<>(n);
        for (int c : count) out.add(c);
        return out;
    }

    private void sort(int[] nums, int[] idx, int[] buf, int[] count, int lo, int hi) {
        if (lo >= hi) return;
        int mid = (lo + hi) >>> 1;
        sort(nums, idx, buf, count, lo, mid);
        sort(nums, idx, buf, count, mid + 1, hi);
        int i = lo, j = mid + 1, k = lo;
        while (i <= mid || j <= hi) {
            if (j > hi || (i <= mid && nums[idx[i]] <= nums[idx[j]])) {
                count[idx[i]] += j - (mid + 1);
                buf[k++] = idx[i++];
            } else {
                buf[k++] = idx[j++];
            }
        }
        System.arraycopy(buf, lo, idx, lo, hi - lo + 1);
    }
}
''',
test=r'''
class CountSmallerTest {

    private final CountSmaller solution = new CountSmaller();

    @Test
    void examples() {
        assertEquals(List.of(2, 1, 1, 0), solution.countSmaller(new int[]{5, 2, 6, 1}));
        assertEquals(List.of(0), solution.countSmaller(new int[]{-1}));
        assertEquals(List.of(0, 0), solution.countSmaller(new int[]{-1, -1}));
        assertEquals(List.of(2, 0, 0), solution.countSmaller(new int[]{2, 0, 1}));
    }

    @Test
    void matchesBruteForce() {
        Random rnd = new Random(3);
        int[] a = new int[300];
        for (int i = 0; i < a.length; i++) a[i] = rnd.nextInt(41) - 20;
        List<Integer> got = solution.countSmaller(a);
        for (int i = 0; i < a.length; i++) {
            int c = 0;
            for (int j = i + 1; j < a.length; j++) if (a[j] < a[i]) c++;
            assertEquals(c, got.get(i));
        }
    }
}
''',
trace=r'''
function run(nums) {
  const n = nums.length, count = new Array(n).fill(0); let idx = nums.map((_, i) => i);
  A.step('Merge sort the positions by value. Count, for each element, the smaller right-half elements that overtake it.', A.arr('nums', nums), A.arr('count', count));
  (function sort(lo, hi) {
    if (lo >= hi) return;
    const mid = (lo + hi) >> 1; sort(lo, mid); sort(mid + 1, hi);
    const buf = []; let i = lo, j = mid + 1; const notes = [];
    while (i <= mid || j <= hi) {
      if (j > hi || (i <= mid && nums[idx[i]] <= nums[idx[j]])) { const c = j - (mid + 1); if (c) notes.push(`${nums[idx[i]]} +${c}`); count[idx[i]] += c; buf.push(idx[i++]); }
      else buf.push(idx[j++]);
    }
    const left = idx.slice(lo, mid + 1).map(k => nums[k]), right = idx.slice(mid + 1, hi + 1).map(k => nums[k]);
    for (let k = lo; k <= hi; k++) idx[k] = buf[k - lo];
    A.step(`Merge [${left}] with [${right}]. ${notes.length ? `Smaller ones overtook: ${notes.join(', ')}.` : 'No left element is overtaken.'}`, A.arr('sorted by value', idx.map(k => nums[k]), { range: [lo, hi] }), A.arr('count', count, { hl: Object.fromEntries(buf.map(k => [k, 'cur'])) }));
  })(0, n - 1);
  A.step(`Counts: [${count}].`, A.arr('nums', nums), A.arr('count', count, { hl: Object.fromEntries(count.map((_, i) => [i, 'ok'])) }));
}
A.scenario('Example', '[5,2,6,1]', () => run([5, 2, 6, 1]));
A.scenario('With ties', '[3,1,3,2,1]', () => run([3, 1, 3, 2, 1]));
''',
variants=[dict(
name="Brute force",
idea="For every element, scan everything to its right.",
approach=r'''
**Double loop.** Count `nums[j] < nums[i]` for each `j > i`.

* Time: **O(n²)** — every pair.
* Space: **O(1)** — besides the output.
''',
tc="n2", sc="1",
java=r'''
public class CountSmaller {

    public List<Integer> countSmaller(int[] nums) {
        List<Integer> out = new ArrayList<>(nums.length);
        for (int i = 0; i < nums.length; i++) {
            int c = 0;
            for (int j = i + 1; j < nums.length; j++) if (nums[j] < nums[i]) c++;
            out.add(c);
        }
        return out;
    }
}
''',
trace=r'''
function run(nums) {
  const out = [];
  A.step('For each element, look at everything to its right.', A.arr('nums', nums));
  nums.forEach((v, i) => {
    const hl = { [i]: 'cur' }; let c = 0;
    for (let j = i + 1; j < nums.length; j++) { if (nums[j] < v) { c++; hl[j] = 'ok'; } else hl[j] = 'dim'; }
    out.push(c);
    A.step(`${v}: ${c} smaller element${c === 1 ? '' : 's'} to the right.`, A.arr('nums', nums, { hl }), A.arr('count', out));
  });
  A.step(`Counts: [${out}].`, A.text('Result', `[${out}]`, 'ok'));
}
A.scenario('Example', '[5,2,6,1]', () => run([5, 2, 6, 1]));
''')]),
]
