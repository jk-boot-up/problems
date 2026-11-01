package com.jk.explore.problems.leetcode.p0653.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TwoSumIVTest {

    private final TwoSumIV solution = new TwoSumIV();

    @Test
    void examples() {
        assertTrue(solution.findTarget(TreeNode.of(5, 3, 6, 2, 4, null, 7), 9));
        assertFalse(solution.findTarget(TreeNode.of(5, 3, 6, 2, 4, null, 7), 28));
        assertFalse(solution.findTarget(TreeNode.of(1), 2));
    }
}
