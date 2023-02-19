package com.jk.explore.problems.palindrome.string;

public class PalindromeString {

    public boolean isPalindrome(String input) {
        if(input == null) {
            return false;
        }
        input = input.trim();
        if(input.length() == 0) {
            return false;
        }
        int left = 0;
        int right = input.length() - 1;
        while (left < right) {
            if(input.charAt(left) != input.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
