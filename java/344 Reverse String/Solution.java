/************author: litao******************/
/************date:2016/08/24****************/
/************number:344*********************/
/************title:reverse string**************/
/*********************************************
*  Describe:
*  Write a function that takes a string as input
*  and returns the string reversed.
*
*  Examples:
*  Given s = "hello", return "olleh".
*
**********************************************/
public class Solution{
	public String reverseString(String s){
		int i=0,j=s.length()-1;
		char[] str=s.toCharArray();
		while(i<j){
			char temp=str[i];
			str[i]=str[j];
			str[j]=temp;
			i++;
			j--;
		
		}
		return String.copyValueOf(str);
	}

}
