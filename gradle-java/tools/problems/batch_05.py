PROBLEMS = [
P(num=290, slug="word-pattern", title="Word Pattern", diff="Easy", topic="Hashmap", cls="WordPattern",
idea="Each pattern letter must map to exactly one word and each word to exactly one letter.",
vname="Two-way mapping",
spec=r'''
Given a `pattern` of letters and a string `s` of space-separated words, return `true` if `s` **follows** the pattern: there is a
one-to-one correspondence between pattern letters and words.

**Example 1**
```
Input:  pattern = "abba", s = "dog cat cat dog"
Output: true
```

**Example 2**
```
Input:  pattern = "abba", s = "dog cat cat fish"
Output: false
```

**Example 3**
```
Input:  pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

**Constraints**
* `1 <= pattern.length <= 300`; `1 <= s.length <= 3000`; words are lowercase and separated by single spaces.
''',
approach=r'''
**Bijection check.** Split `s` into words; if the counts differ, return `false`. Walk both together with two maps
(letter → word and word → letter); any conflict means the pattern is not followed.

* Time: **O(n)** — n is the length of s; each word is hashed once.
* Space: **O(n)** — the maps hold the distinct words.
''',
java=r'''
public class WordPattern {

    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if (words.length != pattern.length()) return false;
        MyHashMap<Character, String> letterToWord = new MyHashMap<>();
        MyHashMap<String, Character> wordToLetter = new MyHashMap<>();
        for (int i = 0; i < words.length; i++) {
            char c = pattern.charAt(i);
            String w = words[i];
            String mapped = letterToWord.putIfAbsent(c, w);
            Character back = wordToLetter.putIfAbsent(w, c);
            if ((mapped != null && !mapped.equals(w)) || (back != null && back != c)) return false;
        }
        return true;
    }
}
''',
test=r'''
class WordPatternTest {

    private final WordPattern solution = new WordPattern();

    @ParameterizedTest
    @CsvSource({"abba,dog cat cat dog,true", "abba,dog cat cat fish,false", "aaaa,dog cat cat dog,false", "abba,dog dog dog dog,false", "ab,dog,false"})
    void checks(String pattern, String s, boolean expected) {
        assertEquals(expected, solution.wordPattern(pattern, s));
    }
}
''',
trace=r'''
function run(p, s) {
  const w = s.split(' '), pw = new Map(), wp = new Map();
  A.step(`Split s into ${w.length} words and pair them with the ${p.length} pattern letters.`, A.chars('pattern', p), A.arr('words', w));
  if (w.length !== p.length) { A.step('The counts differ, so the pattern cannot match.', A.text('Result', 'false', 'bad')); return; }
  for (let i = 0; i < w.length; i++) {
    const c = p[i];
    if ((pw.has(c) && pw.get(c) !== w[i]) || (wp.has(w[i]) && wp.get(w[i]) !== c)) {
      A.step(pw.has(c) && pw.get(c) !== w[i] ? `'${c}' already means "${pw.get(c)}", not "${w[i]}". The pattern is not followed.` : `"${w[i]}" already belongs to '${wp.get(w[i])}', so '${c}' cannot use it. The pattern is not followed.`, A.chars('pattern', p, { hl: { [i]: 'bad' } }), A.arr('words', w, { hl: { [i]: 'bad' } }), A.hashTable('letter → word', pw), A.hashTable('word → letter', wp), A.text('Result', 'false', 'bad'));
      return;
    }
    pw.set(c, w[i]); wp.set(w[i], c);
    A.step(`'${c}' ↔ "${w[i]}" is consistent.`, A.chars('pattern', p, { hl: { [i]: 'ok' } }), A.arr('words', w, { hl: { [i]: 'ok' } }), A.hashTable('letter → word', pw), A.hashTable('word → letter', wp));
  }
  A.step('Every pair was consistent in both directions, so the answer is true.', A.text('Result', 'true', 'ok'));
}
A.scenario('Follows the pattern', 'pattern = "abba", s = "dog cat cat dog"', () => run('abba', 'dog cat cat dog'));
A.scenario('Word reused for two letters', 'pattern = "abba", s = "dog dog dog dog"', () => run('abba', 'dog dog dog dog'));
'''),

P(num=242, slug="valid-anagram", title="Valid Anagram", diff="Easy", topic="Hashmap", cls="ValidAnagram",
idea="Two strings are anagrams exactly when every letter appears the same number of times in both.",
vname="Letter counts",
spec=r'''
Return `true` if `t` is an **anagram** of `s`: it uses exactly the same letters, the same number of times, in any order.

**Example 1**
```
Input:  s = "anagram", t = "nagaram"
Output: true
```

**Example 2**
```
Input:  s = "rat", t = "car"
Output: false
```

**Constraints**
* `1 <= s.length, t.length <= 5 * 10^4`; lowercase letters.

**Follow-up:** what if the inputs contain Unicode characters? (Use a hash map instead of a fixed array.)
''',
approach=r'''
**Counting.** Add 1 for each letter of `s`, subtract 1 for each letter of `t`. All 26 counters end at zero exactly for anagrams.

* Time: **O(n)** — one pass over each string.
* Space: **O(1)** — 26 counters.
''',
java=r'''
public class ValidAnagram {

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        for (int c : count) {
            if (c != 0) return false;
        }
        return true;
    }
}
''',
test=r'''
class ValidAnagramTest {

    private final ValidAnagram solution = new ValidAnagram();

    @ParameterizedTest
    @CsvSource({"anagram,nagaram,true", "rat,car,false", "a,ab,false", "listen,silent,true"})
    void checks(String s, String t, boolean expected) {
        assertEquals(expected, solution.isAnagram(s, t));
    }
}
''',
trace=r'''
function run(s, t) {
  const cnt = new Map();
  A.step('Add one for each letter of s, subtract one for each letter of t.', A.chars('s', s), A.chars('t', t), A.map('count', cnt));
  for (let i = 0; i < Math.max(s.length, t.length); i++) {
    if (i < s.length) cnt.set(s[i], (cnt.get(s[i]) || 0) + 1);
    if (i < t.length) cnt.set(t[i], (cnt.get(t[i]) || 0) - 1);
    A.step(`+1 for '${s[i] ?? '-'}', −1 for '${t[i] ?? '-'}'.`, A.chars('s', s, { hl: { [i]: 'cur' } }), A.chars('t', t, { hl: { [i]: 'cur' } }), A.map('count', cnt));
  }
  const bad = [...cnt].filter(([, v]) => v !== 0);
  A.step(bad.length ? `'${bad[0][0]}' has count ${bad[0][1]}, not zero, so these are not anagrams.` : 'Every count is zero, so these are anagrams.', A.map('count', cnt), A.text('Result', String(!bad.length), bad.length ? 'bad' : 'ok'));
}
A.scenario('Anagrams', 's = "anagram", t = "nagaram"', () => run('anagram', 'nagaram'));
A.scenario('Not anagrams', 's = "rat", t = "car"', () => run('rat', 'car'));
''',
variants=[dict(
name="Sort both strings",
idea="Anagrams become identical strings once their letters are sorted.",
approach=r'''
**Sort and compare.** Sort the characters of both strings and compare the arrays.

* Time: **O(n log n)** — sorting.
* Space: **O(n)** — the character arrays.
''',
tc="nlogn",
java=r'''
public class ValidAnagram {

    public boolean isAnagram(String s, String t) {
        char[] a = s.toCharArray(), b = t.toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);
        return Arrays.equals(a, b);
    }
}
''',
trace=r'''
function run(s, t) {
  const a = [...s].sort(), b = [...t].sort();
  A.step('Sort the letters of both strings.', A.chars('s', s), A.chars('t', t));
  A.step('Compare the sorted letters position by position.', A.arr('sorted s', a, { hl: a.map((c, i) => [i, c === b[i] ? 'ok' : 'bad']) }), A.arr('sorted t', b, { hl: b.map((c, i) => [i, c === a[i] ? 'ok' : 'bad']) }));
  const eq = a.join('') === b.join('');
  A.step(eq ? 'They are identical, so these are anagrams.' : 'They differ, so these are not anagrams.', A.text('Result', String(eq), eq ? 'ok' : 'bad'));
}
A.scenario('Anagrams', 's = "anagram", t = "nagaram"', () => run('anagram', 'nagaram'));
A.scenario('Not anagrams', 's = "rat", t = "car"', () => run('rat', 'car'));
''')]),

P(num=49, slug="group-anagrams", title="Group Anagrams", diff="Medium", topic="Hashmap", cls="GroupAnagrams",
idea="Give every word a key that is identical for all its anagrams, and group words by key.",
vname="Letter-count key",
spec=r'''
Group the strings in `strs` so that anagrams are together. Return the groups in any order.

**Example 1**
```
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2**
```
Input:  strs = [""]
Output: [[""]]
```

**Constraints**
* `1 <= strs.length <= 10^4`, `0 <= strs[i].length <= 100`; lowercase letters.
''',
approach=r'''
**Count signature.** Build a key from the 26 letter counts (e.g. `"1#0#0#...#1"`). Anagrams share the same counts, so they share a key.
Collect words in a `Map<String, List<String>>`.

* Time: **O(n·k)** — n words of length up to k; each key takes O(k + 26).
* Space: **O(n·k)** — the map stores every word.
''',
tc="n", sc="n",
java=r'''
public class GroupAnagrams {

    public List<List<String>> groupAnagrams(String[] strs) {
        MyHashMap<String, List<String>> groups = new MyHashMap<>();
        for (String s : strs) {
            int[] count = new int[26];
            for (char c : s.toCharArray()) count[c - 'a']++;
            groups.computeIfAbsent(Arrays.toString(count), k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(groups.values());
    }
}
''',
test=r'''
class GroupAnagramsTest {

    private final GroupAnagrams solution = new GroupAnagrams();

    private static Set<Set<String>> normalize(List<List<String>> groups) {
        Set<Set<String>> out = new HashSet<>();
        for (List<String> g : groups) out.add(new HashSet<>(g));
        return out;
    }

    @Test
    void example1() {
        assertEquals(Set.of(Set.of("bat"), Set.of("nat", "tan"), Set.of("ate", "eat", "tea")),
                normalize(solution.groupAnagrams(new String[]{"eat", "tea", "tan", "ate", "nat", "bat"})));
    }

    @Test
    void emptyString() {
        assertEquals(List.of(List.of("")), solution.groupAnagrams(new String[]{""}));
    }

    @Test
    void single() {
        assertEquals(List.of(List.of("a")), solution.groupAnagrams(new String[]{"a"}));
    }
}
''',
trace=r'''
function run(strs) {
  const g = new Map();
  A.step('Give every word a key made from its letter counts. Anagrams share the same key.', A.arr('strs', strs), A.hashTable('groups', g));
  strs.forEach((s, i) => {
    const cnt = {}; for (const c of s) cnt[c] = (cnt[c] || 0) + 1;
    const key = Object.keys(cnt).sort().map(c => c + cnt[c]).join('') || '∅';
    const isNew = !g.has(key);
    if (isNew) g.set(key, []);
    g.get(key).push(s);
    A.step(`"${s}" has counts ${key}. ${isNew ? 'That is a new group.' : `It joins [${g.get(key).slice(0, -1).join(', ')}].`}`, A.arr('strs', strs, { hl: { [i]: 'cur' } }), A.hashTable('groups', g));
  });
  A.step(`${g.size} groups.`, A.arr('result', [...g.values()].map(x => `[${x.join(',')}]`), { hl: [...g.keys()].map((_, i) => [i, 'ok']) }));
}
A.scenario('Classic', 'strs = ["eat","tea","tan","ate","nat","bat"]', () => run(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']));
''',
variants=[dict(
name="Sorted-word key",
idea="Sorting a word's letters gives the same key for all of its anagrams.",
approach=r'''
**Sort each word.** The key is the word with its letters sorted, e.g. `"eat" → "aet"`.

* Time: **O(n·k log k)** — sorting each of n words of length k.
* Space: **O(n·k)** — the map stores every word.
''',
tc="nlogn", sc="n",
java=r'''
public class GroupAnagrams {

    public List<List<String>> groupAnagrams(String[] strs) {
        MyHashMap<String, List<String>> groups = new MyHashMap<>();
        for (String s : strs) {
            char[] key = s.toCharArray();
            Arrays.sort(key);
            groups.computeIfAbsent(new String(key), k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(groups.values());
    }
}
''',
trace=r'''
function run(strs) {
  const g = new Map();
  strs.forEach((s, i) => {
    const key = [...s].sort().join('');
    if (!g.has(key)) g.set(key, []);
    g.get(key).push(s);
    A.step(`Sort "${s}" to get the key "${key}".`, A.arr('strs', strs, { hl: { [i]: 'cur' } }), A.hashTable('groups', g));
  });
  A.step(`${g.size} groups.`, A.arr('result', [...g.values()].map(x => `[${x.join(',')}]`)));
}
A.scenario('Classic', 'strs = ["eat","tea","tan","ate","nat","bat"]', () => run(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']));
''')]),

P(num=1, slug="two-sum", title="Two Sum", diff="Easy", topic="Hashmap", cls="TwoSum",
idea="As you scan, look up target − x among the values already seen; a hash map makes that lookup O(1).",
vname="One-pass hash map",
spec=r'''
Given an integer array `nums` and an integer `target`, return the indices of the two numbers that add up to `target`.
Exactly one solution exists, and you may not use the same element twice. Return the indices in any order.

**Example 1**
```
Input:  nums = [2,7,11,15], target = 9
Output: [0,1]
```

**Example 2**
```
Input:  nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3**
```
Input:  nums = [3,3], target = 6
Output: [0,1]
```

**Constraints**
* `2 <= nums.length <= 10^4`; `-10^9 <= nums[i], target <= 10^9`

**Follow-up:** better than O(n²)?
''',
approach=r'''
**Hash map of seen values.** For each `nums[i]`, check whether `target - nums[i]` was seen earlier; if so, return both indices.
Otherwise store `nums[i] → i`.

* Time: **O(n)** — one pass with O(1) average lookups.
* Space: **O(n)** — the map.
''',
java=r'''
public class TwoSum {

    public int[] twoSum(int[] nums, int target) {
        MyHashMap<Integer, Integer> seen = new MyHashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer j = seen.get(target - nums[i]);
            if (j != null) {
                return new int[]{j, i};
            }
            seen.put(nums[i], i);
        }
        throw new IllegalArgumentException("No solution");
    }
}
''',
test=r'''
class TwoSumTest {

    private final TwoSum solution = new TwoSum();

    @Test
    void example1() {
        assertArrayEquals(new int[]{0, 1}, solution.twoSum(new int[]{2, 7, 11, 15}, 9));
    }

    @Test
    void example2() {
        assertArrayEquals(new int[]{1, 2}, solution.twoSum(new int[]{3, 2, 4}, 6));
    }

    @Test
    void duplicates() {
        assertArrayEquals(new int[]{0, 1}, solution.twoSum(new int[]{3, 3}, 6));
    }
}
''',
trace=r'''
function run(a, target) {
  const seen = new Map();
  A.step(`For each value, the partner we need is ${target} minus it. Check whether we have already seen that partner.`, A.arr('nums', a), A.hashTable('seen (value → index)', seen));
  for (let i = 0; i < a.length; i++) {
    const need = target - a[i];
    if (seen.has(need)) { A.step(`We need ${need}, and it was seen at index ${seen.get(need)}. Answer: [${seen.get(need)}, ${i}].`, A.arr('nums', a, { hl: { [seen.get(need)]: 'ok', [i]: 'ok' } }), A.hashTable('seen (value → index)', seen, { hl: need }), A.text('Result', `[${seen.get(need)}, ${i}]`, 'ok')); return; }
    seen.set(a[i], i);
    A.step(`${a[i]} needs ${need}, which we have not seen yet. Remember ${a[i]} at index ${i}.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.hashTable('seen (value → index)', seen, { hl: a[i] }), A.vars({ target, need }));
  }
}
A.scenario('Partner appears later', 'nums = [3,2,4], target = 6', () => run([3, 2, 4], 6));
A.scenario('Classic', 'nums = [2,7,11,15], target = 9', () => run([2, 7, 11, 15], 9));
A.scenario('Edge: equal values', 'nums = [3,3], target = 6', () => run([3, 3], 6));
''',
variants=[dict(
name="Brute force",
idea="Check every pair of indices.",
approach=r'''
**All pairs.** Try every `i < j` until `nums[i] + nums[j] == target`.

* Time: **O(n²)** — about n²/2 pairs.
* Space: **O(1)** — no extra structures.
''',
java=r'''
public class TwoSum {

    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        throw new IllegalArgumentException("No solution");
    }
}
''',
trace=r'''
function run(a, target) {
  let checks = 0;
  for (let i = 0; i < a.length; i++) for (let j = i + 1; j < a.length; j++) {
    checks++;
    const hit = a[i] + a[j] === target;
    A.step(`${a[i]} + ${a[j]} = ${a[i] + a[j]}${hit ? ` = ${target}. Found it.` : '.'}`, A.arr('nums', a, { ptr: [[i, 'i'], [j, 'j']], hl: { [i]: hit ? 'ok' : 'cur', [j]: hit ? 'ok' : 'cur' } }), A.vars({ target, pairsChecked: checks }));
    if (hit) { A.step(`Answer [${i}, ${j}] after ${checks} checks. The worst case checks every pair.`, A.text('Result', `[${i}, ${j}]`, 'ok')); return; }
  }
}
A.scenario('Partner appears late', 'nums = [1,5,3,8,4], target = 12', () => run([1, 5, 3, 8, 4], 12));
''')]),

P(num=202, slug="happy-number", title="Happy Number", diff="Easy", topic="Hashmap", cls="HappyNumber",
idea="The digit-square sequence either reaches 1 or falls into a cycle; detect the cycle with fast and slow pointers.",
vname="Floyd cycle detection",
spec=r'''
A number is **happy** if repeatedly replacing it with the sum of the squares of its digits eventually reaches `1`. Numbers that
never reach 1 loop forever in a cycle. Return `true` if `n` is happy.

**Example 1**
```
Input:  n = 19
Output: true   (1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1)
```

**Example 2**
```
Input:  n = 2
Output: false
```

**Constraints**
* `1 <= n <= 2^31 - 1`
''',
approach=r'''
**Fast and slow pointers.** Treat `next(x)` = sum of squared digits as a linked list. `slow` moves one step, `fast` two. If they meet
at 1 the number is happy; if they meet elsewhere, there is a cycle without 1.

* Time: **O(log n)** — the values quickly drop below a few hundred, and each step costs O(number of digits).
* Space: **O(1)** — two numbers.
''',
tc="log",
java=r'''
public class HappyNumber {

    private static int next(int x) {
        int sum = 0;
        while (x > 0) {
            int d = x % 10;
            sum += d * d;
            x /= 10;
        }
        return sum;
    }

    public boolean isHappy(int n) {
        int slow = n, fast = next(n);
        while (fast != 1 && slow != fast) {
            slow = next(slow);
            fast = next(next(fast));
        }
        return fast == 1;
    }
}
''',
test=r'''
class HappyNumberTest {

    private final HappyNumber solution = new HappyNumber();

    @ParameterizedTest
    @CsvSource({"19,true", "2,false", "1,true", "7,true", "4,false"})
    void checks(int n, boolean expected) {
        assertEquals(expected, solution.isHappy(n));
    }
}
''',
trace=r'''
const nx = x => String(x).split('').reduce((s, d) => s + d * d, 0);
function run(n) {
  let slow = n, fast = nx(n);
  const seq = [n]; let x = n; for (let i = 0; i < 12 && x !== 1; i++) { x = nx(x); seq.push(x); }
  A.step('Each number leads to the sum of the squares of its digits. Run a slow pointer, one step at a time, and a fast pointer, two steps at a time.', A.arr('sequence', seq), A.vars({ slow, fast }));
  let k = 0;
  while (fast !== 1 && slow !== fast && k++ < 20) {
    slow = nx(slow); fast = nx(nx(fast));
    A.step(`slow moves to ${slow}; fast moves to ${fast}.`, A.arr('sequence', seq, { hl: seq.map((v, i) => [i, v === fast ? 'alt' : v === slow ? 'cur' : '']) }), A.vars({ slow, fast }));
  }
  A.step(fast === 1 ? 'fast reached 1, so the number is happy.' : `slow and fast met at ${fast}, which is not 1. That is a cycle, so the number is not happy.`, A.text('Result', String(fast === 1), fast === 1 ? 'ok' : 'bad'));
}
A.scenario('Happy', 'n = 19', () => run(19));
A.scenario('Unhappy cycle', 'n = 2', () => run(2));
''',
variants=[dict(
name="Seen set",
idea="Remember every value; seeing one again means we are in a cycle.",
approach=r'''
**Hash set.** Keep applying `next` until reaching 1 or a value already in the set.

* Time: **O(log n)** — same number of steps as Floyd.
* Space: **O(log n)** — the set holds the values visited before the cycle closes.
''',
tc="log", sc="log",
java=r'''
public class HappyNumber {

    private static int next(int x) {
        int sum = 0;
        while (x > 0) {
            int d = x % 10;
            sum += d * d;
            x /= 10;
        }
        return sum;
    }

    public boolean isHappy(int n) {
        MyHashSet<Integer> seen = new MyHashSet<>();
        while (n != 1 && seen.add(n)) {
            n = next(n);
        }
        return n == 1;
    }
}
''',
trace=r'''
const nx = x => String(x).split('').reduce((s, d) => s + d * d, 0);
function run(n) {
  const seen = new Set();
  while (n !== 1 && !seen.has(n)) { seen.add(n); const m = nx(n); A.step(`${n} → ${String(n).split('').map(d => d + '²').join(' + ')} = ${m}.`, A.hashTable('seen', seen), A.vars({ n: m })); n = m; }
  A.step(n === 1 ? 'Reached 1: happy.' : `${n} was seen before, so we are in a cycle: not happy.`, A.hashTable('seen', seen), A.text('Result', String(n === 1), n === 1 ? 'ok' : 'bad'));
}
A.scenario('Happy', 'n = 19', () => run(19));
A.scenario('Unhappy cycle', 'n = 2', () => run(2));
''')]),

P(num=219, slug="contains-duplicate-ii", title="Contains Duplicate II", diff="Easy", topic="Hashmap", cls="ContainsDuplicateII",
idea="Remember the last index of every value; a repeat within k positions answers true.",
vname="Last-index map",
spec=r'''
Return `true` if there are two **distinct** indices `i` and `j` with `nums[i] == nums[j]` and `|i - j| <= k`.

**Example 1**
```
Input:  nums = [1,2,3,1], k = 3
Output: true
```

**Example 2**
```
Input:  nums = [1,0,1,1], k = 1
Output: true
```

**Example 3**
```
Input:  nums = [1,2,3,1,2,3], k = 2
Output: false
```

**Constraints**
* `1 <= nums.length <= 10^5`; `0 <= k <= 10^5`
''',
approach=r'''
**Last occurrence.** Map each value to the last index where it appeared. At index `i`, if `nums[i]` was seen at `j` with
`i - j <= k`, return `true`; then update the map.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the map of distinct values.
''',
java=r'''
public class ContainsDuplicateII {

    public boolean containsNearbyDuplicate(int[] nums, int k) {
        MyHashMap<Integer, Integer> last = new MyHashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer j = last.put(nums[i], i);
            if (j != null && i - j <= k) {
                return true;
            }
        }
        return false;
    }
}
''',
test=r'''
class ContainsDuplicateIITest {

    private final ContainsDuplicateII solution = new ContainsDuplicateII();

    @Test
    void farApartButWithinK() {
        assertTrue(solution.containsNearbyDuplicate(new int[]{1, 2, 3, 1}, 3));
    }

    @Test
    void adjacent() {
        assertTrue(solution.containsNearbyDuplicate(new int[]{1, 0, 1, 1}, 1));
    }

    @Test
    void tooFar() {
        assertFalse(solution.containsNearbyDuplicate(new int[]{1, 2, 3, 1, 2, 3}, 2));
    }
}
''',
trace=r'''
function run(a, k) {
  const last = new Map();
  A.step(`Look for equal values at most ${k} positions apart. Remember the last index of each value.`, A.arr('nums', a), A.hashTable('last index', last));
  for (let i = 0; i < a.length; i++) {
    if (last.has(a[i])) {
      const j = last.get(a[i]), ok = i - j <= k;
      if (ok) { A.step(`${a[i]} was last at index ${j}, which is ${i - j} away, within ${k}. The answer is true.`, A.arr('nums', a, { range: [j, i], hl: { [j]: 'ok', [i]: 'ok' } }), A.text('Result', 'true', 'ok')); return; }
      A.step(`${a[i]} was last at index ${j}, which is ${i - j} away. That is too far, so update its last index to ${i}.`, A.arr('nums', a, { range: [j, i], hl: { [j]: 'bad', [i]: 'cur' } }), A.hashTable('last index', last));
    } else A.step(`${a[i]} is new. Remember it at index ${i}.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.hashTable('last index', last));
    last.set(a[i], i);
  }
  A.step('No close duplicate exists, so the answer is false.', A.hashTable('last index', last), A.text('Result', 'false', 'bad'));
}
A.scenario('Close duplicate', 'nums = [1,2,3,1], k = 3', () => run([1, 2, 3, 1], 3));
A.scenario('Duplicates too far apart', 'nums = [1,2,3,1,2,3], k = 2', () => run([1, 2, 3, 1, 2, 3], 2));
''',
variants=[dict(
name="Check the next k values",
idea="For each index, compare with the following k values.",
approach=r'''
**Bounded brute force.** For every `i`, compare `nums[i]` with `nums[i+1..i+k]`.

* Time: **O(n·k)** — up to k comparisons per index.
* Space: **O(1)** — no extra structures.
''',
tc="n2", sc="1",
java=r'''
public class ContainsDuplicateII {

    public boolean containsNearbyDuplicate(int[] nums, int k) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j <= i + k && j < nums.length; j++) {
                if (nums[i] == nums[j]) return true;
            }
        }
        return false;
    }
}
''',
trace=r'''
function run(a, k) {
  for (let i = 0; i < a.length; i++) {
    const hi = Math.min(a.length - 1, i + k);
    for (let j = i + 1; j <= hi; j++) if (a[i] === a[j]) { A.step(`nums[${i}] equals nums[${j}], within ${k}. The answer is true.`, A.arr('nums', a, { range: [i, hi], hl: { [i]: 'ok', [j]: 'ok' } }), A.text('Result', 'true', 'ok')); return; }
    A.step(`Compare ${a[i]} with the next ${hi - i} value${hi - i === 1 ? '' : 's'}: no match.`, A.arr('nums', a, { range: [i, hi], hl: { [i]: 'cur' } }));
  }
  A.step('No match found. Each index did up to k comparisons.', A.text('Result', 'false', 'bad'));
}
A.scenario('Duplicates too far apart', 'nums = [1,2,3,1,2,3], k = 2', () => run([1, 2, 3, 1, 2, 3], 2));
''')]),

P(num=128, slug="longest-consecutive-sequence", title="Longest Consecutive Sequence", diff="Medium", topic="Hashmap", cls="LongestConsecutiveSequence",
idea="Put everything in a set; only start counting from numbers whose predecessor is missing.",
vname="Hash set, count from run starts",
spec=r'''
Given an unsorted integer array `nums`, return the length of the longest run of consecutive integers (e.g. 1, 2, 3, 4) that can be
formed from its values. Your algorithm must run in **O(n)** time.

**Example 1**
```
Input:  nums = [100,4,200,1,3,2]
Output: 4   (1, 2, 3, 4)
```

**Example 2**
```
Input:  nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Constraints**
* `0 <= nums.length <= 10^5`; `-10^9 <= nums[i] <= 10^9`
''',
approach=r'''
**Run starts only.** Put all values in a hash set (our own `MyHashSet`). A value `x` starts a run if `x - 1` is not in the set. Only from such starts,
count `x + 1, x + 2, …` while present. Each value is visited by at most one counting walk.

* Time: **O(n)** — every value is counted at most once across all runs.
* Space: **O(n)** — the set.
''',
java=r'''
public class LongestConsecutiveSequence {

    public int longestConsecutive(int[] nums) {
        MyHashSet<Integer> set = new MyHashSet<>();
        for (int x : nums) set.add(x);
        int best = 0;
        for (int x : set) {
            if (!set.contains(x - 1)) {
                int len = 1;
                while (set.contains(x + len)) len++;
                best = Math.max(best, len);
            }
        }
        return best;
    }
}
''',
test=r'''
class LongestConsecutiveSequenceTest {

    private final LongestConsecutiveSequence solution = new LongestConsecutiveSequence();

    @Test
    void example1() {
        assertEquals(4, solution.longestConsecutive(new int[]{100, 4, 200, 1, 3, 2}));
    }

    @Test
    void withDuplicates() {
        assertEquals(9, solution.longestConsecutive(new int[]{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}));
    }

    @Test
    void empty() {
        assertEquals(0, solution.longestConsecutive(new int[]{}));
    }
}
''',
trace=r'''
function run(a) {
  const set = new Set(a), vals = [...set];
  let best = 0;
  A.step('Put every value in a set. A value starts a run only if value − 1 is missing.', A.arr('nums', a), A.hashTable('set', set));
  for (const x of vals) {
    if (set.has(x - 1)) { A.step(`${x} is not a run start, because ${x - 1} is present. Skip it.`, A.arr('values', vals, { hl: { [vals.indexOf(x)]: 'dim' } }), A.vars({ best })); continue; }
    let len = 1; while (set.has(x + len)) len++;
    const run = [...Array(len).keys()].map(t => x + t);
    best = Math.max(best, len);
    A.step(`${x} starts a run: ${run.join(', ')}, length ${len}. Best is ${best}.`, A.arr('values', vals, { hl: vals.map((v, i) => [i, run.includes(v) ? (v === x ? 'cur' : 'ok') : '']) }), A.vars({ best }));
  }
  A.step(`The longest consecutive run has length ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', 'nums = [100,4,200,1,3,2]', () => run([100, 4, 200, 1, 3, 2]));
A.scenario('Edge: duplicates', 'nums = [1,2,0,1]', () => run([1, 2, 0, 1]));
''',
variants=[dict(
name="Sort and scan",
idea="After sorting, consecutive values sit next to each other.",
approach=r'''
**Sort.** Sort, then scan: extend the run when `a[i] == a[i-1] + 1`, ignore duplicates, and reset otherwise.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's recursion stack.
''',
tc="nlogn", sc="log",
java=r'''
public class LongestConsecutiveSequence {

    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        int[] a = nums.clone();
        Arrays.sort(a);
        int best = 1, run = 1;
        for (int i = 1; i < a.length; i++) {
            if (a[i] == a[i - 1]) continue;
            run = (a[i] == a[i - 1] + 1) ? run + 1 : 1;
            best = Math.max(best, run);
        }
        return best;
    }
}
''',
trace=r'''
function run(nums) {
  const a = nums.slice().sort((x, y) => x - y);
  let best = 1, len = 1;
  A.step('Sort the values.', A.arr('nums', nums), A.arr('sorted', a));
  for (let i = 1; i < a.length; i++) {
    if (a[i] === a[i - 1]) { A.step(`${a[i]} is a duplicate. Ignore it.`, A.arr('sorted', a, { hl: { [i]: 'dim' } }), A.vars({ run: len, best })); continue; }
    len = a[i] === a[i - 1] + 1 ? len + 1 : 1; best = Math.max(best, len);
    A.step(len > 1 ? `${a[i]} follows ${a[i - 1]}, so the run grows to ${len}.` : `${a[i]} does not follow ${a[i - 1]}, so a new run starts.`, A.arr('sorted', a, { hl: { [i]: len > 1 ? 'ok' : 'bad' } }), A.vars({ run: len, best }));
  }
  A.step(`Longest run: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', 'nums = [100,4,200,1,3,2]', () => run([100, 4, 200, 1, 3, 2]));
''')]),

P(num=228, slug="summary-ranges", title="Summary Ranges", diff="Easy", topic="Intervals", cls="SummaryRanges",
idea="Walk the sorted unique values, extending a range while the next value is exactly one more.",
vname="Single scan",
spec=r'''
`nums` is sorted and has no duplicates. Return the smallest sorted list of ranges that covers every number exactly. A range
`[a,b]` is written `"a->b"` if `a != b`, else `"a"`.

**Example 1**
```
Input:  nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
```

**Example 2**
```
Input:  nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
```

**Constraints**
* `0 <= nums.length <= 20`; values fit in 32-bit integers; sorted, unique.
''',
approach=r'''
**Grow each range.** Mark a range start `i`; advance `j` while `nums[j+1] == nums[j] + 1`. Emit the range and continue from `j + 1`.

* Time: **O(n)** — each value is visited once.
* Space: **O(1)** — apart from the output.
''',
java=r'''
public class SummaryRanges {

    public List<String> summaryRanges(int[] nums) {
        List<String> out = new ArrayList<>();
        for (int i = 0; i < nums.length; ) {
            int j = i;
            while (j + 1 < nums.length && nums[j + 1] == nums[j] + 1) j++;
            out.add(i == j ? String.valueOf(nums[i]) : nums[i] + "->" + nums[j]);
            i = j + 1;
        }
        return out;
    }
}
''',
test=r'''
class SummaryRangesTest {

    private final SummaryRanges solution = new SummaryRanges();

    @Test
    void example1() {
        assertEquals(List.of("0->2", "4->5", "7"), solution.summaryRanges(new int[]{0, 1, 2, 4, 5, 7}));
    }

    @Test
    void example2() {
        assertEquals(List.of("0", "2->4", "6", "8->9"), solution.summaryRanges(new int[]{0, 2, 3, 4, 6, 8, 9}));
    }

    @Test
    void empty() {
        assertEquals(List.of(), solution.summaryRanges(new int[]{}));
    }
}
''',
trace=r'''
function run(a) {
  const out = [];
  A.step('Grow a range while the next number is exactly one more.', A.arr('nums', a), A.arr('ranges', out));
  for (let i = 0; i < a.length;) {
    let j = i;
    while (j + 1 < a.length && a[j + 1] === a[j] + 1) j++;
    out.push(i === j ? String(a[i]) : `${a[i]}->${a[j]}`);
    A.step(i === j ? `${a[i]} stands alone.` : `${a[i]} to ${a[j]} are consecutive.${j + 1 < a.length ? ` ${a[j + 1]} breaks the run.` : ''}`, A.arr('nums', a, { range: [i, j], hl: { [i]: 'ok', [j]: 'ok' } }), A.arr('ranges', out, { hl: { [out.length - 1]: 'ok' } }));
    i = j + 1;
  }
  A.step(`Ranges: ${JSON.stringify(out)}.`, A.text('Result', JSON.stringify(out), 'ok'));
}
A.scenario('Classic', 'nums = [0,1,2,4,5,7]', () => run([0, 1, 2, 4, 5, 7]));
A.scenario('Singles and runs', 'nums = [0,2,3,4,6,8,9]', () => run([0, 2, 3, 4, 6, 8, 9]));
'''),

P(num=56, slug="merge-intervals", title="Merge Intervals", diff="Medium", topic="Intervals", cls="MergeIntervals",
idea="Sort by start; each interval either overlaps the last merged one (extend it) or starts a new one.",
vname="Sort, then sweep",
spec=r'''
Given an array of `intervals` where `intervals[i] = [start, end]`, merge all overlapping intervals and return the
non-overlapping intervals that cover exactly the same ranges.

**Example 1**
```
Input:  [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

**Example 2**
```
Input:  [[1,4],[4,5]]
Output: [[1,5]]   (touching intervals overlap)
```

**Constraints**
* `1 <= intervals.length <= 10^4`; `0 <= start <= end <= 10^4`
''',
approach=r'''
**Sort and sweep.** Sort by start. Keep the last merged interval; if the next start is `<=` its end, extend the end to the
maximum of both ends. Otherwise append the next interval as a new merged interval.

* Time: **O(n log n)** — sorting; the sweep is linear.
* Space: **O(n)** — the output (plus the sort's stack).
''',
java=r'''
public class MergeIntervals {

    public int[][] merge(int[][] intervals) {
        int[][] sorted = intervals.clone();
        Arrays.sort(sorted, Comparator.comparingInt(a -> a[0]));
        List<int[]> out = new ArrayList<>();
        for (int[] cur : sorted) {
            if (!out.isEmpty() && cur[0] <= out.getLast()[1]) {
                out.getLast()[1] = Math.max(out.getLast()[1], cur[1]);
            } else {
                out.add(new int[]{cur[0], cur[1]});
            }
        }
        return out.toArray(new int[0][]);
    }
}
''',
test=r'''
class MergeIntervalsTest {

    private final MergeIntervals solution = new MergeIntervals();

    @Test
    void example1() {
        assertArrayEquals(new int[][]{{1, 6}, {8, 10}, {15, 18}}, solution.merge(new int[][]{{1, 3}, {2, 6}, {8, 10}, {15, 18}}));
    }

    @Test
    void touching() {
        assertArrayEquals(new int[][]{{1, 5}}, solution.merge(new int[][]{{1, 4}, {4, 5}}));
    }

    @Test
    void unsortedAndNested() {
        assertArrayEquals(new int[][]{{0, 5}}, solution.merge(new int[][]{{2, 3}, {0, 5}, {1, 4}}));
    }
}
''',
trace=r'''
function run(iv) {
  const s = iv.map(x => x.slice()).sort((a, b) => a[0] - b[0]), out = [];
  const lab = a => a.map(x => `[${x[0]},${x[1]}]`);
  A.step('Sort the intervals by start.', A.arr('input', lab(iv)), A.arr('sorted', lab(s)));
  s.forEach((c, i) => {
    const last = out[out.length - 1];
    if (last && c[0] <= last[1]) { const old = last[1]; last[1] = Math.max(last[1], c[1]); A.step(`[${c}] starts at ${c[0]}, which is at most the last end ${old}, so they overlap. Extend the end to ${last[1]}.`, A.arr('sorted', lab(s), { hl: { [i]: 'cur' } }), A.arr('merged', lab(out), { hl: { [out.length - 1]: 'sel' } })); }
    else { out.push(c.slice()); A.step(last ? `[${c}] starts after ${last[1]}, so there is no overlap. Start a new interval.` : `Start with [${c}].`, A.arr('sorted', lab(s), { hl: { [i]: 'cur' } }), A.arr('merged', lab(out), { hl: { [out.length - 1]: 'ok' } })); }
  });
  A.step(`Merged: ${lab(out).join(' ')}.`, A.arr('merged', lab(out), { hl: out.map((_, i) => [i, 'ok']) }));
}
A.scenario('Classic', '[[1,3],[2,6],[8,10],[15,18]]', () => run([[1, 3], [2, 6], [8, 10], [15, 18]]));
A.scenario('Unsorted and nested', '[[2,3],[0,5],[1,4],[6,7]]', () => run([[2, 3], [0, 5], [1, 4], [6, 7]]));
'''),

P(num=57, slug="insert-interval", title="Insert Interval", diff="Medium", topic="Intervals", cls="InsertInterval",
idea="Copy intervals ending before the new one, merge every interval that overlaps it, then copy the rest.",
vname="Three-phase linear scan",
spec=r'''
`intervals` is sorted by start and non-overlapping. Insert `newInterval` and merge where needed, so the result is still
sorted and non-overlapping. Return the result.

**Example 1**
```
Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2**
```
Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

**Constraints**
* `0 <= intervals.length <= 10^4`; `0 <= start <= end <= 10^5`
''',
approach=r'''
**Three phases.** (1) Copy intervals whose end is before the new start. (2) While an interval starts at or before the new end,
merge it in: `start = min`, `end = max`. Add the merged interval. (3) Copy the rest.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the output.
''',
java=r'''
public class InsertInterval {

    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> out = new ArrayList<>();
        int i = 0, n = intervals.length, start = newInterval[0], end = newInterval[1];
        while (i < n && intervals[i][1] < start) out.add(intervals[i++]);
        while (i < n && intervals[i][0] <= end) {
            start = Math.min(start, intervals[i][0]);
            end = Math.max(end, intervals[i][1]);
            i++;
        }
        out.add(new int[]{start, end});
        while (i < n) out.add(intervals[i++]);
        return out.toArray(new int[0][]);
    }
}
''',
test=r'''
class InsertIntervalTest {

    private final InsertInterval solution = new InsertInterval();

    @Test
    void example1() {
        assertArrayEquals(new int[][]{{1, 5}, {6, 9}}, solution.insert(new int[][]{{1, 3}, {6, 9}}, new int[]{2, 5}));
    }

    @Test
    void mergesSeveral() {
        assertArrayEquals(new int[][]{{1, 2}, {3, 10}, {12, 16}},
                solution.insert(new int[][]{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}}, new int[]{4, 8}));
    }

    @Test
    void intoEmpty() {
        assertArrayEquals(new int[][]{{5, 7}}, solution.insert(new int[][]{}, new int[]{5, 7}));
    }
}
''',
trace=r'''
function run(iv, nw) {
  const lab = a => a.map(x => `[${x[0]},${x[1]}]`), out = [];
  let i = 0, s = nw[0], e = nw[1];
  A.step(`Insert [${nw}]. Phase 1: copy intervals that end before ${s}.`, A.arr('intervals', lab(iv)), A.vars({ newStart: s, newEnd: e }));
  while (i < iv.length && iv[i][1] < s) { out.push(iv[i]); A.step(`[${iv[i]}] ends before ${s}. Copy it unchanged.`, A.arr('intervals', lab(iv), { hl: { [i]: 'ok' } }), A.arr('result', lab(out))); i++; }
  while (i < iv.length && iv[i][0] <= e) { s = Math.min(s, iv[i][0]); e = Math.max(e, iv[i][1]); A.step(`Phase 2: [${iv[i]}] overlaps, so absorb it. The merged interval is now [${s},${e}].`, A.arr('intervals', lab(iv), { hl: { [i]: 'sel' } }), A.vars({ newStart: s, newEnd: e })); i++; }
  out.push([s, e]);
  A.step(`Add the merged interval [${s},${e}].`, A.arr('result', lab(out), { hl: { [out.length - 1]: 'alt' } }));
  while (i < iv.length) { out.push(iv[i]); i++; }
  A.step('Phase 3: copy the remaining intervals.', A.arr('result', lab(out), { hl: out.map((_, t) => [t, 'ok']) }));
}
A.scenario('Merge several', 'intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], new = [4,8]', () => run([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]));
A.scenario('Simple overlap', 'intervals = [[1,3],[6,9]], new = [2,5]', () => run([[1, 3], [6, 9]], [2, 5]));
'''),
]
