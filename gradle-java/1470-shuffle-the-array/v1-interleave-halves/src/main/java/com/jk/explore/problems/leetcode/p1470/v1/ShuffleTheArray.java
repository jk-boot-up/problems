package com.jk.explore.problems.leetcode.p1470.v1;

import java.util.*;

public class ShuffleTheArray {

    public int[] shuffle(int[] nums, int n) {
        int[] out = new int[2 * n];
        for (int i = 0; i < n; i++) {
            out[2 * i] = nums[i];
            out[2 * i + 1] = nums[n + i];
        }
        return out;
    }
}
