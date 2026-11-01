package com.jk.explore.problems.leetcode.p0343.v2;

import java.util.*;

public class IntegerBreak {

    public int integerBreak(int n) {
        if (n <= 3) return n - 1;
        int product = 1;
        while (n > 4) {
            product *= 3;
            n -= 3;
        }
        return product * n;
    }
}
