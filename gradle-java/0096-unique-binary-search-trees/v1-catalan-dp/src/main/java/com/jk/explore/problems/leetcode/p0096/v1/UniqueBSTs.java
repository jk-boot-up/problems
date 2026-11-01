package com.jk.explore.problems.leetcode.p0096.v1;

import java.util.*;

public class UniqueBSTs {

    public int numTrees(int n) {
        int[] g = new int[n + 1];
        g[0] = 1;
        for (int k = 1; k <= n; k++) {
            for (int root = 1; root <= k; root++) g[k] += g[root - 1] * g[k - root];
        }
        return g[n];
    }
}
