# LambdaCalculator

To Use Code:

The README is split into multiple sections, all of which can be found below. To run the tool, you'll need:
    - At least Java 1.7
    - Python3
    - ANTLR (installation instructions below)
    - FLASK (installation instructions below)

Install and setup ANTLR4
    - To do this, you'll need at least Java 1.7 installed (since the back-end of ANTLR is Java and not Python)
    - Follow the steps in this link in section "1. Setup ANTLR" https://tomassetti.me/antlr-mega-tutorial/#setup-antlr
    - Get ANTLR for python using "pip install antlr4-python3-runtime" (using a virtual environment if you want - see steps at the bottom of this README section)
    - Run the following commands from the main directory containing the LambdaCalculus.g4 file
        antlr4 LambdaCalculus.g4
        antlr4 -Dlanguage=Python3 LambdaCalculus.g4 -visitor
    - OPTIONAL: To view an abstract syntax tree of a lambda term do:
        antl4 -Dlanguage=Java LambdaCalculus.g4
        javac *.java
        grun LambdaCalculus term -gui
        -- and then type a lambda term, press enter, and then hit CTRL-Z --
        -- The abstract syntax tree will appear in a separate window --
    - OPTIONAL: To run the code from the command line, run "python LambdaCalculus.py", enter either "a", "v", or "n" for alpha-reduction, call-by-value or call-by-name, then enter your lambda term which is to be reduced. The resultant expression will appear
    For more information on ANTLR, look at https://tomassetti.me/antlr-mega-tutorial/#setup-antlr

Install FLASK - using a virtual environemnt if you want (see below) (recommended)
    - Once you have a virtual environment (optional) run "pip install flask" to get FLASK
    - Then do "flask run" to get the webpage up and running
    - Visit "localhost:5000" in a browser to view the webpage
    For more information, look at https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

INSTALLING A VIRTUAL ENVIRONMENT -- Windows
- From the command line, navigate to the code directory
- Run "python3 -m venv venv"
- Run "venv\Scripts\activate"
- You should now have a virtual environment up and running
For more information, or for instructions on MAC, refer to the virtual environment steps in the following links:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

**********************************************************

FILE INFORMATION
Files Created By Yola
    - everything in testing folder (used for unit-tests)
    - everything in app folder (used for web-interface)
    - AlphaCalculatorFromComplete.py (alpha conversion)
    - AlphaCalculatorPartial.py (alpha conversion)
    - AlphaConversionVisitor.py (alpha conversion)
    - BaseVisitor.py (base beta visitor)
    - BracketCheck.py (support file used by other classes)
    - CallByNameVisitor.py (beta reduction)
    - CallByValueVisitor.py (beta reduction)
    - DeltaReductionVisitor.py (arithmetic evaluation)
    - LamdaCalculus.g4 (grammar file)
    - LambdaCalculus.py (MAIN RUNNABLE FILE)
    - LambdaSessionInformationObject.py (support file used by other classes)
    - interface_runner.py (used to launch web interface)

File Credit Given to https://www.sanfoundry.com/python-program-implement-stack
    - Stack.py (used by other classes)

Files Created (or auto-generated) By ANTLR
    - LambdaCalculusLexer.java
    - LambdaCalculusParser.java
    - LambdaCalculusVisitor.py
    - LambdaCalculusLexer.py
    - LambdaCalculusVisitor.py

