#pragma once
#include "vehiculo.h"
#include <string>

class Bicicleta : public Vehiculo {
public:
    using Vehiculo::Vehiculo;
    std::string mover() const override {
        return "Bici " + getMarca() + " pedalea a " + std::to_string(getVelocidad()) + " km/h.";
    }
};
