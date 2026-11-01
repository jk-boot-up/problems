package com.jk.explore.problems.leetcode.p0979.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DistributeCoinsTest {

    private final DistributeCoins solution = new DistributeCoins();

    @Test
    void examples() {
        assertEquals(2, solution.distributeCoins(TreeNode.of(3, 0, 0)));
        assertEquals(3, solution.distributeCoins(TreeNode.of(0, 3, 0)));
        assertEquals(2, solution.distributeCoins(TreeNode.of(1, 0, 2)));
        assertEquals(0, solution.distributeCoins(TreeNode.of(1)));
        assertEquals(4, solution.distributeCoins(TreeNode.of(1, 0, 0, null, 3)));
    }
}
