This is a simple script that creates a recursive loop, à la recursive functions, except that it loops between separate programs.

**How to run:**

- Either copy/paste ```seed.py``` into the python interpreter
- Or run ```python3 seed.py```

**What's happening here?**

```seed.py``` creates another python script called ```replicate.py```, which in turn creates two other scripts ```rep0.py``` and ```rep1.py```. 

- ```seed.py```
  - Uses bash commands to create a file called ```replicate.py```
- ```replicate.py```
  - Creates and calls ```rep0.py```
- ```rep0.py```:
  - Creates and calls ```rep1.py```
- ```rep1.py```:
  - Calls ```replicate.py```

The effect is what is called a **fork bomb**, and although not my intent, it can crash the system if there are no precautions in place or the user fails to stop the program.

This is a proof of concept and I do NOT condone any malicous use of my code.
