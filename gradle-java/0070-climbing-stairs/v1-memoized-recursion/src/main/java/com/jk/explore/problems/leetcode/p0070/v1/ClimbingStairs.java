package com.jk.explore.problems.leetcode.p0070.v1;

import java.util.*;

public class ClimbingStairs {

    public int climbStairs(int n) {
        return ways(n, new int[n + 1]);
    }

    private int ways(int n, int[] memo) {
        if (n <= 1) return 1;
        if (memo[n] == 0) memo[n] = ways(n - 1, memo) + ways(n - 2, memo);
        return memo[n];
    }
}
