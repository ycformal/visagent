Question: In at least one image there is a sailfish mounted on the wall.

Reference Answer: True

Left image URL: https://lh3.ggpht.com/_t8-Y4w1UKrc/SiSnGpaw4II/AAAAAAAAcN8/L07uWo-RXcw/image_thumb56.png?imgmax=800

Right image URL: https://i.pinimg.com/736x/cb/87/af/cb87afbb73cabca0f3bbb3cde1b4c6d1--living-room-pictures-room-decorating-ideas.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there is a sailfish mounted on the wall.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there is a sailfish mounted on the wall.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

