package com.jk.explore.problems.longest.substring;

import java.util.HashSet;
import java.util.Set;

public class LongestSubstring {

    public int findLengthOfLongestSubstring(String input) {
        Set<Character> characterSet = new HashSet<>();
        int maxLength = 0;
        int left = 0;
        int right = 0;
        while(right < input.length()) {
            if(characterSet.contains(input.charAt(right))) {
                while(input.charAt(left) != input.charAt(right)) {
                    characterSet.remove(input.charAt(left));
                    left++;
                }
                characterSet.remove(input.charAt(left));
                left++;
                characterSet.add(input.charAt(right));
                maxLength = Math.max(maxLength, right - left +1);
            } else {
                characterSet.add(input.charAt(right));
                maxLength = Math.max(maxLength, right - left +1);
            }
            right ++;
        }
        return maxLength;
    }
}
