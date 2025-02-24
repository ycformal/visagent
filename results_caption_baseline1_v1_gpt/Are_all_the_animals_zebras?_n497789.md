Question: Are all the animals zebras?

Reference Answer: no

Image path: ./sampled_GQA/n497789.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='zebra')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == {TOTAL_OBJECTS} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: No, not all the animals are zebras.

