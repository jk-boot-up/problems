package com.jk.explore.problems.leetcode.p0412.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FizzBuzzTest {

    private final FizzBuzz solution = new FizzBuzz();

    @Test
    void fifteen() {
        assertEquals(List.of("1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"), solution.fizzBuzz(15));
    }
}
