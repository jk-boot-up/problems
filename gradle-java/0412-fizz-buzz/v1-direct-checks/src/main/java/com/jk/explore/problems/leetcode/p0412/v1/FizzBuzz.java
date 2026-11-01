package com.jk.explore.problems.leetcode.p0412.v1;

import java.util.*;

public class FizzBuzz {

    public List<String> fizzBuzz(int n) {
        List<String> out = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            String s = (i % 3 == 0 ? "Fizz" : "") + (i % 5 == 0 ? "Buzz" : "");
            out.add(s.isEmpty() ? String.valueOf(i) : s);
        }
        return out;
    }
}
