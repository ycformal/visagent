Question: Each image features an open-mouthed doberman standing in profile, and the right image features a black-and-tan doberman with chain collar, erect ears and docked tail facing leftward.

Reference Answer: True

Left image URL: http://perros.mascotahogar.com/Imagenes/doberman-cachorro.jpg

Right image URL: http://perros.mascotahogar.com/Imagenes/doberman-de-exposicion.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image features an open-mouthed doberman standing in profile, and the right image features a black-and-tan doberman with chain collar, erect ears and docked tail facing leftward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image features an open-mouthed doberman standing in profile, and the right image features a black-and-tan doberman with chain collar, erect ears and docked tail facing leftward.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

