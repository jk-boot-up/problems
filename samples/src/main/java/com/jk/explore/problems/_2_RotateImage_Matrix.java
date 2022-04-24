package com.jk.explore.problems;

import java.util.stream.IntStream;


public class _2_RotateImage_Matrix {

    public void clockwiseRotate(Integer[][] matrix) {
        transpose(matrix);
        reverseAllRows(matrix);
    }

    public void transpose(Integer[][] matrix) {
        int rows = matrix.length;
        int columns = matrix.length;
        for(int i=0; i < rows; i++) {
            for(int j=i+1; j < columns; j++) {
                Integer temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }

    public void reverseAllRows(Integer[][] matrix) {
        // columns length matrix[0].length
        // Assuming square matrix
        IntStream.range(0, matrix.length).forEach(rowIndex -> {
            int leftPointer = 0;
            int rightPointer = matrix.length - 1;
            while(leftPointer < rightPointer) {
                Integer temp = matrix[rowIndex][leftPointer];
                matrix[rowIndex][leftPointer] = matrix[rowIndex][rightPointer];
                matrix[rowIndex][rightPointer] = temp;
                leftPointer++;
                rightPointer--;
            }
        });
    }
}
