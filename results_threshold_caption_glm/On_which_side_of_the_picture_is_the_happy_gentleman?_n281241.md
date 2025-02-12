Question: On which side of the picture is the happy gentleman?

Reference Answer: right

Image path: ./sampled_GQA/n281241.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='happy gentleman')
ANSWER0=LOCATION(box=BOX0)
ANSWER1=EVAL(expr="'left' if {ANSWER0} == 'LEFT' else 'right'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: left

