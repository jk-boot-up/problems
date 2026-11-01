package com.jk.explore.problems.leetcode.p0674.v1;

import java.util.*;

public class LongestContinuousIncreasing {

    public int findLengthOfLCIS(int[] nums) {
        int run = 1, best = 1;
        for (int i = 1; i < nums.length; i++) {
            run = nums[i] > nums[i - 1] ? run + 1 : 1;
            best = Math.max(best, run);
        }
        return best;
    }
}
