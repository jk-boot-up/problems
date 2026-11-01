package com.jk.explore.problems.leetcode.p0134.v1;

import java.util.*;

public class GasStation {

    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        for (int start = 0; start < n; start++) {
            int tank = 0, legs = 0;
            while (legs < n) {
                int i = (start + legs) % n;
                tank += gas[i] - cost[i];
                if (tank < 0) break;
                legs++;
            }
            if (legs == n) return start;
        }
        return -1;
    }
}
