package com.jk.explore.problems.palindrome.number;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class PalindromeNumberTest {

    private PalindromeNumber palindromeNumber;

    @BeforeEach
    public void init() {
        palindromeNumber = new PalindromeNumber();
    }

    @Test
    public void isPalindromeTest() {
        assertTrue(palindromeNumber.isPalindrome(121));
        assertTrue(palindromeNumber.isPalindrome(2332));
        assertFalse(palindromeNumber.isPalindrome(23456));
    }

    @Test
    public void isPalindromeForNegativeNumber() {
        assertFalse(palindromeNumber.isPalindrome(-121));
        assertFalse(palindromeNumber.isPalindrome(-12345));
    }

}
