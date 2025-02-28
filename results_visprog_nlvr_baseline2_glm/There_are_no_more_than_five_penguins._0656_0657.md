Question: There are no more than five penguins.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/ed/52/73/ed52735d062fa866b760cc305017a3d9.jpg

Right image URL: https://i.pinimg.com/236x/9e/31/28/9e31280380339b56199bb9206477f218--king-penguin-high-society.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are no more than five penguins.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABYAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDz/C5+739acoAOTGGx2zUhRBkKW5+lKYwOqN1xwRUXNCIqW6KozSPD8udyZHYCrCxxNwdyj65rGbWDaaqZERWEJO1JBlT25FF3Z2DTqWxGQclxilwezCrtrJb6paG8jtvJ5+ZEOVB9vamMifwg4FNPuhehVI24zjmjYADwCO/FTFQD0/MUmFJ4p3A1dAI8qdV4YsD0z2rTm1K2tzGlxeKnmnbHGgy5Pt/jVDQgfKuAhYMGVuEz0+lW7bQYfGfiC3snlaOW3d5I5EGV2qVzkdSM470Sk1Fvog0vqT+eqs5ledSCONoJ2+p4x+FIbmMsCJZec8EgE1Zn068tdUks5IWeSOVkkwmSTnHHOTn29qx7Xw/rNjPew6u5DNL/AKPCWGdpJ5I7ZwP1pe0SfLcdupoNJDvbEzjnkZHFFOSxRgfNXewwMhenA4oquddxWZzpc4wFJP0FAlXdyuD9BWikcbSbUdTnswA/n0pLj7PBAZpixVeWOOoHbpXMpq9iivb28c86JuI3nBOP5Acn8KpeNdAtNGv47iA7xNGMIwPD9yQfbnmvbfA/huLRNLF3MN2p3SB55T1TPIjX0Uenc8ms3x9YWGrtFNNh5FieFkA5JJBDZ9sfrVylKC0VyVZvc8k8KtqM9zEhgH2a4bYkr/JGW9C/QHtzW5rGjz6bdfZpoZLO6PKwXC4Lj1Rujfgab4N0VxqV9FGpMUUxiYMSQ6+hHQ16Vr3ho6n4Ru9PW5e5tlj83TxN80tpKvIUP1K9ueccc1onJ/EtCXZbHkUlvKrYdSSRnBHaj7M4k5hX1G2rsN2jRQzEkyBFZx1BJHpT/tSSg4jcn2AGDWUpOLsWtQtJTYWV5cj5DGpf5iPmIHArX+FF95viO3C7EMNpJnJ5YHbx+fP4Vz2uFG0a6WMzkCJnIcg4I/pik+GjSJ4msnU52o+7af4dp6/pXTR1j6mdTdHqsyQy/EaeQMBHG6yyoOTu2D8hkj8qq/E6KCODSdQRNspaSHzMdRgMA3rg5P5+tVtNuHfxZrlyCp/eKq4POOn/ALKK5/XBPr+teIZL6/aK10OAtBFjhmI4GPc5yfpThTje7FNsz49kcSRvAMoNuN7LjH4856/jRWc1uyhRJC7ttBLRgkfj70VnY1LwgwQRHHuzjcW/pVqy046zrmnWMgzGJllmyD84U5xURuIQwDK5QnczDqD649a2vCVxEfFa7A4Ux4XzBg52sf8ACuSndzTYSuenSXAhBzwK5DVZ0ub0bV4z1rZ1Sc+XgNiuYZ90zPnhea63q7GZZ+FQC2OqzNjdLqEwyRzgGu6dEtGMqD9yTmRR0B9R/WvOfhxdD7Nfop4F4x/NVNeiLKGAycjOKqLsJngmoXVvpXifU7WD5LXe6gZ+7hsjH61BLrts+AwBOMZxzWNrUvmaleXBP/Lww+uWb/CqMEL3c/lxkAngH04rGrTUpXZSZ0bzQXml3nkeady+Xs2l+SOOe1a/gWe20mwe+nQJe2we32Hjdu+bGPU9PoKz9CX+yoZY5J3AmIOEAIbjuavySW08htxOpkI+7sGD+lEMRCK5Uw5Lu9y/4f1eOHUbsTOE3gMScgE7jnk/WtPVtPtBpmt6gLkgX8EYZgQy5Vhg/j0Nc0bq1iISTyJNoI2bcn6c8fhUKy2MFn5EUM0dq0hkMULnarewzgDrxRHFwS5W9RSjruQyTsj4+fHYqmQw9elFX7K8sEt9saJEgJwvl5opLEQtq0Mr/blIyWUqfQ8Vv+CNs3iNfmyQJCvPog4rjhdEHOAT7qK2PB181t4ssnkB2STbMj3Xb/OopwcZGktj1HUAJEO081nRaUz2dy/HCN+eKNdv2sb3aFO1huBHStbSrhbjQ94HLkgiuq2picF8MZgZdUiZuTOXUH0Hy/0r0zLMAq9ua8t8ExrFrV7aq2J0DuhxySHJYfkf0r1HS7hXjYyFcgdvSkhs+e0s0u4Wd4zIXuXwAcZwo/8AiqtJYS2SEQsq8c46n26Vp6jpv9i2dvZzMrTC5mkypzlTwP0ArLV0U5VD9STWdVNsuKVjm/FFxcxz22JXT5TwrEelYP267/5+p/8Av4a2/FrbprU4x8rfzrnKcYq2xL0ZOby5PW4m/wC+zQL26AwLmbH/AF0NQUVXKhEzXdyxy1xKT6lzRUNFFkB6Ujwhh5jEr6Lwf1p9vdC0uY7iMgNE4cfUc1qvHazMF8iNhnkgVHcWcRRpVs2yB9xD8vA964414tm1jrPE/iSC1uoY3jiumeMOsUUgDYxnn0PI4q54M8X2HiJ5LOytjayRruaJ5A2Se4P8xXk8lnfG6M7IF2g5OcqM84Hc1HDa3NlfC6sYp47n725Ou7sc9jXZ7WN9zLkdjoLXUhp3ioXccqeZHdNkAnGN2CD+dd1L4r0JdfFraX6RtPlGJP7oNnru6Dv7V5YLDUHk3SRESMSVywBYnvVE2N19v8uaFw6gBUAB/MjjFTGce42rnReP75LTxbHHJKsiCIFBGcgA/wCPFVEuZJgpEfnFQAvoB6e1U4tDlZjLNtlZvuru4WtWK1jgGJJUQ4+6qkg1zVa6l8I4p2OU8ZFTNZgRlCEbP5iuXrqPGTh5rMgkgIwBIA7iuXrei7wRL3CiiitRBRRRQB607yRJsVSgPQAAECoxclWXcTgdWXr+Qoorz1FG6GvePJPxExB42hRj69KRpkYbchdv90EUUVpyKwbIljVtoeNXdDwMljip4ZPKLCPIxknK8fmaKKyetx3IZopJsbLkNv7DPy/pilFiQM74yw/velFFS5W0SA47xomye05U5Vvu/UVy1FFd1D+GjGW4UUUVqSFFFFAH/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are no more than five penguins.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

