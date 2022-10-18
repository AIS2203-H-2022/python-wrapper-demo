
#ifndef PYTHON_CPP_WRAPPER_VECMATH_HPP
#define PYTHON_CPP_WRAPPER_VECMATH_HPP

// this is a pure C source file

#ifdef __cplusplus
extern "C" {
#endif

typedef struct vecmath_matrix4 vecmath_matrix4_t;

struct vector3 {
    float x, y, z;
};

vector3 vector3_add(vector3 v1, vector3 v2);
vector3 vector3_sub(vector3 v1, vector3 v2);
vector3 vector3_div(vector3 v1, vector3 v2);
vector3 vector3_mul(vector3 v1, vector3 v2);


vecmath_matrix4_t *matrix4_create();
void matrix4_identity(vecmath_matrix4_t *m);
void matrix4_set_position(vecmath_matrix4_t *m, float x, float y, float z);
const float *matrix4_data(vecmath_matrix4_t *m);

#ifdef __cplusplus
} // extern(C)
#endif

#endif //PYTHON_CPP_WRAPPER_VECMATH_HPP
