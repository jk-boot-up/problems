package com.jk.explore.problems;

import java.util.stream.IntStream;

public class ZigzagConversion {

    public String zigzag(String text, int rows) {
        StringBuffer[] buffers = new StringBuffer[rows];
        IntStream.range(0, buffers.length).forEach(index -> buffers[index] = new StringBuffer());
        int currentRow = 0;
        int zigZagDirection = 1;
        for(int i =0; i < text.length(); i++) {
            buffers[currentRow].append(text.charAt(i));
            if(currentRow == (rows -1)) {
                zigZagDirection = -1;
            }
            if(currentRow == 0) {
                zigZagDirection = 1;
            }
            currentRow = currentRow + zigZagDirection;
        }
        StringBuffer results = new StringBuffer();
        IntStream.range(0, rows).forEach(i -> {
            results.append(buffers[i]);
        });
        return results.toString();
    }
}
/*
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

----

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
 */