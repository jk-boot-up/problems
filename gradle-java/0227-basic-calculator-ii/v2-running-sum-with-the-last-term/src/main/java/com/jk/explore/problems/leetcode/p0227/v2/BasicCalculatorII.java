package com.jk.explore.problems.leetcode.p0227.v2;

import java.util.*;

public class BasicCalculatorII {

    public int calculate(String s) {
        long result = 0, last = 0, num = 0;
        char op = '+';
        for (int i = 0; i <= s.length(); i++) {
            char c = i < s.length() ? s.charAt(i) : '+';
            if (c == ' ') continue;
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
                continue;
            }
            switch (op) {
                case '+' -> { result += last; last = num; }
                case '-' -> { result += last; last = -num; }
                case '*' -> last = last * num;
                default -> last = last / num;
            }
            op = c;
            num = 0;
        }
        return (int) (result + last);
    }
}
