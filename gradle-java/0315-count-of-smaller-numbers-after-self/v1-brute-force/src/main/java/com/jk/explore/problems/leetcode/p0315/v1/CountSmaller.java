package com.jk.explore.problems.leetcode.p0315.v1;

import java.util.*;

public class CountSmaller {

    public List<Integer> countSmaller(int[] nums) {
        List<Integer> out = new ArrayList<>(nums.length);
        for (int i = 0; i < nums.length; i++) {
            int c = 0;
            for (int j = i + 1; j < nums.length; j++) if (nums[j] < nums[i]) c++;
            out.add(c);
        }
        return out;
    }
}
