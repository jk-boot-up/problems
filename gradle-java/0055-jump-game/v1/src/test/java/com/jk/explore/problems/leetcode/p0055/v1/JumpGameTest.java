package com.jk.explore.problems.leetcode.p0055.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class JumpGameTest {

    private final JumpGame solution = new JumpGame();

    @Test
    void reachable() {
        assertTrue(solution.canJump(new int[]{2, 3, 1, 1, 4}));
    }

    @Test
    void blockedByZero() {
        assertFalse(solution.canJump(new int[]{3, 2, 1, 0, 4}));
    }

    @Test
    void singleElement() {
        assertTrue(solution.canJump(new int[]{0}));
    }
}
