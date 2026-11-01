package com.jk.explore.problems.leetcode.p1456.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaxVowelsTest {

    private final MaxVowels solution = new MaxVowels();

    @ParameterizedTest
    @CsvSource({"abciiidef,3,3", "aeiou,2,2", "leetcode,3,2", "rhythms,4,0"})
    void counts(String s, int k, int expected) {
        assertEquals(expected, solution.maxVowels(s, k));
    }
}
