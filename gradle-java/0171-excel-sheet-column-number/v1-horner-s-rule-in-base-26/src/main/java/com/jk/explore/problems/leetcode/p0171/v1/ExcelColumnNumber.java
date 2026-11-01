package com.jk.explore.problems.leetcode.p0171.v1;

import java.util.*;

public class ExcelColumnNumber {

    public int titleToNumber(String columnTitle) {
        int result = 0;
        for (int i = 0; i < columnTitle.length(); i++) result = result * 26 + (columnTitle.charAt(i) - 'A' + 1);
        return result;
    }
}
