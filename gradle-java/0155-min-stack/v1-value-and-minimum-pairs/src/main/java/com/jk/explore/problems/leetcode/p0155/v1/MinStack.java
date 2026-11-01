package com.jk.explore.problems.leetcode.p0155.v1;

import java.util.*;

public class MinStack {

    private record Entry(int value, int min) { }

    private final Deque<Entry> stack = new ArrayDeque<>();

    public void push(int val) {
        int min = stack.isEmpty() ? val : Math.min(val, stack.peek().min());
        stack.push(new Entry(val, min));
    }

    public void pop() {
        stack.pop();
    }

    public int top() {
        return stack.peek().value();
    }

    public int getMin() {
        return stack.peek().min();
    }
}
