package com.jk.explore.problems.leetcode.p0459.v1;

import java.util.*;

public class RepeatedSubstringPattern {

    public boolean repeatedSubstringPattern(String s) {
        String doubled = s + s;
        return doubled.substring(1, doubled.length() - 1).contains(s);
    }
}
