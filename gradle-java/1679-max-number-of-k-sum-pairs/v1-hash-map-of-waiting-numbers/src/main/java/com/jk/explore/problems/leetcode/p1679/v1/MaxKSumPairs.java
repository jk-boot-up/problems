package com.jk.explore.problems.leetcode.p1679.v1;

import java.util.*;

public class MaxKSumPairs {

    public int maxOperations(int[] nums, int k) {
        MyHashMap<Integer, Integer> waiting = new MyHashMap<>();
        int ops = 0;
        for (int x : nums) {
            int partner = waiting.getOrDefault(k - x, 0);
            if (partner > 0) {
                waiting.put(k - x, partner - 1);
                ops++;
            } else {
                waiting.merge(x, 1, Integer::sum);
            }
        }
        return ops;
    }
}
