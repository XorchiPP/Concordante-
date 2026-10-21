// Concordante Lab · Xorch · © 2026. Todos los derechos reservados.
// Independent marked-transition orbit census for dinamica_dos_puertos.
// Rebuilds all four directed multigraphs by direct toppling rules.
// Reads only recurrence bitset for selecting the recurrent initial states.
#include <vector>
#include <array>
#include <map>
#include <queue>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <cassert>
#include <cstdint>
using namespace std;
using Mat=array<array<int,9>,9>;
void ensure(bool c,const char*m){if(!c)throw runtime_error(m);}
Mat construct(int kind){
 bool strict=kind<2,out=kind%2==0;
 Mat d{};for(int i=0;i<9;++i)d[i][i]=4;
 for(int i=1;i<=7;++i)for(int j=1;j<=7;++j)
  if(abs(i/3-j/3)+abs(i%3-j%3)==1)d[j][i]=-1;
 for(auto x:vector<pair<int,int>>{{2,1},{6,7}}){d[x.second][x.first]--;d[x.first][x.second]++;}
 int weight=strict?2:1;
 for(auto x:vector<pair<int,int>>{{0,1},{0,3},{8,5},{8,7}}){
  if(out)d[x.second][x.first]-=weight;
  else d[x.first][x.second]-=weight;
 }
 return d;
}
int st_add(Mat const& d,int code,int source){
 int h[9]={0};for(int i=0;i<9;++i)h[i]=(code>>(2*i))&3;
 ++h[source];
 int passes=0;
 for(;;){bool any=false;
  for(int j=0;j<9;++j){int n=h[j]/4;if(!n)continue;any=true;h[j]-=n*4;
   for(int i=0;i<9;++i)if(i!=j&&d[i][j]<0)h[i]-=n*d[i][j];}
  if(!any)break;ensure(++passes<2000,"toppling infinite");
 }
 int out=0;for(int i=0;i<9;++i){ensure(h[i]>=0&&h[i]<=3,"invalid final height");out|=h[i]<<(2*i);}return out;
}
int main(int argc,char** argv){
 try{
 ensure(argc==2,"usage: orbitas_marcadas recurrencia_fifo.bin");
 ifstream in(argv[1],ios::binary);vector<unsigned char> bit((istreambuf_iterator<char>(in)),istreambuf_iterator<char>());
 ensure(bit.size()==4u*(1u<<15),"bitset length wrong");
 int expected_rec=167040;
 for(int mode=0;mode<4;++mode){
   Mat d=construct(mode);auto isrec=[&](int c){return ((bit[mode*(1<<15)+(c>>3)]>>(c&7))&1)!=0;};
   int recurrent_total=0;for(int c=0;c<(1<<18);++c)recurrent_total+=isrec(c);
   ensure(recurrent_total==expected_rec,"bad membership input");
   map<int,int> source_lengths[2];
   for(int which=0;which<2;++which){
     int src=which==0?0:8;
     vector<unsigned char> visited(1<<18,0);
     for(int c=0;c<(1<<18);++c){if(!isrec(c)||visited[c])continue;
       int cur=c, len=0;
       do{ensure(isrec(cur),"addition left recurrent set");ensure(!visited[cur],"non-permutation tail or cycle!");visited[cur]=1;
          cur=st_add(d,cur,src);++len;ensure(len<=167040,"cycle bound");
       }while(cur!=c);
       source_lengths[which][len]++;
     }
     int64_t n=0;for(auto [size,count]:source_lengths[which])n+=(int64_t)size*count;
     ensure(n==expected_rec,"source cycles incomplete");
   }
   vector<unsigned char> visited(1<<18,0);map<int,int> joint_lengths;
   for(int c=0;c<(1<<18);++c){if(!isrec(c)||visited[c])continue;
    vector<int> bfs{c};visited[c]=1;
    for(size_t i=0;i<bfs.size();++i){int from=bfs[i];
     for(int p:{0,8}){int dst=st_add(d,from,p);ensure(isrec(dst),"joint addition left recurrent set");
       if(!visited[dst]){visited[dst]=1;bfs.push_back(dst);}}
    }
    joint_lengths[(int)bfs.size()]++;
   }
   int64_t n=0;for(auto [size,count]:joint_lengths)n+=(int64_t)size*count;
   ensure(n==expected_rec,"joint orbits incomplete");
   map<int,int> want_single, want_joint;
   switch(mode){
     case 0:want_single={{6960,24}};want_joint={{83520,2}};break;
     case 1:want_single={{4,41760}};want_joint={{16,10440}};break;
     case 2:want_single={{13920,12}};want_joint={{167040,1}};break;
     case 3:want_single={{4,41760}};want_joint={{16,10440}};break;
   }
   ensure(source_lengths[0]==want_single && source_lengths[1]==want_single,"single cycle lattice disagreement");
   ensure(joint_lengths==want_joint,"joint orbit lattice disagreement");
   auto show=[](map<int,int> m){for(auto [length,n]:m)cout<<" ("<<length<<" x "<<n<<")";};
   cout<<"MODE "<<mode<<" single_port_0";show(source_lengths[0]);cout<<" single_port_8";show(source_lengths[1]);cout<<" joint";show(joint_lengths);cout<<" PASS\n";
 }
 cout<<"INDEPENDENT_MARKED_ORBIT_COMPLETE_PASS\n";
 }catch(exception const&e){cerr<<"FAILED "<<e.what()<<"\n";return 1;}
}
