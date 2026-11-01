PROBLEMS = [
P(num=88, slug="merge-sorted-array", title="Merge Sorted Array", diff="Easy", topic="Array / String", cls="MergeSortedArray",
idea="Fill nums1 from the back with the larger of the two current tails, so nothing unread is overwritten.",
spec=r'''
You get two integer arrays `nums1` and `nums2`, both sorted in non-decreasing order, plus two counts `m` and `n`.
Only the first `m` values of `nums1` are real; its last `n` slots hold `0` as placeholders. `nums2` holds exactly `n` values.

Merge `nums2` into `nums1` **in place** so that `nums1` becomes one sorted array of length `m + n`. The method returns nothing.

**Example 1**
```
Input:  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: nums1 = [1,2,2,3,5,6]
```

**Example 2**
```
Input:  nums1 = [0], m = 0, nums2 = [1], n = 1
Output: nums1 = [1]
```

**Constraints**
* `nums1.length == m + n`, `nums2.length == n`
* `0 <= m, n <= 200`, `1 <= m + n <= 200`
* `-10^9 <= nums1[i], nums2[j] <= 10^9`
''',
approach=r'''
**Three pointers, writing from the back.** `i` points at the last real value of `nums1`, `j` at the last value of `nums2`,
and `k` at the last slot of `nums1`. At every step copy the larger of `nums1[i]` and `nums2[j]` into `nums1[k]`, then move
the pointer you copied from, and `k`, one step left. Writing from the back means we only ever overwrite slots we have already read.
When `nums2` runs out, the rest of `nums1` is already in place.

* Time: **O(m + n)** — every slot of nums1 is written exactly once.
* Space: **O(1)** — only three index variables.
''',
java=r'''
public class MergeSortedArray {

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1, j = n - 1, k = m + n - 1;
        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
    }
}
''',
test=r'''
class MergeSortedArrayTest {

    private final MergeSortedArray solution = new MergeSortedArray();

    @Test
    void mergesInterleavedValues() {
        int[] nums1 = {1, 2, 3, 0, 0, 0};
        solution.merge(nums1, 3, new int[]{2, 5, 6}, 3);
        assertArrayEquals(new int[]{1, 2, 2, 3, 5, 6}, nums1);
    }

    @Test
    void emptySecondArray() {
        int[] nums1 = {1};
        solution.merge(nums1, 1, new int[]{}, 0);
        assertArrayEquals(new int[]{1}, nums1);
    }

    @Test
    void emptyFirstArray() {
        int[] nums1 = {0};
        solution.merge(nums1, 0, new int[]{1}, 1);
        assertArrayEquals(new int[]{1}, nums1);
    }

    @Test
    void allOfSecondAreSmaller() {
        int[] nums1 = {4, 5, 6, 0, 0, 0};
        solution.merge(nums1, 3, new int[]{1, 2, 3}, 3);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5, 6}, nums1);
    }
}
''',
trace=r'''
function run(a, m, b) {
  const n = b.length;
  let i = m - 1, j = n - 1, k = m + n - 1;
  const view = (h1 = {}, h2 = {}) => [A.arr('nums1', a, { ptr: [[i, 'i'], [k, 'k']], hl: Object.assign(Object.fromEntries(a.map((_, x) => [x, x >= m && x > k ? '' : x >= m ? 'dim' : ''])), h1) }), A.arr('nums2', b, { ptr: [[j, 'j']], hl: h2 }), A.vars({ i, j, k })];
  A.step('We merge from the back. i marks the last real value of nums1, j the end of nums2, and k the last free slot.', view());
  while (j >= 0) {
    if (i >= 0 && a[i] > b[j]) {
      A.step(`Compare ${a[i]} and ${b[j]}. ${a[i]} is larger, so it belongs in slot ${k}.`, view({ [i]: 'cur', [k]: 'sel' }, { [j]: 'cur' }));
      a[k] = a[i]; i--; k--;
      A.step(`Placed ${a[k + 1]}. Move i and k one step left.`, view({ [k + 1]: 'ok' }));
    } else {
      A.step(i >= 0 ? `Compare ${a[i]} and ${b[j]}. ${b[j]} is at least as large, so it belongs in slot ${k}.` : `nums1 has no values left to compare, so copy ${b[j]} into slot ${k}.`, view(i >= 0 ? { [i]: 'cur', [k]: 'sel' } : { [k]: 'sel' }, { [j]: 'cur' }));
      a[k] = b[j]; j--; k--;
      A.step(`Placed ${a[k + 1]}. Move j and k one step left.`, view({ [k + 1]: 'ok' }));
    }
  }
  A.step('nums2 is used up. Whatever remains in nums1 is already in place, so the merge is complete.', A.arr('nums1', a, { hl: a.map((_, x) => [x, 'ok']) }), A.text('Result', JSON.stringify(a), 'ok'));
}
A.scenario('Interleaved values', 'nums1 = [1,2,3,_,_,_], nums2 = [2,5,6]', () => run([1, 2, 3, 0, 0, 0], 3, [2, 5, 6]));
A.scenario('nums2 all smaller', 'nums1 = [4,5,6,_,_,_], nums2 = [1,2,3]', () => run([4, 5, 6, 0, 0, 0], 3, [1, 2, 3]));
A.scenario('Edge: nums1 empty', 'm = 0, nums2 = [1]', () => run([0], 0, [1]));
'''),

P(num=27, slug="remove-element", title="Remove Element", diff="Easy", topic="Array / String", cls="RemoveElement",
idea="A write pointer keeps every value that is not val; the reader skips the ones that are.",
spec=r'''
Given an integer array `nums` and an integer `val`, remove every occurrence of `val` **in place** and return `k`, the number
of elements that are not equal to `val`. The first `k` slots of `nums` must hold those elements (in any order); what remains after
index `k - 1` does not matter.

**Example 1**
```
Input:  nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
```

**Example 2**
```
Input:  nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,3,0,4,_,_,_]
```

**Constraints**
* `0 <= nums.length <= 100`
* `0 <= nums[i] <= 50`, `0 <= val <= 100`
''',
approach=r'''
**Read/write pointers.** Scan the array with a reader `i`. Whenever `nums[i] != val`, copy it to `nums[k]` and advance `k`.
At the end, `k` is the number of kept values and they sit at the front.

* Time: **O(n)** — one pass over the array.
* Space: **O(1)** — the array is rewritten in place.
''',
java=r'''
public class RemoveElement {

    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int x : nums) {
            if (x != val) {
                nums[k++] = x;
            }
        }
        return k;
    }
}
''',
test=r'''
class RemoveElementTest {

    private final RemoveElement solution = new RemoveElement();

    private static void assertPrefix(int[] expected, int[] nums, int k) {
        assertEquals(expected.length, k);
        int[] head = Arrays.copyOf(nums, k);
        Arrays.sort(head);
        int[] exp = expected.clone();
        Arrays.sort(exp);
        assertArrayEquals(exp, head);
    }

    @Test
    void example1() {
        int[] nums = {3, 2, 2, 3};
        assertPrefix(new int[]{2, 2}, nums, solution.removeElement(nums, 3));
    }

    @Test
    void example2() {
        int[] nums = {0, 1, 2, 2, 3, 0, 4, 2};
        assertPrefix(new int[]{0, 1, 3, 0, 4}, nums, solution.removeElement(nums, 2));
    }

    @Test
    void emptyArray() {
        assertEquals(0, solution.removeElement(new int[]{}, 1));
    }

    @Test
    void allRemoved() {
        int[] nums = {7, 7, 7};
        assertEquals(0, solution.removeElement(nums, 7));
    }
}
''',
trace=r'''
function run(a, val) {
  let k = 0;
  A.step(`Remove every ${val}. The reader i scans the array; the writer k marks where the next kept value goes.`, A.arr('nums', a, { ptr: [[0, 'i'], [0, 'k']] }), A.vars({ val, k }));
  for (let i = 0; i < a.length; i++) {
    const keep = [...Array(k).keys()].map(x => [x, 'ok']);
    if (a[i] !== val) {
      const v = a[i]; a[k] = v;
      A.step(`nums[${i}] = ${v} is not ${val}, so keep it: write it at index ${k} and move k forward.`, A.arr('nums', a, { ptr: [[i, 'i'], [k, 'k']], hl: keep.concat([[k, 'ok']], i !== k ? [[i, 'cur']] : []) }), A.vars({ val, k: k + 1 }));
      k++;
    } else {
      A.step(`nums[${i}] equals ${val}, so skip it. k stays at ${k}.`, A.arr('nums', a, { ptr: [[i, 'i'], [k, 'k']], hl: keep.concat([[i, 'bad']]) }), A.vars({ val, k }));
    }
  }
  A.step(`Done. k = ${k}: the first ${k} slots hold every value we kept.`, A.arr('nums', a, { hl: a.map((_, x) => [x, x < k ? 'ok' : 'dim']) }), A.text('Result', `k = ${k}`, 'ok'));
}
A.scenario('Mixed values', 'nums = [0,1,2,2,3,0,4,2], val = 2', () => run([0, 1, 2, 2, 3, 0, 4, 2], 2));
A.scenario('Short example', 'nums = [3,2,2,3], val = 3', () => run([3, 2, 2, 3], 3));
A.scenario('Edge: every value removed', 'nums = [7,7,7], val = 7', () => run([7, 7, 7], 7));
'''),

P(num=26, slug="remove-duplicates-from-sorted-array", title="Remove Duplicates from Sorted Array", diff="Easy", topic="Array / String", cls="RemoveDuplicates",
idea="In a sorted array, a value is new exactly when it differs from the last value we kept.",
spec=r'''
`nums` is sorted in non-decreasing order. Remove the duplicates **in place** so each distinct value appears once, keeping
their relative order. Return `k`, the number of distinct values; the first `k` slots of `nums` must hold them.

**Example 1**
```
Input:  nums = [1,1,2]
Output: 2, nums = [1,2,_]
```

**Example 2**
```
Input:  nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`
* `-100 <= nums[i] <= 100`, sorted non-decreasing
''',
approach=r'''
**Two pointers.** `k` is the length of the unique prefix (starts at 1). For each `i` from 1, if `nums[i] != nums[k-1]` it is a
new value, so write it to `nums[k]` and grow `k`.

* Time: **O(n)** — each element is looked at once.
* Space: **O(1)** — duplicates are overwritten in place.
''',
java=r'''
public class RemoveDuplicates {

    public int removeDuplicates(int[] nums) {
        int k = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[k - 1]) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
}
''',
test=r'''
class RemoveDuplicatesTest {

    private final RemoveDuplicates solution = new RemoveDuplicates();

    @Test
    void example1() {
        int[] nums = {1, 1, 2};
        int k = solution.removeDuplicates(nums);
        assertArrayEquals(new int[]{1, 2}, Arrays.copyOf(nums, k));
    }

    @Test
    void example2() {
        int[] nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        int k = solution.removeDuplicates(nums);
        assertArrayEquals(new int[]{0, 1, 2, 3, 4}, Arrays.copyOf(nums, k));
    }

    @Test
    void singleElement() {
        assertEquals(1, solution.removeDuplicates(new int[]{5}));
    }

    @Test
    void allSame() {
        int[] nums = {2, 2, 2, 2};
        assertEquals(1, solution.removeDuplicates(nums));
    }
}
''',
trace=r'''
function run(a) {
  let k = 1;
  A.step('Because the array is sorted, duplicates sit next to each other. The first value is always kept, so k starts at 1.', A.arr('nums', a, { ptr: [[1, 'i'], [1, 'k']], hl: { 0: 'ok' } }), A.vars({ k }));
  for (let i = 1; i < a.length; i++) {
    const keep = [...Array(k).keys()].map(x => [x, 'ok']);
    if (a[i] !== a[k - 1]) {
      a[k] = a[i];
      A.step(`${a[i]} differs from the last kept value ${a[k - 1]}. It is new: write it at index ${k}.`, A.arr('nums', a, { ptr: [[i, 'i'], [k, 'k']], hl: keep.concat([[k, 'ok'], [i, 'cur']]) }), A.vars({ k: k + 1 }));
      k++;
    } else {
      A.step(`${a[i]} equals the last kept value. It is a duplicate, so skip it.`, A.arr('nums', a, { ptr: [[i, 'i'], [k, 'k']], hl: keep.concat([[k - 1, 'sel'], [i, 'bad']]) }), A.vars({ k }));
    }
  }
  A.step(`Done. There are ${k} unique values at the front of the array.`, A.arr('nums', a, { hl: a.map((_, x) => [x, x < k ? 'ok' : 'dim']) }), A.text('Result', `k = ${k}`, 'ok'));
}
A.scenario('Runs of duplicates', 'nums = [0,0,1,1,1,2,2,3]', () => run([0, 0, 1, 1, 1, 2, 2, 3]));
A.scenario('Already unique', 'nums = [1,2,3]', () => run([1, 2, 3]));
A.scenario('Edge: all equal', 'nums = [2,2,2,2]', () => run([2, 2, 2, 2]));
'''),

P(num=80, slug="remove-duplicates-from-sorted-array-ii", title="Remove Duplicates from Sorted Array II", diff="Medium", topic="Array / String", cls="RemoveDuplicatesII",
idea="Keep a value only if it differs from the value two slots back in the kept prefix.",
spec=r'''
`nums` is sorted in non-decreasing order. Remove extra duplicates **in place** so that every distinct value appears **at most twice**,
keeping the relative order. Return `k`, the length of the result; the first `k` slots of `nums` must hold it. Use O(1) extra memory.

**Example 1**
```
Input:  nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
```

**Example 2**
```
Input:  nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`
* `-10^4 <= nums[i] <= 10^4`, sorted non-decreasing
''',
approach=r'''
**Compare with two back.** Keep a write index `k`. A value `x` may be written if `k < 2` or `x != nums[k - 2]`. If it equals
`nums[k-2]`, then because the array is sorted, `nums[k-2]` and `nums[k-1]` are both `x` already, so writing it would make a third copy.

* Time: **O(n)** — a single pass.
* Space: **O(1)** — in-place overwrite with one write index.
''',
java=r'''
public class RemoveDuplicatesII {

    public int removeDuplicates(int[] nums) {
        int k = 0;
        for (int x : nums) {
            if (k < 2 || x != nums[k - 2]) {
                nums[k++] = x;
            }
        }
        return k;
    }
}
''',
test=r'''
class RemoveDuplicatesIITest {

    private final RemoveDuplicatesII solution = new RemoveDuplicatesII();

    @Test
    void example1() {
        int[] nums = {1, 1, 1, 2, 2, 3};
        int k = solution.removeDuplicates(nums);
        assertArrayEquals(new int[]{1, 1, 2, 2, 3}, Arrays.copyOf(nums, k));
    }

    @Test
    void example2() {
        int[] nums = {0, 0, 1, 1, 1, 1, 2, 3, 3};
        int k = solution.removeDuplicates(nums);
        assertArrayEquals(new int[]{0, 0, 1, 1, 2, 3, 3}, Arrays.copyOf(nums, k));
    }

    @Test
    void shortArrays() {
        assertEquals(1, solution.removeDuplicates(new int[]{1}));
        assertEquals(2, solution.removeDuplicates(new int[]{1, 1}));
    }
}
''',
trace=r'''
function run(a) {
  let k = 0;
  A.step('Each value may appear at most twice. Write a value only if it differs from the value two slots behind the write index k.', A.arr('nums', a, { ptr: [[0, 'i'], [0, 'k']] }), A.vars({ k }));
  for (let i = 0; i < a.length; i++) {
    const x = a[i], keep = [...Array(k).keys()].map(t => [t, 'ok']);
    if (k < 2 || x !== a[k - 2]) {
      a[k] = x;
      A.step(k < 2 ? `The first two values are always kept. Write ${x} at index ${k}.` : `${x} differs from nums[${k - 2}] = ${a[k - 2]}, so it is at most the second copy. Keep it at index ${k}.`, A.arr('nums', a, { ptr: [[i, 'i'], [k, 'k']], hl: keep.concat([[k, 'ok']], k >= 2 ? [[k - 2, 'sel']] : []) }), A.vars({ k: k + 1 }));
      k++;
    } else {
      A.step(`${x} equals nums[${k - 2}], so two copies are already kept. Skip this third copy.`, A.arr('nums', a, { ptr: [[i, 'i'], [k, 'k']], hl: keep.concat([[k - 2, 'sel'], [i, 'bad']]) }), A.vars({ k }));
    }
  }
  A.step(`Done. k = ${k}.`, A.arr('nums', a, { hl: a.map((_, t) => [t, t < k ? 'ok' : 'dim']) }), A.text('Result', `k = ${k}`, 'ok'));
}
A.scenario('Triples to trim', 'nums = [1,1,1,2,2,2,3]', () => run([1, 1, 1, 2, 2, 2, 3]));
A.scenario('Long run', 'nums = [0,0,1,1,1,1,2]', () => run([0, 0, 1, 1, 1, 1, 2]));
A.scenario('Edge: nothing to trim', 'nums = [1,1,2]', () => run([1, 1, 2]));
'''),

P(num=169, slug="majority-element", title="Majority Element", diff="Easy", topic="Array / String", cls="MajorityElement",
idea="Boyer–Moore voting: the majority value survives when every vote is cancelled by a different value.",
spec=r'''
Given an array `nums` of size `n`, return the **majority element**: the value that appears more than `⌊n / 2⌋` times.
You may assume a majority element always exists.

**Example 1**
```
Input:  nums = [3,2,3]
Output: 3
```

**Example 2**
```
Input:  nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints**
* `1 <= n <= 5 * 10^4`
* `-10^9 <= nums[i] <= 10^9`

**Follow-up:** solve it in linear time and O(1) space.
''',
approach=r'''
**Boyer–Moore voting.** Keep a `candidate` and a `count`. When `count` is 0, adopt the current value as the candidate.
A matching value adds a vote, a different value removes one. Each different value cancels one copy of the majority,
but the majority has more copies than all other values together, so it is the candidate left at the end.

* Time: **O(n)** — one pass over the votes.
* Space: **O(1)** — just a candidate and a counter, no hash map.
''',
java=r'''
public class MajorityElement {

    public int majorityElement(int[] nums) {
        int candidate = 0, count = 0;
        for (int x : nums) {
            if (count == 0) {
                candidate = x;
            }
            count += (x == candidate) ? 1 : -1;
        }
        return candidate;
    }
}
''',
test=r'''
class MajorityElementTest {

    private final MajorityElement solution = new MajorityElement();

    @Test
    void example1() {
        assertEquals(3, solution.majorityElement(new int[]{3, 2, 3}));
    }

    @Test
    void example2() {
        assertEquals(2, solution.majorityElement(new int[]{2, 2, 1, 1, 1, 2, 2}));
    }

    @Test
    void single() {
        assertEquals(-7, solution.majorityElement(new int[]{-7}));
    }
}
''',
trace=r'''
function run(a) {
  let cand = null, count = 0;
  A.step('Boyer–Moore voting: keep one candidate and a vote count. A matching value adds a vote; a different value cancels one.', A.arr('nums', a), A.vars({ candidate: '-', count }));
  a.forEach((x, i) => {
    let msg = '';
    if (count === 0) { cand = x; msg = `The count is 0, so ${x} becomes the new candidate. `; }
    if (x === cand) { count++; msg += `${x} matches the candidate, so count rises to ${count}.`; }
    else { count--; msg += `${x} differs from candidate ${cand}, cancelling one vote. Count is ${count}.`; }
    A.step(msg, A.arr('nums', a, { ptr: [[i, 'i']], hl: a.map((v, t) => [t, t < i ? 'dim' : t === i ? (x === cand ? 'ok' : 'bad') : '']) }), A.vars({ candidate: cand, count }));
  });
  A.step(`The candidate left standing is ${cand}: the majority element.`, A.arr('nums', a, { hl: a.map((v, i) => [i, v === cand ? 'ok' : 'dim']) }), A.text('Result', cand, 'ok'));
}
A.scenario('Majority spread out', 'nums = [2,2,1,1,1,2,2]', () => run([2, 2, 1, 1, 1, 2, 2]));
A.scenario('Candidate changes', 'nums = [1,3,3,1,3]', () => run([1, 3, 3, 1, 3]));
A.scenario('Edge: single value', 'nums = [5]', () => run([5]));
'''),

P(num=189, slug="rotate-array", title="Rotate Array", diff="Medium", topic="Array / String", cls="RotateArray",
idea="Rotate right by k with three reversals: the whole array, then the first k, then the rest.",
spec=r'''
Rotate the integer array `nums` to the right by `k` steps, in place. `k` is non-negative and may be larger than the array length.

**Example 1**
```
Input:  nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

**Example 2**
```
Input:  nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
```

**Constraints**
* `1 <= nums.length <= 10^5`
* `-2^31 <= nums[i] <= 2^31 - 1`
* `0 <= k <= 10^5`

**Follow-up:** can you do it in place with O(1) extra space?
''',
approach=r'''
**Triple reversal.** Let `k = k % n`. Reverse the whole array: the last `k` values move to the front, but in reverse order.
Then reverse the first `k` values and the remaining `n - k` values to restore their order.

* Time: **O(n)** — every element is swapped at most twice.
* Space: **O(1)** — swaps happen in place.
''',
java=r'''
public class RotateArray {

    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;
        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }

    private static void reverse(int[] a, int lo, int hi) {
        while (lo < hi) {
            int t = a[lo];
            a[lo++] = a[hi];
            a[hi--] = t;
        }
    }
}
''',
test=r'''
class RotateArrayTest {

    private final RotateArray solution = new RotateArray();

    @Test
    void example1() {
        int[] nums = {1, 2, 3, 4, 5, 6, 7};
        solution.rotate(nums, 3);
        assertArrayEquals(new int[]{5, 6, 7, 1, 2, 3, 4}, nums);
    }

    @Test
    void example2() {
        int[] nums = {-1, -100, 3, 99};
        solution.rotate(nums, 2);
        assertArrayEquals(new int[]{3, 99, -1, -100}, nums);
    }

    @Test
    void kLargerThanLength() {
        int[] nums = {1, 2};
        solution.rotate(nums, 3);
        assertArrayEquals(new int[]{2, 1}, nums);
    }

    @Test
    void kZero() {
        int[] nums = {1, 2, 3};
        solution.rotate(nums, 0);
        assertArrayEquals(new int[]{1, 2, 3}, nums);
    }
}
''',
trace=r'''
function run(a, k0) {
  const n = a.length, k = k0 % n;
  A.step(`Rotate right by ${k0}${k0 !== k ? `, which is the same as ${k} because rotating by ${n} changes nothing` : ''}. We use three reversals and no extra array.`, A.arr('nums', a, { hl: a.map((_, i) => [i, i >= n - k ? 'alt' : '']) }), A.vars({ k, n }));
  function rev(lo, hi, what) {
    if (lo >= hi) { A.step(`Reverse ${what}: nothing to do.`, A.arr('nums', a)); return; }
    A.step(`Reverse ${what}: indices ${lo} to ${hi}.`, A.arr('nums', a, { range: [lo, hi], ptr: [[lo, 'lo'], [hi, 'hi']] }));
    while (lo < hi) {
      [a[lo], a[hi]] = [a[hi], a[lo]];
      A.step(`Swap positions ${lo} and ${hi}.`, A.arr('nums', a, { hl: { [lo]: 'cur', [hi]: 'cur' }, ptr: [[lo, 'lo'], [hi, 'hi']] }));
      lo++; hi--;
    }
  }
  rev(0, n - 1, 'the whole array');
  A.step(`The last ${k} values are now at the front, but in reverse order.`, A.arr('nums', a, { hl: a.map((_, i) => [i, i < k ? 'alt' : '']) }));
  rev(0, k - 1, `the first ${k} values`);
  rev(k, n - 1, 'the rest');
  A.step('Each part is back in order, so the array is rotated.', A.arr('nums', a, { hl: a.map((_, i) => [i, 'ok']) }), A.text('Result', JSON.stringify(a), 'ok'));
}
A.scenario('Rotate by 3', 'nums = [1..7], k = 3', () => run([1, 2, 3, 4, 5, 6, 7], 3));
A.scenario('k larger than n', 'nums = [1,2,3], k = 4', () => run([1, 2, 3], 4));
'''),

P(num=121, slug="best-time-to-buy-and-sell-stock", title="Best Time to Buy and Sell Stock", diff="Easy", topic="Array / String", cls="BestTimeToBuyAndSellStock",
idea="Track the lowest price so far; selling today earns today's price minus that minimum.",
spec=r'''
`prices[i]` is a stock's price on day `i`. Pick **one** day to buy and a **later** day to sell to maximize profit.
Return the maximum profit, or `0` if no profitable trade exists.

**Example 1**
```
Input:  prices = [7,1,5,3,6,4]
Output: 5   (buy at 1 on day 1, sell at 6 on day 4)
```

**Example 2**
```
Input:  prices = [7,6,4,3,1]
Output: 0
```

**Constraints**
* `1 <= prices.length <= 10^5`
* `0 <= prices[i] <= 10^4`
''',
approach=r'''
**One pass with a running minimum.** For each day, the best sale today uses the cheapest price seen before it.
Keep `minPrice` and `best = max(best, price - minPrice)`.

* Time: **O(n)** — each day is visited once.
* Space: **O(1)** — two numbers: the minimum so far and the best profit.
''',
java=r'''
public class BestTimeToBuyAndSellStock {

    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE, best = 0;
        for (int p : prices) {
            minPrice = Math.min(minPrice, p);
            best = Math.max(best, p - minPrice);
        }
        return best;
    }
}
''',
test=r'''
class BestTimeToBuyAndSellStockTest {

    private final BestTimeToBuyAndSellStock solution = new BestTimeToBuyAndSellStock();

    @Test
    void example1() {
        assertEquals(5, solution.maxProfit(new int[]{7, 1, 5, 3, 6, 4}));
    }

    @Test
    void decreasingPrices() {
        assertEquals(0, solution.maxProfit(new int[]{7, 6, 4, 3, 1}));
    }

    @Test
    void singleDay() {
        assertEquals(0, solution.maxProfit(new int[]{3}));
    }
}
''',
trace=r'''
function run(p) {
  let minI = 0, best = 0, bi = -1, bj = -1;
  A.step('Walk through the days and remember the cheapest day so far. Selling today would earn today’s price minus that minimum.', A.arr('prices', p), A.vars({ minPrice: '∞', best }));
  p.forEach((x, i) => {
    if (i === 0 || x < p[minI]) { minI = i; A.step(`Day ${i}: price ${x} is the cheapest so far. Remember it as the buy day.`, A.arr('prices', p, { ptr: [[i, 'today'], [minI, 'min']], hl: { [i]: 'sel' } }), A.vars({ minPrice: p[minI], best })); return; }
    const prof = x - p[minI], better = prof > best;
    if (better) { best = prof; bi = minI; bj = i; }
    A.step(`Day ${i}: buying at ${p[minI]} and selling at ${x} earns ${prof}. ${better ? 'That is a new best.' : `The best stays ${best}.`}`, A.arr('prices', p, { ptr: [[i, 'today'], [minI, 'min']], hl: { [minI]: 'sel', [i]: better ? 'ok' : 'cur' } }), A.vars({ minPrice: p[minI], best }));
  });
  A.step(best > 0 ? `The maximum profit is ${best}: buy on day ${bi}, sell on day ${bj}.` : 'Prices never rise after a low, so no trade makes money. The answer is 0.', A.arr('prices', p, { hl: best > 0 ? { [bi]: 'sel', [bj]: 'ok' } : {} }), A.text('Result', best, 'ok'));
}
A.scenario('Dip then rise', 'prices = [7,1,5,3,6,4]', () => run([7, 1, 5, 3, 6, 4]));
A.scenario('Edge: falling prices', 'prices = [7,6,4,3,1]', () => run([7, 6, 4, 3, 1]));
'''),

P(num=122, slug="best-time-to-buy-and-sell-stock-ii", title="Best Time to Buy and Sell Stock II", diff="Medium", topic="Array / String", cls="BestTimeToBuyAndSellStockII",
idea="With unlimited trades, collect every positive day-to-day rise.",
spec=r'''
`prices[i]` is a stock's price on day `i`. You may buy and sell as many times as you like, but you can hold at most one share
at a time (you may sell and buy again on the same day). Return the maximum total profit.

**Example 1**
```
Input:  prices = [7,1,5,3,6,4]
Output: 7   (buy 1 → sell 5 = 4, buy 3 → sell 6 = 3)
```

**Example 2**
```
Input:  prices = [1,2,3,4,5]
Output: 4
```

**Example 3**
```
Input:  prices = [7,6,4,3,1]
Output: 0
```

**Constraints**
* `1 <= prices.length <= 3 * 10^4`
* `0 <= prices[i] <= 10^4`
''',
approach=r'''
**Greedy.** Any profitable run from a valley to a peak equals the sum of its daily increases. So add
`prices[i] - prices[i-1]` whenever it is positive.

* Time: **O(n)** — one comparison per neighbouring pair of days.
* Space: **O(1)** — a running total.
''',
java=r'''
public class BestTimeToBuyAndSellStockII {

    public int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            profit += Math.max(0, prices[i] - prices[i - 1]);
        }
        return profit;
    }
}
''',
test=r'''
class BestTimeToBuyAndSellStockIITest {

    private final BestTimeToBuyAndSellStockII solution = new BestTimeToBuyAndSellStockII();

    @Test
    void example1() {
        assertEquals(7, solution.maxProfit(new int[]{7, 1, 5, 3, 6, 4}));
    }

    @Test
    void increasing() {
        assertEquals(4, solution.maxProfit(new int[]{1, 2, 3, 4, 5}));
    }

    @Test
    void decreasing() {
        assertEquals(0, solution.maxProfit(new int[]{7, 6, 4, 3, 1}));
    }
}
''',
trace=r'''
function run(p) {
  let profit = 0;
  A.step('With unlimited trades, every rise from one day to the next can be collected.', A.arr('prices', p), A.vars({ profit }));
  for (let i = 1; i < p.length; i++) {
    const d = p[i] - p[i - 1];
    if (d > 0) { profit += d; A.step(`From ${p[i - 1]} to ${p[i]} the price rises by ${d}. Collect it: profit is now ${profit}.`, A.arr('prices', p, { hl: { [i - 1]: 'sel', [i]: 'ok' } }), A.vars({ gain: '+' + d, profit })); }
    else A.step(`From ${p[i - 1]} to ${p[i]} the price does not rise, so we skip this day.`, A.arr('prices', p, { hl: { [i - 1]: 'dim', [i]: 'bad' } }), A.vars({ gain: 0, profit }));
  }
  A.step(`Total profit is ${profit}.`, A.arr('prices', p), A.text('Result', profit, 'ok'));
}
A.scenario('Two separate trades', 'prices = [7,1,5,3,6,4]', () => run([7, 1, 5, 3, 6, 4]));
A.scenario('Steady climb', 'prices = [1,2,3,4,5]', () => run([1, 2, 3, 4, 5]));
A.scenario('Edge: only falling', 'prices = [7,6,4,3,1]', () => run([7, 6, 4, 3, 1]));
'''),

P(num=55, slug="jump-game", title="Jump Game", diff="Medium", topic="Array / String", cls="JumpGame",
idea="Track the farthest index reachable so far; if you ever stand beyond it, you are stuck.",
spec=r'''
You start at index `0` of `nums`. Each `nums[i]` is the **maximum** jump length from position `i`.
Return `true` if you can reach the last index, otherwise `false`.

**Example 1**
```
Input:  nums = [2,3,1,1,4]
Output: true   (0 → 1 → 4)
```

**Example 2**
```
Input:  nums = [3,2,1,0,4]
Output: false  (every path gets stuck at index 3)
```

**Constraints**
* `1 <= nums.length <= 10^4`
* `0 <= nums[i] <= 10^5`
''',
approach=r'''
**Greedy reach.** Keep `reach`, the farthest index reachable so far. Walk `i` left to right. If `i > reach` you can't get here,
so return `false`. Otherwise update `reach = max(reach, i + nums[i])`. Return `true` once `reach` covers the last index.

* Time: **O(n)** — each index is visited at most once.
* Space: **O(1)** — a single reach variable.
''',
java=r'''
public class JumpGame {

    public boolean canJump(int[] nums) {
        int reach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > reach) {
                return false;
            }
            reach = Math.max(reach, i + nums[i]);
            if (reach >= nums.length - 1) {
                return true;
            }
        }
        return true;
    }
}
''',
test=r'''
class JumpGameTest {

    private final JumpGame solution = new JumpGame();

    @Test
    void reachable() {
        assertTrue(solution.canJump(new int[]{2, 3, 1, 1, 4}));
    }

    @Test
    void blockedByZero() {
        assertFalse(solution.canJump(new int[]{3, 2, 1, 0, 4}));
    }

    @Test
    void singleElement() {
        assertTrue(solution.canJump(new int[]{0}));
    }
}
''',
trace=r'''
function run(a) {
  let reach = 0;
  A.step('Track reach: the farthest index we can get to so far. Cells inside reach are shaded blue.', A.arr('nums', a, { hl: { 0: 'sel' } }), A.vars({ reach }));
  for (let i = 0; i < a.length; i++) {
    if (i > reach) { A.step(`Index ${i} is beyond reach ${reach}. We can never stand here, so the answer is false.`, A.arr('nums', a, { ptr: [[i, 'i'], [reach, 'reach']], hl: a.map((_, t) => [t, t <= reach ? 'sel' : t === i ? 'bad' : 'dim']) }), A.text('Result', 'false', 'bad')); return; }
    reach = Math.max(reach, i + a[i]);
    const hl = a.map((_, t) => [t, t <= reach ? 'sel' : '']); hl.push([i, 'cur']);
    A.step(`From index ${i} we can jump up to ${a[i]} steps, so reach becomes ${reach}.`, A.arr('nums', a, { ptr: [[i, 'i'], [Math.min(reach, a.length - 1), 'reach']], hl }), A.vars({ reach }));
    if (reach >= a.length - 1) { A.step('Reach covers the last index, so the answer is true.', A.arr('nums', a, { hl: a.map((_, t) => [t, 'ok']) }), A.text('Result', 'true', 'ok')); return; }
  }
}
A.scenario('Reachable', 'nums = [2,3,1,1,4]', () => run([2, 3, 1, 1, 4]));
A.scenario('Stuck at a zero', 'nums = [3,2,1,0,4]', () => run([3, 2, 1, 0, 4]));
A.scenario('Edge: a zero you can jump over', 'nums = [2,0,0]', () => run([2, 0, 0]));
'''),

P(num=45, slug="jump-game-ii", title="Jump Game II", diff="Medium", topic="Array / String", cls="JumpGameII",
idea="Breadth-first in disguise: each jump covers a window of indices; the next window ends at the farthest reach from it.",
spec=r'''
You start at index `0` of `nums`; `nums[i]` is the maximum jump length from `i`. The last index is always reachable.
Return the **minimum number of jumps** needed to reach the last index.

**Example 1**
```
Input:  nums = [2,3,1,1,4]
Output: 2   (0 → 1 → 4)
```

**Example 2**
```
Input:  nums = [2,3,0,1,4]
Output: 2
```

**Constraints**
* `1 <= nums.length <= 10^4`
* `0 <= nums[i] <= 1000`
* The last index is reachable.
''',
approach=r'''
**Greedy levels.** All indices reachable with `j` jumps form a window ending at `end`. While scanning that window, track
`farthest = max(i + nums[i])`. When `i` reaches `end`, we must take another jump: `jumps++`, `end = farthest`.

* Time: **O(n)** — every index is scanned once across all windows.
* Space: **O(1)** — three counters.
''',
java=r'''
public class JumpGameII {

    public int jump(int[] nums) {
        int jumps = 0, end = 0, farthest = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (i == end) {
                jumps++;
                end = farthest;
            }
        }
        return jumps;
    }
}
''',
test=r'''
class JumpGameIITest {

    private final JumpGameII solution = new JumpGameII();

    @Test
    void example1() {
        assertEquals(2, solution.jump(new int[]{2, 3, 1, 1, 4}));
    }

    @Test
    void example2() {
        assertEquals(2, solution.jump(new int[]{2, 3, 0, 1, 4}));
    }

    @Test
    void alreadyThere() {
        assertEquals(0, solution.jump(new int[]{0}));
    }

    @Test
    void oneStepEachTime() {
        assertEquals(3, solution.jump(new int[]{1, 1, 1, 1}));
    }
}
''',
trace=r'''
function run(a) {
  let jumps = 0, end = 0, far = 0, start = 0;
  A.step('Think in levels: the indices reachable with the same number of jumps form a window. The first window holds only index 0.', A.arr('nums', a, { range: [0, 0] }), A.vars({ jumps, end, farthest: far }));
  for (let i = 0; i < a.length - 1; i++) {
    far = Math.max(far, i + a[i]);
    A.step(`Index ${i} can reach index ${i + a[i]}. The farthest reach from this window is ${far}.`, A.arr('nums', a, { range: [start, end], ptr: [[i, 'i']], hl: { [i]: 'cur', [Math.min(far, a.length - 1)]: 'alt' } }), A.vars({ jumps, end, farthest: far }));
    if (i === end) {
      jumps++; start = end + 1; end = far;
      A.step(`We reached the end of the window, so one more jump is needed. Jumps = ${jumps}; the next window is ${start} to ${Math.min(end, a.length - 1)}.`, A.arr('nums', a, { range: [start, Math.min(end, a.length - 1)] }), A.vars({ jumps, end, farthest: far }));
    }
  }
  A.step(`The last index is inside the current window. The minimum number of jumps is ${jumps}.`, A.arr('nums', a, { hl: { [a.length - 1]: 'ok' } }), A.text('Result', jumps, 'ok'));
}
A.scenario('Two jumps', 'nums = [2,3,1,1,4]', () => run([2, 3, 1, 1, 4]));
A.scenario('One step at a time', 'nums = [1,1,1,1]', () => run([1, 1, 1, 1]));
A.scenario('Edge: already at the end', 'nums = [0]', () => run([0]));
'''),
]
