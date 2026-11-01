package com.jk.explore.problems.leetcode.p0220.v2;

import java.util.*;

public class ContainsDuplicateIII {

    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        TreeSet<Long> window = new TreeSet<>();
        for (int i = 0; i < nums.length; i++) {
            long v = nums[i];
            Long c = window.ceiling(v - valueDiff);
            if (c != null && c <= v + valueDiff) return true;
            window.add(v);
            if (i >= indexDiff) window.remove((long) nums[i - indexDiff]);
        }
        return false;
    }
}
