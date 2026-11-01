package com.jk.explore.problems.leetcode.p0279.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PerfectSquaresTest {

    private final PerfectSquares solution = new PerfectSquares();

    @ParameterizedTest
    @CsvSource({"12,3", "13,2", "1,1", "16,1", "7,4"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.numSquares(n));
    }
}
