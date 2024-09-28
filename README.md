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

**2) Default  Parameters (or) arguments**
		
=>When there is a Common Value for family of Similar Function Calls then Such type of Common Value(s) must be taken  as default parameter with common value (But not recommended to pass by using Posstional arguments OR Parameters)

----------------------------------------------------------------------------------------
Syntax for Function Definition with Default Parameters

----------------------------------------------------------------------------------------
def   functionname(param1,param2,....param-n-1=Val1, Param-n=Val2):
          ------------------------------------------------------------------
	  ------------------------------------------------------------------

->Here param-n-1 and param-n are called "default Parameters".
->and param1,param-2... are called "Formal Possitional parameters".

Rule-: When we use default parameters in the function definition, They must be used as last Parameter(s) otherwise we get Error( SyntaxError: parameter without a default follows parameter with a default)
===============================================================================================

**3) Keyword Parameters (or) arguments**
		============================================
=>In some of the circumstances, we know the function name and formal parameter names and we don't know the order of formal Parameter names and to pass the data / values accurately we must use the concept of Keyword Parameters (or) arguments.
=>The implementation of Keyword Parameters (or) arguments says that all the formal parameter names used as arguments in Function call(s) as keys.

Syntax for function definition:-

-------------------------------------------------
def    functionname(param1,param2...param-n):
         ---------------------------------------------
	 ---------------------------------------------

functionname(param-n=val-n,param1=val1,param-n-1=val-n-1,.........)


Here param-n=val-n,param1=val1,param-n-1=val-n-1,...... are called Keywords arguments
=>When we specify Keyword arguments before Possitional Arguments in Function Calls(s) then we get 
SyntaxError: positional argument follows keyword argument bcoz PVM gives First Priority for positional arguments.


**4) Variables Length Parameters (or) arguments**
		
=>When we have familiy of multiple Similar function calls with Variable number of values / arguments then with normal python programming, we must define mutiple function defintions. This process leads to more development time. 
=>To overcome this process, we must use the concept of Variable length Parameters .
=>To Impelement,  Variable length Parameters concept, we must define single Function Definition and takes a formal Parameter preceded with a symbol called astrisk ( * param) and the formal parameter with astrisk symbol is called Variable length Parameters  and whose purpose is to hold / store any number of values coming from similar function calls and whose type is <class, 'tuple'>.

---------------------------------------------------------------------------------------------------
Syntax for function definition with Variables Length Parameters:

---------------------------------------------------------------------------------------------------
	def   functionname(list of Posstional formal params,  *param1 , param2=value) :
	        --------------------------------------------------
		--------------------------------------------------

=>Here *param1 is called Variable Length parameter and it can hold any number of argument values (or) variable number of argument values and *param1 type is <class,'tuple'>

=>Rule:- The *param1 must always written at last part of Function Heading and it must be only one (but not multiple)
=>Rule:- When we use Variable length and default parameters  in function Heading, we use default parameter as last and before we use variable length parameter and in function calls, we should not use default parameter as Key word argument bcoz Variable number of values are treated as Posstional Argument Value(s) .

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**5) Key Word Variables Length Parameters (or) arguments**
	
=>When we have familiy of multiple function calls with Key Word Variable number of values / arguments then with normal python programming, we must define mutiple function defintions. This process leads to more development time. 
=>To overcome this process, we must use the concept of Keyword Variable length Parameters .
=>To Implement, Keyword Variable length Parameters concept, we must define single Function Definition and takes a formal Parameter preceded with a symbol called double astrisk  ( ** param) and the formal parameter with double astrisk symbol is called Keyword Variable length Parameters  and whose purpose is to hold / store any number of (Key,Value)  coming from similar function calls and whose type is <class, 'dict'>.

---------------------------------------------------------------------------------------------------
Syntax for function definition with Keyword Variables Length Parameters:
---------------------------------------------------------------------------------------------------
	def   functionname(list of formal params,  **param) :
	        --------------------------------------------------
		--------------------------------------------------

=>Here **param is called Keyword Variable Length parameter and it can hold any number of Key word argument values (or) Keyword variable number of argument values and **param type is <class,'dict'>

=>Rule:- The **param must always written at last part of Function Heading and it must be only one (but not multiple)
---------------------------------------------------------------
(*)Final Syntax for defining a Function
---------------------------------------------------------------
def  funcname(PosFormal parms, *Varlenparam, default params, **kwdvarlenparam):
			-------------------------------------------------
			-------------------------------------------------
