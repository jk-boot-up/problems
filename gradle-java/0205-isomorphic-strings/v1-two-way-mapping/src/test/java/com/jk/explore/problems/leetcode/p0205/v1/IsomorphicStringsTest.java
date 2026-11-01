package com.jk.explore.problems.leetcode.p0205.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class IsomorphicStringsTest {

    private final IsomorphicStrings solution = new IsomorphicStrings();

    @ParameterizedTest
    @CsvSource({"egg,add,true", "foo,bar,false", "paper,title,true", "badc,baba,false", "ab,aa,false"})
    void checks(String s, String t, boolean expected) {
        assertEquals(expected, solution.isIsomorphic(s, t));
    }
}
