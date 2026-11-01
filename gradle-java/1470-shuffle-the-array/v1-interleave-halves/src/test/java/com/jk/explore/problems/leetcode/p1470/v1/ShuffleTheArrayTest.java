package com.jk.explore.problems.leetcode.p1470.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ShuffleTheArrayTest {

    private final ShuffleTheArray solution = new ShuffleTheArray();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 3, 5, 4, 1, 7}, solution.shuffle(new int[]{2, 5, 1, 3, 4, 7}, 3));
        assertArrayEquals(new int[]{1, 4, 2, 3, 3, 2, 4, 1}, solution.shuffle(new int[]{1, 2, 3, 4, 4, 3, 2, 1}, 4));
        assertArrayEquals(new int[]{1, 2}, solution.shuffle(new int[]{1, 2}, 1));
    }
}
