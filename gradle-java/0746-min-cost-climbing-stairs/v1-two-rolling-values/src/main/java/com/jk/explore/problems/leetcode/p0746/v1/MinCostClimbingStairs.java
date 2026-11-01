package com.jk.explore.problems.leetcode.p0746.v1;

import java.util.*;

public class MinCostClimbingStairs {

    public int minCostClimbingStairs(int[] cost) {
        int a = 0, b = 0; // cheapest cost to stand on step i-2 and i-1
        for (int i = 2; i <= cost.length; i++) {
            int c = Math.min(b + cost[i - 1], a + cost[i - 2]);
            a = b;
            b = c;
        }
        return b;
    }
}
