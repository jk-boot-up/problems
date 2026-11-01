package com.jk.explore.problems.leetcode.p0225.v1;

import java.util.*;

public class MyStack {

    private final Deque<Integer> queue = new ArrayDeque<>();

    public void push(int x) {
        queue.addLast(x);
        for (int i = 1; i < queue.size(); i++) queue.addLast(queue.pollFirst());
    }

    public int pop() {
        return queue.pollFirst();
    }

    public int top() {
        return queue.peekFirst();
    }

    public boolean empty() {
        return queue.isEmpty();
    }
}
