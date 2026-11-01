package com.jk.explore.problems.leetcode.p0011.v1;

import java.util.*;

public class ContainerWithMostWater {

    public int maxArea(int[] height) {
        int best = 0;
        for (int i = 0; i < height.length; i++) {
            for (int j = i + 1; j < height.length; j++) {
                best = Math.max(best, Math.min(height[i], height[j]) * (j - i));
            }
        }
        return best;
    }
}
