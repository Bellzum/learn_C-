#include <iostream>
#include <cmath>
using namespace std;

int main() {
    // Dimensions
    float cubeSide     = 5.4f;
    float sphereRadius = 2.33f;
    float coneRadius   = 7.65f;
    float coneHeight   = 14.0f;

    // Volumes
    float volCube   = pow(cubeSide, 3);
    float volSphere = (4.0f / 3.0f) * static_cast<float>(M_PI) * pow(sphereRadius, 3);
    float volCone   = static_cast<float>(M_PI) * pow(coneRadius, 2) * (coneHeight / 3.0f);

    cout << "Cube volume:   " << volCube   << '\n';
    cout << "Sphere volume: " << volSphere << '\n';
    cout << "Cone volume:   " << volCone   << '\n';
    return 0;
}
