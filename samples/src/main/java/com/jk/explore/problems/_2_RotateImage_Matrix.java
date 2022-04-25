package com.jk.explore.problems;

import java.util.stream.IntStream;


public class _2_RotateImage_Matrix {

    public void clockwiseRotate(Integer[][] matrix) {
        transpose(matrix);
        reverseAllRows(matrix);
    }

    public void antiClockwiseRotate(Integer[][] matrix) {
        transpose(matrix);
        reverseAllColumns(matrix);
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

    public void reverseAllColumns(Integer[][] matrix) {
        // columns length matrix[0].length
        // Assuming square matrix
        IntStream.range(0, matrix.length).forEach(columnIndex -> {
            int topPointer = 0;
            int bottomPointer = matrix.length - 1;
            while(topPointer < bottomPointer) {
                Integer temp = matrix[topPointer][columnIndex];
                matrix[topPointer][columnIndex] = matrix[bottomPointer][columnIndex];
                matrix[bottomPointer][columnIndex] = temp;
                topPointer++;
                bottomPointer--;
            }
        });
    }
}

/*
     1 2 3
     4 5 6
     7 8 9

 clock wise      7 4 1
                 8 5 2
                 9 6 3

 anti clock wise
                   3 6 9
                   2 5 8
                   1 4 7
 */
