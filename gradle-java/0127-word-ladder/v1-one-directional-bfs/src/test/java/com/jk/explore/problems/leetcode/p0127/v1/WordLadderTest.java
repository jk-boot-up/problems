package com.jk.explore.problems.leetcode.p0127.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class WordLadderTest {

    private final WordLadder solution = new WordLadder();

    @Test
    void reachable() {
        assertEquals(5, solution.ladderLength("hit", "cog", List.of("hot", "dot", "dog", "lot", "log", "cog")));
    }

    @Test
    void endMissing() {
        assertEquals(0, solution.ladderLength("hit", "cog", List.of("hot", "dot", "dog", "lot", "log")));
    }

    @Test
    void oneStep() {
        assertEquals(2, solution.ladderLength("a", "c", List.of("a", "b", "c")));
    }
}
