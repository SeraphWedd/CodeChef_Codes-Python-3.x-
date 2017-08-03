#include <iostream>

using namespace std;

int main(){
    int T;
    long long int mod=1000000007;
    long long int A, B, N, r;


    cin >> T;
    long long int ANS[T];
    for (long long int i=0; i < T; i++){
            cin >> A >> B >> N;
            r = N%6;
            if (r==0){
                ANS[i] = (A-B)%mod;
            }
            else if (r==1){
                ANS[i] = A%mod;
            }
            else if (r==2){
                ANS[i] = B%mod;
            }
            else if (r==3){
                ANS[i] = (B-A)%mod;
            }
            else if (r==4){
                ANS[i] = (mod-A)%mod;
            }
            else if (r==5){
                ANS[i] = (mod-B)%mod;
            }
    }
    for (long long int i=0; i< T; i++){
            if (ANS[i] < 0){
                cout << mod+ANS[i] << endl;
            }
            else{
                cout << ANS[i] << endl;
            }
    }
    return 0;
}
