Question: One orange fish with at least one white stripe is above white anemone tendrils with purplish tips in the left image.

Reference Answer: True

Left image URL: http://fins.actwin.com/pics/Amphiprion_frenatus2.jpg

Right image URL: http://www.meades.org/fish/fish_2005/ritteri_anemone.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One orange fish with at least one white stripe is above white anemone tendrils with purplish tips in the left image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One orange fish with at least one white stripe is above white anemone tendrils with purplish tips in the left image.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

