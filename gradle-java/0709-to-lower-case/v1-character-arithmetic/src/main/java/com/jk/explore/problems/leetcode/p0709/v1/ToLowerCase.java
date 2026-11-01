package com.jk.explore.problems.leetcode.p0709.v1;

import java.util.*;

public class ToLowerCase {

    public String toLowerCase(String s) {
        char[] a = s.toCharArray();
        for (int i = 0; i < a.length; i++) {
            if (a[i] >= 'A' && a[i] <= 'Z') a[i] = (char) (a[i] + ('a' - 'A'));
        }
        return new String(a);
    }
}
