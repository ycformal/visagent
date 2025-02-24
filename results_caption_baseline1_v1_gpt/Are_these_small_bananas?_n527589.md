Question: Are these small bananas?

Reference Answer: yes

Image path: ./sampled_GQA/n527589.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bananas')
ANSWER0=SIZE(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} < 10 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'SIZE'

