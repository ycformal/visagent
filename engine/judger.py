import openai

def judge(results, question, show_analysis=False):
    prompt = f"Question: {question}\nLLM visual agent's generated program: {results['agent']['program']}\nAgent's answer: {results['agent']['answer']}\nDirect VQA result: {results['vqa']}\n\nInstructions:\n1. If the two answers are the same, then it is easy for you to get the answer to the question.\n2. If the two answers are different, and there is an obvious logic error in the agent's program (or the program fails to be executed), then the answer of direct VQA is the final answer.\n3. If the two answers are different, but the agent's program and answer look reasonable, then choose the agent's answer as the final answer.\nNote: When two answers are different, use VQA's answer ONLY when there is an obvious logic error in the program, or the answer indicates there is a runtime error (often with a traceback). You should ALWAYS trust the LLM agent as long as there is no obvious error.\n\nThink step by step. You should strictly follow the above steps and provide your chain of thought."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    analysis = response['choices'][0]['message']['content'].strip()
    if show_analysis:
        print(analysis)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": analysis
            },
            {
                "role": "user",
                "content": f'Based on your analysis, give me the final answer to the question "{question}". Only give me the answer and do not include additional words. Your answer:'
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    answer1 = response['choices'][0]['message']['content'].strip()
    if show_analysis:
        print(answer1)
    prompt = f"""Caption: {results['caption']}\n\nThink step by step. From the information provided in the caption, can we know the answer to the question "{question}"? You should analyze the question, analyze the caption, and give me the answer. Note that you cannot assume things that are not mentioned in the caption."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    analysis = response['choices'][0]['message']['content'].strip()
    if show_analysis:
        print(analysis)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": analysis
            },
            {
                "role": "user",
                "content": f"Question: {question}\nLLM visual agent's answer: \"{answer1}\"\n\nFollow the instructions below to give me the answer.\n- If we got an answer from the caption in the previous analysis, then give me the answer inferred from the caption.\n- If the previous analysis says the caption lacks essential information to get the answer, then give me the answer \"{answer1}\", which is the LLM\'s result.\n\nThink step by step. You should strictly follow the above steps and provide your chain of thought."
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    analysis2 = response['choices'][0]['message']['content'].strip()
    if show_analysis:
        print(analysis2)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": analysis
            },
            {
                "role": "user",
                "content": f"Question: {question}\nLLM visual agent's answer: \"{answer1}\"\n\nFollow the instructions below to give me the answer.\n- If we got an answer from the caption in the previous analysis, then give me the answer inferred from the caption.\n- If the previous analysis says the caption lacks essential information to get the answer, then give me the answer \"{answer1}\", which is the LLM\'s result.\n\nThink step by step. You should strictly follow the above steps and provide your chain of thought."
            },
            {
                "role": "assistant",
                "content": analysis2
            },
            {
                "role": "user",
                "content": f'Based on all the information, give me the answer to question "{question}". Only give me the answer and do not include additional words. You must give me a definite answer and cannot say the answer is not determined. In case the answer cannot be determined from the caption, your answer should be the LLM\'s result, which is "{answer1}". Your answer:'
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    return response['choices'][0]['message']['content'].strip()

def judge(results, question, show_analysis=False):
    prompt = f"{results['agent']['program']}\nThink step by step. Based on the execution result, give me the most possible answer to \"{question}\". Note: VQA may not be accurate. Omit VQA directly asking the question when we can already know the answer from previous steps."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    analysis = response['choices'][0]['message']['content'].strip()
    if show_analysis:
        print(analysis)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": analysis
            },
            {
                "role": "user",
                "content": f'Directly give me the answer to question "{question}" without additional words. Your answer:'
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    answer1 = response['choices'][0]['message']['content'].strip()
    if show_analysis:
        print(answer1)
    prompt = f"""Caption: {results['caption']}\n\nThink step by step. From the information provided in the caption, can we know the answer to the question "{question}"? You should analyze the question, analyze the caption, and give me the answer. Note that you cannot assume things that are not mentioned in the caption."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    analysis = response['choices'][0]['message']['content'].strip()
    if show_analysis:
        print(analysis)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": analysis
            },
            {
                "role": "user",
                "content": f"Question: {question}\nLLM visual agent's answer: \"{answer1}\"\n\nFollow the instructions below to give me the answer.\n- If we got an answer from the caption in the previous analysis, then give me the answer inferred from the caption.\n- If the previous analysis says the caption lacks essential information to get the answer, then give me the answer \"{answer1}\", which is the LLM\'s result.\n\nThink step by step. You should strictly follow the above steps and provide your chain of thought."
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    analysis2 = response['choices'][0]['message']['content'].strip()
    if show_analysis:
        print(analysis2)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": analysis
            },
            {
                "role": "user",
                "content": f"Question: {question}\nLLM visual agent's answer: \"{answer1}\"\n\nFollow the instructions below to give me the answer.\n- If we got an answer from the caption in the previous analysis, then give me the answer inferred from the caption.\n- If the previous analysis says the caption lacks essential information to get the answer, then give me the answer \"{answer1}\", which is the LLM\'s result.\n\nThink step by step. You should strictly follow the above steps and provide your chain of thought."
            },
            {
                "role": "assistant",
                "content": analysis2
            },
            {
                "role": "user",
                "content": f'Based on all the information, give me the answer to question "{question}". Only give me the answer and do not include additional words. You must give me a definite answer and cannot say the answer is not determined. In case the answer cannot be determined from the caption, your answer should be the LLM\'s result, which is "{answer1}". Your answer:'
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    return response['choices'][0]['message']['content'].strip()

def judge(results, question, show_analysis=False):
    prompt = f"{results['agent']['program']}\nThink step by step. Based on the execution result, give me the most possible answer to \"{question}\". Provide your analysis of each step. \nNote: If LOC gets [], it means the object is not detected. You can assume the object does not exist on that part of image if the question is about its position or existence."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    analysis = response['choices'][0]['message']['content'].strip()
    if show_analysis:
        print(analysis)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": analysis
            },
            {
                "role": "user",
                "content": f'Based on your analysis, directly give me the answer to question "{question}" without additional words. You answer must match the question. Your answer:'
            }
        ],
        temperature = 0,
        n=1,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
        )
    return response['choices'][0]['message']['content'].strip()