Question: A German Shepherd is given a command and barking at something in one of the pictures.

Reference Answer: False

Left image URL: https://i.pinimg.com/236x/77/c4/e7/77c4e7604a3c9b10101e7e5e9c46d700--red-nose-pit-pitbull-mix.jpg

Right image URL: https://i.pinimg.com/736x/0e/50/16/0e50162c43e4bdd07519a8f3d4fac797--malinois-dog-pretty-animals.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A German Shepherd is given a command and barking at something in one of the pictures.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A German Shepherd is given a command and barking at something in one of the pictures.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

