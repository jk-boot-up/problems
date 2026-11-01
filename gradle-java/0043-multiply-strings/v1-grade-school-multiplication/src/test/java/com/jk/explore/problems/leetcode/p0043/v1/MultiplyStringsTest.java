package com.jk.explore.problems.leetcode.p0043.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MultiplyStringsTest {

    private final MultiplyStrings solution = new MultiplyStrings();

    @ParameterizedTest
    @CsvSource({"2,3,6", "123,456,56088", "0,52,0", "999,999,998001"})
    void multiplies(String a, String b, String expected) {
        assertEquals(expected, solution.multiply(a, b));
    }
}
