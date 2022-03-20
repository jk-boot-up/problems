package com.jk.explore.problems.palindrome;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.List;

public class PalindromeProblemsTest {

    private PalindromeProblems pdProblem = new PalindromeProblems();

    @Test
    public void getAllSubStrings() {
        List<String> subStrings= pdProblem.getAllSubStrings("abcdef");
        for(String subString : subStrings) {
            System.out.println(subString);
        }
    }

    @Test
    public void isPalindrome() {
        Assertions.assertTrue(pdProblem.isPalindrome("aba"));
        Assertions.assertTrue(pdProblem.isPalindrome("abba"));
        Assertions.assertTrue(pdProblem.isPalindrome("abcddcba"));
        Assertions.assertTrue(pdProblem.isPalindrome("a"));
        Assertions.assertTrue(pdProblem.isPalindrome("abcdxyxdcba"));
        Assertions.assertTrue(pdProblem.isPalindrome("abcdxyyxdcba"));
    }

    @Test
    public void longestPalindrome() {
        String longestPalindrome = pdProblem.longestPalindrome("abcdxyabayxdcba");
        Assertions.assertEquals("abcdxyabayxdcba", longestPalindrome);
        longestPalindrome = pdProblem.longestPalindrome("abcdabxyzabaabccbabadcba");
        Assertions.assertEquals("abccba", longestPalindrome);
    }





}
