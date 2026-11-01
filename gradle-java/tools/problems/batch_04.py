PROBLEMS = [
P(num=3, slug="longest-substring-without-repeating-characters", title="Longest Substring Without Repeating Characters", diff="Medium", topic="Sliding Window", cls="LongestSubstring",
idea="Keep a window with no repeats; when a character repeats, jump the left edge just past its previous position.",
vname="Window with last-seen index",
spec=r'''
Given a string `s`, return the length of the longest **substring** (contiguous) that contains no repeated characters.

**Example 1**
```
Input:  s = "abcabcbb"
Output: 3   ("abc")
```

**Example 2**
```
Input:  s = "bbbbb"
Output: 1
```

**Example 3**
```
Input:  s = "pwwkew"
Output: 3   ("wke"; "pwke" is a subsequence, not a substring)
```

**Constraints**
* `0 <= s.length <= 5 * 10^4`; letters, digits, symbols and spaces.
''',
approach=r'''
**Sliding window with last positions.** Store the last index of every character. Move `right` across the string; if `s[right]`
was last seen at or after `left`, jump `left` to one past that position. The window `left..right` never contains a repeat.

* Time: **O(n)** — each character is processed once; left only jumps forward.
* Space: **O(k)** — k is the alphabet size (here a fixed array of 128 entries).
''',
java=r'''
public class LongestSubstring {

    public int lengthOfLongestSubstring(String s) {
        int[] last = new int[128];
        Arrays.fill(last, -1);
        int left = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (last[c] >= left) {
                left = last[c] + 1;
            }
            last[c] = right;
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
''',
tc="n", sc="1",
test=r'''
class LongestSubstringTest {

    private final LongestSubstring solution = new LongestSubstring();

    @ParameterizedTest
    @CsvSource(value = {"abcabcbb:3", "bbbbb:1", "pwwkew:3", "abba:2", "dvdf:3"}, delimiter = ':')
    void finds(String s, int expected) {
        assertEquals(expected, solution.lengthOfLongestSubstring(s));
    }

    @Test
    void empty() {
        assertEquals(0, solution.lengthOfLongestSubstring(""));
    }
}
''',
trace=r'''
function run(s) {
  const last = new Map();
  let left = 0, best = 0, bl = 0;
  A.step('Move the right edge one character at a time. Remember where each character was last seen.', A.chars('s', s), A.map('last seen', last), A.vars({ left, best }));
  for (let r = 0; r < s.length; r++) {
    const c = s[r];
    if (last.has(c) && last.get(c) >= left) {
      const old = left; left = last.get(c) + 1;
      A.step(`'${c}' was last seen at ${last.get(c)}, inside the window. Jump left from ${old} to ${left}.`, A.chars('s', s, { range: [old, r], ptr: [[left, 'L'], [r, 'R']], hl: { [last.get(c)]: 'bad', [r]: 'bad' } }), A.map('last seen', last), A.vars({ left, best }));
    }
    last.set(c, r);
    if (r - left + 1 > best) { best = r - left + 1; bl = left; }
    A.step(`Window "${s.slice(left, r + 1)}" has length ${r - left + 1}. Best so far: ${best}.`, A.chars('s', s, { range: [left, r], ptr: [[left, 'L'], [r, 'R']], hl: { [r]: 'cur' } }), A.map('last seen', last), A.vars({ left, best }));
  }
  A.step(`The longest substring without repeats is "${s.slice(bl, bl + best)}", length ${best}.`, A.chars('s', s, { range: [bl, bl + best - 1] }), A.text('Result', best, 'ok'));
}
A.scenario('Classic', 's = "abcabcbb"', () => run('abcabcbb'));
A.scenario('Jump left', 's = "pwwkew"', () => run('pwwkew'));
A.scenario('Edge: old repeat outside the window', 's = "abba"', () => run('abba'));
''',
variants=[dict(
name="Window with a hash set",
idea="Grow the window on the right; while the new character is already inside, shrink from the left.",
approach=r'''
**Sliding window with a set.** The set holds the window's characters. Before adding `s[right]`, remove `s[left]` and advance
`left` until `s[right]` is no longer in the set.

* Time: **O(n)** — each character is added once and removed at most once.
* Space: **O(k)** — the set holds at most k distinct characters.
''',
tc="n", sc="1",
java=r'''
public class LongestSubstring {

    public int lengthOfLongestSubstring(String s) {
        MyHashSet<Character> window = new MyHashSet<>();
        int left = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            while (window.contains(c)) {
                window.remove(s.charAt(left++));
            }
            window.add(c);
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
''',
trace=r'''
function run(s) {
  const win = new Set();
  let left = 0, best = 0;
  A.step('The set holds the characters inside the window.', A.chars('s', s), A.hashTable('window set', win), A.vars({ best }));
  for (let r = 0; r < s.length; r++) {
    while (win.has(s[r])) { A.step(`'${s[r]}' is already in the window. Remove '${s[left]}' from the left.`, A.chars('s', s, { range: [left, r - 1], hl: { [left]: 'bad', [r]: 'cur' } }), A.hashTable('window set', win)); win.delete(s[left++]); }
    win.add(s[r]); best = Math.max(best, r - left + 1);
    A.step(`Add '${s[r]}'. Window "${s.slice(left, r + 1)}", best ${best}.`, A.chars('s', s, { range: [left, r], hl: { [r]: 'ok' } }), A.hashTable('window set', win), A.vars({ best }));
  }
  A.step(`Longest length: ${best}. Characters may be removed one by one, but each only once.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', 's = "abcabcbb"', () => run('abcabcbb'));
''')]),

P(num=30, slug="substring-with-concatenation-of-all-words", title="Substring with Concatenation of All Words", diff="Hard", topic="Sliding Window", cls="SubstringConcatenation",
idea="All words share one length L, so slide a word-sized window for each of the L starting offsets, counting words in the window.",
vname="Word-step sliding window",
spec=r'''
You are given a string `s` and an array `words` of strings that all have the **same length**. A *concatenated substring* is a
substring of `s` made of every word in `words` exactly once, in any order. Return the starting indices of all concatenated
substrings in `s`, in any order.

**Example 1**
```
Input:  s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
```

**Example 2**
```
Input:  s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
```

**Example 3**
```
Input:  s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
```

**Constraints**
* `1 <= s.length <= 10^4`, `1 <= words.length <= 5000`, `1 <= words[i].length <= 30`
''',
approach=r'''
**Sliding window in word-sized steps.** Let `L` be the word length and `k` the number of words. For each offset `0..L-1`, slide
a window over `s` one word at a time, keeping a count of the words inside. If a word is not in `words`, reset the window. If a word
appears too often, drop words from the left until it doesn't. When the window holds `k` words, record its start.

* Time: **O(n·L)** — L offsets, each scanning about n / L words, and each word costs O(L) to cut out and hash.
* Space: **O(k)** — the two word-count maps.
''',
tc="n",
java=r'''
public class SubstringConcatenation {

    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> out = new ArrayList<>();
        int L = words[0].length(), k = words.length, n = s.length();
        MyHashMap<String, Integer> need = new MyHashMap<>();
        for (String w : words) need.merge(w, 1, Integer::sum);
        for (int offset = 0; offset < L; offset++) {
            MyHashMap<String, Integer> have = new MyHashMap<>();
            int left = offset, count = 0;
            for (int right = offset; right + L <= n; right += L) {
                String w = s.substring(right, right + L);
                if (!need.containsKey(w)) {
                    have.clear();
                    count = 0;
                    left = right + L;
                    continue;
                }
                have.merge(w, 1, Integer::sum);
                count++;
                while (have.get(w) > need.get(w)) {
                    have.merge(s.substring(left, left + L), -1, Integer::sum);
                    left += L;
                    count--;
                }
                if (count == k) {
                    out.add(left);
                    have.merge(s.substring(left, left + L), -1, Integer::sum);
                    left += L;
                    count--;
                }
            }
        }
        Collections.sort(out);
        return out;
    }
}
''',
test=r'''
class SubstringConcatenationTest {

    private final SubstringConcatenation solution = new SubstringConcatenation();

    @Test
    void example1() {
        assertEquals(List.of(0, 9), solution.findSubstring("barfoothefoobarman", new String[]{"foo", "bar"}));
    }

    @Test
    void duplicateWordsNoMatch() {
        assertEquals(List.of(), solution.findSubstring("wordgoodgoodgoodbestword", new String[]{"word", "good", "best", "word"}));
    }

    @Test
    void overlappingMatches() {
        assertEquals(List.of(6, 9, 12), solution.findSubstring("barfoofoobarthefoobarman", new String[]{"bar", "foo", "the"}));
    }

    @Test
    void repeatedWord() {
        assertEquals(List.of(8), solution.findSubstring("wordgoodgoodgoodbestword", new String[]{"word", "good", "best", "good"}));
    }
}
''',
trace=r'''
function run(s, words) {
  const L = words[0].length, k = words.length, need = new Map(), out = [];
  words.forEach(w => need.set(w, (need.get(w) || 0) + 1));
  A.step(`Every word has length ${L}, so we scan s in chunks of ${L}, once for each of the ${L} possible offsets.`, A.chars('s', s), A.hashTable('need', need));
  for (let off = 0; off < L; off++) {
    const have = new Map(); let left = off, count = 0;
    for (let r = off; r + L <= s.length; r += L) {
      const w = s.slice(r, r + L);
      const chunk = []; for (let t = r; t < r + L; t++) chunk.push([t, 'cur']);
      if (!need.has(w)) { A.step(`Offset ${off}: "${w}" is not a word, so reset the window past it.`, A.chars('s', s, { hl: chunk.map(([t]) => [t, 'bad']) }), A.hashTable('have', have)); have.clear(); count = 0; left = r + L; continue; }
      have.set(w, (have.get(w) || 0) + 1); count++;
      while (have.get(w) > need.get(w)) { const d = s.slice(left, left + L); have.set(d, have.get(d) - 1); left += L; count--; }
      A.step(`Offset ${off}: add "${w}". The window holds ${count} of ${k} words.`, A.chars('s', s, { range: [left, r + L - 1], hl: chunk }), A.hashTable('have', have), A.arr('found', out));
      if (count === k) {
        out.push(left);
        A.step(`All ${k} words are present, so record start ${left}. Then slide past the first word.`, A.chars('s', s, { range: [left, r + L - 1], hl: [...Array(k * L).keys()].map(t => [left + t, 'ok']) }), A.arr('found', out, { hl: { [out.length - 1]: 'ok' } }));
        const d = s.slice(left, left + L); have.set(d, have.get(d) - 1); left += L; count--;
      }
    }
  }
  out.sort((a, b) => a - b);
  A.step(`Starting indices: [${out}].`, A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Two words', 's = "barfoothefoobarman", words = ["foo","bar"]', () => run('barfoothefoobarman', ['foo', 'bar']));
A.scenario('Overlapping matches', 's = "barfoofoobarthe", words = ["bar","foo","the"]', () => run('barfoofoobarthe', ['bar', 'foo', 'the']));
''',
variants=[dict(
name="Check every start",
idea="For each start index, cut k words and compare their counts with the required counts.",
approach=r'''
**Brute force.** For each start `i` with room for `k` words, read the `k` consecutive chunks of length `L` and count them;
stop early when a chunk is not needed or is seen too often.

* Time: **O(n·k·L)** — n starts × k words × L characters to cut each word.
* Space: **O(k)** — the per-start count map.
''',
tc="n2",
java=r'''
public class SubstringConcatenation {

    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> out = new ArrayList<>();
        int L = words[0].length(), k = words.length;
        MyHashMap<String, Integer> need = new MyHashMap<>();
        for (String w : words) need.merge(w, 1, Integer::sum);
        for (int i = 0; i + k * L <= s.length(); i++) {
            MyHashMap<String, Integer> seen = new MyHashMap<>();
            int j = 0;
            for (; j < k; j++) {
                String w = s.substring(i + j * L, i + (j + 1) * L);
                if (seen.merge(w, 1, Integer::sum) > need.getOrDefault(w, 0)) break;
            }
            if (j == k) out.add(i);
        }
        return out;
    }
}
''',
trace=r'''
function run(s, words) {
  const L = words[0].length, k = words.length, need = new Map(), out = [];
  words.forEach(w => need.set(w, (need.get(w) || 0) + 1));
  for (let i = 0; i + k * L <= s.length; i++) {
    const seen = new Map(); let j = 0;
    for (; j < k; j++) { const w = s.slice(i + j * L, i + (j + 1) * L); seen.set(w, (seen.get(w) || 0) + 1); if (seen.get(w) > (need.get(w) || 0)) break; }
    const ok = j === k; if (ok) out.push(i);
    A.step(ok ? `Start ${i}: all ${k} words match.` : `Start ${i}: fails at word ${j + 1}.`, A.chars('s', s, { range: [i, i + k * L - 1], hl: ok ? [...Array(k * L).keys()].map(t => [i + t, 'ok']) : [[i + j * L, 'bad']] }), A.arr('found', out));
  }
  A.step(`Every start was checked from scratch. Starting indices: [${out}].`, A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Two words', 's = "barfoothefoobarman", words = ["foo","bar"]', () => run('barfoothefoobarman', ['foo', 'bar']));
''')]),

P(num=76, slug="minimum-window-substring", title="Minimum Window Substring", diff="Hard", topic="Sliding Window", cls="MinimumWindowSubstring",
idea="Expand right until the window covers t, then shrink left as far as it stays covering; remember the smallest.",
vname="Sliding window with counts",
spec=r'''
Given strings `s` and `t`, return the **shortest substring** of `s` that contains every character of `t` (including duplicates).
Return `""` if there is none. The answer is unique when it exists.

**Example 1**
```
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Example 2**
```
Input:  s = "a", t = "a"
Output: "a"
```

**Example 3**
```
Input:  s = "a", t = "aa"
Output: ""
```

**Constraints**
* `1 <= s.length, t.length <= 10^5`; upper- and lower-case letters.
''',
approach=r'''
**Sliding window.** `need[c]` counts what `t` still needs; `missing` is how many characters are still missing.
Move `right`: if `need[s[right]] > 0`, it fills a gap (`missing--`); decrement `need` either way. When `missing == 0`, shrink from
the left while `need[s[left]] < 0` (that character is in surplus), record the window, then give up `s[left]` to keep searching.

* Time: **O(m + n)** — each pointer passes over s once, plus one pass over t.
* Space: **O(1)** — a fixed 128-entry count array.
''',
tc="n", sc="1",
java=r'''
public class MinimumWindowSubstring {

    public String minWindow(String s, String t) {
        int[] need = new int[128];
        for (char c : t.toCharArray()) need[c]++;
        int missing = t.length(), left = 0, bestStart = 0, bestLen = Integer.MAX_VALUE;
        for (int right = 0; right < s.length(); right++) {
            if (need[s.charAt(right)]-- > 0) missing--;
            while (missing == 0) {
                if (right - left + 1 < bestLen) {
                    bestLen = right - left + 1;
                    bestStart = left;
                }
                if (++need[s.charAt(left++)] > 0) missing++;
            }
        }
        return bestLen == Integer.MAX_VALUE ? "" : s.substring(bestStart, bestStart + bestLen);
    }
}
''',
test=r'''
class MinimumWindowSubstringTest {

    private final MinimumWindowSubstring solution = new MinimumWindowSubstring();

    @ParameterizedTest
    @CsvSource(value = {"ADOBECODEBANC:ABC:BANC", "a:a:a", "a:aa:''", "ab:b:b", "aaflslflsldkalskaaa:aaa:aaa"}, delimiter = ':')
    void finds(String s, String t, String expected) {
        assertEquals(expected, solution.minWindow(s, t));
    }
}
''',
trace=r'''
function run(s, t) {
  const need = new Map(); for (const c of t) need.set(c, (need.get(c) || 0) + 1);
  let missing = t.length, left = 0, bs = 0, bl = Infinity;
  const needView = () => new Map([...need].filter(([c]) => t.includes(c)));
  A.step(`We need the characters of "${t}". Expand right until nothing is missing, then shrink left.`, A.chars('s', s), A.map('still needed', needView()), A.vars({ missing }));
  for (let r = 0; r < s.length; r++) {
    const c = s[r], useful = (need.get(c) || 0) > 0;
    need.set(c, (need.get(c) || 0) - 1); if (useful) missing--;
    A.step(useful ? `'${c}' fills a gap. ${missing} character${missing === 1 ? '' : 's'} still missing.` : `'${c}' is not needed right now.`, A.chars('s', s, { range: [left, r], hl: { [r]: useful ? 'ok' : 'cur' } }), A.map('still needed', needView()), A.vars({ missing, best: bl === Infinity ? '-' : s.substr(bs, bl) }));
    while (missing === 0) {
      if (r - left + 1 < bl) { bl = r - left + 1; bs = left; A.step(`The window "${s.slice(left, r + 1)}" covers t. It is the smallest so far.`, A.chars('s', s, { range: [left, r], hl: [...Array(r - left + 1).keys()].map(x => [left + x, 'sel']) }), A.vars({ missing, best: s.substr(bs, bl) })); }
      const d = s[left]; need.set(d, need.get(d) + 1);
      if (need.get(d) > 0) { missing++; A.step(`Removing '${d}' from the left breaks the cover. Go back to expanding.`, A.chars('s', s, { range: [left, r], hl: { [left]: 'bad' } }), A.map('still needed', needView()), A.vars({ missing })); }
      left++;
    }
  }
  const res = bl === Infinity ? '' : s.substr(bs, bl);
  A.step(res ? `The minimum window is "${res}".` : 'No window covers t, so the answer is "".', A.chars('s', s, res ? { range: [bs, bs + bl - 1] } : {}), A.text('Result', `"${res}"`, res ? 'ok' : 'bad'));
}
A.scenario('Classic', 's = "ADOBECODEBANC", t = "ABC"', () => run('ADOBECODEBANC', 'ABC'));
A.scenario('Edge: impossible', 's = "ab", t = "aa"', () => run('ab', 'aa'));
'''),

P(num=36, slug="valid-sudoku", title="Valid Sudoku", diff="Medium", topic="Matrix", cls="ValidSudoku",
idea="One pass over the cells, remembering each digit per row, per column and per 3×3 box.",
vname="Seen sets in one pass",
spec=r'''
Decide whether a partially filled 9×9 Sudoku board is **valid**. Only the filled cells need to follow the rules:
* each row has the digits `1-9` at most once,
* each column has the digits `1-9` at most once,
* each of the nine 3×3 boxes has the digits `1-9` at most once.

Empty cells are `'.'`. A valid board does not need to be solvable.

**Example**
```
Input: the classic example board (rows "53..7....", "6..195...", ...)
Output: true
Changing the top-left 5 to 8 makes column 0 contain 8 twice → false
```

**Constraints**
* `board` is 9×9; each cell is a digit `1-9` or `'.'`.
''',
approach=r'''
**Boolean tables.** Keep `rows[9][9]`, `cols[9][9]` and `boxes[9][9]`. For each digit `d` at `(r, c)`, the box index is
`(r / 3) * 3 + c / 3`. If any of the three tables already marks `d`, the board is invalid; otherwise mark it.

* Time: **O(1)** — the board is always 81 cells.
* Space: **O(1)** — three fixed 9×9 tables.
''',
java=r'''
public class ValidSudoku {

    public boolean isValidSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][9], cols = new boolean[9][9], boxes = new boolean[9][9];
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char ch = board[r][c];
                if (ch == '.') continue;
                int d = ch - '1', b = (r / 3) * 3 + c / 3;
                if (rows[r][d] || cols[c][d] || boxes[b][d]) return false;
                rows[r][d] = cols[c][d] = boxes[b][d] = true;
            }
        }
        return true;
    }
}
''',
test=r'''
class ValidSudokuTest {

    private final ValidSudoku solution = new ValidSudoku();

    private static char[][] board(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    private static final String[] VALID = {
        "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
        "7...2...6", ".6....28.", "...419..5", "....8..79"};

    @Test
    void validBoard() {
        assertTrue(solution.isValidSudoku(board(VALID)));
    }

    @Test
    void duplicateInColumn() {
        String[] rows = VALID.clone();
        rows[0] = "83..7....";
        assertFalse(solution.isValidSudoku(board(rows)));
    }

    @Test
    void duplicateInBox() {
        String[] rows = VALID.clone();
        rows[1] = "6.5195...";
        assertFalse(solution.isValidSudoku(board(rows)));
    }
}
''',
trace=r'''
function run(rowsStr, title) {
  const g = rowsStr.map(r => [...r].map(c => (c === '.' ? '' : c)));
  const R = Array.from({ length: 9 }, () => new Set()), C = Array.from({ length: 9 }, () => new Set()), B = Array.from({ length: 9 }, () => new Set());
  const hl = [];
  A.step('Visit every filled cell once. Each digit must be new in its row, its column and its 3×3 box.', A.grid('board', g));
  for (let r = 0; r < 9; r++) for (let c = 0; c < 9; c++) {
    const d = g[r][c]; if (!d) continue;
    const b = Math.floor(r / 3) * 3 + Math.floor(c / 3);
    const where = R[r].has(d) ? 'row ' + r : C[c].has(d) ? 'column ' + c : B[b].has(d) ? 'box ' + b : '';
    if (where) {
      const clash = [];
      for (let x = 0; x < 9; x++) for (let y = 0; y < 9; y++) if (g[x][y] === d && ((where.startsWith('row') && x === r) || (where.startsWith('col') && y === c) || (where.startsWith('box') && Math.floor(x / 3) * 3 + Math.floor(y / 3) === b))) clash.push([`${x},${y}`, 'bad']);
      A.step(`Digit ${d} at (${r}, ${c}) already appears in ${where}. The board is invalid.`, A.grid('board', g, { hl: hl.concat(clash) }), A.text('Result', 'false', 'bad'));
      return;
    }
    R[r].add(d); C[c].add(d); B[b].add(d); hl.push([`${r},${c}`, 'ok']);
    if (hl.length % 6 === 1 || hl.length < 4) A.step(`Digit ${d} at (${r}, ${c}) is new in row ${r}, column ${c} and box ${b}.`, A.grid('board', g, { hl: hl.slice(0, -1).concat([[`${r},${c}`, 'cur']]) }), A.vars({ checked: hl.length }));
  }
  A.step('Every digit was unique in its row, column and box. The board is valid.', A.grid('board', g, { hl }), A.text('Result', 'true', 'ok'));
}
const VALID = ['53..7....', '6..195...', '.98....6.', '8...6...3', '4..8.3..1', '7...2...6', '.6....28.', '...419..5', '....8..79'];
A.scenario('Valid board', 'the classic example', () => run(VALID));
A.scenario('Duplicate in a box', 'row 1 = "6.5195..."', () => run(['53..7....', '6.5195...'].concat(VALID.slice(2))));
'''),

P(num=54, slug="spiral-matrix", title="Spiral Matrix", diff="Medium", topic="Matrix", cls="SpiralMatrix",
idea="Peel the matrix layer by layer: walk the top row, right column, bottom row and left column, shrinking the bounds.",
vname="Shrinking boundaries",
spec=r'''
Given an `m × n` matrix, return all of its elements in **spiral order** (clockwise, starting at the top-left).

**Example 1**
```
Input:  [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2**
```
Input:  [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

**Constraints**
* `1 <= m, n <= 10`, `-100 <= matrix[i][j] <= 100`
''',
approach=r'''
**Four boundaries.** Keep `top`, `bottom`, `left`, `right`. Walk the top row left→right (`top++`), the right column top→bottom
(`right--`), then, if rows remain, the bottom row right→left (`bottom--`), and if columns remain, the left column bottom→top
(`left++`). Repeat until the bounds cross.

* Time: **O(m·n)** — every cell is visited once.
* Space: **O(1)** — four bounds, apart from the output list.
''',
tc="n",
java=r'''
public class SpiralMatrix {

    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> out = new ArrayList<>();
        int top = 0, bottom = matrix.length - 1, left = 0, right = matrix[0].length - 1;
        while (top <= bottom && left <= right) {
            for (int c = left; c <= right; c++) out.add(matrix[top][c]);
            top++;
            for (int r = top; r <= bottom; r++) out.add(matrix[r][right]);
            right--;
            if (top <= bottom) {
                for (int c = right; c >= left; c--) out.add(matrix[bottom][c]);
                bottom--;
            }
            if (left <= right) {
                for (int r = bottom; r >= top; r--) out.add(matrix[r][left]);
                left++;
            }
        }
        return out;
    }
}
''',
test=r'''
class SpiralMatrixTest {

    private final SpiralMatrix solution = new SpiralMatrix();

    @Test
    void square() {
        assertEquals(List.of(1, 2, 3, 6, 9, 8, 7, 4, 5), solution.spiralOrder(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}));
    }

    @Test
    void wide() {
        assertEquals(List.of(1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7),
                solution.spiralOrder(new int[][]{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}));
    }

    @Test
    void singleColumn() {
        assertEquals(List.of(1, 2, 3), solution.spiralOrder(new int[][]{{1}, {2}, {3}}));
    }
}
''',
trace=r'''
function run(m) {
  let top = 0, bottom = m.length - 1, left = 0, right = m[0].length - 1;
  const out = [], seen = [];
  const visit = (r, c, dir) => { out.push(m[r][c]); seen.push([`${r},${c}`, 'ok']); A.step(`Walk ${dir}: take ${m[r][c]}.`, A.grid('matrix', m, { hl: seen.slice(0, -1).concat([[`${r},${c}`, 'cur']]) }), A.arr('output', out, { hl: { [out.length - 1]: 'ok' } }), A.vars({ top, bottom, left, right })); };
  A.step('Walk around the outer layer clockwise, then shrink the bounds and repeat.', A.grid('matrix', m), A.vars({ top, bottom, left, right }));
  while (top <= bottom && left <= right) {
    for (let c = left; c <= right; c++) visit(top, c, 'right along the top row');
    top++;
    for (let r = top; r <= bottom; r++) visit(r, right, 'down the right column');
    right--;
    if (top <= bottom) { for (let c = right; c >= left; c--) visit(bottom, c, 'left along the bottom row'); bottom--; }
    if (left <= right) { for (let r = bottom; r >= top; r--) visit(r, left, 'up the left column'); left++; }
  }
  A.step('The bounds crossed, so every cell has been visited.', A.grid('matrix', m, { hl: seen }), A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('3 × 3', 'matrix = [[1,2,3],[4,5,6],[7,8,9]]', () => run([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
A.scenario('3 × 4', 'matrix = [[1..4],[5..8],[9..12]]', () => run([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]));
'''),

P(num=48, slug="rotate-image", title="Rotate Image", diff="Medium", topic="Matrix", cls="RotateImage",
idea="A clockwise rotation equals a transpose followed by reversing every row.",
vname="Transpose + reverse rows",
spec=r'''
Rotate an `n × n` matrix by 90 degrees **clockwise**, **in place** (do not allocate another matrix).

**Example 1**
```
Input:  [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Example 2**
```
Input:  [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

**Constraints**
* `1 <= n <= 20`, `-1000 <= matrix[i][j] <= 1000`
''',
approach=r'''
**Transpose, then mirror.** Swap `a[i][j]` with `a[j][i]` for `j > i` (transpose), then reverse each row.
Element `(i, j)` ends at `(j, n-1-i)`, which is exactly the clockwise rotation.

* Time: **O(n²)** — every cell is swapped a constant number of times.
* Space: **O(1)** — swaps in place.
''',
tc="n2",
java=r'''
public class RotateImage {

    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int t = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = t;
            }
        }
        for (int[] row : matrix) {
            for (int l = 0, r = n - 1; l < r; l++, r--) {
                int t = row[l];
                row[l] = row[r];
                row[r] = t;
            }
        }
    }
}
''',
test=r'''
class RotateImageTest {

    private final RotateImage solution = new RotateImage();

    @Test
    void threeByThree() {
        int[][] m = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        solution.rotate(m);
        assertArrayEquals(new int[][]{{7, 4, 1}, {8, 5, 2}, {9, 6, 3}}, m);
    }

    @Test
    void fourByFour() {
        int[][] m = {{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}};
        solution.rotate(m);
        assertArrayEquals(new int[][]{{15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11}}, m);
    }

    @Test
    void single() {
        int[][] m = {{1}};
        solution.rotate(m);
        assertArrayEquals(new int[][]{{1}}, m);
    }
}
''',
trace=r'''
function run(m) {
  const n = m.length;
  A.step('Step 1: transpose. Swap each cell above the diagonal with its mirror below it.', A.grid('matrix', m, { hl: m.flatMap((r, i) => r.map((_, j) => [`${i},${j}`, i === j ? 'alt' : ''])) }));
  for (let i = 0; i < n; i++) for (let j = i + 1; j < n; j++) {
    [m[i][j], m[j][i]] = [m[j][i], m[i][j]];
    A.step(`Swap (${i},${j}) with (${j},${i}).`, A.grid('matrix', m, { hl: { [`${i},${j}`]: 'cur', [`${j},${i}`]: 'cur' } }));
  }
  A.step('The matrix is transposed: rows have become columns. Step 2: reverse every row.', A.grid('matrix', m));
  m.forEach((row, i) => { row.reverse(); A.step(`Reverse row ${i}.`, A.grid('matrix', m, { hl: row.map((_, j) => [`${i},${j}`, 'ok']) })); });
  A.step('The matrix is rotated 90° clockwise, using no extra matrix.', A.grid('matrix', m, { hl: m.flatMap((r, i) => r.map((_, j) => [`${i},${j}`, 'ok'])) }));
}
A.scenario('3 × 3', 'matrix = [[1,2,3],[4,5,6],[7,8,9]]', () => run([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
A.scenario('4 × 4', 'the second example', () => run([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]));
''',
variants=[dict(
name="Copy into a new matrix",
idea="Cell (i, j) moves to (j, n−1−i); fill a copy, then copy it back.",
approach=r'''
**Extra matrix.** Write `rotated[j][n-1-i] = matrix[i][j]` for every cell, then copy `rotated` back row by row.
Easy to reason about, but it breaks the in-place requirement.

* Time: **O(n²)** — each cell is copied twice.
* Space: **O(n²)** — the second matrix.
''',
tc="n2", sc="n2",
java=r'''
public class RotateImage {

    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int[][] rotated = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rotated[j][n - 1 - i] = matrix[i][j];
            }
        }
        for (int i = 0; i < n; i++) {
            matrix[i] = rotated[i].clone();
        }
    }
}
''',
trace=r'''
function run(m) {
  const n = m.length, out = Array.from({ length: n }, () => new Array(n).fill(''));
  A.step('Cell (i, j) moves to (j, n − 1 − i). Fill a new matrix.', A.grid('matrix', m), A.grid('rotated', out));
  for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) { out[j][n - 1 - i] = m[i][j]; A.step(`(${i},${j}) = ${m[i][j]} goes to (${j},${n - 1 - i}).`, A.grid('matrix', m, { hl: { [`${i},${j}`]: 'cur' } }), A.grid('rotated', out, { hl: { [`${j},${n - 1 - i}`]: 'ok' } })); }
  A.step('Copy it back. This needs a second n × n matrix.', A.grid('matrix', out, { hl: out.flatMap((r, i) => r.map((_, j) => [`${i},${j}`, 'ok'])) }));
}
A.scenario('3 × 3', 'matrix = [[1,2,3],[4,5,6],[7,8,9]]', () => run([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
''')]),

P(num=73, slug="set-matrix-zeroes", title="Set Matrix Zeroes", diff="Medium", topic="Matrix", cls="SetMatrixZeroes",
idea="Use the first row and first column as the zero markers, with two flags for the first row and column themselves.",
vname="Markers in row/column 0",
spec=r'''
Given an `m × n` integer matrix, if a cell is `0`, set its entire row and column to `0`. Do it **in place**.

**Example 1**
```
Input:  [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2**
```
Input:  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

**Constraints**
* `1 <= m, n <= 200`, `-2^31 <= matrix[i][j] <= 2^31 - 1`

**Follow-up:** a constant-space solution.
''',
approach=r'''
**Reuse the first row and column.** First remember whether row 0 and column 0 contain a zero. Then, for every zero at `(i, j)`
with `i, j >= 1`, mark `matrix[i][0] = 0` and `matrix[0][j] = 0`. Zero every inner cell whose row or column is marked. Finally
zero row 0 and column 0 if their flags are set.

* Time: **O(m·n)** — a few passes over the matrix.
* Space: **O(1)** — two boolean flags.
''',
tc="n2",
java=r'''
public class SetMatrixZeroes {

    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean firstRow = false, firstCol = false;
        for (int j = 0; j < n; j++) if (matrix[0][j] == 0) firstRow = true;
        for (int i = 0; i < m; i++) if (matrix[i][0] == 0) firstCol = true;
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) matrix[i][j] = 0;
            }
        }
        if (firstRow) Arrays.fill(matrix[0], 0);
        if (firstCol) for (int i = 0; i < m; i++) matrix[i][0] = 0;
    }
}
''',
test=r'''
class SetMatrixZeroesTest {

    private final SetMatrixZeroes solution = new SetMatrixZeroes();

    @Test
    void centreZero() {
        int[][] m = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
        solution.setZeroes(m);
        assertArrayEquals(new int[][]{{1, 0, 1}, {0, 0, 0}, {1, 0, 1}}, m);
    }

    @Test
    void zerosInFirstRow() {
        int[][] m = {{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}};
        solution.setZeroes(m);
        assertArrayEquals(new int[][]{{0, 0, 0, 0}, {0, 4, 5, 0}, {0, 3, 1, 0}}, m);
    }

    @Test
    void zeroInFirstColumnOnly() {
        int[][] m = {{1, 2}, {0, 3}};
        solution.setZeroes(m);
        assertArrayEquals(new int[][]{{0, 2}, {0, 0}}, m);
    }
}
''',
trace=r'''
function run(m) {
  const R = m.length, C = m[0].length;
  const fr = m[0].includes(0), fc = m.some(r => r[0] === 0);
  const marks = () => [...Array(C).keys()].map(j => [`0,${j}`, 'alt']).concat([...Array(R).keys()].map(i => [`${i},0`, 'alt']));
  A.step(`Row 0 and column 0 (purple) will store the markers. First note whether they hold a zero themselves: row 0 ${fr ? 'does' : 'does not'}, column 0 ${fc ? 'does' : 'does not'}.`, A.grid('matrix', m, { hl: marks() }), A.vars({ firstRowHasZero: fr, firstColHasZero: fc }));
  for (let i = 1; i < R; i++) for (let j = 1; j < C; j++) if (m[i][j] === 0) {
    m[i][0] = 0; m[0][j] = 0;
    A.step(`Zero at (${i},${j}): mark row ${i} in column 0 and column ${j} in row 0.`, A.grid('matrix', m, { hl: marks().concat([[`${i},${j}`, 'bad'], [`${i},0`, 'cur'], [`0,${j}`, 'cur']]) }));
  }
  const z = [];
  for (let i = 1; i < R; i++) for (let j = 1; j < C; j++) if ((m[i][0] === 0 || m[0][j] === 0) && m[i][j] !== 0) { m[i][j] = 0; z.push([`${i},${j}`, 'bad']); }
  A.step('Zero every inner cell whose row or column is marked.', A.grid('matrix', m, { hl: marks().concat(z) }));
  if (fr) { m[0].fill(0); A.step('Row 0 had a zero originally, so zero all of row 0.', A.grid('matrix', m, { hl: m[0].map((_, j) => [`0,${j}`, 'bad']) })); }
  if (fc) { m.forEach(r => (r[0] = 0)); A.step('Column 0 had a zero originally, so zero all of column 0.', A.grid('matrix', m, { hl: m.map((_, i) => [`${i},0`, 'bad']) })); }
  A.step('Done, using only two extra flags.', A.grid('matrix', m), A.text('Result', JSON.stringify(m), 'ok'));
}
A.scenario('Centre zero', 'matrix = [[1,1,1],[1,0,1],[1,1,1]]', () => run([[1, 1, 1], [1, 0, 1], [1, 1, 1]]));
A.scenario('Zeros in row 0', 'matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]', () => run([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]));
''',
variants=[dict(
name="Row and column sets",
idea="Record which rows and columns contain a zero, then zero them in a second pass.",
approach=r'''
**Two boolean arrays.** `zeroRow[i]` and `zeroCol[j]` are set for every zero. A second pass zeroes a cell if its row or column is flagged.

* Time: **O(m·n)** — two passes.
* Space: **O(m + n)** — the two flag arrays.
''',
tc="n2", sc="n",
java=r'''
public class SetMatrixZeroes {

    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean[] zeroRow = new boolean[m], zeroCol = new boolean[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    zeroRow[i] = true;
                    zeroCol[j] = true;
                }
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (zeroRow[i] || zeroCol[j]) matrix[i][j] = 0;
            }
        }
    }
}
''',
trace=r'''
function run(m) {
  const R = m.length, C = m[0].length, zr = new Array(R).fill(false), zc = new Array(C).fill(false);
  for (let i = 0; i < R; i++) for (let j = 0; j < C; j++) if (m[i][j] === 0) { zr[i] = zc[j] = true; A.step(`Zero at (${i},${j}): flag row ${i} and column ${j}.`, A.grid('matrix', m, { hl: { [`${i},${j}`]: 'bad' } }), A.arr('zeroRow', zr.map(Number)), A.arr('zeroCol', zc.map(Number))); }
  const z = [];
  for (let i = 0; i < R; i++) for (let j = 0; j < C; j++) if (zr[i] || zc[j]) { m[i][j] = 0; z.push([`${i},${j}`, 'bad']); }
  A.step('Second pass: zero every cell in a flagged row or column. The flags take O(m + n) space.', A.grid('matrix', m, { hl: z }), A.arr('zeroRow', zr.map(Number)), A.arr('zeroCol', zc.map(Number)));
}
A.scenario('Centre zero', 'matrix = [[1,1,1],[1,0,1],[1,1,1]]', () => run([[1, 1, 1], [1, 0, 1], [1, 1, 1]]));
''')]),

P(num=289, slug="game-of-life", title="Game of Life", diff="Medium", topic="Matrix", cls="GameOfLife",
idea="Update in place by encoding both the old and new state in each cell (bit 0 = now, bit 1 = next).",
vname="In-place two-bit states",
spec=r'''
The board is an `m × n` grid of cells, each live (`1`) or dead (`0`). Each cell looks at its 8 neighbours and, **all at the
same time**:
1. a live cell with fewer than 2 live neighbours dies;
2. a live cell with 2 or 3 live neighbours lives on;
3. a live cell with more than 3 live neighbours dies;
4. a dead cell with exactly 3 live neighbours becomes live.

Update `board` in place to the next state.

**Example**
```
Input:  [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
```

**Constraints**
* `1 <= m, n <= 25`

**Follow-up:** solve it in place.
''',
approach=r'''
**Two bits per cell.** Bit 0 is the current state, bit 1 the next state. Count live neighbours using `cell & 1`, so cells
already updated still report their old state. Set bit 1 when the cell lives next round. Finally shift every cell right by one.

* Time: **O(m·n)** — 8 neighbour checks per cell.
* Space: **O(1)** — the board stores both generations.
''',
tc="n2",
java=r'''
public class GameOfLife {

    public void gameOfLife(int[][] board) {
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int live = 0;
                for (int di = -1; di <= 1; di++) {
                    for (int dj = -1; dj <= 1; dj++) {
                        if ((di != 0 || dj != 0) && i + di >= 0 && i + di < m && j + dj >= 0 && j + dj < n) {
                            live += board[i + di][j + dj] & 1;
                        }
                    }
                }
                if (live == 3 || (live == 2 && (board[i][j] & 1) == 1)) {
                    board[i][j] |= 2;
                }
            }
        }
        for (int[] row : board) {
            for (int j = 0; j < n; j++) row[j] >>= 1;
        }
    }
}
''',
test=r'''
class GameOfLifeTest {

    private final GameOfLife solution = new GameOfLife();

    @Test
    void glider() {
        int[][] b = {{0, 1, 0}, {0, 0, 1}, {1, 1, 1}, {0, 0, 0}};
        solution.gameOfLife(b);
        assertArrayEquals(new int[][]{{0, 0, 0}, {1, 0, 1}, {0, 1, 1}, {0, 1, 0}}, b);
    }

    @Test
    void block() {
        int[][] b = {{1, 1}, {1, 0}};
        solution.gameOfLife(b);
        assertArrayEquals(new int[][]{{1, 1}, {1, 1}}, b);
    }

    @Test
    void blinker() {
        int[][] b = {{0, 0, 0}, {1, 1, 1}, {0, 0, 0}};
        solution.gameOfLife(b);
        assertArrayEquals(new int[][]{{0, 1, 0}, {0, 1, 0}, {0, 1, 0}}, b);
    }
}
''',
trace=r'''
function run(b) {
  const m = b.length, n = b[0].length;
  const view = (i, j) => A.grid('board (bit1 = next, bit0 = now)', b.map(r => r.map(v => ['0', '1', '2', '3'][v])), { hl: b.flatMap((r, x) => r.map((v, y) => [`${x},${y}`, x === i && y === j ? 'cur' : v & 1 ? 'ok' : v & 2 ? 'sel' : ''])) });
  A.step('Green cells are alive. Each cell stores two bits: bit 0 is now, bit 1 is the next state. Neighbours are counted with bit 0 only.', view(-1, -1));
  for (let i = 0; i < m; i++) for (let j = 0; j < n; j++) {
    let live = 0;
    for (let di = -1; di <= 1; di++) for (let dj = -1; dj <= 1; dj++) if ((di || dj) && b[i + di] && b[i + di][j + dj] !== undefined) live += b[i + di][j + dj] & 1;
    const alive = b[i][j] & 1, next = live === 3 || (live === 2 && alive);
    if (next) b[i][j] |= 2;
    A.step(`(${i},${j}) is ${alive ? 'alive' : 'dead'} with ${live} live neighbour${live === 1 ? '' : 's'}, so next round it is ${next ? 'alive' : 'dead'}${next ? '. Set bit 1' : ''}.`, view(i, j));
  }
  b.forEach(r => r.forEach((v, j) => (r[j] = v >> 1)));
  A.step('Shift every cell right by one bit: the next state becomes the current state.', A.grid('board', b, { hl: b.flatMap((r, x) => r.map((v, y) => [`${x},${y}`, v ? 'ok' : ''])) }));
}
A.scenario('Blinker', 'board = [[0,0,0],[1,1,1],[0,0,0]]', () => run([[0, 0, 0], [1, 1, 1], [0, 0, 0]]));
A.scenario('Glider', 'board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]', () => run([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]));
''',
variants=[dict(
name="Copy of the board",
idea="Read neighbours from an untouched copy and write the new states into the board.",
approach=r'''
**Snapshot.** Copy the board; count neighbours in the copy and write each cell's next state into the original.

* Time: **O(m·n)** — 8 neighbour checks per cell.
* Space: **O(m·n)** — the copy.
''',
tc="n2", sc="n2",
java=r'''
public class GameOfLife {

    public void gameOfLife(int[][] board) {
        int m = board.length, n = board[0].length;
        int[][] old = new int[m][];
        for (int i = 0; i < m; i++) old[i] = board[i].clone();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int live = 0;
                for (int di = -1; di <= 1; di++) {
                    for (int dj = -1; dj <= 1; dj++) {
                        if ((di != 0 || dj != 0) && i + di >= 0 && i + di < m && j + dj >= 0 && j + dj < n) {
                            live += old[i + di][j + dj];
                        }
                    }
                }
                board[i][j] = (live == 3 || (live == 2 && old[i][j] == 1)) ? 1 : 0;
            }
        }
    }
}
''',
trace=r'''
function run(b) {
  const old = b.map(r => r.slice()), m = b.length, n = b[0].length;
  const g = (x, i, j) => x.flatMap((r, a) => r.map((v, c) => [`${a},${c}`, a === i && c === j ? 'cur' : v ? 'ok' : '']));
  A.step('Keep a snapshot of the current generation; write the next generation into the board.', A.grid('snapshot', old, { hl: g(old, -1, -1) }), A.grid('board', b, { hl: g(b, -1, -1) }));
  for (let i = 0; i < m; i++) for (let j = 0; j < n; j++) {
    let live = 0;
    for (let di = -1; di <= 1; di++) for (let dj = -1; dj <= 1; dj++) if ((di || dj) && old[i + di] && old[i + di][j + dj] !== undefined) live += old[i + di][j + dj];
    b[i][j] = live === 3 || (live === 2 && old[i][j]) ? 1 : 0;
    A.step(`(${i},${j}) has ${live} live neighbours in the snapshot, so it becomes ${b[i][j] ? 'alive' : 'dead'}.`, A.grid('snapshot', old, { hl: g(old, i, j) }), A.grid('board', b, { hl: g(b, i, j) }));
  }
  A.step('Done. The snapshot cost O(m·n) extra space.', A.grid('board', b, { hl: g(b, -1, -1) }));
}
A.scenario('Blinker', 'board = [[0,0,0],[1,1,1],[0,0,0]]', () => run([[0, 0, 0], [1, 1, 1], [0, 0, 0]]));
''')]),

P(num=383, slug="ransom-note", title="Ransom Note", diff="Easy", topic="Hashmap", cls="RansomNote",
idea="Count the magazine's letters, then spend one count per letter of the note.",
vname="Letter counts",
spec=r'''
Return `true` if `ransomNote` can be built from the letters of `magazine`, using each magazine letter at most once.

**Example 1**
```
Input:  ransomNote = "a", magazine = "b"
Output: false
```

**Example 2**
```
Input:  ransomNote = "aa", magazine = "aab"
Output: true
```

**Constraints**
* `1 <= ransomNote.length, magazine.length <= 10^5`; lowercase letters.
''',
approach=r'''
**Counting array.** Count each letter of `magazine` in an `int[26]`. For each letter of the note, decrement its count; if it
goes negative, the magazine lacks that letter.

* Time: **O(m + n)** — one pass over each string.
* Space: **O(1)** — 26 counters.
''',
tc="n",
java=r'''
public class RansomNote {

    public boolean canConstruct(String ransomNote, String magazine) {
        int[] count = new int[26];
        for (char c : magazine.toCharArray()) count[c - 'a']++;
        for (char c : ransomNote.toCharArray()) {
            if (--count[c - 'a'] < 0) return false;
        }
        return true;
    }
}
''',
test=r'''
class RansomNoteTest {

    private final RansomNote solution = new RansomNote();

    @ParameterizedTest
    @CsvSource({"a,b,false", "aa,ab,false", "aa,aab,true", "abc,cbaxyz,true"})
    void checks(String note, String magazine, boolean expected) {
        assertEquals(expected, solution.canConstruct(note, magazine));
    }
}
''',
trace=r'''
function run(note, mag) {
  const cnt = new Map();
  for (const c of mag) cnt.set(c, (cnt.get(c) || 0) + 1);
  A.step('Count the letters available in the magazine.', A.chars('magazine', mag), A.map('available', cnt));
  for (let i = 0; i < note.length; i++) {
    const c = note[i], left = (cnt.get(c) || 0) - 1;
    cnt.set(c, left);
    if (left < 0) { A.step(`The note needs another '${c}', but the magazine has none left. The answer is false.`, A.chars('ransomNote', note, { hl: { [i]: 'bad' } }), A.map('available', cnt), A.text('Result', 'false', 'bad')); return; }
    A.step(`Use one '${c}'. ${left} left.`, A.chars('ransomNote', note, { hl: [...Array(i + 1).keys()].map(t => [t, t === i ? 'cur' : 'ok']) }), A.map('available', cnt));
  }
  A.step('Every letter of the note was covered, so the answer is true.', A.chars('ransomNote', note, { hl: [...note].map((_, t) => [t, 'ok']) }), A.text('Result', 'true', 'ok'));
}
A.scenario('Enough letters', 'ransomNote = "aab", magazine = "baac"', () => run('aab', 'baac'));
A.scenario('Missing a letter', 'ransomNote = "aa", magazine = "ab"', () => run('aa', 'ab'));
'''),

P(num=205, slug="isomorphic-strings", title="Isomorphic Strings", diff="Easy", topic="Hashmap", cls="IsomorphicStrings",
idea="Map characters both ways (s→t and t→s); any conflicting mapping means not isomorphic.",
vname="Two-way mapping",
spec=r'''
Two strings `s` and `t` are **isomorphic** if the characters of `s` can be replaced to get `t`: every occurrence of a character
is replaced by the same character, and no two different characters map to the same character (a character may map to itself).

**Example 1**
```
Input:  s = "egg", t = "add"
Output: true
```

**Example 2**
```
Input:  s = "foo", t = "bar"
Output: false
```

**Example 3**
```
Input:  s = "paper", t = "title"
Output: true
```

**Constraints**
* `1 <= s.length <= 5 * 10^4`, `t.length == s.length`; any ASCII characters.
''',
approach=r'''
**Two maps.** Walk both strings together. If `s[i]` already maps to something other than `t[i]`, or `t[i]` is already the image
of a different character, return `false`. Otherwise record both directions.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two arrays of 256 entries.
''',
tc="n",
java=r'''
public class IsomorphicStrings {

    public boolean isIsomorphic(String s, String t) {
        int[] sToT = new int[256], tToS = new int[256];
        for (int i = 0; i < s.length(); i++) {
            char a = s.charAt(i), b = t.charAt(i);
            if (sToT[a] == 0 && tToS[b] == 0) {
                sToT[a] = b;
                tToS[b] = a;
            } else if (sToT[a] != b || tToS[b] != a) {
                return false;
            }
        }
        return true;
    }
}
''',
test=r'''
class IsomorphicStringsTest {

    private final IsomorphicStrings solution = new IsomorphicStrings();

    @ParameterizedTest
    @CsvSource({"egg,add,true", "foo,bar,false", "paper,title,true", "badc,baba,false", "ab,aa,false"})
    void checks(String s, String t, boolean expected) {
        assertEquals(expected, solution.isIsomorphic(s, t));
    }
}
''',
trace=r'''
function run(s, t) {
  const st = new Map(), ts = new Map();
  A.step('Walk both strings together and build the mapping in both directions.', A.chars('s', s), A.chars('t', t), A.map('s → t', st), A.map('t → s', ts));
  for (let i = 0; i < s.length; i++) {
    const a = s[i], b = t[i];
    if ((st.has(a) && st.get(a) !== b) || (ts.has(b) && ts.get(b) !== a)) {
      A.step(st.has(a) && st.get(a) !== b ? `'${a}' already maps to '${st.get(a)}', but here it would map to '${b}'. Not isomorphic.` : `'${b}' is already the image of '${ts.get(b)}', so '${a}' cannot map to it. Not isomorphic.`, A.chars('s', s, { hl: { [i]: 'bad' } }), A.chars('t', t, { hl: { [i]: 'bad' } }), A.map('s → t', st), A.map('t → s', ts), A.text('Result', 'false', 'bad'));
      return;
    }
    const isNew = !st.has(a); st.set(a, b); ts.set(b, a);
    A.step(isNew ? `New pair: '${a}' ↔ '${b}'.` : `'${a}' → '${b}' is consistent with the mapping so far.`, A.chars('s', s, { hl: { [i]: 'cur' } }), A.chars('t', t, { hl: { [i]: 'cur' } }), A.map('s → t', st), A.map('t → s', ts));
  }
  A.step('Every pair was consistent in both directions. The strings are isomorphic.', A.text('Result', 'true', 'ok'));
}
A.scenario('Isomorphic', 's = "paper", t = "title"', () => run('paper', 'title'));
A.scenario('Two letters, one image', 's = "badc", t = "baba"', () => run('badc', 'baba'));
'''),
]
