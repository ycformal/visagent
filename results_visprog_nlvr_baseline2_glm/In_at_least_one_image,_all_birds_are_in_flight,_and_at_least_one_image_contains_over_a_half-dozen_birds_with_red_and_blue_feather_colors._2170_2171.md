Question: In at least one image, all birds are in flight, and at least one image contains over a half-dozen birds with red and blue feather colors.

Reference Answer: False

Left image URL: http://www.sandovallake.com/wp-content/uploads/2015/10/chuncho-Macaw-Clay-Lick-3.jpg

Right image URL: https://i.pinimg.com/736x/8f/9d/2f/8f9d2fdfc5f5708173a2e9733b410423--exotic-animals-exotic-birds.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image, all birds are in flight, and at least one image contains over a half-dozen birds with red and blue feather colors.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAqAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDkrK8lH7q5sEljc4XeuDMx4H1xnGTUl9ZQTwT/AGctEQSWycAFR0IPUdRnPWsi61m2EpUBptx3Ky5BxjlSM9PQiof7bYQfZsFW4ADDeT1/D0riUJXukckYXeuiIra5vbHO+cRQZB3bckn9ajurw6iFtjyzvsQKvTp3xUTRyCBnKERGQh2wc5649vwpjSzWUrxoT5bfdMffgc5rZb3RSR1em39rpzJ5sLbHiKfMAd5wOcHnn07VWfWI5bdYlysjSFI1ZgMLjqTjA+lZFjPbW80W8GS4yZP3hwo4PG3Pf+dV7RfO1i2iBVN5LIeNp4yMfU1MoJ+8wlTTdr/1/W53FvZRG2TGpwDbku7pvQErnJHp2PcVp6Pb2kLGCaaGOabAQKCw2KoC89CByR+HeuV0KW0k1/8Asd18yKeUvI5fdtKjOAfTtXeo1msTglHjG5oii7T64P41zzlyrlY0/c13/Qp6slnpV1M0qiaO6KEZ/gbIyfXPIqrK0CForCOSeVcTBI1Y4z1IPrznHuKk1UxSwCNlXMTh1kSLfsAHOMHjOeh9e9a1rqGYHltrWaNSoLupUFhwOnr/AFGKFCTjztWWwJRb83+Xr5/oS22mxyAPKvllwuzcw+YdyR681eeDS3jaycrKCfuuOHBzlcf1qgdZ5QlGmIcMu9MEEHqR1z/npVe7Id3d/wB03LjYDtGec/Wk7Rdupr7qTtuaUGjeHliCLbxBU+VQyqcD0orngsxZzHGTlsn5uh9OKKltkc3keZG0aCNZ0DrjPO3BNPZZ4HDxqHjZQWVlyyn0znn/AOtVqSzuF3Ro7uoUt8y5wPTH41Emi3UjokUbb3AdO+F9fpXW5I19jeKZJHaF0WYQtJHxkl9vI6HI/lT5TOlt5Ulv6E5Bwo68c9SPTrRJol41symZ3CnACnJBPGPats+C9Vh0z7RHcRSxlQ4QsW+XHQN9KzlUirXZUsM3tucglsby/AEIAB5MR6/U9jV6S2sbSVJh5iTggxsTxGfUd+DTU1YQAKY2VRIMuTgYHr7+pqFb23v7giSeQMVY5CgqCx5wPQDmttepzS5rcti/p1spzMjkTSDKStnO3JyRnkj/AArp1nuLbTbVI3khTa5ZkP3ccjjPGeOO/NchFKbcLNEnltENm5mLYA4z+XaumgW4hsjuiUoY1JgkGTLknO39OOOlZyuncSsr3ZNZokloXknScJIQxn/5a8cjHTHNX5tSuNPtLWa0tYBFvOYl5OwnIB+hH8qpSwFfItTGqRDMrKqFsqMk8DsOBn24pbe9kmviLUNDbrH/AKpCTuYtgZPf/wCvUSvK93e5SjZJJ7G4moTQ35mcxraysqpDn7pPXn8e/PTFXZ4/NvFddirGjKSJMKScbS2ewzmsDTnvhcMXjARW+bYm7IzkcHvwauxWsBSSO3uJ5HCn5F2k8knBBGMe/wCFZwjyy7ktya31NNNLvF3Ykt2G7qSSaKr2FxJbW5W4t5lZmLAmUyFge5KjGfailaS6/gbzUVK0dUZtuLecywmxEckyIsivIocge3vV2exBknvE2RGMblCMf4SAFPbGMjFeAmeYtuMrlvXcc0v2m4Ix58mPTea1eGd9Jf195rRlyRs9T3Kxxp/idJZI12TytKsoHYp8oxjjB/GtbUtVsorR7NnWOMRnJBK4Bz37e1fO/wBon4/fScf7Rphkdjkux+pqXg+ZpuRusQ0tjvX0NrucRuxWDO7YmWZR/tVauLDTrJQbXy5WwQVzlseg+vtXnPnSj/lo/wD30aTzHP8AG3510+zfc4pQu73O/wBOvrW61a2ElvMkMe4hMjg44PuR7110FxblmaGKKVFX93E0Wwh+eueuBk4HWvJ/DrMdYXLE/u37/wCya66SWRtKtiZHOIZG5Y9dw5rCrD3reRi4qM9NrHXjVLpsRX0UcarEWW4BwB0wAR1HIqa3sLdoJyJI2nYbigJG4DnI54OTx071y+pE/wDEvXJwZeR/wFKuQsTdupJIJUEe2BxSjT91PuKM1bz9TW0a2vAszO6KjzLskznKkcjnpzmrau1lc3HnpDCN+yDZuYlOitk5wfxp1+qiazUKAu+Q4A4yAuKi1AlAEU7V8wnA4H3RUTspcvcpz5Hyr7/xLBtmf/UTJBGvACSEbvc89fWiuRboP896K2WJdtYr7jJPs2f/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image, all birds are in flight, and at least one image contains over a half-dozen birds with red and blue feather colors.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

