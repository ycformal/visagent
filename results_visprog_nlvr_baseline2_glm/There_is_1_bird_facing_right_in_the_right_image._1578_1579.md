Question: There is 1 bird facing right in the right image.

Reference Answer: False

Left image URL: https://gmenchaca821.files.wordpress.com/2014/03/american-pelican.jpg

Right image URL: http://i0.kym-cdn.com/photos/images/original/001/221/831/ba9.png

Original program:

```
The program is asking if there is 1 bird facing right in the right image. The answer is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA/AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDJtLmPeyrNBjPUNVsDT5WL4jkcdzVtNHtBhvKiViMcCnDSYo0xG4TPoop2YropGeLy9reXu6LtGcVSfUrYSiFo0Zs8Epz+Fak0NnB8txPGGI4yoBrc0XQ7aYR3MCwSnIZd77QO+T3OPTvWc5qCu2XCDm7I5VtYitFKFMTDsy7cfUGmR64ZORPDuzyiLk13fi20in+wSNbxvO+8ys69VBAGP1rAGm22cm3iH0TFFGbqwU+4qkeSTiZT6lG8ZZsg984FNtpLWe/t2SE+arcMHGMVsNZ220BreFh7rSR2ltFJGUhjRs8FUANa2Zm3oOuGkUR+V1LgHIzx3qbFWVijW3Ekis5MoG0HHAGSc+vNFxbGCUryVPKkjqKmM/eepMqb9nF2K2M0mKl20u2r5jPlIdtFTbRRRzIrkYwFhndj/gJpq4kPDBc9i3NLguuHwvtmmmOJMtyW9zVWKuYQ0t7+e9muoApeRUjDdQF/nmuv0F4LJC8luYeQm9V/d7icDGOATwKyPtMeNodS3QKK7ma1Gl+B5yQPNkgDEn+9nIP4cfjXBjsFHEQs20/L9Trw2JlTdrXRneK2Rbixgc7WW2BIA5yWJrntuwY3OwPYrXX6rcLBdC4kCsyxxly6hgRt9+3JrM8RaRbrFb6lZQ4t5jteNRkI/wDQGuiglTpxguxjU96TkYJjCsSoOfQU6JGLBjHtqKeaCAr5pKDsN3Wqmo6jN9jlTTwPtpX9wrnIZuwxW7vYyNxo5HtoPKQt+8KtjtnufatfVI0ayRjgOnSuC8IXutXz+IX1edov7MhU4hAUK5yeo68CtPQ9WXXNJgvluJJmdRvV3yY27rjtXJyy57nXzr2fKX8e1Jj2qjaa5YX+qnTLSVprobjtjjJHy8nkelaNaGFhmKKdRTHYwPsVoUkkIWQMDu5HP48Vx3iGxkSN7zSNWmhMI3G1e6BDDvtwx/I11FlpE9m7P5/nDooec8fhjFZmqWGpNLuGpWttk52mM4/PvXQ1cxWhc0TWdMmgsrspDGzqrylRyOxya7jxv4wtE09rO2njdZimGU5AUGvN9L8PxpYJa+ZHKcks3lnv6E44/wAa2R4f8lP3dxFljku8JLfmDmsql9GzSHVI7zxTrWjadp0N3eahAguIlCoGDMSF/ujnFZOh+MdGu/DN5Y6tdJCzxkoAjYLDlccdemB+Fche+BdJddzO7Sv3WJkJP1Zj/Ks9fA9og8uSO7kB+6PPAH5YrOMJOKLlNJsup4nsHJVJHhXPR8jd+FXYNRs7vVbVY927cMEE4P19qzbfw3axxmMWUkYTr5l0cH+fP4Vf0/TLW2vIJRblCGBVhKXGff5RXRrYwVrnf6b4djHhbVbUsIrrWHkkkkxkoGXan5Lz+Jry678I654R1E6FZ3sTC4tPtF3dx5Cqm4qOG+6e2e+favTBra8DcFIFTtq1rcMn2hYjnarMR1Udj6jmuWMu50uJ5h4Ps7zQ/FdletfabA9oCEtoMPJPGw53txnOev5cV6NrV9ZX1ys9pAYmYZkBGMn+VZlzptnpd9NHZW8UKN8wKDqDz19OfpUWTVkku6ios0UDPE5PHWuzKA9xGQOmIgv8qcPH3iALgXMXt+4XP8q5iiq5mRZHSyePPEEgIa8Xn0iUUkfjrXYl2pcoB/1zFc3RRzMLI6KXxvr0337z8lxUT+L9ZkQKbkADuEGfz61hUUcz7hyo24/FusxABbrp6qD/ADrb8OeK9Wv/ABJp9vczI6PKFb90ucfXFcTXTfDyxXUvH+i2buyLLchSy9RwaHJgkj1e6fz7yCEMAF/eSEHnb0C/if5VOskcI449+tdn/wAK2tjMHU3wbH3x5X+NSw/DS0uod8l5exckbWCZ/wDHSRU2XYu5wovwGbdI7rxtGCdvsPapY7rzPuo344ruv+FWWOc/2ldZ/wB1aevwxsU6X8//AHwtJ3GmjhhK39z9aK77/hXNqP8AmIXH/fC0Uajuj//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

