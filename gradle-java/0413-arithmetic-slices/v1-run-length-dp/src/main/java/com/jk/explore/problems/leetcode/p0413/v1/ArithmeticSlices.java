package com.jk.explore.problems.leetcode.p0413.v1;

import java.util.*;

public class ArithmeticSlices {

    public int numberOfArithmeticSlices(int[] nums) {
        int total = 0, cur = 0;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) total += ++cur;
            else cur = 0;
        }
        return total;
    }
}
