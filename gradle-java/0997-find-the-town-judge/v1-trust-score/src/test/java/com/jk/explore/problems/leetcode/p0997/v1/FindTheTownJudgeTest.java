package com.jk.explore.problems.leetcode.p0997.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindTheTownJudgeTest {

    private final FindTheTownJudge solution = new FindTheTownJudge();

    @Test
    void examples() {
        assertEquals(2, solution.findJudge(2, new int[][]{{1, 2}}));
        assertEquals(3, solution.findJudge(3, new int[][]{{1, 3}, {2, 3}}));
        assertEquals(-1, solution.findJudge(3, new int[][]{{1, 3}, {2, 3}, {3, 1}}));
        assertEquals(1, solution.findJudge(1, new int[][]{}));
    }
}
