package com.jk.explore.problems.leetcode.p0135.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CandyTest {

    private final Candy solution = new Candy();

    @Test
    void valley() {
        assertEquals(5, solution.candy(new int[]{1, 0, 2}));
    }

    @Test
    void equalNeighbours() {
        assertEquals(4, solution.candy(new int[]{1, 2, 2}));
    }

    @Test
    void decreasing() {
        assertEquals(6, solution.candy(new int[]{3, 2, 1}));
    }

    @Test
    void single() {
        assertEquals(1, solution.candy(new int[]{7}));
    }
}
