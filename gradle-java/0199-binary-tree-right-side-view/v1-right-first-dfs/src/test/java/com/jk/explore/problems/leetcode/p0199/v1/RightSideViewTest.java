package com.jk.explore.problems.leetcode.p0199.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RightSideViewTest {

    private final RightSideView solution = new RightSideView();

    @Test
    void example1() {
        assertEquals(List.of(1, 3, 4), solution.rightSideView(TreeNode.of(1, 2, 3, null, 5, null, 4)));
    }

    @Test
    void leftDeeper() {
        assertEquals(List.of(1, 3, 4, 5), solution.rightSideView(TreeNode.of(1, 2, 3, 4, null, null, null, 5)));
    }

    @Test
    void empty() {
        assertEquals(List.of(), solution.rightSideView(null));
    }
}
