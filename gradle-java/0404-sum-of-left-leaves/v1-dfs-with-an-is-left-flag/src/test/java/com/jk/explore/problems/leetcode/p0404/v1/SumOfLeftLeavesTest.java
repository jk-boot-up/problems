package com.jk.explore.problems.leetcode.p0404.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SumOfLeftLeavesTest {

    private final SumOfLeftLeaves solution = new SumOfLeftLeaves();

    @Test
    void examples() {
        assertEquals(24, solution.sumOfLeftLeaves(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertEquals(0, solution.sumOfLeftLeaves(TreeNode.of(1)));
        assertEquals(4, solution.sumOfLeftLeaves(TreeNode.of(1, 2, 3, 4, 5)));
        assertEquals(0, solution.sumOfLeftLeaves(TreeNode.of(1, null, 2)));
    }
}
