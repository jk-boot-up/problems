package com.jk.explore.problems.leetcode.p0342.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PowerOfFourTest {

    private final PowerOfFour solution = new PowerOfFour();

    @ParameterizedTest
    @CsvSource({"1,true", "4,true", "16,true", "1073741824,true", "2,false", "8,false", "5,false", "0,false", "-4,false", "-2147483648,false"})
    void check(int n, boolean expected) {
        assertEquals(expected, solution.isPowerOfFour(n));
    }
}
