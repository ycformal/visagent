Question: Each image includes at least four flutes displayed vertically, and the right image contains exactly five flutes.

Reference Answer: True

Left image URL: http://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Sound_wave_propagation_in_the_soprano_clarinet.jpg/440px-Sound_wave_propagation_in_the_soprano_clarinet.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/236x/9a/c0/5b/9ac05beeb77e79426df30356bd4fa425.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image includes at least four flutes displayed vertically, and the right image contains exactly five flutes.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image includes at least four flutes displayed vertically, and the right image contains exactly five flutes.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

