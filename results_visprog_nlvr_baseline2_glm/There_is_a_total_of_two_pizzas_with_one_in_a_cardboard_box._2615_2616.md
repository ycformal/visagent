Question: There is a total of two pizzas with one in a cardboard box.

Reference Answer: False

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/06/68/18/b2/mamma-mia-pizza-takeaway.jpg

Right image URL: http://s3.amazonaws.com/listing-admin/attachments/597059b5421aa9138600214a/medium/9.jpg?1500535221

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is a total of two pizzas with one in a cardboard box.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a total of two pizzas with one in a cardboard box.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

