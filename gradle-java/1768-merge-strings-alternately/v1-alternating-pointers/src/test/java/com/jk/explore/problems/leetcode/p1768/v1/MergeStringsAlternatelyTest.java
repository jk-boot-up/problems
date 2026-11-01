package com.jk.explore.problems.leetcode.p1768.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MergeStringsAlternatelyTest {

    private final MergeStringsAlternately solution = new MergeStringsAlternately();

    @ParameterizedTest
    @CsvSource({"abc,pqr,apbqcr", "ab,pqrs,apbqrs", "abcd,pq,apbqcd"})
    void merges(String a, String b, String expected) {
        assertEquals(expected, solution.mergeAlternately(a, b));
    }
}
