package com.jk.explore.problems.leetcode.p1424.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DiagonalTraverseIITest {

    private final DiagonalTraverseII solution = new DiagonalTraverseII();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 4, 2, 7, 5, 3, 8, 6, 9},
                solution.findDiagonalOrder(List.of(List.of(1, 2, 3), List.of(4, 5, 6), List.of(7, 8, 9))));
        assertArrayEquals(new int[]{1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16},
                solution.findDiagonalOrder(List.of(List.of(1, 2, 3, 4, 5), List.of(6, 7), List.of(8), List.of(9, 10, 11), List.of(12, 13, 14, 15, 16))));
        assertArrayEquals(new int[]{1, 2, 3}, solution.findDiagonalOrder(List.of(List.of(1, 2, 3))));
    }
}
