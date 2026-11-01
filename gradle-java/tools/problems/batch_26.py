PROBLEMS = [
P(num=1768, slug="merge-strings-alternately", title="Merge Strings Alternately", diff="Easy", topic="Two Pointers", cls="MergeStringsAlternately",
idea="Take one letter from each string in turn; append whatever is left of the longer one.",
vname="Alternating pointers",
spec=r'''
Merge `word1` and `word2` by alternating their letters, starting with `word1`. If one is longer, append its remaining letters.

**Example**
```
"abc", "pqr"  → "apbqcr"
"ab", "pqrs"  → "apbqrs"
```

**Constraints**
* `1 <= word1.length, word2.length <= 100`
''',
approach=r'''
**One loop.** For `i` from 0 to the longer length, append `word1[i]` and `word2[i]` when they exist.

* Time: **O(m + n)** — each letter once.
* Space: **O(m + n)** — the result.
''',
sc="n",
java=r'''
public class MergeStringsAlternately {

    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < Math.max(word1.length(), word2.length()); i++) {
            if (i < word1.length()) sb.append(word1.charAt(i));
            if (i < word2.length()) sb.append(word2.charAt(i));
        }
        return sb.toString();
    }
}
''',
test=r'''
class MergeStringsAlternatelyTest {

    private final MergeStringsAlternately solution = new MergeStringsAlternately();

    @ParameterizedTest
    @CsvSource({"abc,pqr,apbqcr", "ab,pqrs,apbqrs", "abcd,pq,apbqcd"})
    void merges(String a, String b, String expected) {
        assertEquals(expected, solution.mergeAlternately(a, b));
    }
}
''',
trace=r'''
function run(a, b) {
  let out = '';
  for (let i = 0; i < Math.max(a.length, b.length); i++) {
    if (i < a.length) out += a[i];
    if (i < b.length) out += b[i];
    A.step(`Position ${i}: take ${i < a.length ? `'${a[i]}'` : 'nothing'} from word1 and ${i < b.length ? `'${b[i]}'` : 'nothing'} from word2.`, A.chars('word1', a, { hl: { [i]: 'sel' } }), A.chars('word2', b, { hl: { [i]: 'alt' } }), A.chars('merged', out, { hl: { [out.length - 1]: 'ok' } }));
  }
  A.step(`Result: "${out}".`, A.text('Result', out, 'ok'));
}
A.scenario('Different lengths', 'word1 = "ab", word2 = "pqrs"', () => run('ab', 'pqrs'));
'''),

P(num=1071, slug="greatest-common-divisor-of-strings", title="Greatest Common Divisor of Strings", diff="Easy", topic="Math", cls="GcdOfStrings",
idea="A common divisor exists only if s + t == t + s; then its length is gcd(|s|, |t|).",
vname="Concatenation check + gcd",
spec=r'''
`t` divides `s` if `s` is `t` repeated some number of times. Return the largest string that divides both `str1` and `str2`, or `""`.

**Example**
```
"ABCABC", "ABC" → "ABC",   "ABABAB", "ABAB" → "AB",   "LEET", "CODE" → ""
```

**Constraints**
* `1 <= str1.length, str2.length <= 1000`; uppercase letters.
''',
approach=r'''
**Commuting strings.** If both are repetitions of some base `x`, then `str1 + str2` and `str2 + str1` are the same string; the converse
also holds. In that case the largest base has length `gcd(|str1|, |str2|)`.

* Time: **O(m + n)** — one concatenation comparison plus a gcd.
* Space: **O(m + n)** — the concatenations.
''',
sc="n",
java=r'''
public class GcdOfStrings {

    public String gcdOfStrings(String str1, String str2) {
        if (!(str1 + str2).equals(str2 + str1)) return "";
        return str1.substring(0, gcd(str1.length(), str2.length()));
    }

    private static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
''',
test=r'''
class GcdOfStringsTest {

    private final GcdOfStrings solution = new GcdOfStrings();

    @ParameterizedTest
    @CsvSource({"ABCABC,ABC,ABC", "ABABAB,ABAB,AB", "LEET,CODE,''"})
    void divides(String a, String b, String expected) {
        assertEquals(expected, solution.gcdOfStrings(a, b));
    }
}
''',
trace=r'''
function run(a, b) {
  const ok = a + b === b + a;
  A.step(`Compare str1 + str2 with str2 + str1. They are equal only if both strings repeat the same base.`, A.chars('str1 + str2', a + b, { hl: Object.fromEntries([...a].map((_, i) => [i, 'sel'])) }), A.chars('str2 + str1', b + a, { hl: Object.fromEntries([...b].map((_, i) => [i, 'alt'])) }));
  if (!ok) { A.step('They differ, so no common divisor exists.', A.text('Result', '""', 'bad')); return; }
  const gcd = (x, y) => (y ? gcd(y, x % y) : x), g = gcd(a.length, b.length);
  A.step(`They match. The base length is gcd(${a.length}, ${b.length}) = ${g}.`, A.chars('str1', a, { hl: Object.fromEntries([...Array(g)].map((_, i) => [i, 'ok'])) }), A.text('Result', a.slice(0, g), 'ok'));
}
A.scenario('Common base', 'str1 = "ABABAB", str2 = "ABAB"', () => run('ABABAB', 'ABAB'));
A.scenario('None', 'str1 = "LEET", str2 = "CODE"', () => run('LEET', 'CODE'));
'''),

P(num=1431, slug="kids-with-the-greatest-number-of-candies", title="Kids With the Greatest Number of Candies", diff="Easy", topic="Arrays & Hashing", cls="KidsWithCandies",
idea="A kid can become (tied) greatest exactly when candies + extra reaches the current maximum.",
vname="Compare with the maximum",
spec=r'''
For each kid, return whether giving them all `extraCandies` would make their count at least the largest count among all kids.

**Example**
```
candies = [2,3,5,1,3], extraCandies = 3 → [true,true,true,false,true]
```

**Constraints**
* `2 <= n <= 100`
''',
approach=r'''
**One maximum.** Compute `max`; kid `i` qualifies iff `candies[i] + extra >= max`.

* Time: **O(n)** — two passes.
* Space: **O(1)** — apart from the output.
''',
java=r'''
public class KidsWithCandies {

    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = 0;
        for (int c : candies) max = Math.max(max, c);
        List<Boolean> out = new ArrayList<>();
        for (int c : candies) out.add(c + extraCandies >= max);
        return out;
    }
}
''',
test=r'''
class KidsWithCandiesTest {

    private final KidsWithCandies solution = new KidsWithCandies();

    @Test
    void examples() {
        assertEquals(List.of(true, true, true, false, true), solution.kidsWithCandies(new int[]{2, 3, 5, 1, 3}, 3));
        assertEquals(List.of(true, false, false, false, false), solution.kidsWithCandies(new int[]{4, 2, 1, 1, 2}, 1));
    }
}
''',
trace=r'''
function run(c, extra) {
  const max = Math.max(...c);
  A.step(`The most candies any kid has is ${max}.`, A.arr('candies', c, { hl: { [c.indexOf(max)]: 'alt' } }));
  const out = c.map(x => x + extra >= max);
  c.forEach((x, i) => A.step(`Kid ${i}: ${x} + ${extra} = ${x + extra} ${x + extra >= max ? '≥' : '<'} ${max}.`, A.arr('candies', c, { hl: { [i]: out[i] ? 'ok' : 'bad' } }), A.arr('result', out.slice(0, i + 1).map(String))));
}
A.scenario('Classic', 'candies = [2,3,5,1,3], extra = 3', () => run([2, 3, 5, 1, 3], 3));
'''),

P(num=605, slug="can-place-flowers", title="Can Place Flowers", diff="Easy", topic="Greedy", cls="CanPlaceFlowers",
idea="Plant greedily in every empty plot whose neighbours are empty too.",
vname="Greedy left to right",
spec=r'''
A flowerbed is an array of `0` (empty) and `1` (planted); flowers may not be adjacent. Return `true` if `n` new flowers can be planted.

**Example**
```
flowerbed = [1,0,0,0,1], n = 1 → true
flowerbed = [1,0,0,0,1], n = 2 → false
```

**Constraints**
* `1 <= flowerbed.length <= 2 * 10^4`
''',
approach=r'''
**Greedy.** Scan left to right; plant in plot `i` when it and both neighbours (treating the ends as empty) are `0`. Planting as early as
possible never blocks a better arrangement.

* Time: **O(n)** — one pass.
* Space: **O(1)** — works on a copy only to avoid changing the input.
''',
sc="n",
java=r'''
public class CanPlaceFlowers {

    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int[] bed = flowerbed.clone();
        for (int i = 0; i < bed.length && n > 0; i++) {
            boolean leftEmpty = i == 0 || bed[i - 1] == 0;
            boolean rightEmpty = i == bed.length - 1 || bed[i + 1] == 0;
            if (bed[i] == 0 && leftEmpty && rightEmpty) {
                bed[i] = 1;
                n--;
            }
        }
        return n <= 0;
    }
}
''',
test=r'''
class CanPlaceFlowersTest {

    private final CanPlaceFlowers solution = new CanPlaceFlowers();

    @Test
    void examples() {
        assertTrue(solution.canPlaceFlowers(new int[]{1, 0, 0, 0, 1}, 1));
        assertFalse(solution.canPlaceFlowers(new int[]{1, 0, 0, 0, 1}, 2));
        assertTrue(solution.canPlaceFlowers(new int[]{0, 0, 1, 0, 0}, 2));
        assertTrue(solution.canPlaceFlowers(new int[]{0}, 1));
    }
}
''',
trace=r'''
function run(bed0, n) {
  const bed = bed0.slice(); let left = n;
  A.step(`Plant ${n} flower${n > 1 ? 's' : ''} wherever a plot and both neighbours are empty.`, A.arr('flowerbed', bed));
  for (let i = 0; i < bed.length && left > 0; i++) {
    const ok = bed[i] === 0 && (i === 0 || bed[i - 1] === 0) && (i === bed.length - 1 || bed[i + 1] === 0);
    if (ok) { bed[i] = 1; left--; }
    A.step(ok ? `Plot ${i} and its neighbours are empty: plant here. ${left} left to plant.` : `Plot ${i}: ${bed[i] ? 'already planted' : 'a neighbour is planted'}.`, A.arr('flowerbed', bed, { hl: { [i]: ok ? 'ok' : 'dim' } }));
  }
  A.step(left <= 0 ? 'All flowers fit.' : `${left} flower${left > 1 ? 's' : ''} could not be placed.`, A.text('Result', String(left <= 0), left <= 0 ? 'ok' : 'bad'));
}
A.scenario('Two flowers', 'flowerbed = [0,0,1,0,0], n = 2', () => run([0, 0, 1, 0, 0], 2));
'''),

P(num=345, slug="reverse-vowels-of-a-string", title="Reverse Vowels of a String", diff="Easy", topic="Two Pointers", cls="ReverseVowels",
idea="Two pointers move inward, skipping consonants, and swap each pair of vowels they stop on.",
vname="Two pointers",
spec=r'''
Reverse only the vowels (`a, e, i, o, u` in either case) of `s`.

**Example**
```
"IceCreAm" → "AceCreIm",   "leetcode" → "leotcede"
```

**Constraints**
* `1 <= s.length <= 3 * 10^5`; printable ASCII.
''',
approach=r'''
**Swap vowels from both ends.** Move `l` right and `r` left until each points at a vowel, swap, repeat.

* Time: **O(n)** — each character is visited once.
* Space: **O(n)** — the character array.
''',
sc="n",
java=r'''
public class ReverseVowels {

    private static boolean vowel(char c) {
        return "aeiouAEIOU".indexOf(c) >= 0;
    }

    public String reverseVowels(String s) {
        char[] a = s.toCharArray();
        for (int l = 0, r = a.length - 1; l < r; ) {
            if (!vowel(a[l])) l++;
            else if (!vowel(a[r])) r--;
            else {
                char t = a[l];
                a[l++] = a[r];
                a[r--] = t;
            }
        }
        return new String(a);
    }
}
''',
test=r'''
class ReverseVowelsTest {

    private final ReverseVowels solution = new ReverseVowels();

    @ParameterizedTest
    @CsvSource({"IceCreAm,AceCreIm", "leetcode,leotcede", "xyz,xyz"})
    void reverses(String s, String expected) {
        assertEquals(expected, solution.reverseVowels(s));
    }
}
''',
trace=r'''
function run(s) {
  const a = [...s], v = c => 'aeiouAEIOU'.includes(c);
  for (let l = 0, r = a.length - 1; l < r;) {
    if (!v(a[l])) { l++; continue; } if (!v(a[r])) { r--; continue; }
    [a[l], a[r]] = [a[r], a[l]];
    A.step(`Swap the vowels at ${l} and ${r}.`, A.chars('s', a.join(''), { ptr: [[l, 'l'], [r, 'r']], hl: { [l]: 'ok', [r]: 'ok' } }));
    l++; r--;
  }
  A.step(`Result: "${a.join('')}".`, A.text('Result', a.join(''), 'ok'));
}
A.scenario('leetcode', 's = "leetcode"', () => run('leetcode'));
'''),

P(num=334, slug="increasing-triplet-subsequence", title="Increasing Triplet Subsequence", diff="Medium", topic="Greedy", cls="IncreasingTriplet",
idea="Keep the smallest possible first and second values; any number above both completes a triplet.",
vname="Two smallest tails",
spec=r'''
Return `true` if there are indices `i < j < k` with `nums[i] < nums[j] < nums[k]`.

**Example**
```
[1,2,3,4,5] → true,   [5,4,3,2,1] → false,   [2,1,5,0,4,6] → true
```

**Constraints**
* `1 <= nums.length <= 5 * 10^5`

**Follow-up:** O(n) time, O(1) space.
''',
approach=r'''
**Greedy tails.** `first` is the smallest value seen; `second` the smallest value that has a smaller value before it. A number larger than
`second` closes a triplet. Lowering `first` later is safe: `second` still has some smaller value before it.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two numbers.
''',
java=r'''
public class IncreasingTriplet {

    public boolean increasingTriplet(int[] nums) {
        int first = Integer.MAX_VALUE, second = Integer.MAX_VALUE;
        for (int x : nums) {
            if (x <= first) first = x;
            else if (x <= second) second = x;
            else return true;
        }
        return false;
    }
}
''',
test=r'''
class IncreasingTripletTest {

    private final IncreasingTriplet solution = new IncreasingTriplet();

    @Test
    void examples() {
        assertTrue(solution.increasingTriplet(new int[]{1, 2, 3, 4, 5}));
        assertFalse(solution.increasingTriplet(new int[]{5, 4, 3, 2, 1}));
        assertTrue(solution.increasingTriplet(new int[]{2, 1, 5, 0, 4, 6}));
    }
}
''',
trace=r'''
function run(a) {
  let f = Infinity, s = Infinity; const fm = x => (x === Infinity ? '∞' : x);
  A.step('first: smallest value so far. second: smallest value that has something smaller before it.', A.arr('nums', a), A.vars({ first: '∞', second: '∞' }));
  for (let i = 0; i < a.length; i++) {
    const x = a[i];
    if (x <= f) { f = x; A.step(`${x} is a new smallest first value.`, A.arr('nums', a, { hl: { [i]: 'sel' } }), A.vars({ first: fm(f), second: fm(s) })); }
    else if (x <= s) { s = x; A.step(`${x} is larger than first but a better (smaller) second value.`, A.arr('nums', a, { hl: { [i]: 'alt' } }), A.vars({ first: fm(f), second: fm(s) })); }
    else { A.step(`${x} is larger than second (${s}), which is larger than a value before it: a triplet exists.`, A.arr('nums', a, { hl: { [i]: 'ok' } }), A.text('Result', 'true', 'ok')); return; }
  }
  A.step('No triplet.', A.text('Result', 'false', 'bad'));
}
A.scenario('Tricky order', 'nums = [2,1,5,0,4,6]', () => run([2, 1, 5, 0, 4, 6]));
'''),

P(num=443, slug="string-compression", title="String Compression", diff="Medium", topic="Two Pointers", cls="StringCompression",
idea="Read each run of equal characters and write the character plus its count (if > 1) back into the same array.",
vname="Read/write pointers",
spec=r'''
Compress `chars` in place: each run of a repeated character becomes the character followed by the run length (if the length is more than
1, written digit by digit). Return the new length.

**Example**
```
["a","a","b","b","c","c","c"] → 6, chars = ["a","2","b","2","c","3"]
["a"]                          → 1
["a","b","b","b","b","b","b","b","b","b","b","b","b"] → 4 ("a","b","1","2")
```

**Constraints**
* `1 <= chars.length <= 2000`
''',
approach=r'''
**Two pointers.** `read` finds the end of each run; `write` writes the character and, if the run is longer than 1, its digits. Writing
never overtakes reading, because a run's encoding is never longer than the run.

* Time: **O(n)** — each character is read once.
* Space: **O(1)** — in place.
''',
java=r'''
public class StringCompression {

    public int compress(char[] chars) {
        int write = 0;
        for (int read = 0; read < chars.length; ) {
            char c = chars[read];
            int start = read;
            while (read < chars.length && chars[read] == c) read++;
            chars[write++] = c;
            if (read - start > 1) {
                for (char d : String.valueOf(read - start).toCharArray()) chars[write++] = d;
            }
        }
        return write;
    }
}
''',
test=r'''
class StringCompressionTest {

    private final StringCompression solution = new StringCompression();

    private String run(String s) {
        char[] c = s.toCharArray();
        return new String(c, 0, solution.compress(c));
    }

    @Test
    void examples() {
        assertEquals("a2b2c3", run("aabbccc"));
        assertEquals("a", run("a"));
        assertEquals("ab12", run("abbbbbbbbbbbb"));
    }
}
''',
trace=r'''
function run(s) {
  const a = [...s]; let w = 0;
  for (let r = 0; r < a.length;) {
    const c = a[r], st = r; while (r < a.length && a[r] === c) r++;
    a[w++] = c; if (r - st > 1) for (const d of String(r - st)) a[w++] = d;
    A.step(`A run of ${r - st} '${c}': write "${c}${r - st > 1 ? r - st : ''}".`, A.arr('chars', a, { ptr: [[Math.min(w, a.length - 1), 'write'], [Math.min(r, a.length - 1), 'read']], hl: Object.fromEntries([...Array(w)].map((_, t) => [t, 'ok'])) }));
  }
  A.step(`New length: ${w} ("${a.slice(0, w).join('')}").`, A.text('Result', w, 'ok'));
}
A.scenario('Three runs', 'chars = aabbccc', () => run('aabbccc'));
'''),

P(num=1679, slug="max-number-of-k-sum-pairs", title="Max Number of K-Sum Pairs", diff="Medium", topic="Arrays & Hashing", cls="MaxKSumPairs",
idea="For each number, if its partner k − x is waiting in the hash map, pair them; otherwise wait.",
vname="Hash map of waiting numbers",
spec=r'''
In one operation, remove two numbers whose sum is `k`. Return the maximum number of operations.

**Example**
```
nums = [1,2,3,4], k = 5   → 2
nums = [3,1,3,4,3], k = 6 → 1
```

**Constraints**
* `1 <= nums.length <= 10^5`
''',
approach=r'''
**Waiting counts.** Keep counts of unpaired numbers in a `MyHashMap`. For each `x`, if `k - x` is waiting, pair them (decrement); otherwise
add `x` to the waiting counts.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the map.
''',
java=r'''
public class MaxKSumPairs {

    public int maxOperations(int[] nums, int k) {
        MyHashMap<Integer, Integer> waiting = new MyHashMap<>();
        int ops = 0;
        for (int x : nums) {
            int partner = waiting.getOrDefault(k - x, 0);
            if (partner > 0) {
                waiting.put(k - x, partner - 1);
                ops++;
            } else {
                waiting.merge(x, 1, Integer::sum);
            }
        }
        return ops;
    }
}
''',
test=r'''
class MaxKSumPairsTest {

    private final MaxKSumPairs solution = new MaxKSumPairs();

    @Test
    void examples() {
        assertEquals(2, solution.maxOperations(new int[]{1, 2, 3, 4}, 5));
        assertEquals(1, solution.maxOperations(new int[]{3, 1, 3, 4, 3}, 6));
    }
}
''',
trace=r'''
function run(a, k) {
  const w = new Map(); let ops = 0;
  a.forEach((x, i) => {
    const p = w.get(k - x) || 0;
    if (p) { w.set(k - x, p - 1); ops++; A.step(`${x} pairs with a waiting ${k - x}. Operations: ${ops}.`, A.arr('nums', a, { hl: { [i]: 'ok' } }), A.hashTable('waiting', w, { hl: k - x })); }
    else { w.set(x, (w.get(x) || 0) + 1); A.step(`${x} has no partner yet. It waits.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.hashTable('waiting', w, { hl: x })); }
  });
  A.step(`${ops} operations.`, A.text('Result', ops, 'ok'));
}
A.scenario('k = 6', 'nums = [3,1,3,4,3]', () => run([3, 1, 3, 4, 3], 6));
'''),

P(num=643, slug="maximum-average-subarray-i", title="Maximum Average Subarray I", diff="Easy", topic="Sliding Window", cls="MaximumAverageSubarray",
idea="Slide a window of size k, adding the new element and dropping the old one.",
vname="Fixed sliding window",
spec=r'''
Find the contiguous subarray of length `k` with the maximum average and return that average.

**Example**
```
nums = [1,12,-5,-6,50,3], k = 4 → 12.75
```

**Constraints**
* `1 <= k <= n <= 10^5`
''',
approach=r'''
**Rolling sum.** Sum the first `k` values, then for each step add `nums[i]` and subtract `nums[i - k]`; keep the largest sum.

* Time: **O(n)** — one pass.
* Space: **O(1)** — a running sum.
''',
java=r'''
public class MaximumAverageSubarray {

    public double findMaxAverage(int[] nums, int k) {
        long sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        long best = sum;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            best = Math.max(best, sum);
        }
        return (double) best / k;
    }
}
''',
test=r'''
class MaximumAverageSubarrayTest {

    private final MaximumAverageSubarray solution = new MaximumAverageSubarray();

    @Test
    void examples() {
        assertEquals(12.75, solution.findMaxAverage(new int[]{1, 12, -5, -6, 50, 3}, 4), 1e-9);
        assertEquals(5.0, solution.findMaxAverage(new int[]{5}, 1), 1e-9);
    }
}
''',
trace=r'''
function run(a, k) {
  let sum = a.slice(0, k).reduce((s, x) => s + x, 0), best = sum, bi = 0;
  A.step(`The first window of ${k} sums to ${sum}.`, A.arr('nums', a, { range: [0, k - 1] }), A.vars({ sum, best }));
  for (let i = k; i < a.length; i++) {
    sum += a[i] - a[i - k]; if (sum > best) { best = sum; bi = i - k + 1; }
    A.step(`Slide: add ${a[i]}, drop ${a[i - k]}. Sum ${sum}.`, A.arr('nums', a, { range: [i - k + 1, i], hl: { [i]: 'ok', [i - k]: 'bad' } }), A.vars({ sum, best }));
  }
  A.step(`Best window sum ${best}, average ${best / k}.`, A.arr('nums', a, { range: [bi, bi + k - 1] }), A.text('Result', best / k, 'ok'));
}
A.scenario('Classic', 'nums = [1,12,-5,-6,50,3], k = 4', () => run([1, 12, -5, -6, 50, 3], 4));
'''),

P(num=1456, slug="maximum-number-of-vowels-in-a-substring-of-given-length", title="Maximum Number of Vowels in a Substring of Given Length", diff="Medium", topic="Sliding Window", cls="MaxVowels",
idea="Slide a window of size k, counting vowels that enter and leave.",
vname="Fixed sliding window",
spec=r'''
Return the maximum number of vowels in any substring of `s` with length `k`.

**Example**
```
s = "abciiidef", k = 3 → 3,   s = "aeiou", k = 2 → 2,   s = "leetcode", k = 3 → 2
```

**Constraints**
* `1 <= k <= s.length <= 10^5`
''',
approach=r'''
**Rolling count.** Add 1 when a vowel enters the window, subtract 1 when one leaves; track the maximum.

* Time: **O(n)** — one pass.
* Space: **O(1)** — a counter.
''',
java=r'''
public class MaxVowels {

    private static int v(char c) {
        return "aeiou".indexOf(c) >= 0 ? 1 : 0;
    }

    public int maxVowels(String s, int k) {
        int count = 0, best = 0;
        for (int i = 0; i < s.length(); i++) {
            count += v(s.charAt(i));
            if (i >= k) count -= v(s.charAt(i - k));
            best = Math.max(best, count);
        }
        return best;
    }
}
''',
test=r'''
class MaxVowelsTest {

    private final MaxVowels solution = new MaxVowels();

    @ParameterizedTest
    @CsvSource({"abciiidef,3,3", "aeiou,2,2", "leetcode,3,2", "rhythms,4,0"})
    void counts(String s, int k, int expected) {
        assertEquals(expected, solution.maxVowels(s, k));
    }
}
''',
trace=r'''
function run(s, k) {
  const v = c => 'aeiou'.includes(c); let cnt = 0, best = 0;
  for (let i = 0; i < s.length; i++) {
    cnt += v(s[i]); if (i >= k) cnt -= v(s[i - k]); best = Math.max(best, cnt);
    A.step(`Window ending at ${i}: ${cnt} vowel${cnt === 1 ? '' : 's'}. Best ${best}.`, A.chars('s', s, { range: [Math.max(0, i - k + 1), i], hl: Object.fromEntries([...s].map((c, t) => [t, t >= i - k + 1 && t <= i && v(c) ? 'ok' : ''])) }), A.vars({ count: cnt, best }));
  }
  A.step(`Maximum: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('k = 3', 's = "abciiidef"', () => run('abciiidef', 3));
'''),
]
