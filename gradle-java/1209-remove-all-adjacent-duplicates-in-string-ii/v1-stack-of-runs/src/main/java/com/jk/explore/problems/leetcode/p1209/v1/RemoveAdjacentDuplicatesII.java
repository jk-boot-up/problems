package com.jk.explore.problems.leetcode.p1209.v1;

import java.util.*;

public class RemoveAdjacentDuplicatesII {

    public String removeDuplicates(String s, int k) {
        char[] letter = new char[s.length()];
        int[] count = new int[s.length()];
        int top = -1;
        for (char c : s.toCharArray()) {
            if (top >= 0 && letter[top] == c) {
                if (++count[top] == k) top--;
            } else {
                letter[++top] = c;
                count[top] = 1;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= top; i++) sb.repeat(letter[i], count[i]);
        return sb.toString();
    }
}
