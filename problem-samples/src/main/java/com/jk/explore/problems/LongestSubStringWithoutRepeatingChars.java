package com.jk.explore.problems;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

public class LongestSubStringWithoutRepeatingChars {

    public int longestSubStringLength(String input) {
        if(input == null || input.length() == 0 || input.trim().length() == 0) {
            return -1;
        }
        int left = 0;
        int right = 0;
        int length = 0;
        Map<Character, Integer> charCountMap = new LinkedHashMap<>();
        while(right < input.length()) {
            Character currentChar = input.charAt(right);
            charCountMap.put(currentChar, charCountMap.getOrDefault(currentChar, 0) + 1);
            while(charCountMap.get(currentChar) > 1) {
                Character leftChar = input.charAt(left);
                charCountMap.put(leftChar, charCountMap.get(leftChar)-1);
                left++;
            }
            length = Math.max(length, right - left + 1);
            right++;
        }
        System.out.println("Longest sub string length is: " + length);
        return length;
    }

    public String getLongestSubstring(String input) {
        String longestSubstring = "";
        Map<Character, Integer> visitedCharAndIndex = new HashMap<>();
        for(int start = 0,end = 0; end < input.length(); end ++) {
            Character current = input.charAt(end);
            if(visitedCharAndIndex.containsKey(current)) {
                start = Math.max(visitedCharAndIndex.get(current)+1, start);
            }
            // it will faile for abcded
            if(longestSubstring.length() < end - start + 1) {
                longestSubstring = input.substring(start, end + 1);
            }
            visitedCharAndIndex.put(current, end);
        }
        return longestSubstring;
    }
}
