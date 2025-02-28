Question: At least one of the scarves hangs lower than the shirt; you can clearly see it against the pant legs.

Reference Answer: True

Left image URL: http://g02.a.alicdn.com/kf/HTB1v1sLOpXXXXaHXFXXq6xXFXXXc/CIVICHIC-Stylish-Girl-Regalo-Invierno-Colorido-Tejer-La-Bufanda-Del-Sombrero-Guante-3-Unidades-Espesar-Headwear.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1tx16OFXXXXc7XXXXq6xXFXXX9/CIVICHIC-Hot-Fashion-Korean-Lady-Winter-Warm-Set-Knit-font-b-Hat-b-font-Scarf-Gloves.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'At least one of the scarves hangs lower than the shirt; you can clearly see it against the pant legs.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one of the scarves hangs lower than the shirt; you can clearly see it against the pant legs.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

