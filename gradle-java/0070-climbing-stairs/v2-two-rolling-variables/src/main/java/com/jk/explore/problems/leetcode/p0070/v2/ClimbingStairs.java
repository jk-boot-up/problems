package com.jk.explore.problems.leetcode.p0070.v2;

import java.util.*;

public class ClimbingStairs {

    public int climbStairs(int n) {
        int a = 1, b = 1; // ways to reach step i-2 and i-1
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}
