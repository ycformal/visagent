Question: There are no more than 3 monkeys.

Reference Answer: True

Left image URL: http://1.bp.blogspot.com/-TARNFOIdHSg/T3PAC0aHDFI/AAAAAAAADDc/sDgIctwNc7A/s1600/Olive-baboon-grooming.jpg

Right image URL: http://s3.amazonaws.com/medias.photodeck.com/9565c3ed-00b2-4b28-98de-6d5f4e86aee9/Brett-Cole-South-Africa-00046_medium.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are no more than 3 monkeys.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are no more than 3 monkeys.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

