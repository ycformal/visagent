Question: One right facing elephant is walking near a wood fence.

Reference Answer: False

Left image URL: http://blogs.smithsonianmag.com/aroundthemall/files/2009/08/national-zoos-asian-elephant-ambika-covers-her-head-and-back-with-dirt-to-protect-herself-from-the-sun.jpg

Right image URL: https://c402277.ssl.cf1.rackcdn.com/photos/1732/images/hero_full/Asian_Elephant_8.13.2012_Hero_And_Circle_HI_247511.jpg?1345551842

Original program:

```
The program provided does not contain a statement or a program related to the given problem.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One right facing elephant is walking near a wood fence.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAhAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDmPC2vyw60Jbmzk1Dc24BpnjdWwBvVl6HCj6132kaBa3Rim1RZvNz5pUyH5mJLEt69e+TXOeEdPn2zXc6qX/hI6qKg1DxndW11PBBiREYqrY5B7896x5n1BI9Vt20a1l82KCGNjnuBj8alkvrOSJnjRCP7yc14Lb6ldXly090zuiYITJAdjwFqXUda1VJUtkl2rwPlHyue+Pb3qbtuxotrna+NtPTxPo8gtrXfqVrIv2ZzIAxUkbhk9sc89MVw7fDbXIU8yVrRS3JBnyf0FNlmktbqOSO5ZsqG3ejAkcCuug8WNDEisVZgMcijVITSbOJ/sm6sb+10qURecrKGIOVbJyDyOwrW8R38EUH2CzUCGIYGTy4B5J9zUmrxSTXKeICGb7TIQMjAyoxx69PzqjBY2mrqYZ7trO7hZgHaMtlT1BXIOa0i7o57b2NX4fyw27XN8tqXmjAjUs2Quck/j0ro9W8YR2m1ktBO/G5ehHPasqOLT9KsI7LT2kkxzJO4wWY9TjtXO6zFCsysLvZgZ3r3z2qrWNI6Is+IrqzvbGW6B2sTuEeOQahsLr7Hp8UMCDayglz1zVJ412GNnUuV4yeoqvp8pZUVWJED7P8AeoKR6Ppd95mmQGaU+Yq7Tnnof8KKy7Ji9srJjBoouM6S6+xaNpLxRxSklARhguc8Ht9a4xbayhcCDTrt5iJfMhuSruhAJHAAGOD711nibTNSvEX7LaSuyquMMF7njk1l2/h7Vv8AhKJ7qW3Is5HkyxmHRgRwBz3rK/kI46GFXd3uAVRP9XGGxsPXmsxpm85ZpQ5VdwQBuq/05r0LU/B9xewMY7a3huMoqN5pwVAOcgdzxVKbwPeTW1pEXtY2g8zceSDkgjtk8CpTLucHDNJLK8ksjFxhRk5wvYD2p0t3JHwGINb/AIp0NNJvt6PHtuHaRERSNgzwK5edJJp444wWdiAB6mrQFq2+Iet6JGljbfZHghfeglgDHJ55Oax7zxXqF7PJcSJbrcSSGR5kjwxJ7delUdXt5rTVJoJ42jlQgMrDkcVRrVJPUztqbH/CT6pwDOCAehXioJNbvpX3yShz/tDNZ1FOwF86vdMMZT8FxTrbW7y0ZmjKfMcnKZrOoosB1EXj3WoYwiG2wP8ApiKK5eiiwXPsCbvVRupoornZZHJ0qmfv0UVLGeffED/j9tv+uf8AU1x2l/8AIatP+uoooq+gIzvHP/I333/AP/QFrnaKK2jsZhRRRTAKKKKACiiigD//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One right facing elephant is walking near a wood fence.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

