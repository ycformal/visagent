Question: Are there any men to the left of the bowl?

Reference Answer: No, the man is to the right of the bowl.

Image path: ./sampled_GQA/2360799.jpg

Program:

```
 Are there any A <planar pos> B?
Program:
BOX0=LOC(image=IMAGE,object='bowl')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='men')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='bowl')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP_LEFTOF</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDy8IueQPyo8tc/dH5VKFp22nyhci8pcfdFMMS5+6Ks7eKaV5o5UK5CIl/u1AcnJX7oOOKuGPcOpFQQQNLdLCn3mcKPrmomio6jlQFQGOD0zmo2XBxzXqWkeDbGGPzZsTSHuyZ4qDXvCthLDLNDHsn24U5+U4/TNZ3R1/VppXZ5oDipUbtUbA5+bA5waFO3jvSasc5Zz79qYx96RTmlegBn40UYoqQLQWnbayhcyudokcfjWnZhntwWJY5PJrqhNSdjOUWlcftppWrAWq9yspi2wqWkchVA9ScVb0VyVqXdG0q61y/FpZIzlSDIyjhFzySelO1TT38O+LvLdJI40lV4jJyXTOM8fjXu3hjw9a+HtFt7GCNUZUXz2A5eTblmNeQ/GCSFPF1vFGgEi2imQ+uWJA/AD9a5nK7uzr9moR8zvkee3jjWPJVweCd3AGc9OKsG3SSwkZiXDIRgnjn2rkfCmvDWNDgtnfNxasFkBOC64wDn/PSuugCxxMd3ySHhSc4qTvi1KN0eS674eTTrKe7NxlvOVVQjGc5P6Cucz8wrr/GUaXWoRCN1Lxhtyntk8CuObPmFWGCvGPSi5wVYWltoWk5oY80yM44zTmoZkhpJopSBRSAoWwzOBjsa27AZt/8AgVZFs4WZAEXoyk+uRW1p+DC2Oxq6XxDn8Il+zxWjPGxVgRyKq297Np+o2873TfI24EoDgjocd+avXEbXFgythHK5Oe2Oa56YSTTEkkk9K1qO2pnBHvnhL4jW2t2628kS/a4lPmnOA5J++B6H07VyHxksYpLuw1qPAeZfs8qg5+7yp/LIrH+F9tv8QSybhxCV2+pJH+Fdt8VrSL+ydFIQZF0c46AbD/XFc99zutzRXdnk2hteQXgntZGi2feYDr7e9elajqbW3hqzvY5nkmuG2qSflTj5vl6ZBGK46EMqF/TAH+9/nmrEl7cSafbWbOxgjLOqEAYYnk+9ZObtc6qVFRaRUf5yXYkuTyT3PrUclpHMMug+vep1GRnFSY4rJTaOl0lLcxJ7QwHIBKZ6+n1prABM9z0rbKAryOorGu4/Il2qTtIyB6V0QndHl4ihyO62IiPaikB46UVRzFBDiVT71t6W+5ZB7g1lSQJHaW06zBnkZg0fdMEY/PNaGlkB5B7CnSfvIc/hZoXLbbd/cYrBIjEvzsdmSDs5Nal5K24oWXaSMDv2/wAaypSWcEgBu5A/nXVOzijGLaZ0WhTtbAXNpuhk3n5lPIwMVpa3rOo6vDaw3t00iRSDblQCPy69Kpaa8MekNGqqXOzDenXP61FcBpCqqRncMZrzJzbm2fQ04xVBLsSkE7cFjzkKD3NNVdq49z/OnMih8SIDxwVkzinKAo4qG+5cFd6KyFAxgcUmeM0E4BPpSD+Ie9Qi5Ow7ofwrH1L/AI+APRa129azNSjZrmIKrMzfKAoySc+n4100YylJRirtnn4v4LlEdKKsv9ntj5dwskcno6sD/KivVjlONkuaNKTXo/8AI8n2sO5SktZngtmEYy4IQKoywB6+5zkfhUtg8i3JRIyzMvQ8Y5+lJI86JZwhPurvQ7Dk7jnoev4Vr6LaQT36rGyPK7Rwq7hkEe5wucAgscH1rvoZdCleNeLcu+8U9N7Nd+6JdRvbYx5JC0jyttBYjAz0xUDspY5Y4xjpXQeMbWTTNWj0xzCyW0KBGji2fKdxwcknue9c2cEj615ldclSUVte69HqvwaLVnqbGkShoDHn5lPI9quh8yBc55/KsGFtjFlZg3Y56Vb0+WR7hTJIx6nBPFcNWj9o9HD4vRQaNjrzxk9/al4qINtX36Uu7oBXIz0lIkJ+Q0QtuGDwR1pjNldvali+Uk5z9aaREpakjiqs5lS8tJ4Y3kaGRZNqDJwGBq0zZqleSywPHJFI8bDI3KSDXVhp+yqxqdnc4sV70GjX8aLLrOsQ3Wn2F68QtlVi1sykNliR+oorJTXtVRQovZcD1waK+uw3FMsPSjShTVkeI8O273KumokjRyGGILtCZYkgkfxH0/CtG8t47W38xJrZGZ05hR1K/MOck9utdZF4bs1IZ41yOm9yavxabYpxmEkdlQH/ABryKtaVXG/WpLqnbVuy6X/4HyO6OIjGl7NX27q33cv6nld5bPLcXE0U0t2VALucsec8559KzhwRXuSW9uqEKCAeoxtzXKXPhTTdOur3VJGD2iQOy2xX7rEev8qzxk54mp7ST6JfcvKxjzRu7KyZ55u6HHardi2J+fQ1WUAn5qkhYq4IrglqmjSEuWSZs7sgE0oPf1qkbggkKMjsSMU5biQ8BQK5vZM7/rMS2Wp6HApq2V29obnIEYPXFInCAE5PenKm4bijXU3oTKcjnvVO+YFlUduauZrOuDumJ9OKqKM60tLEYFFOA4oqjkO3sGlv5IhJM6ARhj5eAWOT1OM/liugUHb94/TOKKK9CGxgxQcA4rC8Wu3/AAjd1g4+5/6EKKKcvhYLc8yAqWMfMBRRXA9zfoWGHWgfU0UVTEhwZjhSzYz0zxWgB0oorKob0Oo7PX2FVNoZCx65oooiKruNxRRRTMj/2Q==">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAEsAB8DASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDyvYmR8tHlIO3FSYox61PKh3GeUh7UGFcZwfzqUEcY60hXHfFPlQXYY5o5/wDrUuOKB2qrCAcdaU9c0tGPTrRYQcEc0oxuzzShaMdKoAxzS7cnAzS45+lLjPagAGaO/SgUvpQITp9acpUEbgWHpnFHB7UoHYUAJQB7VW+3DkCMn8aQ34X/AJZ/rUe0j3K5JFzBoHWqDaljjyh+dA1An/lmoH1p+0iHJIrBk5yPxz0pu9T1AxUYYsMFsdxxTQecE/nXKbk3BG7aMU7YMkDsP607Hye2KdtznHpQBT7UmOPeilz1zQBdCjyc4528UqAM447U6PBhHUjHFPtv9cvPBH9KFuPoZh6dqaaliieaRY4wSzdBT7m1ktZNj43UXV7BbS5ciGLZCfQUyNirq3t/jVySARWFg6sredbhzg9CGZcH34qrtOOACMf1pPRjWxSikMTh16jvRNM8z75CS1N45yOexz0pOnHtTsK5pQybrOEHogK/qT/WjJJIA556VDanMDL1INTBtrA8+lJ7gtjPYDOB09T3pp4pTSE8UxFqzP3xnHepnIBwOmep+lVrZsO3HapWOTSe5S2Kp646ZpCADgZNBJzzzSY70xEsB/eHjt3qQHrnqDjNRQ/fqUfxDPGaQDbaET3cUJfbvYLuxnFaGv6K2i3McRk3q6hlOMVn2knlXkMhBO1wcDr1rc8Watb6nNbeQSSkY3H0JHT8Kyl7T2it8PUpcvK77nPR43g1OF5NQIcOPrVjJx71qyUT6XYDUNQjt2lESHln9BVe9gS2vJYEkEioxXcDnOKjwce1Wbqxe1trSdnjYXSGRFVwWUBivzAdOnQ1W6J6lNSNw+tWDkjFV889Bj1qcEYHFSykW9ItYbvU44bgsImznb16Va1uzgsNV+zRKWjRuA/JIIB5xVDTmAvoieme1a/ilca8WPGUQ+w+UVpZct/MyfxEn/CNpL4dfVo3Rtt4LbysYJ+TcW+lW9H8HR6jZzTS33kSRybDHgf41lxOW0q7ZbmJQroPLMmGYnPKjvjHJqWwugunXwMqhzsZSxwfvY4/z2rVKPUV5dC63hddNumK3jzy2xDSGGDKIfck1ha7LJLeiZ7r7QSoySgXbjtgV1mnyXHlTicPJHIdx3/dPXBx0J64rltTkjupmkVSuw7dvrWcn9lIa7sz0QNG7AcIMk1fv9La1sra5jldllHzL/dPX8qgsrO4uneG3i35GTlgoGOeSfpV2Cc7GF3ESEUKsf8A9btU2b2KvY1typIY0lcx5+RQeVFYOpP/AKbKqoF3Ht3rdur42R2xWsS7xnf97+dZb3DSXKuIckcnP8yaXJJP3mW5wa91C2lreuiG0inZ8Ers4CHPr3q/D4O1S6aSSUiAbcqAdxZsjj27n8KeJ9bdV+ztGidtpFNa08RXbDzLggH1lwP0razfRmd13GXjQuoigTO08NnOB9e9UHUjgDGeDV3ad4GCfYU42FzPIfKtpCOx20O7ZKskJpl7PbuqModM9+CK623eJxnzkUY7n+lYFvod6B80YX/eYVox6JMR80qD8zWseZIh2NRBEmdqIv0FSjcThVJPsKvLHEgG2NR+FShwO4rYkoiCZhxGfxqRbKY8naD9aueYCMg8fWo3vraI/PPGp9N3NK6GZiy377QBbIT2L7j+lQ3U8Vr5iX+qJFjIaNMKR/WsbTd+j6h9otJWEwVlV3wxQkY3DI4Izwe1WLfw3YTE3Fx5s8rHcxkfOT71mrsewW+s6XM629rZ3V0B0yxI/HsB9a6OMW8QG2ONCRyFUVXt7O3tk2Qwoi+gFWgi+lWo23Jvc//Z"></div><hr><div><b><span style='color: blue;'>BOX1</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAAoDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDy8IM8gflRsH90flUqrTtlPlC48LTsVlC5lc4Er9M9af5k3/PV/wA6j2q7FezZXthmbHsatjbgVBbOFlUbF+6yk+ue9WeKwNijGdsyn3qzuJ5pkkCx21rOsqs0pbcndMHHP1pce9Te4yX7FcTRQGOHJKMyhF5ZVPLH17/lV9PDmsyIrrptyVYZBCjkUX8T2T2lvDJ5gWNgG2YYhjnkVOt1fKoWO6hMYGFJTnHbvWqjHqZXfQe4SXUVDqvyjYpZztznqdta40JsD/Q9K/GOQ/rurah8NWikM6ZI/vyH+lXP7Hshx/o/+fxrojStuQ5tmVYzzX9xAskrIPKDtsxljk9Scn8sVv4+n5CiitIEM//Z">, <b><span style='color: darkorange;'>object</span></b>='men')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAAoDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDy8IM8gflRsH90flUqrTtlPlC48LTsVlC5lc4Er9M9af5k3/PV/wA6j2q7FezZXthmbHsatjbgVBbOFlUbF+6yk+ue9WeKwNijGdsyn3qzuJ5pkkCx21rOsqs0pbcndMHHP1pce9Te4yX7FcTRQGOHJKMyhF5ZVPLH17/lV9PDmsyIrrptyVYZBCjkUX8T2T2lvDJ5gWNgG2YYhjnkVOt1fKoWO6hMYGFJTnHbvWqjHqZXfQe4SXUVDqvyjYpZztznqdta40JsD/Q9K/GOQ/rurah8NWikM6ZI/vyH+lXP7Hshx/o/+fxrojStuQ5tmVYzzX9xAskrIPKDtsxljk9Scn8sVv4+n5CiitIEM//Z">)=<b><span style='color: green;'>0</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 0 > 0 else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No
