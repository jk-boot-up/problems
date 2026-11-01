package com.jk.explore.problems.leetcode.p0518.v1;

import java.util.*;

public class CoinChangeII {

    public int change(int amount, int[] coins) {
        int[] ways = new int[amount + 1];
        ways[0] = 1;
        for (int c : coins) {
            for (int a = c; a <= amount; a++) ways[a] += ways[a - c];
        }
        return ways[amount];
    }
}
