Question: What type of furniture is made of the same material as the white ceiling?

Reference Answer: chair

Image path: ./sampled_GQA/n68769.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='ceiling')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the ceiling?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'white' else 'no'")
ANSWER2=IF(condition={ANSWER1},then='white',else='other')
BOX1=LOC(image=IMAGE,object=ANSWER2)
ANSWER3=VQA(image=IMAGE,question='What type of furniture is this?')
FINAL_RESULT=RESULT(var=ANSWER3)
```
Answer: "runtime error"

