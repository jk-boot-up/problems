PROBLEMS = [
P(num=227, slug="basic-calculator-ii", title="Basic Calculator II", diff="Medium", topic="Stack", cls="BasicCalculatorII",
idea="Keep a running sum plus the last term; * and / only change the last term.",
vname="Running sum with the last term",
spec=r'''
Evaluate an expression string containing non-negative integers, `+ - * /` and spaces. Integer division truncates toward zero. The
expression is always valid and every intermediate value fits in 32 bits. Do not use `eval`.

**Example**
```
"3+2*2"      → 7
" 3/2 "      → 1
" 3+5 / 2 "  → 5
```

**Constraints**
* `1 <= s.length <= 3 * 10^5`
''',
approach=r'''
**No stack needed.** `*` and `/` bind tighter, so they only ever change the most recent term. Keep `result` (all finished terms) and
`last` (the term being built). When an operator ends a number: for `+`/`-`, fold `last` into `result` and start a new term `±num`; for
`*`/`/`, update `last` in place. A sentinel `+` at the end flushes the final number.

* Time: **O(n)** — one pass.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class BasicCalculatorII {

    public int calculate(String s) {
        long result = 0, last = 0, num = 0;
        char op = '+';
        for (int i = 0; i <= s.length(); i++) {
            char c = i < s.length() ? s.charAt(i) : '+';
            if (c == ' ') continue;
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
                continue;
            }
            switch (op) {
                case '+' -> { result += last; last = num; }
                case '-' -> { result += last; last = -num; }
                case '*' -> last = last * num;
                default -> last = last / num;
            }
            op = c;
            num = 0;
        }
        return (int) (result + last);
    }
}
''',
test=r'''
class BasicCalculatorIITest {

    private final BasicCalculatorII solution = new BasicCalculatorII();

    @ParameterizedTest
    @CsvSource(delimiter = '|', value = {"3+2*2|7", " 3/2 |1", " 3+5 / 2 |5", "14-3/2|13", "1-1+1|1", "0|0", "2*3*4-10/3|21", "1-5/2|-1", "42|42"})
    void evaluates(String s, int expected) {
        assertEquals(expected, solution.calculate(s));
    }
}
''',
trace=r'''
function run(s) {
  let result = 0, last = 0, num = 0, op = '+';
  A.step('Scan left to right. result holds finished terms; last is the term that * and / may still change.', A.chars('expression', s), A.vars({ result, last, op }));
  for (let i = 0; i <= s.length; i++) {
    const c = i < s.length ? s[i] : '+';
    if (c === ' ') continue;
    if (c >= '0' && c <= '9') { num = num * 10 + +c; continue; }
    let say;
    if (op === '+') { result += last; last = num; say = `'+${num}': fold the old term into result and start the term ${num}.`; }
    else if (op === '-') { result += last; last = -num; say = `'-${num}': fold the old term into result and start the term −${num}.`; }
    else if (op === '*') { last *= num; say = `'*${num}': multiply the current term → ${last}.`; }
    else { last = Math.trunc(last / num); say = `'/${num}': divide the current term (toward zero) → ${last}.`; }
    A.step(say, A.chars('expression', s, i < s.length ? { hl: { [i]: 'cur' } } : {}), A.vars({ result, last, 'next op': i < s.length ? c : 'end' }));
    op = c; num = 0;
  }
  A.step(`End of input: ${result} + ${last} = ${result + last}.`, A.text('Result', result + last, 'ok'));
}
A.scenario('Precedence', '"3+2*2"', () => run('3+2*2'));
A.scenario('Mixed', '"14-3/2"', () => run('14-3/2'));
''',
variants=[dict(
name="Stack of terms",
idea="Push each term (negated for −, combined with the top for * and /) and sum the stack at the end.",
approach=r'''
**Stack.** Read a number, then apply the operator before it: push `num` for `+`, `-num` for `-`, and replace the top with `top * num` or
`top / num` for `*` and `/`. The answer is the sum of the stack.

* Time: **O(n)** — one pass plus the final sum.
* Space: **O(n)** — up to one stacked term per number.
''',
java=r'''
public class BasicCalculatorII {

    public int calculate(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        int num = 0;
        char op = '+';
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) num = num * 10 + (c - '0');
            if ((!Character.isDigit(c) && c != ' ') || i == s.length() - 1) {
                switch (op) {
                    case '+' -> stack.push(num);
                    case '-' -> stack.push(-num);
                    case '*' -> stack.push(stack.pop() * num);
                    default -> stack.push(stack.pop() / num);
                }
                op = c;
                num = 0;
            }
        }
        int sum = 0;
        for (int v : stack) sum += v;
        return sum;
    }
}
''',
trace=r'''
function run(s) {
  const st = []; let num = 0, op = '+';
  A.step('Push each finished term. * and / combine with the term on top.', A.chars('expression', s), A.stack('terms', st));
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (c >= '0' && c <= '9') num = num * 10 + +c;
    if ((!(c >= '0' && c <= '9') && c !== ' ') || i === s.length - 1) {
      if (op === '+') st.push(num); else if (op === '-') st.push(-num); else if (op === '*') st.push(st.pop() * num); else st.push(Math.trunc(st.pop() / num));
      A.step(`Apply '${op}' to ${num}: the top term is now ${st[st.length - 1]}.`, A.chars('expression', s, { hl: { [i]: 'cur' } }), A.stack('terms', st));
      op = c; num = 0;
    }
  }
  const sum = st.reduce((a, b) => a + b, 0);
  A.step(`Sum of the terms: ${st.join(' + ')} = ${sum}.`, A.text('Result', sum, 'ok'));
}
A.scenario('Precedence', '"3+2*2"', () => run('3+2*2'));
''')]),

P(num=231, slug="power-of-two", title="Power of Two", diff="Easy", topic="Bit Manipulation", cls="PowerOfTwo",
idea="A power of two has exactly one 1-bit, and n & (n − 1) clears the lowest 1-bit.",
vname="Clear the lowest set bit",
spec=r'''
Return `true` if `n` is a power of two, that is `n == 2^x` for some integer `x >= 0`.

**Example**
```
1  → true   (2^0)
16 → true
3  → false
```

**Constraints**
* `-2^31 <= n <= 2^31 - 1`
''',
approach=r'''
**One bit.** Powers of two are positive and have a single 1-bit. Subtracting 1 turns that bit off and every bit below it on, so
`n & (n - 1)` is 0 exactly for powers of two (and for 0, which the `n > 0` check excludes).

* Time: **O(1)**.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class PowerOfTwo {

    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
}
''',
test=r'''
class PowerOfTwoTest {

    private final PowerOfTwo solution = new PowerOfTwo();

    @ParameterizedTest
    @CsvSource({"1,true", "2,true", "16,true", "1073741824,true", "3,false", "0,false", "-16,false", "-2147483648,false", "2147483647,false"})
    void check(int n, boolean expected) {
        assertEquals(expected, solution.isPowerOfTwo(n));
    }
}
''',
trace=r'''
function run(n) {
  const bits = v => (v >>> 0).toString(2).padStart(8, '0').slice(-8);
  A.step(`Is ${n} a power of two? Look at its bits.`, A.chars(`${n} in binary`, bits(n)));
  if (n <= 0) { A.step(`${n} is not positive, so it cannot be a power of two.`, A.text('Result', 'false', 'bad')); return; }
  A.step(`n − 1 = ${n - 1}: the lowest 1-bit becomes 0 and the bits below it become 1.`, A.chars(`${n}`, bits(n)), A.chars(`${n - 1}`, bits(n - 1)));
  const and = n & (n - 1);
  A.step(`n & (n − 1) = ${and}.`, A.chars('n & (n − 1)', bits(and), { hl: Object.fromEntries([...bits(and)].map((b, i) => [i, b === '1' ? 'bad' : 'ok'])) }));
  A.step(and === 0 ? 'Nothing left, so there was only one 1-bit: a power of two.' : 'Bits remain, so there was more than one 1-bit.', A.text('Result', String(and === 0), and === 0 ? 'ok' : 'bad'));
}
A.scenario('Power', 'n = 16', () => run(16));
A.scenario('Not a power', 'n = 12', () => run(12));
'''),

P(num=237, slug="delete-node-in-a-linked-list", title="Delete Node in a Linked List", diff="Medium", topic="Linked List", cls="DeleteNode",
idea="You cannot reach the previous node, so become the next node instead: copy its value and skip it.",
vname="Copy the next node", helpers=["ListNode"],
spec=r'''
You are given only a reference to a node in a singly linked list (not the head). The node is not the tail and all values are unique.
Delete that node's value from the list: afterwards the list should read the same as before, minus that value.

**Example**
```
head = [4,5,1,9], node = 5 → [4,1,9]
head = [4,5,1,9], node = 1 → [4,5,9]
```

**Constraints**
* `2 <= n <= 1000`; the given node is not the last one
''',
approach=r'''
**Steal the successor.** Copy `node.next.val` into `node`, then unlink `node.next`. The node that physically disappears is the successor,
but the sequence of values is exactly the list without the deleted value.

* Time: **O(1)**.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class DeleteNode {

    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
''',
test=r'''
class DeleteNodeTest {

    private final DeleteNode solution = new DeleteNode();

    @Test
    void examples() {
        ListNode head = ListNode.of(4, 5, 1, 9);
        solution.deleteNode(head.next);
        assertArrayEquals(new int[]{4, 1, 9}, ListNode.toArray(head));
        ListNode other = ListNode.of(4, 5, 1, 9);
        solution.deleteNode(other.next.next);
        assertArrayEquals(new int[]{4, 5, 9}, ListNode.toArray(other));
        ListNode pair = ListNode.of(1, 2);
        solution.deleteNode(pair);
        assertArrayEquals(new int[]{2}, ListNode.toArray(pair));
    }
}
''',
trace=r'''
function run(vals, idx) {
  const a = vals.slice();
  A.step(`Delete ${a[idx]}. We only hold that node; the node before it is out of reach.`, A.list('list', a, { hl: { [idx]: 'cur' }, ptr: { [idx]: 'node' } }));
  A.step(`Copy the next value, ${a[idx + 1]}, into this node.`, A.list('list', a.map((v, i) => (i === idx ? a[idx + 1] : v)), { hl: { [idx]: 'ok', [idx + 1]: 'dim' }, ptr: { [idx]: 'node' } }));
  a[idx] = a[idx + 1];
  A.step(`Now two nodes hold ${a[idx]}. Point this node past its successor.`, A.list('list', a, { hl: { [idx + 1]: 'bad' }, ptr: { [idx]: 'node' } }));
  a.splice(idx + 1, 1);
  A.step(`The duplicate is gone. The list reads [${a}].`, A.list('list', a, { hl: { [idx]: 'ok' } }));
}
A.scenario('Middle node', '[4,5,1,9], delete 5', () => run([4, 5, 1, 9], 1));
A.scenario('Before the tail', '[4,5,1,9], delete 1', () => run([4, 5, 1, 9], 2));
'''),

P(num=257, slug="binary-tree-paths", title="Binary Tree Paths", diff="Easy", topic="Binary Tree DFS", cls="BinaryTreePaths",
idea="Carry the path string down; at a leaf, the path is complete.",
vname="DFS carrying the path", helpers=["TreeNode"],
spec=r'''
Return all root-to-leaf paths of a binary tree, in any order, written as `"a->b->c"`.

**Example**
```
[1,2,3,null,5] → ["1->2->5","1->3"]
[1]            → ["1"]
```

**Constraints**
* `1 <= n <= 100`
''',
approach=r'''
**DFS.** Pass the path so far into each call. Append the current value; at a leaf, record the path; otherwise recurse into the children
with `"->"` appended. A `StringBuilder` that is trimmed back after each call avoids copying.

* Time: **O(n · h)** — each leaf's path has up to `h` values to write.
* Space: **O(h)** — the recursion and the builder.
''',
tc="n2", sc="n",
java=r'''
public class BinaryTreePaths {

    public List<String> binaryTreePaths(TreeNode root) {
        List<String> out = new ArrayList<>();
        dfs(root, new StringBuilder(), out);
        return out;
    }

    private void dfs(TreeNode node, StringBuilder path, List<String> out) {
        if (node == null) return;
        int mark = path.length();
        if (mark > 0) path.append("->");
        path.append(node.val);
        if (node.left == null && node.right == null) out.add(path.toString());
        else {
            dfs(node.left, path, out);
            dfs(node.right, path, out);
        }
        path.setLength(mark);
    }
}
''',
test=r'''
class BinaryTreePathsTest {

    private final BinaryTreePaths solution = new BinaryTreePaths();

    @Test
    void examples() {
        assertEquals(List.of("1->2->5", "1->3"), solution.binaryTreePaths(TreeNode.of(1, 2, 3, null, 5)));
        assertEquals(List.of("1"), solution.binaryTreePaths(TreeNode.of(1)));
        assertEquals(List.of("-1->-2"), solution.binaryTreePaths(TreeNode.of(-1, -2)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), out = [], hl = {};
  A.step('Walk down from the root, carrying the path so far.', A.tree('tree', root));
  (function dfs(n, path) {
    if (!n) return;
    const p = path ? `${path}->${n.val}` : `${n.val}`; hl[n.id] = 'cur';
    if (!n.left && !n.right) { out.push(p); hl[n.id] = 'ok'; A.step(`${n.val} is a leaf: record "${p}".`, A.tree('tree', root, { hl }), A.arr('paths', out, { hl: { [out.length - 1]: 'ok' } })); }
    else { A.step(`At ${n.val}, path "${p}". Go to the children.`, A.tree('tree', root, { hl }), A.text('Path', p)); dfs(n.left, p); dfs(n.right, p); hl[n.id] = 'dim'; }
  })(root, '');
  A.step(`${out.length} root-to-leaf path${out.length === 1 ? '' : 's'}.`, A.arr('paths', out));
}
A.scenario('Classic', '[1,2,3,null,5]', () => run([1, 2, 3, null, 5]));
'''),

P(num=258, slug="add-digits", title="Add Digits", diff="Easy", topic="Math", cls="AddDigits",
idea="A number and its digit sum leave the same remainder mod 9, so the answer is the digital root.",
vname="Digital root formula",
spec=r'''
Given a non-negative integer `num`, repeatedly add its digits until one digit remains, and return it.

**Example**
```
38 → 3 + 8 = 11 → 1 + 1 = 2
0  → 0
```

**Constraints**
* `0 <= num <= 2^31 - 1`
''',
approach=r'''
**Mod 9.** Since `10 ≡ 1 (mod 9)`, a number and its digit sum are congruent mod 9, and so is the final digit. That digit is between 1 and
9 for positive input, so it equals `1 + (num - 1) % 9`. Zero stays zero.

* Time: **O(1)**.
* Space: **O(1)**.
''',
tc="1", sc="1",
java=r'''
public class AddDigits {

    public int addDigits(int num) {
        return num == 0 ? 0 : 1 + (num - 1) % 9;
    }
}
''',
test=r'''
class AddDigitsTest {

    private final AddDigits solution = new AddDigits();

    @ParameterizedTest
    @CsvSource({"38,2", "0,0", "9,9", "10,1", "18,9", "19,1", "2147483647,1"})
    void roots(int num, int expected) {
        assertEquals(expected, solution.addDigits(num));
    }
}
''',
trace=r'''
function run(num) {
  A.step(`Find the final digit of ${num}. Adding digits never changes the remainder mod 9, because 10 leaves remainder 1.`, A.vars({ num, 'num mod 9': num % 9 }));
  let n = num;
  while (n >= 10) { const d = [...String(n)].map(Number), s = d.reduce((a, b) => a + b, 0); A.step(`Check: ${d.join(' + ')} = ${s} (still ${s % 9} mod 9).`, A.chars('digits', String(n)), A.vars({ sum: s, 'mod 9': s % 9 })); n = s; }
  const r = num === 0 ? 0 : 1 + (num - 1) % 9;
  A.step(`Formula: 1 + (${num} − 1) mod 9 = ${r}. The shift by one maps a remainder of 0 to 9 instead of 0.`, A.vars({ formula: r }));
  A.step(`The digital root of ${num} is ${r}.`, A.text('Result', r, 'ok'));
}
A.scenario('Two rounds', 'num = 38', () => run(38));
A.scenario('Multiple of 9', 'num = 99', () => run(99));
''',
variants=[dict(
name="Repeated digit sums",
idea="Literally add the digits until one is left.",
approach=r'''
**Simulation.** While `num >= 10`, replace it with the sum of its digits.

* Time: **O(log n)** — the first sum reads every digit; later sums are tiny.
* Space: **O(1)**.
''',
tc="log", sc="1",
java=r'''
public class AddDigits {

    public int addDigits(int num) {
        while (num >= 10) {
            int sum = 0;
            for (int n = num; n > 0; n /= 10) sum += n % 10;
            num = sum;
        }
        return num;
    }
}
''',
trace=r'''
function run(num) {
  A.step(`Start with ${num}.`, A.chars('digits', String(num)));
  let n = num;
  while (n >= 10) { const d = [...String(n)].map(Number), s = d.reduce((a, b) => a + b, 0); A.step(`${d.join(' + ')} = ${s}.`, A.chars('digits', String(n), { hl: Object.fromEntries(d.map((_, i) => [i, 'cur'])) }), A.vars({ sum: s })); n = s; }
  A.step(`${n} has one digit. Stop.`, A.chars('digits', String(n), { hl: { 0: 'ok' } }));
  A.step(`Answer: ${n}.`, A.text('Result', n, 'ok'));
}
A.scenario('Two rounds', 'num = 38', () => run(38));
''')]),

P(num=260, slug="single-number-iii", title="Single Number III", diff="Medium", topic="Bit Manipulation", cls="SingleNumberIII",
idea="XOR of everything is a ^ b; any set bit of it splits the numbers into two groups, one holding each answer.",
vname="XOR and split by a differing bit",
spec=r'''
In `nums`, exactly two elements appear once and every other element appears exactly twice. Return the two single elements, in any order,
using O(1) extra space.

**Example**
```
[1,2,1,3,2,5] → [3,5]
[-1,0]        → [-1,0]
```

**Constraints**
* `2 <= nums.length <= 3 * 10^4`
''',
approach=r'''
**Two-group XOR.** XOR-ing everything cancels the pairs and leaves `x = a ^ b`, which is non-zero. Its lowest set bit `x & -x` is a bit
where `a` and `b` differ. XOR the numbers that have that bit into one value and the rest into another: pairs still cancel inside each
group, leaving `a` and `b`.

* Time: **O(n)** — two passes.
* Space: **O(1)**.
''',
tc="n", sc="1",
java=r'''
public class SingleNumberIII {

    public int[] singleNumber(int[] nums) {
        int x = 0;
        for (int v : nums) x ^= v;
        int bit = x & -x;
        int a = 0, b = 0;
        for (int v : nums) {
            if ((v & bit) != 0) a ^= v;
            else b ^= v;
        }
        return new int[]{a, b};
    }
}
''',
test=r'''
class SingleNumberIIITest {

    private final SingleNumberIII solution = new SingleNumberIII();

    private int[] sorted(int[] a) {
        Arrays.sort(a);
        return a;
    }

    @Test
    void examples() {
        assertArrayEquals(new int[]{3, 5}, sorted(solution.singleNumber(new int[]{1, 2, 1, 3, 2, 5})));
        assertArrayEquals(new int[]{-1, 0}, sorted(solution.singleNumber(new int[]{-1, 0})));
        assertArrayEquals(new int[]{0, 1}, sorted(solution.singleNumber(new int[]{0, 1})));
        assertArrayEquals(new int[]{Integer.MIN_VALUE, 7}, sorted(solution.singleNumber(new int[]{7, 4, Integer.MIN_VALUE, 4})));
    }
}
''',
trace=r'''
function run(nums) {
  const bin = v => (v >>> 0).toString(2).padStart(4, '0').slice(-4);
  let x = 0; nums.forEach(v => (x ^= v));
  A.step('XOR every number. Pairs cancel, so what remains is a ^ b.', A.arr('nums', nums), A.vars({ 'a ^ b': x, bits: bin(x) }));
  const bit = x & -x;
  A.step(`The lowest set bit of ${x} is ${bit} (${bin(bit)}). a and b differ there, so it splits them apart.`, A.vars({ 'a ^ b': bin(x), bit: bin(bit) }));
  let a = 0, b = 0; const hl = {};
  nums.forEach((v, i) => { if (v & bit) { a ^= v; hl[i] = 'cur'; } else { b ^= v; hl[i] = 'alt'; } });
  A.step(`Group with the bit (orange): XOR = ${a}. Group without it (blue): XOR = ${b}. Pairs always land in the same group and cancel.`, A.arr('nums', nums, { hl }), A.vars({ groupWithBit: a, groupWithout: b }));
  A.step(`The two single numbers are ${a} and ${b}.`, A.text('Result', `[${a}, ${b}]`, 'ok'));
}
A.scenario('Classic', '[1,2,1,3,2,5]', () => run([1, 2, 1, 3, 2, 5]));
'''),

P(num=263, slug="ugly-number", title="Ugly Number", diff="Easy", topic="Math", cls="UglyNumber",
idea="Divide out every 2, 3 and 5; an ugly number is left with 1.",
vname="Divide out 2, 3 and 5",
spec=r'''
An **ugly number** is a positive integer whose only prime factors are 2, 3 and 5. Return `true` if `n` is ugly. (1 counts as ugly.)

**Example**
```
6  → true   (2 × 3)
1  → true
14 → false  (has the factor 7)
```

**Constraints**
* `-2^31 <= n <= 2^31 - 1`
''',
approach=r'''
**Strip the allowed factors.** Non-positive numbers are not ugly. Otherwise divide by 2 while possible, then 3, then 5. Only 1 remains if
no other prime was present.

* Time: **O(log n)** — each division at least halves… or thirds… the number.
* Space: **O(1)**.
''',
tc="log", sc="1",
java=r'''
public class UglyNumber {

    public boolean isUgly(int n) {
        if (n <= 0) return false;
        for (int p : new int[]{2, 3, 5}) while (n % p == 0) n /= p;
        return n == 1;
    }
}
''',
test=r'''
class UglyNumberTest {

    private final UglyNumber solution = new UglyNumber();

    @ParameterizedTest
    @CsvSource({"6,true", "1,true", "8,true", "30,true", "14,false", "0,false", "-6,false", "7,false", "2147483647,false"})
    void check(int n, boolean expected) {
        assertEquals(expected, solution.isUgly(n));
    }
}
''',
trace=r'''
function run(n) {
  A.step(`Is ${n} ugly? Divide out every factor 2, 3 and 5 and see what is left.`, A.vars({ n }));
  let m = n;
  for (const p of [2, 3, 5]) { const before = m; let k = 0; while (m % p === 0) { m /= p; k++; } A.step(k ? `${before} has ${k} factor${k > 1 ? 's' : ''} of ${p}: ${before} → ${m}.` : `${before} is not divisible by ${p}.`, A.vars({ prime: p, left: m })); }
  A.step(m === 1 ? 'Only 1 is left: no other prime factor. Ugly.' : `${m} is left, so another prime divides ${n}. Not ugly.`, A.text('Result', String(m === 1), m === 1 ? 'ok' : 'bad'));
}
A.scenario('Ugly', 'n = 60', () => run(60));
A.scenario('Not ugly', 'n = 14', () => run(14));
'''),

P(num=264, slug="ugly-number-ii", title="Ugly Number II", diff="Medium", topic="Dynamic Programming", cls="UglyNumberII",
idea="Every ugly number is a smaller ugly number times 2, 3 or 5; merge those three sequences with three pointers.",
vname="Three pointers",
spec=r'''
Return the `n`-th ugly number (prime factors only 2, 3 and 5; the sequence starts `1, 2, 3, 4, 5, 6, 8, 9, 10, 12, …`).

**Example**
```
n = 10 → 12
n = 1  → 1
```

**Constraints**
* `1 <= n <= 1690`
''',
approach=r'''
**Merge three streams.** The sequence times 2, times 3 and times 5 are each sorted. Keep a pointer into the sequence for each factor. The
next ugly number is the smallest of the three candidates; advance **every** pointer that produced it, so duplicates such as `6 = 2·3 =
3·2` appear once.

* Time: **O(n)** — one step per number.
* Space: **O(n)** — the sequence.
''',
tc="n", sc="n",
java=r'''
public class UglyNumberII {

    public int nthUglyNumber(int n) {
        int[] ugly = new int[n];
        ugly[0] = 1;
        int i2 = 0, i3 = 0, i5 = 0;
        for (int k = 1; k < n; k++) {
            int a = ugly[i2] * 2, b = ugly[i3] * 3, c = ugly[i5] * 5;
            int next = Math.min(a, Math.min(b, c));
            ugly[k] = next;
            if (next == a) i2++;
            if (next == b) i3++;
            if (next == c) i5++;
        }
        return ugly[n - 1];
    }
}
''',
test=r'''
class UglyNumberIITest {

    private final UglyNumberII solution = new UglyNumberII();

    @ParameterizedTest
    @CsvSource({"1,1", "2,2", "7,8", "10,12", "11,15", "1690,2123366400"})
    void nth(int n, int expected) {
        assertEquals(expected, solution.nthUglyNumber(n));
    }
}
''',
trace=r'''
function run(n) {
  const u = [1]; let i2 = 0, i3 = 0, i5 = 0;
  A.step('Start with 1. Each pointer marks the smallest number not yet multiplied by its factor.', A.arr('ugly', u, { ptr: { 0: '2,3,5' } }));
  for (let k = 1; k < n; k++) {
    const a = u[i2] * 2, b = u[i3] * 3, c = u[i5] * 5, next = Math.min(a, b, c);
    u.push(next);
    const moved = []; if (next === a) { i2++; moved.push('×2'); } if (next === b) { i3++; moved.push('×3'); } if (next === c) { i5++; moved.push('×5'); }
    const ptr = {}; [[i2, '×2'], [i3, '×3'], [i5, '×5']].forEach(([i, l]) => (ptr[i] = ptr[i] ? ptr[i] + ' ' + l : l));
    A.step(`Candidates ${a}, ${b}, ${c}. Take ${next}; advance ${moved.join(' and ')}.`, A.arr('ugly', u, { hl: { [k]: 'ok' }, ptr }), A.vars({ '×2': a, '×3': b, '×5': c }));
  }
  A.step(`The ${n}th ugly number is ${u[n - 1]}.`, A.text('Result', u[n - 1], 'ok'));
}
A.scenario('Tenth', 'n = 10', () => run(10));
''',
variants=[dict(
name="Min-heap with a seen set",
idea="Pop the smallest ugly number and push its ×2, ×3, ×5 multiples, skipping ones already queued.",
approach=r'''
**Heap.** Start the heap with 1. Pop `n` times; after each pop push `x·2`, `x·3`, `x·5` unless they are already in a `MyHashSet`. The
`n`-th pop is the answer. Use `long`, since multiples can pass `2^31`.

* Time: **O(n log n)** — `3n` pushes into a heap of size `O(n)`.
* Space: **O(n)** — the heap and the set.
''',
tc="nlogn", sc="n",
java=r'''
public class UglyNumberII {

    public int nthUglyNumber(int n) {
        PriorityQueue<Long> heap = new PriorityQueue<>();
        MyHashSet<Long> queued = new MyHashSet<>();
        heap.add(1L);
        queued.add(1L);
        long x = 1;
        for (int k = 0; k < n; k++) {
            x = heap.poll();
            for (long f : new long[]{2, 3, 5}) if (queued.add(x * f)) heap.add(x * f);
        }
        return (int) x;
    }
}
''',
trace=r'''
function run(n) {
  const heap = [1], seen = new Set([1]), out = [];
  A.step('The heap starts with 1.', A.arr('heap (sorted view)', heap));
  for (let k = 0; k < n; k++) {
    const x = heap.shift(); out.push(x);
    const added = [2, 3, 5].map(f => x * f).filter(v => !seen.has(v));
    added.forEach(v => { seen.add(v); heap.push(v); }); heap.sort((a, b) => a - b);
    A.step(`Pop ${x} (ugly #${k + 1}). Push ${added.length ? added.join(', ') : 'nothing new'}.`, A.arr('ugly so far', out, { hl: { [k]: 'ok' } }), A.arr('heap (sorted view)', heap));
  }
  A.step(`The ${n}th pop is ${out[n - 1]}.`, A.text('Result', out[n - 1], 'ok'));
}
A.scenario('Tenth', 'n = 10', () => run(10));
''')]),

P(num=273, slug="integer-to-english-words", title="Integer to English Words", diff="Hard", topic="String", cls="IntegerToEnglish",
idea="Split into groups of three digits; each group is spelled the same way, followed by Billion, Million or Thousand.",
vname="Three-digit groups",
spec=r'''
Convert a non-negative integer to its English words representation.

**Example**
```
123        → "One Hundred Twenty Three"
12345      → "Twelve Thousand Three Hundred Forty Five"
1234567    → "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

**Constraints**
* `0 <= num <= 2^31 - 1`
''',
approach=r'''
**Groups of three.** From the billions down, take each three-digit chunk. Spell a chunk as `"<d> Hundred"` (if any) plus either a word for
1–19 or a tens word and an optional unit word, then add the group's scale word. Skip empty chunks so `1000010` reads "One Million Ten".
`0` is the only input that says "Zero".

* Time: **O(1)** — at most four groups.
* Space: **O(1)** — the output is bounded.
''',
tc="1", sc="1",
java=r'''
public class IntegerToEnglish {

    private static final String[] BELOW_20 = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    private static final String[] TENS = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    private static final String[] SCALES = {"", "Thousand", "Million", "Billion"};
    private static final int[] DIVISORS = {1, 1_000, 1_000_000, 1_000_000_000};

    public String numberToWords(int num) {
        if (num == 0) return "Zero";
        List<String> words = new ArrayList<>();
        for (int g = 3; g >= 0; g--) {
            int chunk = num / DIVISORS[g] % 1000;
            if (chunk == 0) continue;
            spell(chunk, words);
            if (g > 0) words.add(SCALES[g]);
        }
        return String.join(" ", words);
    }

    private void spell(int n, List<String> words) {
        if (n >= 100) {
            words.add(BELOW_20[n / 100]);
            words.add("Hundred");
            n %= 100;
        }
        if (n >= 20) {
            words.add(TENS[n / 10]);
            n %= 10;
        }
        if (n > 0) words.add(BELOW_20[n]);
    }
}
''',
test=r'''
class IntegerToEnglishTest {

    private final IntegerToEnglish solution = new IntegerToEnglish();

    @ParameterizedTest
    @CsvSource(delimiter = '|', value = {
            "0|Zero", "5|Five", "13|Thirteen", "20|Twenty", "100|One Hundred", "123|One Hundred Twenty Three",
            "12345|Twelve Thousand Three Hundred Forty Five",
            "1234567|One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
            "1000000|One Million", "1000010|One Million Ten",
            "2147483647|Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"})
    void words(int num, String expected) {
        assertEquals(expected, solution.numberToWords(num));
    }
}
''',
trace=r'''
const B20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'];
const TENS = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'], SC = ['', 'Thousand', 'Million', 'Billion'];
function spell(n) { const w = []; if (n >= 100) { w.push(B20[Math.floor(n / 100)], 'Hundred'); n %= 100; } if (n >= 20) { w.push(TENS[Math.floor(n / 10)]); n %= 10; } if (n) w.push(B20[n]); return w; }
function run(num) {
  const groups = []; for (let g = 3; g >= 0; g--) groups.push(Math.floor(num / 1000 ** g) % 1000);
  A.step(`Split ${num.toLocaleString('en-US')} into groups of three digits: billions, millions, thousands, ones.`, A.arr('groups', groups.map(String), { noIdx: true }));
  const words = [];
  groups.forEach((c, k) => {
    const g = 3 - k;
    if (!c) { A.step(`The ${SC[g] || 'ones'} group is 0: skip it.`, A.arr('groups', groups.map(String), { noIdx: true, hl: { [k]: 'dim' } })); return; }
    const w = spell(c); words.push(...w); if (g) words.push(SC[g]);
    A.step(`${c} → "${w.join(' ')}"${g ? ` + "${SC[g]}"` : ''}.`, A.arr('groups', groups.map(String), { noIdx: true, hl: { [k]: 'cur' } }), A.text('Words so far', words.join(' ')));
  });
  A.step('Join the words with spaces.', A.text('Result', words.join(' '), 'ok'));
}
A.scenario('Millions', '1234567', () => run(1234567));
A.scenario('Empty group', '1000010', () => run(1000010));
'''),

P(num=278, slug="first-bad-version", title="First Bad Version", diff="Easy", topic="Binary Search", cls="FirstBadVersion",
idea="Bad versions form a suffix; binary search for where the suffix starts.",
vname="Binary search for the boundary",
spec=r'''
Versions `1..n` were released in order. Once a version is bad, every later version is bad too. Given an API `isBadVersion(v)`, find the
first bad version while calling the API as few times as possible.

In this project the API is passed to the constructor as an `IntPredicate`.

**Example**
```
n = 5, first bad = 4 → 4   (isBad(3) = false, isBad(5) = true, isBad(4) = true)
n = 1, first bad = 1 → 1
```

**Constraints**
* `1 <= bad <= n <= 2^31 - 1`
''',
approach=r'''
**Lower bound.** Keep `lo..hi` containing the answer. Test the middle: if it is bad, the answer is at `mid` or to its left (`hi = mid`);
otherwise it is to the right (`lo = mid + 1`). Compute `mid = lo + (hi - lo) / 2` so `lo + hi` cannot overflow.

* Time: **O(log n)** — about 31 API calls at most.
* Space: **O(1)**.
''',
tc="log", sc="1",
java=r'''
public class FirstBadVersion {

    private final java.util.function.IntPredicate isBadVersion;

    public FirstBadVersion(java.util.function.IntPredicate isBadVersion) {
        this.isBadVersion = isBadVersion;
    }

    public int firstBadVersion(int n) {
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (isBadVersion.test(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
''',
test=r'''
class FirstBadVersionTest {

    private int calls;

    private int solve(int n, int bad) {
        calls = 0;
        return new FirstBadVersion(v -> {
            calls++;
            return v >= bad;
        }).firstBadVersion(n);
    }

    @Test
    void examples() {
        assertEquals(4, solve(5, 4));
        assertEquals(1, solve(1, 1));
        assertEquals(1, solve(10, 1));
        assertEquals(10, solve(10, 10));
    }

    @Test
    void hugeRangeUsesFewCalls() {
        assertEquals(1702766719, solve(2126753390, 1702766719));
        assertTrue(calls <= 32);
        assertEquals(Integer.MAX_VALUE, solve(Integer.MAX_VALUE, Integer.MAX_VALUE));
    }
}
''',
trace=r'''
function run(n, bad) {
  const vs = Array.from({ length: n }, (_, i) => i + 1);
  let lo = 1, hi = n, calls = 0;
  A.step(`Versions 1..${n}. Some suffix is bad; find where it starts with as few checks as possible.`, A.arr('versions', vs, { noIdx: true }));
  const hl = {};
  while (lo < hi) {
    const mid = lo + Math.floor((hi - lo) / 2), b = mid >= bad; calls++;
    hl[mid - 1] = b ? 'bad' : 'ok';
    A.step(`Check version ${mid}: ${b ? 'bad, so the first bad one is here or earlier' : 'good, so the first bad one is later'}.`, A.arr('versions', vs, { noIdx: true, hl, range: [lo - 1, hi - 1], ptr: { [mid - 1]: 'mid' } }), A.vars({ lo, hi, calls }));
    if (b) hi = mid; else lo = mid + 1;
  }
  A.step(`lo = hi = ${lo}: version ${lo} is the first bad one, found with ${calls} check${calls === 1 ? '' : 's'}.`, A.arr('versions', vs, { noIdx: true, hl: { ...hl, [lo - 1]: 'bad' }, ptr: { [lo - 1]: 'first bad' } }), A.text('Result', lo, 'ok'));
}
A.scenario('Near the end', 'n = 5, bad = 4', () => run(5, 4));
A.scenario('Longer run', 'n = 16, bad = 11', () => run(16, 11));
'''),
]
