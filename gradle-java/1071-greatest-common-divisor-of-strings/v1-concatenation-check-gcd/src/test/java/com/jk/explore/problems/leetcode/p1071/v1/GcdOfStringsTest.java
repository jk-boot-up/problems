package com.jk.explore.problems.leetcode.p1071.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class GcdOfStringsTest {

    private final GcdOfStrings solution = new GcdOfStrings();

    @ParameterizedTest
    @CsvSource({"ABCABC,ABC,ABC", "ABABAB,ABAB,AB", "LEET,CODE,''"})
    void divides(String a, String b, String expected) {
        assertEquals(expected, solution.gcdOfStrings(a, b));
    }
}
