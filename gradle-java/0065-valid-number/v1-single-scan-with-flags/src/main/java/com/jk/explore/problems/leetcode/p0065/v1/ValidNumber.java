package com.jk.explore.problems.leetcode.p0065.v1;

import java.util.*;

public class ValidNumber {

    public boolean isNumber(String s) {
        boolean digits = false, dot = false, exp = false;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                digits = true;
            } else if (c == '+' || c == '-') {
                if (i > 0 && s.charAt(i - 1) != 'e' && s.charAt(i - 1) != 'E') return false;
            } else if (c == '.') {
                if (dot || exp) return false;
                dot = true;
            } else if (c == 'e' || c == 'E') {
                if (exp || !digits) return false;
                exp = true;
                digits = false;
            } else {
                return false;
            }
        }
        return digits;
    }
}
