package com.jk.explore.problems.leetcode.p0027.v1;

import java.util.*;

public class RemoveElement {

    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int x : nums) {
            if (x != val) {
                nums[k++] = x;
            }
        }
        return k;
    }
}
