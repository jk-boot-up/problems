PROBLEMS = [
P(num=17, slug="letter-combinations-of-a-phone-number", title="Letter Combinations of a Phone Number", diff="Medium", topic="Backtracking", cls="LetterCombinations",
idea="Choose one letter per digit, depth by depth; each complete choice is one combination.",
vname="Backtracking",
spec=r'''
Given a string of digits `2-9`, return all letter combinations the number could represent on a phone keypad
(`2 = abc, 3 = def, 4 = ghi, 5 = jkl, 6 = mno, 7 = pqrs, 8 = tuv, 9 = wxyz`), in any order. An empty input gives an empty list.

**Example**
```
Input:  digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Constraints**
* `0 <= digits.length <= 4`
''',
approach=r'''
**Backtracking.** At depth `i`, try each letter for `digits[i]`, append it, recurse to depth `i + 1`, then remove it. At depth
`digits.length` the builder holds a full combination.

* Time: **O(4ⁿ · n)** — up to 4 letters per digit, and each of the up to 4ⁿ results costs O(n) to copy.
* Space: **O(n)** — the recursion depth and builder (plus the output).
''',
tc="exp", sc="n",
java=r'''
public class LetterCombinations {

    private static final String[] KEYS = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        List<String> out = new ArrayList<>();
        if (!digits.isEmpty()) backtrack(digits, 0, new StringBuilder(), out);
        return out;
    }

    private void backtrack(String digits, int i, StringBuilder sb, List<String> out) {
        if (i == digits.length()) {
            out.add(sb.toString());
            return;
        }
        for (char c : KEYS[digits.charAt(i) - '0'].toCharArray()) {
            sb.append(c);
            backtrack(digits, i + 1, sb, out);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
''',
test=r'''
class LetterCombinationsTest {

    private final LetterCombinations solution = new LetterCombinations();

    @Test
    void twoDigits() {
        assertEquals(List.of("ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"), solution.letterCombinations("23"));
    }

    @Test
    void empty() {
        assertEquals(List.of(), solution.letterCombinations(""));
    }

    @Test
    void fourLetterKey() {
        assertEquals(List.of("p", "q", "r", "s"), solution.letterCombinations("7"));
    }
}
''',
trace=r'''
const KEYS = { 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz' };
function run(digits) {
  const out = [], path = [];
  A.step(`Pick one letter for each digit. ${[...digits].map(d => `${d} → ${KEYS[d]}`).join(', ')}.`, A.chars('digits', digits), A.arr('combinations', out));
  (function bt(i) {
    if (i === digits.length) { out.push(path.join('')); A.step(`All digits have a letter: record "${path.join('')}".`, A.chars('digits', digits), A.stack('current path', path), A.arr('combinations', out, { hl: { [out.length - 1]: 'ok' } })); return; }
    for (const c of KEYS[digits[i]]) {
      path.push(c);
      A.step(`Digit ${digits[i]}: try '${c}'.`, A.chars('digits', digits, { hl: { [i]: 'cur' } }), A.stack('current path', path), A.arr('combinations', out));
      bt(i + 1);
      path.pop();
    }
  })(0);
  A.step(`${out.length} combinations in total.`, A.arr('combinations', out, { hl: out.map((_, k) => [k, 'ok']) }));
}
A.scenario('Two digits', 'digits = "23"', () => run('23'));
''',
variants=[dict(
name="Iterative expansion",
idea="Start with [\"\"]; for each digit, extend every partial string with every letter of that digit.",
approach=r'''
**Breadth-first build.** Keep a list of partial strings; for each digit, replace the list by every partial string extended with
each of its letters.

* Time: **O(4ⁿ · n)** — the final list has up to 4ⁿ strings of length n.
* Space: **O(4ⁿ · n)** — the intermediate lists.
''',
tc="exp", sc="exp",
java=r'''
public class LetterCombinations {

    private static final String[] KEYS = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) return new ArrayList<>();
        List<String> partial = new ArrayList<>(List.of(""));
        for (char d : digits.toCharArray()) {
            List<String> next = new ArrayList<>();
            for (String p : partial) {
                for (char c : KEYS[d - '0'].toCharArray()) next.add(p + c);
            }
            partial = next;
        }
        return partial;
    }
}
''',
trace=r'''
const KEYS = { 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz' };
function run(digits) {
  let partial = [''];
  A.step('Start with one empty string.', A.arr('partial', ['""']));
  for (const d of digits) { partial = partial.flatMap(p => [...KEYS[d]].map(c => p + c)); A.step(`Digit ${d} (${KEYS[d]}): extend every partial string with each letter.`, A.arr('partial', partial, { hl: partial.map((_, i) => [i, 'sel']) })); }
  A.step(`${partial.length} combinations.`, A.text('Result', JSON.stringify(partial), 'ok'));
}
A.scenario('Two digits', 'digits = "23"', () => run('23'));
''')]),

P(num=77, slug="combinations", title="Combinations", diff="Medium", topic="Backtracking", cls="Combinations",
idea="Choose numbers in increasing order so each set is built exactly once; stop early when too few numbers remain.",
vname="Backtracking with pruning",
spec=r'''
Return all combinations of `k` numbers chosen from `1..n`, in any order.

**Example**
```
Input:  n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

**Constraints**
* `1 <= n <= 20`; `1 <= k <= n`
''',
approach=r'''
**Increasing choices.** `backtrack(start)`: if the path has `k` numbers, record it. Otherwise try each `i` from `start` up to
`n - (k - path.size()) + 1` (later starts could not fill the remaining slots), push `i`, recurse with `i + 1`, pop.

* Time: **O(C(n, k) · k)** — one copy of length k per combination.
* Space: **O(k)** — the recursion depth and path.
''',
tc="exp", sc="n",
java=r'''
public class Combinations {

    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> out = new ArrayList<>();
        backtrack(n, k, 1, new ArrayList<>(), out);
        return out;
    }

    private void backtrack(int n, int k, int start, List<Integer> path, List<List<Integer>> out) {
        if (path.size() == k) {
            out.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i <= n - (k - path.size()) + 1; i++) {
            path.add(i);
            backtrack(n, k, i + 1, path, out);
            path.removeLast();
        }
    }
}
''',
test=r'''
class CombinationsTest {

    private final Combinations solution = new Combinations();

    @Test
    void fourChooseTwo() {
        assertEquals(List.of(List.of(1, 2), List.of(1, 3), List.of(1, 4), List.of(2, 3), List.of(2, 4), List.of(3, 4)), solution.combine(4, 2));
    }

    @Test
    void chooseAll() {
        assertEquals(List.of(List.of(1, 2, 3)), solution.combine(3, 3));
    }

    @Test
    void count() {
        assertEquals(184756, solution.combine(20, 10).size());
    }
}
''',
trace=r'''
function run(n, k) {
  const out = [], path = [];
  A.step(`Choose ${k} of 1..${n}, always in increasing order, so each set appears once.`, A.arr('numbers', [...Array(n)].map((_, i) => i + 1)), A.arr('combinations', out));
  (function bt(start) {
    if (path.length === k) { out.push('[' + path + ']'); A.step(`Path [${path}] has ${k} numbers. Record it.`, A.stack('path', path), A.arr('combinations', out, { hl: { [out.length - 1]: 'ok' } })); return; }
    const last = n - (k - path.length) + 1;
    for (let i = start; i <= last; i++) {
      path.push(i);
      A.step(`Add ${i}. ${last < n ? `(Starting above ${last} could not fill the remaining slots, so those branches are pruned.)` : ''}`, A.arr('numbers', [...Array(n)].map((_, t) => t + 1), { hl: Object.fromEntries(path.map(v => [v - 1, 'sel']).concat([[i - 1, 'cur']])) }), A.stack('path', path), A.arr('combinations', out));
      bt(i + 1);
      path.pop();
    }
  })(1);
  A.step(`${out.length} combinations.`, A.arr('combinations', out));
}
A.scenario('4 choose 2', 'n = 4, k = 2', () => run(4, 2));
'''),

P(num=46, slug="permutations", title="Permutations", diff="Medium", topic="Backtracking", cls="Permutations",
idea="Fix positions left to right by swapping each remaining value into the current position.",
vname="In-place swapping",
spec=r'''
Given an array `nums` of **distinct** integers, return all possible permutations, in any order.

**Example**
```
Input:  nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]
```

**Constraints**
* `1 <= nums.length <= 6`; values are distinct.
''',
approach=r'''
**Swap into place.** `permute(i)`: positions `0..i-1` are fixed. For each `j >= i`, swap `nums[i]` and `nums[j]`, recurse with `i + 1`,
then swap back. At `i == n`, record the array.

* Time: **O(n · n!)** — n! permutations, each copied in O(n).
* Space: **O(n)** — the recursion depth (no "used" array needed).
''',
tc="exp", sc="n",
java=r'''
public class Permutations {

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> out = new ArrayList<>();
        permute(nums.clone(), 0, out);
        return out;
    }

    private void permute(int[] a, int i, List<List<Integer>> out) {
        if (i == a.length) {
            List<Integer> p = new ArrayList<>();
            for (int x : a) p.add(x);
            out.add(p);
            return;
        }
        for (int j = i; j < a.length; j++) {
            swap(a, i, j);
            permute(a, i + 1, out);
            swap(a, i, j);
        }
    }

    private static void swap(int[] a, int i, int j) {
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
}
''',
test=r'''
class PermutationsTest {

    private final Permutations solution = new Permutations();

    @Test
    void three() {
        assertEquals(Set.of(List.of(1, 2, 3), List.of(1, 3, 2), List.of(2, 1, 3), List.of(2, 3, 1), List.of(3, 1, 2), List.of(3, 2, 1)),
                new HashSet<>(solution.permute(new int[]{1, 2, 3})));
    }

    @Test
    void count() {
        assertEquals(720, solution.permute(new int[]{1, 2, 3, 4, 5, 6}).size());
    }

    @Test
    void single() {
        assertEquals(List.of(List.of(1)), solution.permute(new int[]{1}));
    }
}
''',
trace=r'''
function run(nums) {
  const a = nums.slice(), out = [];
  A.step('Fix positions left to right. For each position, swap every remaining value into it, recurse, then swap back.', A.arr('nums', a), A.arr('permutations', out));
  (function perm(i) {
    if (i === a.length) { out.push('[' + a + ']'); A.step(`Every position is fixed: record [${a}].`, A.arr('nums', a, { hl: a.map((_, t) => [t, 'ok']) }), A.arr('permutations', out, { hl: { [out.length - 1]: 'ok' } })); return; }
    for (let j = i; j < a.length; j++) {
      [a[i], a[j]] = [a[j], a[i]];
      A.step(`Position ${i}: swap in ${a[i]}${i !== j ? ` (from index ${j})` : ''}.`, A.arr('nums', a, { hl: a.map((_, t) => [t, t < i ? 'sel' : t === i ? 'cur' : '']) }), A.arr('permutations', out));
      perm(i + 1);
      [a[i], a[j]] = [a[j], a[i]];
    }
  })(0);
  A.step(`${out.length} permutations (${a.length}!).`, A.arr('permutations', out));
}
A.scenario('Three numbers', 'nums = [1,2,3]', () => run([1, 2, 3]));
''',
variants=[dict(
name="Path with used flags",
idea="Build each permutation in a path, marking which values are already used.",
approach=r'''
**Used array.** At each depth try every value whose `used` flag is false; mark it, recurse, unmark.

* Time: **O(n · n!)** — n! leaves, each copied in O(n).
* Space: **O(n)** — the path, flags and recursion.
''',
tc="exp", sc="n",
java=r'''
public class Permutations {

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> out = new ArrayList<>();
        backtrack(nums, new boolean[nums.length], new ArrayList<>(), out);
        return out;
    }

    private void backtrack(int[] nums, boolean[] used, List<Integer> path, List<List<Integer>> out) {
        if (path.size() == nums.length) {
            out.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            path.add(nums[i]);
            backtrack(nums, used, path, out);
            path.removeLast();
            used[i] = false;
        }
    }
}
''',
trace=r'''
function run(nums) {
  const used = nums.map(() => false), path = [], out = [];
  (function bt() {
    if (path.length === nums.length) { out.push('[' + path + ']'); A.step(`Record [${path}].`, A.stack('path', path), A.arr('permutations', out, { hl: { [out.length - 1]: 'ok' } })); return; }
    nums.forEach((v, i) => { if (used[i]) return; used[i] = true; path.push(v); A.step(`Use ${v}.`, A.arr('nums', nums, { hl: Object.fromEntries(used.map((u, t) => [t, u ? 'sel' : ''])) }), A.stack('path', path)); bt(); path.pop(); used[i] = false; });
  })();
}
A.scenario('Three numbers', 'nums = [1,2,3]', () => run([1, 2, 3]));
''')]),

P(num=39, slug="combination-sum", title="Combination Sum", diff="Medium", topic="Backtracking", cls="CombinationSum",
idea="Try candidates in sorted order, allowing reuse; stop a branch as soon as a candidate exceeds what remains.",
vname="Sorted backtracking",
spec=r'''
Given **distinct** positive `candidates` and a `target`, return all unique combinations whose sum is `target`. Each candidate may be
used **any number of times**. Two combinations are different if some number is used a different number of times.

**Example**
```
Input:  candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

**Constraints**
* `1 <= candidates.length <= 30`; `2 <= candidates[i] <= 40`; `1 <= target <= 40`
''',
approach=r'''
**Backtracking from a start index.** Sort the candidates. `bt(start, remaining)`: if `remaining == 0`, record the path. Otherwise for
`i >= start`, break once `candidates[i] > remaining`; else push it and recurse with the **same** `i` (reuse allowed).

* Time: **O(N^(T/M))** — roughly, with T the target and M the smallest candidate (the depth of the search tree).
* Space: **O(T/M)** — the recursion depth.
''',
tc="exp", sc="n",
java=r'''
public class CombinationSum {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        int[] c = candidates.clone();
        Arrays.sort(c);
        List<List<Integer>> out = new ArrayList<>();
        backtrack(c, 0, target, new ArrayList<>(), out);
        return out;
    }

    private void backtrack(int[] c, int start, int remaining, List<Integer> path, List<List<Integer>> out) {
        if (remaining == 0) {
            out.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < c.length && c[i] <= remaining; i++) {
            path.add(c[i]);
            backtrack(c, i, remaining - c[i], path, out);
            path.removeLast();
        }
    }
}
''',
test=r'''
class CombinationSumTest {

    private final CombinationSum solution = new CombinationSum();

    @Test
    void example1() {
        assertEquals(List.of(List.of(2, 2, 3), List.of(7)), solution.combinationSum(new int[]{2, 3, 6, 7}, 7));
    }

    @Test
    void example2() {
        assertEquals(List.of(List.of(2, 2, 2, 2), List.of(2, 3, 3), List.of(3, 5)), solution.combinationSum(new int[]{2, 3, 5}, 8));
    }

    @Test
    void none() {
        assertEquals(List.of(), solution.combinationSum(new int[]{2}, 1));
    }
}
''',
trace=r'''
function run(cands, target) {
  const c = cands.slice().sort((x, y) => x - y), out = [], path = [];
  A.step(`Sorted candidates: [${c}]. Each may be reused. Stop a branch once a candidate is larger than what remains.`, A.arr('candidates', c), A.vars({ target }));
  (function bt(start, rem) {
    if (rem === 0) { out.push('[' + path + ']'); A.step(`[${path}] adds up to ${target}. Record it.`, A.stack('path', path), A.arr('found', out, { hl: { [out.length - 1]: 'ok' } })); return; }
    for (let i = start; i < c.length; i++) {
      if (c[i] > rem) { A.step(`${c[i]} is larger than the remaining ${rem}. Every candidate after it is too, so stop this branch.`, A.arr('candidates', c, { hl: { [i]: 'bad' } }), A.stack('path', path), A.vars({ remaining: rem })); break; }
      path.push(c[i]);
      A.step(`Take ${c[i]}: ${rem - c[i]} remains.`, A.arr('candidates', c, { hl: { [i]: 'cur' } }), A.stack('path', path), A.vars({ remaining: rem - c[i] }));
      bt(i, rem - c[i]);
      path.pop();
    }
  })(0, target);
  A.step(`Combinations: ${out.join(', ')}.`, A.arr('found', out));
}
A.scenario('Target 7', 'candidates = [2,3,6,7]', () => run([2, 3, 6, 7], 7));
'''),

P(num=52, slug="n-queens-ii", title="N-Queens II", diff="Hard", topic="Backtracking", cls="NQueensII",
idea="Place one queen per row; three bitmasks track attacked columns and both diagonals.",
vname="Bitmask backtracking",
spec=r'''
Place `n` queens on an `n × n` chessboard so that no two attack each other (no shared row, column or diagonal). Return the number of
distinct solutions.

**Example**
```
Input:  n = 4
Output: 2
```

**Constraints**
* `1 <= n <= 9`
''',
approach=r'''
**Bitmasks.** Go row by row. `cols`, `diag1` and `diag2` mark attacked squares for the current row (the diagonal masks shift by one
column per row). Free squares are `~(cols | diag1 | diag2) & full`; take the lowest free bit, recurse, repeat.

* Time: **O(n!)** — at most n choices in row 0, n − 1 in row 1, and so on (far fewer after pruning).
* Space: **O(n)** — the recursion depth.
''',
tc="exp", sc="n",
java=r'''
public class NQueensII {

    public int totalNQueens(int n) {
        return place(n, 0, 0, 0, 0);
    }

    private int place(int n, int row, int cols, int diag1, int diag2) {
        if (row == n) return 1;
        int count = 0, full = (1 << n) - 1;
        int free = ~(cols | diag1 | diag2) & full;
        while (free != 0) {
            int bit = free & -free; // lowest free column
            free -= bit;
            count += place(n, row + 1, cols | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1);
        }
        return count;
    }
}
''',
test=r'''
class NQueensIITest {

    private final NQueensII solution = new NQueensII();

    @ParameterizedTest
    @CsvSource({"1,1", "2,0", "3,0", "4,2", "5,10", "8,92", "9,352"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.totalNQueens(n));
    }
}
''',
trace=r'''
function run(n) {
  const qs = []; let count = 0;
  const board = () => { const g = [...Array(n)].map(() => new Array(n).fill('')); qs.forEach((c, r) => (g[r][c] = '♛')); return g; };
  const attacked = r => { const s = new Set(); qs.forEach((c, rr) => { const d = r - rr; [c, c - d, c + d].forEach(x => x >= 0 && x < n && s.add(x)); }); return s; };
  A.step(`Place one queen per row on a ${n} × ${n} board. Red squares in the next row are attacked.`, A.grid('board', board()));
  (function place(r) {
    if (r === n) { count++; A.step(`All ${n} queens are placed: solution #${count}.`, A.grid('board', board(), { hl: qs.map((c, rr) => [`${rr},${c}`, 'ok']) }), A.vars({ solutions: count })); return; }
    const att = attacked(r);
    for (let c = 0; c < n; c++) {
      if (att.has(c)) continue;
      qs.push(c);
      A.step(`Row ${r}: column ${c} is safe. Place a queen.`, A.grid('board', board(), { hl: qs.map((cc, rr) => [`${rr},${cc}`, rr === r ? 'cur' : 'sel']).concat(r + 1 < n ? [...attacked(r + 1)].map(x => [`${r + 1},${x}`, 'bad']) : []) }), A.vars({ solutions: count }));
      place(r + 1);
      qs.pop();
    }
    if (r > 0 && [...Array(n).keys()].every(c => att.has(c))) A.step(`Row ${r}: every column is attacked. Backtrack.`, A.grid('board', board(), { hl: [...Array(n).keys()].map(c => [`${r},${c}`, 'bad']) }));
  })(0);
  A.step(`${count} solutions for n = ${n}.`, A.text('Result', count, 'ok'));
}
A.scenario('n = 4', 'two solutions', () => run(4));
''',
variants=[dict(
name="Boolean arrays",
idea="Same row-by-row search, tracking attacked columns and diagonals in boolean arrays.",
approach=r'''
**Three boolean arrays.** `col[c]`, `d1[r + c]` and `d2[r - c + n - 1]` mark attacked columns and diagonals.

* Time: **O(n!)** — same search tree as the bitmask version, with slightly more work per step.
* Space: **O(n)** — the arrays and recursion.
''',
tc="exp", sc="n",
java=r'''
public class NQueensII {

    private boolean[] col, d1, d2;

    public int totalNQueens(int n) {
        col = new boolean[n];
        d1 = new boolean[2 * n];
        d2 = new boolean[2 * n];
        return place(n, 0);
    }

    private int place(int n, int r) {
        if (r == n) return 1;
        int count = 0;
        for (int c = 0; c < n; c++) {
            if (col[c] || d1[r + c] || d2[r - c + n - 1]) continue;
            col[c] = d1[r + c] = d2[r - c + n - 1] = true;
            count += place(n, r + 1);
            col[c] = d1[r + c] = d2[r - c + n - 1] = false;
        }
        return count;
    }
}
''',
trace=r'''
function run(n) {
  const qs = []; let count = 0;
  (function place(r) {
    if (r === n) { count++; const g = [...Array(n)].map(() => new Array(n).fill('')); qs.forEach((c, rr) => (g[rr][c] = '♛')); A.step(`Solution #${count}.`, A.grid('board', g, { hl: qs.map((c, rr) => [`${rr},${c}`, 'ok']) })); return; }
    for (let c = 0; c < n; c++) if (qs.every((cc, rr) => cc !== c && Math.abs(cc - c) !== r - rr)) { qs.push(c); place(r + 1); qs.pop(); }
  })(0);
  A.step(`${count} solutions.`, A.text('Result', count, 'ok'));
}
A.scenario('n = 4', 'two solutions', () => run(4));
''')]),

P(num=22, slug="generate-parentheses", title="Generate Parentheses", diff="Medium", topic="Backtracking", cls="GenerateParentheses",
idea="Add '(' while some remain, and ')' only when it would close an open one.",
vname="Backtracking with open/close counts",
spec=r'''
Given `n` pairs of parentheses, generate all combinations of **well-formed** parentheses.

**Example**
```
Input:  n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Constraints**
* `1 <= n <= 8`
''',
approach=r'''
**Track open and close counts.** Append `(` if `open < n`; append `)` if `close < open`. A string of length `2n` built this way is
always valid, and every valid string is reached exactly once.

* Time: **O(4ⁿ / √n)** — the number of valid strings (the Catalan number), each of length 2n.
* Space: **O(n)** — the recursion depth.
''',
tc="exp", sc="n",
java=r'''
public class GenerateParentheses {

    public List<String> generateParenthesis(int n) {
        List<String> out = new ArrayList<>();
        backtrack(n, 0, 0, new StringBuilder(), out);
        return out;
    }

    private void backtrack(int n, int open, int close, StringBuilder sb, List<String> out) {
        if (sb.length() == 2 * n) {
            out.add(sb.toString());
            return;
        }
        if (open < n) {
            sb.append('(');
            backtrack(n, open + 1, close, sb, out);
            sb.deleteCharAt(sb.length() - 1);
        }
        if (close < open) {
            sb.append(')');
            backtrack(n, open, close + 1, sb, out);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
''',
test=r'''
class GenerateParenthesesTest {

    private final GenerateParentheses solution = new GenerateParentheses();

    @Test
    void three() {
        assertEquals(List.of("((()))", "(()())", "(())()", "()(())", "()()()"), solution.generateParenthesis(3));
    }

    @Test
    void one() {
        assertEquals(List.of("()"), solution.generateParenthesis(1));
    }

    @Test
    void catalanCount() {
        assertEquals(1430, solution.generateParenthesis(8).size());
    }
}
''',
trace=r'''
function run(n) {
  const out = []; let s = '';
  A.step(`Build strings of length ${2 * n}. Add '(' while fewer than ${n} are open; add ')' only when it closes an open one.`, A.vars({ open: 0, close: 0 }), A.arr('results', out));
  (function bt(open, close) {
    if (s.length === 2 * n) { out.push(s); A.step(`"${s}" is complete and well formed.`, A.chars('current', s), A.arr('results', out, { hl: { [out.length - 1]: 'ok' } })); return; }
    if (open < n) { s += '('; A.step(`Add '(' (${open + 1} opened).`, A.chars('current', s, { hl: { [s.length - 1]: 'cur' } }), A.vars({ open: open + 1, close })); bt(open + 1, close); s = s.slice(0, -1); }
    if (close < open) { s += ')'; A.step(`Add ')' to close one.`, A.chars('current', s, { hl: { [s.length - 1]: 'alt' } }), A.vars({ open, close: close + 1 })); bt(open, close + 1); s = s.slice(0, -1); }
  })(0, 0);
  A.step(`${out.length} well-formed strings.`, A.arr('results', out));
}
A.scenario('n = 3', 'five results', () => run(3));
'''),

P(num=79, slug="word-search", title="Word Search", diff="Medium", topic="Backtracking", cls="WordSearch",
idea="DFS from every cell, matching one letter per step and marking cells as used along the current path.",
vname="DFS backtracking",
spec=r'''
Given an `m × n` grid of letters and a `word`, return `true` if the word can be traced through **adjacent** cells (horizontally or
vertically), using each cell at most once.

**Example**
```
Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED" → true,  "SEE" → true,  "ABCB" → false
```

**Constraints**
* `1 <= m, n <= 6`; `1 <= word.length <= 15`
''',
approach=r'''
**Backtracking.** Try each cell as the start. `dfs(r, c, i)` fails if out of bounds or the letter differs from `word[i]`; otherwise
mark the cell (`'#'`), try the four neighbours for `i + 1`, then restore the letter.

* Time: **O(m·n·3^L)** — each start explores up to 3 new directions per letter (the cell it came from is used).
* Space: **O(L)** — the recursion depth.
''',
tc="exp", sc="n",
java=r'''
public class WordSearch {

    public boolean exist(char[][] board, String word) {
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                if (dfs(board, r, c, word, 0)) return true;
            }
        }
        return false;
    }

    private boolean dfs(char[][] b, int r, int c, String word, int i) {
        if (i == word.length()) return true;
        if (r < 0 || c < 0 || r >= b.length || c >= b[0].length || b[r][c] != word.charAt(i)) return false;
        char ch = b[r][c];
        b[r][c] = '#';
        boolean found = dfs(b, r + 1, c, word, i + 1) || dfs(b, r - 1, c, word, i + 1)
                || dfs(b, r, c + 1, word, i + 1) || dfs(b, r, c - 1, word, i + 1);
        b[r][c] = ch;
        return found;
    }
}
''',
test=r'''
class WordSearchTest {

    private final WordSearch solution = new WordSearch();

    private static char[][] board() {
        return new char[][]{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}};
    }

    @ParameterizedTest
    @CsvSource({"ABCCED,true", "SEE,true", "ABCB,false", "ASADFBCCEESE,true"})
    void searches(String word, boolean expected) {
        assertEquals(expected, solution.exist(board(), word));
    }
}
''',
trace=r'''
function run(rows, word) {
  const b = rows.map(r => [...r]), m = b.length, n = b[0].length, path = [];
  let found = false;
  const view = (msg, extra = []) => A.step(msg, A.grid('board', rows.map(r => [...r]), { hl: path.map(([x, y], k) => [`${x},${y}`, k === path.length - 1 ? 'cur' : 'ok']).concat(extra) }), A.chars('word', word, { hl: [...word].map((_, k) => [k, k < path.length ? 'ok' : '']) }));
  const dfs = (x, y, i) => {
    if (i === word.length) return true;
    if (x < 0 || y < 0 || x >= m || y >= n || b[x][y] !== word[i]) return false;
    const ch = b[x][y]; b[x][y] = '#'; path.push([x, y]);
    view(`'${ch}' at (${x},${y}) matches letter ${i + 1}. Look at its neighbours for '${word[i + 1] || ''}'.`);
    const ok = dfs(x + 1, y, i + 1) || dfs(x - 1, y, i + 1) || dfs(x, y + 1, i + 1) || dfs(x, y - 1, i + 1);
    if (!ok) { path.pop(); view(`No neighbour continues the word. Backtrack from (${x},${y}) and unmark it.`, [[`${x},${y}`, 'bad']]); }
    b[x][y] = ch; return ok;
  };
  for (let r = 0; r < m && !found; r++) for (let c = 0; c < n && !found; c++) if (b[r][c] === word[0]) found = dfs(r, c, 0);
  view(found ? `"${word}" was traced through adjacent cells.` : `"${word}" cannot be traced.`);
  A.step(found ? 'Found.' : 'Not found.', A.text('Result', String(found), found ? 'ok' : 'bad'));
}
A.scenario('Found', 'word = "ABCCED"', () => run(['ABCE', 'SFCS', 'ADEE'], 'ABCCED'));
A.scenario('Cell reuse needed', 'word = "ABCB"', () => run(['ABCE', 'SFCS', 'ADEE'], 'ABCB'));
'''),

P(num=108, slug="convert-sorted-array-to-binary-search-tree", title="Convert Sorted Array to Binary Search Tree", diff="Easy", topic="Divide & Conquer", cls="SortedArrayToBST",
idea="The middle element becomes the root; the left and right halves become balanced subtrees.",
vname="Middle element as root", helpers=["TreeNode"],
spec=r'''
Given a strictly increasing array `nums`, build a **height-balanced** BST (the depths of the two subtrees of every node differ by at
most one). Any valid answer is accepted.

**Example**
```
Input:  nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]   (one possible answer)
```

**Constraints**
* `1 <= nums.length <= 10^4`; strictly increasing.
''',
approach=r'''
**Divide and conquer.** `build(lo, hi)`: the middle index `mid = (lo + hi) / 2` is the root; build the left subtree from `lo..mid-1`
and the right from `mid+1..hi`. Halving keeps the tree balanced.

* Time: **O(n)** — each element becomes exactly one node.
* Space: **O(log n)** — the recursion depth.
''',
tc="n", sc="log",
java=r'''
public class SortedArrayToBST {

    public TreeNode sortedArrayToBST(int[] nums) {
        return build(nums, 0, nums.length - 1);
    }

    private TreeNode build(int[] nums, int lo, int hi) {
        if (lo > hi) return null;
        int mid = (lo + hi) >>> 1;
        return new TreeNode(nums[mid], build(nums, lo, mid - 1), build(nums, mid + 1, hi));
    }
}
''',
test=r'''
class SortedArrayToBSTTest {

    private final SortedArrayToBST solution = new SortedArrayToBST();

    private static int height(TreeNode n) {
        if (n == null) return 0;
        int l = height(n.left), r = height(n.right);
        if (l < 0 || r < 0 || Math.abs(l - r) > 1) return -1;
        return 1 + Math.max(l, r);
    }

    private static void inorder(TreeNode n, List<Integer> out) {
        if (n == null) return;
        inorder(n.left, out);
        out.add(n.val);
        inorder(n.right, out);
    }

    @Test
    void balancedAndSorted() {
        int[] nums = {-10, -3, 0, 5, 9};
        TreeNode root = solution.sortedArrayToBST(nums);
        assertTrue(height(root) > 0);
        List<Integer> values = new ArrayList<>();
        inorder(root, values);
        assertEquals(List.of(-10, -3, 0, 5, 9), values);
    }

    @Test
    void large() {
        int[] nums = new int[1000];
        for (int i = 0; i < nums.length; i++) nums[i] = i;
        assertEquals(10, height(solution.sortedArrayToBST(nums)));
    }
}
''',
trace=r'''
function run(nums) {
  let root = null;
  A.step('The middle value becomes the root, so both sides get the same number of values (or one fewer).', A.arr('nums', nums));
  (function build(lo, hi, attach) {
    if (lo > hi) return;
    const mid = (lo + hi) >> 1, node = A.node(nums[mid]);
    if (!root) root = node; attach(node);
    A.step(`Range ${lo}..${hi}: the middle is ${nums[mid]}. Its left half becomes the left subtree, its right half the right subtree.`, A.arr('nums', nums, { range: [lo, hi], hl: { [mid]: 'cur' } }), A.tree('BST', root, { hl: { [node.id]: 'cur' } }));
    build(lo, mid - 1, c => (node.left = c)); build(mid + 1, hi, c => (node.right = c));
  })(0, nums.length - 1, () => {});
  A.step('The tree is height-balanced, and its in-order traversal is the sorted array.', A.tree('BST', root));
}
A.scenario('Five values', 'nums = [-10,-3,0,5,9]', () => run([-10, -3, 0, 5, 9]));
A.scenario('Seven values', 'nums = [1..7]', () => run([1, 2, 3, 4, 5, 6, 7]));
'''),

P(num=148, slug="sort-list", title="Sort List", diff="Medium", topic="Divide & Conquer", cls="SortList",
idea="Merge sort without recursion: merge runs of size 1, 2, 4, … across the whole list.",
vname="Bottom-up merge sort (O(1) space)", helpers=["ListNode"],
spec=r'''
Sort a linked list in ascending order and return its head.

**Example**
```
Input:  4 → 2 → 1 → 3
Output: 1 → 2 → 3 → 4
```

**Constraints**
* `0 <= n <= 5 * 10^4`; `-10^5 <= Node.val <= 10^5`

**Follow-up:** O(n log n) time and O(1) memory.
''',
approach=r'''
**Bottom-up merge sort.** For `size = 1, 2, 4, …` while `size < length`: walk the list, cut off two runs of `size` nodes, merge them, and
attach the result to the tail of the rebuilt list. No recursion, so the extra memory is constant.

* Time: **O(n log n)** — log n rounds, each a linear pass.
* Space: **O(1)** — only a few pointers.
''',
tc="nlogn", sc="1",
java=r'''
public class SortList {

    public ListNode sortList(ListNode head) {
        int length = 0;
        for (ListNode p = head; p != null; p = p.next) length++;
        ListNode dummy = new ListNode(0, head);
        for (int size = 1; size < length; size <<= 1) {
            ListNode tail = dummy, cur = dummy.next;
            while (cur != null) {
                ListNode left = cur;
                ListNode right = split(left, size);
                cur = split(right, size);
                tail = merge(left, right, tail);
            }
        }
        return dummy.next;
    }

    /** Cuts the list after size nodes and returns the head of the rest. */
    private static ListNode split(ListNode head, int size) {
        for (int i = 1; head != null && i < size; i++) head = head.next;
        if (head == null) return null;
        ListNode rest = head.next;
        head.next = null;
        return rest;
    }

    /** Merges a and b after tail and returns the new tail. */
    private static ListNode merge(ListNode a, ListNode b, ListNode tail) {
        while (a != null && b != null) {
            if (a.val <= b.val) { tail.next = a; a = a.next; } else { tail.next = b; b = b.next; }
            tail = tail.next;
        }
        tail.next = a != null ? a : b;
        while (tail.next != null) tail = tail.next;
        return tail;
    }
}
''',
test=r'''
class SortListTest {

    private final SortList solution = new SortList();

    @Test
    void four() {
        assertArrayEquals(new int[]{1, 2, 3, 4}, ListNode.toArray(solution.sortList(ListNode.of(4, 2, 1, 3))));
    }

    @Test
    void withNegatives() {
        assertArrayEquals(new int[]{-1, 0, 3, 4, 5}, ListNode.toArray(solution.sortList(ListNode.of(-1, 5, 3, 4, 0))));
    }

    @Test
    void empty() {
        assertNull(solution.sortList(null));
    }

    @Test
    void random() {
        Random rnd = new Random(7);
        int[] values = rnd.ints(1000, -100, 100).toArray();
        int[] expected = values.clone();
        Arrays.sort(expected);
        assertArrayEquals(expected, ListNode.toArray(solution.sortList(ListNode.of(values))));
    }
}
''',
trace=r'''
function run(vals) {
  let a = vals.slice();
  A.step('Bottom-up merge sort: merge runs of size 1, then 2, then 4, until one run covers the whole list.', A.list('list', a));
  for (let size = 1; size < a.length; size *= 2) {
    const out = [];
    for (let i = 0; i < a.length; i += 2 * size) {
      const L = a.slice(i, i + size), R = a.slice(i + size, i + 2 * size), m = [];
      let x = 0, y = 0; while (x < L.length && y < R.length) m.push(L[x] <= R[y] ? L[x++] : R[y++]); m.push(...L.slice(x), ...R.slice(y));
      out.push(...m);
      A.step(`Size ${size}: merge [${L}] with [${R.length ? R : '∅'}] into [${m}].`, A.list('list', out.concat(a.slice(i + 2 * size)), { hl: [...Array(m.length).keys()].map(t => [i + t, 'ok']) }), A.vars({ runSize: size }));
    }
    a = out;
  }
  A.step('One sorted run remains. Only pointers were rearranged: no recursion and no extra list.', A.list('sorted', a, { hl: a.map((_, i) => [i, 'ok']) }));
}
A.scenario('Six values', '5→2→4→6→1→3', () => run([5, 2, 4, 6, 1, 3]));
''',
variants=[dict(
name="Top-down merge sort",
idea="Split at the middle with slow and fast pointers, sort both halves recursively, then merge them.",
approach=r'''
**Recursive merge sort.** Find the middle with slow/fast pointers, cut the list, sort each half, merge.

* Time: **O(n log n)** — log n levels of linear merging.
* Space: **O(log n)** — the recursion stack.
''',
tc="nlogn", sc="log",
java=r'''
public class SortList {

    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode slow = head, fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode right = slow.next;
        slow.next = null;
        return merge(sortList(head), sortList(right));
    }

    private static ListNode merge(ListNode a, ListNode b) {
        ListNode dummy = new ListNode(0), tail = dummy;
        while (a != null && b != null) {
            if (a.val <= b.val) { tail.next = a; a = a.next; } else { tail.next = b; b = b.next; }
            tail = tail.next;
        }
        tail.next = a != null ? a : b;
        return dummy.next;
    }
}
''',
trace=r'''
function run(vals) {
  const sort = (a, depth) => {
    if (a.length <= 1) return a;
    const mid = Math.ceil(a.length / 2), L = a.slice(0, mid), R = a.slice(mid);
    A.step(`${'  '.repeat(depth)}Split [${a}] into [${L}] and [${R}].`, A.list('left half', L), A.list('right half', R), A.vars({ depth }));
    const sl = sort(L, depth + 1), sr = sort(R, depth + 1), m = [];
    let x = 0, y = 0; while (x < sl.length && y < sr.length) m.push(sl[x] <= sr[y] ? sl[x++] : sr[y++]); m.push(...sl.slice(x), ...sr.slice(y));
    A.step(`Merge [${sl}] and [${sr}] into [${m}].`, A.list('merged', m, { hl: m.map((_, i) => [i, 'ok']) }), A.vars({ depth }));
    return m;
  };
  sort(vals, 0);
}
A.scenario('Four values', '4→2→1→3', () => run([4, 2, 1, 3]));
''')]),

P(num=427, slug="construct-quad-tree", title="Construct Quad-Tree", diff="Medium", topic="Divide & Conquer", cls="ConstructQuadTree",
idea="If a square is uniform it becomes a leaf; otherwise split it into four quadrants and recurse.",
vname="Recursive quadrants",
spec=r'''
Given an `n × n` grid of `0`s and `1`s (`n` a power of two), build its **quad tree**. Each node has `val`, `isLeaf` and four children
(`topLeft`, `topRight`, `bottomLeft`, `bottomRight`). A uniform region is a leaf whose `val` is that value; any other region is an
internal node (its `val` may be anything) whose four children represent its four equal quadrants.

**Example**
```
Input:  grid = [[0,1],[1,0]]
Output: an internal node with four leaves 0, 1, 1, 0
```

**Constraints**
* `n == 2^x` with `0 <= x <= 6`
''',
approach=r'''
**Build bottom-up by recursion.** `build(r, c, size)`: for size 1 return a leaf. Otherwise build the four quadrants; if all four are
leaves with the same value, merge them into one leaf, else return an internal node with those children.

* Time: **O(n²)** — every cell is visited once, and each internal node does O(1) merging work.
* Space: **O(log n)** — the recursion depth (plus the tree itself).
''',
tc="n2", sc="log",
java=r'''
public class ConstructQuadTree {

    /** Quad tree node. */
    public static class Node {
        public boolean val, isLeaf;
        public Node topLeft, topRight, bottomLeft, bottomRight;

        public Node(boolean val, boolean isLeaf) {
            this.val = val;
            this.isLeaf = isLeaf;
        }

        public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
            this(val, isLeaf);
            this.topLeft = topLeft;
            this.topRight = topRight;
            this.bottomLeft = bottomLeft;
            this.bottomRight = bottomRight;
        }
    }

    public Node construct(int[][] grid) {
        return build(grid, 0, 0, grid.length);
    }

    private Node build(int[][] g, int r, int c, int size) {
        if (size == 1) return new Node(g[r][c] == 1, true);
        int h = size / 2;
        Node tl = build(g, r, c, h), tr = build(g, r, c + h, h), bl = build(g, r + h, c, h), br = build(g, r + h, c + h, h);
        if (tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf && tl.val == tr.val && tr.val == bl.val && bl.val == br.val) {
            return new Node(tl.val, true);
        }
        return new Node(true, false, tl, tr, bl, br);
    }
}
''',
test=r'''
class ConstructQuadTreeTest {

    private final ConstructQuadTree solution = new ConstructQuadTree();

    /** Serializes like LeetCode: [isLeaf, val] per node in level order. */
    private static List<String> serialize(ConstructQuadTree.Node root) {
        List<String> out = new ArrayList<>();
        Deque<ConstructQuadTree.Node> q = new ArrayDeque<>(List.of(root));
        while (!q.isEmpty()) {
            ConstructQuadTree.Node n = q.poll();
            out.add(n.isLeaf ? "[1," + (n.val ? 1 : 0) + "]" : "[0,*]");
            if (!n.isLeaf) q.addAll(List.of(n.topLeft, n.topRight, n.bottomLeft, n.bottomRight));
        }
        return out;
    }

    @Test
    void checkerboard() {
        assertEquals(List.of("[0,*]", "[1,0]", "[1,1]", "[1,1]", "[1,0]"), serialize(solution.construct(new int[][]{{0, 1}, {1, 0}})));
    }

    @Test
    void uniform() {
        assertEquals(List.of("[1,1]"), serialize(solution.construct(new int[][]{{1, 1}, {1, 1}})));
    }

    @Test
    void mixed() {
        int[][] g = {{1, 1, 0, 0}, {1, 1, 0, 0}, {1, 1, 1, 1}, {1, 1, 1, 1}};
        assertEquals(List.of("[0,*]", "[1,1]", "[1,0]", "[1,1]", "[1,1]"), serialize(solution.construct(g)));
    }
}
''',
trace=r'''
function run(g) {
  const n = g.length, leaves = [];
  const view = (msg, r, c, s, cls) => A.step(msg, A.grid('grid', g, { hl: leaves.flatMap(([lr, lc, ls, v]) => { const o = []; for (let i = lr; i < lr + ls; i++) for (let j = lc; j < lc + ls; j++) o.push([`${i},${j}`, v ? 'ok' : 'sel']); return o; }).concat(cls ? (() => { const o = []; for (let i = r; i < r + s; i++) for (let j = c; j < c + s; j++) o.push([`${i},${j}`, cls]); return o; })() : []) }), A.vars({ leaves: leaves.length }));
  view('Uniform squares become leaves. Mixed squares split into four quadrants.');
  (function build(r, c, s) {
    let uniform = true; for (let i = r; i < r + s; i++) for (let j = c; j < c + s; j++) if (g[i][j] !== g[r][c]) uniform = false;
    if (uniform) { leaves.push([r, c, s, g[r][c]]); view(`The ${s} × ${s} square at (${r},${c}) is all ${g[r][c]}: one leaf.`, r, c, s); return; }
    view(`The ${s} × ${s} square at (${r},${c}) is mixed: split it into four ${s / 2} × ${s / 2} quadrants.`, r, c, s, 'cur');
    const h = s / 2; build(r, c, h); build(r, c + h, h); build(r + h, c, h); build(r + h, c + h, h);
  })(0, 0, n);
  A.step(`Done: ${leaves.length} leaves describe the whole grid.`, A.text('Result', `${leaves.length} leaves`, 'ok'));
}
A.scenario('4 × 4 grid', 'two uniform halves and a mixed corner', () => run([[1, 1, 0, 1], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]));
'''),
]
