Question: There is a warthog laying down.

Reference Answer: True

Left image URL: http://www.paesieimmagini.it/Kenya/Imm_Kenya/Kenya08-0020.jpg

Right image URL: http://2.bp.blogspot.com/-_muudxsj7I4/T7p_OYFJ_MI/AAAAAAAAAGk/bXsLUpfsXMs/s1600/images-1.jpeg

Program:

```
ANSWER0=VQA(image=LEFT,question='How many warthogs are laying down?')
ANSWER1=VQA(image=RIGHT,question='How many warthogs are laying down?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} == 1')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: unsupported operand type(s) for +: 'int' and 'str'

