Question: There are two sneakers in each photo and each has a black Nike swoosh logo on the side.

Reference Answer: False

Left image URL: https://cdn.shopify.com/s/files/1/0516/1357/products/844833-009-p.jpg?v=1488260839

Right image URL: https://images.nike.com/is/image/DotCom/PDP_HERO_M/844929_005_A_PREM/roshe-two-flyknit-womens-shoe.jpg

Original program:

```
The program is not provided, so I cannot determine if the statement is true or false.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are two sneakers in each photo and each has a black Nike swoosh logo on the side.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are two sneakers in each photo and each has a black Nike swoosh logo on the side.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

