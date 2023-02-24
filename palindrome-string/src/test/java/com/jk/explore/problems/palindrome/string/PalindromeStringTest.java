package com.jk.explore.problems.palindrome.string;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class PalindromeStringTest {

    private PalindromeString palindromeString;

    @BeforeEach
    public void init() {
        palindromeString = new PalindromeString();
    }

    @Test
    public void isPalindrome() {
        assertTrue(palindromeString.isPalindrome("abcdcba"));
        assertFalse(palindromeString.isPalindrome("xyz"));
        assertTrue(palindromeString.isPalindrome("abba"));
        assertTrue(palindromeString.isPalindrome("bob"));
    }

    @Test
    public void isPalindromeForNullAndEmpty() {
        assertFalse(palindromeString.isPalindrome(null));
        assertFalse(palindromeString.isPalindrome(""));
        assertFalse(palindromeString.isPalindrome("   "));
    }
}
