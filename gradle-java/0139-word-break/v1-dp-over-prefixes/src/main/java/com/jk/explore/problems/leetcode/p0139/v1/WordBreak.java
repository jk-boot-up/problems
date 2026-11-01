package com.jk.explore.problems.leetcode.p0139.v1;

import java.util.*;

public class WordBreak {

    public boolean wordBreak(String s, List<String> wordDict) {
        MyHashSet<String> words = new MyHashSet<>();
        int maxLen = 0;
        for (String w : wordDict) {
            words.add(w);
            maxLen = Math.max(maxLen, w.length());
        }
        boolean[] ok = new boolean[s.length() + 1];
        ok[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = i - 1; j >= Math.max(0, i - maxLen); j--) {
                if (ok[j] && words.contains(s.substring(j, i))) {
                    ok[i] = true;
                    break;
                }
            }
        }
        return ok[s.length()];
    }
}
