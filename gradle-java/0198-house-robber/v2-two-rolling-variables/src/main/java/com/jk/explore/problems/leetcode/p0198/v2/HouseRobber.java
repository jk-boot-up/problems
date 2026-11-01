package com.jk.explore.problems.leetcode.p0198.v2;

import java.util.*;

public class HouseRobber {

    public int rob(int[] nums) {
        int prev2 = 0, prev1 = 0;
        for (int x : nums) {
            int cur = Math.max(prev1, prev2 + x);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}
