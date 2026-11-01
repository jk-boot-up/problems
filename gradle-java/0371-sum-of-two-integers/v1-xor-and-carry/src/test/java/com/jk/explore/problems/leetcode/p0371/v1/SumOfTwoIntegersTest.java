package com.jk.explore.problems.leetcode.p0371.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SumOfTwoIntegersTest {

    private final SumOfTwoIntegers solution = new SumOfTwoIntegers();

    @ParameterizedTest
    @CsvSource({"1,2,3", "2,3,5", "-1,1,0", "-12,-8,-20", "1000,-999,1"})
    void sums(int a, int b, int expected) {
        assertEquals(expected, solution.getSum(a, b));
    }
}
