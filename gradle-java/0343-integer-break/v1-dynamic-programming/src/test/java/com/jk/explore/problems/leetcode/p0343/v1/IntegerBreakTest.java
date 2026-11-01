package com.jk.explore.problems.leetcode.p0343.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class IntegerBreakTest {

    private final IntegerBreak solution = new IntegerBreak();

    @ParameterizedTest
    @CsvSource({"2,1", "3,2", "4,4", "5,6", "6,9", "7,12", "8,18", "10,36", "58,1549681956"})
    void products(int n, int expected) {
        assertEquals(expected, solution.integerBreak(n));
    }
}
