package com.jk.explore.problems.samples.substrings.level.one;

public class LPMIndexImpl implements LPMIndex{

    @Override
    public int[] getLPMIndexArray(String pattern) {
        int[] indexArray = new int[1];
        if (pattern == null || pattern.trim().length() == 0) {
            return indexArray;
        } else {
            indexArray = new int[pattern.length() + 1];
            indexArray[0] = 0;
            indexArray[1] = 0;
            for(int i=2; i <= pattern.length(); i++) {
                int j = indexArray[i-1];
                for(;;) {
                    if(pattern.charAt(j) == pattern.charAt(i-1)) {
                        indexArray[i] = j+1;
                        break;
                    }
                    if(j == 0) {
                        indexArray[i] = 0;
                        break;
                    }
                    j = indexArray[j];
                }
            }
        }

        return indexArray;

    }
}
