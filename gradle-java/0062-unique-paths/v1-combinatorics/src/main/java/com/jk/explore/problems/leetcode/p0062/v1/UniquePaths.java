package com.jk.explore.problems.leetcode.p0062.v1;

import java.util.*;

public class UniquePaths {

    public int uniquePaths(int m, int n) {
        long result = 1;
        int k = Math.min(m, n) - 1, total = m + n - 2;
        for (int i = 1; i <= k; i++) {
            result = result * (total - k + i) / i;
        }
        return (int) result;
    }
}
