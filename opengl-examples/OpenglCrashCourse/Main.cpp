#include <iostream>
#include<glad/glad.h>
#include<GLFW/glfw3.h>

// Vertex Shader source code
const char* vertexShaderSource = "#version 330 core\n"
"layout (location = 0) in vec3 aPos;\n"
"void main()\n"
"{\n"
"   gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n"
"}\0";
//Fragment Shader source code
const char* fragmentShaderSource = "#version 330 core\n"
"out vec4 FragColor;\n"
"void main()\n"
"{\n"
"   FragColor = vec4(0.8f, 0.3f, 0.02f, 1.0f);\n"
"}\n\0";

int main() {

	/*
	now we create the window by using GLFWINIT to intilise the window
	*/
	glfwInit();
	// tell GLFW what version of OPENGL we are using
	// we are using the newest version
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 4);
	// tell GLFW we are using the CORE profile
	// so that means we only have the modern functions
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	GLfloat vertices[] =
	{
		-0.5f, -0.5f * float(sqrt(3)) / 3, 0.0f,
		0.5f, -0.5f * float(sqrt(3)) / 3, 0.0f,
		0.0f, 0.5f * float(sqrt(3)) * 2 / 3, 0.0f
	};

	// all opengl objects are opened by a reference

	// create a GLFW window object of 800 by 800 pixels
	// naming it "jadeOpenGl"
	// error check if the window fails to create
	GLFWwindow* window = glfwCreateWindow(800, 800, "jadeOpenGl", NULL, NULL);
	if (window == NULL) {
		std::cout << "Failed to create GUI window" << std::endl;
		glfwTerminate();
		return -1;
	}

	// introduce the window into the current context
	glfwMakeContextCurrent(window); 

	// load GLAD so it configures OpenGl
	gladLoadGL();

	// specify the viewport of OpenGl in the window
	// In this case the viewport goes from x=0, y=0 to x=800 y=800
	glViewport(0, 0, 800, 800);

	GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
	glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
	glCompileShader(vertexShader);

	GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
	glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
	glCompileShader(fragmentShader);

	GLuint shaderProgram = glCreateProgram();

	glAttachShader(shaderProgram, vertexShader);
	// specify the color of the background
	glClearColor(0.07f, 0.13f, 0.17f, 1.0f);
	// clean the back buffer and assgn the new color to it
	glClear(GL_COLOR_BUFFER_BIT);
	// swap the back buffer with the front buffer
	glfwSwapBuffers(window);
	
	
	while (!glfwWindowShouldClose(window)) {
		glfwPollEvents();
	}

	glfwDestroyWindow(window);
	// we should also terminate it at the end of the function
	glfwTerminate();
	return 0;
}