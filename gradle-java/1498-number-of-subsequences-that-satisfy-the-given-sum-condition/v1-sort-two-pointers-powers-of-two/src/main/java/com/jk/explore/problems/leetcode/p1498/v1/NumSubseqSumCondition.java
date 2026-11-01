package com.jk.explore.problems.leetcode.p1498.v1;

import java.util.*;

public class NumSubseqSumCondition {

    private static final int MOD = 1_000_000_007;

    public int numSubseq(int[] nums, int target) {
        int[] a = nums.clone();
        Arrays.sort(a);
        int n = a.length;
        int[] pow = new int[n];
        pow[0] = 1;
        for (int i = 1; i < n; i++) pow[i] = pow[i - 1] * 2 % MOD;
        int lo = 0, hi = n - 1;
        long count = 0;
        while (lo <= hi) {
            if (a[lo] + a[hi] <= target) count = (count + pow[hi - lo++]) % MOD;
            else hi--;
        }
        return (int) count;
    }
}
