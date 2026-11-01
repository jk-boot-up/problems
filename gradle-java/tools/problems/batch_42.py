PROBLEMS = [
P(num=382, slug="linked-list-random-node", title="Linked List Random Node", diff="Medium", topic="Randomized", cls="LinkedListRandomNode",
idea="Reservoir sampling: keep the i-th node with probability 1/i and every node ends up equally likely.",
vname="Reservoir sampling", helpers=["ListNode"],
spec=r'''
Given a singly linked list, implement `getRandom()` returning the value of a node chosen uniformly at random. Each node must be equally
likely.

* `LinkedListRandomNode(ListNode head)`
* `int getRandom()`

**Example**
```
list [1,2,3]: getRandom() returns 1, 2 or 3, each with probability 1/3
```

**Constraints**
* `1 <= n <= 10^4`; up to `10^4` calls
* Follow-up: what if the list is huge and its length unknown? Use O(1) extra space.
''',
approach=r'''
**Reservoir of size one.** Walk the list. At the `i`-th node (1-based), replace the current pick with probability `1/i`. Node `i` is
picked at step `i` with probability `1/i` and then survives every later step `j` with probability `(j-1)/j`; the product telescopes to
`1/n`. No length, no copy.

* Time: **O(n)** — per call.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class LinkedListRandomNode {

    private final ListNode head;
    private final Random rnd;

    public LinkedListRandomNode(ListNode head) {
        this(head, new Random());
    }

    LinkedListRandomNode(ListNode head, Random rnd) {
        this.head = head;
        this.rnd = rnd;
    }

    public int getRandom() {
        int pick = head.val, i = 1;
        for (ListNode n = head.next; n != null; n = n.next) {
            i++;
            if (rnd.nextInt(i) == 0) pick = n.val;
        }
        return pick;
    }
}
''',
test=r'''
class LinkedListRandomNodeTest {

    @Test
    void singleNode() {
        assertEquals(5, new LinkedListRandomNode(ListNode.of(5)).getRandom());
    }

    @Test
    void roughlyUniform() {
        LinkedListRandomNode s = new LinkedListRandomNode(ListNode.of(1, 2, 3, 4), new Random(42));
        int[] seen = new int[5];
        int draws = 40_000;
        for (int i = 0; i < draws; i++) seen[s.getRandom()]++;
        for (int v = 1; v <= 4; v++) assertEquals(draws / 4.0, seen[v], draws * 0.02, "value " + v);
    }
}
''',
trace=r'''
function run(vals) {
  let seed = 7; const rand = k => { seed = (seed * 1103515245 + 12345) % 2147483648; return seed % k; };
  A.step('Walk the list once. Node i replaces the current pick with probability 1/i.', A.list('list', vals));
  let pick = vals[0];
  A.step(`Node 1 (${vals[0]}) is kept with probability 1/1.`, A.list('list', vals, { hl: { 0: 'ok' }, ptr: { 0: 'i=1' } }), A.vars({ pick }));
  for (let i = 2; i <= vals.length; i++) {
    const r = rand(i), take = r === 0; if (take) pick = vals[i - 1];
    A.step(`Node ${i} (${vals[i - 1]}): replace with probability 1/${i}. Draw ${r} of 0..${i - 1} → ${take ? 'replace' : 'keep'}.`, A.list('list', vals, { hl: { [i - 1]: take ? 'ok' : 'cur', [vals.indexOf(pick)]: 'ok' }, ptr: { [i - 1]: `i=${i}` } }), A.vars({ pick, 'P(keep node i to the end)': `1/${i} × … = 1/${vals.length}` }));
  }
  A.step(`Returned ${pick}. Over many calls, every node comes out ${1}/${vals.length} of the time.`, A.text('Result', pick, 'ok'));
}
A.scenario('Five nodes', '[10,20,30,40,50]', () => run([10, 20, 30, 40, 50]));
''',
variants=[dict(
name="Copy into an array",
idea="Store the values once; each call picks a random index.",
approach=r'''
**Array.** Copy the values into a list in the constructor. `getRandom` returns a uniformly random index's value.

* Time: **O(1)** — per call, after O(n) setup.
* Space: **O(n)** — the copy.
''',
tc="1", sc="n",
java=r'''
public class LinkedListRandomNode {

    private final List<Integer> values = new ArrayList<>();
    private final Random rnd;

    public LinkedListRandomNode(ListNode head) {
        this(head, new Random());
    }

    LinkedListRandomNode(ListNode head, Random rnd) {
        for (ListNode n = head; n != null; n = n.next) values.add(n.val);
        this.rnd = rnd;
    }

    public int getRandom() {
        return values.get(rnd.nextInt(values.size()));
    }
}
''',
trace=r'''
function run(vals) {
  A.step('Copy the list into an array once.', A.list('list', vals), A.arr('array', vals));
  [3, 0, 4, 1].forEach(i => A.step(`getRandom(): random index ${i} → ${vals[i]}.`, A.arr('array', vals, { hl: { [i]: 'ok' } })));
  A.step('Each call is O(1), but the copy costs O(n) memory.', A.vars({ stored: vals.length }));
}
A.scenario('Five nodes', '[10,20,30,40,50]', () => run([10, 20, 30, 40, 50]));
''')]),

P(num=384, slug="shuffle-an-array", title="Shuffle an Array", diff="Medium", topic="Randomized", cls="ShuffleArray",
idea="Fisher–Yates: fill positions from the end, each with a random pick from the not-yet-placed prefix.",
vname="Fisher–Yates shuffle",
spec=r'''
Implement `ShuffleArray`:

* `ShuffleArray(int[] nums)`
* `int[] reset()` — the original array.
* `int[] shuffle()` — a random permutation; all `n!` permutations equally likely.

**Example**
```
nums = [1,2,3]
shuffle() → e.g. [3,1,2], reset() → [1,2,3], shuffle() → e.g. [1,3,2]
```

**Constraints**
* `1 <= nums.length <= 50`, values unique
''',
approach=r'''
**Fisher–Yates.** For `i` from `n - 1` down to 1, swap `a[i]` with `a[j]` for a uniform `j` in `0..i`. Every element is equally likely to
land in position `i`, and the rest is shuffled the same way, giving `n · (n-1) · … · 1` equally likely outcomes.

* Time: **O(n)** — per shuffle.
* Space: **O(n)** — the original copy.
''',
tc="n", sc="n",
java=r'''
public class ShuffleArray {

    private final int[] original;
    private final Random rnd;

    public ShuffleArray(int[] nums) {
        this(nums, new Random());
    }

    ShuffleArray(int[] nums, Random rnd) {
        original = nums.clone();
        this.rnd = rnd;
    }

    public int[] reset() {
        return original.clone();
    }

    public int[] shuffle() {
        int[] a = original.clone();
        for (int i = a.length - 1; i > 0; i--) {
            int j = rnd.nextInt(i + 1);
            int t = a[i];
            a[i] = a[j];
            a[j] = t;
        }
        return a;
    }
}
''',
test=r'''
class ShuffleArrayTest {

    @Test
    void resetAndPermutation() {
        ShuffleArray s = new ShuffleArray(new int[]{1, 2, 3, 4, 5});
        int[] shuffled = s.shuffle();
        int[] sorted = shuffled.clone();
        Arrays.sort(sorted);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, sorted);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, s.reset());
    }

    @Test
    void allPermutationsEquallyLikely() {
        ShuffleArray s = new ShuffleArray(new int[]{1, 2, 3}, new Random(1));
        TreeMap<String, Integer> seen = new TreeMap<>();
        int draws = 60_000;
        for (int i = 0; i < draws; i++) seen.merge(Arrays.toString(s.shuffle()), 1, Integer::sum);
        assertEquals(6, seen.size());
        for (int c : seen.values()) assertEquals(draws / 6.0, c, draws * 0.01);
    }
}
''',
trace=r'''
function run(nums) {
  let seed = 11; const rand = k => { seed = (seed * 1103515245 + 12345) % 2147483648; return seed % k; };
  const a = nums.slice(), done = {};
  A.step('Fill positions from the right. Each one gets a random element from the part not placed yet.', A.arr('array', a));
  for (let i = a.length - 1; i > 0; i--) {
    const j = rand(i + 1);
    A.step(`Position ${i}: pick j uniformly from 0..${i} → ${j}.`, A.arr('array', a, { hl: { ...done, [j]: 'cur', [i]: 'alt' }, range: [0, i] }));
    [a[i], a[j]] = [a[j], a[i]]; done[i] = 'ok';
    A.step(`Swap: ${a[i]} is now fixed at position ${i}.`, A.arr('array', a, { hl: done }));
  }
  done[0] = 'ok';
  A.step(`Shuffled: [${a}]. Each of the ${nums.length}! orders had the same chance.`, A.arr('array', a, { hl: done }));
}
A.scenario('Five numbers', '[1,2,3,4,5]', () => run([1, 2, 3, 4, 5]));
'''),

P(num=386, slug="lexicographical-numbers", title="Lexicographical Numbers", diff="Medium", topic="Trie", cls="LexicographicalNumbers",
idea="Walk the implicit 10-ary trie in pre-order: go deeper by ×10, otherwise step to the next sibling.",
vname="Iterative pre-order walk",
spec=r'''
Return the numbers `1..n` sorted in **lexicographical** (dictionary) order, in O(n) time and O(1) extra space.

**Example**
```
n = 13 → [1,10,11,12,13,2,3,4,5,6,7,8,9]
n = 2  → [1,2]
```

**Constraints**
* `1 <= n <= 5 * 10^4`
''',
approach=r'''
**Pre-order of a digit trie.** After `cur`, the next number in dictionary order is `cur * 10` if that is `<= n` (go to the first child).
Otherwise go to the next sibling `cur + 1`; but first climb up (`cur /= 10`) while `cur` ends in 9 or `cur + 1 > n`, since those have no
next sibling at this level.

* Time: **O(n)** — each step moves along the trie a bounded amortised amount.
* Space: **O(1)** — besides the output.
''',
tc="n", sc="1",
java=r'''
public class LexicographicalNumbers {

    public List<Integer> lexicalOrder(int n) {
        List<Integer> out = new ArrayList<>(n);
        int cur = 1;
        for (int i = 0; i < n; i++) {
            out.add(cur);
            if (cur * 10 <= n) cur *= 10;
            else {
                while (cur % 10 == 9 || cur + 1 > n) cur /= 10;
                cur++;
            }
        }
        return out;
    }
}
''',
test=r'''
class LexicographicalNumbersTest {

    private final LexicographicalNumbers solution = new LexicographicalNumbers();

    @Test
    void examples() {
        assertEquals(List.of(1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9), solution.lexicalOrder(13));
        assertEquals(List.of(1, 2), solution.lexicalOrder(2));
        assertEquals(List.of(1), solution.lexicalOrder(1));
    }

    @Test
    void matchesStringSort() {
        for (int n : new int[]{9, 10, 99, 100, 101, 1234, 50000}) {
            List<String> s = new ArrayList<>();
            for (int i = 1; i <= n; i++) s.add(String.valueOf(i));
            Collections.sort(s);
            List<Integer> expected = new ArrayList<>();
            for (String x : s) expected.add(Integer.parseInt(x));
            assertEquals(expected, solution.lexicalOrder(n));
        }
    }
}
''',
trace=r'''
function run(n) {
  const out = []; let cur = 1;
  A.step(`Visit 1..${n} as a dictionary would. Think of a tree where the children of x are x0..x9.`, A.vars({ n }));
  for (let i = 0; i < n; i++) {
    out.push(cur);
    let say;
    if (cur * 10 <= n) { say = `${cur}: its first child ${cur * 10} exists, so go down.`; cur *= 10; }
    else { const from = cur; while (cur % 10 === 9 || cur + 1 > n) cur = Math.floor(cur / 10); cur++; say = `${from}: no child ≤ ${n}. ${from !== cur - 1 ? `Climb up to ${cur - 1}, then` : 'Step'} to the next sibling ${cur}.`; }
    A.step(say, A.arr('order', out, { hl: { [out.length - 1]: 'ok' } }), A.vars({ next: i < n - 1 ? cur : '—' }));
  }
  A.step(`All ${n} numbers in dictionary order.`, A.arr('order', out));
}
A.scenario('n = 13', 'n = 13', () => run(13));
A.scenario('n = 21', 'climbs after 19', () => run(21));
'''),

P(num=395, slug="longest-substring-with-at-least-k-repeating-characters", title="Longest Substring with At Least K Repeating Characters", diff="Medium", topic="Sliding Window", cls="LongestSubstringKRepeating",
idea="Fix how many distinct letters the window may hold (1..26); for each, a plain sliding window works.",
vname="Sliding window per distinct count",
spec=r'''
Return the length of the longest substring of `s` in which **every** character appears at least `k` times.

**Example**
```
s = "aaabb",  k = 3 → 3   ("aaa")
s = "ababbc", k = 2 → 5   ("ababb")
```

**Constraints**
* `1 <= s.length <= 10^4`, lower-case letters, `1 <= k <= 10^5`
''',
approach=r'''
**Add a constraint.** A plain window fails because adding a letter can make things worse or better. Fixing `target` = the number of
distinct letters allowed makes it monotone: grow the right end; shrink from the left while more than `target` distinct letters are in
the window. When the window has exactly `target` distinct letters and all of them reach `k`, it is a candidate. Try `target = 1..26`.

* Time: **O(26 · n)** — 26 linear sweeps.
* Space: **O(1)** — 26 counters.
''',
tc="n", sc="1",
java=r'''
public class LongestSubstringKRepeating {

    public int longestSubstring(String s, int k) {
        int best = 0, n = s.length();
        for (int target = 1; target <= 26; target++) {
            int[] count = new int[26];
            int distinct = 0, atLeastK = 0;
            for (int lo = 0, hi = 0; hi < n; hi++) {
                int c = s.charAt(hi) - 'a';
                if (count[c]++ == 0) distinct++;
                if (count[c] == k) atLeastK++;
                while (distinct > target) {
                    int d = s.charAt(lo++) - 'a';
                    if (count[d]-- == k) atLeastK--;
                    if (count[d] == 0) distinct--;
                }
                if (distinct == target && atLeastK == target) best = Math.max(best, hi - lo + 1);
            }
        }
        return best;
    }
}
''',
test=r'''
class LongestSubstringKRepeatingTest {

    private final LongestSubstringKRepeating solution = new LongestSubstringKRepeating();

    @ParameterizedTest
    @CsvSource({"aaabb,3,3", "ababbc,2,5", "a,2,0", "a,1,1", "bbaaacbd,3,3", "ababacb,3,0", "aaabbbcdd,3,6"})
    void longest(String s, int k, int expected) {
        assertEquals(expected, solution.longestSubstring(s, k));
    }
}
''',
trace=r'''
function run(s, k) {
  let best = 0, bestRange = null;
  const distinctTotal = new Set(s).size;
  A.step(`For each target number of distinct letters (1..${distinctTotal} here), slide a window holding at most that many.`, A.chars('s', s), A.vars({ k }));
  for (let target = 1; target <= distinctTotal; target++) {
    const cnt = {}; let lo = 0, distinct = 0, atK = 0, found = null;
    for (let hi = 0; hi < s.length; hi++) {
      const c = s[hi]; if (!cnt[c]) distinct++; cnt[c] = (cnt[c] || 0) + 1; if (cnt[c] === k) atK++;
      while (distinct > target) { const d = s[lo++]; if (cnt[d] === k) atK--; cnt[d]--; if (!cnt[d]) distinct--; }
      if (distinct === target && atK === target && hi - lo + 1 > (found ? found[1] - found[0] + 1 : 0)) found = [lo, hi];
    }
    if (found && found[1] - found[0] + 1 > best) { best = found[1] - found[0] + 1; bestRange = found; }
    A.step(found ? `target = ${target}: the longest valid window is "${s.slice(found[0], found[1] + 1)}" (length ${found[1] - found[0] + 1}).` : `target = ${target}: no window has ${target} letters that all reach ${k}.`, A.chars('s', s, found ? { range: found } : {}), A.vars({ target, best }));
  }
  A.step(best ? `Longest: "${s.slice(bestRange[0], bestRange[1] + 1)}", length ${best}.` : 'No substring qualifies.', A.text('Result', best, best ? 'ok' : 'bad'));
}
A.scenario('Two letters', '"ababbc", k = 2', () => run('ababbc', 2));
A.scenario('One letter', '"aaabb", k = 3', () => run('aaabb', 3));
''',
variants=[dict(
name="Divide and conquer on rare letters",
idea="A letter that appears fewer than k times can never be inside the answer, so split around it.",
approach=r'''
**Split.** Count the letters of the current range. If every letter appears at least `k` times, the whole range is valid. Otherwise any
letter with a count below `k` is a wall: solve each piece between walls recursively and keep the best.

* Time: **O(26 · n)** — each level of recursion removes at least one distinct letter, so there are at most 26 levels of linear work.
* Space: **O(26)** — the recursion depth (plus a counter array per level).
''',
tc="n", sc="1",
java=r'''
public class LongestSubstringKRepeating {

    public int longestSubstring(String s, int k) {
        return solve(s, 0, s.length(), k);
    }

    private int solve(String s, int lo, int hi, int k) {
        if (hi - lo < k) return 0;
        int[] count = new int[26];
        for (int i = lo; i < hi; i++) count[s.charAt(i) - 'a']++;
        int best = 0, start = lo;
        boolean split = false;
        for (int i = lo; i < hi; i++) {
            if (count[s.charAt(i) - 'a'] < k) {
                split = true;
                best = Math.max(best, solve(s, start, i, k));
                start = i + 1;
            }
        }
        if (!split) return hi - lo;
        return Math.max(best, solve(s, start, hi, k));
    }
}
''',
trace=r'''
function run(s, k) {
  A.step(`Letters that appear fewer than ${k} times in a range can never be part of the answer. Split around them.`, A.chars('s', s));
  let best = 0;
  (function solve(lo, hi) {
    if (hi - lo < k) return;
    const cnt = {}; for (let i = lo; i < hi; i++) cnt[s[i]] = (cnt[s[i]] || 0) + 1;
    const walls = []; for (let i = lo; i < hi; i++) if (cnt[s[i]] < k) walls.push(i);
    if (!walls.length) { best = Math.max(best, hi - lo); A.step(`"${s.slice(lo, hi)}": every letter appears at least ${k} times. Valid, length ${hi - lo}.`, A.chars('s', s, { range: [lo, hi - 1] }), A.vars({ best })); return; }
    A.step(`"${s.slice(lo, hi)}": ${[...new Set(walls.map(i => s[i]))].join(', ')} appear${walls.length === 1 ? 's' : ''} too rarely. Split there.`, A.chars('s', s, { range: [lo, hi - 1], hl: Object.fromEntries(walls.map(i => [i, 'bad'])) }));
    let start = lo; walls.forEach(w => { solve(start, w); start = w + 1; }); solve(start, hi);
  })(0, s.length);
  A.step(`Longest valid piece: ${best}.`, A.text('Result', best, best ? 'ok' : 'bad'));
}
A.scenario('Two letters', '"ababbc", k = 2', () => run('ababbc', 2));
''')]),

P(num=402, slug="remove-k-digits", title="Remove K Digits", diff="Medium", topic="Monotonic Stack", cls="RemoveKDigits",
idea="Scan left to right; whenever a digit is smaller than the one before it, removing the bigger one earlier helps most.",
vname="Monotonic increasing stack",
spec=r'''
Given a non-negative integer as a string `num` and an integer `k`, remove `k` digits so the remaining number is as small as possible.
Return it without leading zeros (`"0"` if nothing is left).

**Example**
```
num = "1432219", k = 3 → "1219"
num = "10200",   k = 1 → "200"
num = "10",      k = 2 → "0"
```

**Constraints**
* `1 <= k <= num.length <= 10^5`; `num` has no leading zeros except `"0"` itself
''',
approach=r'''
**Greedy with a stack.** A smaller digit should move as far left as possible. Push digits onto a stack; before pushing `d`, pop larger
digits while removals remain. Leftover removals come off the end (the stack is then non-decreasing, so the tail is the largest). Finally
strip leading zeros.

* Time: **O(n)** — each digit is pushed and popped at most once.
* Space: **O(n)** — the stack.
''',
tc="n", sc="n",
java=r'''
public class RemoveKDigits {

    public String removeKdigits(String num, int k) {
        StringBuilder stack = new StringBuilder();
        for (char d : num.toCharArray()) {
            while (k > 0 && stack.length() > 0 && stack.charAt(stack.length() - 1) > d) {
                stack.setLength(stack.length() - 1);
                k--;
            }
            stack.append(d);
        }
        stack.setLength(stack.length() - k);
        int start = 0;
        while (start < stack.length() - 1 && stack.charAt(start) == '0') start++;
        return stack.length() == 0 ? "0" : stack.substring(start);
    }
}
''',
test=r'''
class RemoveKDigitsTest {

    private final RemoveKDigits solution = new RemoveKDigits();

    @ParameterizedTest
    @CsvSource({"1432219,3,1219", "10200,1,200", "10,2,0", "112,1,11", "9,1,0", "123456,3,123", "100,1,0", "5337,2,33"})
    void smallest(String num, int k, String expected) {
        assertEquals(expected, solution.removeKdigits(num, k));
    }
}
''',
trace=r'''
function run(num, k) {
  const st = [];
  A.step(`Remove ${k} digits. Keep a stack of digits; a smaller digit kicks out bigger digits before it while removals remain.`, A.chars('num', num), A.stack('kept', st), A.vars({ k }));
  for (let i = 0; i < num.length; i++) {
    const d = num[i], popped = [];
    while (k > 0 && st.length && st[st.length - 1] > d) { popped.push(st.pop()); k--; }
    st.push(d);
    A.step(popped.length ? `${d} is smaller than ${popped.join(', ')}: remove ${popped.length === 1 ? 'it' : 'them'}, then keep ${d}.` : `Keep ${d}.`, A.chars('num', num, { hl: { [i]: popped.length ? 'bad' : 'cur' } }), A.stack('kept', st), A.vars({ 'removals left': k }));
  }
  if (k) { st.length -= k; A.step(`${k} removal${k > 1 ? 's' : ''} left: drop from the end, where the largest digits are.`, A.stack('kept', st)); }
  const res = st.join('').replace(/^0+(?=.)/, '') || '0';
  A.step(`Strip leading zeros: "${res}".`, A.text('Result', res, 'ok'));
}
A.scenario('Classic', '"1432219", k = 3', () => run('1432219', 3));
A.scenario('Leading zeros', '"10200", k = 1', () => run('10200', 1));
'''),

P(num=404, slug="sum-of-left-leaves", title="Sum of Left Leaves", diff="Easy", topic="Binary Tree DFS", cls="SumOfLeftLeaves",
idea="A node is a left leaf when it is a parent's left child and has no children; pass that flag down.",
vname="DFS with an is-left flag", helpers=["TreeNode"],
spec=r'''
Return the sum of all **left leaves**: leaves that are the left child of their parent.

**Example**
```
[3,9,20,null,null,15,7] → 24   (9 + 15)
[1]                     → 0
```

**Constraints**
* `1 <= n <= 1000`
''',
approach=r'''
**DFS.** Recurse with a flag saying whether the node is a left child. A leaf contributes its value only when the flag is set.

* Time: **O(n)**.
* Space: **O(h)** — recursion depth.
''',
tc="n", sc="n",
java=r'''
public class SumOfLeftLeaves {

    public int sumOfLeftLeaves(TreeNode root) {
        return dfs(root, false);
    }

    private int dfs(TreeNode node, boolean isLeft) {
        if (node == null) return 0;
        if (node.left == null && node.right == null) return isLeft ? node.val : 0;
        return dfs(node.left, true) + dfs(node.right, false);
    }
}
''',
test=r'''
class SumOfLeftLeavesTest {

    private final SumOfLeftLeaves solution = new SumOfLeftLeaves();

    @Test
    void examples() {
        assertEquals(24, solution.sumOfLeftLeaves(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertEquals(0, solution.sumOfLeftLeaves(TreeNode.of(1)));
        assertEquals(4, solution.sumOfLeftLeaves(TreeNode.of(1, 2, 3, 4, 5)));
        assertEquals(0, solution.sumOfLeftLeaves(TreeNode.of(1, null, 2)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {}; let sum = 0;
  A.step('Visit every node, remembering whether it is a left child.', A.tree('tree', root));
  (function dfs(n, isLeft) {
    if (!n) return;
    if (!n.left && !n.right) {
      if (isLeft) { sum += n.val; hl[n.id] = 'ok'; A.step(`${n.val} is a leaf and a left child: add it. Sum = ${sum}.`, A.tree('tree', root, { hl }), A.vars({ sum })); }
      else { hl[n.id] = 'dim'; A.step(`${n.val} is a leaf but ${n === root ? 'the root' : 'a right child'}: skip it.`, A.tree('tree', root, { hl }), A.vars({ sum })); }
      return;
    }
    dfs(n.left, true); dfs(n.right, false);
  })(root, false);
  A.step(`Sum of left leaves: ${sum}.`, A.text('Result', sum, 'ok'));
}
A.scenario('Classic', '[3,9,20,null,null,15,7]', () => run([3, 9, 20, null, null, 15, 7]));
A.scenario('Deeper', '[1,2,3,4,5]', () => run([1, 2, 3, 4, 5]));
'''),

P(num=406, slug="queue-reconstruction-by-height", title="Queue Reconstruction by Height", diff="Medium", topic="Greedy", cls="QueueReconstruction",
idea="Place the tallest people first; a shorter person inserted later at index k does not disturb anyone taller.",
vname="Sort tall-first, insert at k",
spec=r'''
Each person is `[h, k]`: height `h`, and exactly `k` people **in front** of them have height `>= h`. Reconstruct the queue from a shuffled
list.

**Example**
```
[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] → [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
```

**Constraints**
* `1 <= n <= 2000`; a valid queue always exists
''',
approach=r'''
**Tall first.** Sort by height descending, and by `k` ascending for equal heights. Insert each person at index `k` of the result. Everyone
already placed is at least as tall, so exactly `k` of them end up in front; people inserted later are shorter and invisible to them.

* Time: **O(n²)** — list insertions.
* Space: **O(n)** — the result list.
''',
tc="n2", sc="n",
java=r'''
public class QueueReconstruction {

    public int[][] reconstructQueue(int[][] people) {
        int[][] p = people.clone();
        Arrays.sort(p, (a, b) -> a[0] != b[0] ? Integer.compare(b[0], a[0]) : Integer.compare(a[1], b[1]));
        List<int[]> queue = new ArrayList<>();
        for (int[] person : p) queue.add(person[1], person);
        return queue.toArray(new int[0][]);
    }
}
''',
test=r'''
class QueueReconstructionTest {

    private final QueueReconstruction solution = new QueueReconstruction();

    @Test
    void examples() {
        assertArrayEquals(new int[][]{{5, 0}, {7, 0}, {5, 2}, {6, 1}, {4, 4}, {7, 1}},
                solution.reconstructQueue(new int[][]{{7, 0}, {4, 4}, {7, 1}, {5, 0}, {6, 1}, {5, 2}}));
        assertArrayEquals(new int[][]{{4, 0}, {5, 0}, {2, 2}, {3, 2}, {1, 4}, {6, 0}},
                solution.reconstructQueue(new int[][]{{6, 0}, {5, 0}, {4, 0}, {3, 2}, {2, 2}, {1, 4}}));
    }
}
''',
trace=r'''
function run(people) {
  const p = people.slice().sort((a, b) => b[0] - a[0] || a[1] - b[1]), q = [];
  A.step('Sort tallest first (ties by k). Each person is inserted at index k.', A.arr('input', people.map(x => `[${x}]`)), A.arr('sorted', p.map(x => `[${x}]`)));
  p.forEach(x => {
    q.splice(x[1], 0, x);
    A.step(`Insert [${x}] at index ${x[1]}: everyone already placed is at least ${x[0]} tall, so exactly ${x[1]} of them are in front.`, A.arr('queue', q.map(y => `[${y}]`), { hl: { [x[1]]: 'ok' } }));
  });
  A.step('Every k is satisfied.', A.arr('queue', q.map(y => `[${y}]`)));
}
A.scenario('Example', '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]', () => run([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]));
'''),

P(num=409, slug="longest-palindrome", title="Longest Palindrome", diff="Easy", topic="Hash Map", cls="LongestPalindrome",
idea="Use every pair of equal letters, plus one odd letter in the middle if there is any.",
vname="Count letters",
spec=r'''
Given a string of upper- and lower-case letters, return the length of the longest palindrome that can be **built** from those letters.
Letters are case-sensitive (`"Aa"` is not a palindrome).

**Example**
```
"abccccdd" → 7   ("dccaccd")
"a"        → 1
```

**Constraints**
* `1 <= s.length <= 2000`
''',
approach=r'''
**Pairs plus a centre.** Count each letter. A palindrome can use `count / 2 * 2` copies of every letter (mirrored pairs), and one more
letter in the middle if any count is odd.

* Time: **O(n)**.
* Space: **O(1)** — 128 counters.
''',
tc="n", sc="1",
java=r'''
public class LongestPalindrome {

    public int longestPalindrome(String s) {
        int[] count = new int[128];
        for (char c : s.toCharArray()) count[c]++;
        int length = 0;
        boolean odd = false;
        for (int c : count) {
            length += c / 2 * 2;
            if (c % 2 == 1) odd = true;
        }
        return length + (odd ? 1 : 0);
    }
}
''',
test=r'''
class LongestPalindromeTest {

    private final LongestPalindrome solution = new LongestPalindrome();

    @ParameterizedTest
    @CsvSource({"abccccdd,7", "a,1", "Aa,1", "bb,2", "ccc,3", "abc,1", "aabbccdd,8"})
    void length(String s, int expected) {
        assertEquals(expected, solution.longestPalindrome(s));
    }
}
''',
trace=r'''
function run(s) {
  const cnt = {}; [...s].forEach(c => (cnt[c] = (cnt[c] || 0) + 1));
  A.step('Count every letter.', A.chars('s', s), A.map('counts', cnt));
  let len = 0, odd = false;
  Object.entries(cnt).forEach(([c, n]) => { len += Math.floor(n / 2) * 2; if (n % 2) odd = true; A.step(`'${c}' × ${n}: use ${Math.floor(n / 2) * 2} as mirrored pairs${n % 2 ? '; one is left over' : ''}.`, A.map('counts', cnt), A.vars({ length: len, oddLeft: odd })); });
  A.step(odd ? `A leftover letter can sit in the middle: ${len} + 1 = ${len + 1}.` : `No leftover letter: ${len}.`, A.text('Result', len + (odd ? 1 : 0), 'ok'));
}
A.scenario('Classic', '"abccccdd"', () => run('abccccdd'));
'''),

P(num=410, slug="split-array-largest-sum", title="Split Array Largest Sum", diff="Hard", topic="Binary Search", cls="SplitArrayLargestSum",
idea="Binary search on the answer: can the array be cut into at most k pieces whose sums stay below a cap?",
vname="Binary search on the cap",
spec=r'''
Split `nums` into `k` non-empty contiguous subarrays so that the **largest** subarray sum is as small as possible. Return that sum.

**Example**
```
nums = [7,2,5,10,8], k = 2 → 18   ([7,2,5] and [10,8])
nums = [1,2,3,4,5],  k = 2 → 9
nums = [1,4,4],      k = 3 → 4
```

**Constraints**
* `1 <= nums.length <= 1000`, `0 <= nums[i] <= 10^6`, `1 <= k <= min(50, nums.length)`
''',
approach=r'''
**Feasibility is monotone.** For a cap `c`, greedily extend the current piece until the next number would exceed `c`, then start a new
piece. If that needs at most `k` pieces, any larger cap works too. Binary search `c` between `max(nums)` (each number must fit) and
`sum(nums)` (one piece). Fewer than `k` pieces is fine, since pieces can always be split further.

* Time: **O(n log S)** — `S` is the sum; each check is linear.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class SplitArrayLargestSum {

    public int splitArray(int[] nums, int k) {
        long lo = 0, hi = 0;
        for (int v : nums) {
            lo = Math.max(lo, v);
            hi += v;
        }
        while (lo < hi) {
            long cap = (lo + hi) >>> 1;
            if (pieces(nums, cap) <= k) hi = cap;
            else lo = cap + 1;
        }
        return (int) lo;
    }

    private int pieces(int[] nums, long cap) {
        int count = 1;
        long sum = 0;
        for (int v : nums) {
            if (sum + v > cap) {
                count++;
                sum = 0;
            }
            sum += v;
        }
        return count;
    }
}
''',
test=r'''
class SplitArrayLargestSumTest {

    private final SplitArrayLargestSum solution = new SplitArrayLargestSum();

    @Test
    void examples() {
        assertEquals(18, solution.splitArray(new int[]{7, 2, 5, 10, 8}, 2));
        assertEquals(9, solution.splitArray(new int[]{1, 2, 3, 4, 5}, 2));
        assertEquals(4, solution.splitArray(new int[]{1, 4, 4}, 3));
        assertEquals(0, solution.splitArray(new int[]{0}, 1));
        assertEquals(32, solution.splitArray(new int[]{7, 2, 5, 10, 8}, 1));
        assertEquals(10, solution.splitArray(new int[]{7, 2, 5, 10, 8}, 5));
    }
}
''',
trace=r'''
function run(nums, k) {
  let lo = Math.max(...nums), hi = nums.reduce((a, b) => a + b, 0);
  A.step(`The answer is at least the biggest number (${lo}) and at most the total (${hi}). Binary search on that cap.`, A.arr('nums', nums), A.vars({ k, lo, hi }));
  while (lo < hi) {
    const cap = Math.floor((lo + hi) / 2), cut = []; let sum = 0, cnt = 1;
    nums.forEach((v, i) => { if (sum + v > cap) { cnt++; sum = 0; cut.push(i); } sum += v; });
    const hl = {}; let g = 0; nums.forEach((_, i) => { if (cut.includes(i)) g++; hl[i] = g % 2 ? 'alt' : 'cur'; });
    A.step(`Cap ${cap}: greedy pieces need ${cnt}. ${cnt <= k ? `That is ≤ ${k}, so try a smaller cap.` : `More than ${k}, so the cap must grow.`}`, A.arr('nums', nums, { hl }), A.vars({ lo, hi, cap, pieces: cnt }));
    if (cnt <= k) hi = cap; else lo = cap + 1;
  }
  A.step(`lo = hi = ${lo}: the smallest possible largest sum.`, A.text('Result', lo, 'ok'));
}
A.scenario('Example', '[7,2,5,10,8], k = 2', () => run([7, 2, 5, 10, 8], 2));
''',
variants=[dict(
name="DP over prefixes and pieces",
idea="best[j][i] = the best largest sum for the first i numbers in j pieces, trying every position for the last cut.",
approach=r'''
**DP.** With prefix sums, `best[j][i] = min over p < i of max(best[j-1][p], sum(p..i-1))`. The answer is `best[k][n]`.

* Time: **O(k · n²)** — `k · n` states, each trying `n` cut positions.
* Space: **O(k · n)** — the table.
''',
tc="n2", sc="n2",
java=r'''
public class SplitArrayLargestSum {

    public int splitArray(int[] nums, int k) {
        int n = nums.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        long[][] best = new long[k + 1][n + 1];
        for (long[] row : best) Arrays.fill(row, Long.MAX_VALUE);
        best[0][0] = 0;
        for (int j = 1; j <= k; j++)
            for (int i = 1; i <= n; i++)
                for (int p = j - 1; p < i; p++)
                    if (best[j - 1][p] != Long.MAX_VALUE)
                        best[j][i] = Math.min(best[j][i], Math.max(best[j - 1][p], prefix[i] - prefix[p]));
        return (int) best[k][n];
    }
}
''',
trace=r'''
function run(nums, k) {
  const n = nums.length, pre = [0]; nums.forEach(v => pre.push(pre[pre.length - 1] + v));
  const INF = Infinity, best = Array.from({ length: k + 1 }, () => new Array(n + 1).fill(INF)); best[0][0] = 0;
  const show = () => best.map(r => r.map(v => (v === INF ? '∞' : v)));
  A.step('best[j][i]: smallest possible largest sum for the first i numbers cut into j pieces.', A.arr('nums', nums), A.grid('best', show()));
  for (let j = 1; j <= k; j++) {
    for (let i = 1; i <= n; i++) for (let p = j - 1; p < i; p++) if (best[j - 1][p] !== INF) best[j][i] = Math.min(best[j][i], Math.max(best[j - 1][p], pre[i] - pre[p]));
    A.step(`Row j = ${j} filled: every split of each prefix into ${j} piece${j > 1 ? 's' : ''}.`, A.grid('best', show(), { hl: Object.fromEntries(Array.from({ length: n + 1 }, (_, i) => [`${j},${i}`, 'cur'])) }));
  }
  A.step(`best[${k}][${n}] = ${best[k][n]}.`, A.grid('best', show(), { hl: { [`${k},${n}`]: 'ok' } }), A.text('Result', best[k][n], 'ok'));
}
A.scenario('Example', '[7,2,5,10,8], k = 2', () => run([7, 2, 5, 10, 8], 2));
''')]),

P(num=413, slug="arithmetic-slices", title="Arithmetic Slices", diff="Medium", topic="Dynamic Programming", cls="ArithmeticSlices",
idea="If the slice ending at i − 1 extends to i, every one of those slices grows by one, plus one new 3-element slice.",
vname="Run length DP",
spec=r'''
An array is **arithmetic** if it has at least three elements and equal differences between neighbours. Return the number of arithmetic
contiguous subarrays of `nums`.

**Example**
```
[1,2,3,4] → 3   ([1,2,3], [2,3,4], [1,2,3,4])
[1]       → 0
```

**Constraints**
* `1 <= nums.length <= 5000`
''',
approach=r'''
**Count slices ending here.** Let `cur` be the number of arithmetic slices ending at `i`. If `nums[i] - nums[i-1] == nums[i-1] - nums[i-2]`,
then `cur = previous cur + 1` (all earlier slices extend, plus the new three-element one); otherwise `cur = 0`. Sum `cur` over all `i`.

* Time: **O(n)**.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class ArithmeticSlices {

    public int numberOfArithmeticSlices(int[] nums) {
        int total = 0, cur = 0;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) total += ++cur;
            else cur = 0;
        }
        return total;
    }
}
''',
test=r'''
class ArithmeticSlicesTest {

    private final ArithmeticSlices solution = new ArithmeticSlices();

    @Test
    void examples() {
        assertEquals(3, solution.numberOfArithmeticSlices(new int[]{1, 2, 3, 4}));
        assertEquals(0, solution.numberOfArithmeticSlices(new int[]{1}));
        assertEquals(2, solution.numberOfArithmeticSlices(new int[]{1, 2, 3, 8, 9, 10}));
        assertEquals(6, solution.numberOfArithmeticSlices(new int[]{1, 3, 5, 7, 9}));
        assertEquals(1, solution.numberOfArithmeticSlices(new int[]{7, 7, 7}));
    }
}
''',
trace=r'''
function run(nums) {
  let total = 0, cur = 0;
  A.step('cur = number of arithmetic slices that end at the current index.', A.arr('nums', nums), A.vars({ cur, total }));
  for (let i = 2; i < nums.length; i++) {
    const d1 = nums[i] - nums[i - 1], d0 = nums[i - 1] - nums[i - 2];
    if (d1 === d0) { cur++; total += cur; A.step(`Differences ${d0} and ${d1} match: the ${cur - 1} slice${cur - 1 === 1 ? '' : 's'} ending at ${i - 1} extend, plus [${nums.slice(i - 2, i + 1)}]. cur = ${cur}.`, A.arr('nums', nums, { range: [i - cur - 1, i], hl: { [i]: 'ok' } }), A.vars({ cur, total })); }
    else { cur = 0; A.step(`Differences ${d0} and ${d1} differ: the run breaks. cur = 0.`, A.arr('nums', nums, { hl: { [i]: 'bad' } }), A.vars({ cur, total })); }
  }
  A.step(`Total arithmetic slices: ${total}.`, A.text('Result', total, 'ok'));
}
A.scenario('One run', '[1,3,5,7,9]', () => run([1, 3, 5, 7, 9]));
A.scenario('Two runs', '[1,2,3,8,9,10]', () => run([1, 2, 3, 8, 9, 10]));
'''),
]
