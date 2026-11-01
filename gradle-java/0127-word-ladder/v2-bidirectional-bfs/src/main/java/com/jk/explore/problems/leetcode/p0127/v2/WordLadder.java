package com.jk.explore.problems.leetcode.p0127.v2;

import java.util.*;

public class WordLadder {

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        MyHashSet<String> words = new MyHashSet<>();
        for (String w : wordList) words.add(w);
        if (!words.contains(endWord)) return 0;
        MyHashSet<String> front = new MyHashSet<>(), back = new MyHashSet<>();
        front.add(beginWord);
        back.add(endWord);
        words.remove(beginWord);
        words.remove(endWord);
        for (int length = 2; !front.isEmpty(); length++) {
            if (front.size() > back.size()) {
                MyHashSet<String> t = front; front = back; back = t;
            }
            MyHashSet<String> next = new MyHashSet<>();
            for (String w : front) {
                char[] chars = w.toCharArray();
                for (int i = 0; i < chars.length; i++) {
                    char original = chars[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        chars[i] = c;
                        String candidate = new String(chars);
                        if (back.contains(candidate)) return length;
                        if (words.remove(candidate)) next.add(candidate);
                    }
                    chars[i] = original;
                }
            }
            front = next;
        }
        return 0;
    }
}
