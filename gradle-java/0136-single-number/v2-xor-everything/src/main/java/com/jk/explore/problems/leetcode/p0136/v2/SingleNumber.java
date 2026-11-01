package com.jk.explore.problems.leetcode.p0136.v2;

import java.util.*;

public class SingleNumber {

    public int singleNumber(int[] nums) {
        int x = 0;
        for (int v : nums) x ^= v;
        return x;
    }
}
