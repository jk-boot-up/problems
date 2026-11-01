package com.jk.explore.problems.leetcode.p0010.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RegularExpressionMatchingTest {

    private final RegularExpressionMatching solution = new RegularExpressionMatching();

    @ParameterizedTest
    @CsvSource({"aa,a,false", "aa,a*,true", "ab,.*,true", "aab,c*a*b,true", "mississippi,mis*is*p*.,false", "ab,.*c,false"})
    void matches(String s, String p, boolean expected) {
        assertEquals(expected, solution.isMatch(s, p));
    }
}
