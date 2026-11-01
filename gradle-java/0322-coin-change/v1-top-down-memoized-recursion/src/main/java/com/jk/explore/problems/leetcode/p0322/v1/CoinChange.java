package com.jk.explore.problems.leetcode.p0322.v1;

import java.util.*;

public class CoinChange {

    private int[] memo;

    public int coinChange(int[] coins, int amount) {
        memo = new int[amount + 1];
        Arrays.fill(memo, Integer.MIN_VALUE);
        return solve(coins, amount);
    }

    private int solve(int[] coins, int a) {
        if (a == 0) return 0;
        if (memo[a] != Integer.MIN_VALUE) return memo[a];
        int best = Integer.MAX_VALUE;
        for (int c : coins) {
            if (c <= a) {
                int sub = solve(coins, a - c);
                if (sub >= 0) best = Math.min(best, sub + 1);
            }
        }
        return memo[a] = best == Integer.MAX_VALUE ? -1 : best;
    }
}
