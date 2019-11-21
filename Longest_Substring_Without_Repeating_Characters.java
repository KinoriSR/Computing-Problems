import java.util.*;
class Solution {    
    public int lengthOfLongestSubstring(String s) {
    
        //use char as key in hashmap
        Integer[] max = {0,0};
        int count = 0;
        int startindex = 0;
        HashMap<String,Integer> dict = new HashMap<>();
        String ch;
        int i=0;
        while (i<s.length()){
            ch=s.substring(i,i+1);
            if (!dict.containsKey(ch)){
                dict.put(ch,i);
                count++;
                if (max[0]<count){
                    max[0]=count;
                    max[1]=startindex;
                }
            }
            else {
                i=dict.get(ch);
                dict.clear();
                count=0;
                startindex=i+1;
                
            }
            i++;
        }
        return max[0];
    }
}
