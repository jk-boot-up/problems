package com.jk.explore.problems.string.search;

import java.util.HashMap;
import java.util.Map;

public class SmallestSubstringWIthAllCharsInAnyOrder {

    public String shortestSubstringWindow(String text, String pattern) {
        Map<Character, Integer> patternCharCountMap = new HashMap<>();
        for(int i=0; i < pattern.length(); i++) {
            char current = pattern.charAt(i);
            int charCount = patternCharCountMap.getOrDefault(current, 0);
            patternCharCountMap.put(current, charCount + 1);
        }
        int leftIndex = 0;
        int rightIndex = 0;
        int charMatchCount = 0;
        int charMatchCountRequired = patternCharCountMap.size();
        int[] minWindow = new int[3];
        minWindow[0] = -1;
        minWindow[1] = leftIndex;
        minWindow[2] = rightIndex;
        Map<Character, Integer> charMatchTracker = new HashMap<>();
        while(rightIndex < text.length()) {
            char current = text.charAt(rightIndex);
            int charCount = charMatchTracker.getOrDefault(current, 0);
            charMatchTracker.put(current, charCount + 1);
            if(patternCharCountMap.containsKey(current) && patternCharCountMap.get(current) == charMatchTracker.get(current)) {
                charMatchCount ++;
            }
            while (leftIndex <= rightIndex && charMatchCount == charMatchCountRequired) {
                char leftChar = text.charAt(leftIndex);
                if(minWindow[0] == -1 ||  minWindow[0] > (rightIndex - leftIndex + 1)) {
                    minWindow[0] = (rightIndex - leftIndex + 1);
                    minWindow[1] = leftIndex;
                    minWindow[2] = rightIndex;
                }
                charMatchTracker.put(leftChar, charMatchTracker.get(leftChar) -1);
                if(patternCharCountMap.containsKey(leftChar)  && charMatchTracker.get(leftChar) < patternCharCountMap.get(leftChar)) {
                    charMatchCount--;
                }
                leftIndex = leftIndex + 1;
            }
            rightIndex++;
        }
        if(minWindow[0] == -1) {
            return "";
        } else {
            return text.substring(minWindow[1], minWindow[2] + 1);
        }

    }

}

/*
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 */
