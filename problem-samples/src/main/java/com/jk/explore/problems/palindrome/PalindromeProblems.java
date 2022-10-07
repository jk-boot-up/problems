package com.jk.explore.problems.palindrome;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PalindromeProblems {

    public PalindromeProblems() {

    }

    public List<String> getAllSubStrings(String text) {
        if(text == null || text.length() == 0) {
            return null;
        }
        List<String> subStrings = new ArrayList<>();
        for(int i=0; i < text.length(); i++) {
            for(int j=i; j < text.length(); j++) {
                String subString = text.substring(i, j+1);
                subStrings.add(subString);
            }
        }
        return subStrings;
    }

    public boolean isPalindrome(String string) {
        if(string == null || string.trim().length() == 0) {
            return false;
        }
        int length = string.length();
        for(int i=0; i < (length/2); i++) {
            int targetIndex = length -1 - i;
            if(string.charAt(i) != string.charAt(targetIndex)) {
                return false;
            }
        }
        return true;
    }

    public String longestPalindrome(String string) {
        List<String> allSubStrings = getAllSubStrings(string);
        Map<String, Integer> palindromes = new HashMap<>();
        String largestPalindrome = null;
        for(String subString : allSubStrings) {
            String currentPalindrome = null;
            if(isPalindrome(subString)) {
                currentPalindrome = subString;
                if(largestPalindrome == null || largestPalindrome.length() < currentPalindrome.length()) {
                    largestPalindrome = currentPalindrome;
                }
            }
        }
        return largestPalindrome;
    }
}

/*    Given a string s, return the longest palindromic substring in s.

        Example 1:

        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.
        Example 2:

        Input: s = "cbbd"
        Output: "bb"
        Constraints:
        1 <= s.length <= 1000
        s consist of only digits and English letters

 */