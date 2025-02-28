Question: there are clear jars in a row with a beetle inside

Reference Answer: False

Left image URL: http://cdn-ak.f.st-hatena.com/images/fotolife/M/MAGAMI-TOHRU/20070204/20070204140109.jpg

Right image URL: https://st2.depositphotos.com/7677414/12522/i/950/depositphotos_125223936-stock-photo-multiple-vending-machines-in-akihabara.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'there are clear jars in a row with a beetle inside' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'there are clear jars in a row with a beetle inside' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

