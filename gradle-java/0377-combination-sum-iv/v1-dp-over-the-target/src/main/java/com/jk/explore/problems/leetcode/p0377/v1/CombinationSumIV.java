package com.jk.explore.problems.leetcode.p0377.v1;

import java.util.*;

public class CombinationSumIV {

    public int combinationSum4(int[] nums, int target) {
        int[] ways = new int[target + 1];
        ways[0] = 1;
        for (int t = 1; t <= target; t++)
            for (int x : nums) if (x <= t) ways[t] += ways[t - x];
        return ways[target];
    }
}
