package com.jk.explore.problems.leetcode.p0105.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BuildTreePreInTest {

    private final BuildTreePreIn solution = new BuildTreePreIn();

    @Test
    void example1() {
        assertEquals(Arrays.asList(3, 9, 20, null, null, 15, 7), TreeNode.toList(solution.buildTree(new int[]{3, 9, 20, 15, 7}, new int[]{9, 3, 15, 20, 7})));
    }

    @Test
    void single() {
        assertEquals(List.of(-1), TreeNode.toList(solution.buildTree(new int[]{-1}, new int[]{-1})));
    }

    @Test
    void leftChain() {
        assertEquals(Arrays.asList(3, 2, null, 1), TreeNode.toList(solution.buildTree(new int[]{3, 2, 1}, new int[]{1, 2, 3})));
    }
}
