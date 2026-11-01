package com.jk.explore.problems.leetcode.p0106.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BuildTreeInPostTest {

    private final BuildTreeInPost solution = new BuildTreeInPost();

    @Test
    void example1() {
        assertEquals(Arrays.asList(3, 9, 20, null, null, 15, 7), TreeNode.toList(solution.buildTree(new int[]{9, 3, 15, 20, 7}, new int[]{9, 15, 7, 20, 3})));
    }

    @Test
    void single() {
        assertEquals(List.of(-1), TreeNode.toList(solution.buildTree(new int[]{-1}, new int[]{-1})));
    }

    @Test
    void rightChain() {
        assertEquals(Arrays.asList(1, null, 2, null, 3), TreeNode.toList(solution.buildTree(new int[]{1, 2, 3}, new int[]{3, 2, 1})));
    }
}
