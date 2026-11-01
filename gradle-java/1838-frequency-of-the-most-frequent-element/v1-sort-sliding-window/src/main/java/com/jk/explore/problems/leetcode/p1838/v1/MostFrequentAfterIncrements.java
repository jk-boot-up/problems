package com.jk.explore.problems.leetcode.p1838.v1;

import java.util.*;

public class MostFrequentAfterIncrements {

    public int maxFrequency(int[] nums, int k) {
        int[] a = nums.clone();
        Arrays.sort(a);
        long sum = 0;
        int lo = 0, best = 0;
        for (int hi = 0; hi < a.length; hi++) {
            sum += a[hi];
            while ((long) a[hi] * (hi - lo + 1) - sum > k) sum -= a[lo++];
            best = Math.max(best, hi - lo + 1);
        }
        return best;
    }
}
