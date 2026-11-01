package com.jk.explore.problems.leetcode.p0290.v1;

import java.util.*;

public class WordPattern {

    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if (words.length != pattern.length()) return false;
        MyHashMap<Character, String> letterToWord = new MyHashMap<>();
        MyHashMap<String, Character> wordToLetter = new MyHashMap<>();
        for (int i = 0; i < words.length; i++) {
            char c = pattern.charAt(i);
            String w = words[i];
            String mapped = letterToWord.putIfAbsent(c, w);
            Character back = wordToLetter.putIfAbsent(w, c);
            if ((mapped != null && !mapped.equals(w)) || (back != null && back != c)) return false;
        }
        return true;
    }
}
