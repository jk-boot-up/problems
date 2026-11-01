package com.jk.explore.problems.leetcode.p0714.v1;

import java.util.*;

public class StockWithFee {

    public int maxProfit(int[] prices, int fee) {
        int cash = 0, hold = -prices[0];
        for (int p : prices) {
            cash = Math.max(cash, hold + p - fee);
            hold = Math.max(hold, cash - p);
        }
        return cash;
    }
}
