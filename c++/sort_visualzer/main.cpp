#include <SDL2/SDL.h>
#include <iostream>
#include <random>
#include <ranges>
#include <algorithm>



  void draw_state(std::vector<int>& v,SDL_Renderer* renderer, unsigned int red, unsigned int blue) {
    int index = 0;
    for(int i : v){
      SDL_SetRenderDrawColor(renderer, 150,155,155,255);
      if(index==red) SDL_SetRenderDrawColor(renderer, 255,0,0,255);
      if(index==blue) SDL_SetRenderDrawColor(renderer, 0,0,255,255);
      SDL_RenderDrawLine(renderer,index,99,index,i);
      index += 1;
    }
  }


int main(){
  std::random_device rd;
  std::uniform_int_distribution d(1,99);
  std::vector<int> v;
  



  for(int i = 0;i < 100;i++) {
    v.push_back(d(rd));
  }

  SDL_Window* window = nullptr;
  SDL_Renderer* renderer = nullptr;
  SDL_CreateWindowAndRenderer(300,300,0,&window, &renderer);
  SDL_RenderSetScale(renderer,3,3);

  
  for(int i=0;i<v.size();i++){
    for(int j=i;j<v.size();j++){
      if (v[j]<v[i])  std::swap(v[i],v[j]);
      SDL_SetRenderDrawColor(renderer,255,255,255,255);
      SDL_RenderClear(renderer);
      draw_state(v,renderer,i,j);
      SDL_RenderPresent(renderer);
      //SDL_Delay(1);
    }
  }

  for(int i : v){
     std::cout << i << " "; //std::endl;
  }

  if(std::ranges::is_sorted(v)) std::cout<<std::endl<<"sorted"<<std::endl;



  return 0;
}
