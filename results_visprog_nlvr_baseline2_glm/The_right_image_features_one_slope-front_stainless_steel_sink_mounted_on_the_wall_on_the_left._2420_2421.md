Question: The right image features one slope-front stainless steel sink mounted on the wall on the left.

Reference Answer: True

Left image URL: http://www.kavika.fi/wp-content/uploads/2015/10/Artikkelikuva7110b.jpg

Right image URL: http://www.hosser.ru/sites/default/files/mkdc_kazan_10.jpg

Original program:

```
The statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image features one slope-front stainless steel sink mounted on the wall on the left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image features one slope-front stainless steel sink mounted on the wall on the left.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

