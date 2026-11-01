package com.jk.explore.problems.leetcode.p1657.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CloseStringsTest {

    private final CloseStrings solution = new CloseStrings();

    @ParameterizedTest
    @CsvSource({"abc,bca,true", "a,aa,false", "cabbba,abbccc,true", "uau,ssx,false"})
    void checks(String a, String b, boolean expected) {
        assertEquals(expected, solution.closeStrings(a, b));
    }
}
