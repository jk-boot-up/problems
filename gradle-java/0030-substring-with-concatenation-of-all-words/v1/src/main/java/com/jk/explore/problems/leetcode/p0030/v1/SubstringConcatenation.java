package com.jk.explore.problems.leetcode.p0030.v1;

import java.util.*;

public class SubstringConcatenation {

    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> out = new ArrayList<>();
        int L = words[0].length(), k = words.length;
        Map<String, Integer> need = new HashMap<>();
        for (String w : words) need.merge(w, 1, Integer::sum);
        for (int i = 0; i + k * L <= s.length(); i++) {
            Map<String, Integer> seen = new HashMap<>();
            int j = 0;
            for (; j < k; j++) {
                String w = s.substring(i + j * L, i + (j + 1) * L);
                if (seen.merge(w, 1, Integer::sum) > need.getOrDefault(w, 0)) break;
            }
            if (j == k) out.add(i);
        }
        return out;
    }
}
