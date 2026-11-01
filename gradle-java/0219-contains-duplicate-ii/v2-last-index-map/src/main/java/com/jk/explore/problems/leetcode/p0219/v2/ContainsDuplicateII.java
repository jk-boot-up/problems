package com.jk.explore.problems.leetcode.p0219.v2;

import java.util.*;

public class ContainsDuplicateII {

    public boolean containsNearbyDuplicate(int[] nums, int k) {
        MyHashMap<Integer, Integer> last = new MyHashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer j = last.put(nums[i], i);
            if (j != null && i - j <= k) {
                return true;
            }
        }
        return false;
    }
}
