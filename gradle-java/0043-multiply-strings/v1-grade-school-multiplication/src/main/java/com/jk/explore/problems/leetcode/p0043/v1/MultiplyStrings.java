package com.jk.explore.problems.leetcode.p0043.v1;

import java.util.*;

public class MultiplyStrings {

    public String multiply(String num1, String num2) {
        int m = num1.length(), n = num2.length();
        int[] pos = new int[m + n];
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int sum = (num1.charAt(i) - '0') * (num2.charAt(j) - '0') + pos[i + j + 1];
                pos[i + j + 1] = sum % 10;
                pos[i + j] += sum / 10;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int d : pos) if (!(sb.isEmpty() && d == 0)) sb.append(d);
        return sb.isEmpty() ? "0" : sb.toString();
    }
}
