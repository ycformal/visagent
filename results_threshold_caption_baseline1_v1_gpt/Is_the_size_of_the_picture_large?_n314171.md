Question: Is the size of the picture large?

Reference Answer: no

Image path: ./sampled_GQA/n314171.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the size of the picture?')
ANSWER1=EVAL(expr="'large' if {ANSWER0} > 1000 else 'small'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: no

