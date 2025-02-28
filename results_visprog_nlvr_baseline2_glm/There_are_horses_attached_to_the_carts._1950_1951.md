Question: There are horses attached to the carts.

Reference Answer: True

Left image URL: http://img-aws.ehowcdn.com/750x428p/s3.amazonaws.com/cme_public_images/www_ehow_com/i.ehow.com/images/a04/kn/4t/build-horse-cart-800x800.jpg

Right image URL: http://img-aws.ehowcdn.com/600x400/s3.amazonaws.com/cme_public_images/www_ehow_com/i.ehow.com/images/a04/kn/4t/build-horse-cart-1.1-800x800.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are horses attached to the carts.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are horses attached to the carts.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

