package com.jk.explore.problems.leetcode.p1365.v1;

import java.util.*;

public class SmallerThanCurrent {

    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] less = new int[102];
        for (int x : nums) less[x + 1]++;
        for (int v = 1; v < less.length; v++) less[v] += less[v - 1];
        int[] out = new int[nums.length];
        for (int i = 0; i < nums.length; i++) out[i] = less[nums[i]];
        return out;
    }
}
