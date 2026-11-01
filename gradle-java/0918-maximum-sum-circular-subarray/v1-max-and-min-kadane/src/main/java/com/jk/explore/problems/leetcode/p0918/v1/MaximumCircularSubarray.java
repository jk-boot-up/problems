package com.jk.explore.problems.leetcode.p0918.v1;

import java.util.*;

public class MaximumCircularSubarray {

    public int maxSubarraySumCircular(int[] nums) {
        int total = 0, curMax = 0, curMin = 0, best = nums[0], worst = nums[0];
        for (int x : nums) {
            curMax = Math.max(x, curMax + x);
            best = Math.max(best, curMax);
            curMin = Math.min(x, curMin + x);
            worst = Math.min(worst, curMin);
            total += x;
        }
        return best < 0 ? best : Math.max(best, total - worst);
    }
}
