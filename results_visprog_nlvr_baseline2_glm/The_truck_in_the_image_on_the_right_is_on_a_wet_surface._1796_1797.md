Question: The truck in the image on the right is on a wet surface.

Reference Answer: True

Left image URL: http://wtop.com/wp-content/uploads/2015/11/IMG_5478.jpg

Right image URL: https://bdn-data.s3.amazonaws.com/uploads/2010/09/1283601116_6f9a-1024x664.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The truck in the image on the right is on a wet surface.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The truck in the image on the right is on a wet surface.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

