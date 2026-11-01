package com.jk.explore.problems.leetcode.p0682.v1;

import java.util.*;

public class BaseballGame {

    public int calPoints(String[] operations) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (String op : operations) {
            switch (op) {
                case "+" -> {
                    int top = stack.pop(), second = stack.peek();
                    stack.push(top);
                    stack.push(top + second);
                }
                case "D" -> stack.push(2 * stack.peek());
                case "C" -> stack.pop();
                default -> stack.push(Integer.parseInt(op));
            }
        }
        int sum = 0;
        for (int x : stack) sum += x;
        return sum;
    }
}
