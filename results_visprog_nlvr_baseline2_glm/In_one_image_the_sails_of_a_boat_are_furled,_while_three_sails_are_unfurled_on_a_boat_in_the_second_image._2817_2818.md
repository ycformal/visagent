Question: In one image the sails of a boat are furled, while three sails are unfurled on a boat in the second image.

Reference Answer: True

Left image URL: http://newimages.yachtworld.com/resize/1/33/51/5143351_20150703074737776_1_XLARGE.jpg?f=/1/33/51/5143351_20150703074737776_1_XLARGE.jpg&w=600&h=450&t=1435913484000

Right image URL: http://www.sandemanyachtcompany.co.uk/images/boats/0x0_476_802777275a0ac9785c3da.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In one image the sails of a boat are furled, while three sails are unfurled on a boat in the second image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one image the sails of a boat are furled, while three sails are unfurled on a boat in the second image.' true or false?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

