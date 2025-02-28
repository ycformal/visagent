Question: Each image shows one red-orange dog with open eyes and a closed mouth.

Reference Answer: False

Left image URL: http://www.hungarianvizsla.co.hu/download/Vizsla_05_1024x768.jpg

Right image URL: https://i.pinimg.com/736x/18/06/f1/1806f189ff947d72b8fc7eef226e6be7--vizsla-obsession.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows one red-orange dog with open eyes and a closed mouth.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows one red-orange dog with open eyes and a closed mouth.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

