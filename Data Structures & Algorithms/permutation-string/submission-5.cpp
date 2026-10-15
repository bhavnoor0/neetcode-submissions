class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) return false;

        array<int, 26> count_s1{};
        
        for (int i = 0; i < s1.length(); i++){
            count_s1[(int) s1[i] - (int) 'a'] ++;
        }
        int left = 0;
        int right = s1.length();
        array<int, 26> count_s2{};
        for (int i = left; i < right; i++){
            count_s2[(int) s2[i] - (int) 'a'] ++;
        }
        while (right <= s2.length()){
            if (count_s1 == count_s2){
                return true;
            } else {
                count_s2[(int) s2[left] - (int) 'a'] --;
                if (right < s2.length()){
                    count_s2[(int) s2[right] - (int) 'a'] ++;
                }
                left += 1;
                right += 1;
            }
        }
        return false;
    }
};
