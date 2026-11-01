package com.jk.explore.problems.leetcode.p0140.v1;

import java.util.*;

public class WordBreakII {

    private final MyHashMap<Integer, List<String>> memo = new MyHashMap<>();
    private MyHashSet<String> dict;

    public List<String> wordBreak(String s, List<String> wordDict) {
        dict = new MyHashSet<>();
        for (String w : wordDict) dict.add(w);
        return sentences(s, 0);
    }

    private List<String> sentences(String s, int i) {
        List<String> cached = memo.get(i);
        if (cached != null) return cached;
        List<String> out = new ArrayList<>();
        if (i == s.length()) out.add("");
        for (int j = i + 1; j <= s.length(); j++) {
            String word = s.substring(i, j);
            if (!dict.contains(word)) continue;
            for (String rest : sentences(s, j)) out.add(rest.isEmpty() ? word : word + " " + rest);
        }
        memo.put(i, out);
        return out;
    }
}
