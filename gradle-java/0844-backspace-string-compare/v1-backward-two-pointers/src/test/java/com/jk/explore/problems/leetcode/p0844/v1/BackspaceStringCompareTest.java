package com.jk.explore.problems.leetcode.p0844.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BackspaceStringCompareTest {

    private final BackspaceStringCompare solution = new BackspaceStringCompare();

    @ParameterizedTest
    @CsvSource({"ab#c,ad#c,true", "ab##,c#d#,true", "a#c,b,false", "bxj##tw,bxo#j##tw,true"})
    void compares(String s, String t, boolean expected) {
        assertEquals(expected, solution.backspaceCompare(s, t));
    }
}
