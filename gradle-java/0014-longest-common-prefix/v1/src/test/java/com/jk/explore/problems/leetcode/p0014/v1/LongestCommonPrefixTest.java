package com.jk.explore.problems.leetcode.p0014.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestCommonPrefixTest {

    private final LongestCommonPrefix solution = new LongestCommonPrefix();

    @Test
    void sharedPrefix() {
        assertEquals("fl", solution.longestCommonPrefix(new String[]{"flower", "flow", "flight"}));
    }

    @Test
    void noPrefix() {
        assertEquals("", solution.longestCommonPrefix(new String[]{"dog", "racecar", "car"}));
    }

    @Test
    void singleString() {
        assertEquals("alone", solution.longestCommonPrefix(new String[]{"alone"}));
    }

    @Test
    void oneIsPrefixOfOther() {
        assertEquals("ab", solution.longestCommonPrefix(new String[]{"abc", "ab"}));
    }
}
