# AVP-Assembler
This is a assembly language for a Stack based virtual machine named "Ameer Virtual Processor" or AVP for short.

## Target
The target of this assembler is a simple assembly language made with it which itself is targeted to a stack based virtual machine which is already on Github, [here to be specific](https://github.com/ameerwasi001/Ameer-Virtual-Processor). This virtual machine is turing complete and has multile frames of both main stack, and both heaps.

## Instruction Set
This assembler supports all the instructions found in Ameer Virtual Processor, and it will be updated everytime Ameer Virtual Machine will be, as it's a companion of both implementation of that VM. What follows is an instruction set of this virtual machine changed into mnemonics.

**END |** This instruction is used to tell the program that the file is ended before it does or for cleanliness of code. 

**EOI |** This code is used to end every instruction.

**PUSH |** PUSH to the top of the stack.

**POP  |** Pop either top or a certain index from the stack.

**PRINT |** Used to print the top of the sack.

**ADD |** Add two numbers at the top of the stack.

**SUBSTRACT |** Substract two numbers at the top of the stack.

**MULTIPLY |** Multiply two numbers at the top of the stack.

**DIVIDE |** Divide two numbers at the top of the stack

**SHUFFLE |** Shuffle two elements from the stack, takes an argument as to what stack number should the first stack be shuffled with.

**GOTO |** Unconditional GOTO and it pops the line number of the stack.

**IFEQUAL |** Add either True or False on the stack depending on if first and second values on the stack are equal and pops conditions.

**MODULUS |** Modulus of first two values from stack and append the result onto it.

**INCREMENT |** Increment the last number from the stack.

**DECREMENT |** Decrement the last number from the stack.

**EXPONENT |** Exponent of first two values from stack and append the result onto it.   

**STORE |** Store the first element from the stack in a heap of numbered name, numbered according to the given in the instruction.

**RETRIVE |** Retrive and append from the storage onto the stack.

**DELETE |** Delete an item from storage.

**IFGREAT |** Adds either True or False on the stack depending on if first is greater than the and second value on the stack and pops conditions.

**IFNULL |** Adds either True or False on the stack depending on if the first value on the stack is null and pops conditions.

**IFPLUS |** Adds either True or False on the stack depending on if the first value on the stack is positive and pops conditions.

**IFMINUS |** Adds either True or False on the stack depending on if the first value on the stack is negative and pops conditions.

**IFUNEQUAL |** Adds either True or False on the stack depending on if first is unequal to the second value on the stack and pops conditions.

**IFEQUAL |** Adds either True or False on the stack depending on if first is equal to the second value on the stack and pops conditions. 

**IFSMALL |** Adds either True or False on the stack depending on if first is unequal to the second value on the stack and pops conditions.

**GOTO_L |** GOTO without popping line number from stack.

**IFGREAT_0 |** Adds either True or False on the stack depending on if first is greater than the and second value on the stack.

**IFNULL_0 |** Adds either True or False on the stack depending on if the first value on the stack is null.

**IFPLUS_0 |** Adds either True or False on the stack depending on if the first value on the stack is positive.

**IFMINUS_0 |** Adds either True or False on the stack depending on if the first value on the stack is negative.

**IFUNEQUAL_0 |** Adds either True or False on the stack depending on if first is unequal to the second value on the stack.   

**IFEQUAL_0 |** Adds either True or False on the stack depending on if first is equal to the second value on the stack.

**IFSMALL_0 |** Adds either True or False on the stack depending on if first is unequal to the second value on the stack.

**SADD |** Concatenates first two elements of the stack and appends them.

**SCONV |** Converts the first element of the stack to a string.  

**POP_TOP |** Pops the first elememnts from the stack depending on the indx you provide.    

**GOTO_CONDITIONALLY |** Conditionally GOTO a line number depending on the first value on the stack and if it's True or False.

**GOTO_CONDITIONALLY_L |** Conditionally GOTO a line number depending on the first value on the stack and if it's True or False and don't pop conditions off the stack.

**LITERAL_PRINT |** Print stuff with literals. 

**NOT |** Inverts the first condition on the stack.

**OR |** OR operation on the first condition on the stack. 

**AND |** AND operation on the first condition on the stack.

**REGISTER |** Adds first element of the stack to this register with a string name.

**UNREGISTER |** Removes the given element from the register.

**GETREGISTER |** Add the given element from the register to the top of the stack.

**FLOATCONV |** Converts the first element of the stack to a float. 

**INTCONV |** Converts the first element of the stack to a integer.  

**DUPLICATE |** Duplicate the first value of the stack.

**ARCREATE |** Creates an array with the array length on the top of the stack and append it onto the stack.

**ARCREATE_1 |** Creates an array with the array length on the top of the stack and append it onto the stack and removes those from the stack.

**MEMDUMP |** Print entire stack.

**ARDISASSEMBLE |** Disassemble the array on the top of the stack.      

**ARGET |** Get list's place from the top of the stack and them gets the reference from the stack. Either from the top or bottom depending on it's mode.

**ARSET |** Sets an array the same way it get's it. 

**ARLEN |** Get the length of the array from the given index.

**ARAPPEND_0 |** Appends the memory on a certain index from top.

**ARAPPEND_1 |** Appends the memory on a certain index from bottom.   

**ARPOP_1 |** Pops array on a certain list's place counted from bottom.

**ARLEN_0 |** Length of an array from bottom.

**ARSET_TOP |** Set an array from top index.

**ARINSERT_TOP |** Insert into an array from top index.

**ARINSERT |** Insert into an array from bottom index.

**INPUT |** With this insruction you can input anything in a string form.

**PUSH_NONE |** With this insruction you can push none on to the stack.

**SHUFFLE_1 |** Shuffles the first item in the stack with another one given in the instruction itself, counted from bottom.

**ARPOP_0 |** Pops array on a certain list's place counted from top.

**ARPOP_TOP_1 |** Pops array's top index on a certain list's place counted from top.

**ARPOP_TOP_0 |** Pops array's top index on a certain list's place counted from bottom.

**PUSH_TRUE |** Pushes a true value onto the stack.

**PUSH_FALSE |** Pushes a false value onto the stack.

**XOR |** XOR gate that checks for first two value of the stack and pops them of it.

**ASSERT |** Assert statement that raises assertion error if condition on the top of the stack isn't true and proceeds if it is.

**NEGATE |** Negates the first value on the top of the stack.

**IFSAME |** Checks if two value on the top of the stack are the same value and pops them off the stack.

**IFSAME_0 |** Checks if two value on the top of the stack are the same value and doesn't pops them off the stack.

**SPLIT |** Splits a string into an array by a seprator and pops it off the stack.

**JOIN |** Joins an array from a string by a seprator and pops it off the stack.

**STRINSERT |** Inserts into a string, specifically substitutes curly braces.

**RECORD |** Records current memory seprately.

**RECAP |** Sets currently recorded memory to current memory.

**FRAMDUMP |** Prints entire frame in which memories is recorded.

**RECORDHEAP |** Records current heap seprately, and choses it by an argument in which 0 means storage and 1 means register.

**RECAPHEAP |** Sets currently recorded heap to the current heap, and choses it by an argument in which 0 means storage and 1 means register.

**HEAPDUMP |** Prints entire frame in which heaps is recorded.

**PUSH_LAST |** Pushes the last heap frame's onto the memory.

## Labels
In the aforementioned virtual machine there's literally no concept of labels, you just jump by providing a line number but if you want to use labels, this assembler let's you do that and compiles your labels down to line numbers. Jumping by providing a line number is possible in AVP Assembler but is higly discouraged because first of all defining a label isn't much work and secondly, it leads to inconsistent output which in most cases doesn't work in Ameer Virtual Machine.

### Usage labels
To define a label all you have to do is saying #label_name and same goes for calling but be aware that labels can only be called through ``PUSH`` instructions

What follows is an example of a program that takes defines and calls labels.

```
PUSH_NULL
INPUT
SETUP_EXCEPT
INTCONV
END_EXCEPT
IFEXCEPTION "ValueError"
PUSH #EXCEPT
GOTO_CONDITIONALLY
DUPLICATE
ADD
PRINT
END
#EXCEPT
PUSH 0
PRINT
```

As you can also see in the above example, a lable can be called before it's definiton, and that is a feature rather than a bug because in many cases labels are defined before calling but in many other cases it's quite the opposite so, that's my justification.

## Strings
Ameer virtual machine doesn't recogonize strings on it's own, for example to say "Hello World", you must type that with ASCII characters, and start it by ``0x`` such as what follows, ``{0x48656c6c6f20576f726c64}`` but with AVP Assembler it's very simple to write strings like "Hello World", all you gotta do is to write ``"Hello World"``, which then by this assembler is translated to it's aforementioned ASCII form.

Following is a primarily string based example of the program provided in labels section which just means it outputs string at appropriate times.

```
PUSH "Type your number: "
INPUT
SETUP_EXCEPT
INTCONV
END_EXCEPT
IFEXCEPTION "ValueError"
PUSH #EXCEPT
GOTO_CONDITIONALLY
DUPLICATE
ADD
PRINT
END
#EXCEPT
PUSH "Well, I don't know how that's a number..."
PRINT
```
## Numbers
One last thing before wrapping up, Ameer Virtual machine takes numbers in hexadecimal form, for example 74 will be written by as ``{0x4A}``, but in AVP Assembler 74 can simply be written as `74` with no conversion of bases whatsoever because it's made to handle the conversion by itself.

# Thanks
Thanks for reading through, both Ameer Virtual Machine and AVP Assembler were extremely useful experience for me to have and maybe you would like to improve on the status of both of these projects and if so, then you help me by contributing to this project.
