package com.jk.explore.problems.leetcode.p0029.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DivideTwoIntegersTest {

    private final DivideTwoIntegers solution = new DivideTwoIntegers();

    @ParameterizedTest
    @CsvSource({"10,3,3", "7,-3,-2", "-2147483648,-1,2147483647", "-2147483648,1,-2147483648", "1,1,1", "0,5,0", "2147483647,2,1073741823"})
    void divides(int a, int b, int expected) {
        assertEquals(expected, solution.divide(a, b));
    }
}
