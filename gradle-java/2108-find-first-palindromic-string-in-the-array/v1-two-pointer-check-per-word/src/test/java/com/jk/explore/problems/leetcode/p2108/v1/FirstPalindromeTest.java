package com.jk.explore.problems.leetcode.p2108.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FirstPalindromeTest {

    private final FirstPalindrome solution = new FirstPalindrome();

    @Test
    void examples() {
        assertEquals("ada", solution.firstPalindrome(new String[]{"abc", "car", "ada", "racecar", "cool"}));
        assertEquals("racecar", solution.firstPalindrome(new String[]{"notapalindrome", "racecar"}));
        assertEquals("", solution.firstPalindrome(new String[]{"def", "ghi"}));
        assertEquals("a", solution.firstPalindrome(new String[]{"ab", "a"}));
    }
}
