package com.jk.explore.problems.leetcode.p0060.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PermutationSequenceTest {

    private final PermutationSequence solution = new PermutationSequence();

    @ParameterizedTest
    @CsvSource({"3,3,213", "4,9,2314", "3,1,123", "3,6,321", "9,362880,987654321"})
    void finds(int n, int k, String expected) {
        assertEquals(expected, solution.getPermutation(n, k));
    }
}
