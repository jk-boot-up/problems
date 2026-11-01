PROBLEMS = [
P(num=567, slug="permutation-in-string", title="Permutation in String", diff="Medium", topic="Sliding Window", cls="PermutationInString",
idea="Slide a window of length |s1| over s2; a permutation exists when the window's letter counts equal s1's.",
vname="Fixed window with counts",
spec=r'''
Return `true` if `s2` contains a permutation of `s1` as a substring.

**Example**
```
s1 = "ab", s2 = "eidbaooo" → true ("ba"),   s1 = "ab", s2 = "eidboaoo" → false
```

**Constraints**
* `1 <= s1.length, s2.length <= 10^4`; lowercase letters.
''',
approach=r'''
**Counts + matches.** Keep `need[26]` (s1 minus window) and `zero` = how many letters currently have `need == 0`. Each letter entering or
leaving the window updates one count and `zero` in O(1); `zero == 26` means the window is a permutation.

* Time: **O(n)** — n = |s2|.
* Space: **O(1)** — 26 counters.
''',
java=r'''
public class PermutationInString {

    public boolean checkInclusion(String s1, String s2) {
        int k = s1.length();
        if (k > s2.length()) return false;
        int[] need = new int[26];
        for (char c : s1.toCharArray()) need[c - 'a']++;
        int zero = 0;
        for (int x : need) if (x == 0) zero++;
        for (int i = 0; i < s2.length(); i++) {
            zero += update(need, s2.charAt(i) - 'a', -1);
            if (i >= k) zero += update(need, s2.charAt(i - k) - 'a', +1);
            if (zero == 26) return true;
        }
        return false;
    }

    /** Applies delta and returns the change in the number of zero entries. */
    private static int update(int[] need, int c, int delta) {
        int before = need[c] == 0 ? 1 : 0;
        need[c] += delta;
        return (need[c] == 0 ? 1 : 0) - before;
    }
}
''',
test=r'''
class PermutationInStringTest {

    private final PermutationInString solution = new PermutationInString();

    @ParameterizedTest
    @CsvSource({"ab,eidbaooo,true", "ab,eidboaoo,false", "adc,dcda,true", "abc,ab,false"})
    void checks(String s1, String s2, boolean expected) {
        assertEquals(expected, solution.checkInclusion(s1, s2));
    }
}
''',
trace=r'''
function run(s1, s2) {
  const k = s1.length, need = {}; [...s1].forEach(c => (need[c] = (need[c] || 0) + 1));
  const cnt = {};
  A.step(`Slide a window of ${k} letters over s2 and compare its letter counts with those of "${s1}".`, A.chars('s2', s2), A.map('counts in s1', need));
  for (let i = 0; i < s2.length; i++) {
    cnt[s2[i]] = (cnt[s2[i]] || 0) + 1;
    if (i >= k) { cnt[s2[i - k]]--; if (!cnt[s2[i - k]]) delete cnt[s2[i - k]]; }
    if (i >= k - 1) {
      const ok = Object.keys(need).every(c => need[c] === cnt[c]) && Object.keys(cnt).length === Object.keys(need).length;
      A.step(`Window "${s2.slice(i - k + 1, i + 1)}": ${ok ? 'same counts, so it is a permutation of s1.' : 'counts differ.'}`, A.chars('s2', s2, { range: [i - k + 1, i], hl: ok ? Object.fromEntries([...Array(k)].map((_, t) => [i - k + 1 + t, 'ok'])) : {} }), A.map('window counts', cnt));
      if (ok) { A.step('Found a permutation.', A.text('Result', 'true', 'ok')); return; }
    }
  }
  A.step('No window matched.', A.text('Result', 'false', 'bad'));
}
A.scenario('Found', 's1 = "ab", s2 = "eidbaooo"', () => run('ab', 'eidbaooo'));
'''),

P(num=424, slug="longest-repeating-character-replacement", title="Longest Repeating Character Replacement", diff="Medium", topic="Sliding Window", cls="LongestRepeatingReplacement",
idea="A window is fixable if its length minus its most frequent letter count is at most k.",
vname="Sliding window with max count",
spec=r'''
You may change at most `k` characters of `s` (uppercase letters). Return the length of the longest substring containing a single
repeated letter after the changes.

**Example**
```
s = "ABAB", k = 2 → 4,   s = "AABABBA", k = 1 → 4
```

**Constraints**
* `1 <= s.length <= 10^5`; `0 <= k <= s.length`
''',
approach=r'''
**Window that never shrinks.** Track letter counts and `maxCount` (the highest count seen in any window). If
`windowLength - maxCount > k`, move the left edge by one. `maxCount` never needs to decrease: only a larger `maxCount` can produce a longer
valid window, so the window size only grows when the answer grows.

* Time: **O(n)** — each index enters and leaves once.
* Space: **O(1)** — 26 counters.
''',
java=r'''
public class LongestRepeatingReplacement {

    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int left = 0, maxCount = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            maxCount = Math.max(maxCount, ++count[s.charAt(right) - 'A']);
            if (right - left + 1 - maxCount > k) count[s.charAt(left++) - 'A']--;
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
''',
test=r'''
class LongestRepeatingReplacementTest {

    private final LongestRepeatingReplacement solution = new LongestRepeatingReplacement();

    @ParameterizedTest
    @CsvSource({"ABAB,2,4", "AABABBA,1,4", "A,0,1", "ABCDE,1,2"})
    void lengths(String s, int k, int expected) {
        assertEquals(expected, solution.characterReplacement(s, k));
    }
}
''',
trace=r'''
function run(s, k) {
  const cnt = {}; let left = 0, maxc = 0, best = 0;
  A.step(`A window is fine if its length minus its most common letter count is at most ${k} (the letters we would change).`, A.chars('s', s), A.vars({ k }));
  for (let r = 0; r < s.length; r++) {
    cnt[s[r]] = (cnt[s[r]] || 0) + 1; maxc = Math.max(maxc, cnt[s[r]]);
    let shrunk = false;
    if (r - left + 1 - maxc > k) { cnt[s[left]]--; left++; shrunk = true; }
    best = Math.max(best, r - left + 1);
    A.step(`Add '${s[r]}'. The window needs ${r - left + 1 - maxc + (shrunk ? 1 : 0)} change${shrunk ? `s, more than ${k}, so slide the left edge` : 's'}. Best: ${best}.`, A.chars('s', s, { range: [left, r], hl: { [r]: 'cur' } }), A.map('counts in window', cnt), A.vars({ maxCount: maxc, best }));
  }
  A.step(`Longest length: ${best}.`, A.text('Result', best, 'ok'));
}
A.scenario('k = 1', 's = "AABABBA"', () => run('AABABBA', 1));
'''),

P(num=560, slug="subarray-sum-equals-k", title="Subarray Sum Equals K", diff="Medium", topic="Arrays & Hashing", cls="SubarraySumEqualsK",
idea="A subarray sums to k when two prefix sums differ by k; count earlier prefix sums in a hash map.",
vname="Prefix sums + hash map",
spec=r'''
Return the number of contiguous subarrays of `nums` whose sum equals `k`.

**Example**
```
nums = [1,1,1], k = 2 → 2,   nums = [1,2,3], k = 3 → 2
```

**Constraints**
* `1 <= nums.length <= 2 * 10^4`; `-1000 <= nums[i] <= 1000`
''',
approach=r'''
**Prefix-sum counting.** Let `sum` be the running total. A subarray ending here sums to `k` when an earlier prefix equals `sum - k`. Keep
how many times each prefix sum occurred in a `MyHashMap` (starting with `0 → 1`). Negative numbers make a sliding window impossible.

* Time: **O(n)** — one pass with O(1) map operations.
* Space: **O(n)** — the map.
''',
java=r'''
public class SubarraySumEqualsK {

    public int subarraySum(int[] nums, int k) {
        MyHashMap<Integer, Integer> seen = new MyHashMap<>();
        seen.put(0, 1);
        int sum = 0, count = 0;
        for (int x : nums) {
            sum += x;
            count += seen.getOrDefault(sum - k, 0);
            seen.merge(sum, 1, Integer::sum);
        }
        return count;
    }
}
''',
test=r'''
class SubarraySumEqualsKTest {

    private final SubarraySumEqualsK solution = new SubarraySumEqualsK();

    @Test
    void examples() {
        assertEquals(2, solution.subarraySum(new int[]{1, 1, 1}, 2));
        assertEquals(2, solution.subarraySum(new int[]{1, 2, 3}, 3));
    }

    @Test
    void negatives() {
        assertEquals(4, solution.subarraySum(new int[]{1, -1, 1, -1}, 0));
    }
}
''',
trace=r'''
function run(a, k) {
  const seen = new Map([[0, 1]]); let sum = 0, count = 0;
  A.step(`Running total so far. A subarray ending here sums to ${k} exactly when an earlier running total equals (current − ${k}).`, A.arr('nums', a), A.hashTable('prefix sum → times seen', seen), A.vars({ sum, count }));
  a.forEach((x, i) => {
    sum += x; const hits = seen.get(sum - k) || 0; count += hits;
    seen.set(sum, (seen.get(sum) || 0) + 1);
    A.step(`Add ${x}: total ${sum}. Look up ${sum} − ${k} = ${sum - k}: seen ${hits} time${hits === 1 ? '' : 's'}, so ${hits} new subarray${hits === 1 ? '' : 's'}.`, A.arr('nums', a, { hl: { [i]: 'cur' } }), A.hashTable('prefix sum → times seen', seen, { hl: sum - k }), A.vars({ sum, count }));
  });
  A.step(`${count} subarrays sum to ${k}.`, A.text('Result', count, 'ok'));
}
A.scenario('With negatives', 'nums = [1,-1,1,-1], k = 0', () => run([1, -1, 1, -1], 0));
A.scenario('Classic', 'nums = [1,2,3], k = 3', () => run([1, 2, 3], 3));
'''),

P(num=739, slug="daily-temperatures", title="Daily Temperatures", diff="Medium", topic="Stack", cls="DailyTemperatures",
idea="A stack holds days still waiting for a warmer day; each new day resolves all colder days on the stack.",
vname="Monotonic stack",
spec=r'''
For each day, return how many days you must wait for a **warmer** temperature (0 if none).

**Example**
```
[73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]
```

**Constraints**
* `1 <= n <= 10^5`; `30 <= temperatures[i] <= 100`
''',
approach=r'''
**Decreasing stack of indices.** For each day `i`, while today is warmer than the day on top of the stack, pop it and set
`answer[top] = i - top`. Then push `i`.

* Time: **O(n)** — each index is pushed and popped once.
* Space: **O(n)** — the stack.
''',
java=r'''
public class DailyTemperatures {

    public int[] dailyTemperatures(int[] temperatures) {
        int[] answer = new int[temperatures.length];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                int j = stack.pop();
                answer[j] = i - j;
            }
            stack.push(i);
        }
        return answer;
    }
}
''',
test=r'''
class DailyTemperaturesTest {

    private final DailyTemperatures solution = new DailyTemperatures();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 1, 4, 2, 1, 1, 0, 0}, solution.dailyTemperatures(new int[]{73, 74, 75, 71, 69, 72, 76, 73}));
        assertArrayEquals(new int[]{1, 1, 1, 0}, solution.dailyTemperatures(new int[]{30, 40, 50, 60}));
    }
}
''',
trace=r'''
function run(t) {
  const ans = new Array(t.length).fill(''), st = [];
  A.step('The stack holds days still waiting for a warmer day.', A.arr('temperatures', t), A.arr('answer', ans));
  t.forEach((x, i) => {
    const res = [];
    while (st.length && t[st[st.length - 1]] < x) { const j = st.pop(); ans[j] = i - j; res.push(j); }
    st.push(i);
    A.step(res.length ? `Day ${i} (${x}) is warmer than day${res.length > 1 ? 's' : ''} ${res.join(', ')}. Their wait ends now.` : `Day ${i} (${x}) warms nobody on the stack. It waits too.`, A.arr('temperatures', t, { hl: { [i]: 'cur', ...Object.fromEntries(res.map(j => [j, 'ok'])) } }), A.stack('waiting days', st.map(j => `${j}:${t[j]}`)), A.arr('answer', ans, { hl: Object.fromEntries(res.map(j => [j, 'ok'])) }));
  });
  st.forEach(j => (ans[j] = 0));
  A.step('Days left on the stack never get warmer: their answer is 0.', A.arr('answer', ans));
}
A.scenario('Classic', '[73,74,75,71,69,72,76,73]', () => run([73, 74, 75, 71, 69, 72, 76, 73]));
'''),

P(num=853, slug="car-fleet", title="Car Fleet", diff="Medium", topic="Stack", cls="CarFleet",
idea="Sort cars from closest to the target; a car that would arrive no later than the fleet ahead joins it.",
vname="Sort by position, compare arrival times",
spec=r'''
Cars on a one-lane road drive toward `target`. Car `i` starts at `position[i]` with speed `speed[i]`. A faster car that catches a slower
one slows down and they move together as a **fleet**. Return the number of fleets that reach the target.

**Example**
```
target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3] → 3
```

**Constraints**
* `1 <= n <= 10^5`; positions are distinct and `< target`.
''',
approach=r'''
**Arrival times.** Sort cars by position, closest to the target first. Each car's solo arrival time is `(target - position) / speed`. Walk
from the front: if a car's time is greater than the current fleet's time, it can never catch up and starts a new fleet; otherwise it joins.

* Time: **O(n log n)** — sorting.
* Space: **O(n)** — the sorted order.
''',
tc="nlogn",
java=r'''
public class CarFleet {

    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, (a, b) -> Integer.compare(position[b], position[a]));
        int fleets = 0;
        double slowest = 0;
        for (int i : order) {
            double time = (double) (target - position[i]) / speed[i];
            if (time > slowest) {
                fleets++;
                slowest = time;
            }
        }
        return fleets;
    }
}
''',
test=r'''
class CarFleetTest {

    private final CarFleet solution = new CarFleet();

    @Test
    void examples() {
        assertEquals(3, solution.carFleet(12, new int[]{10, 8, 0, 5, 3}, new int[]{2, 4, 1, 1, 3}));
        assertEquals(1, solution.carFleet(10, new int[]{3}, new int[]{3}));
        assertEquals(1, solution.carFleet(100, new int[]{0, 2, 4}, new int[]{4, 2, 1}));
    }
}
''',
trace=r'''
function run(target, pos, spd) {
  const order = pos.map((_, i) => i).sort((a, b) => pos[b] - pos[a]);
  const times = order.map(i => (target - pos[i]) / spd[i]);
  A.step('Sort cars from closest to the target. Each car’s solo arrival time is distance ÷ speed.', A.arr('positions (closest first)', order.map(i => pos[i])), A.arr('arrival time', times.map(t => +t.toFixed(2))));
  let fleets = 0, slow = 0;
  times.forEach((t, k) => {
    const lead = t > slow;
    if (lead) { fleets++; slow = t; }
    A.step(lead ? `Car at ${pos[order[k]]} arrives at ${+t.toFixed(2)}, later than the fleet ahead (${k ? '' : 'none'}${k ? +slow.toFixed(2) : ''}). It leads a new fleet.` : `Car at ${pos[order[k]]} would arrive at ${+t.toFixed(2)}, before the fleet ahead at ${+slow.toFixed(2)}, so it catches up and joins.`, A.arr('arrival time', times.map(x => +x.toFixed(2)), { hl: { [k]: lead ? 'ok' : 'sel' } }), A.vars({ fleets }));
  });
  A.step(`${fleets} fleets reach the target.`, A.text('Result', fleets, 'ok'));
}
A.scenario('Five cars', 'target = 12', () => run(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]));
'''),

P(num=875, slug="koko-eating-bananas", title="Koko Eating Bananas", diff="Medium", topic="Binary Search", cls="KokoEatingBananas",
idea="Binary-search the eating speed: a faster speed never needs more hours.",
vname="Binary search on the answer",
spec=r'''
Koko eats bananas from `piles` at `k` bananas per hour, finishing one pile before moving on (an hour with fewer than `k` left in a pile is
still a full hour). Return the minimum `k` that lets her finish within `h` hours.

**Example**
```
piles = [3,6,7,11], h = 8 → 4,   piles = [30,11,23,4,20], h = 5 → 30
```

**Constraints**
* `piles.length <= h <= 10^9`; `1 <= piles[i] <= 10^9`
''',
approach=r'''
**Monotone predicate.** Hours needed at speed `k` is `Σ ceil(p / k)`, which only decreases as `k` grows. Binary-search the smallest `k`
in `[1, max(piles)]` with `hours <= h` (sum in a `long`).

* Time: **O(n log M)** — M is the largest pile.
* Space: **O(1)** — a few variables.
''',
tc="nlogn",
java=r'''
public class KokoEatingBananas {

    public int minEatingSpeed(int[] piles, int h) {
        int lo = 1, hi = Arrays.stream(piles).max().getAsInt();
        while (lo < hi) {
            int k = (lo + hi) >>> 1;
            long hours = 0;
            for (int p : piles) hours += (p - 1) / k + 1; // ceil(p / k) without overflow
            if (hours <= h) hi = k; else lo = k + 1;
        }
        return lo;
    }
}
''',
test=r'''
class KokoEatingBananasTest {

    private final KokoEatingBananas solution = new KokoEatingBananas();

    @Test
    void examples() {
        assertEquals(4, solution.minEatingSpeed(new int[]{3, 6, 7, 11}, 8));
        assertEquals(30, solution.minEatingSpeed(new int[]{30, 11, 23, 4, 20}, 5));
        assertEquals(23, solution.minEatingSpeed(new int[]{30, 11, 23, 4, 20}, 6));
    }

    @Test
    void huge() {
        assertEquals(2, solution.minEatingSpeed(new int[]{1000000000, 1000000000}, 1000000000));
    }
}
''',
trace=r'''
function run(piles, h) {
  let lo = 1, hi = Math.max(...piles);
  A.step(`Search speeds from ${lo} to ${hi}. Faster speeds never need more hours.`, A.arr('piles', piles), A.vars({ h, lo, hi }));
  while (lo < hi) {
    const k = (lo + hi) >> 1, per = piles.map(p => Math.ceil(p / k)), hours = per.reduce((s, x) => s + x, 0);
    A.step(`Speed ${k}: hours per pile [${per}] = ${hours}. ${hours <= h ? `Within ${h}, so try slower.` : `More than ${h}, so go faster.`}`, A.arr('hours per pile', per, { hl: Object.fromEntries(per.map((_, i) => [i, hours <= h ? 'ok' : 'bad'])) }), A.vars({ h, lo, hi, k }));
    if (hours <= h) hi = k; else lo = k + 1;
  }
  A.step(`The slowest speed that works is ${lo}.`, A.text('Result', lo, 'ok'));
}
A.scenario('h = 8', 'piles = [3,6,7,11]', () => run([3, 6, 7, 11], 8));
'''),

P(num=981, slug="time-based-key-value-store", title="Time Based Key-Value Store", diff="Medium", topic="Binary Search", cls="TimeMap",
idea="Keep each key's (timestamp, value) list in increasing time order; get binary-searches the latest timestamp ≤ t.",
vname="Hash map of sorted lists",
spec=r'''
Implement `TimeMap`:
* `set(key, value, timestamp)` stores a value; timestamps for set calls are strictly increasing;
* `get(key, timestamp)` returns the value set for `key` at the largest `timestamp_prev <= timestamp`, or `""` if none.

**Example**
```
set("foo","bar",1); get("foo",1) → "bar"; get("foo",3) → "bar";
set("foo","bar2",4); get("foo",4) → "bar2"; get("foo",5) → "bar2"
```

**Constraints**
* `1 <= timestamp <= 10^7`; at most `2 * 10^5` calls.
''',
approach=r'''
**`MyHashMap<key, list>`.** Because timestamps only increase, appending keeps each list sorted. `get` binary-searches the last entry with
`time <= timestamp`.

* Time: **O(log n)** — per get (set is O(1) amortized).
* Space: **O(n)** — every stored value.
''',
tc="log", sc="n",
java=r'''
public class TimeMap {

    private record Entry(int time, String value) { }

    private final MyHashMap<String, List<Entry>> map = new MyHashMap<>();

    public void set(String key, String value, int timestamp) {
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(new Entry(timestamp, value));
    }

    public String get(String key, int timestamp) {
        List<Entry> list = map.get(key);
        if (list == null) return "";
        int lo = 0, hi = list.size() - 1, found = -1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            if (list.get(mid).time() <= timestamp) {
                found = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return found < 0 ? "" : list.get(found).value();
    }
}
''',
test=r'''
class TimeMapTest {

    @Test
    void example() {
        TimeMap m = new TimeMap();
        m.set("foo", "bar", 1);
        assertEquals("bar", m.get("foo", 1));
        assertEquals("bar", m.get("foo", 3));
        m.set("foo", "bar2", 4);
        assertEquals("bar2", m.get("foo", 4));
        assertEquals("bar2", m.get("foo", 5));
        assertEquals("", m.get("foo", 0));
        assertEquals("", m.get("missing", 9));
    }
}
''',
trace=r'''
A.scenario('One key, many times', 'set at 1, 4, 7, 10 · get at 5 and 0', () => {
  const list = [[1, 'a'], [4, 'b'], [7, 'c'], [10, 'd']], m = new Map([['foo', list.map(([t, v]) => `${t}:${v}`)]]);
  A.step('Each key maps to its (time, value) list. Times only increase, so every list stays sorted.', A.hashTable('key → list', m), A.arr('foo', list.map(([t, v]) => `${t}:${v}`)));
  for (const q of [5, 0]) {
    let lo = 0, hi = list.length - 1, f = -1;
    while (lo <= hi) { const mid = (lo + hi) >> 1; const ok = list[mid][0] <= q; A.step(`get(foo, ${q}): time ${list[mid][0]} is ${ok ? `≤ ${q}, a candidate; look right for a later one` : `> ${q}; look left`}.`, A.arr('foo', list.map(([t, v]) => `${t}:${v}`), { range: [lo, hi], hl: { [mid]: ok ? 'sel' : 'bad' } })); if (ok) { f = mid; lo = mid + 1; } else hi = mid - 1; }
    A.step(f < 0 ? `No time ≤ ${q}: return "".` : `The latest time ≤ ${q} is ${list[f][0]}: return "${list[f][1]}".`, A.arr('foo', list.map(([t, v]) => `${t}:${v}`), { hl: f >= 0 ? { [f]: 'ok' } : {} }), A.text(`get(foo, ${q})`, f < 0 ? '""' : list[f][1], f < 0 ? 'bad' : 'ok'));
  }
});
'''),

P(num=543, slug="diameter-of-binary-tree", title="Diameter of Binary Tree", diff="Easy", topic="Binary Tree General", cls="DiameterOfBinaryTree",
idea="The longest path through a node is its left height plus its right height; track the maximum while computing heights.",
vname="Heights with a running best", helpers=["TreeNode"],
spec=r'''
Return the **diameter** of a binary tree: the number of edges on the longest path between any two nodes (it need not pass through the root).

**Example**
```
[1,2,3,4,5] → 3   (4 → 2 → 1 → 3 or 5 → 2 → 1 → 3)
```

**Constraints**
* `1 <= n <= 10^4`
''',
approach=r'''
**Post-order heights.** `height(n) = 1 + max(height(left), height(right))`. At each node, `left + right` edges form the longest path
bending there; keep the maximum.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the recursion stack.
''',
tc="n", sc="n",
java=r'''
public class DiameterOfBinaryTree {

    private int best;

    public int diameterOfBinaryTree(TreeNode root) {
        best = 0;
        height(root);
        return best;
    }

    private int height(TreeNode n) {
        if (n == null) return 0;
        int l = height(n.left), r = height(n.right);
        best = Math.max(best, l + r);
        return 1 + Math.max(l, r);
    }
}
''',
test=r'''
class DiameterOfBinaryTreeTest {

    private final DiameterOfBinaryTree solution = new DiameterOfBinaryTree();

    @Test
    void examples() {
        assertEquals(3, solution.diameterOfBinaryTree(TreeNode.of(1, 2, 3, 4, 5)));
        assertEquals(1, solution.diameterOfBinaryTree(TreeNode.of(1, 2)));
    }

    @Test
    void notThroughRoot() {
        assertEquals(4, solution.diameterOfBinaryTree(TreeNode.of(1, 2, null, 3, 4, 5, null, null, 6)));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), hl = {}; let best = 0;
  (function h(n) {
    if (!n) return 0;
    const l = h(n.left), r = h(n.right);
    const nb = l + r > best; if (nb) best = l + r;
    hl[n.id] = 'ok';
    A.step(`${n.val}: left height ${l}, right height ${r}. A path bending here has ${l + r} edges.${nb ? ' New best.' : ''}`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'cur' } }), A.vars({ best }));
    return 1 + Math.max(l, r);
  })(root);
  A.step(`The diameter is ${best} edges.`, A.text('Result', best, 'ok'));
}
A.scenario('Classic', '[1,2,3,4,5]', () => run([1, 2, 3, 4, 5]));
'''),

P(num=572, slug="subtree-of-another-tree", title="Subtree of Another Tree", diff="Easy", topic="Binary Tree General", cls="SubtreeOfAnotherTree",
idea="Try every node of root as a starting point and compare the two trees exactly from there.",
vname="Same-tree check at every node", helpers=["TreeNode"],
spec=r'''
Return `true` if `subRoot` appears in `root` as a **subtree**: some node of `root` together with all its descendants is identical to
`subRoot`.

**Example**
```
root = [3,4,5,1,2], subRoot = [4,1,2]                       → true
root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] → false
```

**Constraints**
* `1 <= n <= 2000`; `1 <= m <= 1000`
''',
approach=r'''
**Brute-force matching.** For each node of `root`, check `sameTree(node, subRoot)`.

* Time: **O(n·m)** — up to n starting points, each comparing up to m nodes.
* Space: **O(h)** — the recursion stack.
''',
tc="n2", sc="n",
java=r'''
public class SubtreeOfAnotherTree {

    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;
        return same(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean same(TreeNode a, TreeNode b) {
        if (a == null || b == null) return a == b;
        return a.val == b.val && same(a.left, b.left) && same(a.right, b.right);
    }
}
''',
test=r'''
class SubtreeOfAnotherTreeTest {

    private final SubtreeOfAnotherTree solution = new SubtreeOfAnotherTree();

    @Test
    void examples() {
        assertTrue(solution.isSubtree(TreeNode.of(3, 4, 5, 1, 2), TreeNode.of(4, 1, 2)));
        assertFalse(solution.isSubtree(TreeNode.of(3, 4, 5, 1, 2, null, null, null, null, 0), TreeNode.of(4, 1, 2)));
    }
}
''',
trace=r'''
function run(ra, sa) {
  const root = A.mkTree(ra), sub = A.mkTree(sa);
  const same = (a, b) => (!a || !b ? a === b : a.val === b.val && same(a.left, b.left) && same(a.right, b.right));
  const mark = (n, o, c) => { if (!n) return; o[n.id] = c; mark(n.left, o, c); mark(n.right, o, c); };
  const order = []; (function pre(n) { if (!n) return; order.push(n); pre(n.left); pre(n.right); })(root);
  for (const n of order) {
    const ok = same(n, sub), hl = {}; mark(n, hl, ok ? 'ok' : 'sel'); hl[n.id] = ok ? 'ok' : 'cur';
    A.step(`Compare the subtree rooted at ${n.val} with subRoot: ${ok ? 'identical' : 'different'}.`, A.tree('root', root, { hl }), A.tree('subRoot', sub));
    if (ok) { A.step('Found a matching subtree.', A.text('Result', 'true', 'ok')); return; }
  }
  A.step('No node starts an identical subtree.', A.text('Result', 'false', 'bad'));
}
A.scenario('Present', 'root = [3,4,5,1,2], subRoot = [4,1,2]', () => run([3, 4, 5, 1, 2], [4, 1, 2]));
'''),

P(num=297, slug="serialize-and-deserialize-binary-tree", title="Serialize and Deserialize Binary Tree", diff="Hard", topic="Binary Tree General", cls="Codec",
idea="Write the tree in preorder with a marker for every null child; reading it back in the same order rebuilds it uniquely.",
vname="Preorder with null markers", helpers=["TreeNode"],
spec=r'''
Design `serialize(TreeNode)` → `String` and `deserialize(String)` → `TreeNode` so that deserializing a serialized tree reproduces it
exactly. Any format is allowed.

**Example**
```
[1,2,3,null,null,4,5] → "1,2,#,#,3,4,#,#,5,#,#" → [1,2,3,null,null,4,5]
```

**Constraints**
* `0 <= n <= 10^4`; `-1000 <= Node.val <= 1000`
''',
approach=r'''
**Preorder + `#`.** Serialize: value, then left subtree, then right subtree, with `#` for null. Deserialize: read tokens in the same order;
`#` returns null, otherwise create the node and build its left then right subtree. An explicit stack avoids deep recursion.

* Time: **O(n)** — each node is written and read once.
* Space: **O(n)** — the string and the stack.
''',
tc="n", sc="n",
java=r'''
public class Codec {

    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode marker = new TreeNode(0); // stands for null on the stack
        stack.push(root == null ? marker : root);
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            if (!sb.isEmpty()) sb.append(',');
            if (n == marker) {
                sb.append('#');
                continue;
            }
            sb.append(n.val);
            stack.push(n.right == null ? marker : n.right);
            stack.push(n.left == null ? marker : n.left);
        }
        return sb.toString();
    }

    public TreeNode deserialize(String data) {
        Iterator<String> it = Arrays.asList(data.split(",")).iterator();
        return build(it);
    }

    private TreeNode build(Iterator<String> it) {
        String token = it.next();
        if (token.equals("#")) return null;
        TreeNode n = new TreeNode(Integer.parseInt(token));
        n.left = build(it);
        n.right = build(it);
        return n;
    }
}
''',
test=r'''
class CodecTest {

    private final Codec codec = new Codec();

    @Test
    void roundTrip() {
        TreeNode root = TreeNode.of(1, 2, 3, null, null, 4, 5);
        String s = codec.serialize(root);
        assertEquals("1,2,#,#,3,4,#,#,5,#,#", s);
        assertEquals(TreeNode.toList(root), TreeNode.toList(codec.deserialize(s)));
    }

    @Test
    void empty() {
        assertNull(codec.deserialize(codec.serialize(null)));
    }

    @Test
    void negatives() {
        TreeNode root = TreeNode.of(-1, null, -2, -3);
        assertEquals(TreeNode.toList(root), TreeNode.toList(codec.deserialize(codec.serialize(root))));
    }
}
''',
trace=r'''
function run(arr) {
  const root = A.mkTree(arr), tokens = [], hl = {};
  (function ser(n) {
    if (!n) { tokens.push('#'); A.step('Empty child: write #.', A.tree('tree', root, { hl }), A.arr('serialized', tokens, { hl: { [tokens.length - 1]: 'dim' } })); return; }
    tokens.push(String(n.val)); hl[n.id] = 'ok';
    A.step(`Write ${n.val}, then its left subtree, then its right subtree.`, A.tree('tree', root, { hl: { ...hl, [n.id]: 'cur' } }), A.arr('serialized', tokens, { hl: { [tokens.length - 1]: 'ok' } }));
    ser(n.left); ser(n.right);
  })(root);
  let i = 0, rebuilt = null;
  (function des(attach) {
    const t = tokens[i++];
    if (t === '#') return;
    const n = A.node(+t); if (!rebuilt) rebuilt = n; attach(n);
    A.step(`Read ${t}: create the node; the next tokens describe its left subtree, then its right.`, A.arr('serialized', tokens, { hl: { [i - 1]: 'cur' } }), A.tree('rebuilt', rebuilt, { hl: { [n.id]: 'cur' } }));
    des(c => (n.left = c)); des(c => (n.right = c));
  })(() => {});
  A.step(`"${tokens.join(',')}" rebuilds exactly the same tree.`, A.tree('rebuilt', rebuilt), A.text('Result', tokens.join(','), 'ok'));
}
A.scenario('Five nodes', '[1,2,3,null,null,4,5]', () => run([1, 2, 3, null, null, 4, 5]));
'''),
]
