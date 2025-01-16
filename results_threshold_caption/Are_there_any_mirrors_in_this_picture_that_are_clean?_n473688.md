Question: Are there any mirrors in this picture that are clean?

Reference Answer: Yes, there is a mirror that is clean.

Image path: ./sampled_GQA/n473688.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='mirror')
ANSWER0=VQA(image=IMAGE,question='Are there any mirrors in this picture?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes

