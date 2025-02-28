Question: The model in the right image wears matching mittens, scarf and pom-pom hat with a distinctive pattern of red stripes around a white stripe.

Reference Answer: True

Left image URL: https://ae01.alicdn.com/kf/HTB1yNIlJVXXXXcuXpXXq6xXFXXXq/De-punto-sombreros-de-invierno-para-mujer-de-sombrero-de-la-bufanda-guante-de-tres-piezas.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB13nQmOFXXXXXoXpXXq6xXFXXXV/CIVICHIC-Regalo-Caliente-de-Invierno-de-Punto-Guantes-Sombrero-Bufanda-3-Unids-Mujer-Chic-Gorros-Pomp&oacute;n.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The model in the right image wears matching mittens, scarf and pom-pom hat with a distinctive pattern of red stripes around a white stripe.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The model in the right image wears matching mittens, scarf and pom-pom hat with a distinctive pattern of red stripes around a white stripe.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

