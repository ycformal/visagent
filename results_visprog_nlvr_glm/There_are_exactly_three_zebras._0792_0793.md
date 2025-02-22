Question: There are exactly three zebras.

Reference Answer: False

Left image URL: https://vetstreet-brightspot.s3.amazonaws.com/51/6a/d50c97624087a9ce5b6c1fd31f24/baby-zebra-mom-630mk081212.jpg

Right image URL: http://www.awf.org/sites/default/files/media/gallery/wildlife/Plains%20Zebra/Z-Billy_Dodson_3.jpg?itok=rzMdZ7LM

Program:

```
Statement: There are exactly three zebras.
Program:
ANSWER0=VQA(image=LEFT,question='How many zebras are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many zebras are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} == 3')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'There'

