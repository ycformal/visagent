def convert(chain):
    input_image_var_name = None
    n_image_vars = 0
    n_box_vars = 0
    n_answer_vars = 0
    prog = []
    lines = chain.strip().split('\n')
    for line in lines:
        instructions = line.split('|')
        is_first_instruction = True
        is_cropped = False
        for instruction in instructions:
            if 'INPUT' in instruction:
                input_image_var_name = instruction.split('(')[1].split(')')[0]
                continue
            image_var_name = None
            if not is_cropped:
                image_var_name = input_image_var_name
            else:
                image_var_name = f"IMAGE{n_image_vars - 1}"
            if 'LOC' in instruction:
                if not is_first_instruction and 'CROP' not in prog[-1]:
                    prog.append(f"IMAGE{n_image_vars}=CROP(image={image_var_name},box=BOX{n_box_vars - 1})")
                    n_image_vars += 1
                    is_cropped = True
                    object_name = instruction.split('(')[1].split(')')[0]
                    prog.append(f"BOX{n_box_vars}=LOC(image=IMAGE{n_image_vars - 1},object='{object_name}')")
                    n_box_vars += 1
                else:
                    object_name = instruction.split('(')[1].split(')')[0]
                    prog.append(f"BOX{n_box_vars}=LOC(image={image_var_name},object='{object_name}')")
                    n_box_vars += 1
                
            elif 'VQA' in instruction:
                if not is_first_instruction and 'CROP' not in prog[-1]:
                    prog.append(f"IMAGE{n_image_vars}=CROP(image={image_var_name},box=BOX{n_box_vars - 1})")
                    n_image_vars += 1
                    is_cropped = True
                    question = instruction.split('VQA')[1][1:-1]
                    prog.append(f"ANSWER{n_answer_vars}=VQA(image=IMAGE{n_image_vars - 1},question='{question}')")
                    n_answer_vars += 1
                else:
                    question = instruction.split('VQA')[1][1:-1]
                    prog.append(f"ANSWER{n_answer_vars}=VQA(image={image_var_name},question='{question}')")
                    n_answer_vars += 1
            elif 'LEFT' in instruction:
                prog.append(f"IMAGE{n_image_vars}=CROP_LEFTOF(image={image_var_name},box=BOX{n_box_vars - 1})")
                n_image_vars += 1
                is_cropped = True
            elif 'RIGHT' in instruction:
                prog.append(f"IMAGE{n_image_vars}=CROP_RIGHTOF(image={image_var_name},box=BOX{n_box_vars - 1})")
                n_image_vars += 1
                is_cropped = True
            elif 'ABOVE' in instruction or 'TOP' in instruction.split('_'):
                prog.append(f"IMAGE{n_image_vars}=CROP_ABOVE(image={image_var_name},box=BOX{n_box_vars - 1})")
                n_image_vars += 1
                is_cropped = True
            elif 'BELOW' in instruction or 'BOTTOM' in instruction.split('_'):
                prog.append(f"IMAGE{n_image_vars}=CROP_BELOW(image={image_var_name},box=BOX{n_box_vars - 1})")
                n_image_vars += 1
                is_cropped = True
            elif 'BEHIND' in instruction:
                prog.append(f"IMAGE{n_image_vars}=CROP_BEHIND(image={image_var_name},box=BOX{n_box_vars - 1})")
                n_image_vars += 1
                is_cropped = True
            elif 'ASSIGN' in instruction:
                var_name = prog[-1].split('=')[0]
                output_var_name = instruction.split('(')[1].split(')')[0]
                prog.append(f"{output_var_name}=ASSIGN(var={var_name})")
            elif 'EVAL' in instruction:
                expression = instruction.split('(')[1].split(')')[0]
                prog.append(f"ANSWER{n_answer_vars}=EVAL(expr=\"{expression}\")")
                n_answer_vars += 1
            elif 'COUNT' in instruction:
                prog.append(f"ANSWER{n_answer_vars}=COUNT(box=BOX{n_box_vars - 1})")
                n_answer_vars += 1
            else:
                prog.append(f"IMAGE{n_image_vars}=CROP(image={image_var_name},box=BOX{n_box_vars - 1})")
                n_image_vars += 1
                is_cropped = True
            is_first_instruction = False
    return '\n'.join(prog)
