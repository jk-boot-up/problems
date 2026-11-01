package com.jk.explore.problems.leetcode.p0003.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestSubstringTest {

    private final LongestSubstring solution = new LongestSubstring();

    @ParameterizedTest
    @CsvSource(value = {"abcabcbb:3", "bbbbb:1", "pwwkew:3", "abba:2", "dvdf:3"}, delimiter = ':')
    void finds(String s, int expected) {
        assertEquals(expected, solution.lengthOfLongestSubstring(s));
    }

    @Test
    void empty() {
        assertEquals(0, solution.lengthOfLongestSubstring(""));
    }
}
