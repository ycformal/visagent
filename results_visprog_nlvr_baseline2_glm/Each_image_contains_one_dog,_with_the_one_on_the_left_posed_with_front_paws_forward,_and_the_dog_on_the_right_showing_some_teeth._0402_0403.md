Question: Each image contains one dog, with the one on the left posed with front paws forward, and the dog on the right showing some teeth.

Reference Answer: True

Left image URL: https://moderndogmagazine.com/sites/default/files/images/articles/top_images/Untitled%20design%20%2840%29.jpg

Right image URL: https://pbs.twimg.com/media/Cwbv1_ZVEAMVZOy.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains one dog, with the one on the left posed with front paws forward, and the dog on the right showing some teeth.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABAAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0UykDpWdqd/aWUam6nSLzCQm89TXnVjpNxNJKlxr2pM0EhQ+W4XcPfrSeJdNNjolvdSXWoT2rzkN9plDMMY6Y6CtZ10o3iKEOZ2Oj1ORWQkEEEcEHrWfpdwu0LnnOMVkWYG+0ha9eGxvDsjm6+U54BIPYHqKp6lBqfhu8MFzqmmXA2s2LZtztj2B4rm503c35baF/U5ZNc1KWNJdlrbfIO2Wxyc11fgjUWfUtPEkheRGaJm9eDjmvLtO12OPSp4DseYyjkjlVPJ/Ouv8ABGqojfagGKxAyNGpGcA0oy1uypRXLoa3jnTftfibWvLTM32KK4jOOeCwbH1H8qo/DKzaXxCJZYQFhQsMjnOMVq32s2es6jNeowjaa3FuQsvIAbdkEc57fSmWiQ2soktw4kGBvXJb8zWkuXmuiISai4nTK+6LcD1Y4/Kr1oeWz+FeUeJ79zqYmhmZBYjChJMENnk8fhXd+EtcGt6SlywCyhikgHqMc/jXlOm4xUjrum2jpyc8D1zTwT7VQvL6GytZbmaQJEiEsT2FcFJ47vbnU4prd/JslkAMIQEuCcfMT/SiMXLYh6HpLthuCaKic5Y4ziiouOx5jZMEuJERifNuWbJ67Tin6xDFqnhu7tkkkBgmZowxGNo4bA6kDNZdndCDU5vObyZVdlWNh8wOfTrT7jVre2k0y3tmWdzIYnVgQJN3X9a7Z6x0OKm+WWpyp1OaPRZNMlVHmLqUAONuO4+o/pXMTQ3El2WdWLseGJzXUPDDF4n1NggWG3BC5Jxj/wDXVEampWXzrVYZI2ygI7VcX2R0Ss92ZUum3dsrOrEOBhhkE8+1dx8OsXkjxySojMhUREY3kDOfc1wunG8uZpTGSWZi5ZuQMc4NdZ4O1Fre9kt5ojCkn7xGHXdjIH51bvsyFrsdKLvTFm81reJJOhZPlP44q5FqGdsiTeXERwHOSf8A631ri9Qaa51V47eN5d77nKjAA759KZdXs0DlXbBqFUlHQmxqXVzFBLqb3se2OeRgjtyCc9vWrfhbxlBpjzxRWimJ2LKnmbWP045rF8TSWLxeZPG8kgUrAN+FU9ScDvXLWuzzklcneOODSjFThqdEm4y0PTfEPiaXX9PKRxNbW4b5kkkG5+fQVFLZW66hpFlan55XUuc5LEmuQja3v02tOVaFg24nofcV6D4Fsgv2e8jnFwI/mKnGY2wQceoIOamSVOOg0+ZnpYk5OD39KKYhBGaK865tY5241Pw548BmiSOx1tP9X5wCif0UkjGfSuauEV5Xsr5fKnhJK7l6MPTPQjpiuJuPNtiS8hUdiT/SrVv4hvLrdbTD7WxHyyZw8ZA4JJ6ivQU77nBKnrdFIiK21dZmlKo8hRlPTnpWX4httt07KiIpxhF9eaNWsrkYMtyXyoYFRn6c1TtryG5tfs95GzzIRtbdgjk569e1a01Z3HO9rGz4O015NSRLmFlSRDguCAx7c10lwsc+tGK1gSPaFUKMlif7w9sisG78WTX+n6Pp915CQaYxEc8a7XMZA+VvXBA6Vt6LrljcXDXcMMu4PjdtOcdvwrpfK4mcbpkV7dvDP9hyVI/hTJLGtC08J6vqeycWscXOUkuvuj6D+I/pWfHrUEeoSagYhJdbiqpKOF5649a6ex8VT3bxtcsvoSTgD0rllZPUvXoec+NLL+zr6KONmKFec927msew0+41FyLcpuVdzBmxxXonjLw/cSWG+RGcjlZQP5+lcBpLS6dfLLKgXaQVMi5UkHoaqlK8NDeStP3jo7XwF4lfkaZ8p+9lhzjrmu++GNjNPp1zIkqxxK37tMZ3DHr1xxWf4X1W41+V7OHSEVJeLmZZn2hCfmwN2FJ5zjrmvTlgW1hVLGGKFFAG1UA49OKxrz0sy0lf3Suj/L2oqRbBiMngnk5orgsze6PItU0ltjTsMknqewrmrVYU1CSK4ykRR8Hvvxhc+gzXqs0IkiKrgj3rB1DRoyHdYwN3XA61vGdjlt1OJu7OS7gW5Zo1RpGc8/woAij8TmorDwe+qzICGKyS7fNjbpnoAelb02gQuyJOu1NwJ7nFemeGbPSYpEWSaK3gtwGC7gC0mOM+yg/mfat4Sb2ZFR36Hl9t4GtbO5uLW7tPtkH2SR1uAxB3oecHseCMVpjwzD4JvkabVGOnXi5hk8rLA4yFYD2PBHX2r0rxBpmm6JpWtukrMFt2Me85IlmLcD8DXm/iu6vPENnYyBUV7eGMRBTkZCjJ981bqWdmzKEXe5vf8IV4e8Taiy2WuiK/AHm7YgVkO0NnGcnA4yK5+90W68Oan9knlSRdqyw3EYOyVD0Iz+R9KwtBOtJqKRxQNGs8wV5Yj8wJ7ex9DXpXirw3eX8NhH9ptLKWxtAkNuknmZIJLBsdyMfjSl7yNW0mdB5KzweVKMqV715z4w8JWEBtHicx+fOEcH7oXufrXY6D4n03V28sSFJl+VlbqD71sa3pFlrGmNZyY353Ix7GueF4s3k0zN0fUdD8O6ZFbWrW8MOSqBjznuT61cv/ABtpNhbLJLMjyZ2qF5zXNaf4Kt30x5b+4mMrzOkkKkBeD2PXP0rnPEOi2FtqcMVhD5cUUZLYJOWPfn2rZpdTK+p2X/Cw0m+aPT2ZemWkAz+FFc9YW0clorMsQPfIorJ2uWrH/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains one dog, with the one on the left posed with front paws forward, and the dog on the right showing some teeth.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

