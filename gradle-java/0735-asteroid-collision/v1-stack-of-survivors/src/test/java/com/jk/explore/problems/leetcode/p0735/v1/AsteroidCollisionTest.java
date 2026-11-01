package com.jk.explore.problems.leetcode.p0735.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class AsteroidCollisionTest {

    private final AsteroidCollision solution = new AsteroidCollision();

    @Test
    void examples() {
        assertArrayEquals(new int[]{5, 10}, solution.asteroidCollision(new int[]{5, 10, -5}));
        assertArrayEquals(new int[]{}, solution.asteroidCollision(new int[]{8, -8}));
        assertArrayEquals(new int[]{10}, solution.asteroidCollision(new int[]{10, 2, -5}));
        assertArrayEquals(new int[]{-2, -1, 1, 2}, solution.asteroidCollision(new int[]{-2, -1, 1, 2}));
    }
}
