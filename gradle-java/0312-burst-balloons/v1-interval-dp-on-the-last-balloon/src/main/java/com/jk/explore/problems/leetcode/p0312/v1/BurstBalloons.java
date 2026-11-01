package com.jk.explore.problems.leetcode.p0312.v1;

import java.util.*;

public class BurstBalloons {

    public int maxCoins(int[] nums) {
        int n = nums.length + 2;
        int[] a = new int[n];
        a[0] = a[n - 1] = 1;
        System.arraycopy(nums, 0, a, 1, nums.length);
        int[][] dp = new int[n][n];
        for (int gap = 2; gap < n; gap++) {
            for (int l = 0; l + gap < n; l++) {
                int r = l + gap;
                for (int k = l + 1; k < r; k++) {
                    dp[l][r] = Math.max(dp[l][r], dp[l][k] + a[l] * a[k] * a[r] + dp[k][r]);
                }
            }
        }
        return dp[0][n - 1];
    }
}
