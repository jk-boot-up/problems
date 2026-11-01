package com.jk.explore.problems.leetcode.p0950.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RevealCardsIncreasingTest {

    private final RevealCardsIncreasing solution = new RevealCardsIncreasing();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 13, 3, 11, 5, 17, 7}, solution.deckRevealedIncreasing(new int[]{17, 13, 11, 2, 3, 5, 7}));
        assertArrayEquals(new int[]{1, 1000}, solution.deckRevealedIncreasing(new int[]{1000, 1}));
        assertArrayEquals(new int[]{4}, solution.deckRevealedIncreasing(new int[]{4}));
    }
}
