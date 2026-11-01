package com.jk.explore.problems.leetcode.p0326.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PowerOfThreeTest {

    private final PowerOfThree solution = new PowerOfThree();

    @ParameterizedTest
    @CsvSource({"1,true", "3,true", "27,true", "1162261467,true", "0,false", "-1,false", "-27,false", "45,false", "6,false", "2147483647,false"})
    void check(int n, boolean expected) {
        assertEquals(expected, solution.isPowerOfThree(n));
    }
}
