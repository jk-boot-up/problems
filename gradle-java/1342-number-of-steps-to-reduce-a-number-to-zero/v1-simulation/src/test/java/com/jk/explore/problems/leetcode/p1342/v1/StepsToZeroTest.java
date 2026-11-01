package com.jk.explore.problems.leetcode.p1342.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class StepsToZeroTest {

    private final StepsToZero solution = new StepsToZero();

    @ParameterizedTest
    @CsvSource({"14,6", "8,4", "123,12", "0,0"})
    void steps(int num, int expected) {
        assertEquals(expected, solution.numberOfSteps(num));
    }
}
