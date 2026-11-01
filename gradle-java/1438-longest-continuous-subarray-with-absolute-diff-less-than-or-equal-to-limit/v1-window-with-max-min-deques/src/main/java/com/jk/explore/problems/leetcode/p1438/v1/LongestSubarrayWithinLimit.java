package com.jk.explore.problems.leetcode.p1438.v1;

import java.util.*;

public class LongestSubarrayWithinLimit {

    public int longestSubarray(int[] nums, int limit) {
        Deque<Integer> maxQ = new ArrayDeque<>(), minQ = new ArrayDeque<>();
        int lo = 0, best = 0;
        for (int hi = 0; hi < nums.length; hi++) {
            int v = nums[hi];
            while (!maxQ.isEmpty() && maxQ.peekLast() < v) maxQ.pollLast();
            while (!minQ.isEmpty() && minQ.peekLast() > v) minQ.pollLast();
            maxQ.addLast(v);
            minQ.addLast(v);
            while (maxQ.peekFirst() - minQ.peekFirst() > limit) {
                if (maxQ.peekFirst() == nums[lo]) maxQ.pollFirst();
                if (minQ.peekFirst() == nums[lo]) minQ.pollFirst();
                lo++;
            }
            best = Math.max(best, hi - lo + 1);
        }
        return best;
    }
}
