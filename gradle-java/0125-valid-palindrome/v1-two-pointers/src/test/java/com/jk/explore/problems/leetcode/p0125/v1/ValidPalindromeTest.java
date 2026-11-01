package com.jk.explore.problems.leetcode.p0125.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ValidPalindromeTest {

    private final ValidPalindrome solution = new ValidPalindrome();

    @Test
    void sentencePalindrome() {
        assertTrue(solution.isPalindrome("A man, a plan, a canal: Panama"));
    }

    @Test
    void notPalindrome() {
        assertFalse(solution.isPalindrome("race a car"));
    }

    @Test
    void onlySpaces() {
        assertTrue(solution.isPalindrome(" "));
    }

    @Test
    void digitsMatter() {
        assertFalse(solution.isPalindrome("0P"));
    }
}
