package com.jk.explore.problems.leetcode.p0179.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LargestNumberTest {

    private final LargestNumber solution = new LargestNumber();

    @Test
    void examples() {
        assertEquals("210", solution.largestNumber(new int[]{10, 2}));
        assertEquals("9534330", solution.largestNumber(new int[]{3, 30, 34, 5, 9}));
        assertEquals("0", solution.largestNumber(new int[]{0, 0}));
        assertEquals("1", solution.largestNumber(new int[]{1}));
        assertEquals("43243432", solution.largestNumber(new int[]{432, 43243}));
    }
}
