package com.jk.explore.problems.leetcode.p0012.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class IntegerToRomanTest {

    private final IntegerToRoman solution = new IntegerToRoman();

    @ParameterizedTest
    @CsvSource({"3749,MMMDCCXLIX", "58,LVIII", "1994,MCMXCIV", "4,IV", "3999,MMMCMXCIX", "1,I"})
    void converts(int num, String expected) {
        assertEquals(expected, solution.intToRoman(num));
    }
}
