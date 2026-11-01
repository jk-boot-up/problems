package com.jk.explore.problems.leetcode.p1523.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CountOddsInRangeTest {

    private final CountOddsInRange solution = new CountOddsInRange();

    @ParameterizedTest
    @CsvSource({"3,7,3", "8,10,1", "0,0,0", "1,1,1", "2,2,0", "0,1000000000,500000000", "999999999,1000000000,1"})
    void count(int low, int high, int expected) {
        assertEquals(expected, solution.countOdds(low, high));
    }
}
