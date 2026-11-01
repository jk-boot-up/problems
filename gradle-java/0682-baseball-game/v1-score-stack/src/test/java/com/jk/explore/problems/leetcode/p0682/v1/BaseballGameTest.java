package com.jk.explore.problems.leetcode.p0682.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BaseballGameTest {

    private final BaseballGame solution = new BaseballGame();

    @Test
    void examples() {
        assertEquals(30, solution.calPoints(new String[]{"5", "2", "C", "D", "+"}));
        assertEquals(27, solution.calPoints(new String[]{"5", "-2", "4", "C", "D", "9", "+", "+"}));
        assertEquals(0, solution.calPoints(new String[]{"1", "C"}));
    }
}
