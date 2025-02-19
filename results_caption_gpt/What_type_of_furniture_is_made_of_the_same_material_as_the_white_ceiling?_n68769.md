Question: What type of furniture is made of the same material as the white ceiling?

Reference Answer: chair

Image path: ./sampled_GQA/n68769.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='ceiling')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the ceiling?')
BOX1=LOC(image=IMAGE,object='furniture')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER1=VQA(image=IMAGE1,question='What type of furniture is this?')
ANSWER2=EVAL(expr="'{ANSWER1}' if {ANSWER0} == 'white' else 'none'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: runtime error

