package com.jk.explore.problems.leetcode.p0433.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinimumGeneticMutationTest {

    private final MinimumGeneticMutation solution = new MinimumGeneticMutation();

    @Test
    void one() {
        assertEquals(1, solution.minMutation("AACCGGTT", "AACCGGTA", new String[]{"AACCGGTA"}));
    }

    @Test
    void two() {
        assertEquals(2, solution.minMutation("AACCGGTT", "AAACGGTA", new String[]{"AACCGGTA", "AACCGCTA", "AAACGGTA"}));
    }

    @Test
    void impossible() {
        assertEquals(-1, solution.minMutation("AAAAAAAA", "CCCCCCCC", new String[]{"AAAAAAAC", "CCCCCCCC"}));
        assertEquals(-1, solution.minMutation("AACCGGTT", "AACCGGTA", new String[]{}));
    }
}
