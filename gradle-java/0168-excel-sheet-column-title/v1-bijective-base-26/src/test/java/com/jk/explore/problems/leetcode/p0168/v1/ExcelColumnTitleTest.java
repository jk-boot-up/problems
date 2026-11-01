package com.jk.explore.problems.leetcode.p0168.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ExcelColumnTitleTest {

    private final ExcelColumnTitle solution = new ExcelColumnTitle();

    @ParameterizedTest
    @CsvSource({"1,A", "26,Z", "27,AA", "28,AB", "52,AZ", "701,ZY", "702,ZZ", "703,AAA", "2147483647,FXSHRXW"})
    void titles(int n, String expected) {
        assertEquals(expected, solution.convertToTitle(n));
    }
}
