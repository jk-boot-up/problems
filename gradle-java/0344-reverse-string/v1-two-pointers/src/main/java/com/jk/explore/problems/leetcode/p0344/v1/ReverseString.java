package com.jk.explore.problems.leetcode.p0344.v1;

import java.util.*;

public class ReverseString {

    public void reverseString(char[] s) {
        for (int l = 0, r = s.length - 1; l < r; l++, r--) {
            char t = s[l];
            s[l] = s[r];
            s[r] = t;
        }
    }
}
