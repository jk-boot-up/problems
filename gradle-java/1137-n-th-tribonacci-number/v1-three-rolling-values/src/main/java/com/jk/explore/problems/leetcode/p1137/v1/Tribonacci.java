package com.jk.explore.problems.leetcode.p1137.v1;

import java.util.*;

public class Tribonacci {

    public int tribonacci(int n) {
        if (n == 0) return 0;
        int a = 0, b = 1, c = 1;
        for (int i = 3; i <= n; i++) {
            int d = a + b + c;
            a = b;
            b = c;
            c = d;
        }
        return c;
    }
}
