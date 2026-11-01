package com.jk.explore.problems.leetcode.p0065.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ValidNumberTest {

    private final ValidNumber solution = new ValidNumber();

    @ParameterizedTest
    @CsvSource({"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "53.5e93"})
    void valid(String s) {
        assertTrue(solution.isNumber(s));
    }

    @ParameterizedTest
    @CsvSource({"abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "."})
    void invalid(String s) {
        assertFalse(solution.isNumber(s));
    }
}
