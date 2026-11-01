package com.jk.explore.problems.leetcode.p0201.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RangeBitwiseAndTest {

    private final RangeBitwiseAnd solution = new RangeBitwiseAnd();

    @ParameterizedTest
    @CsvSource({"5,7,4", "0,0,0", "1,2147483647,0", "12,15,12", "6,6,6"})
    void ands(int left, int right, int expected) {
        assertEquals(expected, solution.rangeBitwiseAnd(left, right));
    }
}
