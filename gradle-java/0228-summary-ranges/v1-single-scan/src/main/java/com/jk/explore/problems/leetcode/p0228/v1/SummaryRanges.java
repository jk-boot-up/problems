package com.jk.explore.problems.leetcode.p0228.v1;

import java.util.*;

public class SummaryRanges {

    public List<String> summaryRanges(int[] nums) {
        List<String> out = new ArrayList<>();
        for (int i = 0; i < nums.length; ) {
            int j = i;
            while (j + 1 < nums.length && nums[j + 1] == nums[j] + 1) j++;
            out.add(i == j ? String.valueOf(nums[i]) : nums[i] + "->" + nums[j]);
            i = j + 1;
        }
        return out;
    }
}
