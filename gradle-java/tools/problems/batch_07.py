PROBLEMS = [
P(num=92, slug="reverse-linked-list-ii", title="Reverse Linked List II", diff="Medium", topic="Linked List", cls="ReverseLinkedListII",
idea="Walk to the node before position left, then repeatedly move the next node to the front of the sub-list.",
vname="One pass, head insertion", helpers=["ListNode"],
spec=r'''
Given the `head` of a singly linked list and positions `left <= right` (1-based), reverse the nodes from position `left` to
`right` and return the list.

**Example 1**
```
Input:  head = 1 → 2 → 3 → 4 → 5, left = 2, right = 4
Output: 1 → 4 → 3 → 2 → 5
```

**Example 2**
```
Input:  head = 5, left = 1, right = 1
Output: 5
```

**Constraints**
* `1 <= n <= 500`; `1 <= left <= right <= n`

**Follow-up:** one pass.
''',
approach=r'''
**Head insertion.** Use a dummy node and move `prev` to the node just before `left`. Let `cur = prev.next`; `right - left` times,
take the node after `cur` and insert it right after `prev`. Each move pushes one more node to the front of the reversed part.

* Time: **O(n)** — one walk to `left`, then `right - left` constant-time moves.
* Space: **O(1)** — a few pointers.
''',
java=r'''
public class ReverseLinkedListII {

    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(0, head), prev = dummy;
        for (int i = 1; i < left; i++) prev = prev.next;
        ListNode cur = prev.next;
        for (int i = 0; i < right - left; i++) {
            ListNode move = cur.next;
            cur.next = move.next;
            move.next = prev.next;
            prev.next = move;
        }
        return dummy.next;
    }
}
''',
test=r'''
class ReverseLinkedListIITest {

    private final ReverseLinkedListII solution = new ReverseLinkedListII();

    @Test
    void middle() {
        assertArrayEquals(new int[]{1, 4, 3, 2, 5}, ListNode.toArray(solution.reverseBetween(ListNode.of(1, 2, 3, 4, 5), 2, 4)));
    }

    @Test
    void single() {
        assertArrayEquals(new int[]{5}, ListNode.toArray(solution.reverseBetween(ListNode.of(5), 1, 1)));
    }

    @Test
    void whole() {
        assertArrayEquals(new int[]{3, 2, 1}, ListNode.toArray(solution.reverseBetween(ListNode.of(1, 2, 3), 1, 3)));
    }
}
''',
trace=r'''
function run(vals, left, right) {
  const a = vals.slice();
  const p = left - 2; // index of prev (-1 = dummy)
  A.step(`Reverse positions ${left} to ${right}. prev stops just before position ${left}; cur is the first node of the section.`, A.list('list', a, { range: [left - 1, right - 1], ptr: [...(p >= 0 ? [[p, 'prev']] : []), [left - 1, 'cur']] }));
  let curIdx = left - 1;
  for (let k = 0; k < right - left; k++) {
    const moveIdx = curIdx + 1, v = a[moveIdx];
    a.splice(moveIdx, 1); a.splice(left - 1, 0, v); curIdx++;
    A.step(`Take ${v}, the node after cur, and insert it right after prev. It is now at the front of the section.`, A.list('list', a, { range: [left - 1, right - 1], ptr: [...(p >= 0 ? [[p, 'prev']] : []), [curIdx, 'cur']], hl: { [left - 1]: 'ok', [curIdx]: 'cur' } }));
  }
  A.step(`Positions ${left} to ${right} are reversed in one pass.`, A.list('list', a, { hl: a.map((_, i) => [i, i >= left - 1 && i <= right - 1 ? 'ok' : '']) }), A.text('Result', a.join(' → '), 'ok'));
}
A.scenario('Middle section', '1→2→3→4→5, left = 2, right = 4', () => run([1, 2, 3, 4, 5], 2, 4));
A.scenario('Whole list', '1→2→3, left = 1, right = 3', () => run([1, 2, 3], 1, 3));
'''),

P(num=25, slug="reverse-nodes-in-k-group", title="Reverse Nodes in k-Group", diff="Hard", topic="Linked List", cls="ReverseKGroup",
idea="For each full group of k nodes, reverse it in place and stitch it between the previous group and the rest.",
vname="Iterative group reversal", helpers=["ListNode"],
spec=r'''
Reverse the nodes of a linked list `k` at a time and return the new head. If the number of remaining nodes is less than `k`,
leave them as they are. Only change the links, not the values.

**Example 1**
```
Input:  head = 1 → 2 → 3 → 4 → 5, k = 2
Output: 2 → 1 → 4 → 3 → 5
```

**Example 2**
```
Input:  head = 1 → 2 → 3 → 4 → 5, k = 3
Output: 3 → 2 → 1 → 4 → 5
```

**Constraints**
* `1 <= k <= n <= 5000`

**Follow-up:** O(1) extra memory.
''',
approach=r'''
**Group by group.** `groupPrev` is the node before the current group. Check that `k` nodes follow; if not, stop. Reverse those `k`
nodes with the usual three-pointer loop, then connect `groupPrev` to the new group head and the old group head (now the tail) to
the next group. Move `groupPrev` to that tail.

* Time: **O(n)** — each node is checked once and reversed once.
* Space: **O(1)** — a fixed number of pointers.
''',
java=r'''
public class ReverseKGroup {

    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0, head), groupPrev = dummy;
        while (true) {
            ListNode kth = groupPrev;
            for (int i = 0; i < k && kth != null; i++) kth = kth.next;
            if (kth == null) break;
            ListNode groupNext = kth.next, prev = groupNext, cur = groupPrev.next;
            while (cur != groupNext) {
                ListNode next = cur.next;
                cur.next = prev;
                prev = cur;
                cur = next;
            }
            ListNode oldHead = groupPrev.next;
            groupPrev.next = kth;
            groupPrev = oldHead;
        }
        return dummy.next;
    }
}
''',
test=r'''
class ReverseKGroupTest {

    private final ReverseKGroup solution = new ReverseKGroup();

    @Test
    void pairs() {
        assertArrayEquals(new int[]{2, 1, 4, 3, 5}, ListNode.toArray(solution.reverseKGroup(ListNode.of(1, 2, 3, 4, 5), 2)));
    }

    @Test
    void triples() {
        assertArrayEquals(new int[]{3, 2, 1, 4, 5}, ListNode.toArray(solution.reverseKGroup(ListNode.of(1, 2, 3, 4, 5), 3)));
    }

    @Test
    void kOne() {
        assertArrayEquals(new int[]{1, 2}, ListNode.toArray(solution.reverseKGroup(ListNode.of(1, 2), 1)));
    }
}
''',
trace=r'''
function run(vals, k) {
  const a = vals.slice();
  A.step(`Split the list into groups of ${k}. Full groups get reversed; a short last group stays as it is.`, A.list('list', a, { hl: a.map((_, i) => [i, Math.floor(i / k) % 2 ? 'alt' : 'sel']) }));
  for (let s = 0; ; s += k) {
    if (s + k > a.length) { A.step(`Only ${a.length - s} node${a.length - s === 1 ? '' : 's'} left, fewer than ${k}. Leave them unchanged.`, A.list('list', a, { range: [s, a.length - 1] })); break; }
    A.step(`Group ${s / k + 1}: nodes ${a.slice(s, s + k).join(', ')}. Reverse their links.`, A.list('list', a, { range: [s, s + k - 1], hl: { [s]: 'cur', [s + k - 1]: 'cur' } }));
    const g = a.slice(s, s + k).reverse(); a.splice(s, k, ...g);
    A.step(`Reversed and stitched back in: the previous group now points to ${g[0]}, and ${g[k - 1]} points to the next group.`, A.list('list', a, { range: [s, s + k - 1], hl: [...Array(k).keys()].map(t => [s + t, 'ok']) }));
  }
  A.step(`Result: ${a.join(' → ')}.`, A.text('Result', a.join(' → '), 'ok'));
}
A.scenario('k = 2', '1→2→3→4→5', () => run([1, 2, 3, 4, 5], 2));
A.scenario('k = 3', '1→2→3→4→5', () => run([1, 2, 3, 4, 5], 3));
'''),

P(num=19, slug="remove-nth-node-from-end-of-list", title="Remove Nth Node From End of List", diff="Medium", topic="Linked List", cls="RemoveNthFromEnd",
idea="Send a lead pointer n steps ahead; when it falls off the end, the trailing pointer sits just before the target.",
vname="One pass, gap of n", helpers=["ListNode"],
spec=r'''
Remove the `n`-th node from the **end** of the list and return its head.

**Example 1**
```
Input:  head = 1 → 2 → 3 → 4 → 5, n = 2
Output: 1 → 2 → 3 → 5
```

**Example 2**
```
Input:  head = 1, n = 1
Output: (empty)
```

**Constraints**
* `1 <= sz <= 30`; `1 <= n <= sz`

**Follow-up:** one pass.
''',
approach=r'''
**Two pointers with a gap.** Start `fast` and `slow` at a dummy node. Move `fast` `n + 1` steps. Then move both until `fast` is
`null`: `slow` is now just before the node to delete, so set `slow.next = slow.next.next`.

* Time: **O(L)** — one pass over the list.
* Space: **O(1)** — two pointers.
''',
tc="n",
java=r'''
public class RemoveNthFromEnd {

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head), fast = dummy, slow = dummy;
        for (int i = 0; i <= n; i++) fast = fast.next;
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }
}
''',
test=r'''
class RemoveNthFromEndTest {

    private final RemoveNthFromEnd solution = new RemoveNthFromEnd();

    @Test
    void middle() {
        assertArrayEquals(new int[]{1, 2, 3, 5}, ListNode.toArray(solution.removeNthFromEnd(ListNode.of(1, 2, 3, 4, 5), 2)));
    }

    @Test
    void onlyNode() {
        assertNull(solution.removeNthFromEnd(ListNode.of(1), 1));
    }

    @Test
    void head() {
        assertArrayEquals(new int[]{2}, ListNode.toArray(solution.removeNthFromEnd(ListNode.of(1, 2), 2)));
    }
}
''',
trace=r'''
function run(vals, n) {
  const a = ['D', ...vals]; // index 0 is the dummy
  let fast = 0, slow = 0;
  A.step(`A dummy node D sits before the head. Move fast ${n + 1} steps ahead of slow.`, A.list('list', a, { ptr: [[0, 'slow,fast']], hl: { 0: 'dim' } }));
  for (let i = 0; i <= n; i++) fast++;
  A.step(`fast is now ${n + 1} nodes ahead${fast >= a.length ? ', already past the end' : ''}.`, A.list('list', a, { ptr: [[slow, 'slow'], ...(fast < a.length ? [[fast, 'fast']] : [])], hl: { 0: 'dim' } }));
  while (fast < a.length) { fast++; slow++; A.step('Move both pointers one step; the gap stays the same.', A.list('list', a, { ptr: [[slow, 'slow'], ...(fast < a.length ? [[fast, 'fast']] : [])], hl: { 0: 'dim' } })); }
  A.step(`fast fell off the end, so slow is right before the ${n}th node from the end: ${a[slow + 1]}. Unlink it.`, A.list('list', a, { ptr: [[slow, 'slow']], hl: { 0: 'dim', [slow + 1]: 'bad' } }));
  a.splice(slow + 1, 1);
  A.step(`Result: ${a.slice(1).join(' → ') || '(empty)'}.`, A.list('list', a.slice(1), { hl: a.slice(1).map((_, i) => [i, 'ok']) }));
}
A.scenario('Remove 2nd from end', '1→2→3→4→5, n = 2', () => run([1, 2, 3, 4, 5], 2));
A.scenario('Edge: remove the head', '1→2, n = 2', () => run([1, 2], 2));
''',
variants=[dict(
name="Count length, then remove",
idea="First count the nodes, then walk to position length − n.",
approach=r'''
**Two passes.** Count the length `L`. The node to remove is at index `L - n`; walk `L - n` steps from a dummy and unlink the next node.

* Time: **O(L)** — two passes.
* Space: **O(1)** — a counter and a pointer.
''',
tc="n",
java=r'''
public class RemoveNthFromEnd {

    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length = 0;
        for (ListNode p = head; p != null; p = p.next) length++;
        ListNode dummy = new ListNode(0, head), prev = dummy;
        for (int i = 0; i < length - n; i++) prev = prev.next;
        prev.next = prev.next.next;
        return dummy.next;
    }
}
''',
trace=r'''
function run(vals, n) {
  const L = vals.length;
  vals.forEach((_, i) => A.step(`Pass 1: count node ${i + 1}.`, A.list('list', vals, { ptr: [[i, 'p']], hl: { [i]: 'cur' } }), A.vars({ length: i + 1 })));
  A.step(`Pass 2: the target is at index ${L} − ${n} = ${L - n}. Walk there and unlink it.`, A.list('list', vals, { hl: { [L - n]: 'bad' } }));
  const out = vals.filter((_, i) => i !== L - n);
  A.step(`Result: ${out.join(' → ') || '(empty)'}. Two passes instead of one.`, A.list('list', out));
}
A.scenario('Remove 2nd from end', '1→2→3→4→5, n = 2', () => run([1, 2, 3, 4, 5], 2));
''')]),

P(num=82, slug="remove-duplicates-from-sorted-list-ii", title="Remove Duplicates from Sorted List II", diff="Medium", topic="Linked List", cls="RemoveDuplicatesListII",
idea="When a value repeats, skip the whole run; otherwise keep the node.",
vname="Skip whole runs", helpers=["ListNode"],
spec=r'''
Given the head of a **sorted** linked list, delete every node whose value appears more than once, leaving only values that were
distinct in the original list. Return the sorted result.

**Example 1**
```
Input:  1 → 2 → 3 → 3 → 4 → 4 → 5
Output: 1 → 2 → 5
```

**Example 2**
```
Input:  1 → 1 → 1 → 2 → 3
Output: 2 → 3
```

**Constraints**
* `0 <= n <= 300`; sorted ascending.
''',
approach=r'''
**Dummy + prev.** `prev` is the last kept node. If `cur` starts a run (`cur.next.val == cur.val`), advance past the whole run and set
`prev.next` to the node after it. Otherwise keep `cur`: `prev = cur`.

* Time: **O(n)** — each node is visited once.
* Space: **O(1)** — pointers only.
''',
java=r'''
public class RemoveDuplicatesListII {

    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0, head), prev = dummy, cur = head;
        while (cur != null) {
            if (cur.next != null && cur.next.val == cur.val) {
                int dup = cur.val;
                while (cur != null && cur.val == dup) cur = cur.next;
                prev.next = cur;
            } else {
                prev = cur;
                cur = cur.next;
            }
        }
        return dummy.next;
    }
}
''',
test=r'''
class RemoveDuplicatesListIITest {

    private final RemoveDuplicatesListII solution = new RemoveDuplicatesListII();

    @Test
    void middleRuns() {
        assertArrayEquals(new int[]{1, 2, 5}, ListNode.toArray(solution.deleteDuplicates(ListNode.of(1, 2, 3, 3, 4, 4, 5))));
    }

    @Test
    void runAtHead() {
        assertArrayEquals(new int[]{2, 3}, ListNode.toArray(solution.deleteDuplicates(ListNode.of(1, 1, 1, 2, 3))));
    }

    @Test
    void allDuplicates() {
        assertNull(solution.deleteDuplicates(ListNode.of(1, 1)));
    }
}
''',
trace=r'''
function run(a) {
  const keep = []; const hl = [];
  A.step('Walk the sorted list. A value that repeats is removed entirely, run and all.', A.list('list', a));
  for (let i = 0; i < a.length;) {
    if (i + 1 < a.length && a[i + 1] === a[i]) {
      let j = i; while (j < a.length && a[j] === a[i]) { hl.push([j, 'bad']); j++; }
      A.step(`${a[i]} repeats ${j - i} times. Skip the whole run; prev now links past it.`, A.list('list', a, { hl: hl.slice(), ptr: [[i, 'run start']] }), A.list('kept', keep));
      i = j;
    } else { keep.push(a[i]); hl.push([i, 'ok']); A.step(`${a[i]} appears once. Keep it.`, A.list('list', a, { hl: hl.slice(), ptr: [[i, 'cur']] }), A.list('kept', keep, { hl: { [keep.length - 1]: 'ok' } })); i++; }
  }
  A.step(`Result: ${keep.join(' → ') || '(empty)'}.`, A.list('kept', keep));
}
A.scenario('Runs in the middle', '1→2→3→3→4→4→5', () => run([1, 2, 3, 3, 4, 4, 5]));
A.scenario('Run at the head', '1→1→1→2→3', () => run([1, 1, 1, 2, 3]));
'''),

P(num=61, slug="rotate-list", title="Rotate List", diff="Medium", topic="Linked List", cls="RotateList",
idea="Close the list into a ring, then cut it n − k mod n nodes after the old head.",
vname="Ring and cut", helpers=["ListNode"],
spec=r'''
Rotate a linked list to the right by `k` places and return the new head.

**Example 1**
```
Input:  1 → 2 → 3 → 4 → 5, k = 2
Output: 4 → 5 → 1 → 2 → 3
```

**Example 2**
```
Input:  0 → 1 → 2, k = 4
Output: 2 → 0 → 1
```

**Constraints**
* `0 <= n <= 500`; `0 <= k <= 2 * 10^9`
''',
approach=r'''
**Ring.** Find the length `n` and the tail; link the tail to the head. The new tail is `n - k % n - 1` steps from the old head; the new
head is the node after it. Break the ring there.

* Time: **O(n)** — at most two passes.
* Space: **O(1)** — pointers only.
''',
java=r'''
public class RotateList {

    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) return head;
        int n = 1;
        ListNode tail = head;
        while (tail.next != null) {
            tail = tail.next;
            n++;
        }
        tail.next = head;
        ListNode newTail = head;
        for (int i = 0; i < n - k % n - 1; i++) newTail = newTail.next;
        ListNode newHead = newTail.next;
        newTail.next = null;
        return newHead;
    }
}
''',
test=r'''
class RotateListTest {

    private final RotateList solution = new RotateList();

    @Test
    void byTwo() {
        assertArrayEquals(new int[]{4, 5, 1, 2, 3}, ListNode.toArray(solution.rotateRight(ListNode.of(1, 2, 3, 4, 5), 2)));
    }

    @Test
    void kLargerThanLength() {
        assertArrayEquals(new int[]{2, 0, 1}, ListNode.toArray(solution.rotateRight(ListNode.of(0, 1, 2), 4)));
    }

    @Test
    void empty() {
        assertNull(solution.rotateRight(null, 3));
    }
}
''',
trace=r'''
function run(a, k) {
  const n = a.length, cut = n - (k % n) - 1;
  A.step(`Find the length (${n}) and the tail (${a[n - 1]}). Link the tail back to the head to make a ring.`, A.list('list', a, { ptr: [[0, 'head'], [n - 1, 'tail']], note: `back to ${a[0]}` }));
  A.step(`Rotating by ${k} is the same as rotating by ${k} mod ${n} = ${k % n}. The new tail is ${cut} step${cut === 1 ? '' : 's'} from the head: ${a[cut]}.`, A.list('list', a, { ptr: [[cut, 'new tail'], [(cut + 1) % n, 'new head']], hl: { [cut]: 'bad', [(cut + 1) % n]: 'ok' }, note: `back to ${a[0]}` }));
  const out = a.slice(cut + 1).concat(a.slice(0, cut + 1));
  A.step(`Break the ring after ${a[cut]}. The list now starts at ${out[0]}.`, A.list('list', out, { hl: { 0: 'ok' } }), A.text('Result', out.join(' → '), 'ok'));
}
A.scenario('k = 2', '1→2→3→4→5', () => run([1, 2, 3, 4, 5], 2));
A.scenario('k larger than n', '0→1→2, k = 4', () => run([0, 1, 2], 4));
'''),

P(num=86, slug="partition-list", title="Partition List", diff="Medium", topic="Linked List", cls="PartitionList",
idea="Build two chains, nodes below x and the rest, preserving order, then join them.",
vname="Two chains", helpers=["ListNode"],
spec=r'''
Given the head of a linked list and a value `x`, rearrange it so that all nodes **less than** `x` come before nodes greater than or
equal to `x`. Keep the original relative order inside each part.

**Example 1**
```
Input:  1 → 4 → 3 → 2 → 5 → 2, x = 3
Output: 1 → 2 → 2 → 4 → 3 → 5
```

**Example 2**
```
Input:  2 → 1, x = 2
Output: 1 → 2
```

**Constraints**
* `0 <= n <= 200`; `-100 <= Node.val <= 100`; `-200 <= x <= 200`
''',
approach=r'''
**Two dummy heads.** Append each node to the `less` chain or the `rest` chain. Then terminate `rest` and link `less`'s tail to `rest`'s head.

* Time: **O(n)** — one pass.
* Space: **O(1)** — nodes are re-linked, not copied.
''',
java=r'''
public class PartitionList {

    public ListNode partition(ListNode head, int x) {
        ListNode lessHead = new ListNode(0), restHead = new ListNode(0), less = lessHead, rest = restHead;
        for (ListNode n = head; n != null; n = n.next) {
            if (n.val < x) {
                less.next = n;
                less = n;
            } else {
                rest.next = n;
                rest = n;
            }
        }
        rest.next = null;
        less.next = restHead.next;
        return lessHead.next;
    }
}
''',
test=r'''
class PartitionListTest {

    private final PartitionList solution = new PartitionList();

    @Test
    void example1() {
        assertArrayEquals(new int[]{1, 2, 2, 4, 3, 5}, ListNode.toArray(solution.partition(ListNode.of(1, 4, 3, 2, 5, 2), 3)));
    }

    @Test
    void twoNodes() {
        assertArrayEquals(new int[]{1, 2}, ListNode.toArray(solution.partition(ListNode.of(2, 1), 2)));
    }

    @Test
    void empty() {
        assertNull(solution.partition(null, 0));
    }
}
''',
trace=r'''
function run(a, x) {
  const less = [], rest = [];
  A.step(`Send each node to one of two chains: less than ${x}, or the rest.`, A.list('list', a), A.list('less', less), A.list('rest', rest));
  a.forEach((v, i) => {
    (v < x ? less : rest).push(v);
    A.step(`${v} ${v < x ? '<' : '≥'} ${x}: append it to ${v < x ? 'less' : 'rest'}.`, A.list('list', a, { hl: { [i]: 'cur' } }), A.list('less', less, { hl: v < x ? { [less.length - 1]: 'ok' } : {} }), A.list('rest', rest, { hl: v >= x ? { [rest.length - 1]: 'alt' } : {} }));
  });
  const out = less.concat(rest);
  A.step('Link the tail of less to the head of rest.', A.list('result', out, { hl: out.map((_, i) => [i, i < less.length ? 'ok' : 'alt']) }));
}
A.scenario('Classic', '1→4→3→2→5→2, x = 3', () => run([1, 4, 3, 2, 5, 2], 3));
'''),

P(num=146, slug="lru-cache", title="LRU Cache", diff="Medium", topic="Linked List", cls="LRUCache",
idea="A hash map finds nodes in O(1); a doubly linked list keeps them in recency order so the oldest is at the tail.",
vname="Hash map + doubly linked list",
spec=r'''
Design a **Least Recently Used** cache with a fixed `capacity`:
* `int get(int key)`: return the value if the key exists, otherwise `-1`. A successful get marks the key as most recently used.
* `void put(int key, int value)`: insert or update the key. If this exceeds the capacity, evict the **least recently used** key.

Both operations must run in **O(1)** average time.

**Example**
```
LRUCache(2); put(1,1); put(2,2); get(1) → 1; put(3,3) evicts 2; get(2) → -1;
put(4,4) evicts 1; get(1) → -1; get(3) → 3; get(4) → 4
```

**Constraints**
* `1 <= capacity <= 3000`; at most `2 * 10^5` calls.
''',
approach=r'''
**`MyHashMap<key, node>` + doubly linked list.** The list runs from most recent (after `head`) to least recent (before `tail`), with two
sentinel nodes so there are no null checks. `get` moves the node to the front. `put` updates or inserts at the front; if the size
exceeds capacity, remove the node before `tail` and delete its key from the map. No `java.util.LinkedHashMap` is used.

* Time: **O(1)** — average per operation: hash lookups plus constant pointer changes.
* Space: **O(capacity)** — one node and one map entry per cached key.
''',
sc="n",
java=r'''
public class LRUCache {

    private static final class Node {
        int key, value;
        Node prev, next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    private final int capacity;
    private final MyHashMap<Integer, Node> nodes = new MyHashMap<>();
    private final Node head = new Node(0, 0), tail = new Node(0, 0); // sentinels

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        Node n = nodes.get(key);
        if (n == null) return -1;
        unlink(n);
        addFront(n);
        return n.value;
    }

    public void put(int key, int value) {
        Node n = nodes.get(key);
        if (n != null) {
            n.value = value;
            unlink(n);
            addFront(n);
            return;
        }
        n = new Node(key, value);
        nodes.put(key, n);
        addFront(n);
        if (nodes.size() > capacity) {
            Node lru = tail.prev;
            unlink(lru);
            nodes.remove(lru.key);
        }
    }

    private void unlink(Node n) {
        n.prev.next = n.next;
        n.next.prev = n.prev;
    }

    private void addFront(Node n) {
        n.next = head.next;
        n.prev = head;
        head.next.prev = n;
        head.next = n;
    }
}
''',
test=r'''
class LRUCacheTest {

    @Test
    void example() {
        LRUCache c = new LRUCache(2);
        c.put(1, 1);
        c.put(2, 2);
        assertEquals(1, c.get(1));
        c.put(3, 3);
        assertEquals(-1, c.get(2));
        c.put(4, 4);
        assertEquals(-1, c.get(1));
        assertEquals(3, c.get(3));
        assertEquals(4, c.get(4));
    }

    @Test
    void updateRefreshesRecency() {
        LRUCache c = new LRUCache(2);
        c.put(1, 1);
        c.put(2, 2);
        c.put(1, 10);
        c.put(3, 3);
        assertEquals(10, c.get(1));
        assertEquals(-1, c.get(2));
    }
}
''',
trace=r'''
A.scenario('Capacity 2', 'put 1, put 2, get 1, put 3, get 2, put 4, get 1, get 3', () => {
  const order = [], map = new Map(), cap = 2; // order[0] = most recent
  const view = (hl, msg) => A.step(msg, A.list('recency list (most → least recent)', order.map(k => `${k}:${map.get(k)}`), { hl, note: 'tail' }), A.hashTable('key → node (MyHashMap)', new Map(order.map(k => [k, `${k}:${map.get(k)}`]))));
  view({}, 'The list orders keys from most to least recently used; the map finds any node in O(1).');
  const touch = k => { order.splice(order.indexOf(k), 1); order.unshift(k); };
  const put = (k, v) => {
    if (map.has(k)) { map.set(k, v); touch(k); view({ 0: 'ok' }, `put(${k}, ${v}): the key exists, so update it and move it to the front.`); return; }
    map.set(k, v); order.unshift(k);
    if (order.length > cap) { const old = order[order.length - 1]; view({ 0: 'ok', [order.length - 1]: 'bad' }, `put(${k}, ${v}): insert at the front. That exceeds capacity ${cap}, so evict ${old}, the least recently used key.`); order.pop(); map.delete(old); view({ 0: 'ok' }, `${old} is gone from both the list and the map.`); }
    else view({ 0: 'ok' }, `put(${k}, ${v}): insert at the front.`);
  };
  const get = k => {
    if (!map.has(k)) { view({}, `get(${k}): not in the map, so return -1.`); return; }
    touch(k); view({ 0: 'cur' }, `get(${k}) returns ${map.get(k)} and moves ${k} to the front: it is now the most recent.`);
  };
  put(1, 1); put(2, 2); get(1); put(3, 3); get(2); put(4, 4); get(1); get(3);
});
'''),

P(num=104, slug="maximum-depth-of-binary-tree", title="Maximum Depth of Binary Tree", diff="Easy", topic="Binary Tree General", cls="MaximumDepth",
idea="The depth of a tree is one more than the deeper of its two subtrees.",
vname="Recursive DFS", helpers=["TreeNode"],
spec=r'''
Return the **maximum depth** of a binary tree: the number of nodes on the longest path from the root down to a leaf.

**Example 1**
```
Input:  root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2**
```
Input:  root = [1,null,2]
Output: 2
```

**Constraints**
* `0 <= n <= 10^4`; `-100 <= Node.val <= 100`
''',
approach=r'''
**Recursion.** `depth(null) = 0`; otherwise `1 + max(depth(left), depth(right))`.

* Time: **O(n)** — each node is visited once.
* Space: **O(h)** — the recursion stack, where h is the tree height (O(n) when skewed).
''',
tc="n", sc="n",
java=r'''
public class MaximumDepth {

    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
''',
test=r'''
class MaximumDepthTest {

    private final MaximumDepth solution = new MaximumDepth();

    @Test
    void balanced() {
        assertEquals(3, solution.maxDepth(TreeNode.of(3, 9, 20, null, null, 15, 7)));
    }

    @Test
    void rightOnly() {
        assertEquals(2, solution.maxDepth(TreeNode.of(1, null, 2)));
    }

    @Test
    void empty() {
        assertEquals(0, solution.maxDepth(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), done = {};
  A.step('The depth of a tree is 1 plus the deeper of its two subtrees. An empty tree has depth 0.', A.tree('tree', root));
  function depth(n) {
    if (!n) return 0;
    A.step(`Visit ${n.val}: first find the depths of its subtrees.`, A.tree('tree', root, { hl: { ...done, [n.id]: 'cur' } }));
    const l = depth(n.left), r = depth(n.right), d = 1 + Math.max(l, r);
    done[n.id] = 'ok';
    A.step(`${n.val}: left depth ${l}, right depth ${r}, so its depth is 1 + ${Math.max(l, r)} = ${d}.`, A.tree('tree', root, { hl: { ...done, [n.id]: 'sel' } }), A.vars({ node: n.val, depth: d }));
    return d;
  }
  const d = depth(root);
  A.step(`The maximum depth is ${d}.`, A.tree('tree', root, { hl: done }), A.text('Result', d, 'ok'));
}
A.scenario('Balanced', 'root = [3,9,20,null,null,15,7]', () => run([3, 9, 20, null, null, 15, 7]));
A.scenario('Skewed', 'root = [1,null,2,null,3]', () => run([1, null, 2, null, 3]));
''',
variants=[dict(
name="Level-order BFS",
idea="Count how many levels a breadth-first traversal visits.",
approach=r'''
**Queue by levels.** Push the root; for each level, pop exactly the nodes currently in the queue and push their children. Count the levels.

* Time: **O(n)** — each node is enqueued once.
* Space: **O(w)** — w is the widest level (up to about n/2).
''',
tc="n", sc="n",
java=r'''
public class MaximumDepth {

    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        int depth = 0;
        while (!queue.isEmpty()) {
            depth++;
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
        }
        return depth;
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr); let q = [root], depth = 0; const done = {};
  while (q.length) {
    depth++;
    q.forEach(n => (done[n.id] = 'cur'));
    A.step(`Level ${depth}: ${q.map(n => n.val).join(', ')}.`, A.tree('tree', root, { hl: done }), A.arr('queue', q.map(n => n.val)), A.vars({ depth }));
    q.forEach(n => (done[n.id] = 'ok'));
    q = q.flatMap(n => [n.left, n.right].filter(Boolean));
  }
  A.step(`${depth} levels, so the depth is ${depth}.`, A.tree('tree', root, { hl: done }), A.text('Result', depth, 'ok'));
}
A.scenario('Balanced', 'root = [3,9,20,null,null,15,7]', () => run([3, 9, 20, null, null, 15, 7]));
''')]),

P(num=100, slug="same-tree", title="Same Tree", diff="Easy", topic="Binary Tree General", cls="SameTree",
idea="Two trees are the same when their roots match and both pairs of subtrees are the same.",
vname="Recursive comparison", helpers=["TreeNode"],
spec=r'''
Given the roots `p` and `q` of two binary trees, return `true` if they are structurally identical with equal values in every node.

**Example 1**
```
Input:  p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2**
```
Input:  p = [1,2], q = [1,null,2]
Output: false
```

**Constraints**
* `0 <= n <= 100`; `-10^4 <= Node.val <= 10^4`
''',
approach=r'''
**Recursion.** Both null → same. One null, or values differ → different. Otherwise compare the left pair and the right pair.

* Time: **O(n)** — each node pair is compared once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class SameTree {

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null || q == null) return p == q;
        return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
''',
test=r'''
class SameTreeTest {

    private final SameTree solution = new SameTree();

    @Test
    void same() {
        assertTrue(solution.isSameTree(TreeNode.of(1, 2, 3), TreeNode.of(1, 2, 3)));
    }

    @Test
    void differentShape() {
        assertFalse(solution.isSameTree(TreeNode.of(1, 2), TreeNode.of(1, null, 2)));
    }

    @Test
    void differentValues() {
        assertFalse(solution.isSameTree(TreeNode.of(1, 2, 1), TreeNode.of(1, 1, 2)));
    }
}
''',
trace=r'''
function run(pa, qa) {
  const p = A.mkTree(pa), q = A.mkTree(qa), hp = {}, hq = {};
  const view = () => [A.tree('p', p, { hl: hp }), A.tree('q', q, { hl: hq })];
  A.step('Compare the trees node by node, walking both in the same order.', ...view());
  function same(a, b) {
    if (!a || !b) {
      const ok = a === b;
      if (!ok) { if (a) hp[a.id] = 'bad'; if (b) hq[b.id] = 'bad'; A.step(`One side has node ${(a || b).val}, the other is empty. Different.`, ...view()); }
      return ok;
    }
    hp[a.id] = hq[b.id] = 'cur';
    if (a.val !== b.val) { hp[a.id] = hq[b.id] = 'bad'; A.step(`${a.val} differs from ${b.val}. Different.`, ...view()); return false; }
    A.step(`Both nodes hold ${a.val}. Now compare their children.`, ...view());
    hp[a.id] = hq[b.id] = 'ok';
    return same(a.left, b.left) && same(a.right, b.right);
  }
  const r = same(p, q);
  A.step(r ? 'Every node matched. The trees are the same.' : 'A mismatch was found. The trees differ.', ...view(), A.text('Result', String(r), r ? 'ok' : 'bad'));
}
A.scenario('Same', 'p = [1,2,3], q = [1,2,3]', () => run([1, 2, 3], [1, 2, 3]));
A.scenario('Mirrored shape', 'p = [1,2], q = [1,null,2]', () => run([1, 2], [1, null, 2]));
'''),

P(num=226, slug="invert-binary-tree", title="Invert Binary Tree", diff="Easy", topic="Binary Tree General", cls="InvertBinaryTree",
idea="Swap every node's left and right children; the whole tree becomes its mirror image.",
vname="Recursive swap", helpers=["TreeNode"],
spec=r'''
Invert a binary tree (mirror it left-to-right) and return its root.

**Example 1**
```
Input:  [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

**Example 2**
```
Input:  [2,1,3]
Output: [2,3,1]
```

**Constraints**
* `0 <= n <= 100`; `-100 <= Node.val <= 100`
''',
approach=r'''
**Recursion.** Invert both subtrees, then swap them.

* Time: **O(n)** — each node is visited once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class InvertBinaryTree {

    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        TreeNode left = invertTree(root.left);
        root.left = invertTree(root.right);
        root.right = left;
        return root;
    }
}
''',
test=r'''
class InvertBinaryTreeTest {

    private final InvertBinaryTree solution = new InvertBinaryTree();

    @Test
    void full() {
        assertEquals(List.of(4, 7, 2, 9, 6, 3, 1), TreeNode.toList(solution.invertTree(TreeNode.of(4, 2, 7, 1, 3, 6, 9))));
    }

    @Test
    void small() {
        assertEquals(List.of(2, 3, 1), TreeNode.toList(solution.invertTree(TreeNode.of(2, 1, 3))));
    }

    @Test
    void empty() {
        assertNull(solution.invertTree(null));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), done = {};
  A.step('Mirror the tree by swapping the two children of every node.', A.tree('tree', root));
  (function inv(n) {
    if (!n) return;
    inv(n.left); inv(n.right);
    [n.left, n.right] = [n.right, n.left];
    done[n.id] = 'ok';
    A.step(`Both subtrees of ${n.val} are already mirrored. Swap its left and right children.`, A.tree('tree', root, { hl: { ...done, [n.id]: 'cur' } }));
  })(root);
  A.step('Every node has been swapped. The tree is its own mirror image.', A.tree('tree', root, { hl: done }));
}
A.scenario('Full tree', 'root = [4,2,7,1,3,6,9]', () => run([4, 2, 7, 1, 3, 6, 9]));
''',
variants=[dict(
name="Iterative BFS",
idea="Visit nodes level by level with a queue and swap each node's children.",
approach=r'''
**Queue.** Pop a node, swap its children, push the non-null children. No recursion.

* Time: **O(n)** — each node is processed once.
* Space: **O(w)** — the widest level sits in the queue.
''',
tc="n", sc="n",
java=r'''
public class InvertBinaryTree {

    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        while (!queue.isEmpty()) {
            TreeNode n = queue.poll();
            TreeNode t = n.left;
            n.left = n.right;
            n.right = t;
            if (n.left != null) queue.add(n.left);
            if (n.right != null) queue.add(n.right);
        }
        return root;
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), q = [root], done = {};
  while (q.length) {
    const n = q.shift();
    [n.left, n.right] = [n.right, n.left];
    done[n.id] = 'ok';
    [n.left, n.right].forEach(c => c && q.push(c));
    A.step(`Pop ${n.val}, swap its children, and queue them.`, A.tree('tree', root, { hl: { ...done, [n.id]: 'cur' } }), A.arr('queue', q.map(x => x.val)));
  }
  A.step('The queue is empty. The tree is mirrored.', A.tree('tree', root, { hl: done }));
}
A.scenario('Full tree', 'root = [4,2,7,1,3,6,9]', () => run([4, 2, 7, 1, 3, 6, 9]));
''')]),
]
