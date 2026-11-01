package com.jk.explore.problems.leetcode.p0076.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinimumWindowSubstringTest {

    private final MinimumWindowSubstring solution = new MinimumWindowSubstring();

    @ParameterizedTest
    @CsvSource(value = {"ADOBECODEBANC:ABC:BANC", "a:a:a", "a:aa:''", "ab:b:b", "aaflslflsldkalskaaa:aaa:aaa"}, delimiter = ':')
    void finds(String s, String t, String expected) {
        assertEquals(expected, solution.minWindow(s, t));
    }
}
