Question: Are both the cabbage to the left of the other cabbage and the vegetable to the right of the broccoli purple?

Reference Answer: yes

Image path: ./sampled_GQA/n429961.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cabbage')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cabbage')
IMAGE1=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX2=LOC(image=IMAGE1,object='vegetable')
IMAGE2=CROP_RIGHTOF(image=IMAGE,box=BOX1)
BOX3=LOC(image=IMAGE2,object='broccoli')
ANSWER0=VQA(image=IMAGE0,question='What color is the cabbage?')
ANSWER1=VQA(image=IMAGE2,question='What color is the vegetable?')
ANSWER2=VQA(image=IMAGE3,question='What color is the broccoli?')
ANSWER3=EVAL(expr="'yes' if {ANSWER0} == 'purple' and {ANSWER1} == 'purple' and {ANSWER2} == 'purple' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER3)
```
Answer: Runtime error: 'IMAGE3'

