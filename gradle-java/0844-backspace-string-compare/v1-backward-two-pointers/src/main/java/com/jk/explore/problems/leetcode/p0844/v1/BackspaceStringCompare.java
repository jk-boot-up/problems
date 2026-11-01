package com.jk.explore.problems.leetcode.p0844.v1;

import java.util.*;

public class BackspaceStringCompare {

    public boolean backspaceCompare(String s, String t) {
        int i = s.length() - 1, j = t.length() - 1;
        while (true) {
            i = nextValid(s, i);
            j = nextValid(t, j);
            if (i < 0 || j < 0) return i < 0 && j < 0;
            if (s.charAt(i--) != t.charAt(j--)) return false;
        }
    }

    /** Index of the next character (from the right) that survives the backspaces, or -1. */
    private static int nextValid(String s, int i) {
        int skip = 0;
        while (i >= 0) {
            if (s.charAt(i) == '#') skip++;
            else if (skip > 0) skip--;
            else break;
            i--;
        }
        return i;
    }
}
