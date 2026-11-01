package com.jk.explore.problems.leetcode.p0459.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RepeatedSubstringPatternTest {

    private final RepeatedSubstringPattern solution = new RepeatedSubstringPattern();

    @ParameterizedTest
    @CsvSource({"abab,true", "aba,false", "abcabcabcabc,true", "a,false", "aa,true", "abac,false", "abaababaab,true", "aabaaba,false"})
    void check(String s, boolean expected) {
        assertEquals(expected, solution.repeatedSubstringPattern(s));
    }
}
