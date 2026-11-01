PROBLEMS = [
P(num=394, slug="decode-string", title="Decode String", diff="Medium", topic="Stack", cls="DecodeString",
idea="On '[', save the current string and repeat count; on ']', repeat the inner string and append it to the saved one.",
vname="Two stacks",
spec=r'''
Decode a string encoded as `k[encoded]`, meaning `encoded` repeated `k` times. Encodings may be nested; digits only appear as repeat counts.

**Example**
```
"3[a]2[bc]" → "aaabcbc",   "3[a2[c]]" → "accaccacc",   "2[abc]3[cd]ef" → "abcabccdcdcdef"
```

**Constraints**
* `1 <= s.length <= 30`; output length at most `10^5`.
''',
approach=r'''
**Stacks of context.** Build the current string and current number. On `[`, push both and reset. On `]`, pop the outer string and count, and
set `current = outer + current × count`.

* Time: **O(output)** — every output character is written a constant number of times per nesting level.
* Space: **O(output)** — the builders and stacks.
''',
tc="n", sc="n",
java=r'''
public class DecodeString {

    public String decodeString(String s) {
        Deque<Integer> counts = new ArrayDeque<>();
        Deque<StringBuilder> outer = new ArrayDeque<>();
        StringBuilder cur = new StringBuilder();
        int k = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                k = k * 10 + (c - '0');
            } else if (c == '[') {
                counts.push(k);
                outer.push(cur);
                cur = new StringBuilder();
                k = 0;
            } else if (c == ']') {
                StringBuilder prev = outer.pop();
                prev.append(cur.toString().repeat(counts.pop()));
                cur = prev;
            } else {
                cur.append(c);
            }
        }
        return cur.toString();
    }
}
''',
test=r'''
class DecodeStringTest {

    private final DecodeString solution = new DecodeString();

    @ParameterizedTest
    @CsvSource({"3[a]2[bc],aaabcbc", "3[a2[c]],accaccacc", "2[abc]3[cd]ef,abcabccdcdcdef", "10[a],aaaaaaaaaa"})
    void decodes(String s, String expected) {
        assertEquals(expected, solution.decodeString(s));
    }
}
''',
trace=r'''
function run(s) {
  const counts = [], outer = []; let cur = '', k = 0;
  const view = (msg, i) => A.step(msg, A.chars('s', s, { hl: { [i]: 'cur' } }), A.stack('saved (string, count)', outer.map((o, t) => `"${o}" ×${counts[t]}`)), A.vars({ current: `"${cur}"`, k }));
  [...s].forEach((c, i) => {
    if (/\d/.test(c)) { k = k * 10 + +c; view(`Digit ${c}: repeat count ${k}.`, i); }
    else if (c === '[') { counts.push(k); outer.push(cur); cur = ''; k = 0; view("'[': save the current string and count, then start fresh inside the brackets.", i); }
    else if (c === ']') { const n = counts.pop(), o = outer.pop(); cur = o + cur.repeat(n); view(`']': repeat the inner string ${n} times and append it to the saved string.`, i); }
    else { cur += c; view(`Letter '${c}'.`, i); }
  });
  A.step(`Decoded: "${cur}".`, A.text('Result', cur, 'ok'));
}
A.scenario('Nested', 's = "3[a2[c]]"', () => run('3[a2[c]]'));
'''),

P(num=933, slug="number-of-recent-calls", title="Number of Recent Calls", diff="Easy", topic="Queue", cls="RecentCounter",
idea="Keep pings in a queue and drop those older than t − 3000 from the front.",
vname="Sliding queue",
spec=r'''
Implement `RecentCounter` with `ping(t)`: record a request at time `t` (strictly increasing) and return how many requests happened in the
inclusive range `[t - 3000, t]`.

**Example**
```
ping(1) → 1, ping(100) → 2, ping(3001) → 3, ping(3002) → 3
```

**Constraints**
* `1 <= t <= 10^9`; at most `10^4` calls.
''',
approach=r'''
**Queue window.** Append `t`; pop from the front while the front is less than `t - 3000`; return the size.

* Time: **O(1)** — amortized per ping (each time is added and removed once).
* Space: **O(W)** — the pings within the last 3000 ms.
''',
tc="1", sc="n",
java=r'''
public class RecentCounter {

    private final Deque<Integer> pings = new ArrayDeque<>();

    public int ping(int t) {
        pings.addLast(t);
        while (pings.peekFirst() < t - 3000) pings.pollFirst();
        return pings.size();
    }
}
''',
test=r'''
class RecentCounterTest {

    @Test
    void example() {
        RecentCounter r = new RecentCounter();
        assertEquals(1, r.ping(1));
        assertEquals(2, r.ping(100));
        assertEquals(3, r.ping(3001));
        assertEquals(3, r.ping(3002));
    }
}
''',
trace=r'''
A.scenario('Four pings', 'ping 1, 100, 3001, 3002', () => {
  const q = [];
  for (const t of [1, 100, 3001, 3002]) {
    q.push(t); const dropped = []; while (q[0] < t - 3000) dropped.push(q.shift());
    A.step(`ping(${t}): the window is [${t - 3000}, ${t}].${dropped.length ? ` Drop ${dropped.join(', ')}.` : ''} ${q.length} call${q.length > 1 ? 's' : ''} in range.`, A.arr('queue', q, { hl: { [q.length - 1]: 'ok' } }), A.text('ping returns', q.length, 'ok'));
  }
});
'''),

P(num=649, slug="dota2-senate", title="Dota2 Senate", diff="Medium", topic="Queue", cls="Dota2Senate",
idea="Two queues of senator positions; the earlier senator bans the other and goes to the back of the line (index + n).",
vname="Two queues by turn order",
spec=r'''
Senators from parties `R` and `D` act in order, round after round. Each active senator bans one opponent from all future rounds. When only
one party has active senators, it wins. Return `"Radiant"` or `"Dire"`.

**Example**
```
"RD" → "Radiant",   "RDD" → "Dire"
```

**Constraints**
* `1 <= n <= 10^4`
''',
approach=r'''
**Queues of turn indices.** Queue the positions of each party. Compare the fronts: the earlier one bans the other (who is dropped) and
re-enters its queue at `index + n`, i.e. in the next round.

* Time: **O(n)** — each ban removes one senator.
* Space: **O(n)** — the queues.
''',
java=r'''
public class Dota2Senate {

    public String predictPartyVictory(String senate) {
        int n = senate.length();
        Deque<Integer> r = new ArrayDeque<>(), d = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (senate.charAt(i) == 'R') r.add(i); else d.add(i);
        }
        while (!r.isEmpty() && !d.isEmpty()) {
            int a = r.poll(), b = d.poll();
            if (a < b) r.add(a + n); else d.add(b + n);
        }
        return r.isEmpty() ? "Dire" : "Radiant";
    }
}
''',
test=r'''
class Dota2SenateTest {

    private final Dota2Senate solution = new Dota2Senate();

    @ParameterizedTest
    @CsvSource({"RD,Radiant", "RDD,Dire", "DDRRR,Dire", "RRDDD,Radiant"})
    void predicts(String s, String expected) {
        assertEquals(expected, solution.predictPartyVictory(s));
    }
}
''',
trace=r'''
function run(s) {
  const n = s.length, r = [], d = [];
  [...s].forEach((c, i) => (c === 'R' ? r : d).push(i));
  A.step('Queue each party’s senators by turn. The earlier senator bans the other and returns for the next round.', A.chars('senate', s), A.arr('R turns', r), A.arr('D turns', d));
  while (r.length && d.length) {
    const a = r.shift(), b = d.shift();
    if (a < b) { r.push(a + n); A.step(`R at turn ${a} acts before D at turn ${b}: D is banned. R returns at turn ${a + n}.`, A.arr('R turns', r, { hl: { [r.length - 1]: 'ok' } }), A.arr('D turns', d)); }
    else { d.push(b + n); A.step(`D at turn ${b} acts before R at turn ${a}: R is banned. D returns at turn ${b + n}.`, A.arr('R turns', r), A.arr('D turns', d, { hl: { [d.length - 1]: 'ok' } })); }
  }
  A.step(`${r.length ? 'Radiant' : 'Dire'} wins.`, A.text('Result', r.length ? 'Radiant' : 'Dire', 'ok'));
}
A.scenario('Dire wins', 'senate = "RDD"', () => run('RDD'));
A.scenario('Longer', 'senate = "DDRRR"', () => run('DDRRR'));
'''),

P(num=2095, slug="delete-the-middle-node-of-a-linked-list", title="Delete the Middle Node of a Linked List", diff="Medium", topic="Linked List", cls="DeleteMiddleNode",
idea="Start fast one step ahead so slow stops just before the middle, then unlink it.",
vname="Slow and fast pointers", helpers=["ListNode"],
spec=r'''
Delete the middle node (index `⌊n/2⌋`, 0-based) of a linked list and return the head.

**Example**
```
1→3→4→7→1→2→6 becomes 1→3→4→1→2→6,   1→2→3→4 becomes 1→2→4,   2→1 becomes 2
```

**Constraints**
* `1 <= n <= 10^5`
''',
approach=r'''
**Offset pointers.** With one node, return null. Otherwise start `slow = head`, `fast = head.next.next`; advance slow by 1 and fast by 2.
When fast runs out, `slow.next` is the middle: skip it.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two pointers.
''',
java=r'''
public class DeleteMiddleNode {

    public ListNode deleteMiddle(ListNode head) {
        if (head.next == null) return null;
        ListNode slow = head, fast = head.next.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        slow.next = slow.next.next;
        return head;
    }
}
''',
test=r'''
class DeleteMiddleNodeTest {

    private final DeleteMiddleNode solution = new DeleteMiddleNode();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 3, 4, 1, 2, 6}, ListNode.toArray(solution.deleteMiddle(ListNode.of(1, 3, 4, 7, 1, 2, 6))));
        assertArrayEquals(new int[]{1, 2, 4}, ListNode.toArray(solution.deleteMiddle(ListNode.of(1, 2, 3, 4))));
        assertArrayEquals(new int[]{2}, ListNode.toArray(solution.deleteMiddle(ListNode.of(2, 1))));
        assertNull(solution.deleteMiddle(ListNode.of(1)));
    }
}
''',
trace=r'''
function run(v) {
  let slow = 0, fast = 2;
  A.step('slow starts at the head and fast two nodes ahead, so slow stops just before the middle.', A.list('list', v, { ptr: [[slow, 'slow'], ...(fast < v.length ? [[fast, 'fast']] : [])] }));
  while (fast < v.length && fast + 1 < v.length) { slow++; fast += 2; A.step('slow moves 1, fast moves 2.', A.list('list', v, { ptr: [[slow, 'slow'], ...(fast < v.length ? [[fast, 'fast']] : [])] })); }
  A.step(`slow.next = ${v[slow + 1]} is the middle node. Unlink it.`, A.list('list', v, { ptr: [[slow, 'slow']], hl: { [slow + 1]: 'bad' } }));
  const out = v.filter((_, i) => i !== slow + 1);
  A.step(`Result: ${out.join(' → ')}.`, A.list('list', out));
}
A.scenario('Seven nodes', '1→3→4→7→1→2→6', () => run([1, 3, 4, 7, 1, 2, 6]));
'''),

P(num=2130, slug="maximum-twin-sum-of-a-linked-list", title="Maximum Twin Sum of a Linked List", diff="Medium", topic="Linked List", cls="MaximumTwinSum",
idea="Reverse the second half, then walk both halves together adding twins.",
vname="Reverse second half", helpers=["ListNode"],
spec=r'''
In a linked list of even length `n`, node `i` and node `n - 1 - i` are twins. Return the maximum twin sum.

**Example**
```
5→4→2→1 → 6,   4→2→2→3 → 7,   1→100000 → 100001
```

**Constraints**
* `n` is even, `2 <= n <= 10^5`
''',
approach=r'''
**Half reversal.** Find the middle with slow/fast pointers, reverse the second half, then walk the first half and the reversed second half in
step, summing twins.

* Time: **O(n)** — a few passes.
* Space: **O(1)** — pointers only.
''',
java=r'''
public class MaximumTwinSum {

    public int pairSum(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode prev = null;
        while (slow != null) {
            ListNode next = slow.next;
            slow.next = prev;
            prev = slow;
            slow = next;
        }
        int best = 0;
        for (ListNode a = head, b = prev; b != null; a = a.next, b = b.next) best = Math.max(best, a.val + b.val);
        return best;
    }
}
''',
test=r'''
class MaximumTwinSumTest {

    private final MaximumTwinSum solution = new MaximumTwinSum();

    @Test
    void examples() {
        assertEquals(6, solution.pairSum(ListNode.of(5, 4, 2, 1)));
        assertEquals(7, solution.pairSum(ListNode.of(4, 2, 2, 3)));
        assertEquals(100001, solution.pairSum(ListNode.of(1, 100000)));
    }
}
''',
trace=r'''
function run(v) {
  const half = v.length / 2, first = v.slice(0, half), second = v.slice(half).reverse();
  A.step('Reverse the second half so twins line up.', A.list('first half', first), A.list('second half reversed', second, { hl: second.map((_, i) => [i, 'alt']) }));
  let best = 0;
  first.forEach((x, i) => { const s = x + second[i]; best = Math.max(best, s); A.step(`Twins ${x} + ${second[i]} = ${s}. Best ${best}.`, A.list('first half', first, { hl: { [i]: 'cur' } }), A.list('second half reversed', second, { hl: { [i]: 'cur' } }), A.vars({ best })); });
  A.step(`Maximum twin sum: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Four nodes', '4→2→2→3', () => run([4, 2, 2, 3]));
'''),

P(num=872, slug="leaf-similar-trees", title="Leaf-Similar Trees", diff="Easy", topic="Binary Tree General", cls="LeafSimilarTrees",
idea="Collect each tree's leaves left to right and compare the two sequences.",
vname="Collect leaf sequences", helpers=["TreeNode"],
spec=r'''
Two binary trees are **leaf-similar** if their leaf values, read left to right, form the same sequence. Return whether `root1` and `root2`
are leaf-similar.

**Example**
```
[3,5,1,6,2,9,8,null,null,7,4] and [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8] → true
[1,2,3] and [1,3,2] → false
```

**Constraints**
* `1 <= nodes <= 200`
''',
approach=r'''
**DFS to the leaves.** A left-first DFS lists leaves in left-to-right order; compare the two lists.

* Time: **O(n + m)** — both trees once.
* Space: **O(n + m)** — the leaf lists and recursion.
''',
tc="n", sc="n",
java=r'''
public class LeafSimilarTrees {

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> a = new ArrayList<>(), b = new ArrayList<>();
        leaves(root1, a);
        leaves(root2, b);
        return a.equals(b);
    }

    private void leaves(TreeNode n, List<Integer> out) {
        if (n == null) return;
        if (n.left == null && n.right == null) out.add(n.val);
        leaves(n.left, out);
        leaves(n.right, out);
    }
}
''',
test=r'''
class LeafSimilarTreesTest {

    private final LeafSimilarTrees solution = new LeafSimilarTrees();

    @Test
    void examples() {
        assertTrue(solution.leafSimilar(TreeNode.of(3, 5, 1, 6, 2, 9, 8, null, null, 7, 4),
                TreeNode.of(3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8)));
        assertFalse(solution.leafSimilar(TreeNode.of(1, 2, 3), TreeNode.of(1, 3, 2)));
    }
}
''',
trace=r'''
function run(x, y) {
  const r1 = A.mkTree(x), r2 = A.mkTree(y);
  const leaves = r => { const out = [], hl = {}; (function d(n) { if (!n) return; if (!n.left && !n.right) { out.push(n.val); hl[n.id] = 'ok'; } d(n.left); d(n.right); })(r); return [out, hl]; };
  const [a, ha] = leaves(r1), [b, hb] = leaves(r2);
  A.step(`Tree 1 leaves, left to right: [${a}].`, A.tree('tree 1', r1, { hl: ha }), A.arr('leaves 1', a));
  A.step(`Tree 2 leaves, left to right: [${b}].`, A.tree('tree 2', r2, { hl: hb }), A.arr('leaves 2', b));
  const ok = a.join() === b.join();
  A.step(ok ? 'The sequences are equal.' : 'The sequences differ.', A.arr('leaves 1', a), A.arr('leaves 2', b), A.text('Result', String(ok), ok ? 'ok' : 'bad'));
}
A.scenario('Similar', 'two trees with leaves 6,7,4,9,8', () => run([3, 5, 1, 6, 2, 9, 8, null, null, 7, 4], [3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8]));
'''),

P(num=1448, slug="count-good-nodes-in-binary-tree", title="Count Good Nodes in Binary Tree", diff="Medium", topic="Binary Tree General", cls="CountGoodNodes",
idea="Carry the largest value seen on the path from the root; a node is good if it is at least that large.",
vname="DFS with path maximum", helpers=["TreeNode"],
spec=r'''
A node is **good** if no node on the path from the root to it has a greater value. Return the number of good nodes.

**Example**
```
[3,1,4,3,null,1,5] → 4,   [3,3,null,4,2] → 3,   [1] → 1
```

**Constraints**
* `1 <= n <= 10^5`
''',
approach=r'''
**Path maximum.** `dfs(node, maxSoFar)`: count the node if `node.val >= maxSoFar`, then recurse with `max(maxSoFar, node.val)`.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class CountGoodNodes {

    public int goodNodes(TreeNode root) {
        return dfs(root, Integer.MIN_VALUE);
    }

    private int dfs(TreeNode n, int maxSoFar) {
        if (n == null) return 0;
        int good = n.val >= maxSoFar ? 1 : 0;
        int m = Math.max(maxSoFar, n.val);
        return good + dfs(n.left, m) + dfs(n.right, m);
    }
}
''',
test=r'''
class CountGoodNodesTest {

    private final CountGoodNodes solution = new CountGoodNodes();

    @Test
    void examples() {
        assertEquals(4, solution.goodNodes(TreeNode.of(3, 1, 4, 3, null, 1, 5)));
        assertEquals(3, solution.goodNodes(TreeNode.of(3, 3, null, 4, 2)));
        assertEquals(1, solution.goodNodes(TreeNode.of(1)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {}; let count = 0;
  (function dfs(n, mx) {
    if (!n) return;
    const good = n.val >= mx; if (good) count++;
    hl[n.id] = good ? 'ok' : 'bad';
    A.step(`${n.val}: the largest value above it is ${mx === -Infinity ? 'none' : mx}. ${good ? 'Good.' : 'Not good.'}`, A.tree('tree', root, { hl: { ...hl, [n.id]: good ? 'ok' : 'bad' } }), A.vars({ good: count }));
    dfs(n.left, Math.max(mx, n.val)); dfs(n.right, Math.max(mx, n.val));
  })(root, -Infinity);
  A.step(`${count} good nodes.`, A.text('Result', count, 'ok'));
}
A.scenario('Classic', '[3,1,4,3,null,1,5]', () => run([3, 1, 4, 3, null, 1, 5]));
'''),

P(num=437, slug="path-sum-iii", title="Path Sum III", diff="Medium", topic="Binary Tree General", cls="PathSumIII",
idea="Prefix sums along the root-to-node path: a downward path ending here sums to target when an earlier prefix equals current − target.",
vname="Prefix sums on the path", helpers=["TreeNode"],
spec=r'''
Count the downward paths (from a node to one of its descendants, not necessarily root or leaf) whose values sum to `targetSum`.

**Example**
```
root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8 → 3
```

**Constraints**
* `0 <= n <= 1000`; sums may need 64 bits.
''',
approach=r'''
**Prefix-sum counts.** Keep a `MyHashMap` of prefix sums on the current root-to-node path. At each node, add the count of
`prefix - target`, insert the new prefix, recurse, then remove it when backtracking.

* Time: **O(n)** — O(1) map work per node.
* Space: **O(h)** — the map holds one entry per path node, plus the recursion.
''',
tc="n", sc="n",
java=r'''
public class PathSumIII {

    private final MyHashMap<Long, Integer> prefix = new MyHashMap<>();

    public int pathSum(TreeNode root, int targetSum) {
        prefix.put(0L, 1);
        return dfs(root, 0L, targetSum);
    }

    private int dfs(TreeNode n, long sum, int target) {
        if (n == null) return 0;
        sum += n.val;
        int count = prefix.getOrDefault(sum - target, 0);
        prefix.merge(sum, 1, Integer::sum);
        count += dfs(n.left, sum, target) + dfs(n.right, sum, target);
        prefix.merge(sum, -1, Integer::sum);
        return count;
    }
}
''',
test=r'''
class PathSumIIITest {

    @Test
    void examples() {
        assertEquals(3, new PathSumIII().pathSum(TreeNode.of(10, 5, -3, 3, 2, null, 11, 3, -2, null, 1), 8));
        assertEquals(3, new PathSumIII().pathSum(TreeNode.of(5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1), 22));
    }

    @Test
    void largeValues() {
        assertEquals(0, new PathSumIII().pathSum(TreeNode.of(1000000000, 1000000000, null, 294967296, null, 1000000000, null, 1000000000, null, 1000000000), 0));
    }
}
''',
trace=r'''
function run(arr, target) {
  const root = A.mkTree(arr), pre = new Map([[0, 1]]), path = []; let count = 0;
  (function dfs(n, sum) {
    if (!n) return;
    sum += n.val; path.push(n.id);
    const hits = pre.get(sum - target) || 0; count += hits;
    pre.set(sum, (pre.get(sum) || 0) + 1);
    A.step(`${n.val}: path sum ${sum}. Earlier prefix ${sum} − ${target} = ${sum - target} occurs ${hits} time${hits === 1 ? '' : 's'}, so ${hits} path${hits === 1 ? '' : 's'} end here.`, A.tree('tree', root, { hl: Object.fromEntries(path.map(id => [id, id === n.id ? 'cur' : 'sel'])) }), A.hashTable('prefix sums on path', pre, { hl: sum - target }), A.vars({ count }));
    dfs(n.left, sum); dfs(n.right, sum);
    pre.set(sum, pre.get(sum) - 1); if (!pre.get(sum)) pre.delete(sum); path.pop();
  })(root, 0);
  A.step(`${count} downward paths sum to ${target}.`, A.text('Result', count, 'ok'));
}
A.scenario('target = 8', '[10,5,-3,3,2,null,11,3,-2,null,1]', () => run([10, 5, -3, 3, 2, null, 11, 3, -2, null, 1], 8));
'''),

P(num=1372, slug="longest-zigzag-path-in-a-binary-tree", title="Longest ZigZag Path in a Binary Tree", diff="Medium", topic="Binary Tree General", cls="LongestZigZag",
idea="Each node knows the zigzag length arriving from the left and from the right; turning extends, going straight restarts.",
vname="DFS with two lengths", helpers=["TreeNode"],
spec=r'''
A zigzag path alternates between left and right child moves. Its length is the number of edges. Return the longest zigzag path in the tree.

**Example**
```
[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1] → 3
[1,1,1,null,1,null,null,1,1,null,1]                  → 4
```

**Constraints**
* `1 <= n <= 5 * 10^4`
''',
approach=r'''
**Carry both directions.** `dfs(node, leftLen, rightLen)`: `leftLen` is the zigzag length if the last move was to the left (so the next
must go right). Going left continues `rightLen + 1` and resets the other to 0; going right continues `leftLen + 1`.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class LongestZigZag {

    private int best;

    public int longestZigZag(TreeNode root) {
        best = 0;
        dfs(root, 0, 0);
        return best;
    }

    /** left: length of a zigzag that arrived here by a left move; right: by a right move. */
    private void dfs(TreeNode n, int left, int right) {
        if (n == null) return;
        best = Math.max(best, Math.max(left, right));
        dfs(n.left, right + 1, 0);
        dfs(n.right, 0, left + 1);
    }
}
''',
test=r'''
class LongestZigZagTest {

    private final LongestZigZag solution = new LongestZigZag();

    @Test
    void examples() {
        assertEquals(3, solution.longestZigZag(TreeNode.of(1, null, 1, 1, 1, null, null, 1, 1, null, 1, null, null, null, 1)));
        assertEquals(4, solution.longestZigZag(TreeNode.of(1, 1, 1, null, 1, null, null, 1, 1, null, 1)));
        assertEquals(0, solution.longestZigZag(TreeNode.of(1)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {}; let best = 0, bestId = null;
  (function dfs(n, l, r) {
    if (!n) return;
    if (Math.max(l, r) > best) { best = Math.max(l, r); bestId = n.id; }
    hl[n.id] = 'sel';
    A.step(`At this node: a zigzag arriving by a left move has length ${l}; by a right move, ${r}. Best ${best}.`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'cur' } }), A.vars({ arrivedLeft: l, arrivedRight: r, best }));
    dfs(n.left, r + 1, 0); dfs(n.right, 0, l + 1);
  })(root, 0, 0);
  A.step(`The longest zigzag has ${best} edges.`, A.tree('tree', root, { hl: { [bestId]: 'ok' } }), A.text('Result', best, 'ok'));
}
A.scenario('Length 4', '[1,1,1,null,1,null,null,1,1,null,1]', () => run([1, 1, 1, null, 1, null, null, 1, 1, null, 1]));
'''),

P(num=1161, slug="maximum-level-sum-of-a-binary-tree", title="Maximum Level Sum of a Binary Tree", diff="Medium", topic="Binary Tree BFS", cls="MaximumLevelSum",
idea="Sum each level with BFS and keep the smallest level number with the largest sum.",
vname="Level-order BFS", helpers=["TreeNode"],
spec=r'''
The root is level 1, its children level 2, and so on. Return the smallest level whose node values have the maximal sum.

**Example**
```
[1,7,0,7,-8,null,null] → 2,   [989,null,10250,98693,-89388,null,null,null,-32127] → 2
```

**Constraints**
* `1 <= n <= 10^4`
''',
approach=r'''
**BFS by levels.** Sum each level; update the answer only on a strictly larger sum, so ties keep the smaller level.

* Time: **O(n)** — each node once.
* Space: **O(w)** — the widest level.
''',
tc="n", sc="n",
java=r'''
public class MaximumLevelSum {

    public int maxLevelSum(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        int best = Integer.MIN_VALUE, bestLevel = 0;
        for (int level = 1; !queue.isEmpty(); level++) {
            int sum = 0;
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                sum += n.val;
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
            if (sum > best) {
                best = sum;
                bestLevel = level;
            }
        }
        return bestLevel;
    }
}
''',
test=r'''
class MaximumLevelSumTest {

    private final MaximumLevelSum solution = new MaximumLevelSum();

    @Test
    void examples() {
        assertEquals(2, solution.maxLevelSum(TreeNode.of(1, 7, 0, 7, -8, null, null)));
        assertEquals(2, solution.maxLevelSum(TreeNode.of(989, null, 10250, 98693, -89388, null, null, null, -32127)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {}; let q = [root], best = -Infinity, bl = 0;
  for (let lvl = 1; q.length; lvl++) {
    const s = q.reduce((t, n) => t + n.val, 0), nb = s > best; if (nb) { best = s; bl = lvl; }
    q.forEach(n => (hl[n.id] = nb ? 'ok' : 'sel'));
    A.step(`Level ${lvl}: ${q.map(n => n.val).join(' + ')} = ${s}.${nb ? ' New best.' : ''}`, A.tree('tree', root, { hl }), A.vars({ bestSum: best, bestLevel: bl }));
    q = q.flatMap(n => [n.left, n.right].filter(Boolean));
  }
  A.step(`Level ${bl} has the largest sum (${best}).`, A.text('Result', bl, 'ok'));
}
A.scenario('Classic', '[1,7,0,7,-8,null,null]', () => run([1, 7, 0, 7, -8, null, null]));
'''),
]
