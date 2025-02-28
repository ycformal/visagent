Question: In one image, one person with her head turned rightward is standing behind a non-curved glass display with tiered shelves of baked goods.

Reference Answer: False

Left image URL: https://sc01.alicdn.com/kf/HTB1Kt1MRFXXXXbDXpXXq6xXFXXXB/222471043/HTB1Kt1MRFXXXXbDXpXXq6xXFXXXB.jpg

Right image URL: https://farm3.staticflickr.com/2881/13593621493_4bc4656ab7_z.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In one image, one person with her head turned rightward is standing behind a non-curved glass display with tiered shelves of baked goods.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one image, one person with her head turned rightward is standing behind a non-curved glass display with tiered shelves of baked goods.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

