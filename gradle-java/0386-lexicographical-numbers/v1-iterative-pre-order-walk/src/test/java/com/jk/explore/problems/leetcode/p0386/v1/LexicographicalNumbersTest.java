package com.jk.explore.problems.leetcode.p0386.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LexicographicalNumbersTest {

    private final LexicographicalNumbers solution = new LexicographicalNumbers();

    @Test
    void examples() {
        assertEquals(List.of(1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9), solution.lexicalOrder(13));
        assertEquals(List.of(1, 2), solution.lexicalOrder(2));
        assertEquals(List.of(1), solution.lexicalOrder(1));
    }

    @Test
    void matchesStringSort() {
        for (int n : new int[]{9, 10, 99, 100, 101, 1234, 50000}) {
            List<String> s = new ArrayList<>();
            for (int i = 1; i <= n; i++) s.add(String.valueOf(i));
            Collections.sort(s);
            List<Integer> expected = new ArrayList<>();
            for (String x : s) expected.add(Integer.parseInt(x));
            assertEquals(expected, solution.lexicalOrder(n));
        }
    }
}
