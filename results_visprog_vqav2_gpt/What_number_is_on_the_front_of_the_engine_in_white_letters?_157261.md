Question: What number is on the front of the engine in white letters?

Reference Answer: 958

Image path: ./sampled_GQA/157261.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='engine')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What number is on the engine?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'white' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

