package com.jk.explore.problems.leetcode.p0485.v1;

import java.util.*;

public class MaxConsecutiveOnes {

    public int findMaxConsecutiveOnes(int[] nums) {
        int run = 0, best = 0;
        for (int x : nums) {
            run = x == 1 ? run + 1 : 0;
            best = Math.max(best, run);
        }
        return best;
    }
}
