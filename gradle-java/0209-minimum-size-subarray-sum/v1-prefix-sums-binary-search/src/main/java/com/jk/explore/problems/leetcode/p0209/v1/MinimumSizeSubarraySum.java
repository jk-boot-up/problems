package com.jk.explore.problems.leetcode.p0209.v1;

import java.util.*;

public class MinimumSizeSubarraySum {

    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int[] pre = new int[n + 1];
        for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + nums[i];
        int best = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int lo = i + 1, hi = n;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (pre[mid] - pre[i] >= target) hi = mid; else lo = mid + 1;
            }
            if (pre[lo] - pre[i] >= target) best = Math.min(best, lo - i);
        }
        return best == Integer.MAX_VALUE ? 0 : best;
    }
}
