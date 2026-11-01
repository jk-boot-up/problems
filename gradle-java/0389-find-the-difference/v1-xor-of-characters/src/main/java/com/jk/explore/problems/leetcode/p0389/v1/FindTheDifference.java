package com.jk.explore.problems.leetcode.p0389.v1;

import java.util.*;

public class FindTheDifference {

    public char findTheDifference(String s, String t) {
        int x = 0;
        for (char c : s.toCharArray()) x ^= c;
        for (char c : t.toCharArray()) x ^= c;
        return (char) x;
    }
}
