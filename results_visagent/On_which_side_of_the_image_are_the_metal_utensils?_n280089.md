Question: On which side of the image are the metal utensils?

Reference Answer: The utensils are on the left of the image.

Image path: ./sampled_GQA/n280089.jpg

Program:

```
 On which side is A?
Program:
BOX0=LOC(image=IMAGE,object='metal utensils')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='On which side of the image are the metal utensils?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABNAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzhNQjxzFP/wB8VMuoRAghZ1PQ/uz0qnGtW4VBOM/rQBEJFvPEdrLGHEYwPmXHODXTJH7VVsirRgowZDyCDkGtFF4oAdHHz0qwsdEaVZVKAJII+BVxI6ZAnAq2q8UARM8cK7pHVR6scUC7tf8AntH/AN9CsvXkV5tPVgCDcdCMj7rVlzajYRTGMCMqMYKRhqAOsjngkYKkqFj2DCrAQYrmLWa3ubdZYRFneMbQARhhzjqK6iI5iX6UAVpYwXNFS4IZvrRQB4qks0TfNkgdQwx+tXYo5r2K6FpC8nlws7HIGBjt6nnpVBo7hPmuDhnGSoXge3XmpdI1G5sb1bjaptzIIJQD1yCB/n2oA29EDQ2dvEeu3p+taZ1BUk2Ipcg4bHasa1uTFJFuIxgL15z0rTspoVjdQjFgTkhTzn/9dAGxb3EMhGx60ExiuY06Q3OsERtboiEgrco+Dx1xjkfQ1p39zdWYZ0WCQdVSBG5H0xQBuRvipjcDIXPPXrWVptxPcQiUPaFCwyskbBsdwNwGDWel1PPrYtTJbhOSu4OV47Ftu3PHTPTvQBY127jS8sUMiblm3EBhwNrc1hzW9pBGJLlZGaRd+2NvmQZ9T168/SlvLRodYZS6KggZU8lHkAOd3zEjuSfWqMVxcJpskYtL9bosdsixucDPTp0xQBvaPbeUivtdEdVdA7Akgtzn+Y9jXa24zCn0rzLRriUXoMy6t8vznzUYrx1zxk9ulej6ddxXFqjRMGQ8Aj1HBH1zQBYCZJ+tFWY48gketFAHkT+W6YZHIPGChqoNG06W3k2apJDuIYh7MsR19Gp1hqMF7YkqFByBggA9RVddrMqs7FjIQD2oAq+IDDaWyG2u7iSV5Ml/K8oAY7fMT/Ks15V/s0TC9lMgQNlpzlnLYK7RzgDnPt710EOnxy6tZx3KI0PnElCQ275T26nt0rtbDwzoV5amYWunqEG5wygbR3Jz0oA8s1GZI4ka2v5T821R55YsmPvED7pz2/wpbeeN9Kkke+kWYbyS1yQwIA2BV/izzk9vbHPqo03wdCVDz6MpI44B/pWrbeG9AnuJLe3XSZJo+HiVULr9R1oA8F+1SP8A6y6m/wC+yf606SdSPlu539mJH9TX0QnhHT1/5crL/wAB1/wqYeF7BelnZf8AgOv+FAHz5pktsVl+03BXBH3pWGE53FcdW6YB4qvZXCm5Hnzvja23dI23djjOOcV9FN4dsV5+x2YPtAv+FC6JZA82tt/35X/CgDwBZdNMlyGmYxhhgs7fd2n7vqd3r2/GvWPh4u/wXp7dwZM/99muvj0m0L4FtbjPfyV/wqOzt44wUijVF3E7UGBknnigC3ZKWiYkdHIoq1ZxbITnuxNFAHjt54WjkRHsoFs0RSWWLJ3HPUk1ci8EqqOEvLhd2dwaNTz9e1d9c6ciafOxA+VCa0Y9PTnigDzC18HS2+oQ3S3cskltODh8Y2kf/X/Suk1P+z4vCd0LvYhETIJZR918dAetdT9gjS/KeX8s0J6eqnH8m/SojaQPO9ncwJIlzHvCOoZSw4bg/nQB5bbwWd9odruh0WRFfb50UyrMBuBYEFgOhP610OkazoWm6sk0kunDUbrcrLAytg8Y+cc8gdz1z2rA8Qa74VtZWsovBMZkgchpbqPyQfThBk/iaztO8a2enzNLaeFNDwgySiOxUeuSTQB7Pb6pHMQPJfPtVzeGGRGa57wf4zTxRvjOj3Vo6DJkC7oT7BsDB9q64KPSgDOmby4XlaF2VFLEKCSceg7153qXxUtbWdo7fQ7p9pwWuG8rn6YNesLwelea+LdD8e6pfOsFxbzWBYmOOGQRDGeN4PUgYHegA0D4iR6tfw27aJdq7sADbEzY+o2iu+l0z7M5ZkaME5yBlf8A61eIy6F42tpyh0m/jYDG62lAU++VPNdToEfj2JlKzfZE7i9vGdfxTDZ/SgD0tIzsGMH3FFOjGn+RF595AZ/LXzWjYRqz45IXJwM9s0UAeZ3fjjT2s5kPiKAkoQFXZzx7LUjfEHRl+/4kc/7m7+i15GszrwojH0iX/Cpo5pOfnI47AD+lAHpzfELQXurdxrV7IqFt5Hm9CP8AGtvRvFGn6hY2t0uoxG3WaYiS6cK+Rtx945714rcu5Me52bAOMmu+8B2trc+A7ZLi0t51+1yv+9hV8Hgdx6UAd5J420OHIk1nT+Rg/vUOR6dazP8AhK/Bcb7hdaOGznKwoT+grnPE066Nb2z2VraxGSXYdtvH6f7tYUGv6pNcIgvHjycfu1Vf0AoA9JHxB8Pbdserx4HRY4mP8lqJ/H2lN/qrm9k/652kp/8AZas6Xey6Pp1x5skl+29WDXBGVyMYGB04pLrxRcKzw/Zbdkb5cMueD2oAot41gf7lrrT/AO7YS/1FQnxVLKD5Wja7L24tiP5tVaTxvqETpDZ29pbwtAk6qEJ2kscjOeRxT5/E+qS37W3mxokqBv3cYXBKkn65IH5UAD65qLKWXw3q+0DJL+WvHry1MNzr8/8Aq/Cl4c9N9xEP6mm32v3ccNxFcu9xiFQ7ZCbgxPoOOlS6bfXl7aS3k11IWt5CkQU4wM7ecdeB/L0oAw59d1KGd4pNGijkRtrI92MqfQ/LRVPV5ri51KWR7mYHCjiRh2HvRQB//9k=">, <b><span style='color: darkorange;'>object</span></b>='metal utensils')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='On which side of the image are the metal utensils?')=<b><span style='color: green;'>right</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>right</span></b></div><hr>

Answer: right
