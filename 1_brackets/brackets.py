# function for correct '()' brackets count
def brackets_sequence_counter(n: int):
    open_bracket_list = ['(' for bracket in range(n)]
    close_bracket_list = [')' for bracket in range(n)]
    brackets_list = open_bracket_list + close_bracket_list
    print(brackets_list)
    # list of correct bracket sequence
    correct_sequences = 1

    while True:
        # variable, which control that all '(' must be closed
        # it can be possible if this variable < 0
        close_bracket_controller = 0

        brackets_quantity = len(brackets_list)

        # index of bracket in a list
        bracket_index = brackets_quantity - 1

        # loop for detecting and replacing '('
        while bracket_index >= 0:
            if brackets_list[bracket_index] == ')':
                close_bracket_controller -= 1
            if brackets_list[bracket_index] == '(':
                close_bracket_controller += 1
            if close_bracket_controller < 0 and brackets_list[bracket_index] == '(':
                break
            bracket_index -= 1
        if bracket_index < 0:
            break

        # here is replacing of '('
        brackets_list[bracket_index] = ')'

        for i in range(bracket_index+1, brackets_quantity):
            # Lexicographic order: ( is smaller than  )
            # here we replace to the minimal
            if i <= (brackets_quantity - bracket_index + close_bracket_controller)/2 + bracket_index:
                brackets_list[i] = '('
            else:
                brackets_list[i] = ')'

        # incrementing of correct sequences
        correct_sequences += 1
    print(correct_sequences)


integer = int(input())
brackets_sequence_counter(integer)


