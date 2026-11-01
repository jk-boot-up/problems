package com.jk.explore.problems.leetcode.p0581.v2;

import java.util.*;

public class ShortestUnsortedSubarray {

    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length, end = -1, start = 0;
        int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, nums[i]);
            if (nums[i] < max) end = i;
        }
        for (int i = n - 1; i >= 0; i--) {
            min = Math.min(min, nums[i]);
            if (nums[i] > min) start = i;
        }
        return end == -1 ? 0 : end - start + 1;
    }
}
