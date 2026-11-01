package com.jk.explore.problems.leetcode.p0045.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class JumpGameIITest {

    private final JumpGameII solution = new JumpGameII();

    @Test
    void example1() {
        assertEquals(2, solution.jump(new int[]{2, 3, 1, 1, 4}));
    }

    @Test
    void example2() {
        assertEquals(2, solution.jump(new int[]{2, 3, 0, 1, 4}));
    }

    @Test
    void alreadyThere() {
        assertEquals(0, solution.jump(new int[]{0}));
    }

    @Test
    void oneStepEachTime() {
        assertEquals(3, solution.jump(new int[]{1, 1, 1, 1}));
    }
}
