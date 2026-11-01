package com.jk.explore.problems.leetcode.p0044.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class WildcardMatchingTest {

    private final WildcardMatching solution = new WildcardMatching();

    @ParameterizedTest
    @CsvSource({"aa,a,false", "aa,*,true", "cb,?a,false", "adceb,*a*b,true", "acdcb,a*c?b,false", "'',*,true", "abc,'',false"})
    void matches(String s, String p, boolean expected) {
        assertEquals(expected, solution.isMatch(s, p));
    }
}
