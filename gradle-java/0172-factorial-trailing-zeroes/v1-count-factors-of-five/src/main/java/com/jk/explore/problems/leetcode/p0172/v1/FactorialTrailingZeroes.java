package com.jk.explore.problems.leetcode.p0172.v1;

import java.util.*;

public class FactorialTrailingZeroes {

    public int trailingZeroes(int n) {
        int count = 0;
        while (n > 0) {
            n /= 5;
            count += n;
        }
        return count;
    }
}
