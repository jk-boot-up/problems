package com.jk.explore.problems;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TwoSumTest {

    @Test
    public void sample1() {
        List<Integer> numbers = Arrays.asList(2, 1, 7, 15, 9);
        TwoSum twoSum = new TwoSum();
        TwoSum.Results results = twoSum.getIndicesResults(numbers, 16);
        assertEquals(results.getFirstIndex(), 1);
        assertEquals(results.getSecondIndex(), 3);
        assertEquals(16,
                numbers.get(results.getFirstIndex()) + numbers.get(results.getSecondIndex())
                    );
    }
}
