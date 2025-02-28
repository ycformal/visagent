Question: Both images are top views showing at least six cymbals per image along with multiple cylindrical drums.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/ce/66/9b/ce669b8a60aa3b010bf02e418bf86170.jpg

Right image URL: https://i.pinimg.com/736x/fd/47/6a/fd476a3ffbf230cfc8a1afad7e5dd804--double-bass-drum-sets.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Both images are top views showing at least six cymbals per image along with multiple cylindrical drums.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both images are top views showing at least six cymbals per image along with multiple cylindrical drums.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

