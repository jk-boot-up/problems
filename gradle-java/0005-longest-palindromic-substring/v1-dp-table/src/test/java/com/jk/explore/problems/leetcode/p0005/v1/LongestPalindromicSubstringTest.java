package com.jk.explore.problems.leetcode.p0005.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestPalindromicSubstringTest {

    private final LongestPalindromicSubstring solution = new LongestPalindromicSubstring();

    @Test
    void odd() {
        assertTrue(Set.of("bab", "aba").contains(solution.longestPalindrome("babad")));
    }

    @Test
    void even() {
        assertEquals("bb", solution.longestPalindrome("cbbd"));
    }

    @Test
    void whole() {
        assertEquals("racecar", solution.longestPalindrome("racecar"));
        assertEquals("a", solution.longestPalindrome("a"));
    }
}
