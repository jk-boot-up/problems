package com.jk.explore.problems.leetcode.p1143.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestCommonSubsequenceTest {

    private final LongestCommonSubsequence solution = new LongestCommonSubsequence();

    @ParameterizedTest
    @CsvSource({"abcde,ace,3", "abc,abc,3", "abc,def,0", "bsbininm,jmjkbkjkv,1"})
    void lengths(String a, String b, int expected) {
        assertEquals(expected, solution.longestCommonSubsequence(a, b));
    }
}
