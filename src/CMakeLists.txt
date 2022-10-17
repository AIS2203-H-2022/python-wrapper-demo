
set(sources
        "ais2203/person.cpp"
        )

add_library(person ${sources})
target_include_directories(person
        PUBLIC
        "${CMAKE_SOURCE_DIR}/include"
        )

set(csources
        "ais2203/personc.cpp"
        )

add_library(personc SHARED ${csources})


