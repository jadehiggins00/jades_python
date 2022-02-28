#include <iostream>
#include<glad/glad.h>
#include<GLFW/glfw3.h>

int main() {

	/*
	now we create the window by using GLFWINIT to intilise the window
	*/
	glfwInit();
	// this is a hint for the version of opengl
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 4);
	//glfwWindowHint(GLFW_OPENGL_PROFILE, )
	// we should also terminate it at the end of the function
	glfwTerminate();
	return 0;
}