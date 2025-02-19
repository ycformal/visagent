Question: Are there any beds in the picture that are not dirty?

Reference Answer: yes

Image path: ./sampled_GQA/n23181.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bed')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: no

