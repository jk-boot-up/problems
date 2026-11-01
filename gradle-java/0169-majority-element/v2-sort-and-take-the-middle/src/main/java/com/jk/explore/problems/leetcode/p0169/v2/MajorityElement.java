package com.jk.explore.problems.leetcode.p0169.v2;

import java.util.*;

public class MajorityElement {

    public int majorityElement(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        return sorted[sorted.length / 2];
    }
}
