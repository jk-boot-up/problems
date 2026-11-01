package com.jk.explore.problems.leetcode.p0853.v1;

import java.util.*;

public class CarFleet {

    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, (a, b) -> Integer.compare(position[b], position[a]));
        int fleets = 0;
        double slowest = 0;
        for (int i : order) {
            double time = (double) (target - position[i]) / speed[i];
            if (time > slowest) {
                fleets++;
                slowest = time;
            }
        }
        return fleets;
    }
}
