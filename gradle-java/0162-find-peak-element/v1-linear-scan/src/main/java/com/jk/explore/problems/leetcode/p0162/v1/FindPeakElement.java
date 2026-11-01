package com.jk.explore.problems.leetcode.p0162.v1;

import java.util.*;

public class FindPeakElement {

    public int findPeakElement(int[] nums) {
        for (int i = 0; i + 1 < nums.length; i++) {
            if (nums[i] > nums[i + 1]) return i;
        }
        return nums.length - 1;
    }
}
