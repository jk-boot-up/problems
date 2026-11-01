package com.jk.explore.problems.leetcode.p0129.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SumRootToLeafTest {

    private final SumRootToLeaf solution = new SumRootToLeaf();

    @Test
    void small() {
        assertEquals(25, solution.sumNumbers(TreeNode.of(1, 2, 3)));
    }

    @Test
    void example2() {
        assertEquals(1026, solution.sumNumbers(TreeNode.of(4, 9, 0, 5, 1)));
    }

    @Test
    void single() {
        assertEquals(7, solution.sumNumbers(TreeNode.of(7)));
    }
}
