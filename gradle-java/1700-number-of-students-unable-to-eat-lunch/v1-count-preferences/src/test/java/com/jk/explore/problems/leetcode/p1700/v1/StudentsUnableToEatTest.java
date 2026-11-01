package com.jk.explore.problems.leetcode.p1700.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class StudentsUnableToEatTest {

    private final StudentsUnableToEat solution = new StudentsUnableToEat();

    @Test
    void examples() {
        assertEquals(0, solution.countStudents(new int[]{1, 1, 0, 0}, new int[]{0, 1, 0, 1}));
        assertEquals(3, solution.countStudents(new int[]{1, 1, 1, 0, 0, 1}, new int[]{1, 0, 0, 0, 1, 1}));
        assertEquals(1, solution.countStudents(new int[]{0}, new int[]{1}));
    }
}
