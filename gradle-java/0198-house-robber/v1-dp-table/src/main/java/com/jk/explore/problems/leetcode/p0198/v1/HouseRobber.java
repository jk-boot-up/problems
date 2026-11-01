package com.jk.explore.problems.leetcode.p0198.v1;

import java.util.*;

public class HouseRobber {

    public int rob(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n + 1]; // dp[i] = best using the first i houses
        dp[1] = nums[0];
        for (int i = 2; i <= n; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i - 1]);
        }
        return dp[n];
    }
}
