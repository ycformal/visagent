Question: The sole baboon in the image is eating a piece of fruit

Reference Answer: True

Left image URL: https://www.jamiiforums.com/attachments/451742/

Right image URL: https://c1.staticflickr.com/6/5524/10910910014_c9289e911b_b.jpg

Original program:

```
Statement: The sole baboon in the image is eating a piece of fruit
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The sole baboon in the image is eating a piece of fruit' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The sole baboon in the image is eating a piece of fruit' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

