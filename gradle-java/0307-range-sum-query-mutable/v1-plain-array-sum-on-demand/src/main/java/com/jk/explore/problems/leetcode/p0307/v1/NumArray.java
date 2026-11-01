package com.jk.explore.problems.leetcode.p0307.v1;

import java.util.*;

public class NumArray {

    private final int[] values;

    public NumArray(int[] nums) {
        values = nums.clone();
    }

    public void update(int index, int val) {
        values[index] = val;
    }

    public int sumRange(int left, int right) {
        int s = 0;
        for (int i = left; i <= right; i++) s += values[i];
        return s;
    }
}
