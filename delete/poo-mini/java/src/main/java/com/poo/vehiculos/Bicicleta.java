package com.poo.vehiculos;

public class Bicicleta extends Vehiculo {
    public Bicicleta(String marca) { super(marca); }
    @Override public String mover() {
        return "Bici " + getMarca() + " pedalea a " + getVelocidad() + " km/h.";
    }
}
