package com.jk.explore.problems.leetcode.p0072.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class EditDistanceTest {

    private final EditDistance solution = new EditDistance();

    @ParameterizedTest
    @CsvSource({"horse,ros,3", "intention,execution,5", "'',abc,3", "abc,abc,0", "kitten,sitting,3"})
    void distances(String a, String b, int expected) {
        assertEquals(expected, solution.minDistance(a, b));
    }
}
