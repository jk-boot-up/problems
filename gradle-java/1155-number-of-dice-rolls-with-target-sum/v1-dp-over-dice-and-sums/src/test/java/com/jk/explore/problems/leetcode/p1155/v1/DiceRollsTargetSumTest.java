package com.jk.explore.problems.leetcode.p1155.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DiceRollsTargetSumTest {

    private final DiceRollsTargetSum solution = new DiceRollsTargetSum();

    @ParameterizedTest
    @CsvSource({"1,6,3,1", "2,6,7,6", "30,30,500,222616187", "2,6,13,0", "3,2,4,3"})
    void ways(int n, int k, int target, int expected) {
        assertEquals(expected, solution.numRollsToTarget(n, k, target));
    }
}
