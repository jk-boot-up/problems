package com.jk.explore.problems.leetcode.p0318.v1;

import java.util.*;

public class MaxProductWordLengths {

    public int maxProduct(String[] words) {
        int n = words.length;
        int[] mask = new int[n];
        for (int i = 0; i < n; i++) for (char c : words[i].toCharArray()) mask[i] |= 1 << (c - 'a');
        int best = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                if ((mask[i] & mask[j]) == 0) best = Math.max(best, words[i].length() * words[j].length());
        return best;
    }
}
