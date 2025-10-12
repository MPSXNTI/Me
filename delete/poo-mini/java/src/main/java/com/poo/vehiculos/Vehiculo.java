package com.poo.vehiculos;

public abstract class Vehiculo {
    private final String marca;
    private int velocidad;

    public Vehiculo(String marca) {
        this.marca = marca;
        this.velocidad = 0;
    }
    public String getMarca() { return marca; }
    public int getVelocidad() { return velocidad; }

    public void acelerar(int delta) {
        if (delta < 0) throw new IllegalArgumentException("delta debe ser >= 0");
        this.velocidad += delta;
    }
    public void frenar(int delta) {
        if (delta < 0) throw new IllegalArgumentException("delta debe ser >= 0");
        this.velocidad = Math.max(0, this.velocidad - delta);
    }

    public abstract String mover();
}
