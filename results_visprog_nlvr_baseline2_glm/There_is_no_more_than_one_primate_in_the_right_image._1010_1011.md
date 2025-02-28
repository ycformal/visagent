Question: There is no more than one primate in the right image.

Reference Answer: True

Left image URL: http://s3.amazonaws.com/medias.photodeck.com/058f9070-2a9b-4570-a272-6a290243468d/Brett-Cole-South-Africa-00053_medium.jpg

Right image URL: http://s3.amazonaws.com/medias.photodeck.com/013ca52f-f79d-4ded-918f-b71db871148b/Brett-Cole-South-Africa-00051_medium.jpg

Original program:

```
The program is asking if there is no more than one primate in the right image. This means that there could be zero or one primate in the image. The program uses the VQA function to ask the question and then evaluates the answer using the EVAL function. The final answer is returned using the RESULT function.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is no more than one primate in the right image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is no more than one primate in the right image.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

