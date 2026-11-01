package com.jk.explore.problems.leetcode.p0128.v2;

import java.util.*;

public class LongestConsecutiveSequence {

    public int longestConsecutive(int[] nums) {
        MyHashSet<Integer> set = new MyHashSet<>();
        for (int x : nums) set.add(x);
        int best = 0;
        for (int x : set) {
            if (!set.contains(x - 1)) {
                int len = 1;
                while (set.contains(x + len)) len++;
                best = Math.max(best, len);
            }
        }
        return best;
    }
}
