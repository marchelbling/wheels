cmake_minimum_required(VERSION 3.11)
project(ObabelPythonDistributions CXX)

# https://scikit-build-core.readthedocs.io/en/latest/getting_started.html#cmake-file
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
find_package(SWIG COMPONENTS python REQUIRED)
include(UseSWIG)

set(CMAKE_INSTALL_PREFIX ${SKBUILD_PLATLIB_DIR})
set(PYTHON_INSTDIR ${SKBUILD_PLATLIB_DIR})

# download OpenBabel to ${OBABEL_SOURCE_ROOT}
include(FetchContent)
FetchContent_Declare(openbabel
    GIT_REPOSITORY    https://github.com/openbabel/openbabel
    GIT_TAG           ${OBABEL_VERSION}
)
FetchContent_MakeAvailable(openbabel) # this will fetch the repository synchronously and expose ${openbabel_SOURCE_DIR} variable
