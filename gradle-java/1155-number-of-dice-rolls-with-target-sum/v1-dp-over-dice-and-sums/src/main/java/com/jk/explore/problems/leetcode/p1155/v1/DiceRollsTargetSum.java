package com.jk.explore.problems.leetcode.p1155.v1;

import java.util.*;

public class DiceRollsTargetSum {

    private static final int MOD = 1_000_000_007;

    public int numRollsToTarget(int n, int k, int target) {
        int[] ways = new int[target + 1];
        ways[0] = 1;
        for (int d = 1; d <= n; d++) {
            int[] next = new int[target + 1];
            for (int s = 1; s <= target; s++)
                for (int f = 1; f <= k && f <= s; f++) next[s] = (next[s] + ways[s - f]) % MOD;
            ways = next;
        }
        return ways[target];
    }
}
