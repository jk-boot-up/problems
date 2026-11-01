package com.jk.explore.problems.leetcode.p0367.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ValidPerfectSquareTest {

    private final ValidPerfectSquare solution = new ValidPerfectSquare();

    @ParameterizedTest
    @CsvSource({"1,true", "4,true", "16,true", "2147395600,true", "2,false", "14,false", "2147483647,false", "808201,true"})
    void check(int num, boolean expected) {
        assertEquals(expected, solution.isPerfectSquare(num));
    }
}
