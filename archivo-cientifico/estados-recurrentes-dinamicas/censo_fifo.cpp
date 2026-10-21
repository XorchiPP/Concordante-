// Concordante Lab · Xorch · © 2026. Todos los derechos reservados.
// dinamica_dos_puertos independent FIFO one-topple exact census.
// Reads 4 matrices and burning scripts from casos.txt; computes all 4^9 states.
#include <array>
#include <vector>
#include <queue>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <cstdint>
using namespace std;
struct Net {int n;vector<vector<int>> D;vector<int> sigma,beta;};
void check(bool ok,const string& msg){if(!ok)throw runtime_error(msg);}
Net core(const Net& x){
 const int coords[7]={1,2,3,4,5,6,7};Net y{7,vector<vector<int>>(7,vector<int>(7)),vector<int>(7,1),vector<int>(7)};
 for(int i=0;i<7;++i)for(int j=0;j<7;++j)y.D[i][j]=x.D[coords[i]][coords[j]];
 for(int i=0;i<7;++i)for(int j=0;j<7;++j)y.beta[i]+=y.D[i][j];
 return y;
}
bool recurrent_fifo(const Net& net,int code,int* odometer_out=nullptr){
 const int n=net.n;
 int h[9]={0},ods[9]={0};queue<int> unstable;
 for(int i=0;i<n;++i){h[i]=((code>>(2*i))&3)+net.beta[i]; if(h[i]>=4)unstable.push(i);}
 long long it=0;
 while(!unstable.empty()){
  int j=unstable.front();unstable.pop();if(h[j]<4)continue;
  h[j]-=4;++ods[j];if(h[j]>=4)unstable.push(j);
  for(int i=0;i<n;++i){if(i==j||net.D[i][j]>=0)continue;
    int old=h[i];h[i]-=net.D[i][j];if(old<4&&h[i]>=4)unstable.push(i);}
  check(++it<100000,"Nonterminating FIFO toppling");
 }
 for(int i=0;i<n;++i){if(h[i]!=((code>>(2*i))&3) || ods[i]!=net.sigma[i])return false;}
 return true;
}
int core_code(int full){int t=0;for(int i=1;i<=7;++i)t|=((full>>(2*i))&3)<<(2*(i-1));return t;}
int main(int argc,char**argv){
 try{
  check(argc==3,"usage: censo_fifo casos.txt recurrencia_fifo.bin");ifstream in(argv[1]);check(bool(in),"cases missing");
  int count;in>>count;check(count==4,"expected four variants");
  vector<Net> nets;
  for(int t=0;t<count;++t){Net n{9,vector<vector<int>>(9,vector<int>(9)),vector<int>(9),vector<int>(9)};
   for(int i=0;i<9;++i)for(int j=0;j<9;++j)in>>n.D[i][j];
   for(int i=0;i<9;++i)in>>n.sigma[i];for(int i=0;i<9;++i)in>>n.beta[i];
   check(bool(in),"truncated case");nets.push_back(n);
  }
  Net A=core(nets[0]);vector<unsigned char> corebits(1<<14,0);
  int core_count=0;for(int c=0;c<(1<<14);++c){bool ok=recurrent_fifo(A,c);corebits[c]=(unsigned char)ok;core_count+=ok;}
  check(core_count==10440,"core recurrence count mismatch");
  vector<unsigned char> full(count*(1<<15),0);int64_t evaluated=0;
  for(int t=0;t<count;++t){int cnt=0;int bad=0;
   for(int c=0;c<(1<<18);++c){bool rec=recurrent_fifo(nets[t],c);if(rec!=bool(corebits[core_code(c)]))++bad;
    if(rec)full[t*(1<<15)+(c>>3)]|=(unsigned char)(1u<<(c&7));cnt+=rec;++evaluated;}
   check(cnt==167040&&bad==0,"full recurrence disagrees with SCC product");
   cout<<"PRIMARY_FIFO variant="<<t<<" recurrent="<<cnt<<" mismatches="<<bad<<"\n";
  }
  ofstream out(argv[2],ios::binary);out.write((char*)full.data(),full.size());check(bool(out),"write error");
  cout<<"PRIMARY_COMPLETE exact_tests="<<evaluated+16384<<" full_memberships="<<evaluated<<" bytes="<<full.size()<<"\n";
 }catch(exception const&e){cerr<<"ERROR "<<e.what()<<"\n";return 1;}
}
