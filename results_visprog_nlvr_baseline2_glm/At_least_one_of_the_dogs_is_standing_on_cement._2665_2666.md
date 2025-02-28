Question: At least one of the dogs is standing on cement.

Reference Answer: False

Left image URL: https://i.pinimg.com/236x/10/3f/8b/103f8b8fdd1bf4d8dc45926a51e24b9c--schnauzer-dogs-miniature-schnauzer.jpg

Right image URL: https://lh6.googleusercontent.com/proxy/r8Ge6nnU4_ZKp2qksfoY-kpozxILPVZ-MgNXki4Ip7KaL5ZO6HH-hElDmoUr2SV2cgZgg37uyTUJd1BBQRBtyQehmh3sp7xjkqF0dydHkMBbCFcvI7H62ju3BOK0k4rYYO-sijO2eika=s0-d

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
ANSWER0=VQA(image=IMAGE,question="Is 'At least one of the dogs is standing on cement.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one of the dogs is standing on cement.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

