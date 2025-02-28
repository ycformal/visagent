Question: Both images show an animal perched on a rock.

Reference Answer: True

Left image URL: https://www.mountainphotography.com/images/320/20160721-Marmot-Grin.jpg

Right image URL: https://www.nps.gov/romo/learn/nature/images/Marmot_Cover_WaltKaesler_688x344.jpg?maxwidth=1200&maxheight=1200&autorotate=false

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
ANSWER0=VQA(image=IMAGE,question="Is 'Both images show an animal perched on a rock.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both images show an animal perched on a rock.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

