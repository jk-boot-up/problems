package com.jk.explore.problems.leetcode.p0451.v1;

import java.util.*;

public class FrequencySort {

    public String frequencySort(String s) {
        int[] count = new int[128];
        for (char c : s.toCharArray()) count[c]++;
        List<List<Character>> buckets = new ArrayList<>();
        for (int i = 0; i <= s.length(); i++) buckets.add(new ArrayList<>());
        for (char c = 0; c < 128; c++) if (count[c] > 0) buckets.get(count[c]).add(c);
        StringBuilder sb = new StringBuilder(s.length());
        for (int f = s.length(); f > 0; f--)
            for (char c : buckets.get(f)) sb.repeat(c, f);
        return sb.toString();
    }
}
