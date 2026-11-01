package com.jk.explore.problems.leetcode.p0307.v2;

import java.util.*;

public class NumArray {

    private final int[] values, tree;

    public NumArray(int[] nums) {
        values = nums.clone();
        tree = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) add(i + 1, nums[i]);
    }

    private void add(int i, int delta) {
        for (; i < tree.length; i += i & -i) tree[i] += delta;
    }

    private int prefix(int i) {
        int s = 0;
        for (; i > 0; i -= i & -i) s += tree[i];
        return s;
    }

    public void update(int index, int val) {
        add(index + 1, val - values[index]);
        values[index] = val;
    }

    public int sumRange(int left, int right) {
        return prefix(right + 1) - prefix(left);
    }
}
