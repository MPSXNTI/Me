#include <iostream>
#include <memory>
#include <vector>
#include "auto.h"
#include "bicicleta.h"

int main() {
    std::vector<std::unique_ptr<Vehiculo>> flota;
    flota.emplace_back(std::make_unique<Auto>("Toyota"));
    flota.emplace_back(std::make_unique<Bicicleta>("Trek"));
    flota[0]->acelerar(50);
    flota[1]->acelerar(20);
    for (const auto& v : flota) std::cout << v->mover() << "\n";
    return 0;
}
