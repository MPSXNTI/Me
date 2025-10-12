#pragma once
#include "vehiculo.h"
#include <string>

class Auto : public Vehiculo {
public:
    using Vehiculo::Vehiculo;
    std::string mover() const override {
        return "Auto " + getMarca() + " avanza a " + std::to_string(getVelocidad()) + " km/h.";
    }
};
