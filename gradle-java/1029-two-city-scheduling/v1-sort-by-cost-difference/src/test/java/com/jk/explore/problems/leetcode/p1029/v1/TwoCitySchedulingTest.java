package com.jk.explore.problems.leetcode.p1029.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TwoCitySchedulingTest {

    private final TwoCityScheduling solution = new TwoCityScheduling();

    @Test
    void examples() {
        assertEquals(110, solution.twoCitySchedCost(new int[][]{{10, 20}, {30, 200}, {400, 50}, {30, 20}}));
        assertEquals(1859, solution.twoCitySchedCost(new int[][]{{259, 770}, {448, 54}, {926, 667}, {184, 139}, {840, 118}, {577, 469}}));
        assertEquals(3086, solution.twoCitySchedCost(new int[][]{{515, 563}, {451, 713}, {537, 709}, {343, 819}, {855, 779}, {457, 60}, {650, 359}, {631, 42}}));
    }
}
