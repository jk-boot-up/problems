package com.jk.explore.problems.leetcode.p0424.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestRepeatingReplacementTest {

    private final LongestRepeatingReplacement solution = new LongestRepeatingReplacement();

    @ParameterizedTest
    @CsvSource({"ABAB,2,4", "AABABBA,1,4", "A,0,1", "ABCDE,1,2"})
    void lengths(String s, int k, int expected) {
        assertEquals(expected, solution.characterReplacement(s, k));
    }
}
