# arguments-and-perameters

Arguments and Parameters
=================================================
Parameters
-----------------
=>Parameters (Variables) are Classified into two Types. They are
			1) Formal Parameters------->Written in Function Heading
							            ---> Used for Holding OR Storing the Input coming Function Calls

			20 Local Parameters--------->written in Function Body
								            --> Used for Storing Temp Result as  Part of Function Processing Logic
>The Values of Formal Parameters and Local Parameters can be accesed within Corresponding Function Definition only But Not Possible to access in Other Part of Program.
----------------
Example

			def  sumop(a,b): # Function Definition--- Here a, b are called Formal Parameters
			     c=a+b		    # Here c is called Local Parameter
			     ----------
			     ----------
----------------------------------------------------------
Arguments
----------------------------------------------------------
=>Arguments are also called Actual Parameters.
=>Arguments are the Variables OR Values used inside of Function Calls and They are Considered as Inputs to 
    Function Definition.
			Example:       x=10
					           y=20
					           sumop(x,y) # Function Call--- Here x and y are called arguments
					       OR
					    sumop(100,200) # Function call--- Here 100 and 200 are called Argument Values
=>In the above example, the argument values x,y of Function call are passing formal Parameters a,b of Function 
   Definition.
=>Hence all values of argument(s) of Function call are passing to Parameter(s)  of Function  Definition.
=>The Process of Passing argument(s) of Function call to Parameter(s)  of Function  Definition is called Argument 
    Passing Mechanism.

  **Types of Arguments and Parameters**
	======================================================
=>We Know that, All values of argument(s) of Function call are passing to Parameter(s)  of Function  Definition.
=>The Process of Passing argument(s) of Function call to Parameter(s)  of Function  Definition is called Argument 
    Passing Mechanism.
=>In Python Programming, we have 5 Types of Arguments. They are

			1. Positional Arguments
			2. Default Arguments
			3. Keyword Arguments
			4. Variable Length Arguments
			5. Keyword Variable Length Arguments

  **1. Posstional Arguments**
=========================================================================
=>Posstional Arguments Mechanism is the default passing arguments  mechanism used by PVM in Functions for Passing the values of Arguments of Function Call to Formal Parameters of Function Defintion.
=>Possitional Arguments concept says that Every Argument  Value Passing to Every  Formal Parameter Based on their Posstion by maintaining Order and Meaning for Higher Accuracy. In Otherwords The number of arguments must be equal to Number of Formal Parameters.
=>Possitional Arguments concept always used for Passing Specific Data from Function calls to Function Definitions.
 =>PVM gives High Priority for Possitional Arguments
 
---------------------------------
Syntax:     def  functionname(Param1,Param2,....Param-n):  # Function Definition
			           -----------------------------------------------
			           -----------------------------------------------
			           Block of Statements--perform Operation
			           ------------------------------------------------
			          -----------------------------------------------
            functioname(arg1,arg2,.....,arg-n)  # Function call

=>Here the values of arg1,arg2,.....,arg-n of  Function call are passing to Param1,Param2,....Param-n of Function Definition Respectively.
