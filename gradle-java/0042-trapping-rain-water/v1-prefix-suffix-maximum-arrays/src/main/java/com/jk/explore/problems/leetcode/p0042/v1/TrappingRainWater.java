package com.jk.explore.problems.leetcode.p0042.v1;

import java.util.*;

public class TrappingRainWater {

    public int trap(int[] height) {
        int n = height.length;
        int[] leftMax = new int[n], rightMax = new int[n];
        for (int i = 0; i < n; i++) leftMax[i] = Math.max(i > 0 ? leftMax[i - 1] : 0, height[i]);
        for (int i = n - 1; i >= 0; i--) rightMax[i] = Math.max(i < n - 1 ? rightMax[i + 1] : 0, height[i]);
        int water = 0;
        for (int i = 0; i < n; i++) water += Math.min(leftMax[i], rightMax[i]) - height[i];
        return water;
    }
}
