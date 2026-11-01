package com.jk.explore.problems.leetcode.p0172.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FactorialTrailingZeroesTest {

    private final FactorialTrailingZeroes solution = new FactorialTrailingZeroes();

    @ParameterizedTest
    @CsvSource({"3,0", "5,1", "0,0", "25,6", "100,24", "10000,2499"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.trailingZeroes(n));
    }
}
