package com.jk.explore.problems.leetcode.p0647.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PalindromicSubstringsTest {

    private final PalindromicSubstrings solution = new PalindromicSubstrings();

    @ParameterizedTest
    @CsvSource({"abc,3", "aaa,6", "a,1", "abba,6"})
    void counts(String s, int expected) {
        assertEquals(expected, solution.countSubstrings(s));
    }
}
