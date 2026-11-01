package com.jk.explore.problems.leetcode.p0399.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class EvaluateDivisionTest {

    private final EvaluateDivision solution = new EvaluateDivision();

    @Test
    void example() {
        double[] out = solution.calcEquation(
                List.of(List.of("a", "b"), List.of("b", "c")), new double[]{2.0, 3.0},
                List.of(List.of("a", "c"), List.of("b", "a"), List.of("a", "e"), List.of("a", "a"), List.of("x", "x")));
        assertArrayEquals(new double[]{6.0, 0.5, -1.0, 1.0, -1.0}, out, 1e-9);
    }

    @Test
    void disconnectedComponents() {
        double[] out = solution.calcEquation(
                List.of(List.of("a", "b"), List.of("c", "d")), new double[]{1.5, 2.5},
                List.of(List.of("a", "d"), List.of("d", "c")));
        assertArrayEquals(new double[]{-1.0, 0.4}, out, 1e-9);
    }
}
