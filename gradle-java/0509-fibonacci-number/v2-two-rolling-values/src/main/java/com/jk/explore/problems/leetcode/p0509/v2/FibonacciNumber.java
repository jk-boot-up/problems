package com.jk.explore.problems.leetcode.p0509.v2;

import java.util.*;

public class FibonacciNumber {

    public int fib(int n) {
        int a = 0, b = 1;
        for (int i = 0; i < n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return a;
    }
}
