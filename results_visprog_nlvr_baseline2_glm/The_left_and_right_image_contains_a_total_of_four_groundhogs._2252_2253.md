Question: The left and right image contains a total of four groundhogs.

Reference Answer: False

Left image URL: http://2.bp.blogspot.com/-llsSG2BnOKA/UDt7PplW6uI/AAAAAAAARvA/y6JjmnauyoU/s1600/The%2Breal%2Blife%2BMowgli%2BSchoolboy%2BMatteo%2BWalch%2B8%2Bstruck%2Bremarkable%2Bfriendship%2Bcolony%2Balpine%2Banimals%2B6.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/6e/6c/fe/6e6cfed2a015dda65cb70ddc7b122732.jpg

Original program:

```
Statement: The left and right image contains a total of four groundhogs.
Program:
ANSWER0=VQA(image=LEFT,question='How many groundhogs are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many groundhogs are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} == 4')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAhAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0uy8c+FtTjx9sS1dhylwmw5+vI/I1l6v4n0OwnhitpPthf75twGEY9STjJ9hXjKw3LfMIpR/wEkVZjeaKQozFWVQWGDwD6+lTGu4/CDpqW6PVtX8UaTaeG7zUbJ457qGLekDhl3MSBjp7549KofDrXLzxgt3Bd2yq8CiRZkjKKQTjB7Z/pXketeIblrmXToZgkaKFZowMsep59vSu5+GPxJtNCSfT9YkjSE4kadl2t6fj9K1VapdSuT7KnZqx6zFoIWc+ZEHUDoeRUNz4T8wHytqHPVjwagufiXpNklpNe2WoQ2d5kwXfkho2TOA3ByMjnGM45rdOt6ZcWwmg1CF4mXcGDZGK1WJm3dMzdCKWpj2nhfTbeWJbm5hlum+7CzDB/DOTRf8AhiHzA0EITd1Vc4/AHmvHfGV0j+MtRnh2sjSgxzIOD8o5BqO38V68lu1sNUvDCVIKecSMd/es/rMlK9yvZRatY9Uj0FJxmJg4zjK8jNVdP1Wz1e5msrPUUu5rVdvl84AHBK+uDxkV5mviaTQLRZ4mljLuFRYpdoY9ea0fhFrWh2fiSeTUI1gvJEfypfMyoBOWJz0/pzWn1uTs7ErDxV9T0A6DPdMxJLMq9XJ59qy7vRJ4ztMTEnpgZrvYfE/hybUEtI9StftMufLRjt34JGVJ4IyDgjrjir91cCJD5bIMehArVYx9iHh7bs8xh8L3JjzLpMrsTkNv28fTNFdbNr0iyECaAgesyH+tFQ682/8Aglezijxy2uftFysCMVATLN0PpWvs0230uVLklZJO8bAM5HT5scVwFo13bSNl2kLc5xg1fvZJb6zjtyhCo+8kjk14nJruepGfu2LknhMa3Zzmze3ElspdpiDmX0Qn2Heufs9NkewdZWUpMQqTKc7fc57ZrqdH1zU9J0m60+3tkZJkK+c2CVyOo+lY1tpcljEz2YKkEDynyQ2fT0zXQqqtymLh1LWnzax/wi0gNw0tn5gxbzncVAPDr6H29K1NMvcae0YLFFx8m7jJ71zE815LczqlslorEFYwx2oMc/1OKDrUccf2a4027ePO1WVchvfiknJPmjuOSjZxexumdVu3Zl2gNnGOv1rSsVhv0DXG3yCxBjJxkA/r9K5CdIm3QRuyR9VwTkVbsXubfZtfOzpu61lJXd7lU2om1qOkabr2qm2s3WRpDtTcP9U3dgB2A7H2rl/7Bktr29srh4ZTAxh3qclCe+DzjHNa+mvd6RfC+s7gRT5JLsuevJpGtftV3PdtN/pszFzMvDMxOefatY1FFWJlG7uOS81K48NWcd5NHcW9vJsgV8eZCo4+Uj+E+nbituXVZJrKESSvI235VZ8H0/H61zE1hqMt3LJIVZi2/EahVJAAxj/PeljOovKF1CxtiijIlQ/Nn6HpQqjg7xYpRi1ytGg7qrfPEM/59DRVM3Cqxwxx14bH86Kft5mfso9jMh/1Q/3R/Opj/wAfMv8AnvRRRLYpbjJPv1ai+5+FFFZ9ixJf+PmWq6feH1/rRRTYmNh/4+G+p/nWmv3W+ooorJ7iRbg6fhT7b7/4D+tFFS9i0S/xmj/lj+BoopdQe5hTff8A8+tFFFbrYk//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

