package com.jk.explore.problems.leetcode.p0169.v3;

import java.util.*;

public class MajorityElement {

    public int majorityElement(int[] nums) {
        int candidate = 0, count = 0;
        for (int x : nums) {
            if (count == 0) {
                candidate = x;
            }
            count += (x == candidate) ? 1 : -1;
        }
        return candidate;
    }
}
