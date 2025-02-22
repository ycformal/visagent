Question: One right facing elephant is walking near a wood fence.

Reference Answer: False

Left image URL: http://blogs.smithsonianmag.com/aroundthemall/files/2009/08/national-zoos-asian-elephant-ambika-covers-her-head-and-back-with-dirt-to-protect-herself-from-the-sun.jpg

Right image URL: https://c402277.ssl.cf1.rackcdn.com/photos/1732/images/hero_full/Asian_Elephant_8.13.2012_Hero_And_Circle_HI_247511.jpg?1345551842

Program:

```
ANSWER0=VQA(image=LEFT,question='How many right facing elephants are walking near a wood fence?')
ANSWER1=VQA(image=RIGHT,question='How many right facing elephants are walking near a wood fence?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} == 1')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: can only concatenate str (not "int") to str

