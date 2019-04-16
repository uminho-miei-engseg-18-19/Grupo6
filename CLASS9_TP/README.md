## Question 1.1
### 1
If we consider that for each 1000 source lines of code there exists 5 to 50 bugs:
 1. Facebook has around 62 million SLOC, then we can estimate that there is about 310 000 to 3 100 000 bugs in their software
 2. A car software has around 100 million SLOC, then we can estimate that there is about 500 000 to 5 000 000 bugs in the software
 3. Linux 3.1 has around 15 million SLOC, then we can estimate that there is about 75 000 to 750 000 bugs in their software

In each estimation, the first value refers to the lower limit and aplies to software developed using rigorous methods, the second value refers to the higher limit and aplies to normal software.

### 2 
Some of this bugs are vulnerabilities but there is no way to predict how many vulnerabilities there are just by knowing the number of SLOC.

## Question 1.2

### Project Vulnerabilities 
1. Argument Injection or Modification
This means the software does not sufficiently delimit the arguments being passed to a component in another control sphere, allowing alternate arguments to be provided, leading to potentially security-relevant changes.<br\>
This vulnerabilities are easly mitigated by understanding all the potential areas where untrusted inputs can enter the software and performing input validation at well-defined interfaces.

2. Information Exposure
More specifically the intentional or unintentional disclosure of information to an actor that is not explicitly authorized to have access to that information.<br\>
This kind of vulnerability is also simply solved by compartmentalizing the system properly, taking into account where trust boundaries can be unambigously drawn, not allowing sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside the safe area. 

### Codification vulnerabilities 
1. Compiler Removal of Code to Clear Buffers 
Precisely sensitive memory is cleard according to the source code, but compiler optimizations leave the memory untouched when it is not read again, that is to say "dead sotre removal"<br\>
This vulnerabilities can be mitigated by storing the sensitive data in a "volatile" memory location if available or if possible by configuring the compiler so that it does not remove dead sotres.

2. External Control of System or Configuration Setting
Meaning allowing external control of system settings, which can disrupt service or cause an application to behave unexpectedly, and in a pottencially malicious way.
This occurs when an attacker can control values that govern the behaviour of the system. <br\>
A possible way to solve this problem is to not allow user-provided or otherwise untrusted data to control sensitive values. 

### Operational vulnerabilities
1. Argument Injection or Modification
Specifically the software does not delimit the arguments being passed to a component in another control sphere, allowing alternate arguments to be provided, leading to potentially security-relevant changes.<br\>
A conceivable way to mitigate this problem is using automated static analysis tools that target this kind of vulnerabilities, or using dynamic tools and techniques that interact with the software using large test suites with many diverse inputs.

2. Download of Code Without Integrity Check
Precisely the product downloads source code or an executable from a remote location and executes the code without sufficently verifying the origin and integrity of the code.<br\>
Possible way to prevent this vulnerability is running the code using the lowest possible privileges to perform the necessary tasks.



## Question 1.3 
Day-zero vulnerabilities are only known by a restrict circle of entities, but not known by the computer security community. On the other hand, non day-zero vulnerabilities are public to the computer security community.