package com.jk.explore.problems.longest.substring;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class LongestSubstringTest {

    private LongestSubstring longestSubstring;

    @BeforeEach
    void setUp() {
        longestSubstring = new LongestSubstring();
    }

    @Test
    void test1() {
        int actual = longestSubstring.findLengthOfLongestSubstring("abcabcbb");
        Assertions.assertEquals(3, actual);
    }
}
