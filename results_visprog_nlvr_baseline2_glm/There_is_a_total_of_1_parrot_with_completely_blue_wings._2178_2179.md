Question: There is a total of 1 parrot with completely blue wings.

Reference Answer: False

Left image URL: https://st2.depositphotos.com/3383759/9767/i/950/depositphotos_97671624-stock-photo-face-of-the-blue-and.jpg

Right image URL: https://c1.staticflickr.com/1/98/246377093_bb2e461995_z.jpg?zz=1

Original program:

```
The statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is a total of 1 parrot with completely blue wings.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a total of 1 parrot with completely blue wings.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

