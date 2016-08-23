# leetcode
my solution for java.
|题号|题目|难度|代码|
|283|Move Zeroes|easy|code
## 题目283. Move Zeroes 
## 描述
>Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
## java解决方案
```java
 public void moveZeroes(int[] nums) {
        int len=nums.length;
        int j=0;
        for(int i=0;i<len;i++){
            if(nums[i]!=0){
                nums[j++]=nums[i];
            }
        }
        while(j<len){
            nums[j]=0;
            j++;
        }
    }
```
