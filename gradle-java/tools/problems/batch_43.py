PROBLEMS = [
P(num=415, slug="add-strings", title="Add Strings", diff="Easy", topic="Math", cls="AddStrings",
idea="Grade-school addition from the last digit, carrying as you go.",
vname="Digit-by-digit with carry",
spec=r'''
Given two non-negative integers as strings, return their sum as a string, without converting the inputs to numbers.

**Example**
```
"11"  + "123" → "134"
"456" + "77"  → "533"
"0"   + "0"   → "0"
```

**Constraints**
* `1 <= length <= 10^4`; no leading zeros except `"0"`
''',
approach=r'''
**Column addition.** Walk both strings from the right, adding digits and the carry. A missing digit counts as 0. Keep going while
either string has digits or a carry is left, then reverse the built string.

* Time: **O(max(m, n))**.
* Space: **O(max(m, n))** — the result.
''',
tc="n", sc="n",
java=r'''
public class AddStrings {

    public String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        int i = num1.length() - 1, j = num2.length() - 1, carry = 0;
        while (i >= 0 || j >= 0 || carry > 0) {
            int sum = carry;
            if (i >= 0) sum += num1.charAt(i--) - '0';
            if (j >= 0) sum += num2.charAt(j--) - '0';
            sb.append((char) ('0' + sum % 10));
            carry = sum / 10;
        }
        return sb.reverse().toString();
    }
}
''',
test=r'''
class AddStringsTest {

    private final AddStrings solution = new AddStrings();

    @ParameterizedTest
    @CsvSource({"11,123,134", "456,77,533", "0,0,0", "999,1,1000", "1,9999,10000", "123456789123456789,987654321987654321,1111111111111111110"})
    void sums(String a, String b, String expected) {
        assertEquals(expected, solution.addStrings(a, b));
    }
}
''',
trace=r'''
function run(a, b) {
  let i = a.length - 1, j = b.length - 1, carry = 0, out = '';
  A.step(`Add "${a}" and "${b}" column by column from the right.`, A.chars('num1', a), A.chars('num2', b));
  while (i >= 0 || j >= 0 || carry) {
    const x = i >= 0 ? +a[i] : 0, y = j >= 0 ? +b[j] : 0, s = x + y + carry;
    out = (s % 10) + out;
    A.step(`${x} + ${y} + carry ${carry} = ${s}: write ${s % 10}, carry ${Math.floor(s / 10)}.`, A.chars('num1', a, i >= 0 ? { hl: { [i]: 'cur' } } : {}), A.chars('num2', b, j >= 0 ? { hl: { [j]: 'cur' } } : {}), A.chars('sum', out, { hl: { 0: 'ok' } }));
    carry = Math.floor(s / 10); i--; j--;
  }
  A.step(`Result: ${out}.`, A.text('Result', out, 'ok'));
}
A.scenario('Different lengths', '"456" + "77"', () => run('456', '77'));
A.scenario('Carry grows the number', '"999" + "1"', () => run('999', '1'));
'''),

P(num=419, slug="battleships-in-a-board", title="Battleships in a Board", diff="Medium", topic="Matrix", cls="BattleshipsInBoard",
idea="Count only the top-left cell of each ship: an X with no X above it and no X to its left.",
vname="Count ship heads",
spec=r'''
A board of `'X'` (ship) and `'.'` (water) holds straight horizontal or vertical ships, never touching each other. Count the ships in one
pass, using O(1) extra memory and without modifying the board.

**Example**
```
X . . X
. . . X    → 2
. . . X
```

**Constraints**
* `1 <= m, n <= 200`
''',
approach=r'''
**Heads only.** Every ship has exactly one cell with no ship cell directly above it or directly to its left: its top-left end. Count
those cells.

* Time: **O(mn)**.
* Space: **O(1)**.
''',
tc="n2", sc="1",
java=r'''
public class BattleshipsInBoard {

    public int countBattleships(char[][] board) {
        int count = 0;
        for (int r = 0; r < board.length; r++)
            for (int c = 0; c < board[0].length; c++) {
                if (board[r][c] != 'X') continue;
                if (r > 0 && board[r - 1][c] == 'X') continue;
                if (c > 0 && board[r][c - 1] == 'X') continue;
                count++;
            }
        return count;
    }
}
''',
test=r'''
class BattleshipsInBoardTest {

    private final BattleshipsInBoard solution = new BattleshipsInBoard();

    private char[][] board(String... rows) {
        char[][] b = new char[rows.length][];
        for (int i = 0; i < rows.length; i++) b[i] = rows[i].toCharArray();
        return b;
    }

    @Test
    void examples() {
        assertEquals(2, solution.countBattleships(board("X..X", "...X", "...X")));
        assertEquals(0, solution.countBattleships(board(".")));
        assertEquals(3, solution.countBattleships(board("XX.X", "...X", "X...")));
    }
}
''',
trace=r'''
function run(rows) {
  const g = rows.map(r => [...r]), hl = {}; let count = 0;
  A.step('Scan row by row. A ship is counted at its top-left cell only.', A.grid('board', g));
  for (let r = 0; r < g.length; r++) for (let c = 0; c < g[0].length; c++) {
    if (g[r][c] !== 'X') continue;
    const up = r > 0 && g[r - 1][c] === 'X', left = c > 0 && g[r][c - 1] === 'X';
    if (up || left) { hl[`${r},${c}`] = 'dim'; A.step(`(${r},${c}) continues the ship ${up ? 'above' : 'to the left'}. Not a new ship.`, A.grid('board', g, { hl }), A.vars({ ships: count })); }
    else { count++; hl[`${r},${c}`] = 'ok'; A.step(`(${r},${c}) has no ship cell above or to its left: ship #${count} starts here.`, A.grid('board', g, { hl }), A.vars({ ships: count })); }
  }
  A.step(`${count} ships.`, A.text('Result', count, 'ok'));
}
A.scenario('Example', '3 × 4 board', () => run(['X..X', '...X', '...X']));
'''),

P(num=445, slug="add-two-numbers-ii", title="Add Two Numbers II", diff="Medium", topic="Linked List", cls="AddTwoNumbersII",
idea="Digits are stored most-significant first, so push them on stacks to add from the end.",
vname="Two stacks", helpers=["ListNode"],
spec=r'''
Two non-empty linked lists hold non-negative integers with the **most significant digit first**. Return their sum as a list in the same
order, without reversing the input lists.

**Example**
```
[7,2,4,3] + [5,6,4] → [7,8,0,7]    (7243 + 564 = 7807)
[2,4,3]   + [5,6,4] → [8,0,7]
[0] + [0]           → [0]
```

**Constraints**
* `1 <= length <= 100`; no leading zeros except the number 0
''',
approach=r'''
**Stacks.** Push each list's digits onto a stack, so popping yields digits from least significant. Add with a carry, and **prepend** each
result digit as a new head node, which builds the answer in the right order.

* Time: **O(m + n)**.
* Space: **O(m + n)** — the stacks.
''',
tc="n", sc="n",
java=r'''
public class AddTwoNumbersII {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Deque<Integer> a = new ArrayDeque<>(), b = new ArrayDeque<>();
        for (ListNode n = l1; n != null; n = n.next) a.push(n.val);
        for (ListNode n = l2; n != null; n = n.next) b.push(n.val);
        ListNode head = null;
        int carry = 0;
        while (!a.isEmpty() || !b.isEmpty() || carry > 0) {
            int sum = carry + (a.isEmpty() ? 0 : a.pop()) + (b.isEmpty() ? 0 : b.pop());
            head = new ListNode(sum % 10, head);
            carry = sum / 10;
        }
        return head;
    }
}
''',
test=r'''
class AddTwoNumbersIITest {

    private final AddTwoNumbersII solution = new AddTwoNumbersII();

    @Test
    void examples() {
        assertArrayEquals(new int[]{7, 8, 0, 7}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(7, 2, 4, 3), ListNode.of(5, 6, 4))));
        assertArrayEquals(new int[]{8, 0, 7}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(2, 4, 3), ListNode.of(5, 6, 4))));
        assertArrayEquals(new int[]{0}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(0), ListNode.of(0))));
        assertArrayEquals(new int[]{1, 0}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(5), ListNode.of(5))));
        assertArrayEquals(new int[]{1, 0, 0, 0}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(9, 9, 9), ListNode.of(1))));
    }
}
''',
trace=r'''
function run(x, y) {
  const a = x.slice(), b = y.slice(), out = []; let carry = 0;
  A.step('Push each list onto a stack; the last digit ends up on top.', A.list('l1', x), A.list('l2', y), A.stack('stack 1', a), A.stack('stack 2', b));
  while (a.length || b.length || carry) {
    const p = a.length ? a.pop() : 0, q = b.length ? b.pop() : 0, s = p + q + carry;
    out.unshift(s % 10);
    A.step(`Pop ${p} and ${q}; ${p} + ${q} + carry ${carry} = ${s}. New head node ${s % 10}, carry ${Math.floor(s / 10)}.`, A.stack('stack 1', a), A.stack('stack 2', b), A.list('result', out, { hl: { 0: 'ok' } }));
    carry = Math.floor(s / 10);
  }
  A.step(`Sum: [${out}].`, A.list('result', out));
}
A.scenario('Example', '[7,2,4,3] + [5,6,4]', () => run([7, 2, 4, 3], [5, 6, 4]));
A.scenario('Final carry', '[9,9,9] + [1]', () => run([9, 9, 9], [1]));
'''),

P(num=451, slug="sort-characters-by-frequency", title="Sort Characters By Frequency", diff="Medium", topic="Sorting", cls="FrequencySort",
idea="Count the characters, then bucket them by count and read the buckets from high to low.",
vname="Bucket sort by count",
spec=r'''
Sort a string so that characters appearing more often come first; equal characters stay together. Among characters with the same count,
this project lists them in character-code order.

**Example**
```
"tree"   → "eert"
"cccaaa" → "aaaccc"
"Aabb"   → "bbAa"
```

**Constraints**
* `1 <= s.length <= 5 * 10^5`; letters and digits
''',
approach=r'''
**Buckets.** Count every character (128 counters). Counts are at most `n`, so put each character in bucket `count`. Walk the buckets
from `n` down to 1 and write each character `count` times.

* Time: **O(n)** — counting, plus `n + 128` bucket work.
* Space: **O(n)** — the buckets and output.
''',
tc="n", sc="n",
java=r'''
public class FrequencySort {

    public String frequencySort(String s) {
        int[] count = new int[128];
        for (char c : s.toCharArray()) count[c]++;
        List<List<Character>> buckets = new ArrayList<>();
        for (int i = 0; i <= s.length(); i++) buckets.add(new ArrayList<>());
        for (char c = 0; c < 128; c++) if (count[c] > 0) buckets.get(count[c]).add(c);
        StringBuilder sb = new StringBuilder(s.length());
        for (int f = s.length(); f > 0; f--)
            for (char c : buckets.get(f)) sb.repeat(c, f);
        return sb.toString();
    }
}
''',
test=r'''
class FrequencySortTest {

    private final FrequencySort solution = new FrequencySort();

    @ParameterizedTest
    @CsvSource({"tree,eert", "cccaaa,aaaccc", "Aabb,bbAa", "a,a", "2a554442,4442255a"})
    void sorts(String s, String expected) {
        assertEquals(expected, solution.frequencySort(s));
    }
}
''',
trace=r'''
function run(s) {
  const cnt = {}; [...s].forEach(c => (cnt[c] = (cnt[c] || 0) + 1));
  A.step('Count every character.', A.chars('s', s), A.map('counts', cnt));
  const buckets = Array.from({ length: s.length + 1 }, () => []);
  Object.keys(cnt).sort().forEach(c => buckets[cnt[c]].push(c));
  A.step('Bucket i holds the characters that appear exactly i times.', A.arr('buckets', buckets.map(b => b.join('') || '·')));
  let out = '';
  for (let f = s.length; f > 0; f--) if (buckets[f].length) { buckets[f].forEach(c => (out += c.repeat(f))); A.step(`Bucket ${f}: write ${buckets[f].map(c => `'${c}' × ${f}`).join(', ')}.`, A.arr('buckets', buckets.map(b => b.join('') || '·'), { hl: { [f]: 'cur' } }), A.chars('output', out)); }
  A.step(`Result: "${out}".`, A.text('Result', out, 'ok'));
}
A.scenario('Example', '"tree"', () => run('tree'));
A.scenario('Mixed', '"2a554442"', () => run('2a554442'));
'''),

P(num=454, slug="4sum-ii", title="4Sum II", diff="Medium", topic="Hash Map", cls="FourSumII",
idea="Meet in the middle: count every a + b, then look up −(c + d).",
vname="Pair sums in a hash map",
spec=r'''
Given four arrays of length `n`, count tuples `(i, j, k, l)` with `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`.

**Example**
```
nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2] → 2
nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0] → 1
```

**Constraints**
* `1 <= n <= 200`, `-2^28 <= values <= 2^28`
''',
approach=r'''
**Split in halves.** Store how often each sum `a + b` occurs (from the first two arrays) in a `MyHashMap`. For each `c + d` from the other
two, add the count of `-(c + d)`.

* Time: **O(n²)** — two double loops.
* Space: **O(n²)** — up to `n²` distinct sums.
''',
tc="n2", sc="n2",
java=r'''
public class FourSumII {

    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        MyHashMap<Integer, Integer> pairs = new MyHashMap<>();
        for (int a : nums1) for (int b : nums2) pairs.merge(a + b, 1, Integer::sum);
        int count = 0;
        for (int c : nums3) for (int d : nums4) count += pairs.getOrDefault(-(c + d), 0);
        return count;
    }
}
''',
test=r'''
class FourSumIITest {

    private final FourSumII solution = new FourSumII();

    @Test
    void examples() {
        assertEquals(2, solution.fourSumCount(new int[]{1, 2}, new int[]{-2, -1}, new int[]{-1, 2}, new int[]{0, 2}));
        assertEquals(1, solution.fourSumCount(new int[]{0}, new int[]{0}, new int[]{0}, new int[]{0}));
        assertEquals(16, solution.fourSumCount(new int[]{0, 0}, new int[]{0, 0}, new int[]{0, 0}, new int[]{0, 0}));
        assertEquals(0, solution.fourSumCount(new int[]{1}, new int[]{1}, new int[]{1}, new int[]{1}));
    }
}
''',
trace=r'''
function run(A1, A2, A3, A4) {
  const m = new Map();
  A.step('Count every sum a + b from the first two arrays.', A.arr('nums1', A1), A.arr('nums2', A2));
  A1.forEach(a => A2.forEach(b => m.set(a + b, (m.get(a + b) || 0) + 1)));
  A.step(`${m.size} distinct pair sums.`, A.hashTable('a + b → count', m));
  let count = 0;
  A3.forEach(c => A4.forEach(d => { const need = -(c + d), got = m.get(need) || 0; count += got; A.step(`c + d = ${c} + ${d} = ${c + d}; need a + b = ${need}: ${got} way${got === 1 ? '' : 's'}.`, A.hashTable('a + b → count', m, { hl: need }), A.vars({ count })); }));
  A.step(`${count} zero-sum tuples.`, A.text('Result', count, 'ok'));
}
A.scenario('Example', '[1,2] [-2,-1] [-1,2] [0,2]', () => run([1, 2], [-2, -1], [-1, 2], [0, 2]));
''',
variants=[dict(
name="Try every tuple",
idea="Four nested loops over all n⁴ tuples.",
approach=r'''
**Brute force.** Check every `(i, j, k, l)`.

* Time: **O(n⁴)**.
* Space: **O(1)**.
''',
tc="exp", sc="1",
java=r'''
public class FourSumII {

    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        int count = 0;
        for (int a : nums1) for (int b : nums2) for (int c : nums3) for (int d : nums4) if (a + b + c + d == 0) count++;
        return count;
    }
}
''',
trace=r'''
function run(A1, A2, A3, A4) {
  let count = 0;
  A.step(`Try all ${A1.length * A2.length * A3.length * A4.length} tuples.`, A.arr('nums1', A1), A.arr('nums2', A2), A.arr('nums3', A3), A.arr('nums4', A4));
  A1.forEach(a => A2.forEach(b => A3.forEach(c => A4.forEach(d => { const s = a + b + c + d; if (s === 0) count++; A.step(`${a} + ${b} + ${c} + ${d} = ${s}${s === 0 ? ': count it' : ''}.`, A.vars({ count })); }))));
  A.step(`${count} zero-sum tuples.`, A.text('Result', count, 'ok'));
}
A.scenario('Example', '[1,2] [-2,-1] [-1,2] [0,2]', () => run([1, 2], [-2, -1], [-1, 2], [0, 2]));
''')]),

P(num=455, slug="assign-cookies", title="Assign Cookies", diff="Easy", topic="Greedy", cls="AssignCookies",
idea="Sort both; give each cookie, smallest first, to the least greedy child it can satisfy.",
vname="Sort and two pointers",
spec=r'''
Child `i` is content with a cookie of size at least `g[i]`. Cookie `j` has size `s[j]`. Each child gets at most one cookie. Return the
maximum number of content children.

**Example**
```
g = [1,2,3], s = [1,1]   → 1
g = [1,2],   s = [1,2,3] → 2
```

**Constraints**
* `1 <= g.length <= 3 * 10^4`, `0 <= s.length <= 3 * 10^4`
''',
approach=r'''
**Greedy.** Sort both arrays. Walk the cookies from smallest; if the current cookie satisfies the least greedy unsatisfied child, give it
and move to the next child. A cookie too small for that child is too small for everyone left, so skip it.

* Time: **O(n log n + m log m)** — sorting.
* Space: **O(1)** — besides sorting.
''',
tc="nlogn", sc="1",
java=r'''
public class AssignCookies {

    public int findContentChildren(int[] g, int[] s) {
        int[] greed = g.clone(), size = s.clone();
        Arrays.sort(greed);
        Arrays.sort(size);
        int child = 0;
        for (int j = 0; j < size.length && child < greed.length; j++) if (size[j] >= greed[child]) child++;
        return child;
    }
}
''',
test=r'''
class AssignCookiesTest {

    private final AssignCookies solution = new AssignCookies();

    @Test
    void examples() {
        assertEquals(1, solution.findContentChildren(new int[]{1, 2, 3}, new int[]{1, 1}));
        assertEquals(2, solution.findContentChildren(new int[]{1, 2}, new int[]{1, 2, 3}));
        assertEquals(0, solution.findContentChildren(new int[]{1}, new int[]{}));
        assertEquals(2, solution.findContentChildren(new int[]{10, 9, 8, 7}, new int[]{5, 6, 7, 8}));
    }
}
''',
trace=r'''
function run(g, s) {
  const G = g.slice().sort((a, b) => a - b), S = s.slice().sort((a, b) => a - b), hlG = {}, hlS = {}; let child = 0;
  A.step('Sort children by greed and cookies by size.', A.arr('greed', G), A.arr('cookies', S));
  for (let j = 0; j < S.length && child < G.length; j++) {
    if (S[j] >= G[child]) { hlG[child] = 'ok'; hlS[j] = 'ok'; A.step(`Cookie ${S[j]} ≥ greed ${G[child]}: that child is content.`, A.arr('greed', G, { hl: hlG }), A.arr('cookies', S, { hl: hlS }), A.vars({ content: child + 1 })); child++; }
    else { hlS[j] = 'bad'; A.step(`Cookie ${S[j]} < greed ${G[child]}: too small for anyone left. Skip it.`, A.arr('greed', G, { hl: { ...hlG, [child]: 'cur' } }), A.arr('cookies', S, { hl: hlS }), A.vars({ content: child })); }
  }
  A.step(`${child} content child${child === 1 ? '' : 'ren'}.`, A.text('Result', child, 'ok'));
}
A.scenario('Not enough', 'g = [1,2,3], s = [1,1]', () => run([1, 2, 3], [1, 1]));
A.scenario('Skip small cookies', 'g = [10,9,8,7], s = [5,6,7,8]', () => run([10, 9, 8, 7], [5, 6, 7, 8]));
'''),

P(num=456, slug="132-pattern", title="132 Pattern", diff="Medium", topic="Monotonic Stack", cls="Pattern132",
idea="Scan from the right with a decreasing stack; values popped become the best '2', and any smaller element is the '1'.",
vname="Monotonic stack from the right",
spec=r'''
Return `true` if there are indices `i < j < k` with `nums[i] < nums[k] < nums[j]` (a "132" shape).

**Example**
```
[1,2,3,4]  → false
[3,1,4,2]  → true    (1, 4, 2)
[-1,3,2,0] → true
```

**Constraints**
* `1 <= nums.length <= 2 * 10^5`
''',
approach=r'''
**Right to left.** Keep a stack of candidates for the "3", decreasing from bottom to top, and `third`, the largest value that has been
popped (a valid "2": something bigger sits to its left). When a new value is bigger than the top, pop: each popped value has a bigger
"3" left of it, so it can serve as "2". If a value is smaller than `third`, it is the "1".

* Time: **O(n)** — each value is pushed and popped once.
* Space: **O(n)** — the stack.
''',
tc="n", sc="n",
java=r'''
public class Pattern132 {

    public boolean find132pattern(int[] nums) {
        Deque<Integer> stack = new ArrayDeque<>();
        long third = Long.MIN_VALUE;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] < third) return true;
            while (!stack.isEmpty() && stack.peek() < nums[i]) third = stack.pop();
            stack.push(nums[i]);
        }
        return false;
    }
}
''',
test=r'''
class Pattern132Test {

    private final Pattern132 solution = new Pattern132();

    @Test
    void examples() {
        assertFalse(solution.find132pattern(new int[]{1, 2, 3, 4}));
        assertTrue(solution.find132pattern(new int[]{3, 1, 4, 2}));
        assertTrue(solution.find132pattern(new int[]{-1, 3, 2, 0}));
        assertFalse(solution.find132pattern(new int[]{1, 0, 1, -4, -3}));
        assertTrue(solution.find132pattern(new int[]{3, 5, 0, 3, 4}));
        assertFalse(solution.find132pattern(new int[]{1}));
        assertFalse(solution.find132pattern(new int[]{Integer.MIN_VALUE, Integer.MIN_VALUE}));
    }
}
''',
trace=r'''
function run(nums) {
  const st = []; let third = -Infinity;
  A.step('Scan from the right. The stack holds "3" candidates; third is the best "2" found so far (it has a bigger value to its left).', A.arr('nums', nums), A.stack('stack', st), A.vars({ third: '−∞' }));
  for (let i = nums.length - 1; i >= 0; i--) {
    const v = nums[i];
    if (v < third) { A.step(`${v} < third (${third}): ${v} is the "1". Found a 132 pattern.`, A.arr('nums', nums, { hl: { [i]: 'ok' } }), A.vars({ third }), A.text('Result', 'true', 'ok')); return; }
    const popped = [];
    while (st.length && st[st.length - 1] < v) { third = st.pop(); popped.push(third); }
    st.push(v);
    A.step(popped.length ? `${v} is bigger than ${popped.join(', ')}: they can be "2" with ${v} as "3". third = ${third}.` : `Push ${v}.`, A.arr('nums', nums, { hl: { [i]: 'cur' } }), A.stack('stack', st), A.vars({ third: third === -Infinity ? '−∞' : third }));
  }
  A.step('No value was smaller than a valid "2".', A.text('Result', 'false', 'bad'));
}
A.scenario('Found', '[3,1,4,2]', () => run([3, 1, 4, 2]));
A.scenario('Increasing', '[1,2,3,4]', () => run([1, 2, 3, 4]));
''',
variants=[dict(
name="Prefix minimum, check every pair",
idea="For each j, the best '1' is the minimum to its left; look for a k with that minimum < nums[k] < nums[j].",
approach=r'''
**Fix the middle.** Track the smallest value before `j`. For each later `k`, check `min < nums[k] < nums[j]`.

* Time: **O(n²)**.
* Space: **O(1)**.
''',
tc="n2", sc="1",
java=r'''
public class Pattern132 {

    public boolean find132pattern(int[] nums) {
        int min = Integer.MAX_VALUE;
        for (int j = 0; j < nums.length; j++) {
            min = Math.min(min, nums[j]);
            for (int k = j + 1; k < nums.length; k++) if (min < nums[k] && nums[k] < nums[j]) return true;
        }
        return false;
    }
}
''',
trace=r'''
function run(nums) {
  let min = Infinity;
  A.step('For each middle j, use the smallest value seen so far as the "1".', A.arr('nums', nums));
  for (let j = 0; j < nums.length; j++) {
    min = Math.min(min, nums[j]);
    for (let k = j + 1; k < nums.length; k++) {
      const ok = min < nums[k] && nums[k] < nums[j];
      A.step(`j = ${j} (${nums[j]}), min ${min}, k = ${k} (${nums[k]}): ${ok ? 'fits between. Found.' : 'does not fit.'}`, A.arr('nums', nums, { hl: { [j]: 'cur', [k]: ok ? 'ok' : 'bad' } }));
      if (ok) { A.step('A 132 pattern exists.', A.text('Result', 'true', 'ok')); return; }
    }
  }
  A.step('No pattern.', A.text('Result', 'false', 'bad'));
}
A.scenario('Found', '[3,1,4,2]', () => run([3, 1, 4, 2]));
''')]),

P(num=459, slug="repeated-substring-pattern", title="Repeated Substring Pattern", diff="Easy", topic="String", cls="RepeatedSubstringPattern",
idea="The KMP failure function gives the shortest period; the string repeats iff that period divides its length.",
vname="KMP prefix function",
spec=r'''
Return `true` if `s` can be built by repeating one of its substrings two or more times.

**Example**
```
"abab"         → true   ("ab" × 2)
"aba"          → false
"abcabcabcabc" → true
```

**Constraints**
* `1 <= s.length <= 10^4`
''',
approach=r'''
**Shortest period.** `lps[i]` is the length of the longest proper prefix of `s[0..i]` that is also a suffix. For the whole string,
`p = n - lps[n-1]` is its shortest period. `s` is a repetition iff `lps[n-1] > 0` and `n % p == 0`.

* Time: **O(n)** — building `lps`.
* Space: **O(n)** — the table.
''',
tc="n", sc="n",
java=r'''
public class RepeatedSubstringPattern {

    public boolean repeatedSubstringPattern(String s) {
        int n = s.length();
        int[] lps = new int[n];
        for (int i = 1, len = 0; i < n; ) {
            if (s.charAt(i) == s.charAt(len)) lps[i++] = ++len;
            else if (len > 0) len = lps[len - 1];
            else lps[i++] = 0;
        }
        int border = lps[n - 1];
        return border > 0 && n % (n - border) == 0;
    }
}
''',
test=r'''
class RepeatedSubstringPatternTest {

    private final RepeatedSubstringPattern solution = new RepeatedSubstringPattern();

    @ParameterizedTest
    @CsvSource({"abab,true", "aba,false", "abcabcabcabc,true", "a,false", "aa,true", "abac,false", "abaababaab,true", "aabaaba,false"})
    void check(String s, boolean expected) {
        assertEquals(expected, solution.repeatedSubstringPattern(s));
    }
}
''',
trace=r'''
function run(s) {
  const n = s.length, lps = new Array(n).fill(0);
  A.step('lps[i]: the longest proper prefix of s[0..i] that is also its suffix.', A.chars('s', s), A.arr('lps', lps));
  for (let i = 1, len = 0; i < n;) {
    if (s[i] === s[len]) { lps[i] = ++len; A.step(`s[${i}] = '${s[i]}' matches s[${len - 1}]: lps[${i}] = ${len}.`, A.chars('s', s, { hl: { [i]: 'ok', [len - 1]: 'cur' } }), A.arr('lps', lps, { hl: { [i]: 'ok' } })); i++; }
    else if (len) len = lps[len - 1];
    else { lps[i] = 0; A.step(`s[${i}] = '${s[i]}' starts no border: lps[${i}] = 0.`, A.chars('s', s, { hl: { [i]: 'bad' } }), A.arr('lps', lps, { hl: { [i]: 'bad' } })); i++; }
  }
  const b = lps[n - 1], p = n - b, ok = b > 0 && n % p === 0;
  A.step(`Border of the whole string: ${b}, so the shortest period is ${n} − ${b} = ${p}.`, A.chars('s', s, { range: [0, p - 1] }), A.vars({ border: b, period: p, length: n }));
  A.step(ok ? `${n} is a multiple of ${p}: "${s.slice(0, p)}" repeated ${n / p} times.` : `${b === 0 ? 'No border at all' : `${n} is not a multiple of ${p}`}, so s is not a repetition.`, A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('Repeats', '"abcabcabc"', () => run('abcabcabc'));
A.scenario('Does not repeat', '"abaababa"', () => run('abaababa'));
''',
variants=[dict(
name="Doubled-string trick",
idea="s is a repetition iff it appears inside (s + s) with the first and last characters removed.",
approach=r'''
**Rotation.** If `s` is built from a repeated block, rotating it by the block length gives `s` back, so `s` occurs inside `s + s` at a
position other than `0` and `n`. Cutting off the first and last characters removes exactly those two trivial matches.

* Time: **O(n²)** — `String.contains` worst case (O(n) with a linear matcher).
* Space: **O(n)** — the doubled string.
''',
tc="n2", sc="n",
java=r'''
public class RepeatedSubstringPattern {

    public boolean repeatedSubstringPattern(String s) {
        String doubled = s + s;
        return doubled.substring(1, doubled.length() - 1).contains(s);
    }
}
''',
trace=r'''
function run(s) {
  const d = s + s, cut = d.slice(1, -1), at = cut.indexOf(s);
  A.step('Double the string.', A.chars('s + s', d));
  A.step('Drop the first and last characters, removing the two trivial copies of s.', A.chars('trimmed', cut));
  A.step(at >= 0 ? `s appears at position ${at + 1} of s + s: rotating by ${at + 1} gives s back.` : 's does not appear: no rotation reproduces it.', A.chars('trimmed', cut, at >= 0 ? { range: [at, at + s.length - 1] } : {}));
  A.step(at >= 0 ? 'So s is a repeated pattern.' : 'So s is not a repeated pattern.', A.text('Result', String(at >= 0), at >= 0 ? 'ok' : 'bad'));
}
A.scenario('Repeats', '"abab"', () => run('abab'));
A.scenario('Does not repeat', '"aba"', () => run('aba'));
''')]),

P(num=461, slug="hamming-distance", title="Hamming Distance", diff="Easy", topic="Bit Manipulation", cls="HammingDistance",
idea="XOR leaves 1s exactly where the bits differ; count them.",
vname="XOR and count bits",
spec=r'''
Return the number of bit positions where `x` and `y` differ.

**Example**
```
x = 1, y = 4 → 2   (0001 vs 0100)
x = 3, y = 1 → 1
```

**Constraints**
* `0 <= x, y <= 2^31 - 1`
''',
approach=r'''
**Kernighan's trick.** `z = x ^ y` has a 1 at each differing position. `z &= z - 1` clears the lowest 1-bit; count how many times until
`z` is 0.

* Time: **O(1)** — at most 31 iterations.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class HammingDistance {

    public int hammingDistance(int x, int y) {
        int z = x ^ y, count = 0;
        while (z != 0) {
            z &= z - 1;
            count++;
        }
        return count;
    }
}
''',
test=r'''
class HammingDistanceTest {

    private final HammingDistance solution = new HammingDistance();

    @ParameterizedTest
    @CsvSource({"1,4,2", "3,1,1", "0,0,0", "0,2147483647,31", "7,7,0", "93,73,2"})
    void distance(int x, int y, int expected) {
        assertEquals(expected, solution.hammingDistance(x, y));
    }
}
''',
trace=r'''
function run(x, y) {
  const b = v => v.toString(2).padStart(8, '0');
  A.step(`Compare ${x} and ${y} bit by bit.`, A.chars(`x = ${x}`, b(x)), A.chars(`y = ${y}`, b(y)));
  let z = x ^ y;
  A.step(`x ^ y = ${z}: a 1 wherever the bits differ.`, A.chars('x ^ y', b(z), { hl: Object.fromEntries([...b(z)].map((c, i) => [i, c === '1' ? 'cur' : ''])) }));
  let c = 0;
  while (z) { const before = z; z &= z - 1; c++; A.step(`Clear the lowest 1-bit: ${before} → ${z}. Count = ${c}.`, A.chars('z', b(z)), A.vars({ count: c })); }
  A.step(`They differ in ${c} position${c === 1 ? '' : 's'}.`, A.text('Result', c, 'ok'));
}
A.scenario('Example', 'x = 1, y = 4', () => run(1, 4));
A.scenario('More bits', 'x = 93, y = 73', () => run(93, 73));
'''),

P(num=463, slug="island-perimeter", title="Island Perimeter", diff="Easy", topic="Matrix", cls="IslandPerimeter",
idea="Each land cell adds 4 edges; each pair of touching land cells hides 2 of them.",
vname="Count cells and shared edges",
spec=r'''
A grid of `1` (land) and `0` (water) contains exactly one island with no lakes. Return the island's perimeter.

**Example**
```
0 1 0 0
1 1 1 0    → 16
0 1 0 0
1 1 0 0
```

**Constraints**
* `1 <= rows, cols <= 100`
''',
approach=r'''
**Edges.** Every land cell has 4 sides. Each shared side between two land cells is counted once by each and is not part of the
perimeter. Count land cells and neighbours above and to the left: `4 · land - 2 · shared`.

* Time: **O(mn)**.
* Space: **O(1)**.
''',
tc="n2", sc="1",
java=r'''
public class IslandPerimeter {

    public int islandPerimeter(int[][] grid) {
        int land = 0, shared = 0;
        for (int r = 0; r < grid.length; r++)
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] != 1) continue;
                land++;
                if (r > 0 && grid[r - 1][c] == 1) shared++;
                if (c > 0 && grid[r][c - 1] == 1) shared++;
            }
        return 4 * land - 2 * shared;
    }
}
''',
test=r'''
class IslandPerimeterTest {

    private final IslandPerimeter solution = new IslandPerimeter();

    @Test
    void examples() {
        assertEquals(16, solution.islandPerimeter(new int[][]{{0, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 0, 0}, {1, 1, 0, 0}}));
        assertEquals(4, solution.islandPerimeter(new int[][]{{1}}));
        assertEquals(4, solution.islandPerimeter(new int[][]{{1, 0}}));
        assertEquals(8, solution.islandPerimeter(new int[][]{{1, 1}, {1, 1}}));
    }
}
''',
trace=r'''
function run(g) {
  let land = 0, shared = 0; const hl = {};
  A.step('Each land cell starts with 4 sides; every side shared with another land cell is not on the perimeter.', A.grid('grid', g));
  for (let r = 0; r < g.length; r++) for (let c = 0; c < g[0].length; c++) {
    if (g[r][c] !== 1) continue;
    land++; const up = r > 0 && g[r - 1][c] === 1, left = c > 0 && g[r][c - 1] === 1; shared += up + left; hl[`${r},${c}`] = 'ok';
    A.step(`Land at (${r},${c})${up || left ? `, touching land ${[up ? 'above' : '', left ? 'to the left' : ''].filter(Boolean).join(' and ')}` : ''}.`, A.grid('grid', g, { hl: { ...hl, [`${r},${c}`]: 'cur' } }), A.vars({ land, shared }));
  }
  A.step(`4 × ${land} − 2 × ${shared} = ${4 * land - 2 * shared}.`, A.text('Result', 4 * land - 2 * shared, 'ok'));
}
A.scenario('Example', '4 × 4 island', () => run([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]));
'''),
]
