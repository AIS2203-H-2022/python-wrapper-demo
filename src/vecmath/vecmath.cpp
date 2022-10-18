
#include "vecmath/vecmath.h"

#include "vecmath/vector3.hpp"
#include "vecmath/matrix4.hpp"

#include <memory>


namespace {

    vector3 ctype(const vecmath::vector3 &v) {
        return {v.x, v.y, v.z};
    }

    vecmath::vector3 cpptype(const vector3 &v) {
        return {v.x, v.y, v.z};
    }
}

struct vecmath_matrix4 {
    std::unique_ptr<vecmath::matrix4> cpp_matrix;
};


vector3 vector3_add(vector3 v1, vector3 v2) {
    return ctype(cpptype(v1) + cpptype(v2));
}

vector3 vector3_sub(vector3 v1, vector3 v2) {
    return ctype(cpptype(v1) + cpptype(v2));
}

vector3 vector3_div(vector3 v1, vector3 v2) {
    return ctype(cpptype(v1) + cpptype(v2));
}

vector3 vector3_mul(vector3 v1, vector3 v2) {
    return ctype(cpptype(v1) + cpptype(v2));
}

vecmath_matrix4_t *matrix4_create() {
    auto m = std::make_unique<vecmath_matrix4_t>();
    m->cpp_matrix = std::make_unique<vecmath::matrix4>();
    return m.release();
}

void matrix4_identity(vecmath_matrix4_t *m) {
    m->cpp_matrix->identity();
}

void matrix4_set_position(vecmath_matrix4_t *m, float x, float y, float z) {
    m->cpp_matrix->set_position(x, y, z);
}

const float *matrix4_data(vecmath_matrix4_t *m) {
    return m->cpp_matrix->elements.data();
}

