#include <SDL2/SDL.h>
#include <vector>
#include <iostream>

int main(){

    std::cout << " \nPress q to exit, c to clear data,\n1 to increase depth, 2 to decrease depth\nLeft click to add points\n";

    SDL_Init(SDL_INIT_EVERYTHING);
    SDL_Window *window = nullptr;
    SDL_Renderer *renderer = nullptr;
    SDL_CreateWindowAndRenderer(600, 600, 0, &window, &renderer);
    SDL_Event event;
    SDL_Point current;
    std::vector<SDL_Point> points_history;
    int depth=1;
    while (true)
    {
        while(SDL_PollEvent(&event)){
          switch(event.type){
            case SDL_QUIT:
                SDL_Quit();
                exit(0);
                break;
            case SDL_MOUSEBUTTONDOWN:
                int x, y;
                SDL_GetMouseState(&x, &y);
                if(event.button.button == SDL_BUTTON_LEFT)
                    points_history.emplace_back(x, y);
                break;

            case SDL_MOUSEMOTION:
                SDL_GetMouseState(&current.x, &current.y);
                break;
            case SDL_KEYDOWN:
                switch(event.key.keysym.sym){
                    case SDLK_c:
                        points_history.clear();
                        break;
                    case SDLK_1:
                        depth++;
                        break;
                    case SDLK_2:
                        depth--;
                        break;

                    case SDLK_q:
                        SDL_Quit();
                        exit(0);
                    }

                break;
            }
        }

        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderClear(renderer);
        SDL_SetRenderDrawColor(renderer, 100, 100, 255, 255);
        // SDL_RenderDrawLines(renderer, points_history.data(), points_history.size());
        for (int i = 0; i < points_history.size();i++)
        
            for (int j = i - depth < 0 ? 0 : i - depth; j <= i;j++)
                                SDL_RenderDrawLine(renderer, points_history[i].x, points_history[i].y,  points_history[j].x,  points_history[j].y);
        
        SDL_RenderPresent(renderer);
        SDL_Delay(150);
    }
    return 0;
}