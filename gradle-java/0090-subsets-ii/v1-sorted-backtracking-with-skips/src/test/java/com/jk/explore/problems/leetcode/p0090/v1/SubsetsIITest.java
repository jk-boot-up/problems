package com.jk.explore.problems.leetcode.p0090.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SubsetsIITest {

    private final SubsetsII solution = new SubsetsII();

    @Test
    void duplicates() {
        assertEquals(List.of(List.of(), List.of(1), List.of(1, 2), List.of(1, 2, 2), List.of(2), List.of(2, 2)),
                solution.subsetsWithDup(new int[]{1, 2, 2}));
    }

    @Test
    void single() {
        assertEquals(List.of(List.of(), List.of(0)), solution.subsetsWithDup(new int[]{0}));
    }
}
