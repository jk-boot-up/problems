package com.jk.explore.problems.leetcode.p0560.v1;

import java.util.*;

public class SubarraySumEqualsK {

    public int subarraySum(int[] nums, int k) {
        MyHashMap<Integer, Integer> seen = new MyHashMap<>();
        seen.put(0, 1);
        int sum = 0, count = 0;
        for (int x : nums) {
            sum += x;
            count += seen.getOrDefault(sum - k, 0);
            seen.merge(sum, 1, Integer::sum);
        }
        return count;
    }
}
