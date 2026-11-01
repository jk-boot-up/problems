package com.jk.explore.problems.leetcode.p0127.v1;

import java.util.*;

public class WordLadder {

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        MyHashSet<String> words = new MyHashSet<>();
        for (String w : wordList) words.add(w);
        if (!words.contains(endWord)) return 0;
        Deque<String> queue = new ArrayDeque<>(List.of(beginWord));
        for (int length = 1; !queue.isEmpty(); length++) {
            for (int size = queue.size(); size > 0; size--) {
                String w = queue.poll();
                if (w.equals(endWord)) return length;
                char[] chars = w.toCharArray();
                for (int i = 0; i < chars.length; i++) {
                    char original = chars[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        chars[i] = c;
                        String candidate = new String(chars);
                        if (words.remove(candidate)) queue.add(candidate);
                    }
                    chars[i] = original;
                }
            }
        }
        return 0;
    }
}
