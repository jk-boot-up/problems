package com.jk.explore.problems.samples.numeric.level.a;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class FindIndicesForSumTest {

    private FindIndicesForSum cut;

    @BeforeEach
    public void init() {
        cut = new FindIndicesForSum();
    }

    @Test
    public void testForUniqueValidInputWithBruteForce() {
        int[] input = {20, 10, 30, 5, 40, 60, 80, 90, 1};
        int[] indices = cut.getIndicesWhoseElementsSumsToTargetWithBruteForce(input, 31);
        Assertions.assertArrayEquals(indices, new int[] {2, 8});
    }

    @Test
    public void testForInvalidInputWithBruteForce() {
        int[] input = {20, 10, 30, 5, 40, 60, 80, 90, 2};
        int[] indices = cut.getIndicesWhoseElementsSumsToTargetWithBruteForce(input, 31);
        Assertions.assertNull(indices);
    }

    @Test
    public void testForUniqueValidInputWithMap() {
        int[] input = {20, 10, 30, 5, 40, 60, 80, 90, 1};
        int[] indices = cut.getIndicesWhoseElementsSumsToTargetWithMap(input, 31);
        Assertions.assertArrayEquals(indices, new int[] {2, 8});
    }

    @Test
    public void testForInvalidInputWithMap() {
        int[] input = {20, 10, 30, 5, 40, 60, 80, 90, 2};
        int[] indices = cut.getIndicesWhoseElementsSumsToTargetWithBruteForce(input, 31);
        Assertions.assertNull(indices);
    }

}
