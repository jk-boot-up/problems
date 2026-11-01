package com.jk.explore.problems.leetcode.p0113.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PathSumIITest {

    private final PathSumII solution = new PathSumII();

    @Test
    void example() {
        assertEquals(List.of(List.of(5, 4, 11, 2), List.of(5, 8, 4, 5)),
                solution.pathSum(TreeNode.of(5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1), 22));
    }

    @Test
    void none() {
        assertEquals(List.of(), solution.pathSum(TreeNode.of(1, 2, 3), 5));
    }
}
