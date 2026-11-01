package com.jk.explore.problems.leetcode.p0452.v1;

import java.util.*;

public class MinimumArrows {

    public int findMinArrowShots(int[][] points) {
        int[][] p = points.clone();
        Arrays.sort(p, (a, b) -> Integer.compare(a[1], b[1]));
        int arrows = 1;
        int x = p[0][1];
        for (int i = 1; i < p.length; i++) {
            if (p[i][0] > x) {
                arrows++;
                x = p[i][1];
            }
        }
        return arrows;
    }
}
