Question: At least one bird has it's wings spread.

Reference Answer: True

Left image URL: https://images.huffingtonpost.com/2014-03-10-Zackvulture1-thumb.jpg

Right image URL: http://i.dailymail.co.uk/i/pix/2011/09/20/article-0-0DFF2A0300000578-218_634x423.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'At least one bird has it's wings spread.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAjAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDq2dl8pIYpJXZiW3Ptwo69uTz0NXj+6j3FFjVRuZmPAHqTTG1bT47ctGfNkiEm2VVYKDgDHPDdunfNY0r2Wpm4mubpRpyN/qmyVlcDLZ7so6Y9ucVy8j0NVKxmrrettpc915PmR3ckq28QjG4RA7RICp6Z4z37cVraPrLw6cqyTWsjW8AkubaNArQDOOOee3B55zmubv8AT9RnvrD7NeoTdOjRxqQAsQYEKAB8uAM4B6Gsnxjr+tQeKzGtzp6hyVlmhtsSMrjBRieuBxx+pFauCehLb6npN94m06KwRRKzzZ8xQF27hxwCepFUZL+e4sblPIaG7S3lnRUcOCqrndngemRXH6PeDTLeefWtGkurYBRa3DIG25JXBHBAI57Vs3t3/oKtaWq/6VZMkcu3aFTDDHU9AG5z6VlKlF2Qep5/pPifU7OG4itZIokmnFwzYzyRyoz2NdDJ40uNgS0toVdsAkgtg+3pXFrEkbIjKfM/ut0XHc/nV5bS8wXSNzHx0GxeadSNFu7QoxdtzXl8S6urb3u0Qp32rn1qsfH2pNMxLJMSejJgfpVSPw9rF7G0llZSXSJgt5LBmUHpkA57VnwRQMxUyKr98cEH39KPZ02ruKKt2Z6PpHiXT9TjhhmcRXRHEeTy3PHTn19q07nUUtYGkuGCJjduY4GfSvLtmnWtsC87TTE4xuAC/gOv51qI6Tolxcu8m3pvbP5DoK5J4WF9NhqLZt3njdVumWC0kmRcDeZNufwxRXMyFWc4U4HAz1NFbLD0EtiORnVa/rSpZadYWsj+eygyqOxJOckdMnmqmlWOuajcMLyOA2qxFLeLfhU544x0HXvmu3XWdHb7up6crEcE3Mf/AMVUo1vRY2Lf2tYE8K2LpP5ZrZ1OyK5V3ONg8I+IpYb+O61O3iF0qpuTcwBH93ptyOD7V0ltp+qBLeS+k0+7ktYdtp5UJJRsY7g8e3rzVyfxFo8Kq39raey/dbbOmee/WoBr+m5f/ibWIJJABuUyR+frWbqS7D02OcvPDevSqpWffcFfmMzAqOfuhenIrp722J8PPFInlrDaSARp/CdpJHp1py6/o5lUtqliqdgLiPAI/Gn3Os6RLbTwx6pYFpIyoAukJOQRgDNJ1X1QKyPILa8AgDNGHZFB+YDI/GpZ7u5eF2csqMQQuc59K2L/AEu2hjaE20krBPkUABc9z7/Ssm3KXVhJps159naJBIjMhbaMngjr+VZRtJcyHGjePNcbpPiS502ZTvkjjVh5hiRQ+3Izz+GfrzWFPBDqGr7o5GgW6ncmaXA4Yk8gdTn0PQ1oLo/mxxtHc+a033RGhJ+p9B2zWzpXh20g02U3cEl9fTfJBbMuEjXJ+Zj1DEjj2rojUSVmZ2aWxDBpfh8f2RbJYy3Vwr7r7ypjMZsE4SMADAPXsePxrG+2RWt/Nbxlo7VZC0Jc5KoTx9fSu/8ACmiWfhGxur7WYXfVpFZrW2Q7wsXTPfDbsjOcjHauEttPP2vypYGXzGJHyA4B5/ziiVRCi7aorSGSWQtE5KjjIRjz36CiumtobG0hEcGmwuvUuGdNx7nAPtRWTxVtoi5jyWiiiu8AooooAKt6X/yFrP8A67p/6EKKKUtmB9DSEtOATwDUeowRXMQeVFZ1OA+MMB9RzRRXhN2WhrfUqXSqi2zqoVvNkXcowSPk4J71q36qLmNQAAyDPqeR3ooqanQSd1dmabWCzvhb28apFkNtHIycZ/PA/Kpb6NBHK4RVZGypAxj6UUUrt2uZvcdbASK5YAndjp7CiiikNbH/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one bird has it's wings spread.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

