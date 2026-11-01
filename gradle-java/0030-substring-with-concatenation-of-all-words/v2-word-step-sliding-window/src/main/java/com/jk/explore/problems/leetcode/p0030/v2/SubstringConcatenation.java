package com.jk.explore.problems.leetcode.p0030.v2;

import java.util.*;

public class SubstringConcatenation {

    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> out = new ArrayList<>();
        int L = words[0].length(), k = words.length, n = s.length();
        MyHashMap<String, Integer> need = new MyHashMap<>();
        for (String w : words) need.merge(w, 1, Integer::sum);
        for (int offset = 0; offset < L; offset++) {
            MyHashMap<String, Integer> have = new MyHashMap<>();
            int left = offset, count = 0;
            for (int right = offset; right + L <= n; right += L) {
                String w = s.substring(right, right + L);
                if (!need.containsKey(w)) {
                    have.clear();
                    count = 0;
                    left = right + L;
                    continue;
                }
                have.merge(w, 1, Integer::sum);
                count++;
                while (have.get(w) > need.get(w)) {
                    have.merge(s.substring(left, left + L), -1, Integer::sum);
                    left += L;
                    count--;
                }
                if (count == k) {
                    out.add(left);
                    have.merge(s.substring(left, left + L), -1, Integer::sum);
                    left += L;
                    count--;
                }
            }
        }
        Collections.sort(out);
        return out;
    }
}
