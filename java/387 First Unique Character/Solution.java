/************author: litao******************/
/************date:2016/08/23****************/
/************number:387*********************/
/************title:First Unique Character in a String*/
/*********************************************
*  Describe:
*  Given a string, find the first non-repeating 
*  character in it and return it's index. If it 
*   doesn't exist, return -1.
*
*  Examples:
*  s = "leetcode"
*  return 0.
*  s = "loveleetcode",
*  return 2.
*
**********************************************/
public class Solution {
    public int firstUniqChar(String s) {
        int[] arr=new int[26];
        int len=s.length();
        for(int i=0;i<len;i++){
            char x=s.charAt(i);
            //题目假设只有小写，若出现大写则返回-1
            if(Character.isUpperCase(x)){
                return -1;
            }
            arr[x-'a']++;
        }
        for(int i=0;i<len;i++){
            char x=s.charAt(i);
            //题目假设只有小写，若出现大写则返回-1
            if(Character.isUpperCase(x)){
                return -1;
            }
            if(arr[x-'a'] == 1){
                return i;
            }
        }
        return -1;
    }
}