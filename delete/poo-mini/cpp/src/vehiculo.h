#pragma once
#include <string>
#include <algorithm>

class Vehiculo {
private:
    std::string marca;
    int velocidad;
public:
    explicit Vehiculo(std::string m) : marca(std::move(m)), velocidad(0) {}
    virtual ~Vehiculo() = default;

    const std::string& getMarca() const { return marca; }
    int getVelocidad() const { return velocidad; }

    void acelerar(int delta) {
        if (delta < 0) throw std::invalid_argument("delta debe ser >= 0");
        velocidad += delta;
    }
    void frenar(int delta) {
        if (delta < 0) throw std::invalid_argument("delta debe ser >= 0");
        velocidad = std::max(0, velocidad - delta);
    }

    virtual std::string mover() const = 0;
};
