package com.jk.explore.problems.leetcode.p0503.v1;

import java.util.*;

public class NextGreaterElementII {

    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] out = new int[n];
        Arrays.fill(out, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < 2 * n; i++) {
            int x = nums[i % n];
            while (!stack.isEmpty() && nums[stack.peek()] < x) out[stack.pop()] = x;
            if (i < n) stack.push(i);
        }
        return out;
    }
}
