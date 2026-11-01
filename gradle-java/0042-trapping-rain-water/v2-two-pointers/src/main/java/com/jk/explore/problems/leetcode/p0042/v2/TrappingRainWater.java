package com.jk.explore.problems.leetcode.p0042.v2;

import java.util.*;

public class TrappingRainWater {

    public int trap(int[] height) {
        int l = 0, r = height.length - 1, leftMax = 0, rightMax = 0, water = 0;
        while (l < r) {
            leftMax = Math.max(leftMax, height[l]);
            rightMax = Math.max(rightMax, height[r]);
            if (leftMax < rightMax) {
                water += leftMax - height[l++];
            } else {
                water += rightMax - height[r--];
            }
        }
        return water;
    }
}
