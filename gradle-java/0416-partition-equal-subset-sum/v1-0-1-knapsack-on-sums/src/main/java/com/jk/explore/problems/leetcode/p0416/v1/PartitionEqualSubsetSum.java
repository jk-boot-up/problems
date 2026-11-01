package com.jk.explore.problems.leetcode.p0416.v1;

import java.util.*;

public class PartitionEqualSubsetSum {

    public boolean canPartition(int[] nums) {
        int total = 0;
        for (int x : nums) total += x;
        if (total % 2 == 1) return false;
        int target = total / 2;
        boolean[] can = new boolean[target + 1];
        can[0] = true;
        for (int x : nums) {
            for (int s = target; s >= x; s--) can[s] |= can[s - x];
        }
        return can[target];
    }
}
