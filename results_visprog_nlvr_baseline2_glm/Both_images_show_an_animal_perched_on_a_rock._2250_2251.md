Question: Both images show an animal perched on a rock.

Reference Answer: False

Left image URL: https://i.pinimg.com/originals/13/d7/9d/13d79d934ccf6f7919777fcb6dbb6e6c.jpg

Right image URL: https://www.thetimes.co.uk/imageserver/image/methode%2Ftimes%2Fprod%2Fweb%2Fbin%2F337068c8-aa9c-11e7-b9a3-2cac9d6c85bd.jpg?crop=1350%2C759%2C107%2C73&resize=685

Original program:

```
The program is checking if both images show an animal perched on a rock. It does this by asking the user how many animals are in each image and if there is a rock in the image. If the user answers yes to both questions for both images, then the program will return True. Otherwise, it will return False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Both images show an animal perched on a rock.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both images show an animal perched on a rock.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

