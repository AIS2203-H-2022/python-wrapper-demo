
#include <utility>

#include "ais2203/person.hpp"

using namespace ais2203;

person::person(std::string firstName, std::string lastName)
        : firstName_(std::move(firstName)),
          lastName_(std::move(lastName)) {}

std::string person::firstName() const {
    return firstName_;
}

std::string person::lastName() const {
    return lastName_;
}
