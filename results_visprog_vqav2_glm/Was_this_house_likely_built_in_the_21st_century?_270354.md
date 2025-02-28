Question: Was this house likely built in the 21st century?

Reference Answer: no

Image path: ./sampled_GQA/270354.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='When was this house likely built?')
ANSWER1=EVAL(expr="'no' if {ANSWER0} == '21st century' else 'yes'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

