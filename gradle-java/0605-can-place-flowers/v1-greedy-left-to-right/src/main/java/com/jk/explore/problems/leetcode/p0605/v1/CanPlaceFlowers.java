package com.jk.explore.problems.leetcode.p0605.v1;

import java.util.*;

public class CanPlaceFlowers {

    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int[] bed = flowerbed.clone();
        for (int i = 0; i < bed.length && n > 0; i++) {
            boolean leftEmpty = i == 0 || bed[i - 1] == 0;
            boolean rightEmpty = i == bed.length - 1 || bed[i + 1] == 0;
            if (bed[i] == 0 && leftEmpty && rightEmpty) {
                bed[i] = 1;
                n--;
            }
        }
        return n <= 0;
    }
}
