Question: The person in the center of the photo is of what gender?

Reference Answer: The person is female.

Image path: ./sampled_GQA/n466319.jpg

Program:

```
 What <attr> is A <spatial pos> B?
Program:
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP_CENTER(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='The person in the center of the photo is of what gender?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: male

