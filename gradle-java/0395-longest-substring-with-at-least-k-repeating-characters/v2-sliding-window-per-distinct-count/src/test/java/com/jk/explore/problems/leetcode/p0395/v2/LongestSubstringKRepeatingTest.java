package com.jk.explore.problems.leetcode.p0395.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestSubstringKRepeatingTest {

    private final LongestSubstringKRepeating solution = new LongestSubstringKRepeating();

    @ParameterizedTest
    @CsvSource({"aaabb,3,3", "ababbc,2,5", "a,2,0", "a,1,1", "bbaaacbd,3,3", "ababacb,3,0", "aaabbbcdd,3,6"})
    void longest(String s, int k, int expected) {
        assertEquals(expected, solution.longestSubstring(s, k));
    }
}
