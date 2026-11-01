package com.jk.explore.problems.leetcode.p0132.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PalindromePartitioningIITest {

    private final PalindromePartitioningII solution = new PalindromePartitioningII();

    @ParameterizedTest
    @CsvSource({"aab,1", "a,0", "ab,1", "abccba,0", "abacdc,1"})
    void cuts(String s, int expected) {
        assertEquals(expected, solution.minCut(s));
    }
}
