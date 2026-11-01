package com.jk.explore.problems.leetcode.p0456.v2;

import java.util.*;

public class Pattern132 {

    public boolean find132pattern(int[] nums) {
        Deque<Integer> stack = new ArrayDeque<>();
        long third = Long.MIN_VALUE;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] < third) return true;
            while (!stack.isEmpty() && stack.peek() < nums[i]) third = stack.pop();
            stack.push(nums[i]);
        }
        return false;
    }
}
