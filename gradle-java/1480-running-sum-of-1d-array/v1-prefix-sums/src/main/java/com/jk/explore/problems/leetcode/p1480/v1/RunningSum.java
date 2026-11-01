package com.jk.explore.problems.leetcode.p1480.v1;

import java.util.*;

public class RunningSum {

    public int[] runningSum(int[] nums) {
        int[] out = nums.clone();
        for (int i = 1; i < out.length; i++) out[i] += out[i - 1];
        return out;
    }
}
