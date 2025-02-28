Question: One image shows a baboon holding a fruit to its mouth, and one image shows a baboon with a wide-open mouth baring fangs.

Reference Answer: False

Left image URL: https://st.depositphotos.com/2838183/3425/i/950/depositphotos_34253329-stock-photo-baboon-eating-grass.jpg

Right image URL: https://farm9.static.flickr.com/8193/8429748123_dac4045fb1_b.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a baboon holding a fruit to its mouth, and one image shows a baboon with a wide-open mouth baring fangs.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a baboon holding a fruit to its mouth, and one image shows a baboon with a wide-open mouth baring fangs.' true or false?')=<b><span style='color: green;'>baa</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>baa</span></b></div><hr>

Answer: baa

