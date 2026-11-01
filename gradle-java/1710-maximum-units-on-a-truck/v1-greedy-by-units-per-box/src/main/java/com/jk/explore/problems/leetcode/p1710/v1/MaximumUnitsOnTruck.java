package com.jk.explore.problems.leetcode.p1710.v1;

import java.util.*;

public class MaximumUnitsOnTruck {

    public int maximumUnits(int[][] boxTypes, int truckSize) {
        int[] boxesWithUnits = new int[1001];
        for (int[] b : boxTypes) boxesWithUnits[b[1]] += b[0];
        int units = 0;
        for (int u = 1000; u >= 1 && truckSize > 0; u--) {
            int take = Math.min(truckSize, boxesWithUnits[u]);
            units += take * u;
            truckSize -= take;
        }
        return units;
    }
}
