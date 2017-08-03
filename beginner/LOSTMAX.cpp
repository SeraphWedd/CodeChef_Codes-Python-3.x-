#include<iostream>

using namespace std; int main() { int T,N,max; cin>>T; //cin>>N;
int A[51]; max=0; while(T) {
    N=0;
    do{
            cin >> A[N];
            cout << A[N] << " input" << endl;
            N++;
    } while (A[N-1] != '\n');
    cout << A << " input" << endl;
    for(int i=0;i<N;i++)
    {
        cout << A[i] <<" " << N << endl;
        if(A[i]==N-1){}
        else if(A[i]>max){
            max=A[i];
        }
    }
    T--;
}
cout<<max<<endl;
return 0;

}
