package com.jk.explore.problems;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

public class _2_RotateImage_MatrixTest {

        private static _2_RotateImage_Matrix cut;

        @BeforeAll
        public static void setUp() {
            cut = new _2_RotateImage_Matrix();
        }

        @Test
        public void transpose() {
            Integer [][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
            System.out.println("Before Transpose: ");
            PrintUtils.print(matrix);
            cut.transpose(matrix);
            System.out.println("After Transpose: ");
            PrintUtils.print(matrix);
        }

        @Test
        public void reverseAllRows() {
            Integer[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
            System.out.println("Before Reverse: ");
            PrintUtils.print(matrix);
            cut.reverseAllRows(matrix);
            System.out.println("After Reverse: ");
            PrintUtils.print(matrix);
        }

        @Test
        public void clockwiseRotate() {
            Integer[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
            System.out.println("Before clockwise Rotate: ");
            PrintUtils.print(matrix);
            cut.clockwiseRotate(matrix);
            System.out.println("After clockwise Rotate: ");
            PrintUtils.print(matrix);
        }

    @Test
    public void antiClockwiseRotate() {
        Integer[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        System.out.println("Before anticlockwise Rotate: ");
        PrintUtils.print(matrix);
        cut.antiClockwiseRotate(matrix);
        System.out.println("After anticlockwise Rotate: ");
        PrintUtils.print(matrix);
    }

}
