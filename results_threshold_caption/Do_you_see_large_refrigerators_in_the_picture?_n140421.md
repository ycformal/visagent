Question: Do you see large refrigerators in the picture?

Reference Answer: Yes, there is a large refrigerator.

Image path: ./sampled_GQA/n140421.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='refrigerator')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes.

