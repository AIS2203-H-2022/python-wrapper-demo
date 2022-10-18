
#ifndef PYTHON_CPP_WRAPPER_VECTOR3_HPP
#define PYTHON_CPP_WRAPPER_VECTOR3_HPP

namespace vecmath {

    class vector3 {

    public:
        float x;
        float y;
        float z;

        vector3();
        vector3(float x, float y, float z);

        vector3 operator +(const vector3& other) const;
        vector3 operator -(const vector3& other) const;
        vector3 operator /(const vector3& other) const;
        vector3 operator *(const vector3& other) const;

    };

}

#endif //PYTHON_CPP_WRAPPER_VECTOR3_HPP
