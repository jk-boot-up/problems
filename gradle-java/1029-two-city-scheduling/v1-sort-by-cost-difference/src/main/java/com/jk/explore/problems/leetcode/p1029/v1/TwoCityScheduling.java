package com.jk.explore.problems.leetcode.p1029.v1;

import java.util.*;

public class TwoCityScheduling {

    public int twoCitySchedCost(int[][] costs) {
        int[][] c = costs.clone();
        Arrays.sort(c, (x, y) -> Integer.compare(x[0] - x[1], y[0] - y[1]));
        int n = c.length / 2, total = 0;
        for (int i = 0; i < c.length; i++) total += i < n ? c[i][0] : c[i][1];
        return total;
    }
}
