package com.jk.explore.problems.leetcode.p0097.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class InterleavingStringTest {

    private final InterleavingString solution = new InterleavingString();

    @Test
    void examples() {
        assertTrue(solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"));
        assertFalse(solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"));
        assertTrue(solution.isInterleave("", "", ""));
    }

    @Test
    void lengthMismatch() {
        assertFalse(solution.isInterleave("a", "b", "a"));
    }
}
