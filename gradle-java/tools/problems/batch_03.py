PROBLEMS = [
P(num=151, slug="reverse-words-in-a-string", title="Reverse Words in a String", diff="Medium", topic="Array / String", cls="ReverseWords",
idea="Scan from the right, cut out each word, and append it; spaces collapse naturally.",
spec=r'''
Given a string `s`, reverse the order of its **words**. A word is a run of non-space characters. The result must have exactly
one space between words and no leading or trailing spaces, even if `s` has extra spaces.

**Example 1**
```
Input:  s = "the sky is blue"
Output: "blue is sky the"
```

**Example 2**
```
Input:  s = "  hello world  "
Output: "world hello"
```

**Example 3**
```
Input:  s = "a good   example"
Output: "example good a"
```

**Constraints**
* `1 <= s.length <= 10^4`; letters, digits and spaces; at least one word.
''',
approach=r'''
**Right-to-left scan.** Walk `i` from the end. Skip spaces; mark `end`; move `i` left while it points at a non-space;
the word is `s[i+1 .. end]`. Append it to a `StringBuilder`, with a space before every word but the first.

* Time: **O(n)** — every character is visited once and copied once.
* Space: **O(n)** — the output builder.
''',
java=r'''
public class ReverseWords {

    public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder();
        int i = s.length() - 1;
        while (i >= 0) {
            while (i >= 0 && s.charAt(i) == ' ') {
                i--;
            }
            if (i < 0) {
                break;
            }
            int end = i;
            while (i >= 0 && s.charAt(i) != ' ') {
                i--;
            }
            if (!sb.isEmpty()) {
                sb.append(' ');
            }
            sb.append(s, i + 1, end + 1);
        }
        return sb.toString();
    }
}
''',
test=r'''
class ReverseWordsTest {

    private final ReverseWords solution = new ReverseWords();

    @Test
    void simple() {
        assertEquals("blue is sky the", solution.reverseWords("the sky is blue"));
    }

    @Test
    void trimsOuterSpaces() {
        assertEquals("world hello", solution.reverseWords("  hello world  "));
    }

    @Test
    void collapsesInnerSpaces() {
        assertEquals("example good a", solution.reverseWords("a good   example"));
    }
}
''',
trace=r'''
function run(s) {
  const shown = [...s].map(c => (c === ' ' ? '␣' : c));
  let i = s.length - 1, out = [];
  A.step('Scan from the right. Each time we find a word, cut it out and append it to the result.', A.arr('s', shown, { ptr: [[i, 'i']] }), A.arr('result words', out));
  while (i >= 0) {
    while (i >= 0 && s[i] === ' ') i--;
    if (i < 0) break;
    const end = i;
    while (i >= 0 && s[i] !== ' ') i--;
    out.push(s.slice(i + 1, end + 1));
    const hl = []; for (let t = i + 1; t <= end; t++) hl.push([t, 'ok']);
    A.step(`Found the word "${out[out.length - 1]}" at indices ${i + 1} to ${end}. Append it.`, A.arr('s', shown, { hl, ptr: [[Math.max(i, 0), 'i']] }), A.arr('result words', out, { hl: { [out.length - 1]: 'ok' } }));
  }
  A.step(`Join the words with single spaces: "${out.join(' ')}".`, A.arr('result words', out), A.text('Result', `"${out.join(' ')}"`, 'ok'));
}
A.scenario('Plain sentence', 's = "the sky is blue"', () => run('the sky is blue'));
A.scenario('Edge: extra spaces', 's = "  hello  world "', () => run('  hello  world '));
'''),

P(num=6, slug="zigzag-conversion", title="Zigzag Conversion", diff="Medium", topic="Array / String", cls="ZigzagConversion",
idea="Deal characters onto rows, bouncing the row index down and up; then read the rows in order.",
spec=r'''
Write the string `s` in a zigzag pattern on `numRows` rows (down the rows, then diagonally back up, and repeat), then read it
row by row. For `"PAYPALISHIRING"` with 3 rows:
```
P   A   H   N
A P L S I I G
Y   I   R
```
which reads `"PAHNAPLSIIGYIR"`.

**Example 1**
```
Input:  s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
```

**Example 2**
```
Input:  s = "A", numRows = 1
Output: "A"
```

**Constraints**
* `1 <= s.length <= 1000`, `1 <= numRows <= 1000`
''',
approach=r'''
**Simulate the rows.** Keep one `StringBuilder` per row and a current row with a direction. Append each character to the
current row; flip direction at the top and bottom rows. Concatenate the rows. With one row, return `s`.

* Time: **O(n)** — each character is placed once and read once.
* Space: **O(n)** — the row builders hold every character.
''',
java=r'''
public class ZigzagConversion {

    public String convert(String s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }
        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = new StringBuilder();
        }
        int row = 0, step = 1;
        for (char c : s.toCharArray()) {
            rows[row].append(c);
            if (row == 0) {
                step = 1;
            } else if (row == numRows - 1) {
                step = -1;
            }
            row += step;
        }
        StringBuilder out = new StringBuilder();
        for (StringBuilder r : rows) {
            out.append(r);
        }
        return out.toString();
    }
}
''',
test=r'''
class ZigzagConversionTest {

    private final ZigzagConversion solution = new ZigzagConversion();

    @Test
    void threeRows() {
        assertEquals("PAHNAPLSIIGYIR", solution.convert("PAYPALISHIRING", 3));
    }

    @Test
    void fourRows() {
        assertEquals("PINALSIGYAHRPI", solution.convert("PAYPALISHIRING", 4));
    }

    @Test
    void oneRow() {
        assertEquals("AB", solution.convert("AB", 1));
    }
}
''',
trace=r'''
function run(s, R) {
  const cols = s.length, g = Array.from({ length: R }, () => new Array(cols).fill(''));
  let row = 0, step = 1;
  const rows = Array.from({ length: R }, () => '');
  A.step(`Write the letters down the ${R} rows, then diagonally back up, and repeat.`, A.grid('zigzag', g), A.chars('s', s));
  [...s].forEach((c, i) => {
    g[row][i] = c; rows[row] += c;
    A.step(`'${c}' goes on row ${row}. ${row === R - 1 ? 'This is the bottom row, so turn upwards.' : row === 0 && i > 0 ? 'This is the top row, so turn downwards.' : ''}`, A.grid('zigzag', g, { hl: { [row + ',' + i]: 'cur' } }), A.chars('s', s, { hl: { [i]: 'cur' } }));
    if (row === 0) step = 1; else if (row === R - 1) step = -1;
    row += step;
  });
  A.step('Now read each row from left to right and join them.', A.arr('rows', rows, { hl: rows.map((_, t) => [t, 'sel']) }));
  A.step(`Result: "${rows.join('')}".`, A.text('Result', rows.join(''), 'ok'));
}
A.scenario('3 rows', 's = "PAYPALISHI", numRows = 3', () => run('PAYPALISHI', 3));
A.scenario('4 rows', 's = "PAYPALISH", numRows = 4', () => run('PAYPALISH', 4));
'''),

P(num=28, slug="find-the-index-of-the-first-occurrence-in-a-string", title="Find the Index of the First Occurrence in a String", diff="Easy", topic="Array / String", cls="StrStr",
idea="KMP: precompute how far the needle can fall back on a mismatch, so the haystack pointer never moves backwards.",
spec=r'''
Return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` does not occur.

**Example 1**
```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
```

**Example 2**
```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
```

**Constraints**
* `1 <= haystack.length, needle.length <= 10^4`, lowercase letters only.
''',
approach=r'''
**Knuth–Morris–Pratt.** Build `lps[i]`: the length of the longest proper prefix of `needle[0..i]` that is also its suffix.
Then scan the haystack with `j` matched characters. On a mismatch, fall back to `j = lps[j-1]` instead of restarting,
so the haystack index only moves forward.

* Time: **O(n + m)** — building lps is O(m), and the scan is O(n).
* Space: **O(m)** — the lps table.
''',
java=r'''
public class StrStr {

    public int strStr(String haystack, String needle) {
        int m = needle.length();
        int[] lps = new int[m];
        for (int i = 1, len = 0; i < m; ) {
            if (needle.charAt(i) == needle.charAt(len)) {
                lps[i++] = ++len;
            } else if (len > 0) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }
        for (int i = 0, j = 0; i < haystack.length(); ) {
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
                if (j == m) {
                    return i - m;
                }
            } else if (j > 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
        return -1;
    }
}
''',
test=r'''
class StrStrTest {

    private final StrStr solution = new StrStr();

    @ParameterizedTest
    @CsvSource({"sadbutsad,sad,0", "leetcode,leeto,-1", "aaaaab,aab,3", "abc,c,2", "mississippi,issip,4"})
    void finds(String haystack, String needle, int expected) {
        assertEquals(expected, solution.strStr(haystack, needle));
    }
}
''',
trace=r'''
function run(h, nd) {
  const m = nd.length, lps = new Array(m).fill(0);
  for (let i = 1, len = 0; i < m;) { if (nd[i] === nd[len]) lps[i++] = ++len; else if (len) len = lps[len - 1]; else lps[i++] = 0; }
  A.step('First build the fallback table: lps[i] is how many characters still match after a mismatch past position i.', A.chars('needle', nd), A.arr('lps', lps));
  let i = 0, j = 0;
  const view = (hh, nh) => [A.chars('haystack', h, { hl: hh, ptr: [[i, 'i']] }), A.chars('needle', nd, { hl: nh, ptr: [[j, 'j']] }), A.vars({ i, j })];
  while (i < h.length) {
    const mk = []; for (let t = 0; t < j; t++) mk.push([i - j + t, 'ok']);
    if (h[i] === nd[j]) {
      A.step(`'${h[i]}' matches needle[${j}]. Advance both pointers.`, view(mk.concat([[i, 'cur']]), [...Array(j).keys()].map(t => [t, 'ok']).concat([[j, 'cur']])));
      i++; j++;
      if (j === m) { A.step(`All ${m} characters matched. The needle starts at index ${i - m}.`, A.chars('haystack', h, { hl: [...Array(m).keys()].map(t => [i - m + t, 'ok']) }), A.text('Result', i - m, 'ok')); return; }
    } else if (j > 0) {
      A.step(`'${h[i]}' does not match '${nd[j]}'. Instead of restarting, fall back to j = lps[${j - 1}] = ${lps[j - 1]}. i stays put.`, view(mk.concat([[i, 'bad']]), [[j, 'bad']]));
      j = lps[j - 1];
    } else {
      A.step(`'${h[i]}' does not match the first needle character. Move i forward.`, view([[i, 'bad']], [[0, 'bad']]));
      i++;
    }
  }
  A.step('The haystack is exhausted without a full match. The answer is -1.', A.chars('haystack', h), A.text('Result', -1, 'bad'));
}
A.scenario('Fallback in action', 'haystack = "aaaab", needle = "aab"', () => run('aaaab', 'aab'));
A.scenario('Match at the start', 'haystack = "sadbutsad", needle = "sad"', () => run('sadbutsad', 'sad'));
A.scenario('Edge: not found', 'haystack = "leetco", needle = "leeto"', () => run('leetco', 'leeto'));
'''),

P(num=68, slug="text-justification", title="Text Justification", diff="Hard", topic="Array / String", cls="TextJustification",
idea="Greedily pack words per line, then spread the spare spaces across gaps, giving the extra ones to the leftmost gaps.",
spec=r'''
Given `words` and a width `maxWidth`, format the text so that every line has exactly `maxWidth` characters and is fully justified.
* Pack as many words as fit on each line (greedy), with at least one space between words.
* Spread extra spaces as evenly as possible between words; if they don't divide evenly, the **left** gaps get more.
* The **last line**, and any line with a single word, is left-justified and padded with spaces on the right.

**Example**
```
Input:  words = ["This","is","an","example","of","text","justification."], maxWidth = 16
Output: ["This    is    an",
         "example  of text",
         "justification.  "]
```

**Constraints**
* `1 <= words.length <= 300`, `1 <= words[i].length <= 20`
* `words[i].length <= maxWidth <= 100`
''',
approach=r'''
**Greedy lines + space distribution.** Starting at word `i`, extend `j` while `lettersLength + (j - i) <= maxWidth`.
For a normal line with `gaps = j - i - 1`, total spaces = `maxWidth - letters`; each gap gets `spaces / gaps` and the first
`spaces % gaps` gaps get one more. The last line and single-word lines are joined with one space and right-padded.

* Time: **O(L)** — L is the total number of output characters (lines × maxWidth); each is written once.
* Space: **O(maxWidth)** — the builder for the current line, apart from the output.
''',
java=r'''
public class TextJustification {

    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> lines = new ArrayList<>();
        int i = 0;
        while (i < words.length) {
            int j = i, letters = 0;
            while (j < words.length && letters + words[j].length() + (j - i) <= maxWidth) {
                letters += words[j].length();
                j++;
            }
            StringBuilder sb = new StringBuilder();
            int gaps = j - i - 1;
            if (j == words.length || gaps == 0) {
                for (int k = i; k < j; k++) {
                    if (k > i) sb.append(' ');
                    sb.append(words[k]);
                }
                sb.append(" ".repeat(maxWidth - sb.length()));
            } else {
                int spaces = maxWidth - letters;
                for (int k = i; k < j; k++) {
                    sb.append(words[k]);
                    if (k < j - 1) {
                        int g = k - i;
                        sb.append(" ".repeat(spaces / gaps + (g < spaces % gaps ? 1 : 0)));
                    }
                }
            }
            lines.add(sb.toString());
            i = j;
        }
        return lines;
    }
}
''',
test=r'''
class TextJustificationTest {

    private final TextJustification solution = new TextJustification();

    @Test
    void example1() {
        String[] words = {"This", "is", "an", "example", "of", "text", "justification."};
        assertEquals(List.of("This    is    an", "example  of text", "justification.  "), solution.fullJustify(words, 16));
    }

    @Test
    void lastLineLeftJustified() {
        String[] words = {"What", "must", "be", "acknowledgment", "shall", "be"};
        assertEquals(List.of("What   must   be", "acknowledgment  ", "shall be        "), solution.fullJustify(words, 16));
    }

    @Test
    void singleWord() {
        assertEquals(List.of("hi   "), solution.fullJustify(new String[]{"hi"}, 5));
    }
}
''',
trace=r'''
function run(words, W) {
  const lines = [];
  let i = 0;
  A.step(`Pack words greedily into lines of width ${W}, then spread the leftover spaces.`, A.arr('words', words));
  while (i < words.length) {
    let j = i, letters = 0;
    while (j < words.length && letters + words[j].length + (j - i) <= W) { letters += words[j].length; j++; }
    const hl = words.map((_, t) => [t, t < i ? 'dim' : t < j ? 'sel' : '']);
    A.step(`Words ${i} to ${j - 1} fit: ${letters} letters plus at least ${j - i - 1} single spaces is at most ${W}.${j < words.length ? ` Adding "${words[j]}" would overflow.` : ''}`, A.arr('words', words, { hl }));
    const gaps = j - i - 1;
    let line;
    if (j === words.length || gaps === 0) {
      line = words.slice(i, j).join(' '); line += ' '.repeat(W - line.length);
      A.step(j === words.length ? 'This is the last line, so it is left-justified and padded on the right.' : 'A single word on a line is padded on the right.', A.chars('line', line.replace(/ /g, '·'), { noIdx: true, hl: [...line].map((c, t) => [t, c === ' ' ? 'alt' : 'ok']) }));
    } else {
      const sp = W - letters, base = Math.floor(sp / gaps), extra = sp % gaps;
      line = '';
      for (let k = i; k < j; k++) { line += words[k]; if (k < j - 1) line += ' '.repeat(base + (k - i < extra ? 1 : 0)); }
      A.step(`${sp} spaces across ${gaps} gaps: each gets ${base}${extra ? `, and the first ${extra} get one extra` : ''}.`, A.chars('line', line.replace(/ /g, '·'), { noIdx: true, hl: [...line].map((c, t) => [t, c === ' ' ? 'alt' : 'ok']) }));
    }
    lines.push(line); i = j;
  }
  A.step('All lines are exactly the same width.', A.grid('output', lines.map(l => [...l].map(c => (c === ' ' ? '·' : c)))));
}
A.scenario('Classic example', 'maxWidth = 16', () => run(['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], 16));
A.scenario('Single long word', 'maxWidth = 12', () => run(['to', 'acknowledge', 'it', 'all'], 12));
'''),

P(num=125, slug="valid-palindrome", title="Valid Palindrome", diff="Easy", topic="Two Pointers", cls="ValidPalindrome",
idea="Two pointers move inward, skipping non-alphanumerics and comparing letters case-insensitively.",
spec=r'''
A phrase is a **palindrome** if, after lower-casing it and removing every non-alphanumeric character, it reads the same
forward and backward. Return `true` if `s` is a palindrome.

**Example 1**
```
Input:  s = "A man, a plan, a canal: Panama"
Output: true
```

**Example 2**
```
Input:  s = "race a car"
Output: false
```

**Example 3**
```
Input:  s = " "
Output: true
```

**Constraints**
* `1 <= s.length <= 2 * 10^5`, printable ASCII.
''',
approach=r'''
**Two pointers.** `l` starts at 0 and `r` at the end. Skip characters that are not letters or digits. Compare
`toLowerCase(s[l])` with `toLowerCase(s[r])`; on mismatch return `false`; otherwise move both inward.

* Time: **O(n)** — each character is visited at most once.
* Space: **O(1)** — no cleaned copy of the string.
''',
java=r'''
public class ValidPalindrome {

    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
            while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
''',
test=r'''
class ValidPalindromeTest {

    private final ValidPalindrome solution = new ValidPalindrome();

    @Test
    void sentencePalindrome() {
        assertTrue(solution.isPalindrome("A man, a plan, a canal: Panama"));
    }

    @Test
    void notPalindrome() {
        assertFalse(solution.isPalindrome("race a car"));
    }

    @Test
    void onlySpaces() {
        assertTrue(solution.isPalindrome(" "));
    }

    @Test
    void digitsMatter() {
        assertFalse(solution.isPalindrome("0P"));
    }
}
''',
trace=r'''
const isAN = c => /[a-z0-9]/i.test(c);
function run(s) {
  const shown = [...s].map(c => (c === ' ' ? '␣' : c));
  let l = 0, r = s.length - 1;
  const done = [];
  A.step('Two pointers start at both ends and move inward, ignoring punctuation and case.', A.arr('s', shown, { ptr: [[l, 'l'], [r, 'r']], hl: shown.map((c, t) => [t, isAN(s[t]) ? '' : 'dim']) }));
  while (l < r) {
    while (l < r && !isAN(s[l])) l++;
    while (l < r && !isAN(s[r])) r--;
    const base = shown.map((c, t) => [t, isAN(s[t]) ? '' : 'dim']).concat(done);
    if (s[l].toLowerCase() !== s[r].toLowerCase()) { A.step(`'${s[l]}' and '${s[r]}' differ, so this is not a palindrome.`, A.arr('s', shown, { ptr: [[l, 'l'], [r, 'r']], hl: base.concat([[l, 'bad'], [r, 'bad']]) }), A.text('Result', 'false', 'bad')); return; }
    A.step(`'${s[l]}' and '${s[r]}' match, ignoring case. Move both inward.`, A.arr('s', shown, { ptr: [[l, 'l'], [r, 'r']], hl: base.concat([[l, 'cur'], [r, 'cur']]) }));
    done.push([l, 'ok'], [r, 'ok']); l++; r--;
  }
  A.step('The pointers met without a mismatch, so it is a palindrome.', A.arr('s', shown, { hl: shown.map((c, t) => [t, isAN(s[t]) ? 'ok' : 'dim']) }), A.text('Result', 'true', 'ok'));
}
A.scenario('Sentence palindrome', 's = "Was it a cat, I saw?"', () => run('Was it a cat, I saw?'));
A.scenario('Not a palindrome', 's = "race a car"', () => run('race a car'));
'''),

P(num=392, slug="is-subsequence", title="Is Subsequence", diff="Easy", topic="Two Pointers", cls="IsSubsequence",
idea="Walk through t once; advance the pointer in s each time its current character appears.",
spec=r'''
Return `true` if `s` is a **subsequence** of `t`: that is, `s` can be formed by deleting some (possibly zero) characters
of `t` without changing the order of the rest.

**Example 1**
```
Input:  s = "abc", t = "ahbgdc"
Output: true
```

**Example 2**
```
Input:  s = "axc", t = "ahbgdc"
Output: false
```

**Constraints**
* `0 <= s.length <= 100`, `0 <= t.length <= 10^4`, lowercase letters only.
''',
approach=r'''
**Two pointers.** `i` walks `s`, `j` walks `t`. Whenever `s[i] == t[j]`, advance `i`. Always advance `j`.
`s` is a subsequence if `i` reaches `s.length()`.

* Time: **O(n)** — n is the length of t; each character of t is checked once.
* Space: **O(1)** — two indices.
''',
java=r'''
public class IsSubsequence {

    public boolean isSubsequence(String s, String t) {
        int i = 0;
        for (int j = 0; j < t.length() && i < s.length(); j++) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
            }
        }
        return i == s.length();
    }
}
''',
test=r'''
class IsSubsequenceTest {

    private final IsSubsequence solution = new IsSubsequence();

    @Test
    void found() {
        assertTrue(solution.isSubsequence("abc", "ahbgdc"));
    }

    @Test
    void notFound() {
        assertFalse(solution.isSubsequence("axc", "ahbgdc"));
    }

    @Test
    void emptyIsAlwaysSubsequence() {
        assertTrue(solution.isSubsequence("", "abc"));
    }
}
''',
trace=r'''
function run(s, t) {
  let i = 0;
  const hs = [], ht = [];
  A.step('Walk through t once. Each time t has the next character we need from s, move forward in s.', A.chars('s', s, { ptr: [[0, 'i']] }), A.chars('t', t, { ptr: [[0, 'j']] }));
  for (let j = 0; j < t.length && i < s.length; j++) {
    if (s[i] === t[j]) { hs.push([i, 'ok']); ht.push([j, 'ok']); A.step(`t[${j}] = '${t[j]}' is the character we need. Matched s[${i}].`, A.chars('s', s, { ptr: [[i + 1, 'i']], hl: hs.slice() }), A.chars('t', t, { ptr: [[j, 'j']], hl: ht.concat([[j, 'cur']]) })); i++; }
    else A.step(`t[${j}] = '${t[j]}' is not '${s[i]}'. Skip it.`, A.chars('s', s, { ptr: [[i, 'i']], hl: hs.concat([[i, 'sel']]) }), A.chars('t', t, { ptr: [[j, 'j']], hl: ht.concat([[j, 'dim']]) }));
  }
  const ok = i === s.length;
  A.step(ok ? 'Every character of s was found in order, so the answer is true.' : `t ran out before we found '${s[i]}', so the answer is false.`, A.chars('s', s, { hl: ok ? hs : hs.concat([[i, 'bad']]) }), A.chars('t', t, { hl: ht }), A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('Is a subsequence', 's = "abc", t = "ahbgdc"', () => run('abc', 'ahbgdc'));
A.scenario('Not a subsequence', 's = "axc", t = "ahbgdc"', () => run('axc', 'ahbgdc'));
'''),

P(num=167, slug="two-sum-ii-input-array-is-sorted", title="Two Sum II - Input Array Is Sorted", diff="Medium", topic="Two Pointers", cls="TwoSumII",
idea="Sorted input: if the sum is too small move the left pointer right, if too big move the right pointer left.",
spec=r'''
`numbers` is sorted in non-decreasing order (1-indexed). Find two different positions `index1 < index2` whose values add up to
`target`, and return `[index1, index2]` (1-based). Exactly one solution exists. Use only constant extra space.

**Example 1**
```
Input:  numbers = [2,7,11,15], target = 9
Output: [1,2]
```

**Example 2**
```
Input:  numbers = [-1,0], target = -1
Output: [1,2]
```

**Constraints**
* `2 <= numbers.length <= 3 * 10^4`
* `-1000 <= numbers[i], target <= 1000`
''',
approach=r'''
**Two pointers.** Start `l = 0`, `r = n - 1`. If `numbers[l] + numbers[r]` is too small, only a larger left value can help,
so `l++`; if too big, `r--`. Each move rules out a value that can't be part of the answer.

* Time: **O(n)** — the pointers move toward each other at most n times.
* Space: **O(1)** — two indices.
''',
java=r'''
public class TwoSumII {

    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1;
        while (l < r) {
            int sum = numbers[l] + numbers[r];
            if (sum == target) {
                return new int[]{l + 1, r + 1};
            } else if (sum < target) {
                l++;
            } else {
                r--;
            }
        }
        throw new IllegalArgumentException("No solution");
    }
}
''',
test=r'''
class TwoSumIITest {

    private final TwoSumII solution = new TwoSumII();

    @Test
    void example1() {
        assertArrayEquals(new int[]{1, 2}, solution.twoSum(new int[]{2, 7, 11, 15}, 9));
    }

    @Test
    void example2() {
        assertArrayEquals(new int[]{1, 3}, solution.twoSum(new int[]{2, 3, 4}, 6));
    }

    @Test
    void negatives() {
        assertArrayEquals(new int[]{1, 2}, solution.twoSum(new int[]{-1, 0}, -1));
    }
}
''',
trace=r'''
function run(a, target) {
  let l = 0, r = a.length - 1;
  const gone = [];
  A.step(`Find two values that add up to ${target}. Start with the smallest and the largest.`, A.arr('numbers', a, { ptr: [[l, 'l'], [r, 'r']] }), A.vars({ target }));
  while (l < r) {
    const s = a[l] + a[r];
    if (s === target) { A.step(`${a[l]} + ${a[r]} = ${target}. Found it. The 1-based answer is [${l + 1}, ${r + 1}].`, A.arr('numbers', a, { ptr: [[l, 'l'], [r, 'r']], hl: gone.concat([[l, 'ok'], [r, 'ok']]) }), A.text('Result', `[${l + 1}, ${r + 1}]`, 'ok')); return; }
    if (s < target) { A.step(`${a[l]} + ${a[r]} = ${s} is too small. ${a[l]} can't work with any value, so move l right.`, A.arr('numbers', a, { ptr: [[l, 'l'], [r, 'r']], hl: gone.concat([[l, 'bad'], [r, 'cur']]) }), A.vars({ target, sum: s })); gone.push([l, 'dim']); l++; }
    else { A.step(`${a[l]} + ${a[r]} = ${s} is too big. ${a[r]} can't work with any value, so move r left.`, A.arr('numbers', a, { ptr: [[l, 'l'], [r, 'r']], hl: gone.concat([[l, 'cur'], [r, 'bad']]) }), A.vars({ target, sum: s })); gone.push([r, 'dim']); r--; }
  }
}
A.scenario('Pair in the middle', 'numbers = [1,3,4,6,8,11], target = 10', () => run([1, 3, 4, 6, 8, 11], 10));
A.scenario('Pair at the start', 'numbers = [2,7,11,15], target = 9', () => run([2, 7, 11, 15], 9));
'''),

P(num=11, slug="container-with-most-water", title="Container With Most Water", diff="Medium", topic="Two Pointers", cls="ContainerWithMostWater",
idea="Start with the widest container and always move the shorter wall inward: that is the only move that might help.",
spec=r'''
`height[i]` is the height of a vertical line at position `i`. Choose two lines that, together with the x-axis, form a container
holding the most water. Return that maximum amount: `min(height[i], height[j]) × (j - i)`.

**Example 1**
```
Input:  height = [1,8,6,2,5,4,8,3,7]
Output: 49   (lines at 1 and 8: min(8,7) × 7)
```

**Example 2**
```
Input:  height = [1,1]
Output: 1
```

**Constraints**
* `2 <= n <= 10^5`
* `0 <= height[i] <= 10^4`
''',
approach=r'''
**Two pointers.** Start with `l = 0` and `r = n - 1` (maximum width). The area is limited by the shorter wall.
Moving the taller wall inward can only shrink the width without raising the limit, so always move the **shorter** one.

* Time: **O(n)** — each step moves one pointer inward.
* Space: **O(1)** — two pointers and the best area.
''',
java=r'''
public class ContainerWithMostWater {

    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1, best = 0;
        while (l < r) {
            best = Math.max(best, Math.min(height[l], height[r]) * (r - l));
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return best;
    }
}
''',
test=r'''
class ContainerWithMostWaterTest {

    private final ContainerWithMostWater solution = new ContainerWithMostWater();

    @Test
    void example1() {
        assertEquals(49, solution.maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7}));
    }

    @Test
    void twoLines() {
        assertEquals(1, solution.maxArea(new int[]{1, 1}));
    }

    @Test
    void decreasing() {
        assertEquals(16, solution.maxArea(new int[]{4, 3, 2, 1, 4}));
    }
}
''',
trace=r'''
function run(h) {
  const H = Math.max(...h);
  let l = 0, r = h.length - 1, best = 0, bl = 0, br = 0;
  const pic = () => { const g = []; for (let y = H; y >= 1; y--) g.push(h.map(() => '')); return g; };
  const ghl = () => { const o = [], lv = Math.min(h[l], h[r]); for (let y = H; y >= 1; y--) h.forEach((v, x) => { const k = `${H - y},${x}`; if (v >= y && (x === l || x === r)) o.push([k, 'bar,cur']); else if (x > l && x < r && y <= lv) o.push([k, 'water']); else if (v >= y) o.push([k, 'bar']); }); return o; };
  A.step('Start with the widest container: the first and last lines.', A.grid('lines', pic(), { hl: ghl() }), A.vars({ best }));
  while (l < r) {
    const area = Math.min(h[l], h[r]) * (r - l);
    if (area > best) { best = area; bl = l; br = r; }
    const moveL = h[l] < h[r];
    A.step(`Lines ${l} and ${r}: the height is min(${h[l]}, ${h[r]}) = ${Math.min(h[l], h[r])}, the width is ${r - l}, so the area is ${area}.${area === best && bl === l && br === r ? ' That is a new best.' : ''} Move the shorter line, on the ${moveL ? 'left' : 'right'}, inward.`, A.grid('lines', pic(), { hl: ghl() }), A.arr('height', h, { ptr: [[l, 'l'], [r, 'r']], hl: { [moveL ? l : r]: 'bad' } }), A.vars({ area, best }));
    if (moveL) l++; else r--;
  }
  l = bl; r = br;
  A.step(`The best container uses lines ${bl} and ${br}, with area ${best}.`, A.grid('lines', pic(), { hl: ghl() }), A.text('Result', best, 'ok'));
}
A.scenario('Classic', 'height = [1,8,6,2,5,4,8,3,7]', () => run([1, 8, 6, 2, 5, 4, 8, 3, 7]));
A.scenario('Edge: equal walls', 'height = [4,3,2,1,4]', () => run([4, 3, 2, 1, 4]));
'''),

P(num=15, slug="3sum", title="3Sum", diff="Medium", topic="Two Pointers", cls="ThreeSum",
idea="Sort, fix the first number, then find pairs summing to its negative with two pointers, skipping duplicates.",
spec=r'''
Return all **unique** triplets `[a, b, c]` from `nums` (at different indices) with `a + b + c == 0`. The answer must not
contain duplicate triplets; order does not matter.

**Example 1**
```
Input:  nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2**
```
Input:  nums = [0,1,1]
Output: []
```

**Example 3**
```
Input:  nums = [0,0,0]
Output: [[0,0,0]]
```

**Constraints**
* `3 <= nums.length <= 3000`
* `-10^5 <= nums[i] <= 10^5`
''',
approach=r'''
**Sort + two pointers.** Sort the array. For each `i` (skipping a value equal to the previous one), search `i+1..n-1` with `l`
and `r` for pairs summing to `-nums[i]`. On a hit, record it and skip equal neighbours on both sides. Stop once
`nums[i] > 0`, because then all three numbers are positive.

* Time: **O(n²)** — n choices of i, each with a linear two-pointer scan (the sort is O(n log n)).
* Space: **O(1)** — apart from sorting and the output.
''',
java=r'''
public class ThreeSum {

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> out = new ArrayList<>();
        for (int i = 0; i < nums.length - 2 && nums[i] <= 0; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum < 0) {
                    l++;
                } else if (sum > 0) {
                    r--;
                } else {
                    out.add(List.of(nums[i], nums[l], nums[r]));
                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (l < r && nums[r] == nums[r - 1]) r--;
                    l++;
                    r--;
                }
            }
        }
        return out;
    }
}
''',
test=r'''
class ThreeSumTest {

    private final ThreeSum solution = new ThreeSum();

    @Test
    void example1() {
        assertEquals(Set.of(List.of(-1, -1, 2), List.of(-1, 0, 1)), new HashSet<>(solution.threeSum(new int[]{-1, 0, 1, 2, -1, -4})));
    }

    @Test
    void none() {
        assertEquals(List.of(), solution.threeSum(new int[]{0, 1, 1}));
    }

    @Test
    void zeros() {
        assertEquals(List.of(List.of(0, 0, 0)), solution.threeSum(new int[]{0, 0, 0, 0}));
    }
}
''',
trace=r'''
function run(orig) {
  const a = orig.slice().sort((x, y) => x - y), out = [];
  A.step('Sort first. Then fix one number and look for a pair that cancels it.', A.arr('input', orig), A.arr('sorted', a));
  for (let i = 0; i < a.length - 2 && a[i] <= 0; i++) {
    if (i > 0 && a[i] === a[i - 1]) { A.step(`${a[i]} equals the previous fixed value. Skip it to avoid duplicate triplets.`, A.arr('nums', a, { ptr: [[i, 'i']], hl: { [i]: 'dim' } })); continue; }
    let l = i + 1, r = a.length - 1;
    A.step(`Fix nums[${i}] = ${a[i]}. We need a pair summing to ${-a[i]}.`, A.arr('nums', a, { ptr: [[i, 'i'], [l, 'l'], [r, 'r']], hl: { [i]: 'alt' } }), A.arr('triplets', out.map(t => `[${t}]`)));
    while (l < r) {
      const s = a[i] + a[l] + a[r];
      const base = { [i]: 'alt', [l]: 'cur', [r]: 'cur' };
      if (s < 0) { A.step(`${a[i]} + ${a[l]} + ${a[r]} = ${s} is below 0. Move l right.`, A.arr('nums', a, { ptr: [[i, 'i'], [l, 'l'], [r, 'r']], hl: base })); l++; }
      else if (s > 0) { A.step(`${a[i]} + ${a[l]} + ${a[r]} = ${s} is above 0. Move r left.`, A.arr('nums', a, { ptr: [[i, 'i'], [l, 'l'], [r, 'r']], hl: base })); r--; }
      else {
        out.push([a[i], a[l], a[r]]);
        A.step(`${a[i]} + ${a[l]} + ${a[r]} = 0. Record [${a[i]}, ${a[l]}, ${a[r]}], skip any equal neighbours, then move both pointers.`, A.arr('nums', a, { ptr: [[i, 'i'], [l, 'l'], [r, 'r']], hl: { [i]: 'ok', [l]: 'ok', [r]: 'ok' } }), A.arr('triplets', out.map(t => `[${t}]`), { hl: { [out.length - 1]: 'ok' } }));
        while (l < r && a[l] === a[l + 1]) l++;
        while (l < r && a[r] === a[r - 1]) r--;
        l++; r--;
      }
    }
  }
  A.step(`Found ${out.length} unique triplet${out.length === 1 ? '' : 's'}.`, A.arr('triplets', out.map(t => `[${t}]`), { hl: out.map((_, t) => [t, 'ok']) }), A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Duplicates in input', 'nums = [-1,0,1,2,-1,-4]', () => run([-1, 0, 1, 2, -1, -4]));
A.scenario('Edge: all zeros', 'nums = [0,0,0,0]', () => run([0, 0, 0, 0]));
'''),

P(num=209, slug="minimum-size-subarray-sum", title="Minimum Size Subarray Sum", diff="Medium", topic="Sliding Window", cls="MinimumSizeSubarraySum",
idea="Grow the window to the right until the sum reaches the target, then shrink it from the left while it still does.",
spec=r'''
Given positive integers `nums` and a positive `target`, return the minimal length of a contiguous subarray whose sum is
**at least** `target`. Return `0` if no such subarray exists.

**Example 1**
```
Input:  target = 7, nums = [2,3,1,2,4,3]
Output: 2   ([4,3])
```

**Example 2**
```
Input:  target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

**Constraints**
* `1 <= target <= 10^9`
* `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^4`
''',
approach=r'''
**Sliding window.** Extend `right` and add `nums[right]` to `sum`. While `sum >= target`, record the window length and remove
`nums[left]`, moving `left` forward. All values are positive, so shrinking always lowers the sum.

* Time: **O(n)** — each index enters and leaves the window at most once.
* Space: **O(1)** — the window bounds and the running sum.
''',
java=r'''
public class MinimumSizeSubarraySum {

    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, sum = 0, best = Integer.MAX_VALUE;
        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];
            while (sum >= target) {
                best = Math.min(best, right - left + 1);
                sum -= nums[left++];
            }
        }
        return best == Integer.MAX_VALUE ? 0 : best;
    }
}
''',
test=r'''
class MinimumSizeSubarraySumTest {

    private final MinimumSizeSubarraySum solution = new MinimumSizeSubarraySum();

    @Test
    void example1() {
        assertEquals(2, solution.minSubArrayLen(7, new int[]{2, 3, 1, 2, 4, 3}));
    }

    @Test
    void singleElementSuffices() {
        assertEquals(1, solution.minSubArrayLen(4, new int[]{1, 4, 4}));
    }

    @Test
    void impossible() {
        assertEquals(0, solution.minSubArrayLen(11, new int[]{1, 1, 1, 1, 1, 1, 1, 1}));
    }
}
''',
trace=r'''
function run(target, a) {
  let left = 0, sum = 0, best = Infinity;
  A.step(`Find the shortest window whose sum is at least ${target}. The window grows on the right and shrinks on the left.`, A.arr('nums', a), A.vars({ target, sum, best: '∞' }));
  for (let right = 0; right < a.length; right++) {
    sum += a[right];
    A.step(`Add nums[${right}] = ${a[right]}. The window sum is ${sum}.${sum >= target ? ' That reaches the target.' : ''}`, A.arr('nums', a, { range: [left, right], ptr: [[left, 'L'], [right, 'R']], hl: { [right]: 'cur' } }), A.vars({ target, sum, best: best === Infinity ? '∞' : best }));
    while (sum >= target) {
      best = Math.min(best, right - left + 1);
      A.step(`The window from ${left} to ${right} has length ${right - left + 1}, so best is ${best}. Try shrinking: remove ${a[left]}.`, A.arr('nums', a, { range: [left, right], ptr: [[left, 'L'], [right, 'R']], hl: { [left]: 'bad' } }), A.vars({ target, sum, best }));
      sum -= a[left++];
    }
  }
  const res = best === Infinity ? 0 : best;
  A.step(res ? `The minimal length is ${res}.` : `No window ever reaches ${target}, so the answer is 0.`, A.arr('nums', a), A.text('Result', res, res ? 'ok' : 'bad'));
}
A.scenario('Classic', 'target = 7, nums = [2,3,1,2,4,3]', () => run(7, [2, 3, 1, 2, 4, 3]));
A.scenario('Edge: impossible', 'target = 11, nums = [1,1,1,1,1]', () => run(11, [1, 1, 1, 1, 1]));
'''),
]
