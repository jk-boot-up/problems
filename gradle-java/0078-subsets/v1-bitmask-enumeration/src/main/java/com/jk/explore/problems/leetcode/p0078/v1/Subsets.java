package com.jk.explore.problems.leetcode.p0078.v1;

import java.util.*;

public class Subsets {

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> out = new ArrayList<>();
        for (int mask = 0; mask < (1 << nums.length); mask++) {
            List<Integer> s = new ArrayList<>();
            for (int i = 0; i < nums.length; i++) {
                if ((mask >> i & 1) == 1) s.add(nums[i]);
            }
            out.add(s);
        }
        return out;
    }
}
