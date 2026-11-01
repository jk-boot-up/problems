package com.jk.explore.problems.leetcode.p1658.v1;

import java.util.*;

public class MinOperationsReduceX {

    public int minOperations(int[] nums, int x) {
        long total = 0;
        for (int v : nums) total += v;
        long need = total - x;
        if (need < 0) return -1;
        int best = -1, lo = 0;
        long sum = 0;
        for (int hi = 0; hi < nums.length; hi++) {
            sum += nums[hi];
            while (sum > need) sum -= nums[lo++];
            if (sum == need) best = Math.max(best, hi - lo + 1);
        }
        if (need == 0) best = Math.max(best, 0);
        return best < 0 ? -1 : nums.length - best;
    }
}
