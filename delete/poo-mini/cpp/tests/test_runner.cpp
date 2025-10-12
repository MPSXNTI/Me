// Test runner minimalista sin frameworks externos
#include <iostream>
#include <stdexcept>
#include <string>
#include "../src/auto.h"
#include "../src/bicicleta.h"

int fails = 0;
#define ASSERT_TRUE(cond) do { if(!(cond)) { std::cerr << "ASSERT_TRUE falló: " #cond " (" << __FILE__ << ":" << __LINE__ << ")\n"; ++fails; } } while(0)
#define ASSERT_EQ(a,b) do { auto _a=(a); auto _b=(b); if(!((_a)==(_b))) { std::cerr << "ASSERT_EQ falló: " #a " vs " #b " => " << _a << " != " << _b << " (" << __FILE__ << ":" << __LINE__ << ")\n"; ++fails; } } while(0)

void test_encapsulamiento_y_movimiento() {
    Auto a("Toyota");
    Bicicleta b("Trek");
    a.acelerar(10); a.acelerar(5);
    b.acelerar(7);
    ASSERT_EQ(a.getVelocidad(), 15);
    ASSERT_EQ(b.getVelocidad(), 7);
    ASSERT_TRUE(a.mover().find("Auto Toyota") != std::string::npos);
    ASSERT_TRUE(b.mover().find("Bici Trek") != std::string::npos);
}

void test_frenar_no_negativo() {
    Auto a("Toyota");
    a.acelerar(10);
    a.frenar(15);
    ASSERT_EQ(a.getVelocidad(), 0);
}

void test_validacion_delta() {
    Auto a("Toyota");
    bool ok1=false, ok2=false;
    try { a.acelerar(-1); } catch(const std::invalid_argument&) { ok1=true; }
    try { a.frenar(-2); } catch(const std::invalid_argument&) { ok2=true; }
    ASSERT_TRUE(ok1 && ok2);
}

int main() {
    test_encapsulamiento_y_movimiento();
    test_frenar_no_negativo();
    test_validacion_delta();
    if (fails==0) {
        std::cout << "[OK] Todos los tests pasaron\n";
        return 0;
    } else {
        std::cerr << "[FAIL] " << fails << " tests fallaron\n";
        return 1;
    }
}
