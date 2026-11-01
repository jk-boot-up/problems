package com.jk.explore.problems.leetcode.p1512.v1;

import java.util.*;

public class NumberOfGoodPairs {

    public int numIdenticalPairs(int[] nums) {
        int[] seen = new int[101];
        int pairs = 0;
        for (int x : nums) pairs += seen[x]++;
        return pairs;
    }
}
