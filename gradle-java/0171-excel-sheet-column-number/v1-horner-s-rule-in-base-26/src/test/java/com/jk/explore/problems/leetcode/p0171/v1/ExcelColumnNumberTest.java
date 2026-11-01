package com.jk.explore.problems.leetcode.p0171.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ExcelColumnNumberTest {

    private final ExcelColumnNumber solution = new ExcelColumnNumber();

    @ParameterizedTest
    @CsvSource({"A,1", "Z,26", "AA,27", "AB,28", "ZY,701", "AAA,703", "FXSHRXW,2147483647"})
    void numbers(String title, int expected) {
        assertEquals(expected, solution.titleToNumber(title));
    }
}
