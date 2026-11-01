package com.jk.explore.problems.leetcode.p0594.v1;

import java.util.*;

public class LongestHarmoniousSubsequence {

    public int findLHS(int[] nums) {
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int x : nums) count.merge(x, 1, Integer::sum);
        int best = 0;
        for (MyHashMap.Entry<Integer, Integer> e : count.entries()) {
            Integer up = count.get(e.getKey() + 1);
            if (up != null) best = Math.max(best, e.getValue() + up);
        }
        return best;
    }
}
