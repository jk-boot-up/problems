package com.jk.explore.problems.leetcode.p0747.v1;

import java.util.*;

public class LargestAtLeastTwice {

    public int dominantIndex(int[] nums) {
        int best = -1, second = -1, idx = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > best) {
                second = best;
                best = nums[i];
                idx = i;
            } else if (nums[i] > second) {
                second = nums[i];
            }
        }
        return best >= 2 * second ? idx : -1;
    }
}
