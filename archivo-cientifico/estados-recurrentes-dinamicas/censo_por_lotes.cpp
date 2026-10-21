// Concordante Lab · Xorch · © 2026. Todos los derechos reservados.
// dinamica_dos_puertos second, independently reconstructed, batch-toppling full census.
// Does NOT read matrices or scripts from the primary implementation.
// Uses script multiplied by two to audit script independence.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <cstdint>
using namespace std;
using Mat=array<array<int,9>,9>;
void check(bool q,const char*m){if(!q)throw runtime_error(m);}
Mat construct(bool strict,bool outward){
 Mat d{};for(int i=0;i<9;++i)d[i][i]=4;
 const int W[]={1,2,3,4,5,6,7};
 for(int u:W)for(int v:W)if(abs(u/3-v/3)+abs(u%3-v%3)==1)d[v][u]=-1;
 for(auto pr: vector<pair<int,int>>{{2,1},{6,7}}){d[pr.second][pr.first]-=1;d[pr.first][pr.second]+=1;}
 const int weight=strict?2:1;
 for(auto pr:vector<pair<int,int>>{{0,1},{0,3},{8,5},{8,7}}){if(outward)d[pr.second][pr.first]-=weight;else d[pr.first][pr.second]-=weight;}
 return d;
}
void script(const Mat&d,int sigma[9],int beta[9]){
 for(int i=0;i<9;++i)sigma[i]=1;
 for(int k=0;k<100;++k){
  for(int i=0;i<9;++i){beta[i]=0;for(int j=0;j<9;++j)beta[i]+=d[i][j]*sigma[j];}
  int neg=-1;for(int i=0;i<9;++i)if(beta[i]<0){neg=i;break;}
  if(neg<0){for(int i=0;i<9;++i){beta[i]*=2;sigma[i]*=2;}return;}
  ++sigma[neg];
 }
 throw runtime_error("greedy script failed");
}
bool recurrent_batch(const Mat&d,int code,const int sigma[9],const int beta[9]){
 int v[9]={0},od[9]={0};
 for(int i=0;i<9;++i)v[i]=((code>>(2*i))&3)+beta[i];
 int loops=0;
 for(;;){bool any=false;
  for(int j=8;j>=0;--j){int times=v[j]/4;if(times==0)continue;any=true;od[j]+=times;v[j]-=4*times;
   for(int i=0;i<9;++i)if(i!=j&&d[i][j]<0)v[i]-=times*d[i][j];}
  if(!any)break;check(++loops<100000,"batch stabilization failed");
 }
 for(int i=0;i<9;++i)if(v[i]!=((code>>(2*i))&3)||od[i]!=sigma[i])return false;
 return true;
}
int main(int argc,char**argv){
 try{check(argc==2,"usage: censo_por_lotes recurrencia_lotes.bin");
 vector<unsigned char> output(4*(1<<15),0);int64_t examined=0;
 for(int k=0;k<4;++k){bool strict=k<2;bool outward=k%2==0;
  Mat d=construct(strict,outward);int sig[9],beta[9];script(d,sig,beta);int count=0;
  for(int c=0;c<(1<<18);++c){bool good=recurrent_batch(d,c,sig,beta);++examined;
   if(good){++count;output[k*(1<<15)+(c>>3)]|=1u<<(c&7);}}
  check(count==167040,"independent recurrence mismatch");
  cout<<"INDEPENDENT_BATCH variant="<<k<<" recurrent="<<count<<"\n";
 }
 ofstream out(argv[1],ios::binary);out.write((char*)output.data(),output.size());check(bool(out),"write error");
 cout<<"INDEPENDENT_COMPLETE all="<<examined<<" bytes="<<output.size()<<"\n";
 }catch(exception const&e){cerr<<"ERROR "<<e.what()<<"\n";return 1;}
}
