****Image Reconstruction with Primitive Shapes****

This project demonstrates the process of recreating a target image using a set of up to 100 primitive shapes, either circles or triangles. The challenge lies in optimizing these shapes to recreate the image as closely as possible. You can find similar examples of this task on YouTube for Circles and Triangles.

**Project Goal**

The primary objective is to implement a working Python demo that employs Object-Oriented Programming principles and features clean, well-documented code. The code is designed to optimize the placement and characteristics of the shapes to best match the target image. The optimization schemes employed in this project could include Genetic Algorithms and Simulated Annealing, although due to time constraints, the implementation may focus on one of these.

**Constraints**

The project focuses on writing clean, optimized code that doesn't rely on existing libraries for the implementation of the optimization algorithms. The code should be efficient enough to run within 5 minutes on a standard laptop, necessitating thoughtful optimizations and effective design patterns. All code is written from scratch, without using pre-existing solutions.

**Project Structure**

In order to make the code clear and maintainable, it is organized into relevant classes and interfaces. The project structure follows well-known design patterns to ensure scalability and modularity.

**Reporting**

The project includes a detailed report in PDF format, describing the solution and explaining the chosen optimization and heuristic functions. The architecture of the code is also outlined to facilitate understanding and further development.

**Implementation Overview**

_Software Architecture Overview:_

This project emphasizes a high degree of professionalism, focusing on flexibility and the potential for future reuse and maintenance. The design incorporates a modular approach, where components are decoupled and object-oriented programming principles, such as inheritance and design patterns, are extensively employed.

Tunable program parameters are defined in the GlobalDefinitions file for convenience. In addition, a debug mode can be activated in the same file to output running progress to the console. The following design patterns are implemented in the project: Model-View-Controller (MVC), Factory, and Strategy.

_Optimization scheme_

During the development process, I experimented with a few variations of optimization schemes. One such scheme was adopted from a project found online that implemented a genetic algorithm. However, its performance was sub-optimal due to inefficiencies in computation and precision. This was primarily due to the algorithm's strategy of comparing the entire image after each generation cycle.

To rectify this, I implemented an intuitive solution inspired by the examples in the YouTube videos. This solution proved to be more efficient and precise.

Algorithm in general:
Implements an Optimization Scheme in the most basic way:
- Each cycle a random shape is generated
- The shape is compared to the reference image loaded by the user
- It is compared based on pixel colors in the shape coordinates and the ref image
- If the generation is good enough it is drawn
- 'Good enough' is defined by: for each color average difference (r,g,b) test whether it less then pre defined MAX_ALLOWED_ERROR_PERCENT

_Results Overview_

With some fine-tuning and the implementation of heuristics, the algorithm successfully achieves its objective. It quickly reaches a satisfactory level of precision before experiencing a slowdown in progress, exhibiting a logarithmic learning curve. While there is scope for further improvements, due to time constraints, the current state of the project offers a working solution that is quite efficient.


_Files and Classes:_

•	File __ImageEvolution.py – holds the program entry point (main)

•	Global object variable Log – prints standard logging and errors to the console

•	Class ProgramProgress – counters and time stamps that represent algorithm progress

•	File GlobalDefintions.py – definition variables needed for module of the program

•	File ShapesFactory.py – holds geometric shapes handling logic

•	Class AbstractShape – defines a generic geometric shape

•	Class Circle – defines a circle geometric shape. Implements AbstractShape interface

•	Class AbstractShapeFactory – Creates and returns a Shape. Factory design pattern

•	Class CircleShapeFactory – Creates and returns a Circle . Implements AbstractShapeFactory interface. Factory design pattern

•	Class Randomizer – encapsulates logic of generating random values for shape creation

•	File OptimizationScheme.py – holds optimization scheme strategies

•	Class OptimizationSchemeContext – wraps optimization scheme. Strategy design pattern  

•	Class OptimizationSchemeStrategy – interface for abstract optimization scheme algorithm strategies. Strategy design pattern  

•	File NeighboorColorsScheme.py –

•	Class NeighboorColorsScheme  – implements OptimizationSchemeStrategy in a way of neighbor pixels comparison

•	File ImageHandler.py – holds the logic behind Image handling

•	Class ImageWrapper – encapsulates image handling. Is implemented using OpenCV underneath

•	File DrawHandler.py – holds the logic behind the drawing

•	Class AbstractDrawer – interface for 2D graphics drawing

•	Class PILDrawer – implements AbstractDrawer interface. Is implemented using PIL lib

•	Class PILDrawerCircle – implements Circle drawing logic. Inherits from PILDrawer

•	File GUIMainWindow.py – encapsulates window display handling

•	Class AbstractDisplay – interface for window and canvas handling

•	Class TkDisplay – implements AbstractDisplay. Is implemented using Tk lib

•	Class MainGUI – starts a thread for the GUI representation

•	Class MainGUIView – Main GUI window view. MVC design pattern.

•	Class MainGUIController – Main GUI window controller. MVC design pattern.

•	Class MainGUIModel – Main GUI window model. MVC design pattern.

