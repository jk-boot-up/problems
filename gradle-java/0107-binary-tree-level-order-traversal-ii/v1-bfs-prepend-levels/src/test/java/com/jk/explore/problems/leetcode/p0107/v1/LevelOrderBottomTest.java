package com.jk.explore.problems.leetcode.p0107.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LevelOrderBottomTest {

    private final LevelOrderBottom solution = new LevelOrderBottom();

    @Test
    void examples() {
        assertEquals(List.of(List.of(15, 7), List.of(9, 20), List.of(3)), solution.levelOrderBottom(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertEquals(List.of(), solution.levelOrderBottom(null));
    }
}
