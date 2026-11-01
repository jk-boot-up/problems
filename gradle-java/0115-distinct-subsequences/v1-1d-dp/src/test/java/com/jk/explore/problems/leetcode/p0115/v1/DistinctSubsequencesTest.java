package com.jk.explore.problems.leetcode.p0115.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DistinctSubsequencesTest {

    private final DistinctSubsequences solution = new DistinctSubsequences();

    @ParameterizedTest
    @CsvSource({"rabbbit,rabbit,3", "babgbag,bag,5", "abc,abcd,0", "aaa,a,3"})
    void counts(String s, String t, int expected) {
        assertEquals(expected, solution.numDistinct(s, t));
    }
}
