package com.jk.explore.problems.leetcode.p1161.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumLevelSumTest {

    private final MaximumLevelSum solution = new MaximumLevelSum();

    @Test
    void examples() {
        assertEquals(2, solution.maxLevelSum(TreeNode.of(1, 7, 0, 7, -8, null, null)));
        assertEquals(2, solution.maxLevelSum(TreeNode.of(989, null, 10250, 98693, -89388, null, null, null, -32127)));
    }
}
