package com.jk.explore.problems.leetcode.p0315.v2;

import java.util.*;

public class CountSmaller {

    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        int[] idx = new int[n], count = new int[n], buf = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        sort(nums, idx, buf, count, 0, n - 1);
        List<Integer> out = new ArrayList<>(n);
        for (int c : count) out.add(c);
        return out;
    }

    private void sort(int[] nums, int[] idx, int[] buf, int[] count, int lo, int hi) {
        if (lo >= hi) return;
        int mid = (lo + hi) >>> 1;
        sort(nums, idx, buf, count, lo, mid);
        sort(nums, idx, buf, count, mid + 1, hi);
        int i = lo, j = mid + 1, k = lo;
        while (i <= mid || j <= hi) {
            if (j > hi || (i <= mid && nums[idx[i]] <= nums[idx[j]])) {
                count[idx[i]] += j - (mid + 1);
                buf[k++] = idx[i++];
            } else {
                buf[k++] = idx[j++];
            }
        }
        System.arraycopy(buf, lo, idx, lo, hi - lo + 1);
    }
}
