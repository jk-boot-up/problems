package com.jk.explore.problems.leetcode.p0231.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PowerOfTwoTest {

    private final PowerOfTwo solution = new PowerOfTwo();

    @ParameterizedTest
    @CsvSource({"1,true", "2,true", "16,true", "1073741824,true", "3,false", "0,false", "-16,false", "-2147483648,false", "2147483647,false"})
    void check(int n, boolean expected) {
        assertEquals(expected, solution.isPowerOfTwo(n));
    }
}
