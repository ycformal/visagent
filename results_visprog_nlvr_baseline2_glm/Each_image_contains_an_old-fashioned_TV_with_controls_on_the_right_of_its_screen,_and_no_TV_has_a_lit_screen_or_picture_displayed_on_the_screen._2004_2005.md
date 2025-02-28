Question: Each image contains an old-fashioned TV with controls on the right of its screen, and no TV has a lit screen or picture displayed on the screen.

Reference Answer: True

Left image URL: https://static.turbosquid.com/Preview/2014/05/25__12_10_05/tv.jpgfa18ec94-4481-4a5a-abaa-1bc8fe95c8feLarger.jpg

Right image URL: https://i.pinimg.com/736x/ff/dc/90/ffdc9098267b665fe1f501b2dcde2c63--cheap-tvs-tv-sets.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains an old-fashioned TV with controls on the right of its screen, and no TV has a lit screen or picture displayed on the screen.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains an old-fashioned TV with controls on the right of its screen, and no TV has a lit screen or picture displayed on the screen.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

