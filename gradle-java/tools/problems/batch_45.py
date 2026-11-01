PROBLEMS = [
P(num=622, slug="design-circular-queue", title="Design Circular Queue", diff="Medium", topic="Design", cls="MyCircularQueue",
idea="A fixed array with a head index and a size; the tail position is (head + size) mod capacity.",
vname="Array with head and size",
spec=r'''
Implement a fixed-capacity circular queue:

* `MyCircularQueue(int k)`
* `boolean enQueue(int value)`, `boolean deQueue()` — return `false` when full / empty.
* `int Front()`, `int Rear()` — return `-1` when empty.
* `boolean isEmpty()`, `boolean isFull()`

**Example**
```
k = 3: enQueue(1) true, enQueue(2) true, enQueue(3) true, enQueue(4) false,
Rear() 3, isFull() true, deQueue() true, enQueue(4) true, Rear() 4
```

**Constraints**
* `1 <= k <= 1000`, up to 3000 calls
''',
approach=r'''
**Ring buffer.** Store `head` (index of the front) and `size`. The next free slot is `(head + size) % k` and the rear is
`(head + size - 1) % k`. Dequeue just moves `head` forward. Tracking `size` separates "full" from "empty", which both have head == tail.

* Time: **O(1)** — every operation.
* Space: **O(k)** — the array.
''',
tc="1", sc="n",
java=r'''
public class MyCircularQueue {

    private final int[] data;
    private int head, size;

    public MyCircularQueue(int k) {
        data = new int[k];
    }

    public boolean enQueue(int value) {
        if (isFull()) return false;
        data[(head + size) % data.length] = value;
        size++;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) return false;
        head = (head + 1) % data.length;
        size--;
        return true;
    }

    public int Front() {
        return isEmpty() ? -1 : data[head];
    }

    public int Rear() {
        return isEmpty() ? -1 : data[(head + size - 1) % data.length];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == data.length;
    }
}
''',
test=r'''
class MyCircularQueueTest {

    @Test
    void example() {
        MyCircularQueue q = new MyCircularQueue(3);
        assertTrue(q.enQueue(1));
        assertTrue(q.enQueue(2));
        assertTrue(q.enQueue(3));
        assertFalse(q.enQueue(4));
        assertEquals(3, q.Rear());
        assertTrue(q.isFull());
        assertTrue(q.deQueue());
        assertTrue(q.enQueue(4));
        assertEquals(4, q.Rear());
        assertEquals(2, q.Front());
    }

    @Test
    void emptyQueue() {
        MyCircularQueue q = new MyCircularQueue(1);
        assertTrue(q.isEmpty());
        assertEquals(-1, q.Front());
        assertEquals(-1, q.Rear());
        assertFalse(q.deQueue());
        assertTrue(q.enQueue(9));
        assertTrue(q.isFull());
        assertTrue(q.deQueue());
        assertTrue(q.isEmpty());
    }
}
''',
trace=r'''
function run(k, ops) {
  const d = new Array(k).fill('·'); let head = 0, size = 0;
  const view = () => { const ptr = {}; ptr[head] = 'head'; const t = (head + size) % k; ptr[t] = ptr[t] ? 'head/next' : 'next'; const hl = {}; for (let i = 0; i < size; i++) hl[(head + i) % k] = 'ok'; return A.arr('ring', d, { hl, ptr }); };
  A.step(`A ring of ${k} slots. 'next' is (head + size) mod ${k}.`, view(), A.vars({ head, size }));
  ops.forEach(([op, v]) => {
    let r;
    if (op === 'enQueue') { if (size === k) r = false; else { d[(head + size) % k] = v; size++; r = true; } }
    else if (op === 'deQueue') { if (!size) r = false; else { d[head] = '·'; head = (head + 1) % k; size--; r = true; } }
    else if (op === 'Rear') r = size ? d[(head + size - 1) % k] : -1;
    else r = size === k;
    A.step(`${op}(${v ?? ''}) → ${r}.${op === 'enQueue' && r ? ` Wrote ${v}.` : ''}${op === 'enQueue' && !r ? ' The ring is full.' : ''}${op === 'deQueue' && r ? ' head moves forward.' : ''}`, view(), A.vars({ head, size }));
  });
}
A.scenario('Wrap around', 'k = 3', () => run(3, [['enQueue', 1], ['enQueue', 2], ['enQueue', 3], ['enQueue', 4], ['Rear'], ['deQueue'], ['enQueue', 4], ['Rear']]));
'''),

P(num=650, slug="2-keys-keyboard", title="2 Keys Keyboard", diff="Medium", topic="Math", cls="TwoKeysKeyboard",
idea="Copying d letters and pasting them d − 1 more times multiplies the count by d at a cost of d, so the answer is the sum of the prime factors.",
vname="Sum of prime factors",
spec=r'''
The screen starts with one `'A'`. Each step is either **Copy All** (copy everything on screen) or **Paste** (append the last copy). Return
the minimum number of steps to get exactly `n` letters.

**Example**
```
n = 3 → 3   (copy, paste, paste)
n = 1 → 0
n = 6 → 5   (copy, paste → 2; copy, paste, paste → 6)
```

**Constraints**
* `1 <= n <= 1000`
''',
approach=r'''
**Factorisation.** A copy followed by `d - 1` pastes multiplies the length by `d` and costs `d` steps. So any plan is a factorisation
`n = d₁ · d₂ · …` with cost `d₁ + d₂ + …`. Splitting a composite `d = a · b` never costs more (`a + b <= a · b`), so the minimum is the
sum of the prime factors (with multiplicity).

* Time: **O(√n)** — trial division.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class TwoKeysKeyboard {

    public int minSteps(int n) {
        int steps = 0;
        for (int d = 2; d * d <= n; d++)
            while (n % d == 0) {
                steps += d;
                n /= d;
            }
        if (n > 1) steps += n;
        return steps;
    }
}
''',
test=r'''
class TwoKeysKeyboardTest {

    private final TwoKeysKeyboard solution = new TwoKeysKeyboard();

    @ParameterizedTest
    @CsvSource({"1,0", "2,2", "3,3", "4,4", "6,5", "9,6", "997,997", "1000,21"})
    void steps(int n, int expected) {
        assertEquals(expected, solution.minSteps(n));
    }
}
''',
trace=r'''
function run(n) {
  A.step(`Copy once, paste d − 1 times: the count is multiplied by d for d steps. So split ${n} into prime factors.`, A.vars({ n }));
  let m = n, steps = 0; const f = [];
  for (let d = 2; d * d <= m; d++) while (m % d === 0) { f.push(d); steps += d; m /= d; A.step(`${d} divides it: copy + ${d - 1} paste${d > 2 ? 's' : ''} (${d} steps). ${m} left to build up.`, A.arr('factors', f, { hl: { [f.length - 1]: 'cur' } }), A.vars({ steps, left: m })); }
  if (m > 1) { f.push(m); steps += m; A.step(`${m} is prime: copy + ${m - 1} pastes (${m} steps).`, A.arr('factors', f, { hl: { [f.length - 1]: 'cur' } }), A.vars({ steps })); }
  A.step(`${f.length ? f.join(' + ') : '0'} = ${steps} steps.`, A.text('Result', steps, 'ok'));
}
A.scenario('n = 12', 'n = 12', () => run(12));
A.scenario('n = 9', 'n = 9', () => run(9));
''',
variants=[dict(
name="Dynamic programming over divisors",
idea="best[i] = min over divisors d of i of best[d] + i / d: reach d, then copy and paste up to i.",
approach=r'''
**DP.** To reach `i` the last copy happened at some length `d` dividing `i`; then one copy and `i/d - 1` pastes follow. So
`best[i] = min(best[d] + i / d)` over divisors `d < i`, with `best[1] = 0`.

* Time: **O(n²)** — trying every smaller length for each `i`.
* Space: **O(n)** — the table.
''',
tc="n2", sc="n",
java=r'''
public class TwoKeysKeyboard {

    public int minSteps(int n) {
        int[] best = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            best[i] = i;
            for (int d = 2; d < i; d++) if (i % d == 0) best[i] = Math.min(best[i], best[d] + i / d);
        }
        return best[n];
    }
}
''',
trace=r'''
function run(n) {
  const best = new Array(n + 1).fill(0);
  A.step('best[1] = 0: one A is already there.', A.arr('best', best));
  for (let i = 2; i <= n; i++) {
    best[i] = i; let from = 1;
    for (let d = 2; d < i; d++) if (i % d === 0 && best[d] + i / d < best[i]) { best[i] = best[d] + i / d; from = d; }
    A.step(`best[${i}] = ${best[i]}: reach ${from}, then copy and paste ${i / from - 1} time${i / from - 1 === 1 ? '' : 's'}.`, A.arr('best', best, { hl: { [i]: 'ok', [from]: 'cur' } }));
  }
  A.step(`Answer: ${best[n]}.`, A.text('Result', best[n], 'ok'));
}
A.scenario('n = 12', 'n = 12', () => run(12));
''')]),

P(num=673, slug="number-of-longest-increasing-subsequence", title="Number of Longest Increasing Subsequence", diff="Medium", topic="Dynamic Programming", cls="NumberOfLIS",
idea="Alongside the LIS length ending at each index, keep how many subsequences achieve it.",
vname="Length and count DP",
spec=r'''
Return the number of **longest strictly increasing** subsequences of `nums`.

**Example**
```
[1,3,5,4,7] → 2   ([1,3,4,7] and [1,3,5,7])
[2,2,2,2,2] → 5   (each single element)
```

**Constraints**
* `1 <= nums.length <= 2000`
''',
approach=r'''
**Two arrays.** `len[i]` is the longest increasing subsequence ending at `i`, `cnt[i]` how many reach that length. For each `j < i` with
`nums[j] < nums[i]`: a longer chain `len[j] + 1 > len[i]` replaces the count with `cnt[j]`; an equal one adds `cnt[j]`. Finally add up the
counts of all positions whose length is the maximum.

* Time: **O(n²)**.
* Space: **O(n)**.
''',
tc="n2", sc="n",
java=r'''
public class NumberOfLIS {

    public int findNumberOfLIS(int[] nums) {
        int n = nums.length, best = 0, total = 0;
        int[] len = new int[n], cnt = new int[n];
        for (int i = 0; i < n; i++) {
            len[i] = 1;
            cnt[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] >= nums[i]) continue;
                if (len[j] + 1 > len[i]) {
                    len[i] = len[j] + 1;
                    cnt[i] = cnt[j];
                } else if (len[j] + 1 == len[i]) cnt[i] += cnt[j];
            }
            if (len[i] > best) {
                best = len[i];
                total = cnt[i];
            } else if (len[i] == best) total += cnt[i];
        }
        return total;
    }
}
''',
test=r'''
class NumberOfLISTest {

    private final NumberOfLIS solution = new NumberOfLIS();

    @Test
    void examples() {
        assertEquals(2, solution.findNumberOfLIS(new int[]{1, 3, 5, 4, 7}));
        assertEquals(5, solution.findNumberOfLIS(new int[]{2, 2, 2, 2, 2}));
        assertEquals(3, solution.findNumberOfLIS(new int[]{1, 2, 4, 3, 5, 4, 7, 2}));
        assertEquals(1, solution.findNumberOfLIS(new int[]{7}));
    }
}
''',
trace=r'''
function run(nums) {
  const n = nums.length, len = new Array(n).fill(1), cnt = new Array(n).fill(1);
  A.step('len[i]: longest increasing subsequence ending at i. cnt[i]: how many reach that length.', A.arr('nums', nums), A.arr('len', len), A.arr('cnt', cnt));
  for (let i = 1; i < n; i++) {
    const hl = { [i]: 'ok' };
    for (let j = 0; j < i; j++) { if (nums[j] >= nums[i]) continue; hl[j] = 'cur'; if (len[j] + 1 > len[i]) { len[i] = len[j] + 1; cnt[i] = cnt[j]; } else if (len[j] + 1 === len[i]) cnt[i] += cnt[j]; }
    A.step(`${nums[i]}: extends the smaller values before it (orange). len = ${len[i]}, ways = ${cnt[i]}.`, A.arr('nums', nums, { hl }), A.arr('len', len, { hl: { [i]: 'ok' } }), A.arr('cnt', cnt, { hl: { [i]: 'ok' } }));
  }
  const best = Math.max(...len), total = cnt.reduce((s, c, i) => s + (len[i] === best ? c : 0), 0);
  A.step(`The longest length is ${best}. Add the counts where len = ${best}: ${total}.`, A.arr('len', len, { hl: Object.fromEntries(len.map((l, i) => [i, l === best ? 'ok' : 'dim'])) }), A.text('Result', total, 'ok'));
}
A.scenario('Example', '[1,3,5,4,7]', () => run([1, 3, 5, 4, 7]));
A.scenario('Three ways', '[1,2,4,3,5,4,7,2]', () => run([1, 2, 4, 3, 5, 4, 7, 2]));
'''),

P(num=687, slug="longest-univalue-path", title="Longest Univalue Path", diff="Medium", topic="Binary Tree DFS", cls="LongestUnivaluePath",
idea="Each node returns the longest same-value arm going down; a path can bend through a node using two arms.",
vname="DFS returning arm lengths", helpers=["TreeNode"],
spec=r'''
Return the length (number of **edges**) of the longest path in a binary tree where every node has the same value. The path need not pass
through the root.

**Example**
```
[5,4,5,1,1,null,5] → 2
[1,4,5,4,4,null,5] → 2
```

**Constraints**
* `0 <= n <= 10^4`
''',
approach=r'''
**Arms.** `arm(node)` is the longest downward path of equal values starting at `node`. A child's arm counts (plus one edge) only if the
child has the same value. The best path bending at `node` uses both counted arms; record the maximum and return the longer arm.

* Time: **O(n)**.
* Space: **O(h)** — recursion depth.
''',
tc="n", sc="n",
java=r'''
public class LongestUnivaluePath {

    private int best;

    public int longestUnivaluePath(TreeNode root) {
        best = 0;
        arm(root);
        return best;
    }

    private int arm(TreeNode node) {
        if (node == null) return 0;
        int l = arm(node.left), r = arm(node.right);
        l = node.left != null && node.left.val == node.val ? l + 1 : 0;
        r = node.right != null && node.right.val == node.val ? r + 1 : 0;
        best = Math.max(best, l + r);
        return Math.max(l, r);
    }
}
''',
test=r'''
class LongestUnivaluePathTest {

    private final LongestUnivaluePath solution = new LongestUnivaluePath();

    @Test
    void examples() {
        assertEquals(2, solution.longestUnivaluePath(TreeNode.of(5, 4, 5, 1, 1, null, 5)));
        assertEquals(2, solution.longestUnivaluePath(TreeNode.of(1, 4, 5, 4, 4, null, 5)));
        assertEquals(0, solution.longestUnivaluePath(null));
        assertEquals(4, solution.longestUnivaluePath(TreeNode.of(1, 1, 1, 1, 1, 1)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {}; let best = 0;
  A.step('Each node reports its longest same-value arm downward. A path may bend at a node and use two arms.', A.tree('tree', root));
  (function arm(n) {
    if (!n) return 0;
    let l = arm(n.left), r = arm(n.right);
    l = n.left && n.left.val === n.val ? l + 1 : 0; r = n.right && n.right.val === n.val ? r + 1 : 0;
    const through = l + r; if (through > best) best = through;
    hl[n.id] = through ? 'ok' : 'dim';
    A.step(`Node ${n.val}: left arm ${l}, right arm ${r}; path bending here has ${through} edge${through === 1 ? '' : 's'}. Report arm ${Math.max(l, r)} upward.`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'cur' } }), A.vars({ best }));
    return Math.max(l, r);
  })(root);
  A.step(`Longest univalue path: ${best} edges.`, A.text('Result', best, 'ok'));
}
A.scenario('Bends', '[1,4,5,4,4,null,5]', () => run([1, 4, 5, 4, 4, null, 5]));
'''),

P(num=712, slug="minimum-ascii-delete-sum-for-two-strings", title="Minimum ASCII Delete Sum for Two Strings", diff="Medium", topic="Dynamic Programming", cls="MinimumDeleteSum",
idea="Edit-distance style DP where deleting a character costs its ASCII code.",
vname="DP over suffixes",
spec=r'''
Return the lowest total ASCII value of characters deleted from `s1` and `s2` to make the two strings equal.

**Example**
```
"sea", "eat"      → 231   (delete 's' = 115 and 't' = 116)
"delete", "leet"  → 403
```

**Constraints**
* `1 <= length <= 1000`, lower-case letters
''',
approach=r'''
**DP.** `dp[i][j]` is the cost to make the prefixes `s1[0..i)` and `s2[0..j)` equal. Equal last characters cost nothing:
`dp[i-1][j-1]`. Otherwise delete one of them: `min(dp[i-1][j] + s1[i-1], dp[i][j-1] + s2[j-1])`. The first row and column delete
everything.

* Time: **O(mn)**.
* Space: **O(n)** — one row.
''',
tc="n2", sc="n",
java=r'''
public class MinimumDeleteSum {

    public int minimumDeleteSum(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[] dp = new int[n + 1];
        for (int j = 1; j <= n; j++) dp[j] = dp[j - 1] + s2.charAt(j - 1);
        for (int i = 1; i <= m; i++) {
            int diag = dp[0];
            dp[0] += s1.charAt(i - 1);
            for (int j = 1; j <= n; j++) {
                int up = dp[j];
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) dp[j] = diag;
                else dp[j] = Math.min(dp[j] + s1.charAt(i - 1), dp[j - 1] + s2.charAt(j - 1));
                diag = up;
            }
        }
        return dp[n];
    }
}
''',
test=r'''
class MinimumDeleteSumTest {

    private final MinimumDeleteSum solution = new MinimumDeleteSum();

    @ParameterizedTest
    @CsvSource({"sea,eat,231", "delete,leet,403", "a,a,0", "a,b,195"})
    void cost(String a, String b, int expected) {
        assertEquals(expected, solution.minimumDeleteSum(a, b));
    }
}
''',
trace=r'''
function run(a, b) {
  const m = a.length, n = b.length, dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
  for (let j = 1; j <= n; j++) dp[0][j] = dp[0][j - 1] + b.charCodeAt(j - 1);
  for (let i = 1; i <= m; i++) dp[i][0] = dp[i - 1][0] + a.charCodeAt(i - 1);
  A.step('dp[i][j]: cheapest deletions to make the first i letters of s1 equal the first j of s2. Edges delete everything.', A.chars('s1', a), A.chars('s2', b), A.grid('dp', dp));
  for (let i = 1; i <= m; i++) {
    const hl = {};
    for (let j = 1; j <= n; j++) { const eq = a[i - 1] === b[j - 1]; dp[i][j] = eq ? dp[i - 1][j - 1] : Math.min(dp[i - 1][j] + a.charCodeAt(i - 1), dp[i][j - 1] + b.charCodeAt(j - 1)); hl[`${i},${j}`] = eq ? 'ok' : 'cur'; }
    A.step(`Row '${a[i - 1]}' (${a.charCodeAt(i - 1)}): matches (green) keep the diagonal; otherwise pay for one deletion.`, A.grid('dp', dp, { hl }));
  }
  A.step(`Minimum delete sum: ${dp[m][n]}.`, A.grid('dp', dp, { hl: { [`${m},${n}`]: 'ok' } }), A.text('Result', dp[m][n], 'ok'));
}
A.scenario('Example', '"sea" and "eat"', () => run('sea', 'eat'));
'''),

P(num=752, slug="open-the-lock", title="Open the Lock", diff="Medium", topic="Graph BFS", cls="OpenTheLock",
idea="Each of the 10,000 combinations is a node with 8 neighbours; BFS from 0000 avoiding dead ends.",
vname="BFS over combinations",
spec=r'''
A lock has 4 wheels with digits 0–9; one move turns one wheel one step up or down (wrapping 9 ↔ 0). It starts at `"0000"`. Some
combinations are **deadends** that jam the lock. Return the fewest moves to reach `target`, or `-1`.

**Example**
```
deadends = ["0201","0101","0102","1212","2002"], target = "0202" → 6
deadends = ["8888"], target = "0009" → 1
```

**Constraints**
* `1 <= deadends.length <= 500`; all strings have 4 digits
''',
approach=r'''
**Shortest path.** BFS from `"0000"` level by level. From each combination generate the 8 one-move neighbours, skipping deadends and
anything already seen (both kept in a `MyHashSet`). The level at which `target` appears is the answer. If `"0000"` itself is a deadend,
nothing is reachable.

* Time: **O(10⁴ · 8 · 4)** — every combination at most once, 8 neighbours of 4 characters.
* Space: **O(10⁴)** — the visited set and queue.
''',
tc="1", sc="1",
java=r'''
public class OpenTheLock {

    public int openLock(String[] deadends, String target) {
        MyHashSet<String> blocked = new MyHashSet<>();
        for (String d : deadends) blocked.add(d);
        if (blocked.contains("0000")) return -1;
        MyHashSet<String> seen = new MyHashSet<>();
        Deque<String> queue = new ArrayDeque<>(List.of("0000"));
        seen.add("0000");
        for (int moves = 0; !queue.isEmpty(); moves++) {
            for (int size = queue.size(); size > 0; size--) {
                String cur = queue.poll();
                if (cur.equals(target)) return moves;
                char[] c = cur.toCharArray();
                for (int w = 0; w < 4; w++) {
                    char orig = c[w];
                    for (int delta : new int[]{1, 9}) {
                        c[w] = (char) ('0' + (orig - '0' + delta) % 10);
                        String next = new String(c);
                        if (!blocked.contains(next) && seen.add(next)) queue.add(next);
                    }
                    c[w] = orig;
                }
            }
        }
        return -1;
    }
}
''',
test=r'''
class OpenTheLockTest {

    private final OpenTheLock solution = new OpenTheLock();

    @Test
    void examples() {
        assertEquals(6, solution.openLock(new String[]{"0201", "0101", "0102", "1212", "2002"}, "0202"));
        assertEquals(1, solution.openLock(new String[]{"8888"}, "0009"));
        assertEquals(-1, solution.openLock(new String[]{"8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"}, "8888"));
        assertEquals(-1, solution.openLock(new String[]{"0000"}, "8888"));
        assertEquals(0, solution.openLock(new String[]{"1111"}, "0000"));
        assertEquals(20, solution.openLock(new String[]{}, "5555"));
    }
}
''',
trace=r'''
function run(dead, target) {
  const blocked = new Set(dead), seen = new Set(['0000']); let q = ['0000'];
  A.step(`Start at 0000. Each move turns one wheel up or down. Avoid ${dead.join(', ')}.`, A.arr('deadends', dead, { hl: Object.fromEntries(dead.map((_, i) => [i, 'bad'])) }), A.arr('level 0', q));
  for (let moves = 0; q.length; moves++) {
    if (q.includes(target)) { A.step(`${target} is on level ${moves}.`, A.arr(`level ${moves}`, q.length > 12 ? [...q.slice(0, 11), '…'] : q, { hl: { [Math.min(q.indexOf(target), 11)]: 'ok' } }), A.text('Result', moves, 'ok')); return; }
    const next = [];
    q.forEach(cur => { for (let w = 0; w < 4; w++) for (const d of [1, 9]) { const c = [...cur]; c[w] = String((+c[w] + d) % 10); const s = c.join(''); if (!blocked.has(s) && !seen.has(s)) { seen.add(s); next.push(s); } } });
    q = next;
    const show = q.length > 12 ? [...q.slice(0, 11), '…'] : q;
    A.step(`Level ${moves + 1}: ${q.length} new combination${q.length === 1 ? '' : 's'} (deadends and repeats skipped).`, A.arr(`level ${moves + 1}`, show, { hl: Object.fromEntries(show.map((s, i) => [i, s === target ? 'ok' : 'cur'])) }), A.vars({ visited: seen.size }));
  }
  A.step('The queue emptied without reaching the target.', A.text('Result', -1, 'bad'));
}
A.scenario('Example', 'target 0202', () => run(['0201', '0101', '0102', '1212', '2002'], '0202'));
A.scenario('One move', 'target 0009', () => run(['8888'], '0009'));
'''),

P(num=767, slug="reorganize-string", title="Reorganize String", diff="Medium", topic="Greedy", cls="ReorganizeString",
idea="Place the most frequent letter on the even positions first, then fill the remaining slots in order.",
vname="Fill even slots, then odd",
spec=r'''
Rearrange `s` so that no two adjacent characters are equal. Return any valid arrangement, or `""` if none exists.

**Example**
```
"aab"  → "aba"
"aaab" → ""
```

**Constraints**
* `1 <= s.length <= 500`, lower-case letters
''',
approach=r'''
**Even slots first.** If some letter appears more than `(n + 1) / 2` times it is impossible. Otherwise write the most frequent letter at
positions `0, 2, 4, …`, then continue with every other letter, wrapping from the even positions to `1, 3, 5, …`. Equal letters are written
two apart, and the only way a letter could meet itself after the wrap is ruled out because the most frequent letter went first.

* Time: **O(n)**.
* Space: **O(n)** — the output (26 counters otherwise).
''',
tc="n", sc="n",
java=r'''
public class ReorganizeString {

    public String reorganizeString(String s) {
        int n = s.length();
        int[] count = new int[26];
        for (char c : s.toCharArray()) count[c - 'a']++;
        int top = 0;
        for (int c = 1; c < 26; c++) if (count[c] > count[top]) top = c;
        if (count[top] > (n + 1) / 2) return "";
        char[] out = new char[n];
        int pos = 0;
        for (int k = 0; k < 26; k++) {
            int c = k == 0 ? top : (k == top ? 0 : k);
            for (; count[c] > 0; count[c]--) {
                if (pos >= n) pos = 1;
                out[pos] = (char) ('a' + c);
                pos += 2;
            }
        }
        return new String(out);
    }
}
''',
test=r'''
class ReorganizeStringTest {

    private final ReorganizeString solution = new ReorganizeString();

    private void assertValid(String input, String out) {
        assertEquals(input.length(), out.length());
        char[] a = input.toCharArray(), b = out.toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);
        assertArrayEquals(a, b);
        for (int i = 1; i < out.length(); i++) assertNotEquals(out.charAt(i - 1), out.charAt(i), out);
    }

    @Test
    void possible() {
        for (String s : new String[]{"aab", "a", "ab", "aabb", "vvvlo", "bfrbs", "aaabbbccc", "zzzzaaabc", "abbabbaaab"}) assertValid(s, solution.reorganizeString(s));
    }

    @Test
    void impossible() {
        assertEquals("", solution.reorganizeString("aaab"));
        assertEquals("", solution.reorganizeString("aa"));
    }
}
''',
trace=r'''
function run(s) {
  const n = s.length, cnt = {}; [...s].forEach(c => (cnt[c] = (cnt[c] || 0) + 1));
  const order = Object.keys(cnt).sort((a, b) => cnt[b] - cnt[a] || (a < b ? -1 : 1)), top = order[0];
  A.step(`Count letters. The most frequent is '${top}' × ${cnt[top]}; the limit is ⌈${n}/2⌉ = ${Math.ceil(n / 2)}.`, A.chars('s', s), A.map('counts', cnt));
  if (cnt[top] > Math.ceil(n / 2)) { A.step(`'${top}' appears too often: two copies would have to touch.`, A.text('Result', '""', 'bad')); return; }
  const out = new Array(n).fill('·'); let pos = 0;
  order.forEach(c => {
    const placed = [];
    for (let k = 0; k < cnt[c]; k++) { if (pos >= n) pos = 1; out[pos] = c; placed.push(pos); pos += 2; }
    A.step(`Write '${c}' × ${cnt[c]} at positions ${placed.join(', ')} (every other slot${placed.some(p => p % 2) && placed.some(p => p % 2 === 0) ? ', wrapping to the odd slots' : ''}).`, A.arr('result', out, { hl: Object.fromEntries(placed.map(p => [p, 'ok'])) }));
  });
  A.step(`"${out.join('')}" has no two equal neighbours.`, A.text('Result', out.join(''), 'ok'));
}
A.scenario('Possible', '"aaabbc"', () => run('aaabbc'));
A.scenario('Impossible', '"aaab"', () => run('aaab'));
'''),

P(num=779, slug="k-th-symbol-in-grammar", title="K-th Symbol in Grammar", diff="Medium", topic="Recursion", cls="KthSymbolInGrammar",
idea="Each step right in the binary expansion of k − 1 flips the symbol, so the answer is the parity of its 1-bits.",
vname="Parity of the bits of k − 1",
spec=r'''
Row 1 is `0`. Each next row replaces every `0` with `01` and every `1` with `10`. Return the `k`-th (1-indexed) symbol of row `n`.

**Example**
```
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
n = 2, k = 2 → 1;   n = 4, k = 5 → 1
```

**Constraints**
* `1 <= n <= 30`, `1 <= k <= 2^(n-1)`
''',
approach=r'''
**Parent chain.** Symbol `k-1` (0-indexed) of a row comes from symbol `(k-1)/2` of the row above: a left child copies its parent, a
right child flips it. Reading `k-1` in binary from the top, every 1-bit is a "right child" step and flips the symbol. So the answer is the
parity of the number of 1-bits in `k-1`; `n` does not matter.

* Time: **O(1)** — a bit count.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class KthSymbolInGrammar {

    public int kthGrammar(int n, int k) {
        return Integer.bitCount(k - 1) & 1;
    }
}
''',
test=r'''
class KthSymbolInGrammarTest {

    private final KthSymbolInGrammar solution = new KthSymbolInGrammar();

    @ParameterizedTest
    @CsvSource({"1,1,0", "2,1,0", "2,2,1", "3,3,1", "3,4,0", "4,5,1", "30,434991989,0"})
    void symbol(int n, int k, int expected) {
        assertEquals(expected, solution.kthGrammar(n, k));
    }

    @Test
    void matchesBuiltRows() {
        StringBuilder row = new StringBuilder("0");
        for (int n = 1; n <= 10; n++) {
            for (int k = 1; k <= row.length(); k++) assertEquals(row.charAt(k - 1) - '0', solution.kthGrammar(n, k));
            StringBuilder next = new StringBuilder();
            for (char c : row.toString().toCharArray()) next.append(c == '0' ? "01" : "10");
            row = next;
        }
    }
}
''',
trace=r'''
function run(n, k) {
  let row = '0'; const rows = [row]; for (let i = 1; i < n; i++) { row = [...row].map(c => (c === '0' ? '01' : '10')).join(''); rows.push(row); }
  A.step(`Row 1 is 0; each 0 becomes 01 and each 1 becomes 10. Find symbol ${k} of row ${n}.`, ...rows.map((r, i) => A.chars(`row ${i + 1}`, r)));
  let idx = k - 1; const path = [];
  for (let r = n; r >= 1; r--) { path.unshift([r, idx]); idx = Math.floor(idx / 2); }
  path.forEach(([r, i], p) => { if (p === 0) A.step(`Row 1, index 0: the root, 0.`, A.chars('row 1', rows[0], { hl: { 0: 'cur' } })); else A.step(`Row ${r}, index ${i}: a ${i % 2 ? 'right child, which flips' : 'left child, which copies'} its parent → ${rows[r - 1][i]}.`, A.chars(`row ${r}`, rows[r - 1], { hl: { [i]: i % 2 ? 'alt' : 'cur' } })); });
  const bits = (k - 1).toString(2), ones = [...bits].filter(c => c === '1').length;
  A.step(`k − 1 = ${k - 1} = ${bits} in binary has ${ones} one-bit${ones === 1 ? '' : 's'} (right turns), so the symbol is ${ones % 2}.`, A.text('Result', ones % 2, 'ok'));
}
A.scenario('Row 4', 'n = 4, k = 5', () => run(4, 5));
A.scenario('Row 5', 'n = 5, k = 12', () => run(5, 12));
''',
variants=[dict(
name="Recursion on the parent",
idea="Look up the parent symbol in the row above; flip it if k is a right child.",
approach=r'''
**Recursion.** `kth(n, k)`: row 1 is 0. Otherwise the parent is `kth(n - 1, (k + 1) / 2)`; an odd `k` is a left child (same symbol), an
even `k` a right child (flipped).

* Time: **O(n)** — one call per row.
* Space: **O(n)** — recursion depth.
''',
tc="n", sc="n",
java=r'''
public class KthSymbolInGrammar {

    public int kthGrammar(int n, int k) {
        if (n == 1) return 0;
        int parent = kthGrammar(n - 1, (k + 1) / 2);
        return k % 2 == 1 ? parent : 1 - parent;
    }
}
''',
trace=r'''
function run(n, k) {
  const calls = [];
  (function go(r, kk) { calls.push([r, kk]); if (r > 1) go(r - 1, Math.ceil(kk / 2)); })(n, k);
  A.step(`kth(${n}, ${k}) asks for its parent in the row above, until row 1.`, A.stack('calls', calls.map(([r, kk]) => `kth(${r}, ${kk})`)));
  let v = 0;
  for (let i = calls.length - 1; i >= 0; i--) {
    const [r, kk] = calls[i];
    if (r === 1) { A.step('kth(1, 1) = 0.', A.vars({ value: 0 })); continue; }
    v = kk % 2 ? v : 1 - v;
    A.step(`kth(${r}, ${kk}): k is ${kk % 2 ? 'odd, a left child: copy' : 'even, a right child: flip'} → ${v}.`, A.stack('calls', calls.slice(0, i + 1).map(([a, b]) => `kth(${a}, ${b})`)), A.vars({ value: v }));
  }
  A.step(`Answer: ${v}.`, A.text('Result', v, 'ok'));
}
A.scenario('Row 4', 'n = 4, k = 5', () => run(4, 5));
''')]),

P(num=863, slug="all-nodes-distance-k-in-binary-tree", title="All Nodes Distance K in Binary Tree", diff="Medium", topic="Graph BFS", cls="DistanceK",
idea="Record each node's parent, then the tree is an undirected graph; BFS k steps from the target.",
vname="Parent map + BFS", helpers=["TreeNode"],
spec=r'''
Given the root of a binary tree, a `target` node in it and an integer `k`, return the values of all nodes exactly `k` edges away from
`target`, in any order.

**Example**
```
root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2 → [7,4,1]
root = [1], target = 1, k = 3 → []
```

**Constraints**
* `1 <= n <= 500`, unique values, `0 <= k <= 1000`
''',
approach=r'''
**Make it a graph.** One DFS stores each node's parent in a `MyHashMap` (keyed by node identity). Now every node has up to three
neighbours: left, right and parent. Run BFS from `target` for `k` levels, with a visited set so no node is used twice; the last level is
the answer.

* Time: **O(n)**.
* Space: **O(n)** — the parent map, visited set and queue.
''',
tc="n", sc="n",
java=r'''
public class DistanceK {

    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        MyHashMap<TreeNode, TreeNode> parent = new MyHashMap<>();
        Deque<TreeNode> stack = new ArrayDeque<>(List.of(root));
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            for (TreeNode c : new TreeNode[]{n.left, n.right})
                if (c != null) {
                    parent.put(c, n);
                    stack.push(c);
                }
        }
        MyHashSet<TreeNode> seen = new MyHashSet<>();
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(target));
        seen.add(target);
        for (int d = 0; d < k && !queue.isEmpty(); d++) {
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                for (TreeNode m : new TreeNode[]{n.left, n.right, parent.get(n)})
                    if (m != null && seen.add(m)) queue.add(m);
            }
        }
        List<Integer> out = new ArrayList<>();
        for (TreeNode n : queue) out.add(n.val);
        return out;
    }
}
''',
test=r'''
class DistanceKTest {

    private final DistanceK solution = new DistanceK();

    private TreeNode find(TreeNode n, int v) {
        if (n == null || n.val == v) return n;
        TreeNode l = find(n.left, v);
        return l != null ? l : find(n.right, v);
    }

    private List<Integer> run(TreeNode root, int target, int k) {
        List<Integer> out = new ArrayList<>(solution.distanceK(root, find(root, target), k));
        Collections.sort(out);
        return out;
    }

    @Test
    void examples() {
        TreeNode root = TreeNode.of(3, 5, 1, 6, 2, 0, 8, null, null, 7, 4);
        assertEquals(List.of(1, 4, 7), run(root, 5, 2));
        assertEquals(List.of(5), run(root, 5, 0));
        assertEquals(List.of(0, 2, 6, 8), run(root, 3, 2));
        assertEquals(List.of(), run(TreeNode.of(1), 1, 3));
        assertEquals(List.of(1), run(root, 7, 4));
    }
}
''',
trace=r'''
function run(arr, targetVal, k) {
  const root = A.mkTree(arr), parent = new Map(), all = [];
  (function walk(n, p) { if (!n) return; all.push(n); if (p) parent.set(n, p); walk(n.left, n); walk(n.right, n); })(root, null);
  const target = all.find(n => n.val === targetVal);
  A.step('First record every node\'s parent, so we can also walk upward.', A.tree('tree', root), A.map('child → parent', Object.fromEntries([...parent].map(([c, p]) => [c.val, p.val]))));
  const seen = new Set([target]), hl = { [target.id]: 'cur' }; let q = [target];
  A.step(`Start the BFS at the target, ${targetVal}.`, A.tree('tree', root, { hl }), A.vars({ distance: 0 }));
  for (let d = 1; d <= k && q.length; d++) {
    const next = [];
    q.forEach(n => [n.left, n.right, parent.get(n)].forEach(m => { if (m && !seen.has(m)) { seen.add(m); next.push(m); } }));
    q.forEach(n => (hl[n.id] = 'dim')); next.forEach(n => (hl[n.id] = d === k ? 'ok' : 'cur'));
    A.step(`Distance ${d}: ${next.length ? next.map(n => n.val).join(', ') : 'nothing new'} (children and parents of the last level).`, A.tree('tree', root, { hl }), A.vars({ distance: d }));
    q = next;
  }
  A.step(`Nodes at distance ${k}: [${q.map(n => n.val)}].`, A.text('Result', `[${q.map(n => n.val)}]`, 'ok'));
}
A.scenario('Example', 'target 5, k = 2', () => run([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], 5, 2));
'''),

P(num=931, slug="minimum-falling-path-sum", title="Minimum Falling Path Sum", diff="Medium", topic="Dynamic Programming", cls="MinimumFallingPathSum",
idea="Row by row, each cell adds the cheapest of the up to three cells above it.",
vname="Row-by-row DP",
spec=r'''
In an `n × n` matrix, a **falling path** starts anywhere in the first row and moves down one row at a time, to the cell directly below
or diagonally left/right. Return the minimum sum of a falling path.

**Example**
```
[[2,1,3],[6,5,4],[7,8,9]] → 13   (1 → 5 → 7  or  1 → 4 → 8)
[[-19,57],[-40,-5]]       → -59
```

**Constraints**
* `1 <= n <= 100`, `-100 <= matrix[i][j] <= 100`
''',
approach=r'''
**DP.** `best[c]` is the cheapest path ending at column `c` of the current row. For the next row, each cell adds
`min(best[c-1], best[c], best[c+1])` (where they exist). The answer is the minimum of the last row.

* Time: **O(n²)**.
* Space: **O(n)** — two rows.
''',
tc="n2", sc="n",
java=r'''
public class MinimumFallingPathSum {

    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int[] best = matrix[0].clone();
        for (int r = 1; r < n; r++) {
            int[] next = new int[n];
            for (int c = 0; c < n; c++) {
                int above = best[c];
                if (c > 0) above = Math.min(above, best[c - 1]);
                if (c < n - 1) above = Math.min(above, best[c + 1]);
                next[c] = matrix[r][c] + above;
            }
            best = next;
        }
        int ans = Integer.MAX_VALUE;
        for (int v : best) ans = Math.min(ans, v);
        return ans;
    }
}
''',
test=r'''
class MinimumFallingPathSumTest {

    private final MinimumFallingPathSum solution = new MinimumFallingPathSum();

    @Test
    void examples() {
        assertEquals(13, solution.minFallingPathSum(new int[][]{{2, 1, 3}, {6, 5, 4}, {7, 8, 9}}));
        assertEquals(-59, solution.minFallingPathSum(new int[][]{{-19, 57}, {-40, -5}}));
        assertEquals(7, solution.minFallingPathSum(new int[][]{{7}}));
    }
}
''',
trace=r'''
function run(m) {
  const n = m.length, dp = [m[0].slice()];
  A.step('The first row costs just its own values.', A.grid('matrix', m, { hl: Object.fromEntries(m[0].map((_, c) => [`0,${c}`, 'cur'])) }), A.grid('best', dp));
  for (let r = 1; r < n; r++) {
    const row = m[r].map((v, c) => v + Math.min(dp[r - 1][c], c > 0 ? dp[r - 1][c - 1] : Infinity, c < n - 1 ? dp[r - 1][c + 1] : Infinity));
    dp.push(row);
    A.step(`Row ${r}: each cell adds the cheapest of the up-to-three cells above it.`, A.grid('matrix', m, { hl: Object.fromEntries(m[r].map((_, c) => [`${r},${c}`, 'cur'])) }), A.grid('best', dp, { hl: Object.fromEntries(row.map((_, c) => [`${r},${c}`, 'ok'])) }));
  }
  const ans = Math.min(...dp[n - 1]);
  A.step(`The cheapest cell of the last row: ${ans}.`, A.grid('best', dp, { hl: { [`${n - 1},${dp[n - 1].indexOf(ans)}`]: 'ok' } }), A.text('Result', ans, 'ok'));
}
A.scenario('Example', '3 × 3', () => run([[2, 1, 3], [6, 5, 4], [7, 8, 9]]));
'''),
]
