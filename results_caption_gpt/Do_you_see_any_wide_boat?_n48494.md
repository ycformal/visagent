Question: Do you see any wide boat?

Reference Answer: yes

Image path: ./sampled_GQA/n48494.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='boat')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='How wide is the boat?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 10 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

