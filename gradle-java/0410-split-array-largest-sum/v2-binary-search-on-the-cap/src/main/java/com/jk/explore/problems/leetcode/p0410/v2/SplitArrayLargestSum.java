package com.jk.explore.problems.leetcode.p0410.v2;

import java.util.*;

public class SplitArrayLargestSum {

    public int splitArray(int[] nums, int k) {
        long lo = 0, hi = 0;
        for (int v : nums) {
            lo = Math.max(lo, v);
            hi += v;
        }
        while (lo < hi) {
            long cap = (lo + hi) >>> 1;
            if (pieces(nums, cap) <= k) hi = cap;
            else lo = cap + 1;
        }
        return (int) lo;
    }

    private int pieces(int[] nums, long cap) {
        int count = 1;
        long sum = 0;
        for (int v : nums) {
            if (sum + v > cap) {
                count++;
                sum = 0;
            }
            sum += v;
        }
        return count;
    }
}
