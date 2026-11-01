PROBLEMS = [
P(num=452, slug="minimum-number-of-arrows-to-burst-balloons", title="Minimum Number of Arrows to Burst Balloons", diff="Medium", topic="Intervals", cls="MinimumArrows",
idea="Sort balloons by right edge; shoot at the first right edge and skip every balloon that arrow already pierces.",
vname="Greedy by end point",
spec=r'''
Balloons are horizontal intervals `points[i] = [xstart, xend]` on a wall. A vertical arrow shot at `x` bursts every balloon with
`xstart <= x <= xend`. Return the **minimum** number of arrows needed to burst all balloons.

**Example 1**
```
Input:  points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2   (shoot at x = 6 and x = 11)
```

**Example 2**
```
Input:  points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
```

**Example 3**
```
Input:  points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
```

**Constraints**
* `1 <= points.length <= 10^5`; `-2^31 <= xstart < xend <= 2^31 - 1`
''',
approach=r'''
**Greedy.** Sort by end. Shoot the first arrow at the smallest end: it is as far right as possible while still hitting that balloon.
Every balloon starting at or before the arrow is burst. The first balloon starting after it needs a new arrow at its end.
Compare with `Integer.compare` to avoid overflow.

* Time: **O(n log n)** — sorting; the sweep is linear.
* Space: **O(log n)** — the sort's recursion stack.
''',
tc="nlogn", sc="log",
java=r'''
public class MinimumArrows {

    public int findMinArrowShots(int[][] points) {
        int[][] p = points.clone();
        Arrays.sort(p, (a, b) -> Integer.compare(a[1], b[1]));
        int arrows = 1;
        int x = p[0][1];
        for (int i = 1; i < p.length; i++) {
            if (p[i][0] > x) {
                arrows++;
                x = p[i][1];
            }
        }
        return arrows;
    }
}
''',
test=r'''
class MinimumArrowsTest {

    private final MinimumArrows solution = new MinimumArrows();

    @Test
    void overlapping() {
        assertEquals(2, solution.findMinArrowShots(new int[][]{{10, 16}, {2, 8}, {1, 6}, {7, 12}}));
    }

    @Test
    void disjoint() {
        assertEquals(4, solution.findMinArrowShots(new int[][]{{1, 2}, {3, 4}, {5, 6}, {7, 8}}));
    }

    @Test
    void touching() {
        assertEquals(2, solution.findMinArrowShots(new int[][]{{1, 2}, {2, 3}, {3, 4}, {4, 5}}));
    }

    @Test
    void extremeValues() {
        assertEquals(2, solution.findMinArrowShots(new int[][]{{-2147483646, -2147483645}, {2147483646, 2147483647}}));
    }
}
''',
trace=r'''
function run(pts) {
  const s = pts.map(x => x.slice()).sort((a, b) => a[1] - b[1]);
  const lo = Math.min(...s.map(p => p[0])), hi = Math.max(...s.map(p => p[1]));
  const grid = (x, hl) => s.map((p, r) => { const row = []; for (let c = lo; c <= hi; c++) row.push(''); return row; });
  const ghl = (shots, cur) => { const o = []; s.forEach((p, r) => { const hit = shots.some(x => x >= p[0] && x <= p[1]); for (let c = p[0]; c <= p[1]; c++) o.push([`${r},${c - lo}`, shots.includes(c) && c <= p[1] && c >= p[0] ? 'alt' : r === cur ? 'cur' : hit ? 'ok' : 'sel']); }); return o; };
  const lab = s.map(p => `[${p}]`);
  let x = s[0][1], arrows = 1; const shots = [x];
  A.step('Sort the balloons by their right edge. Each row is a balloon; the columns are x positions.', A.grid('balloons (x from ' + lo + ')', grid(), { hl: ghl([], -1) }), A.arr('sorted by end', lab));
  A.step(`Shoot the first arrow at x = ${x}, the smallest right edge. Green balloons are burst.`, A.grid('balloons (x from ' + lo + ')', grid(), { hl: ghl(shots, 0) }), A.vars({ arrows, lastArrow: x }));
  for (let i = 1; i < s.length; i++) {
    if (s[i][0] > x) { x = s[i][1]; arrows++; shots.push(x); A.step(`[${s[i]}] starts after ${shots[shots.length - 2]}, so it needs a new arrow at x = ${x}.`, A.grid('balloons (x from ' + lo + ')', grid(), { hl: ghl(shots, i) }), A.vars({ arrows, lastArrow: x })); }
    else A.step(`[${s[i]}] starts at or before ${x}, so the arrow at ${x} already bursts it.`, A.grid('balloons (x from ' + lo + ')', grid(), { hl: ghl(shots, i) }), A.vars({ arrows, lastArrow: x }));
  }
  A.step(`${arrows} arrow${arrows > 1 ? 's' : ''} at x = ${shots.join(', ')} burst every balloon.`, A.text('Result', arrows, 'ok'));
}
A.scenario('Overlapping balloons', '[[10,16],[2,8],[1,6],[7,12]]', () => run([[10, 16], [2, 8], [1, 6], [7, 12]]));
A.scenario('Touching edges', '[[1,2],[2,3],[3,4],[4,5]]', () => run([[1, 2], [2, 3], [3, 4], [4, 5]]));
'''),

P(num=20, slug="valid-parentheses", title="Valid Parentheses", diff="Easy", topic="Stack", cls="ValidParentheses",
idea="Push every opener; each closer must match the opener on top of the stack.",
vname="Stack of openers",
spec=r'''
Given a string `s` of the characters `()[]{}`, decide whether it is **valid**: every opening bracket is closed by the same type of
bracket, in the correct order, and every closing bracket has a matching opener.

**Example 1**
```
Input:  s = "()[]{}"
Output: true
```

**Example 2**
```
Input:  s = "(]"
Output: false
```

**Example 3**
```
Input:  s = "([])"
Output: true
```

**Constraints**
* `1 <= s.length <= 10^4`; only `()[]{}`.
''',
approach=r'''
**Stack.** Push the expected closer for every opener. For a closer, the stack must be non-empty and its top must equal that closer.
At the end the stack must be empty.

* Time: **O(n)** — each character is pushed or popped once.
* Space: **O(n)** — the stack in the worst case (all openers).
''',
java=r'''
public class ValidParentheses {

    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            switch (c) {
                case '(' -> stack.push(')');
                case '[' -> stack.push(']');
                case '{' -> stack.push('}');
                default -> {
                    if (stack.isEmpty() || stack.pop() != c) return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
''',
test=r'''
class ValidParenthesesTest {

    private final ValidParentheses solution = new ValidParentheses();

    @ParameterizedTest
    @CsvSource({"'()[]{}',true", "'(]',false", "'([])',true", "'([)]',false", "'(((',false", "')',false", "'{[]}',true"})
    void checks(String s, boolean expected) {
        assertEquals(expected, solution.isValid(s));
    }
}
''',
trace=r'''
const CLOSE = { '(': ')', '[': ']', '{': '}' };
function run(s) {
  const st = [];
  A.step('Scan left to right. For each opener, push the closer we expect to see later.', A.chars('s', s), A.stack('expected closers', st));
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (CLOSE[c]) { st.push(CLOSE[c]); A.step(`'${c}' opens a bracket. Push its closer '${CLOSE[c]}'.`, A.chars('s', s, { hl: { [i]: 'cur' } }), A.stack('expected closers', st)); continue; }
    if (!st.length || st[st.length - 1] !== c) { A.step(!st.length ? `'${c}' closes a bracket that was never opened. Invalid.` : `'${c}' arrives, but the top of the stack expects '${st[st.length - 1]}'. Invalid.`, A.chars('s', s, { hl: { [i]: 'bad' } }), A.stack('expected closers', st), A.text('Result', 'false', 'bad')); return; }
    st.pop();
    A.step(`'${c}' matches the top of the stack. Pop it.`, A.chars('s', s, { hl: { [i]: 'ok' } }), A.stack('expected closers', st));
  }
  A.step(st.length ? `The string ended with ${st.length} unclosed bracket${st.length > 1 ? 's' : ''}. Invalid.` : 'The stack is empty, so every bracket was matched. Valid.', A.stack('expected closers', st), A.text('Result', String(!st.length), st.length ? 'bad' : 'ok'));
}
A.scenario('Nested', 's = "{[()]}"', () => run('{[()]}'));
A.scenario('Wrong order', 's = "([)]"', () => run('([)]'));
A.scenario('Edge: unclosed', 's = "(("', () => run('(('));
'''),

P(num=71, slug="simplify-path", title="Simplify Path", diff="Medium", topic="Stack", cls="SimplifyPath",
idea="Split on '/', push real directory names, pop on '..', ignore '.' and empty parts.",
vname="Stack of directories",
spec=r'''
Convert an absolute Unix-style `path` to its **canonical** form:
* `.` means the current directory and `..` the parent directory (staying at `/` if already there);
* multiple slashes count as one; other names, including `...`, are directory names;
* the result starts with one `/`, separates directories with single slashes and has no trailing slash.

**Example 1**
```
Input:  path = "/home//foo/"
Output: "/home/foo"
```

**Example 2**
```
Input:  path = "/a/./b/../../c/"
Output: "/c"
```

**Example 3**
```
Input:  path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
```

**Constraints**
* `1 <= path.length <= 3000`; letters, digits, `.`, `/`, `_`; starts with `/`.
''',
approach=r'''
**Stack.** Split on `/`. Skip empty parts and `.`; for `..` pop if possible; otherwise push the name. Join the stack from bottom
to top with `/`.

* Time: **O(n)** — splitting and joining are linear.
* Space: **O(n)** — the parts and the stack.
''',
java=r'''
public class SimplifyPath {

    public String simplifyPath(String path) {
        Deque<String> stack = new ArrayDeque<>();
        for (String part : path.split("/")) {
            if (part.isEmpty() || part.equals(".")) continue;
            if (part.equals("..")) {
                stack.pollLast();
            } else {
                stack.addLast(part);
            }
        }
        return "/" + String.join("/", stack);
    }
}
''',
test=r'''
class SimplifyPathTest {

    private final SimplifyPath solution = new SimplifyPath();

    @ParameterizedTest
    @CsvSource({"/home/,/home", "/home//foo/,/home/foo", "/home/user/Documents/../Pictures,/home/user/Pictures", "/../,/", "/.../a/../b/c/../d/./,/.../b/d", "/a/./b/../../c/,/c"})
    void simplifies(String path, String expected) {
        assertEquals(expected, solution.simplifyPath(path));
    }
}
''',
trace=r'''
function run(path) {
  const parts = path.split('/'), st = [];
  A.step('Split the path on slashes and process each part.', A.text('path', path), A.arr('parts', parts.map(p => p || '∅')));
  parts.forEach((p, i) => {
    const show = A.arr('parts', parts.map(x => x || '∅'), { hl: { [i]: p === '..' ? 'bad' : p && p !== '.' ? 'ok' : 'dim' } });
    if (!p || p === '.') A.step(p ? '"." means the current directory. Ignore it.' : 'An empty part comes from repeated or edge slashes. Ignore it.', show, A.stack('directories', st));
    else if (p === '..') { const g = st.pop(); A.step(g ? `".." goes up one level: pop "${g}".` : '".." at the root stays at the root.', show, A.stack('directories', st)); }
    else { st.push(p); A.step(`"${p}" is a directory name. Push it.`, show, A.stack('directories', st)); }
  });
  A.step(`Join the stack with slashes: "/${st.join('/')}".`, A.stack('directories', st), A.text('Result', '/' + st.join('/'), 'ok'));
}
A.scenario('Up and down', 'path = "/a/./b/../../c/"', () => run('/a/./b/../../c/'));
A.scenario('Three dots is a name', 'path = "/.../a/../b//c/"', () => run('/.../a/../b//c/'));
'''),

P(num=155, slug="min-stack", title="Min Stack", diff="Medium", topic="Stack", cls="MinStack",
idea="Store, with every pushed value, the minimum of the stack at that moment.",
vname="Value-and-minimum pairs",
spec=r'''
Design a stack that supports `push(val)`, `pop()`, `top()` and `getMin()` (the smallest element in the stack), each in **O(1)** time.
`pop`, `top` and `getMin` are only called on a non-empty stack.

**Example**
```
push(-2), push(0), push(-3)
getMin() → -3
pop()
top()    → 0
getMin() → -2
```

**Constraints**
* `-2^31 <= val <= 2^31 - 1`; at most `3 * 10^4` calls.
''',
approach=r'''
**Pairs.** Each stack entry is `(value, minSoFar)` where `minSoFar = min(value, previous top's minSoFar)`. Popping restores the previous
minimum automatically, because it is stored in the entry below.

* Time: **O(1)** — every operation touches only the top.
* Space: **O(n)** — two numbers per element.
''',
java=r'''
public class MinStack {

    private record Entry(int value, int min) { }

    private final Deque<Entry> stack = new ArrayDeque<>();

    public void push(int val) {
        int min = stack.isEmpty() ? val : Math.min(val, stack.peek().min());
        stack.push(new Entry(val, min));
    }

    public void pop() {
        stack.pop();
    }

    public int top() {
        return stack.peek().value();
    }

    public int getMin() {
        return stack.peek().min();
    }
}
''',
test=r'''
class MinStackTest {

    @Test
    void example() {
        MinStack s = new MinStack();
        s.push(-2);
        s.push(0);
        s.push(-3);
        assertEquals(-3, s.getMin());
        s.pop();
        assertEquals(0, s.top());
        assertEquals(-2, s.getMin());
    }

    @Test
    void duplicatesOfMinimum() {
        MinStack s = new MinStack();
        s.push(1);
        s.push(1);
        s.pop();
        assertEquals(1, s.getMin());
    }
}
''',
trace=r'''
A.scenario('Example sequence', 'push -2, 0, -3 · getMin · pop · top · getMin', () => {
  const st = [];
  const view = () => A.stack('stack (value | min so far)', st.map(e => `${e[0]} | ${e[1]}`));
  A.step('Each entry stores its value and the minimum of the stack up to that point.', view());
  for (const v of [-2, 0, -3]) { const m = st.length ? Math.min(v, st[st.length - 1][1]) : v; st.push([v, m]); A.step(`push(${v}): the minimum so far is min(${v}, previous minimum) = ${m}.`, view()); }
  A.step(`getMin(): read the top entry's minimum: ${st[st.length - 1][1]}. No searching needed.`, view(), A.text('getMin', st[st.length - 1][1], 'ok'));
  const p = st.pop(); A.step(`pop(): remove ${p[0]}. The entry below still remembers its own minimum.`, view());
  A.step(`top() = ${st[st.length - 1][0]}, getMin() = ${st[st.length - 1][1]}.`, view(), A.text('top / getMin', `${st[st.length - 1][0]} / ${st[st.length - 1][1]}`, 'ok'));
});
'''),

P(num=150, slug="evaluate-reverse-polish-notation", title="Evaluate Reverse Polish Notation", diff="Medium", topic="Stack", cls="EvaluateRPN",
idea="Numbers go on a stack; an operator pops two operands, applies itself and pushes the result.",
vname="Operand stack",
spec=r'''
Evaluate an arithmetic expression in **Reverse Polish Notation** given as `tokens`. Operators are `+ - * /`; each operand is an
integer or a sub-expression. Division truncates toward zero. The expression is always valid and fits in 32-bit integers.

**Example 1**
```
Input:  tokens = ["2","1","+","3","*"]
Output: 9   ((2 + 1) * 3)
```

**Example 2**
```
Input:  tokens = ["4","13","5","/","+"]
Output: 6   (4 + 13 / 5)
```

**Constraints**
* `1 <= tokens.length <= 10^4`
''',
approach=r'''
**Stack.** Push numbers. For an operator, pop `b` then `a` (note the order), push `a op b`. The final stack holds the answer.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the operand stack.
''',
java=r'''
public class EvaluateRPN {

    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (String t : tokens) {
            switch (t) {
                case "+" -> stack.push(stack.pop() + stack.pop());
                case "*" -> stack.push(stack.pop() * stack.pop());
                case "-" -> { int b = stack.pop(), a = stack.pop(); stack.push(a - b); }
                case "/" -> { int b = stack.pop(), a = stack.pop(); stack.push(a / b); }
                default -> stack.push(Integer.parseInt(t));
            }
        }
        return stack.pop();
    }
}
''',
test=r'''
class EvaluateRPNTest {

    private final EvaluateRPN solution = new EvaluateRPN();

    @Test
    void simple() {
        assertEquals(9, solution.evalRPN(new String[]{"2", "1", "+", "3", "*"}));
    }

    @Test
    void division() {
        assertEquals(6, solution.evalRPN(new String[]{"4", "13", "5", "/", "+"}));
    }

    @Test
    void longer() {
        assertEquals(22, solution.evalRPN(new String[]{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}));
    }
}
''',
trace=r'''
function run(tokens) {
  const st = [];
  A.step('Read tokens left to right. Numbers wait on the stack until an operator needs them.', A.arr('tokens', tokens), A.stack('stack', st));
  tokens.forEach((t, i) => {
    if ('+-*/'.includes(t) && t.length === 1) {
      const b = st.pop(), a = st.pop();
      const r = t === '+' ? a + b : t === '-' ? a - b : t === '*' ? a * b : Math.trunc(a / b);
      st.push(r);
      A.step(`'${t}': pop ${b} and ${a}, compute ${a} ${t} ${b} = ${r}, and push it.`, A.arr('tokens', tokens, { hl: { [i]: 'alt' } }), A.stack('stack', st));
    } else { st.push(+t); A.step(`Push the number ${t}.`, A.arr('tokens', tokens, { hl: { [i]: 'cur' } }), A.stack('stack', st)); }
  });
  A.step(`The value left on the stack is the answer: ${st[0]}.`, A.text('Result', st[0], 'ok'));
}
A.scenario('Simple', '["2","1","+","3","*"]', () => run(['2', '1', '+', '3', '*']));
A.scenario('Division truncates', '["4","13","5","/","+"]', () => run(['4', '13', '5', '/', '+']));
'''),

P(num=224, slug="basic-calculator", title="Basic Calculator", diff="Hard", topic="Stack", cls="BasicCalculator",
idea="Keep a running result and sign; on '(' push them and start fresh, on ')' fold the inner result back in.",
vname="Sign stack",
spec=r'''
Evaluate a valid expression string `s` containing non-negative integers, `+`, `-`, parentheses and spaces. `-` may also be unary
(e.g. `"-(2 + 3)"`). Do not use `eval`.

**Example 1**
```
Input:  s = "1 + 1"
Output: 2
```

**Example 2**
```
Input:  s = " 2-1 + 2 "
Output: 3
```

**Example 3**
```
Input:  s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

**Constraints**
* `1 <= s.length <= 3 * 10^5`; the result and intermediate values fit in 32-bit integers.
''',
approach=r'''
**Result + sign, with a stack for parentheses.** Read numbers digit by digit; on `+`/`-` add `sign * number` to `result` and set the
next sign. On `(`, push the current `result` and `sign`, then reset both. On `)`, finish the inner number, then
`result = pushedResult + pushedSign * result`.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the stack grows with parenthesis depth.
''',
java=r'''
public class BasicCalculator {

    public int calculate(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        int result = 0, number = 0, sign = 1;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                number = number * 10 + (c - '0');
            } else if (c == '+' || c == '-') {
                result += sign * number;
                number = 0;
                sign = c == '+' ? 1 : -1;
            } else if (c == '(') {
                stack.push(result);
                stack.push(sign);
                result = 0;
                sign = 1;
            } else if (c == ')') {
                result += sign * number;
                number = 0;
                result = stack.pop() * result + stack.pop();
            }
        }
        return result + sign * number;
    }
}
''',
test=r'''
class BasicCalculatorTest {

    private final BasicCalculator solution = new BasicCalculator();

    @ParameterizedTest
    @CsvSource({"'1 + 1',2", "' 2-1 + 2 ',3", "'(1+(4+5+2)-3)+(6+8)',23", "'-(2 + 3)',-5", "'1-(     -2)',3", "'2147483647',2147483647"})
    void evaluates(String s, int expected) {
        assertEquals(expected, solution.calculate(s));
    }
}
''',
trace=r'''
function run(s) {
  const st = []; let result = 0, num = 0, sign = 1;
  const v = (i, c) => [A.chars('s', s.replace(/ /g, '·'), { hl: { [i]: c } }), A.vars({ result, number: num, sign: sign > 0 ? '+' : '−' }), A.stack('saved (result, sign)', st.map((x, k) => (k % 2 ? (x > 0 ? 'sign +' : 'sign −') : 'result ' + x)))];
  A.step('Keep a running result and the sign for the next number. Parentheses save the outer state on a stack.', ...v(-1));
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (c >= '0' && c <= '9') { num = num * 10 + +c; A.step(`Digit ${c}: the number being read is ${num}.`, ...v(i, 'cur')); }
    else if (c === '+' || c === '-') { result += sign * num; num = 0; sign = c === '+' ? 1 : -1; A.step(`'${c}': add the finished number to the result, which is now ${result}. The next number gets sign ${c}.`, ...v(i, 'alt')); }
    else if (c === '(') { st.push(result, sign); result = 0; sign = 1; A.step("'(': save the outer result and sign, then start fresh inside the parentheses.", ...v(i, 'sel')); }
    else if (c === ')') { result += sign * num; num = 0; const sg = st.pop(), prev = st.pop(); const inner = result; result = prev + sg * result; sign = 1; A.step(`')': the inner value is ${inner}. Combine with the saved state: ${prev} ${sg > 0 ? '+' : '−'} ${inner} = ${result}.`, ...v(i, 'ok')); }
  }
  result += sign * num;
  A.step(`Add the last number. The result is ${result}.`, A.text('Result', result, 'ok'));
}
A.scenario('Nested parentheses', 's = "(1+(4+5+2)-3)+(6+8)"', () => run('(1+(4+5+2)-3)+(6+8)'));
A.scenario('Unary minus', 's = "-(2 + 3)"', () => run('-(2 + 3)'));
'''),

P(num=141, slug="linked-list-cycle", title="Linked List Cycle", diff="Easy", topic="Linked List", cls="LinkedListCycle",
idea="A fast pointer (two steps) laps a slow pointer (one step) only if the list loops.",
vname="Floyd fast and slow pointers", helpers=["ListNode"],
spec=r'''
Given the `head` of a linked list, return `true` if the list has a **cycle**: some node can be reached again by following `next`.

**Example 1**
```
Input:  3 → 2 → 0 → -4 → (back to 2)
Output: true
```

**Example 2**
```
Input:  1 → 2 → null
Output: false
```

**Constraints**
* `0 <= number of nodes <= 10^4`

**Follow-up:** O(1) memory.
''',
approach=r'''
**Floyd's tortoise and hare.** Move `slow` one step and `fast` two steps. If `fast` reaches `null` there is no cycle. Inside a cycle,
the gap between them shrinks by one each step, so they must meet.

* Time: **O(n)** — fast enters the cycle within n steps and catches slow within one lap.
* Space: **O(1)** — two pointers.
''',
java=r'''
public class LinkedListCycle {

    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
}
''',
test=r'''
class LinkedListCycleTest {

    private final LinkedListCycle solution = new LinkedListCycle();

    /** Builds a list whose tail points back to the node at index pos (pos = -1: no cycle). */
    private static ListNode withCycle(int pos, int... values) {
        ListNode[] nodes = new ListNode[values.length];
        for (int i = 0; i < values.length; i++) nodes[i] = new ListNode(values[i]);
        for (int i = 0; i + 1 < values.length; i++) nodes[i].next = nodes[i + 1];
        if (pos >= 0) nodes[values.length - 1].next = nodes[pos];
        return nodes[0];
    }

    @Test
    void cycle() {
        assertTrue(solution.hasCycle(withCycle(1, 3, 2, 0, -4)));
    }

    @Test
    void selfLoop() {
        assertTrue(solution.hasCycle(withCycle(0, 1)));
    }

    @Test
    void noCycle() {
        assertFalse(solution.hasCycle(ListNode.of(1, 2)));
        assertFalse(solution.hasCycle(null));
    }
}
''',
trace=r'''
function run(vals, pos) {
  const n = vals.length, next = i => (i + 1 < n ? i + 1 : pos >= 0 ? pos : -1);
  const note = pos >= 0 ? `back to index ${pos} (${vals[pos]})` : 'null';
  let slow = 0, fast = 0;
  A.step(`The last node points ${pos >= 0 ? 'back to index ' + pos : 'to null'}. slow moves 1 step, fast moves 2.`, A.list('list', vals, { ptr: [[0, 'slow'], [0, 'fast']], note }));
  while (true) {
    const f1 = next(fast), f2 = f1 < 0 ? -1 : next(f1);
    if (f1 < 0 || f2 < 0) { A.step('fast ran off the end of the list, so there is no cycle.', A.list('list', vals, { ptr: [[slow, 'slow']], note }), A.text('Result', 'false', 'bad')); return; }
    slow = next(slow); fast = f2;
    if (slow === fast) { A.step(`slow and fast meet at ${vals[slow]}. Only a loop lets fast catch up from behind, so there is a cycle.`, A.list('list', vals, { ptr: [[slow, 'slow'], [fast, 'fast']], hl: { [slow]: 'ok' }, note }), A.text('Result', 'true', 'ok')); return; }
    A.step(`slow moves to ${vals[slow]}; fast jumps to ${vals[fast]}.`, A.list('list', vals, { ptr: [[slow, 'slow'], [fast, 'fast']], hl: { [slow]: 'cur', [fast]: 'alt' }, note }));
  }
}
A.scenario('Cycle', '3 → 2 → 0 → -4 → back to 2', () => run([3, 2, 0, -4], 1));
A.scenario('No cycle', '1 → 2 → 3 → 4 → 5', () => run([1, 2, 3, 4, 5], -1));
''',
variants=[dict(
name="Visited-node set",
idea="Remember every node visited; meeting one again means there is a cycle.",
approach=r'''
**Hash set of nodes.** Walk the list and add each node (by identity) to a `MyHashSet`; if a node is already present, the list loops.

* Time: **O(n)** — each node is visited once.
* Space: **O(n)** — the set of visited nodes.
''',
java=r'''
public class LinkedListCycle {

    public boolean hasCycle(ListNode head) {
        MyHashSet<ListNode> seen = new MyHashSet<>();
        for (ListNode n = head; n != null; n = n.next) {
            if (!seen.add(n)) return true;
        }
        return false;
    }
}
''',
trace=r'''
function run(vals, pos) {
  const n = vals.length, note = pos >= 0 ? `back to index ${pos} (${vals[pos]})` : 'null', seen = new Set();
  for (let i = 0, steps = 0; i >= 0 && steps < 2 * n + 1; steps++) {
    if (seen.has('node' + i)) { A.step(`Node ${vals[i]} was already visited, so there is a cycle.`, A.list('list', vals, { ptr: [[i, 'cur']], hl: { [i]: 'ok' }, note }), A.hashTable('visited nodes', seen, { hl: 'node' + i }), A.text('Result', 'true', 'ok')); return; }
    seen.add('node' + i);
    A.step(`Visit node ${vals[i]} and remember it.`, A.list('list', vals, { ptr: [[i, 'cur']], hl: [...seen].map(k => [+k.slice(4), 'sel']), note }), A.hashTable('visited nodes', seen, { hl: 'node' + i }));
    i = i + 1 < n ? i + 1 : pos;
  }
  A.step('We reached null, so there is no cycle.', A.text('Result', 'false', 'bad'));
}
A.scenario('Cycle', '3 → 2 → 0 → -4 → back to 2', () => run([3, 2, 0, -4], 1));
''')]),

P(num=2, slug="add-two-numbers", title="Add Two Numbers", diff="Medium", topic="Linked List", cls="AddTwoNumbers",
idea="Digits are stored lowest first, so add them pairwise like on paper, carrying into the next node.",
vname="Digit-by-digit with carry", helpers=["ListNode"],
spec=r'''
Two non-negative integers are stored as linked lists with their digits in **reverse order** (ones digit first), one digit per node.
Return their sum as a linked list in the same format. Neither number has leading zeros, except the number 0 itself.

**Example 1**
```
Input:  l1 = 2 → 4 → 3, l2 = 5 → 6 → 4    (342 + 465)
Output: 7 → 0 → 8                         (807)
```

**Example 2**
```
Input:  l1 = 9 → 9 → 9 → 9, l2 = 9 → 9
Output: 8 → 9 → 0 → 0 → 1
```

**Constraints**
* Each list has `1..100` nodes; `0 <= Node.val <= 9`.
''',
approach=r'''
**Schoolbook addition.** Walk both lists together; `sum = x + y + carry`, emit `sum % 10`, carry `sum / 10`. Continue while
either list has nodes or a carry remains. A dummy head keeps the code simple.

* Time: **O(max(m, n))** — one step per digit.
* Space: **O(1)** — apart from the output list.
''',
tc="n",
java=r'''
public class AddTwoNumbers {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0), tail = dummy;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int sum = carry;
            if (l1 != null) { sum += l1.val; l1 = l1.next; }
            if (l2 != null) { sum += l2.val; l2 = l2.next; }
            tail.next = new ListNode(sum % 10);
            tail = tail.next;
            carry = sum / 10;
        }
        return dummy.next;
    }
}
''',
test=r'''
class AddTwoNumbersTest {

    private final AddTwoNumbers solution = new AddTwoNumbers();

    @Test
    void example1() {
        assertArrayEquals(new int[]{7, 0, 8}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(2, 4, 3), ListNode.of(5, 6, 4))));
    }

    @Test
    void zeros() {
        assertArrayEquals(new int[]{0}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(0), ListNode.of(0))));
    }

    @Test
    void carryOut() {
        assertArrayEquals(new int[]{8, 9, 0, 0, 1}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(9, 9, 9, 9), ListNode.of(9, 9))));
    }
}
''',
trace=r'''
function run(a, b) {
  const out = []; let carry = 0, i = 0;
  A.step(`The lists hold ${[...a].reverse().join('')} and ${[...b].reverse().join('')}, ones digit first. Add them column by column.`, A.list('l1', a), A.list('l2', b), A.list('sum', out));
  while (i < a.length || i < b.length || carry) {
    const x = a[i] ?? 0, y = b[i] ?? 0, s = x + y + carry;
    out.push(s % 10);
    A.step(`${x} + ${y}${carry ? ' + carry 1' : ''} = ${s}. Write ${s % 10}${s >= 10 ? ' and carry 1' : ''}.`, A.list('l1', a, { hl: { [i]: 'cur' } }), A.list('l2', b, { hl: { [i]: 'cur' } }), A.list('sum', out, { hl: { [out.length - 1]: 'ok' } }), A.vars({ carry: Math.floor(s / 10) }));
    carry = Math.floor(s / 10); i++;
  }
  A.step(`The sum is ${[...out].reverse().join('')}.`, A.list('sum', out, { hl: out.map((_, k) => [k, 'ok']) }), A.text('Result', out.join(' → '), 'ok'));
}
A.scenario('342 + 465', 'l1 = 2→4→3, l2 = 5→6→4', () => run([2, 4, 3], [5, 6, 4]));
A.scenario('Carry out', 'l1 = 9→9→9→9, l2 = 9→9', () => run([9, 9, 9, 9], [9, 9]));
'''),

P(num=21, slug="merge-two-sorted-lists", title="Merge Two Sorted Lists", diff="Easy", topic="Linked List", cls="MergeTwoSortedLists",
idea="Repeatedly take the smaller head and attach it to the tail of the merged list.",
vname="Iterative with dummy head", helpers=["ListNode"],
spec=r'''
Merge two sorted linked lists `list1` and `list2` into one sorted list by splicing their nodes together. Return its head.

**Example 1**
```
Input:  list1 = 1 → 2 → 4, list2 = 1 → 3 → 4
Output: 1 → 1 → 2 → 3 → 4 → 4
```

**Example 2**
```
Input:  list1 = null, list2 = 0
Output: 0
```

**Constraints**
* `0..50` nodes per list; `-100 <= Node.val <= 100`; both sorted non-decreasing.
''',
approach=r'''
**Dummy head + tail pointer.** While both lists have nodes, attach the smaller head to `tail` and advance it. Attach whatever remains.

* Time: **O(m + n)** — each node is attached once.
* Space: **O(1)** — nodes are re-linked, not copied.
''',
tc="n",
java=r'''
public class MergeTwoSortedLists {

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0), tail = dummy;
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }
        tail.next = list1 != null ? list1 : list2;
        return dummy.next;
    }
}
''',
test=r'''
class MergeTwoSortedListsTest {

    private final MergeTwoSortedLists solution = new MergeTwoSortedLists();

    @Test
    void interleaved() {
        assertArrayEquals(new int[]{1, 1, 2, 3, 4, 4}, ListNode.toArray(solution.mergeTwoLists(ListNode.of(1, 2, 4), ListNode.of(1, 3, 4))));
    }

    @Test
    void bothEmpty() {
        assertNull(solution.mergeTwoLists(null, null));
    }

    @Test
    void oneEmpty() {
        assertArrayEquals(new int[]{0}, ListNode.toArray(solution.mergeTwoLists(null, ListNode.of(0))));
    }
}
''',
trace=r'''
function run(a, b) {
  let i = 0, j = 0; const out = [];
  A.step('Compare the two heads and attach the smaller one to the merged list.', A.list('list1', a, { ptr: [[0, 'p1']] }), A.list('list2', b, { ptr: [[0, 'p2']] }), A.list('merged', out));
  while (i < a.length && j < b.length) {
    const fromA = a[i] <= b[j];
    out.push(fromA ? a[i] : b[j]);
    A.step(`${a[i]} vs ${b[j]}: attach ${fromA ? a[i] + ' from list1' : b[j] + ' from list2'}.`, A.list('list1', a, { ptr: [[i, 'p1']], hl: a.map((_, k) => [k, k < i ? 'dim' : k === i && fromA ? 'ok' : '']) }), A.list('list2', b, { ptr: [[j, 'p2']], hl: b.map((_, k) => [k, k < j ? 'dim' : k === j && !fromA ? 'ok' : '']) }), A.list('merged', out, { hl: { [out.length - 1]: 'ok' } }));
    if (fromA) i++; else j++;
  }
  const rest = i < a.length ? a.slice(i) : b.slice(j);
  out.push(...rest);
  A.step(rest.length ? `One list is empty. Attach the rest of the other (${rest.join(', ')}) in one step.` : 'Both lists are used up.', A.list('merged', out, { hl: out.map((_, k) => [k, k >= out.length - rest.length ? 'sel' : 'ok']) }));
}
A.scenario('Interleaved', 'list1 = 1→2→4, list2 = 1→3→4', () => run([1, 2, 4], [1, 3, 4]));
A.scenario('Long tail', 'list1 = 5, list2 = 1→2→3→6', () => run([5], [1, 2, 3, 6]));
''',
variants=[dict(
name="Recursive",
idea="The smaller head comes first; its next is the merge of everything that remains.",
approach=r'''
**Recursion.** If either list is empty, return the other. Otherwise the smaller head wins and its `next` becomes
`mergeTwoLists(winner.next, other)`.

* Time: **O(m + n)** — one call per node.
* Space: **O(m + n)** — the recursion depth.
''',
tc="n", sc="n",
java=r'''
public class MergeTwoSortedLists {

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;
        if (list1.val <= list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        }
        list2.next = mergeTwoLists(list1, list2.next);
        return list2;
    }
}
''',
trace=r'''
function run(a, b) {
  const calls = [];
  function rec(i, j) {
    calls.push(`merge(${a.slice(i).join('→') || '∅'}, ${b.slice(j).join('→') || '∅'})`);
    A.step(`Call ${calls[calls.length - 1]}.`, A.stack('call stack', calls));
    if (i >= a.length || j >= b.length) { const r = i >= a.length ? b.slice(j) : a.slice(i); calls.pop(); A.step(`One list is empty, so return the other: ${r.join('→') || '∅'}.`, A.stack('call stack', calls)); return r; }
    const fromA = a[i] <= b[j], rest = fromA ? rec(i + 1, j) : rec(i, j + 1), r = [fromA ? a[i] : b[j], ...rest];
    calls.pop();
    A.step(`${fromA ? a[i] : b[j]} is the smaller head; put it in front of the merged rest: ${r.join('→')}.`, A.stack('call stack', calls), A.list('result so far', r, { hl: { 0: 'ok' } }));
    return r;
  }
  rec(0, 0);
}
A.scenario('Interleaved', 'list1 = 1→2→4, list2 = 1→3→4', () => run([1, 2, 4], [1, 3, 4]));
''')]),

P(num=138, slug="copy-list-with-random-pointer", title="Copy List with Random Pointer", diff="Medium", topic="Linked List", cls="CopyRandomList",
idea="Weave each copy right after its original, wire randoms via original.random.next, then unweave.",
vname="Interleaved copies",
spec=r'''
Each node of a linked list has `val`, `next`, and `random`, which points to any node in the list or `null`. Return a **deep copy**:
new nodes with the same values whose `next` and `random` pointers mirror the original structure, never pointing into the original list.

**Example**
```
Input:  [[7,null],[13,0],[11,4],[10,2],[1,0]]   ([val, index of random])
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]   (a separate copy)
```

**Constraints**
* `0 <= n <= 1000`; `-10^4 <= Node.val <= 10^4`
''',
approach=r'''
**Three passes, no map.** (1) Insert a copy after every node: `A → A' → B → B' …`. (2) For each original, set
`copy.random = original.random == null ? null : original.random.next`. (3) Split the woven list into the original and the copy.

* Time: **O(n)** — three linear passes.
* Space: **O(1)** — apart from the copied nodes themselves.
''',
java=r'''
public class CopyRandomList {

    /** List node with an extra random pointer. */
    public static class Node {
        public int val;
        public Node next;
        public Node random;

        public Node(int val) { this.val = val; }
    }

    public Node copyRandomList(Node head) {
        for (Node n = head; n != null; n = n.next.next) {
            Node copy = new Node(n.val);
            copy.next = n.next;
            n.next = copy;
        }
        for (Node n = head; n != null; n = n.next.next) {
            n.next.random = n.random == null ? null : n.random.next;
        }
        Node dummy = new Node(0), tail = dummy;
        for (Node n = head; n != null; n = n.next) {
            tail.next = n.next;
            tail = tail.next;
            n.next = tail.next;
        }
        return dummy.next;
    }
}
''',
test=r'''
class CopyRandomListTest {

    private final CopyRandomList solution = new CopyRandomList();

    /** Builds a list from [val, randomIndex] pairs (randomIndex -1 = null). */
    private static CopyRandomList.Node build(int[][] spec) {
        CopyRandomList.Node[] nodes = new CopyRandomList.Node[spec.length];
        for (int i = 0; i < spec.length; i++) nodes[i] = new CopyRandomList.Node(spec[i][0]);
        for (int i = 0; i < spec.length; i++) {
            if (i + 1 < spec.length) nodes[i].next = nodes[i + 1];
            if (spec[i][1] >= 0) nodes[i].random = nodes[spec[i][1]];
        }
        return spec.length == 0 ? null : nodes[0];
    }

    private static List<String> describe(CopyRandomList.Node head) {
        List<CopyRandomList.Node> order = new ArrayList<>();
        for (CopyRandomList.Node n = head; n != null; n = n.next) order.add(n);
        List<String> out = new ArrayList<>();
        for (CopyRandomList.Node n : order) out.add(n.val + ":" + (n.random == null ? -1 : order.indexOf(n.random)));
        return out;
    }

    @Test
    void deepCopy() {
        int[][] spec = {{7, -1}, {13, 0}, {11, 4}, {10, 2}, {1, 0}};
        CopyRandomList.Node original = build(spec);
        CopyRandomList.Node copy = solution.copyRandomList(original);
        assertEquals(describe(build(spec)), describe(copy));
        assertEquals(describe(build(spec)), describe(original), "original must be restored");
        for (CopyRandomList.Node a = original, b = copy; a != null; a = a.next, b = b.next) assertNotSame(a, b);
    }

    @Test
    void empty() {
        assertNull(solution.copyRandomList(null));
    }
}
''',
trace=r'''
function run(spec) {
  const n = spec.length, vals = spec.map(s => s[0]);
  const rnd = spec.map(s => (s[1] < 0 ? 'null' : vals[s[1]]));
  A.step('Each node has a next pointer (the arrows) and a random pointer (listed below it).', A.list('original', vals), A.arr('random →', rnd, { noIdx: true }));
  const woven = []; vals.forEach(v => woven.push(v, v + "'"));
  A.step("Pass 1: insert a copy right after each original: A → A' → B → B' → …", A.list('woven list', woven, { hl: woven.map((_, i) => [i, i % 2 ? 'alt' : '']) }));
  const crnd = [];
  for (let i = 0; i < n; i++) {
    crnd.push(spec[i][1] < 0 ? 'null' : vals[spec[i][1]] + "'");
    A.step(`Pass 2: ${vals[i]}'.random = ${vals[i]}.random.next = ${crnd[i]}. Each original's next is its copy, so no map is needed.`, A.list('woven list', woven, { hl: { [2 * i]: 'cur', [2 * i + 1]: 'alt', ...(spec[i][1] >= 0 ? { [2 * spec[i][1] + 1]: 'ok' } : {}) } }), A.arr("copy random →", crnd, { noIdx: true }));
  }
  A.step('Pass 3: unweave. The originals get their old next pointers back, and the copies link to each other.', A.list('original', vals, { hl: vals.map((_, i) => [i, 'sel']) }), A.list('copy', vals.map(v => v + "'"), { hl: vals.map((_, i) => [i, 'ok']) }), A.arr('copy random →', crnd, { noIdx: true }));
}
A.scenario('Five nodes', '[[7,null],[13,0],[11,4],[10,2],[1,0]]', () => run([[7, -1], [13, 0], [11, 4], [10, 2], [1, 0]]));
''',
variants=[dict(
name="Old-to-new hash map",
idea="First create a copy of every node in a map, then wire next and random through the map.",
approach=r'''
**Hash map from original to copy.** Pass 1 creates every copy and stores `original → copy` in a `MyHashMap`. Pass 2 sets
`copy.next = map.get(original.next)` and `copy.random = map.get(original.random)`.

* Time: **O(n)** — two passes with O(1) average lookups.
* Space: **O(n)** — the map.
''',
java=r'''
public class CopyRandomList {

    /** List node with an extra random pointer. */
    public static class Node {
        public int val;
        public Node next;
        public Node random;

        public Node(int val) { this.val = val; }
    }

    public Node copyRandomList(Node head) {
        MyHashMap<Node, Node> copyOf = new MyHashMap<>();
        for (Node n = head; n != null; n = n.next) copyOf.put(n, new Node(n.val));
        for (Node n = head; n != null; n = n.next) {
            Node c = copyOf.get(n);
            c.next = copyOf.get(n.next);
            c.random = copyOf.get(n.random);
        }
        return copyOf.get(head);
    }
}
''',
trace=r'''
function run(spec) {
  const vals = spec.map(s => s[0]), m = new Map();
  vals.forEach((v, i) => { m.set(`#${i}:${v}`, v + "'"); A.step(`Pass 1: create a copy of node #${i} (${v}) and store original → copy.`, A.list('original', vals, { hl: { [i]: 'cur' } }), A.hashTable('original → copy', m, { hl: `#${i}:${v}` })); });
  const cr = spec.map(s => (s[1] < 0 ? 'null' : vals[s[1]] + "'"));
  A.step("Pass 2: copy.next = map[original.next] and copy.random = map[original.random].", A.list('copy', vals.map(v => v + "'"), { hl: vals.map((_, i) => [i, 'ok']) }), A.arr('copy random →', cr, { noIdx: true }));
}
A.scenario('Five nodes', '[[7,null],[13,0],[11,4],[10,2],[1,0]]', () => run([[7, -1], [13, 0], [11, 4], [10, 2], [1, 0]]));
''')]),
]
