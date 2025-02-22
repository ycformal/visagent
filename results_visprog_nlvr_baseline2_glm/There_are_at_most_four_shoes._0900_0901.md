Question: There are at most four shoes.

Reference Answer: False

Left image URL: http://img.bleacherreport.net/img/images/photos/002/828/064/ca24bca31337270a178b37f6583b2b10_crop_exact.jpg?w=644&h=430&q=75

Right image URL: https://i.pinimg.com/236x/78/cf/63/78cf63c04d7b389e106af503343ea3bf--cheap-running-shoes-women-running-shoes.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

