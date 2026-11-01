package com.jk.explore.problems.leetcode.p0227.v1;

import java.util.*;

public class BasicCalculatorII {

    public int calculate(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        int num = 0;
        char op = '+';
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) num = num * 10 + (c - '0');
            if ((!Character.isDigit(c) && c != ' ') || i == s.length() - 1) {
                switch (op) {
                    case '+' -> stack.push(num);
                    case '-' -> stack.push(-num);
                    case '*' -> stack.push(stack.pop() * num);
                    default -> stack.push(stack.pop() / num);
                }
                op = c;
                num = 0;
            }
        }
        int sum = 0;
        for (int v : stack) sum += v;
        return sum;
    }
}
