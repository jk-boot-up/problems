package com.jk.explore.problems.leetcode.p0567.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PermutationInStringTest {

    private final PermutationInString solution = new PermutationInString();

    @ParameterizedTest
    @CsvSource({"ab,eidbaooo,true", "ab,eidboaoo,false", "adc,dcda,true", "abc,ab,false"})
    void checks(String s1, String s2, boolean expected) {
        assertEquals(expected, solution.checkInclusion(s1, s2));
    }
}
