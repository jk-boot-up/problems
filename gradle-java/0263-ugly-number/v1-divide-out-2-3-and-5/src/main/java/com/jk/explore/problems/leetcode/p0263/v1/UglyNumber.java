package com.jk.explore.problems.leetcode.p0263.v1;

import java.util.*;

public class UglyNumber {

    public boolean isUgly(int n) {
        if (n <= 0) return false;
        for (int p : new int[]{2, 3, 5}) while (n % p == 0) n /= p;
        return n == 1;
    }
}
