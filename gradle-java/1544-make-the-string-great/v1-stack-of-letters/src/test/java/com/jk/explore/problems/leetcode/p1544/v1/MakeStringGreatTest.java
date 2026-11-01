package com.jk.explore.problems.leetcode.p1544.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MakeStringGreatTest {

    private final MakeStringGreat solution = new MakeStringGreat();

    @Test
    void examples() {
        assertEquals("leetcode", solution.makeGood("leEeetcode"));
        assertEquals("", solution.makeGood("abBAcC"));
        assertEquals("s", solution.makeGood("s"));
        assertEquals("aa", solution.makeGood("aa"));
        assertEquals("", solution.makeGood("PpXxPxXp"));
    }
}
