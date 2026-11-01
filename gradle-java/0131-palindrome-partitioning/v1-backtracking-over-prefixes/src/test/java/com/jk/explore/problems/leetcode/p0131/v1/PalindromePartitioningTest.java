package com.jk.explore.problems.leetcode.p0131.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PalindromePartitioningTest {

    private final PalindromePartitioning solution = new PalindromePartitioning();

    @Test
    void aab() {
        assertEquals(List.of(List.of("a", "a", "b"), List.of("aa", "b")), solution.partition("aab"));
    }

    @Test
    void single() {
        assertEquals(List.of(List.of("a")), solution.partition("a"));
    }
}
