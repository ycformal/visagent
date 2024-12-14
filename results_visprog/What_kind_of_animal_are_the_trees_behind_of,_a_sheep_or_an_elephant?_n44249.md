Question: What kind of animal are the trees behind of, a sheep or an elephant?

Reference Answer: The trees are behind an elephant.

Image path: ./sampled_GQA/n44249.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sheep')
IMAGE0=CROP_BEHIND(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='elephant')
IMAGE1=CROP_BEHIND(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What kind of animal are the trees behind of?')
ANSWER1=VQA(image=IMAGE1,question='What kind of animal are the trees behind of?')
ANSWER2=EVAL(expr="'sheep' if {ANSWER0} > 0 else 'elephant'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: '>' not supported between instances of 'str' and 'int'

