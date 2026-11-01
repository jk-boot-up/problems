package com.jk.explore.problems.leetcode.p0461.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class HammingDistanceTest {

    private final HammingDistance solution = new HammingDistance();

    @ParameterizedTest
    @CsvSource({"1,4,2", "3,1,1", "0,0,0", "0,2147483647,31", "7,7,0", "93,73,2"})
    void distance(int x, int y, int expected) {
        assertEquals(expected, solution.hammingDistance(x, y));
    }
}
