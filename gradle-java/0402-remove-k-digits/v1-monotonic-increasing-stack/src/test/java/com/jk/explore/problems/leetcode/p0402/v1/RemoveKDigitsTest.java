package com.jk.explore.problems.leetcode.p0402.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RemoveKDigitsTest {

    private final RemoveKDigits solution = new RemoveKDigits();

    @ParameterizedTest
    @CsvSource({"1432219,3,1219", "10200,1,200", "10,2,0", "112,1,11", "9,1,0", "123456,3,123", "100,1,0", "5337,2,33"})
    void smallest(String num, int k, String expected) {
        assertEquals(expected, solution.removeKdigits(num, k));
    }
}
