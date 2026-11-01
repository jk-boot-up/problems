package com.jk.explore.problems.leetcode.p0326.v1;

import java.util.*;

public class PowerOfThree {

    public boolean isPowerOfThree(int n) {
        if (n <= 0) return false;
        while (n % 3 == 0) n /= 3;
        return n == 1;
    }
}
