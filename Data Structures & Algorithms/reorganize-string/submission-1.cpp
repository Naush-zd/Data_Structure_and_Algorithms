class Solution {
public:
    string reorganizeString(string s) {
        vector<int> freq(26,0);
        for(char& c:s){
            freq[c-'a']++;
        }
        priority_queue<pair<int,char>>maxHeap;
         for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                maxHeap.push({freq[i], 'a' + i});
            }
        }
        string res="";
        pair<int,char> prev = {0, ' '};
        while(!maxHeap.empty() || prev.first>0){
            if(prev.first>0 && maxHeap.empty()){
                return "";
            }
            auto [cnt, char_] = maxHeap.top();
            maxHeap.pop();
            res+=char_;
            cnt--;
            if(prev.first>0){
                maxHeap.push(prev);
            }
            prev = {cnt,char_};
        }
        return res;
    }
};