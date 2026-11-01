PROBLEMS = [
P(num=680, slug="valid-palindrome-ii", title="Valid Palindrome II", diff="Easy", topic="Two Pointers", cls="ValidPalindromeII",
idea="Compare from both ends; at the first mismatch, try skipping either the left or the right character.",
vname="Two pointers with one skip",
spec=r'''
Return `true` if `s` can be a palindrome after deleting **at most one** character.

**Example**
```
"aba" → true,   "abca" → true (delete 'c'),   "abc" → false
```

**Constraints**
* `1 <= s.length <= 10^5`
''',
approach=r'''
**One chance.** Move inward while the ends match. At the first mismatch, the answer is whether `s[l+1..r]` or `s[l..r-1]` is a palindrome.

* Time: **O(n)** — at most two extra linear checks.
* Space: **O(1)** — indices only.
''',
java=r'''
public class ValidPalindromeII {

    public boolean validPalindrome(String s) {
        for (int l = 0, r = s.length() - 1; l < r; l++, r--) {
            if (s.charAt(l) != s.charAt(r)) return isPalindrome(s, l + 1, r) || isPalindrome(s, l, r - 1);
        }
        return true;
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
class ValidPalindromeIITest {

    private final ValidPalindromeII solution = new ValidPalindromeII();

    @ParameterizedTest
    @CsvSource({"aba,true", "abca,true", "abc,false", "deeee,true", "cbbcc,true"})
    void checks(String s, boolean expected) {
        assertEquals(expected, solution.validPalindrome(s));
    }
}
''',
trace=r'''
function run(s) {
  const pal = (l, r) => { while (l < r) if (s[l++] !== s[r--]) return false; return true; };
  for (let l = 0, r = s.length - 1; l < r; l++, r--) {
    if (s[l] === s[r]) { A.step(`'${s[l]}' = '${s[r]}'. Move inward.`, A.chars('s', s, { hl: { [l]: 'ok', [r]: 'ok' } })); continue; }
    const a = pal(l + 1, r), b = pal(l, r - 1);
    A.step(`'${s[l]}' ≠ '${s[r]}'. Try deleting the left one: ${a ? 'palindrome' : 'no'}. Try deleting the right one: ${b ? 'palindrome' : 'no'}.`, A.chars('s', s, { hl: { [l]: 'bad', [r]: 'bad' } }), A.text('Result', String(a || b), a || b ? 'ok' : 'bad'));
    return;
  }
  A.step('Already a palindrome.', A.text('Result', 'true', 'ok'));
}
A.scenario('One deletion', 's = "abca"', () => run('abca'));
'''),

P(num=682, slug="baseball-game", title="Baseball Game", diff="Easy", topic="Stack", cls="BaseballGame",
idea="A stack of valid scores: numbers push, '+' adds the top two, 'D' doubles the top, 'C' pops.",
vname="Score stack",
spec=r'''
Process operations: an integer records that score; `"+"` records the sum of the previous two scores; `"D"` records double the previous score;
`"C"` removes the previous score. Return the sum of the remaining scores.

**Example**
```
["5","2","C","D","+"] → 30,   ["5","-2","4","C","D","9","+","+"] → 27
```

**Constraints**
* `1 <= operations.length <= 1000`
''',
approach=r'''
**Stack.** Apply each operation to a stack of scores, then sum the stack.

* Time: **O(n)** — O(1) per operation.
* Space: **O(n)** — the stack.
''',
java=r'''
public class BaseballGame {

    public int calPoints(String[] operations) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (String op : operations) {
            switch (op) {
                case "+" -> {
                    int top = stack.pop(), second = stack.peek();
                    stack.push(top);
                    stack.push(top + second);
                }
                case "D" -> stack.push(2 * stack.peek());
                case "C" -> stack.pop();
                default -> stack.push(Integer.parseInt(op));
            }
        }
        int sum = 0;
        for (int x : stack) sum += x;
        return sum;
    }
}
''',
test=r'''
class BaseballGameTest {

    private final BaseballGame solution = new BaseballGame();

    @Test
    void examples() {
        assertEquals(30, solution.calPoints(new String[]{"5", "2", "C", "D", "+"}));
        assertEquals(27, solution.calPoints(new String[]{"5", "-2", "4", "C", "D", "9", "+", "+"}));
        assertEquals(0, solution.calPoints(new String[]{"1", "C"}));
    }
}
''',
trace=r'''
function run(ops) {
  const st = [];
  ops.forEach((op, i) => {
    let msg;
    if (op === '+') { st.push(st[st.length - 1] + st[st.length - 2]); msg = `'+': record ${st[st.length - 3]} + ${st[st.length - 2]} = ${st[st.length - 1]}.`; }
    else if (op === 'D') { st.push(2 * st[st.length - 1]); msg = `'D': record double the last score, ${st[st.length - 1]}.`; }
    else if (op === 'C') { const g = st.pop(); msg = `'C': cancel the last score (${g}).`; }
    else { st.push(+op); msg = `Record ${op}.`; }
    A.step(msg, A.arr('operations', ops, { hl: { [i]: 'cur' } }), A.stack('scores', st));
  });
  const sum = st.reduce((s, x) => s + x, 0);
  A.step(`Total: ${sum}.`, A.text('Result', sum, 'ok'));
}
A.scenario('Classic', '["5","2","C","D","+"]', () => run(['5', '2', 'C', 'D', '+']));
'''),

P(num=692, slug="top-k-frequent-words", title="Top K Frequent Words", diff="Medium", topic="Heap", cls="TopKFrequentWords",
idea="Count words, then keep a size-k heap ordered so the 'worst' word (lowest count, then largest alphabetically) is on top.",
vname="Counting + bounded heap",
spec=r'''
Return the `k` most frequent words, sorted by frequency (highest first); equal frequencies are sorted alphabetically.

**Example**
```
["i","love","leetcode","i","love","coding"], k = 2 → ["i","love"]
["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4 → ["the","is","sunny","day"]
```

**Constraints**
* `1 <= words.length <= 500`; `k` is valid.
''',
approach=r'''
**Bounded heap.** Count with `MyHashMap`. Push each word into a heap whose top is the least desirable word (lower count first, then
alphabetically later); pop when the size exceeds `k`. Pop all and reverse.

* Time: **O(n log k)** — heap operations of size k.
* Space: **O(n)** — the counts.
''',
tc="nlogn", sc="n",
java=r'''
public class TopKFrequentWords {

    public List<String> topKFrequent(String[] words, int k) {
        MyHashMap<String, Integer> count = new MyHashMap<>();
        for (String w : words) count.merge(w, 1, Integer::sum);
        PriorityQueue<String> heap = new PriorityQueue<>((a, b) -> {
            int ca = count.get(a), cb = count.get(b);
            return ca != cb ? Integer.compare(ca, cb) : b.compareTo(a);
        });
        for (String w : count.keys()) {
            heap.add(w);
            if (heap.size() > k) heap.poll();
        }
        LinkedList<String> out = new LinkedList<>();
        while (!heap.isEmpty()) out.addFirst(heap.poll());
        return out;
    }
}
''',
test=r'''
class TopKFrequentWordsTest {

    private final TopKFrequentWords solution = new TopKFrequentWords();

    @Test
    void examples() {
        assertEquals(List.of("i", "love"), solution.topKFrequent(new String[]{"i", "love", "leetcode", "i", "love", "coding"}, 2));
        assertEquals(List.of("the", "is", "sunny", "day"),
                solution.topKFrequent(new String[]{"the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"}, 4));
    }
}
''',
trace=r'''
function run(words, k) {
  const cnt = new Map(); words.forEach(w => cnt.set(w, (cnt.get(w) || 0) + 1));
  A.step('Count every word.', A.hashTable('counts', cnt));
  const sorted = [...cnt.keys()].sort((a, b) => cnt.get(b) - cnt.get(a) || (a < b ? -1 : 1));
  A.step(`Order by count (highest first), ties alphabetically. A heap of size ${k} keeps only the best ${k} while scanning.`, A.arr('ranked', sorted.map(w => `${w}:${cnt.get(w)}`), { hl: Object.fromEntries(sorted.map((_, i) => [i, i < k ? 'ok' : 'dim'])) }));
  A.step(`Top ${k}: [${sorted.slice(0, k)}].`, A.text('Result', JSON.stringify(sorted.slice(0, k)), 'ok'));
}
A.scenario('k = 4', 'the, day, is, sunny …', () => run(['the', 'day', 'is', 'sunny', 'the', 'the', 'the', 'sunny', 'is', 'is'], 4));
'''),

P(num=705, slug="design-hashset", title="Design HashSet", diff="Easy", topic="Design", cls="DesignHashSet",
idea="Buckets of chained keys, indexed by a spread hash; double the bucket array when it gets crowded.",
vname="Separate chaining with resizing",
spec=r'''
Design a hash set **without** any built-in hash table library: `add(key)`, `contains(key)`, `remove(key)` (removing a missing key does
nothing).

**Example**
```
add(1); add(2); contains(1) → true; contains(3) → false; add(2); contains(2) → true; remove(2); contains(2) → false
```

**Constraints**
* `0 <= key <= 10^6`; at most `10^4` calls.
''',
approach=r'''
**Buckets + chaining.** A power-of-two array of singly linked lists. `index = (h ^ h >>> 16) & (capacity - 1)`. `add` prepends when the key is
absent and doubles the array once the number of keys exceeds 75% of the bucket count.

* Time: **O(1)** — average per operation.
* Space: **O(n)** — one node per key plus the buckets.
''',
tc="1", sc="n",
java=r'''
public class DesignHashSet {

    private static final class Node {
        final int key;
        Node next;

        Node(int key, Node next) {
            this.key = key;
            this.next = next;
        }
    }

    private Node[] buckets = new Node[16];
    private int size;

    private int index(int key, int capacity) {
        int h = Integer.hashCode(key);
        return (h ^ (h >>> 16)) & (capacity - 1);
    }

    public void add(int key) {
        if (contains(key)) return;
        int i = index(key, buckets.length);
        buckets[i] = new Node(key, buckets[i]);
        if (++size > buckets.length * 3 / 4) resize();
    }

    public boolean contains(int key) {
        for (Node n = buckets[index(key, buckets.length)]; n != null; n = n.next) {
            if (n.key == key) return true;
        }
        return false;
    }

    public void remove(int key) {
        int i = index(key, buckets.length);
        for (Node prev = null, n = buckets[i]; n != null; prev = n, n = n.next) {
            if (n.key == key) {
                if (prev == null) buckets[i] = n.next; else prev.next = n.next;
                size--;
                return;
            }
        }
    }

    private void resize() {
        Node[] old = buckets;
        buckets = new Node[old.length * 2];
        for (Node head : old) {
            for (Node n = head; n != null; ) {
                Node next = n.next;
                int i = index(n.key, buckets.length);
                n.next = buckets[i];
                buckets[i] = n;
                n = next;
            }
        }
    }
}
''',
test=r'''
class DesignHashSetTest {

    @Test
    void example() {
        DesignHashSet s = new DesignHashSet();
        s.add(1);
        s.add(2);
        assertTrue(s.contains(1));
        assertFalse(s.contains(3));
        s.add(2);
        assertTrue(s.contains(2));
        s.remove(2);
        assertFalse(s.contains(2));
        s.remove(42);
    }

    @Test
    void many() {
        DesignHashSet s = new DesignHashSet();
        for (int k = 0; k < 3000; k++) s.add(k * 32);
        for (int k = 0; k < 3000; k++) assertTrue(s.contains(k * 32));
        assertFalse(s.contains(1));
    }
}
''',
trace=r'''
A.scenario('Add, check, remove', 'add 1, 9, 17, 2 · contains 9 · remove 9', () => {
  const s = new Set();
  const view = (msg, hl) => A.step(msg, A.hashTable('buckets', s, { capacity: 8, hl }));
  view('8 buckets. A key lands in bucket (hash ^ hash >>> 16) & 7; colliding keys are chained.');
  for (const k of [1, 9, 17, 2]) { s.add(k); view(`add(${k}): bucket ${k & 7}.`, k); }
  view('contains(9): walk bucket 1’s chain until 9 is found.', 9);
  s.delete(9); view('remove(9): unlink its node from the chain.');
});
'''),

P(num=709, slug="to-lower-case", title="To Lower Case", diff="Easy", topic="Strings", cls="ToLowerCase",
idea="Upper-case letters A–Z sit exactly 32 code points below their lower-case versions.",
vname="Character arithmetic",
spec=r'''
Return `s` with every uppercase letter replaced by its lowercase version.

**Example**
```
"Hello" → "hello",   "LOVELY" → "lovely"
```

**Constraints**
* `1 <= s.length <= 100`; printable ASCII.
''',
approach=r'''
**ASCII offset.** For each character in `'A'..'Z'`, add 32 (`'a' - 'A'`); leave others alone.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the result.
''',
sc="n",
java=r'''
public class ToLowerCase {

    public String toLowerCase(String s) {
        char[] a = s.toCharArray();
        for (int i = 0; i < a.length; i++) {
            if (a[i] >= 'A' && a[i] <= 'Z') a[i] = (char) (a[i] + ('a' - 'A'));
        }
        return new String(a);
    }
}
''',
test=r'''
class ToLowerCaseTest {

    private final ToLowerCase solution = new ToLowerCase();

    @ParameterizedTest
    @CsvSource({"Hello,hello", "here,here", "LOVELY,lovely", "A1-Z,a1-z"})
    void lowers(String s, String expected) {
        assertEquals(expected, solution.toLowerCase(s));
    }
}
''',
trace=r'''
function run(s) {
  const a = [...s];
  a.forEach((c, i) => { const up = c >= 'A' && c <= 'Z'; if (up) a[i] = String.fromCharCode(c.charCodeAt(0) + 32); A.step(up ? `'${c}' (${c.charCodeAt(0)}) + 32 = '${a[i]}' (${a[i].charCodeAt(0)}).` : `'${c}' is not an uppercase letter.`, A.chars('s', a.join(''), { hl: { [i]: up ? 'ok' : 'dim' } })); });
  A.step(`Result: "${a.join('')}".`, A.text('Result', a.join(''), 'ok'));
}
A.scenario('Mixed case', 's = "HeLLo"', () => run('HeLLo'));
'''),

P(num=713, slug="subarray-product-less-than-k", title="Subarray Product Less Than K", diff="Medium", topic="Sliding Window", cls="SubarrayProductLessThanK",
idea="Grow the window right, shrink left while the product is too big; every window ending at right contributes its length.",
vname="Sliding window on the product",
spec=r'''
Given positive integers `nums`, return the number of contiguous subarrays whose product is **strictly less** than `k`.

**Example**
```
nums = [10,5,2,6], k = 100 → 8,   nums = [1,2,3], k = 0 → 0
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`; `1 <= nums[i] <= 1000`; `0 <= k <= 10^6`
''',
approach=r'''
**Window.** Multiply in `nums[right]`; while the product is `>= k`, divide out `nums[left]` and advance. All subarrays ending at `right` and
starting in `[left, right]` are valid: add `right - left + 1`. If `k <= 1`, nothing qualifies.

* Time: **O(n)** — each index enters and leaves once.
* Space: **O(1)** — a product and two indices.
''',
java=r'''
public class SubarrayProductLessThanK {

    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) return 0;
        long product = 1;
        int count = 0, left = 0;
        for (int right = 0; right < nums.length; right++) {
            product *= nums[right];
            while (product >= k) product /= nums[left++];
            count += right - left + 1;
        }
        return count;
    }
}
''',
test=r'''
class SubarrayProductLessThanKTest {

    private final SubarrayProductLessThanK solution = new SubarrayProductLessThanK();

    @Test
    void examples() {
        assertEquals(8, solution.numSubarrayProductLessThanK(new int[]{10, 5, 2, 6}, 100));
        assertEquals(0, solution.numSubarrayProductLessThanK(new int[]{1, 2, 3}, 0));
        assertEquals(0, solution.numSubarrayProductLessThanK(new int[]{1, 1, 1}, 1));
    }
}
''',
trace=r'''
function run(a, k) {
  let prod = 1, left = 0, count = 0;
  for (let r = 0; r < a.length; r++) {
    prod *= a[r]; let shrunk = 0;
    while (prod >= k) { prod /= a[left++]; shrunk++; }
    count += r - left + 1;
    A.step(`Multiply in ${a[r]}.${shrunk ? ` The product reached ${k}, so drop ${shrunk} from the left.` : ''} Product ${prod}. ${r - left + 1} subarray${r - left ? 's' : ''} end here. Total ${count}.`, A.arr('nums', a, { range: [left, r], hl: { [r]: 'cur' } }), A.vars({ product: prod, count }));
  }
  A.step(`${count} subarrays have a product below ${k}.`, A.text('Result', count, 'ok'));
}
A.scenario('k = 100', 'nums = [10,5,2,6]', () => run([10, 5, 2, 6], 100));
'''),

P(num=733, slug="flood-fill", title="Flood Fill", diff="Easy", topic="Graph General", cls="FloodFill",
idea="DFS from the start pixel, repainting every connected pixel that has the original colour.",
vname="Iterative DFS",
spec=r'''
Starting from pixel `(sr, sc)`, repaint it and every 4-directionally connected pixel of the same original colour with `color`. Return the image.

**Example**
```
image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2 → [[2,2,2],[2,2,0],[2,0,1]]
```

**Constraints**
* `1 <= m, n <= 50`
''',
approach=r'''
**DFS with a stack.** If the start already has the new colour, nothing changes (and we avoid looping). Otherwise paint pixels as they are
pushed and spread to same-coloured neighbours.

* Time: **O(m·n)** — each pixel at most once.
* Space: **O(m·n)** — the stack.
''',
tc="n2", sc="n2",
java=r'''
public class FloodFill {

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int old = image[sr][sc];
        if (old == color) return image;
        int m = image.length, n = image[0].length;
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{sr, sc});
        image[sr][sc] = color;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.isEmpty()) {
            int[] p = stack.pop();
            for (int[] d : dirs) {
                int r = p[0] + d[0], c = p[1] + d[1];
                if (r >= 0 && r < m && c >= 0 && c < n && image[r][c] == old) {
                    image[r][c] = color;
                    stack.push(new int[]{r, c});
                }
            }
        }
        return image;
    }
}
''',
test=r'''
class FloodFillTest {

    private final FloodFill solution = new FloodFill();

    @Test
    void examples() {
        assertArrayEquals(new int[][]{{2, 2, 2}, {2, 2, 0}, {2, 0, 1}}, solution.floodFill(new int[][]{{1, 1, 1}, {1, 1, 0}, {1, 0, 1}}, 1, 1, 2));
        assertArrayEquals(new int[][]{{0, 0, 0}, {0, 0, 0}}, solution.floodFill(new int[][]{{0, 0, 0}, {0, 0, 0}}, 0, 0, 0));
    }
}
''',
trace=r'''
function run(img, sr, sc, color) {
  const g = img.map(r => r.slice()), old = g[sr][sc], m = g.length, n = g[0].length, st = [[sr, sc]];
  g[sr][sc] = color;
  A.step(`Repaint (${sr},${sc}) from ${old} to ${color} and spread to neighbours that were ${old}.`, A.grid('image', g, { hl: { [`${sr},${sc}`]: 'cur' } }));
  while (st.length) {
    const [r, c] = st.pop(), painted = [];
    for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const a = r + dr, b = c + dc; if (a >= 0 && a < m && b >= 0 && b < n && g[a][b] === old) { g[a][b] = color; st.push([a, b]); painted.push(`${a},${b}`); } }
    if (painted.length) A.step(`From (${r},${c}), paint ${painted.length} neighbour${painted.length > 1 ? 's' : ''}.`, A.grid('image', g, { hl: { [`${r},${c}`]: 'sel', ...Object.fromEntries(painted.map(p => [p, 'ok'])) } }));
  }
  A.step('Nothing left to paint.', A.grid('image', g));
}
A.scenario('Classic', 'image = [[1,1,1],[1,1,0],[1,0,1]], start (1,1)', () => run([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2));
'''),

P(num=744, slug="find-smallest-letter-greater-than-target", title="Find Smallest Letter Greater Than Target", diff="Easy", topic="Binary Search", cls="SmallestLetterGreaterThanTarget",
idea="Binary-search the first letter strictly greater than the target; wrap around to the first letter if none.",
vname="Upper-bound binary search",
spec=r'''
`letters` is sorted (non-decreasing) and contains at least two different letters. Return the smallest letter strictly greater than `target`,
or `letters[0]` if none is.

**Example**
```
letters = [c,f,j], target = a → c;  target = c → f;  letters = [x,x,y,y], target = z → x
```

**Constraints**
* `2 <= letters.length <= 10^4`
''',
approach=r'''
**Upper bound.** Find the first index with `letters[i] > target`; if it is `n`, wrap to 0.

* Time: **O(log n)** — binary search.
* Space: **O(1)** — two indices.
''',
tc="log",
java=r'''
public class SmallestLetterGreaterThanTarget {

    public char nextGreatestLetter(char[] letters, char target) {
        int lo = 0, hi = letters.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (letters[mid] <= target) lo = mid + 1; else hi = mid;
        }
        return letters[lo % letters.length];
    }
}
''',
test=r'''
class SmallestLetterGreaterThanTargetTest {

    private final SmallestLetterGreaterThanTarget solution = new SmallestLetterGreaterThanTarget();

    @Test
    void examples() {
        assertEquals('c', solution.nextGreatestLetter(new char[]{'c', 'f', 'j'}, 'a'));
        assertEquals('f', solution.nextGreatestLetter(new char[]{'c', 'f', 'j'}, 'c'));
        assertEquals('x', solution.nextGreatestLetter(new char[]{'x', 'x', 'y', 'y'}, 'z'));
    }
}
''',
trace=r'''
function run(letters, t) {
  let lo = 0, hi = letters.length;
  while (lo < hi) { const mid = (lo + hi) >> 1; const go = letters[mid] <= t; A.step(`'${letters[mid]}' ${go ? `≤ '${t}': look right` : `> '${t}': a candidate; look left for a smaller one`}.`, A.arr('letters', letters, { range: [lo, Math.min(hi, letters.length - 1)], hl: { [mid]: 'cur' } })); if (go) lo = mid + 1; else hi = mid; }
  A.step(lo === letters.length ? `No letter is greater than '${t}', so wrap around to '${letters[0]}'.` : `The first letter greater than '${t}' is '${letters[lo]}'.`, A.arr('letters', letters, { hl: { [lo % letters.length]: 'ok' } }), A.text('Result', letters[lo % letters.length], 'ok'));
}
A.scenario('target = d', "letters = [c,f,j,m,p]", () => run(['c', 'f', 'j', 'm', 'p'], 'd'));
'''),

P(num=747, slug="largest-number-at-least-twice-of-others", title="Largest Number At Least Twice of Others", diff="Easy", topic="Arrays & Hashing", cls="LargestAtLeastTwice",
idea="Only the second-largest value needs checking: largest ≥ 2 × second largest.",
vname="Track the top two",
spec=r'''
The largest value in `nums` is unique. Return its index if it is at least twice every other value, otherwise `-1`.

**Example**
```
[3,6,1,0] → 1,   [1,2,3,4] → -1
```

**Constraints**
* `2 <= nums.length <= 50`
''',
approach=r'''
**Top two.** One pass tracks the largest (and its index) and the second largest; compare `largest >= 2 × second`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — three variables.
''',
java=r'''
public class LargestAtLeastTwice {

    public int dominantIndex(int[] nums) {
        int best = -1, second = -1, idx = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > best) {
                second = best;
                best = nums[i];
                idx = i;
            } else if (nums[i] > second) {
                second = nums[i];
            }
        }
        return best >= 2 * second ? idx : -1;
    }
}
''',
test=r'''
class LargestAtLeastTwiceTest {

    private final LargestAtLeastTwice solution = new LargestAtLeastTwice();

    @Test
    void examples() {
        assertEquals(1, solution.dominantIndex(new int[]{3, 6, 1, 0}));
        assertEquals(-1, solution.dominantIndex(new int[]{1, 2, 3, 4}));
        assertEquals(0, solution.dominantIndex(new int[]{1, 0}));
    }
}
''',
trace=r'''
function run(a) {
  const s = a.map((v, i) => [v, i]).sort((x, y) => y[0] - x[0]), [b, bi] = s[0], sec = s[1][0];
  A.step(`The largest is ${b} at index ${bi}; the second largest is ${sec}.`, A.arr('nums', a, { hl: { [bi]: 'sel', [s[1][1]]: 'alt' } }));
  const ok = b >= 2 * sec;
  A.step(`${b} ${ok ? '≥' : '<'} 2 × ${sec} = ${2 * sec}. ${ok ? 'It dominates every other value.' : 'Not dominant.'}`, A.text('Result', ok ? bi : -1, ok ? 'ok' : 'bad'));
}
A.scenario('Dominant', 'nums = [3,6,1,0]', () => run([3, 6, 1, 0]));
A.scenario('Not dominant', 'nums = [1,2,3,4]', () => run([1, 2, 3, 4]));
'''),

P(num=771, slug="jewels-and-stones", title="Jewels and Stones", diff="Easy", topic="Arrays & Hashing", cls="JewelsAndStones",
idea="Mark the jewel letters in a lookup table, then count stones that are marked.",
vname="Lookup table",
spec=r'''
`jewels` lists the letter types that are jewels; `stones` lists your stones. Return how many of your stones are jewels (case-sensitive).

**Example**
```
jewels = "aA", stones = "aAAbbbb" → 3,   jewels = "z", stones = "ZZ" → 0
```

**Constraints**
* `1 <= jewels.length, stones.length <= 50`; letters only.
''',
approach=r'''
**Boolean table.** `isJewel[128]` marks each jewel letter; count stones with a mark.

* Time: **O(j + s)** — two passes.
* Space: **O(1)** — 128 flags.
''',
java=r'''
public class JewelsAndStones {

    public int numJewelsInStones(String jewels, String stones) {
        boolean[] isJewel = new boolean[128];
        for (char c : jewels.toCharArray()) isJewel[c] = true;
        int count = 0;
        for (char c : stones.toCharArray()) if (isJewel[c]) count++;
        return count;
    }
}
''',
test=r'''
class JewelsAndStonesTest {

    private final JewelsAndStones solution = new JewelsAndStones();

    @ParameterizedTest
    @CsvSource({"aA,aAAbbbb,3", "z,ZZ,0"})
    void counts(String j, String s, int expected) {
        assertEquals(expected, solution.numJewelsInStones(j, s));
    }
}
''',
trace=r'''
function run(j, s) {
  let count = 0;
  A.step(`Jewel types: ${[...j].join(', ')}.`, A.chars('jewels', j));
  [...s].forEach((c, i) => { const hit = j.includes(c); if (hit) count++; A.step(`'${c}' ${hit ? 'is a jewel' : 'is not a jewel'}. Count ${count}.`, A.chars('stones', s, { hl: { [i]: hit ? 'ok' : 'dim' } })); });
  A.step(`${count} jewels.`, A.text('Result', count, 'ok'));
}
A.scenario('Classic', 'jewels = "aA", stones = "aAAbbbb"', () => run('aA', 'aAAbbbb'));
'''),
]
