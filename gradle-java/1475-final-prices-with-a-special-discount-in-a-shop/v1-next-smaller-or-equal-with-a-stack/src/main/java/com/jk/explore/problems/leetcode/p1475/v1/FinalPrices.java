package com.jk.explore.problems.leetcode.p1475.v1;

import java.util.*;

public class FinalPrices {

    public int[] finalPrices(int[] prices) {
        int[] out = prices.clone();
        Deque<Integer> stack = new ArrayDeque<>();
        for (int j = 0; j < prices.length; j++) {
            while (!stack.isEmpty() && prices[stack.peek()] >= prices[j]) out[stack.pop()] -= prices[j];
            stack.push(j);
        }
        return out;
    }
}
