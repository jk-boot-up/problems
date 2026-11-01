package com.jk.explore.problems.leetcode.p1137.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TribonacciTest {

    private final Tribonacci solution = new Tribonacci();

    @ParameterizedTest
    @CsvSource({"0,0", "1,1", "2,1", "4,4", "25,1389537", "37,2082876103"})
    void values(int n, int expected) {
        assertEquals(expected, solution.tribonacci(n));
    }
}
