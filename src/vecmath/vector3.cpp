
#include "vecmath/vector3.hpp"

using namespace vecmath;

vector3::vector3() : vector3(0, 0, 0) {}

vector3::vector3(float x, float y, float z)
        : x(x), y(y), z(z) {}

vector3 vector3::operator+(const vecmath::vector3 &other) const {
    return {x + other.x, y + other.y, z + other.z};
}

vector3 vector3::operator-(const vector3 &other) const {
    return {x - other.x, y - other.y, z - other.z};
}

vector3 vector3::operator/(const vector3 &other) const {
    return {x / other.x, y / other.y, z / other.z};
}

vector3 vector3::operator*(const vector3 &other) const {
    return {x * other.x, y * other.y, z * other.z};
}
