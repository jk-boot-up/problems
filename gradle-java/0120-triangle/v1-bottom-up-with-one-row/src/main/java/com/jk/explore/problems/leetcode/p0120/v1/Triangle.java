package com.jk.explore.problems.leetcode.p0120.v1;

import java.util.*;

public class Triangle {

    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[] best = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            List<Integer> row = triangle.get(i);
            for (int j = 0; j <= i; j++) {
                best[j] = row.get(j) + Math.min(best[j], best[j + 1]);
            }
        }
        return best[0];
    }
}
