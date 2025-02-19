Question: What kind of furniture is made of the same material as the window frame that looks white?

Reference Answer: bookcase

Image path: ./sampled_GQA/n344136.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='window frame')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='furniture')
ANSWER0=VQA(image=IMAGE0,question='What color is the window frame?')
ANSWER1=VQA(image=IMAGE0,question='What kind of furniture is made of the same material as the window frame that looks white?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'white' and {ANSWER1} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: '>' not supported between instances of 'str' and 'int'

