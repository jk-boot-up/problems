package com.jk.explore.problems.samples.substrings.level.one;

import java.util.HashSet;
import java.util.Set;

public class LongestSubString {

    public int getLongestSubStringWithoutRepetitiveCharacter(String input) {
        return lengthOfLongestUniqueSubString(input);
    }

    private int lengthOfLongestUniqueSubString(String inputString) {
        int inputLength = inputString.length();
        int longestUniqueSubStringLength = 0;
        for (int i = 0; i < inputLength; i++)
            for (int j = i + 1; j <= inputLength; j++)
                if (isUnique(inputString, i, j))
                    longestUniqueSubStringLength = Math.max(longestUniqueSubStringLength, j - i);
        return longestUniqueSubStringLength;
    }

    private boolean isUnique(String in, int startIndex, int endIndex) {
        if(in == null || in.length() == 0)
            return true;
        Set<Character> characterSet = new HashSet<>();
        for(int i=startIndex; i < endIndex; i++) {
            Character currentChar = in.charAt(i);
            if (characterSet.contains(currentChar)) {
                return false;
            }
        }
        return true;
    }

    private int solution(String input) {
        if(input == null || input.length() == 0)
            return 0;
        int inputLength = input.length();
        int maxUniqueSubStringLength = 0;
        for(int begin = 0; begin < inputLength; begin++) {
            for(int end = begin+1; end <= inputLength; end++) {
                boolean isUniqueSubString = isUnique(input, begin, end);
                if(isUniqueSubString) {
                    maxUniqueSubStringLength = Math.max(maxUniqueSubStringLength, (end - begin));
                }
            }
        }
        return 0;
    }
}
