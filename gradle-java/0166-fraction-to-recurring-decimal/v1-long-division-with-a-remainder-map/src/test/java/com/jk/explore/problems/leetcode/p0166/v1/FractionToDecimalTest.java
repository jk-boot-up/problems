package com.jk.explore.problems.leetcode.p0166.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FractionToDecimalTest {

    private final FractionToDecimal solution = new FractionToDecimal();

    @Test
    void examples() {
        assertEquals("0.5", solution.fractionToDecimal(1, 2));
        assertEquals("2", solution.fractionToDecimal(2, 1));
        assertEquals("0.(012)", solution.fractionToDecimal(4, 333));
        assertEquals("0.1(6)", solution.fractionToDecimal(1, 6));
        assertEquals("-6.25", solution.fractionToDecimal(-50, 8));
        assertEquals("0", solution.fractionToDecimal(0, -5));
    }

    @Test
    void extremes() {
        assertEquals("0.0000000004656612873077392578125", solution.fractionToDecimal(-1, Integer.MIN_VALUE));
        assertEquals("2147483648", solution.fractionToDecimal(Integer.MIN_VALUE, -1));
    }
}
