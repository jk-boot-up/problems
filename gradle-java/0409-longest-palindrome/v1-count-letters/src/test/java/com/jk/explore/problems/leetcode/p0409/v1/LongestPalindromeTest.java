package com.jk.explore.problems.leetcode.p0409.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestPalindromeTest {

    private final LongestPalindrome solution = new LongestPalindrome();

    @ParameterizedTest
    @CsvSource({"abccccdd,7", "a,1", "Aa,1", "bb,2", "ccc,3", "abc,1", "aabbccdd,8"})
    void length(String s, int expected) {
        assertEquals(expected, solution.longestPalindrome(s));
    }
}
