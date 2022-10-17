
#ifndef PYTHON_CPP_WRAPPER_PERSON_HPP
#define PYTHON_CPP_WRAPPER_PERSON_HPP

#include <string>
#include <utility>

namespace ais2203 {

    class person {

    public:
        person(std::string firstName, std::string lastName);

        std::string firstName() const;
        std::string lastName() const;

    private:
        std::string firstName_;
        std::string lastName_;

    };

}

#endif //PYTHON_CPP_WRAPPER_PERSON_HPP
