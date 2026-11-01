package com.jk.explore.problems.leetcode.p0220.v3;

import java.util.*;

public class ContainsDuplicateIII {

    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        long w = (long) valueDiff + 1;
        MyHashMap<Long, Long> buckets = new MyHashMap<>();
        for (int i = 0; i < nums.length; i++) {
            long v = nums[i], id = Math.floorDiv(v, w);
            if (buckets.containsKey(id)) return true;
            Long lo = buckets.get(id - 1), hi = buckets.get(id + 1);
            if (lo != null && v - lo <= valueDiff) return true;
            if (hi != null && hi - v <= valueDiff) return true;
            buckets.put(id, v);
            if (i >= indexDiff) buckets.remove(Math.floorDiv((long) nums[i - indexDiff], w));
        }
        return false;
    }
}
