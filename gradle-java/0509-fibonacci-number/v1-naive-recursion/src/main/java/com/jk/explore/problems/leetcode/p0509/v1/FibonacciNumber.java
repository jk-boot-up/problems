package com.jk.explore.problems.leetcode.p0509.v1;

import java.util.*;

public class FibonacciNumber {

    public int fib(int n) {
        return n < 2 ? n : fib(n - 1) + fib(n - 2);
    }
}
