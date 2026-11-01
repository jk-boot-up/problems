package com.jk.explore.problems.leetcode.p0260.v1;

import java.util.*;

public class SingleNumberIII {

    public int[] singleNumber(int[] nums) {
        int x = 0;
        for (int v : nums) x ^= v;
        int bit = x & -x;
        int a = 0, b = 0;
        for (int v : nums) {
            if ((v & bit) != 0) a ^= v;
            else b ^= v;
        }
        return new int[]{a, b};
    }
}
