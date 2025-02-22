Question: Some of the bottles of lotion are laying on a pink cloth.

Reference Answer: False

Left image URL: https://i.pinimg.com/originals/e0/9d/27/e09d27647e9e53d927f5b0ae1870dfe6.jpg

Right image URL: http://1.bp.blogspot.com/-eFwmwLQkYwE/UIlv_lrCyVI/AAAAAAAAAR0/cx4LKp7KfRo/s1600/DSC09988.JPG

Program:

```
Statement: Some of the bottles of lotion are laying on a pink cloth.
Program:
ANSWER0=VQA(image=LEFT,question='Are some of the bottles of lotion laying on a pink cloth?')
ANSWER1=VQA(image=RIGHT,question='Are some of the bottles of lotion laying on a pink cloth?')
ANSWER2=EVAL(expr='{ANSWER0} or {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'Some'

