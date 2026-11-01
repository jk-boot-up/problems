package com.jk.explore.problems.leetcode.p1305.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class AllElementsTwoBSTTest {

    private final AllElementsTwoBST solution = new AllElementsTwoBST();

    @Test
    void examples() {
        assertEquals(List.of(0, 1, 1, 2, 3, 4), solution.getAllElements(TreeNode.of(2, 1, 4), TreeNode.of(1, 0, 3)));
        assertEquals(List.of(1, 1, 8, 8), solution.getAllElements(TreeNode.of(1, null, 8), TreeNode.of(8, 1)));
        assertEquals(List.of(5), solution.getAllElements(null, TreeNode.of(5)));
        assertEquals(List.of(), solution.getAllElements(null, null));
    }
}
