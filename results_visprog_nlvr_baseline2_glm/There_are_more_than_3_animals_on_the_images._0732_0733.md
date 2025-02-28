Question: There are more than 3 animals on the images.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/5d/5d/ee/5d5dee2a730510ef8082b38277b020cf--photo-displays-water-buffalo.jpg

Right image URL: https://i.ytimg.com/vi/W9w0OadktGI/hqdefault.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are more than 3 animals on the images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are more than 3 animals on the images.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

