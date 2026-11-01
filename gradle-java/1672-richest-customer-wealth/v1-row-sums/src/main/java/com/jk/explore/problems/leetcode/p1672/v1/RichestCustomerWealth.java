package com.jk.explore.problems.leetcode.p1672.v1;

import java.util.*;

public class RichestCustomerWealth {

    public int maximumWealth(int[][] accounts) {
        int best = 0;
        for (int[] customer : accounts) {
            int sum = 0;
            for (int money : customer) sum += money;
            best = Math.max(best, sum);
        }
        return best;
    }
}
