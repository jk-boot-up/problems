package com.jk.explore.problems.leetcode.p0771.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class JewelsAndStonesTest {

    private final JewelsAndStones solution = new JewelsAndStones();

    @ParameterizedTest
    @CsvSource({"aA,aAAbbbb,3", "z,ZZ,0"})
    void counts(String j, String s, int expected) {
        assertEquals(expected, solution.numJewelsInStones(j, s));
    }
}
