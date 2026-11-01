package com.jk.explore.problems.leetcode.p0415.v1;

import java.util.*;

public class AddStrings {

    public String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        int i = num1.length() - 1, j = num2.length() - 1, carry = 0;
        while (i >= 0 || j >= 0 || carry > 0) {
            int sum = carry;
            if (i >= 0) sum += num1.charAt(i--) - '0';
            if (j >= 0) sum += num2.charAt(j--) - '0';
            sb.append((char) ('0' + sum % 10));
            carry = sum / 10;
        }
        return sb.reverse().toString();
    }
}
