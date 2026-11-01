package com.jk.explore.problems.leetcode.p0096.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class UniqueBSTsTest {

    private final UniqueBSTs solution = new UniqueBSTs();

    @ParameterizedTest
    @CsvSource({"1,1", "2,2", "3,5", "4,14", "19,1767263190"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.numTrees(n));
    }
}
