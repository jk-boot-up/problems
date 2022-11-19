package com.jk.explore.problems.twosum;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

public class TwoSumProblemTest {

    @Test
    public void findIndicesCase1() {
        int [] numbers = new int[] { 2, 7, 11, 13, 15, 20, 40, 80};
        int twoSum = 93;
        TwoSumProblem twoSumProblem = new TwoSumProblem();
        int[] indices = twoSumProblem.findIndices(numbers, twoSum);
        assertNotNull(indices);
        assertArrayEquals(new int[]{7, 3}, indices);
    }

    @Test
    public void findIndicesCase2() {
        int[] myNumbers = {2, 7, 11, 5, 20, 30};
        int twoSum = 41;
        TwoSumProblem twoSumProblem = new TwoSumProblem();
        int[] indices = twoSumProblem.findIndices(myNumbers, twoSum);
        assertNotNull(indices);
        assertArrayEquals(new int[]{5, 2}, indices);
    }


}
