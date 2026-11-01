package com.jk.explore.problems.leetcode.p0169.v1;

import java.util.*;

public class MajorityElement {

    public int majorityElement(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int x : nums) {
            if (count.merge(x, 1, Integer::sum) > nums.length / 2) {
                return x;
            }
        }
        throw new IllegalArgumentException("No majority element");
    }
}
