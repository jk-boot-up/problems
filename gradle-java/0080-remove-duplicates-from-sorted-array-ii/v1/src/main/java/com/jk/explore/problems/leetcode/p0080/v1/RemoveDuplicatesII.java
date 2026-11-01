package com.jk.explore.problems.leetcode.p0080.v1;

import java.util.*;

public class RemoveDuplicatesII {

    public int removeDuplicates(int[] nums) {
        int k = 0;
        for (int x : nums) {
            if (k < 2 || x != nums[k - 2]) {
                nums[k++] = x;
            }
        }
        return k;
    }
}
