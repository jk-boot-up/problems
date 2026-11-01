package com.jk.explore.problems.leetcode.p0204.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CountPrimesTest {

    private final CountPrimes solution = new CountPrimes();

    @ParameterizedTest
    @CsvSource({"0,0", "1,0", "2,0", "3,1", "10,4", "11,4", "12,5", "100,25", "10000,1229"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.countPrimes(n));
    }
}
