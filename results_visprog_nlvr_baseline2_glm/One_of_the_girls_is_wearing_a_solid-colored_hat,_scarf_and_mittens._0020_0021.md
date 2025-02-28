Question: One of the girls is wearing a solid-colored hat, scarf and mittens.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB1sigoOFXXXXahXpXXq6xXFXXX5/CIVICHIC-Korean-Stylish-Warm-Gift-Lady-Knit-Hat-font-b-Gloves-b-font-font-b-Scarf.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1qQYSOFXXXXbQXVXXq6xXFXXXh/CIVICHIC-Korea-Style-3pcs-Warm-Set-Knit-font-b-Hat-b-font-Scarf-font-b-Glove.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One of the girls is wearing a solid-colored hat, scarf and mittens.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One of the girls is wearing a solid-colored hat, scarf and mittens.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

