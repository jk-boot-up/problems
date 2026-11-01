package com.jk.explore.problems.leetcode.p0151.v1;

import java.util.*;

public class ReverseWords {

    public String reverseWords(String s) {
        List<String> words = Arrays.asList(s.trim().split("\\s+"));
        Collections.reverse(words);
        return String.join(" ", words);
    }
}
