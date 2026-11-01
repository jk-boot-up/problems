package com.jk.explore.problems.leetcode.p0258.v2;

import java.util.*;

public class AddDigits {

    public int addDigits(int num) {
        return num == 0 ? 0 : 1 + (num - 1) % 9;
    }
}
