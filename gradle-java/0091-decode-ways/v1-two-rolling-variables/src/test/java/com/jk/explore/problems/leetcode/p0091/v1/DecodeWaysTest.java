package com.jk.explore.problems.leetcode.p0091.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DecodeWaysTest {

    private final DecodeWays solution = new DecodeWays();

    @ParameterizedTest
    @CsvSource({"12,2", "226,3", "06,0", "10,1", "2101,1", "11106,2"})
    void counts(String s, int expected) {
        assertEquals(expected, solution.numDecodings(s));
    }
}
