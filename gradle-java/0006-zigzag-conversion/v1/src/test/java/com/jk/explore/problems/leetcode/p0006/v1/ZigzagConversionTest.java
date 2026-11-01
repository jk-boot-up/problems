package com.jk.explore.problems.leetcode.p0006.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ZigzagConversionTest {

    private final ZigzagConversion solution = new ZigzagConversion();

    @Test
    void threeRows() {
        assertEquals("PAHNAPLSIIGYIR", solution.convert("PAYPALISHIRING", 3));
    }

    @Test
    void fourRows() {
        assertEquals("PINALSIGYAHRPI", solution.convert("PAYPALISHIRING", 4));
    }

    @Test
    void oneRow() {
        assertEquals("AB", solution.convert("AB", 1));
    }
}
