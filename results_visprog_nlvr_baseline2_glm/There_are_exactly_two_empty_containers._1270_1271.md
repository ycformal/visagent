Question: There are exactly two empty containers.

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/31Y49eBuo6L.jpg

Right image URL: http://catalogo.merse.com.br/vidraria/erlenmeyers/boca%20larga.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are exactly two empty containers.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are exactly two empty containers.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

