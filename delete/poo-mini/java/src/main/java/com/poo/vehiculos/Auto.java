package com.poo.vehiculos;

public class Auto extends Vehiculo {
    public Auto(String marca) { super(marca); }
    @Override public String mover() {
        return "Auto " + getMarca() + " avanza a " + getVelocidad() + " km/h.";
    }
}
