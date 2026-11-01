package com.jk.explore.problems.leetcode.p0456.v1;

import java.util.*;

public class Pattern132 {

    public boolean find132pattern(int[] nums) {
        int min = Integer.MAX_VALUE;
        for (int j = 0; j < nums.length; j++) {
            min = Math.min(min, nums[j]);
            for (int k = j + 1; k < nums.length; k++) if (min < nums[k] && nums[k] < nums[j]) return true;
        }
        return false;
    }
}
