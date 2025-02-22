Question: There are seven or less water bottles total.

Reference Answer: True

Left image URL: https://www.qualitylogoproducts.com/custom-waterbottles/easy-clean-water-bottle-28oz-superextralarge.jpg

Right image URL: https://cdn.shopify.com/s/files/1/0878/0246/products/NGN_Water_Bottle_2-pack_CLR_VIOLET_1024x1024.jpg?v=1511942978

Original program:

```
The program is asking for the total number of water bottles in both images. The program first asks how many water bottles are in the left image and assigns the answer to ANSWER0. Then it asks how many water bottles are in the right image and assigns the answer to ANSWER1. The program then adds the two answers together and assigns the result to ANSWER2. Finally, the program checks if ANSWER2 is less than or equal to 7 and assigns the result to FINAL_ANSWER. If the result is true, then the statement is true. If the result is false, then the statement is false.
ANSWER0=VQA(image=LEFT,question='How many water bottles are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many water bottles are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

