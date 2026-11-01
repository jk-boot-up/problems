package com.jk.explore.problems.leetcode.p0001.v2;

import java.util.*;

public class TwoSum {

    public int[] twoSum(int[] nums, int target) {
        MyHashMap<Integer, Integer> seen = new MyHashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer j = seen.get(target - nums[i]);
            if (j != null) {
                return new int[]{j, i};
            }
            seen.put(nums[i], i);
        }
        throw new IllegalArgumentException("No solution");
    }
}
