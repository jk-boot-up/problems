package com.jk.explore.problems.leetcode.p0516.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestPalindromicSubsequenceTest {

    private final LongestPalindromicSubsequence solution = new LongestPalindromicSubsequence();

    @ParameterizedTest
    @CsvSource({"bbbab,4", "cbbd,2", "a,1", "character,5"})
    void lengths(String s, int expected) {
        assertEquals(expected, solution.longestPalindromeSubseq(s));
    }
}
