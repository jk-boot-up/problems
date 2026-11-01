package com.jk.explore.problems.leetcode.p1491.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class AverageSalaryTest {

    private final AverageSalary solution = new AverageSalary();

    @Test
    void examples() {
        assertEquals(2500.0, solution.average(new int[]{4000, 3000, 1000, 2000}), 1e-9);
        assertEquals(2000.0, solution.average(new int[]{1000, 2000, 3000}), 1e-9);
        assertEquals(3500.0, solution.average(new int[]{6000, 5000, 4000, 3000, 2000, 1000}), 1e-9);
    }
}
