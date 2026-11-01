package com.jk.explore.problems.leetcode.p1381.v1;

import java.util.*;

public class CustomStack {

    private final int[] stack, inc;
    private int size;

    public CustomStack(int maxSize) {
        stack = new int[maxSize];
        inc = new int[maxSize];
    }

    public void push(int x) {
        if (size < stack.length) stack[size++] = x;
    }

    public int pop() {
        if (size == 0) return -1;
        int i = --size, v = stack[i] + inc[i];
        if (i > 0) inc[i - 1] += inc[i];
        inc[i] = 0;
        return v;
    }

    public void increment(int k, int val) {
        int top = Math.min(k, size) - 1;
        if (top >= 0) inc[top] += val;
    }
}
