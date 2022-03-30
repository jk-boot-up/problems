package com.jk.explore.problems;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class ContainerWithMostWaterTest {

    @Test
    public void findMaxArea() {
        ContainerWithMostWater containerWithMostWater = new ContainerWithMostWater();
        int[] heights = new int[] {1,8,6,2,5,4,8,3,7};
        Arrays.stream(heights).forEach(i -> System.out.println(i));
        int maxArea = containerWithMostWater.findMaxArea(heights);
        Assertions.assertEquals(maxArea, 49);

    }
}
