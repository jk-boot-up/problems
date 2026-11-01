package com.jk.explore.problems.leetcode.p0189.v1;

import java.util.*;

public class RotateArray {

    public void rotate(int[] nums, int k) {
        int n = nums.length;
        int[] rotated = new int[n];
        for (int i = 0; i < n; i++) {
            rotated[(i + k) % n] = nums[i];
        }
        System.arraycopy(rotated, 0, nums, 0, n);
    }
}
