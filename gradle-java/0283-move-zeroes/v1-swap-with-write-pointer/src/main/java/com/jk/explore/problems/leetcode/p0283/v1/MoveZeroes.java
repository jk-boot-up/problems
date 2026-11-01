package com.jk.explore.problems.leetcode.p0283.v1;

import java.util.*;

public class MoveZeroes {

    public void moveZeroes(int[] nums) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int t = nums[k];
                nums[k++] = nums[i];
                nums[i] = t;
            }
        }
    }
}
