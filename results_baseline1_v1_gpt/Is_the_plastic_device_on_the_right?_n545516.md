Question: Is the plastic device on the right?

Reference Answer: yes

Image path: ./sampled_GQA/n545516.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='plastic device')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=GET(image=IMAGE)
ANSWER0=CROP_RIGHTOF(image=IMAGE,box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

