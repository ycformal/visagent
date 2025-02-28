Question: The right image features one slope-front stainless steel sink mounted on the wall on the left.

Reference Answer: True

Left image URL: http://www.kavika.fi/wp-content/uploads/2015/10/Tuotekuva-ammattikeitti%C3%B6t_uusi.jpg

Right image URL: http://www.incom-inox.com/hr/images/korita/velike/kk-1n.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image features one slope-front stainless steel sink mounted on the wall on the left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image features one slope-front stainless steel sink mounted on the wall on the left.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

