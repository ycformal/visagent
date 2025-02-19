Question: The cable is on what?

Reference Answer: paper

Image path: ./sampled_GQA/n250821.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cable')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cable')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

