package com.jk.explore.problems.leetcode.p0415.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class AddStringsTest {

    private final AddStrings solution = new AddStrings();

    @ParameterizedTest
    @CsvSource({"11,123,134", "456,77,533", "0,0,0", "999,1,1000", "1,9999,10000", "123456789123456789,987654321987654321,1111111111111111110"})
    void sums(String a, String b, String expected) {
        assertEquals(expected, solution.addStrings(a, b));
    }
}
