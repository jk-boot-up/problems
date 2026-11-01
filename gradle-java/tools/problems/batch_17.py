PROBLEMS = [
P(num=75, slug="sort-colors", title="Sort Colors", diff="Medium", topic="Two Pointers", cls="SortColors",
idea="Dutch national flag: three regions (0s, 1s, 2s) grow from both ends in one pass.",
vname="Dutch national flag",
spec=r'''
`nums` holds only `0`, `1` and `2` (red, white, blue). Sort it **in place** so equal colours are adjacent in that order, without a
library sort.

**Example**
```
[2,0,2,1,1,0] → [0,0,1,1,2,2]
```

**Constraints**
* `1 <= n <= 300`

**Follow-up:** one pass, constant space.
''',
approach=r'''
**Three pointers.** `lo` is the end of the 0s, `hi` the start of the 2s, `i` the scanner. A 0 swaps to `lo` (both advance), a 2
swaps to `hi` (only `hi` moves, the swapped-in value still needs checking), a 1 just advances `i`.

* Time: **O(n)** — each element is examined at most twice.
* Space: **O(1)** — three indices.
''',
java=r'''
public class SortColors {

    public void sortColors(int[] nums) {
        int lo = 0, i = 0, hi = nums.length - 1;
        while (i <= hi) {
            if (nums[i] == 0) swap(nums, lo++, i++);
            else if (nums[i] == 2) swap(nums, i, hi--);
            else i++;
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
class SortColorsTest {

    private final SortColors solution = new SortColors();

    @Test
    void examples() {
        int[] a = {2, 0, 2, 1, 1, 0};
        solution.sortColors(a);
        assertArrayEquals(new int[]{0, 0, 1, 1, 2, 2}, a);
        int[] b = {2, 0, 1};
        solution.sortColors(b);
        assertArrayEquals(new int[]{0, 1, 2}, b);
    }
}
''',
trace=r'''
function run(a) {
  let lo = 0, i = 0, hi = a.length - 1;
  const view = (msg, x) => A.step(msg, A.arr('nums', a, { ptr: [[lo, 'lo'], [i, 'i'], [hi, 'hi']], hl: Object.fromEntries(a.map((_, t) => [t, t < lo ? 'bad' : t > hi ? 'sel' : t < i ? 'dim' : t === i ? 'cur' : ''])) }));
  view('Everything left of lo is 0, everything right of hi is 2, and lo..i−1 is 1. i scans the unknown middle.');
  while (i <= hi) {
    if (a[i] === 0) { [a[lo], a[i]] = [a[i], a[lo]]; lo++; i++; view('A 0: swap it into the 0 region and advance lo and i.'); }
    else if (a[i] === 2) { [a[i], a[hi]] = [a[hi], a[i]]; hi--; view('A 2: swap it into the 2 region. Only hi moves, because the swapped-in value is still unchecked.'); }
    else { i++; view('A 1 is already in the right region. Advance i.'); }
  }
  A.step('One pass, and the colours are sorted.', A.arr('nums', a), A.text('Result', JSON.stringify(a), 'ok'));
}
A.scenario('Six colours', 'nums = [2,0,2,1,1,0]', () => run([2, 0, 2, 1, 1, 0]));
'''),

P(num=78, slug="subsets", title="Subsets", diff="Medium", topic="Backtracking", cls="Subsets",
idea="Each element is either in or out; backtracking records the path at every node of the decision tree.",
vname="Backtracking",
spec=r'''
Given an array of **unique** integers, return all possible subsets (the power set), in any order, without duplicates.

**Example**
```
[1,2,3] → [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Constraints**
* `1 <= nums.length <= 10`
''',
approach=r'''
**Start index recursion.** Record the current path, then for each `i >= start` add `nums[i]`, recurse with `i + 1`, remove it.
Every subset is produced exactly once, in increasing index order.

* Time: **O(n · 2ⁿ)** — 2ⁿ subsets, each copied in O(n).
* Space: **O(n)** — the recursion depth.
''',
tc="exp", sc="n",
java=r'''
public class Subsets {

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> out = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), out);
        return out;
    }

    private void backtrack(int[] nums, int start, List<Integer> path, List<List<Integer>> out) {
        out.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrack(nums, i + 1, path, out);
            path.removeLast();
        }
    }
}
''',
test=r'''
class SubsetsTest {

    private final Subsets solution = new Subsets();

    @Test
    void three() {
        Set<List<Integer>> got = new HashSet<>(solution.subsets(new int[]{1, 2, 3}));
        assertEquals(8, got.size());
        assertTrue(got.containsAll(List.of(List.of(), List.of(1, 2, 3), List.of(2), List.of(1, 3))));
    }

    @Test
    void single() {
        assertEquals(List.of(List.of(), List.of(0)), solution.subsets(new int[]{0}));
    }
}
''',
trace=r'''
function run(nums) {
  const out = [], path = [];
  (function bt(start) {
    out.push('[' + path + ']');
    A.step(`Record [${path}].`, A.arr('nums', nums, { hl: Object.fromEntries(path.map(v => [nums.indexOf(v), 'sel'])) }), A.stack('path', path), A.arr('subsets', out, { hl: { [out.length - 1]: 'ok' } }));
    for (let i = start; i < nums.length; i++) { path.push(nums[i]); bt(i + 1); path.pop(); }
  })(0);
  A.step(`${out.length} subsets = 2^${nums.length}.`, A.arr('subsets', out));
}
A.scenario('Three numbers', 'nums = [1,2,3]', () => run([1, 2, 3]));
''',
variants=[dict(
name="Bitmask enumeration",
idea="Each number from 0 to 2ⁿ − 1 is a bitmask choosing a subset.",
approach=r'''
**Bitmasks.** For `mask` in `0 .. 2ⁿ - 1`, include `nums[i]` when bit `i` is set.

* Time: **O(n · 2ⁿ)** — 2ⁿ masks, n bits each.
* Space: **O(n)** — one subset at a time (plus the output).
''',
tc="exp", sc="n",
java=r'''
public class Subsets {

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> out = new ArrayList<>();
        for (int mask = 0; mask < (1 << nums.length); mask++) {
            List<Integer> s = new ArrayList<>();
            for (int i = 0; i < nums.length; i++) {
                if ((mask >> i & 1) == 1) s.add(nums[i]);
            }
            out.add(s);
        }
        return out;
    }
}
''',
trace=r'''
function run(nums) {
  const out = [];
  for (let m = 0; m < 1 << nums.length; m++) {
    const s = nums.filter((_, i) => (m >> i) & 1); out.push('[' + s + ']');
    A.step(`Mask ${m.toString(2).padStart(nums.length, '0')} picks [${s}].`, A.arr('nums', nums, { hl: Object.fromEntries(nums.map((_, i) => [i, (m >> i) & 1 ? 'ok' : 'dim'])) }), A.arr('subsets', out));
  }
}
A.scenario('Three numbers', 'nums = [1,2,3]', () => run([1, 2, 3]));
''')]),

P(num=90, slug="subsets-ii", title="Subsets II", diff="Medium", topic="Backtracking", cls="SubsetsII",
idea="Sort, then at each depth skip a value equal to the previous one tried at that same depth.",
vname="Sorted backtracking with skips",
spec=r'''
`nums` may contain duplicates. Return all **distinct** subsets, in any order.

**Example**
```
[1,2,2] → [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Constraints**
* `1 <= nums.length <= 10`
''',
approach=r'''
**Skip duplicate branches.** Sort. In the loop at a given depth, skip `i > start` with `nums[i] == nums[i-1]`: that choice would
start a branch identical to the one just explored.

* Time: **O(n · 2ⁿ)** — at most 2ⁿ subsets, each copied in O(n).
* Space: **O(n)** — the recursion depth.
''',
tc="exp", sc="n",
java=r'''
public class SubsetsII {

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        List<List<Integer>> out = new ArrayList<>();
        backtrack(a, 0, new ArrayList<>(), out);
        return out;
    }

    private void backtrack(int[] a, int start, List<Integer> path, List<List<Integer>> out) {
        out.add(new ArrayList<>(path));
        for (int i = start; i < a.length; i++) {
            if (i > start && a[i] == a[i - 1]) continue;
            path.add(a[i]);
            backtrack(a, i + 1, path, out);
            path.removeLast();
        }
    }
}
''',
test=r'''
class SubsetsIITest {

    private final SubsetsII solution = new SubsetsII();

    @Test
    void duplicates() {
        assertEquals(List.of(List.of(), List.of(1), List.of(1, 2), List.of(1, 2, 2), List.of(2), List.of(2, 2)),
                solution.subsetsWithDup(new int[]{1, 2, 2}));
    }

    @Test
    void single() {
        assertEquals(List.of(List.of(), List.of(0)), solution.subsetsWithDup(new int[]{0}));
    }
}
''',
trace=r'''
function run(nums) {
  const a = nums.slice().sort((x, y) => x - y), out = [], path = [];
  (function bt(start) {
    out.push('[' + path + ']');
    A.step(`Record [${path}].`, A.stack('path', path), A.arr('subsets', out, { hl: { [out.length - 1]: 'ok' } }));
    for (let i = start; i < a.length; i++) {
      if (i > start && a[i] === a[i - 1]) { A.step(`Skip a second ${a[i]} at this depth: it would repeat the branch we just explored.`, A.arr('sorted', a, { hl: { [i]: 'bad', [i - 1]: 'sel' } }), A.stack('path', path)); continue; }
      path.push(a[i]); bt(i + 1); path.pop();
    }
  })(0);
  A.step(`${out.length} distinct subsets.`, A.arr('subsets', out));
}
A.scenario('Duplicate 2s', 'nums = [1,2,2]', () => run([1, 2, 2]));
'''),

P(num=40, slug="combination-sum-ii", title="Combination Sum II", diff="Medium", topic="Backtracking", cls="CombinationSumII",
idea="Sorted backtracking where each candidate is used once and equal candidates are skipped at the same depth.",
vname="Sorted backtracking with skips",
spec=r'''
Find all unique combinations of `candidates` that sum to `target`. Each candidate may be used **once**; the input may contain duplicates,
but the output must not contain duplicate combinations.

**Example**
```
candidates = [10,1,2,7,6,1,5], target = 8 → [[1,1,6],[1,2,5],[1,7],[2,6]]
```

**Constraints**
* `1 <= candidates.length <= 100`; `1 <= target <= 30`
''',
approach=r'''
**Backtracking.** Sort. At each depth iterate `i >= start`, skip `nums[i] == nums[i-1]` when `i > start`, stop once `nums[i] > remaining`,
and recurse with `i + 1` (no reuse).

* Time: **O(2ⁿ · n)** — worst case explores every subset.
* Space: **O(n)** — the recursion depth.
''',
tc="exp", sc="n",
java=r'''
public class CombinationSumII {

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
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
            if (i > start && c[i] == c[i - 1]) continue;
            path.add(c[i]);
            backtrack(c, i + 1, remaining - c[i], path, out);
            path.removeLast();
        }
    }
}
''',
test=r'''
class CombinationSumIITest {

    private final CombinationSumII solution = new CombinationSumII();

    @Test
    void example1() {
        assertEquals(List.of(List.of(1, 1, 6), List.of(1, 2, 5), List.of(1, 7), List.of(2, 6)), solution.combinationSum2(new int[]{10, 1, 2, 7, 6, 1, 5}, 8));
    }

    @Test
    void example2() {
        assertEquals(List.of(List.of(1, 2, 2), List.of(5)), solution.combinationSum2(new int[]{2, 5, 2, 1, 2}, 5));
    }
}
''',
trace=r'''
function run(cands, target) {
  const c = cands.slice().sort((x, y) => x - y), out = [], path = [];
  A.step(`Sorted: [${c}]. Each number is used at most once; equal numbers are not tried twice at the same depth.`, A.arr('candidates', c));
  (function bt(start, rem) {
    if (rem === 0) { out.push('[' + path + ']'); A.step(`[${path}] adds up to ${target}.`, A.stack('path', path), A.arr('found', out, { hl: { [out.length - 1]: 'ok' } })); return; }
    for (let i = start; i < c.length && c[i] <= rem; i++) {
      if (i > start && c[i] === c[i - 1]) continue;
      path.push(c[i]); A.step(`Take ${c[i]}; ${rem - c[i]} remains.`, A.arr('candidates', c, { hl: { [i]: 'cur' } }), A.stack('path', path));
      bt(i + 1, rem - c[i]); path.pop();
    }
  })(0, target);
}
A.scenario('Target 5', 'candidates = [2,5,2,1,2]', () => run([2, 5, 2, 1, 2], 5));
'''),

P(num=47, slug="permutations-ii", title="Permutations II", diff="Medium", topic="Backtracking", cls="PermutationsII",
idea="Sort, and only use a duplicate value when its earlier twin is already in the path, so equal values keep a fixed order.",
vname="Sorted backtracking with used flags",
spec=r'''
`nums` may contain duplicates. Return all **unique** permutations, in any order.

**Example**
```
[1,1,2] → [[1,1,2],[1,2,1],[2,1,1]]
```

**Constraints**
* `1 <= nums.length <= 8`
''',
approach=r'''
**Order equal values.** Sort. Skip `nums[i]` if it is used, or if `nums[i] == nums[i-1]` and `nums[i-1]` is **not** used: that forces
equal values to be placed left to right, so each distinct arrangement appears once.

* Time: **O(n · n!)** — at most n! permutations, each copied in O(n).
* Space: **O(n)** — flags and recursion.
''',
tc="exp", sc="n",
java=r'''
public class PermutationsII {

    public List<List<Integer>> permuteUnique(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        List<List<Integer>> out = new ArrayList<>();
        backtrack(a, new boolean[a.length], new ArrayList<>(), out);
        return out;
    }

    private void backtrack(int[] a, boolean[] used, List<Integer> path, List<List<Integer>> out) {
        if (path.size() == a.length) {
            out.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < a.length; i++) {
            if (used[i] || (i > 0 && a[i] == a[i - 1] && !used[i - 1])) continue;
            used[i] = true;
            path.add(a[i]);
            backtrack(a, used, path, out);
            path.removeLast();
            used[i] = false;
        }
    }
}
''',
test=r'''
class PermutationsIITest {

    private final PermutationsII solution = new PermutationsII();

    @Test
    void duplicates() {
        assertEquals(List.of(List.of(1, 1, 2), List.of(1, 2, 1), List.of(2, 1, 1)), solution.permuteUnique(new int[]{1, 1, 2}));
    }

    @Test
    void distinct() {
        assertEquals(6, solution.permuteUnique(new int[]{1, 2, 3}).size());
    }
}
''',
trace=r'''
function run(nums) {
  const a = nums.slice().sort((x, y) => x - y), used = a.map(() => false), path = [], out = [];
  (function bt() {
    if (path.length === a.length) { out.push('[' + path + ']'); A.step(`Record [${path}].`, A.arr('permutations', out, { hl: { [out.length - 1]: 'ok' } })); return; }
    for (let i = 0; i < a.length; i++) {
      if (used[i]) continue;
      if (i > 0 && a[i] === a[i - 1] && !used[i - 1]) { A.step(`Skip this ${a[i]}: its earlier twin is unused, so this branch would repeat one we already explored.`, A.arr('sorted', a, { hl: { [i]: 'bad', [i - 1]: 'sel' } }), A.stack('path', path)); continue; }
      used[i] = true; path.push(a[i]); bt(); path.pop(); used[i] = false;
    }
  })();
}
A.scenario('With duplicates', 'nums = [1,1,2]', () => run([1, 1, 2]));
'''),

P(num=51, slug="n-queens", title="N-Queens", diff="Hard", topic="Backtracking", cls="NQueens",
idea="Row by row, place a queen in a column not attacked by column or either diagonal; record full boards.",
vname="Backtracking with attack sets",
spec=r'''
Return all distinct solutions to the `n`-queens puzzle as boards of strings, where `'Q'` is a queen and `'.'` an empty square.

**Example**
```
n = 4 → [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
```

**Constraints**
* `1 <= n <= 9`
''',
approach=r'''
**Backtracking.** Row by row, try each column whose `col[c]`, `d1[r + c]` and `d2[r - c + n - 1]` flags are free. When all rows are
filled, build the board strings.

* Time: **O(n!)** — at most n choices in the first row, n − 1 in the next, and so on.
* Space: **O(n)** — the flags and current placement (plus the output).
''',
tc="exp", sc="n",
java=r'''
public class NQueens {

    public List<List<String>> solveNQueens(int n) {
        List<List<String>> out = new ArrayList<>();
        place(n, 0, new int[n], new boolean[n], new boolean[2 * n], new boolean[2 * n], out);
        return out;
    }

    private void place(int n, int r, int[] queens, boolean[] col, boolean[] d1, boolean[] d2, List<List<String>> out) {
        if (r == n) {
            List<String> board = new ArrayList<>();
            for (int q : queens) {
                char[] row = new char[n];
                Arrays.fill(row, '.');
                row[q] = 'Q';
                board.add(new String(row));
            }
            out.add(board);
            return;
        }
        for (int c = 0; c < n; c++) {
            if (col[c] || d1[r + c] || d2[r - c + n - 1]) continue;
            queens[r] = c;
            col[c] = d1[r + c] = d2[r - c + n - 1] = true;
            place(n, r + 1, queens, col, d1, d2, out);
            col[c] = d1[r + c] = d2[r - c + n - 1] = false;
        }
    }
}
''',
test=r'''
class NQueensTest {

    private final NQueens solution = new NQueens();

    @Test
    void four() {
        assertEquals(List.of(List.of(".Q..", "...Q", "Q...", "..Q."), List.of("..Q.", "Q...", "...Q", ".Q..")), solution.solveNQueens(4));
    }

    @Test
    void counts() {
        assertEquals(1, solution.solveNQueens(1).size());
        assertEquals(92, solution.solveNQueens(8).size());
    }
}
''',
trace=r'''
function run(n) {
  const qs = []; let count = 0;
  const board = () => { const g = [...Array(n)].map(() => new Array(n).fill('')); qs.forEach((c, r) => (g[r][c] = '♛')); return g; };
  (function place(r) {
    if (r === n) { count++; A.step(`Board #${count} complete.`, A.grid('board', board(), { hl: qs.map((c, rr) => [`${rr},${c}`, 'ok']) })); return; }
    for (let c = 0; c < n; c++) {
      if (qs.some((cc, rr) => cc === c || Math.abs(cc - c) === r - rr)) continue;
      qs.push(c); A.step(`Row ${r}: column ${c} is safe.`, A.grid('board', board(), { hl: qs.map((cc, rr) => [`${rr},${cc}`, rr === r ? 'cur' : 'sel']) }));
      place(r + 1); qs.pop();
    }
  })(0);
  A.step(`${count} boards for n = ${n}.`, A.text('Result', count, 'ok'));
}
A.scenario('n = 4', 'two boards', () => run(4));
'''),

P(num=131, slug="palindrome-partitioning", title="Palindrome Partitioning", diff="Medium", topic="Backtracking", cls="PalindromePartitioning",
idea="Cut off a palindromic prefix, then partition the rest the same way.",
vname="Backtracking over prefixes",
spec=r'''
Partition `s` so that every piece is a palindrome. Return all such partitions.

**Example**
```
"aab" → [["a","a","b"],["aa","b"]]
```

**Constraints**
* `1 <= s.length <= 16`; lowercase letters.
''',
approach=r'''
**Backtracking.** From `start`, try every end `e` where `s[start..e]` is a palindrome (two-pointer check), add it to the path and recurse
from `e + 1`. Reaching the end records the path.

* Time: **O(n · 2ⁿ)** — up to 2ⁿ⁻¹ ways to cut, each checked in O(n).
* Space: **O(n)** — the recursion depth.
''',
tc="exp", sc="n",
java=r'''
public class PalindromePartitioning {

    public List<List<String>> partition(String s) {
        List<List<String>> out = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), out);
        return out;
    }

    private void backtrack(String s, int start, List<String> path, List<List<String>> out) {
        if (start == s.length()) {
            out.add(new ArrayList<>(path));
            return;
        }
        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                path.add(s.substring(start, end + 1));
                backtrack(s, end + 1, path, out);
                path.removeLast();
            }
        }
    }

    private static boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--)) return false;
        }
        return true;
    }
}
''',
test=r'''
class PalindromePartitioningTest {

    private final PalindromePartitioning solution = new PalindromePartitioning();

    @Test
    void aab() {
        assertEquals(List.of(List.of("a", "a", "b"), List.of("aa", "b")), solution.partition("aab"));
    }

    @Test
    void single() {
        assertEquals(List.of(List.of("a")), solution.partition("a"));
    }
}
''',
trace=r'''
const pal = s => s === [...s].reverse().join('');
function run(s) {
  const out = [], path = [];
  (function bt(start) {
    if (start === s.length) { out.push('[' + path.join(',') + ']'); A.step(`Reached the end: record ${out[out.length - 1]}.`, A.arr('partitions', out, { hl: { [out.length - 1]: 'ok' } })); return; }
    for (let e = start; e < s.length; e++) {
      const piece = s.slice(start, e + 1), ok = pal(piece);
      A.step(`"${piece}" ${ok ? 'is a palindrome: cut it off and continue' : 'is not a palindrome: skip'}.`, A.chars('s', s, { range: [start, e], hl: Object.fromEntries([...piece].map((_, t) => [start + t, ok ? 'ok' : 'bad'])) }), A.stack('pieces', path));
      if (ok) { path.push(piece); bt(e + 1); path.pop(); }
    }
  })(0);
}
A.scenario('aab', 's = "aab"', () => run('aab'));
'''),

P(num=37, slug="sudoku-solver", title="Sudoku Solver", diff="Hard", topic="Backtracking", cls="SudokuSolver",
idea="Fill empty cells one by one with digits allowed by row, column and box masks; undo on dead ends.",
vname="Backtracking with bitmasks",
spec=r'''
Fill the empty cells (`'.'`) of a 9×9 Sudoku so that every row, column and 3×3 box contains `1-9` exactly once. The input has exactly
one solution; modify `board` in place.

**Constraints**
* `board` is 9×9; the puzzle has exactly one solution.
''',
approach=r'''
**Backtracking + bitmasks.** Keep a 9-bit mask of used digits per row, column and box. Collect the empty cells; `solve(k)` tries each
digit free in all three masks for cell `k`, recurses, and undoes on failure.

* Time: **O(9^E)** — E empty cells in the worst case (much faster in practice thanks to pruning).
* Space: **O(E)** — the recursion depth.
''',
tc="exp", sc="n",
java=r'''
public class SudokuSolver {

    private final int[] rows = new int[9], cols = new int[9], boxes = new int[9];
    private final List<int[]> empty = new ArrayList<>();

    public void solveSudoku(char[][] board) {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') empty.add(new int[]{r, c});
                else toggle(r, c, board[r][c] - '1');
            }
        }
        solve(board, 0);
    }

    private boolean solve(char[][] board, int k) {
        if (k == empty.size()) return true;
        int r = empty.get(k)[0], c = empty.get(k)[1];
        int used = rows[r] | cols[c] | boxes[(r / 3) * 3 + c / 3];
        for (int d = 0; d < 9; d++) {
            if ((used >> d & 1) == 1) continue;
            toggle(r, c, d);
            board[r][c] = (char) ('1' + d);
            if (solve(board, k + 1)) return true;
            toggle(r, c, d);
        }
        board[r][c] = '.';
        return false;
    }

    private void toggle(int r, int c, int d) {
        rows[r] ^= 1 << d;
        cols[c] ^= 1 << d;
        boxes[(r / 3) * 3 + c / 3] ^= 1 << d;
    }
}
''',
test=r'''
class SudokuSolverTest {

    @Test
    void classic() {
        String[] in = {"53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"};
        String[] out = {"534678912", "672195348", "198342567", "859761423", "426853791", "713924856", "961537284", "287419635", "345286179"};
        char[][] board = Arrays.stream(in).map(String::toCharArray).toArray(char[][]::new);
        new SudokuSolver().solveSudoku(board);
        for (int i = 0; i < 9; i++) assertEquals(out[i], new String(board[i]));
    }
}
''',
trace=r'''
function run(rows) {
  const b = rows.map(r => [...r].map(c => (c === '.' ? '' : c))), given = b.map(r => r.map(Boolean)), empty = [];
  b.forEach((r, i) => r.forEach((v, j) => !v && empty.push([i, j])));
  const ok = (r, c, d) => { for (let k = 0; k < 9; k++) if (b[r][k] === d || b[k][c] === d) return false; const br = r - r % 3, bc = c - c % 3; for (let x = 0; x < 3; x++) for (let y = 0; y < 3; y++) if (b[br + x][bc + y] === d) return false; return true; };
  let steps = 0;
  const hl = cur => b.flatMap((r, i) => r.map((v, j) => [`${i},${j}`, i === cur[0] && j === cur[1] ? 'cur' : given[i][j] ? 'dim' : v ? 'ok' : '']));
  A.step(`Grey digits are given. Fill the ${empty.length} empty cells one by one; when a cell has no legal digit, back up.`, A.grid('board', b, { hl: hl([-1, -1]) }));
  (function solve(k) {
    if (k === empty.length) return true;
    const [r, c] = empty[k];
    for (let d = 1; d <= 9; d++) { const s = String(d); if (!ok(r, c, s)) continue; b[r][c] = s; steps++; if (steps <= 12 || k === empty.length - 1) A.step(`Cell (${r},${c}): ${s} is allowed by its row, column and box.`, A.grid('board', b, { hl: hl([r, c]) })); if (solve(k + 1)) return true; b[r][c] = ''; }
    if (steps <= 12) A.step(`Cell (${r},${c}) has no legal digit left: back up.`, A.grid('board', b, { hl: hl([r, c]).concat([[`${r},${c}`, 'bad']]) }));
    return false;
  })(0);
  A.step(`Solved after ${steps} placements.`, A.grid('board', b, { hl: hl([-1, -1]) }));
}
A.scenario('Classic puzzle', 'the classic board from LeetCode', () => run(['53..7....', '6..195...', '.98....6.', '8...6...3', '4..8.3..1', '7...2...6', '.6....28.', '...419..5', '....8..79']));
'''),

P(num=10, slug="regular-expression-matching", title="Regular Expression Matching", diff="Hard", topic="Multidimensional DP", cls="RegularExpressionMatching",
idea="dp[i][j]: does s[i..] match p[j..]? A 'x*' either matches nothing or eats one matching character and stays.",
vname="Bottom-up DP",
spec=r'''
Implement full-string regular expression matching with `.` (any single character) and `*` (zero or more of the preceding element).

**Example**
```
s = "aa",  p = "a"     → false
s = "aa",  p = "a*"    → true
s = "ab",  p = ".*"    → true
s = "aab", p = "c*a*b" → true
```

**Constraints**
* `1 <= s.length <= 20`; `1 <= p.length <= 20`; every `*` follows a valid character.
''',
approach=r'''
**Suffix DP.** `dp[i][j]` is true if `s[i..]` matches `p[j..]`; `dp[m][n] = true`. With `first = i < m && (p[j] == s[i] || p[j] == '.')`:
if `p[j+1] == '*'`, `dp[i][j] = dp[i][j+2] || (first && dp[i+1][j])`; otherwise `dp[i][j] = first && dp[i+1][j+1]`.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the table.
''',
tc="n2", sc="n2",
java=r'''
public class RegularExpressionMatching {

    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[m][n] = true;
        for (int i = m; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                boolean first = i < m && (p.charAt(j) == s.charAt(i) || p.charAt(j) == '.');
                if (j + 1 < n && p.charAt(j + 1) == '*') {
                    dp[i][j] = dp[i][j + 2] || (first && dp[i + 1][j]);
                } else {
                    dp[i][j] = first && dp[i + 1][j + 1];
                }
            }
        }
        return dp[0][0];
    }
}
''',
test=r'''
class RegularExpressionMatchingTest {

    private final RegularExpressionMatching solution = new RegularExpressionMatching();

    @ParameterizedTest
    @CsvSource({"aa,a,false", "aa,a*,true", "ab,.*,true", "aab,c*a*b,true", "mississippi,mis*is*p*.,false", "ab,.*c,false"})
    void matches(String s, String p, boolean expected) {
        assertEquals(expected, solution.isMatch(s, p));
    }
}
''',
trace=r'''
function run(s, p) {
  const m = s.length, n = p.length, dp = [...Array(m + 1)].map(() => new Array(n + 1).fill(null));
  dp[m][n] = true;
  const view = (msg, hl) => A.step(msg, A.grid('dp[i][j]: s[i..] matches p[j..]', [[''].concat([...p, '∅'])].concat(dp.map((r, i) => [i < m ? s[i] : '∅'].concat(r.map(v => (v === null ? '' : v ? 'T' : 'F'))))), { hl: Object.entries(hl || {}).map(([k, c]) => { const [i, j] = k.split(',').map(Number); return [`${i + 1},${j + 1}`, c]; }) }));
  view('Fill from the bottom-right. An empty string matches an empty pattern.', { [`${m},${n}`]: 'ok' });
  for (let i = m; i >= 0; i--) { for (let j = n - 1; j >= 0; j--) { const first = i < m && (p[j] === s[i] || p[j] === '.'); if (j + 1 < n && p[j + 1] === '*') dp[i][j] = dp[i][j + 2] || (first && dp[i + 1][j]); else dp[i][j] = first && dp[i + 1][j + 1]; } const hl = {}; dp[i].forEach((v, j) => (hl[`${i},${j}`] = v ? 'ok' : 'dim')); view(`Row ${i}${i < m ? ` (suffix "${s.slice(i)}")` : ' (empty suffix)'}: a pattern piece "x*" can match nothing, or eat one matching character and stay.`, hl); }
  A.step(`dp[0][0] = ${dp[0][0]}.`, A.text('Result', String(dp[0][0]), dp[0][0] ? 'ok' : 'bad'));
}
A.scenario('Stars', 's = "aab", p = "c*a*b"', () => run('aab', 'c*a*b'));
'''),

P(num=44, slug="wildcard-matching", title="Wildcard Matching", diff="Hard", topic="Multidimensional DP", cls="WildcardMatching",
idea="Greedy with backtracking to the last '*': let the star absorb one more character whenever a mismatch occurs.",
vname="Greedy with star backtracking",
spec=r'''
Implement full-string wildcard matching where `?` matches any single character and `*` matches any sequence (including empty).

**Example**
```
s = "aa", p = "a"    → false
s = "aa", p = "*"    → true
s = "cb", p = "?a"   → false
s = "adceb", p = "*a*b" → true
```

**Constraints**
* `0 <= s.length, p.length <= 2000`
''',
approach=r'''
**Greedy.** Walk `i` in `s` and `j` in `p`. On a direct match or `?`, advance both. On `*`, remember its position and the current `i`, and
advance `j` (the star matches nothing for now). On a mismatch after a star, let the star match one more character: `i = ++mark`,
`j = star + 1`. Finally skip trailing stars.

* Time: **O(m·n)** — worst case, though usually close to linear.
* Space: **O(1)** — a few indices.
''',
tc="n2", sc="1",
java=r'''
public class WildcardMatching {

    public boolean isMatch(String s, String p) {
        int i = 0, j = 0, star = -1, mark = 0;
        while (i < s.length()) {
            if (j < p.length() && (p.charAt(j) == '?' || p.charAt(j) == s.charAt(i))) {
                i++;
                j++;
            } else if (j < p.length() && p.charAt(j) == '*') {
                star = j++;
                mark = i;
            } else if (star >= 0) {
                j = star + 1;
                i = ++mark;
            } else {
                return false;
            }
        }
        while (j < p.length() && p.charAt(j) == '*') j++;
        return j == p.length();
    }
}
''',
test=r'''
class WildcardMatchingTest {

    private final WildcardMatching solution = new WildcardMatching();

    @ParameterizedTest
    @CsvSource({"aa,a,false", "aa,*,true", "cb,?a,false", "adceb,*a*b,true", "acdcb,a*c?b,false", "'',*,true", "abc,'',false"})
    void matches(String s, String p, boolean expected) {
        assertEquals(expected, solution.isMatch(s, p));
    }
}
''',
trace=r'''
function run(s, p) {
  let i = 0, j = 0, star = -1, mark = 0;
  const view = msg => A.step(msg, A.chars('s', s, { ptr: i < s.length ? [[i, 'i']] : [] , hl: Object.fromEntries([...Array(i).keys()].map(t => [t, 'ok'])) }), A.chars('p', p, { ptr: j < p.length ? [[j, 'j']] : [], hl: star >= 0 ? { [star]: 'alt' } : {} }), A.vars({ star: star < 0 ? '-' : star, mark }));
  view('Match greedily. Remember the last star so it can absorb more characters if needed.');
  while (i < s.length) {
    if (j < p.length && (p[j] === '?' || p[j] === s[i])) { i++; j++; view('Characters match (or ?). Advance both.'); }
    else if (j < p.length && p[j] === '*') { star = j++; mark = i; view('A star: first try matching nothing. Remember this position.'); }
    else if (star >= 0) { j = star + 1; i = ++mark; view('Mismatch: let the last star absorb one more character and retry.'); }
    else { view('Mismatch with no star to fall back on.'); A.step('No match.', A.text('Result', 'false', 'bad')); return; }
  }
  while (j < p.length && p[j] === '*') j++;
  const ok = j === p.length;
  A.step(ok ? 's is used up and only stars remained in p.' : 'Pattern characters remain unmatched.', A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('Two stars', 's = "adceb", p = "*a*b"', () => run('adceb', '*a*b'));
''',
variants=[dict(
name="DP table",
idea="dp[i][j]: does s[..i) match p[..j)? A star either matches nothing (left) or one more character (up).",
approach=r'''
**Prefix DP.** `dp[0][0] = true`; leading stars match the empty string. For a star, `dp[i][j] = dp[i][j-1] || dp[i-1][j]`;
for `?` or an equal letter, `dp[i][j] = dp[i-1][j-1]`.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the table.
''',
tc="n2", sc="n2",
java=r'''
public class WildcardMatching {

    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;
        for (int j = 1; j <= n && p.charAt(j - 1) == '*'; j++) dp[0][j] = true;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                char c = p.charAt(j - 1);
                if (c == '*') dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                else dp[i][j] = (c == '?' || c == s.charAt(i - 1)) && dp[i - 1][j - 1];
            }
        }
        return dp[m][n];
    }
}
''',
trace=r'''
function run(s, p) {
  const m = s.length, n = p.length, dp = [...Array(m + 1)].map(() => new Array(n + 1).fill(false)); dp[0][0] = true;
  for (let j = 1; j <= n && p[j - 1] === '*'; j++) dp[0][j] = true;
  for (let i = 1; i <= m; i++) { for (let j = 1; j <= n; j++) { const c = p[j - 1]; dp[i][j] = c === '*' ? dp[i][j - 1] || dp[i - 1][j] : (c === '?' || c === s[i - 1]) && dp[i - 1][j - 1]; } A.step(`Row ${i} (prefix "${s.slice(0, i)}") filled.`, A.grid('dp', [[''].concat(['∅', ...p])].concat(dp.slice(0, i + 1).map((r, x) => [x ? s[x - 1] : '∅'].concat(r.map(v => (v ? 'T' : 'F'))))))); }
  A.step(`dp[m][n] = ${dp[m][n]}.`, A.text('Result', String(dp[m][n]), dp[m][n] ? 'ok' : 'bad'));
}
A.scenario('Two stars', 's = "adceb", p = "*a*b"', () => run('adceb', '*a*b'));
''')]),
]
