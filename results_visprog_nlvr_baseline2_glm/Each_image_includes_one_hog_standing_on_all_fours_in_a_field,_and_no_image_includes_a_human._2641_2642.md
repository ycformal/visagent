Question: Each image includes one hog standing on all fours in a field, and no image includes a human.

Reference Answer: True

Left image URL: https://www.sundaypost.com/wp-content/uploads/sites/13/2017/06/iStock-186545340-900x540.jpg

Right image URL: http://i.dailymail.co.uk/i/pix/2015/01/07/006D73F400000258-0-image-m-10_1420671408863.jpg

Original program:

```
The program provided does not include a statement or a program for this specific question.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image includes one hog standing on all fours in a field, and no image includes a human.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image includes one hog standing on all fours in a field, and no image includes a human.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

