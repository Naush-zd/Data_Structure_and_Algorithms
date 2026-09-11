class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(),people.end());
        int l=0;
        int r= size(people)-1;
        int count=0;
        while(l<=r){
            int remain = limit - people[r];
            count++;
            r--;
            if(l<=r && remain>= people[l]) l++;
        }

        return count;
    }
};