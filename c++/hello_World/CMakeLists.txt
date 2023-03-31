cmake_minimum_required(VERSION 3.22)
project(helloWorld
VERSION 1.0
DESCRIPTION "Hello World"
LANGUAGES CXX)
#include_directories(.)
add_executable(main main.cpp utils.cpp utils.h)