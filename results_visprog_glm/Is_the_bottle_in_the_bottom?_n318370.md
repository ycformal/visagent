Question: Is the bottle in the bottom?

Reference Answer: yes

Image path: ./sampled_GQA/n318370.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bottle')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
ANSWER0=COUNT(image=IMAGE0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'box'

