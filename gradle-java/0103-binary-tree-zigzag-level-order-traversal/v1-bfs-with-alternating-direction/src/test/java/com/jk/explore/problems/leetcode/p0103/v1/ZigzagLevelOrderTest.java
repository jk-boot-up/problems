package com.jk.explore.problems.leetcode.p0103.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ZigzagLevelOrderTest {

    private final ZigzagLevelOrder solution = new ZigzagLevelOrder();

    @Test
    void example() {
        assertEquals(List.of(List.of(3), List.of(20, 9), List.of(15, 7)), solution.zigzagLevelOrder(TreeNode.of(3, 9, 20, null, null, 15, 7)));
    }

    @Test
    void fourLevels() {
        assertEquals(List.of(List.of(1), List.of(3, 2), List.of(4, 5, 6, 7), List.of(8)),
                solution.zigzagLevelOrder(TreeNode.of(1, 2, 3, 4, 5, 6, 7, 8)));
    }

    @Test
    void empty() {
        assertEquals(List.of(), solution.zigzagLevelOrder(null));
    }
}
