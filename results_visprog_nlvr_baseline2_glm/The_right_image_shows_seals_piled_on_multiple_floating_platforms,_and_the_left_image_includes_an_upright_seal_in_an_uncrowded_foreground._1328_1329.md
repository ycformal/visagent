Question: The right image shows seals piled on multiple floating platforms, and the left image includes an upright seal in an uncrowded foreground.

Reference Answer: False

Left image URL: https://www.terragalleria.com/images/us-ca/usca43627.jpeg

Right image URL: https://shopwildsouls.files.wordpress.com/2014/05/20140502_142250.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The right image shows seals piled on multiple floating platforms, and the left image includes an upright seal in an uncrowded foreground.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image shows seals piled on multiple floating platforms, and the left image includes an upright seal in an uncrowded foreground.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

