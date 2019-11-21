import java.util.*;
class Solution {
    public String longestPalindrome(String s) {
        int largest=0;
        String subS;
        int len=s.length();
        int LO;
        int RO;
        int LE;
        int RE;
        int countOdd = 1;
        int countEven = 0;
        Integer [] max = {0,0,0};
        int flag = 1;
        for (int i=0; i<len; i++){
            //odd case
            LO=i-1;
            RO=i+1;
            while (LO>=0 & RO<len & flag==1){
                if (s.substring(LO,LO+1).equals(s.substring(RO,RO+1))){
                    countOdd+=2;
                    LO--;
                    RO++;
                }
                else{
                    flag=0;
                }
            }
            //even case
            LE=i;
            RE=i+1;
            flag=1;
            /*There may be a way to merge the above while loop with this one to speed things up although it is tricky 
            because you want to stop iterating one while doing the other and not cause an out of index range error*/
            while (LE>=0 & RE<len & flag==1){
                if (s.substring(LE,LE+1).equals(s.substring(RE,RE+1))){
                    countEven+=2;
                    LE--;
                    RE++;
                }
                else{
                    flag=0;
                }
            }
            if (countOdd>countEven){
                if (countOdd>max[0]){
                    max[0]=countOdd;
                    max[1]=LO+1;
                    max[2]=RO;
                }
            }
            else{
                if (countEven>max[0]){
                    max[0]=countEven;
                    max[1]=LE+1;
                    max[2]=RE;
            }
            
            }
            //allow next while loop
            flag=1;
            countOdd=1;
            countEven=0;
        }
        return s.substring(max[1],max[2]);
    }
}
