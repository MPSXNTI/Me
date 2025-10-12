cmake_minimum_required(VERSION 3.20)
project(poo_vehiculos CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(vehiculos
    src/vehiculo.h
    src/auto.h
    src/bicicleta.h
)
target_include_directories(vehiculos PUBLIC src)

add_executable(app src/main.cpp)
target_link_libraries(app vehiculos)

add_executable(tests tests/test_runner.cpp)
target_link_libraries(tests vehiculos)
