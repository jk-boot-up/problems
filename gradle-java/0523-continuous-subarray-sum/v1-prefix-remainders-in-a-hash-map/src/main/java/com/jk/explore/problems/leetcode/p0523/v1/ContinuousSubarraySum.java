package com.jk.explore.problems.leetcode.p0523.v1;

import java.util.*;

public class ContinuousSubarraySum {

    public boolean checkSubarraySum(int[] nums, int k) {
        MyHashMap<Long, Integer> first = new MyHashMap<>();
        first.put(0L, -1);
        long mod = 0;
        for (int i = 0; i < nums.length; i++) {
            mod = (mod + nums[i]) % k;
            Integer j = first.get(mod);
            if (j == null) first.put(mod, i);
            else if (i - j >= 2) return true;
        }
        return false;
    }
}
