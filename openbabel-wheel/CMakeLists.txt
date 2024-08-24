cmake_minimum_required(VERSION 3.11)
project(ObabelPythonDistributions CXX)

# https://scikit-build-core.readthedocs.io/en/latest/getting_started.html#cmake-file
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
find_package(SWIG COMPONENTS python REQUIRED)
include(UseSWIG)


# download OpenBabel to ${OBABEL_SOURCE_ROOT}
include(FetchContent)
FetchContent_Declare(openbabel
  GIT_REPOSITORY    https://github.com/openbabel/openbabel
  GIT_TAG           ${OBABEL_VERSION}
)
FetchContent_GetProperties(openbabel)
if(NOT openbabel_POPULATED)
  FetchContent_Populate(openbabel)
  add_subdirectory(${openbabel_SOURCE_DIR} ${openbabel_BINARY_DIR})

  # we assume that the python library is installed at the default location
  if (EXISTS "${openbabel_SOURCE_DIR}/scripts/python/openbabel")
	  install(
	    DIRECTORY "${openbabel_SOURCE_DIR}/scripts/python/openbabel"
	    DESTINATION ${CMAKE_INSTALL_PREFIX}/openbabel
	  )
  endif()
endif()
