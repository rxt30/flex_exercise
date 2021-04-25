set(BUILD_DIR build)
set(SOURCE_DIR sources)

cmake_minimum_required(VERSION 3.20)

project(Compiler)

find_package(BISON)
find_package(FLEX)

BISON_TARGET(Parser ${SOURCE_DIR}/yacc/syntax.y ${BUILD_DIR}/syntax.c)
FLEX_TARGET(Scanner ${SOURCE_DIR}/lex/flex.lex ${BUILD_DIR}/scanner.c)
ADD_FLEX_BISON_DEPENDENCY(Scanner Parser)

include_directories(${BUILD_DIR})
add_executable(Compiler
    ${BISON_Parser_OUTPUTS}
    ${FLEX_Scanner_OUTPUTS}
)
#target_link_libraries(Compiler ${FLEX_LIBRARIES})
