package com.jk.explore.problems.leetcode.p0050.v1;

import java.util.*;

public class PowXN {

    public double myPow(double x, int n) {
        long e = n;
        return e < 0 ? 1 / power(x, -e) : power(x, e);
    }

    private double power(double x, long e) {
        if (e == 0) return 1;
        double half = power(x, e / 2);
        return e % 2 == 0 ? half * half : half * half * x;
    }
}
