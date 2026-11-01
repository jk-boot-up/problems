package com.jk.explore.problems.leetcode.p0343.v1;

import java.util.*;

public class IntegerBreak {

    public int integerBreak(int n) {
        int[] best = new int[n + 1];
        best[1] = 1;
        for (int i = 2; i <= n; i++)
            for (int j = 1; j < i; j++) best[i] = Math.max(best[i], j * Math.max(i - j, best[i - j]));
        return best[n];
    }
}
