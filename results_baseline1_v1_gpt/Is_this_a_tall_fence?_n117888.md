Question: Is this a tall fence?

Reference Answer: yes

Image path: ./sampled_GQA/n117888.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='fence')
ANSWER0=VQA(image=IMAGE,question='How tall is the fence?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 5 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: '>' not supported between instances of 'str' and 'int'

