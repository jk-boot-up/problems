package com.jk.explore.problems.leetcode.p0013.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RomanToIntegerTest {

    private final RomanToInteger solution = new RomanToInteger();

    @ParameterizedTest
    @CsvSource({"III,3", "LVIII,58", "MCMXCIV,1994", "IV,4", "MMMCMXCIX,3999"})
    void converts(String roman, int expected) {
        assertEquals(expected, solution.romanToInt(roman));
    }
}
