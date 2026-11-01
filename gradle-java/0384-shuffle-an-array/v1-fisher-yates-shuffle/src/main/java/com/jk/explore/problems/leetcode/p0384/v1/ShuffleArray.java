package com.jk.explore.problems.leetcode.p0384.v1;

import java.util.*;

public class ShuffleArray {

    private final int[] original;
    private final Random rnd;

    public ShuffleArray(int[] nums) {
        this(nums, new Random());
    }

    ShuffleArray(int[] nums, Random rnd) {
        original = nums.clone();
        this.rnd = rnd;
    }

    public int[] reset() {
        return original.clone();
    }

    public int[] shuffle() {
        int[] a = original.clone();
        for (int i = a.length - 1; i > 0; i--) {
            int j = rnd.nextInt(i + 1);
            int t = a[i];
            a[i] = a[j];
            a[j] = t;
        }
        return a;
    }
}
