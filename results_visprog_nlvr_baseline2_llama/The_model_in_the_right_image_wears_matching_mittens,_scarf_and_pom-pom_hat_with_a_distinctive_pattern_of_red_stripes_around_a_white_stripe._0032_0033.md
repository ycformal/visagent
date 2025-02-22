Question: The model in the right image wears matching mittens, scarf and pom-pom hat with a distinctive pattern of red stripes around a white stripe.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB1B6kaOFXXXXX7XpXXq6xXFXXXl/CIVICHIC-Cute-Warm-Set-Lady-Knit-font-b-Hat-b-font-font-b-Scarf-b-font.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1eZjtOFXXXXXiaVXXq6xXFXXXc/CIVICHIC-Woman-Warm-Set-Knit-Hat-font-b-Scarf-b-font-Glove-3pcs-Color-Mix-Stripes.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Does the model wear matching mittens, scarf and pom-pom hat with a distinctive pattern of red stripes around a white stripe?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Does the model wear matching mittens, scarf and pom-pom hat with a distinctive pattern of red stripes around a white stripe?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the model wear matching mittens, scarf and pom-pom hat with a distinctive pattern of red stripes around a white stripe?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

