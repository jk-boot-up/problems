package com.jk.explore.problems.leetcode.p0026.v1;

import java.util.*;

public class RemoveDuplicates {

    public int removeDuplicates(int[] nums) {
        int k = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[k - 1]) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
}
