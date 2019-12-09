from transitions import Machine


class func:
    name: str
    arg: str


class func_n(func):
    def __init__(self, name, arg):
        self.name = name
        self.arg = arg


class func_n_shift(func):
    def __init__(self, name, arg):
        self.name = name
        self.arg = arg
        self.sign = arg[1]
        self.shift = int(arg[2])


class func_num(func):
    def __init__(self, name, arg):
        self.name = name
        self.arg = int(arg)


class op:
    priority_dict = {"*": 1, "/": 1, "·": 1, ":": 1, "×": 1,
                     "+": 2, "-": 2, "−": 2}

    def __init__(self, symbol):
        self.symbol = symbol
        self.priority = self.priority_dict[symbol]


class n_comp:
    def __init__(self, arg):
        self.sign = arg[1]
        self.comp = int(arg[2])


class n_shift:
    def __init__(self, arg):
        self.sign = arg[1]
        self.shift = int(arg[2])


class brackets_n:
    def __init__(self, arg):
        self.op = arg[2]
        self.shift = int(arg[3])


class equation:
    pass


class cond:
    pass


class num:
    def __init__(self, arg):
        self.num = int(arg)


class word_machine:
    _states = ["empty", "f", "f0", "f00", "f01", "f000", "f010", "f011", "f0110", "f01100",
               "op0", "eq0", "c0", "c00", "c000", "num0",
               "n0", "n00", "n000", "n01", "n010",
               "b0", "b00", "b000", "b0000", "b00000"]

    def __init__(self):
        self.machine = Machine(model=self, states=word_machine._states, initial="empty")
        self.cur_symbol: str = ""
        self.cur_string: str = ""
        self._create_casual_transitions()
        self.classes = []

    def _start_again(self):
        self.cur_symbol = ""
        self.cur_string = ""
        self.machine.set_state("empty")

    def on_enter_f000(self):
        f = func_num(self.cur_string[0], self.cur_string[2])
        self.classes.append(f)
        self._start_again()

    def on_enter_f010(self):
        f = func_n(self.cur_string[0], self.cur_string[2])
        self.classes.append(f)
        self._start_again()

    def on_enter_f01100(self):
        f = func_n_shift(self.cur_string[0], self.cur_string[2:-1])
        self.classes.append(f)
        self._start_again()

    def on_enter_op0(self):
        self.classes.append(op(self.cur_string))
        self._start_again()

    def on_enter_eq0(self):
        self.classes.append(equation())
        self._start_again()

    def on_enter_c000(self):
        self.classes.append(cond())
        self._start_again()

    def on_enter_num0(self):
        self.classes.append(num(self.cur_string))
        self._start_again()

    def on_enter_n000(self):
        self.classes.append(n_shift(self.cur_string))
        self._start_again()

    def on_enter_n010(self):
        self.classes.append(n_comp(self.cur_string))
        self._start_again()

    def on_enter_b00000(self):
        self.classes.append((brackets_n(self.cur_string)))
        self._start_again()

    def is_f(self):
        return self.cur_symbol == "f" or self.cur_symbol == "g"

    def is_open_bracket(self):
        return self.cur_symbol == "("

    def is_num(self):
        return self.cur_symbol.isdigit()

    def is_close_bracket(self):
        return self.cur_symbol == ")"

    def is_n(self):
        return self.cur_symbol == "n"

    def is_op(self):
        ops = "+−*/·-×"
        return self.cur_symbol in ops

    def is_eq(self):
        return self.cur_symbol == "="

    def is_c0(self):
        return self.cur_symbol == "п"

    def is_c00(self):
        return self.cur_symbol == "р"

    def is_c000(self):
        return self.cur_symbol == "и"

    def is_comp(self):
        comparisions = "><=≥≤"
        return self.cur_symbol in comparisions

    def _create_casual_transitions(self):
        self.machine.add_transition("move", "empty", "f", conditions="is_f")
        self.machine.add_transition("move", "f", "f0", conditions="is_open_bracket")
        self.machine.add_transition("move", "f0", "f00", conditions="is_num")
        self.machine.add_transition("move", "f00", "f000", conditions="is_close_bracket")
        self.machine.add_transition("move", "f0", "f01", conditions="is_n")
        self.machine.add_transition("move", "f01", "f010", conditions="is_close_bracket")
        self.machine.add_transition("move", "f01", "f011", conditions="is_op")
        self.machine.add_transition("move", "f011", "f0110", conditions="is_num")
        self.machine.add_transition("move", "f0110", "f01100", conditions="is_close_bracket")
        self.machine.add_transition("move", "empty", "op0", conditions="is_op")
        self.machine.add_transition("move", "empty", "eq0", conditions="is_eq")
        self.machine.add_transition("move", "empty", "c0", conditions="is_c0")
        self.machine.add_transition("move", "c0", "c00", conditions="is_c00")
        self.machine.add_transition("move", "c00", "c000", conditions="is_c000")
        self.machine.add_transition("move", "empty", "num0", conditions="is_num")
        self.machine.add_transition("move", "empty", "n0", conditions="is_n")
        self.machine.add_transition("move", "n0", "n00", conditions="is_op")
        self.machine.add_transition("move", "n00", "n000", conditions="is_num")
        self.machine.add_transition("move", "n0", "n01", conditions="is_comp")
        self.machine.add_transition("move", "n01", "n010", conditions="is_num")
        self.machine.add_transition("move", "empty", "b0", conditions="is_open_bracket")
        self.machine.add_transition("move", "b0", "b00", conditions="is_n")
        self.machine.add_transition("move", "b00", "b000", conditions="is_op")
        self.machine.add_transition("move", "b000", "b0000", conditions="is_num")
        self.machine.add_transition("move", "b0000", "b00000", conditions="is_close_bracket")

    def break_to_classes(self, lines):
        for line in lines:
            for i in line.lower():
                if i != " " and i != "," and i != ";" and i != ".":
                    self.cur_symbol = i
                    self.cur_string += i
                    self.move()
        return self.classes


class expressions_machine:
    _states = ["entry", "func", "procedure_start", "procedure_continue", "procedure_end",
               "condition_start", "condition_end"]

    def __init__(self):
        self.machine = Machine(model=self, states=expressions_machine._states, initial="entry")
        self.cur_class = None
        self.cur_expression = []
        self._create_casual_transitions()
        self.expressions = []

    def is_f(self):
        return type(self.cur_class) == func_n or type(self.cur_class) == func_num

    def is_eq(self):
        return type(self.cur_class) == equation

    def is_expr_element(self):
        return (type(self.cur_class) == func_n_shift or type(self.cur_class) == num or
                type(self.cur_class) == n_shift or type(self.cur_class) == brackets_n)

    def is_op(self):
        return type(self.cur_class) == op

    def is_cond(self):
        return type(self.cur_class) == cond

    def is_n_comp(self):
        return type(self.cur_class) == n_comp

    def on_enter_procedure_end(self):
        self.expressions.append(self.cur_expression[:-1])
        self.cur_expression = [self.cur_class]
        self.machine.set_state("entry")

    def on_enter_condition_end(self):
        self.expressions.append(self.cur_expression)
        self.cur_expression = []
        self.machine.set_state("entry")

    def _create_casual_transitions(self):
        self.machine.add_transition("move", "entry", "func", conditions="is_f")
        self.machine.add_transition("move", "func", "procedure_start", conditions="is_eq")
        self.machine.add_transition("move", "procedure_start", "procedure_continue", conditions="is_expr_element")
        self.machine.add_transition("move", "procedure_continue", "procedure_start", conditions="is_op")
        self.machine.add_transition("move", "procedure_continue", "procedure_end", conditions="is_f")
        self.machine.add_transition("move", "procedure_continue", "condition_start", conditions="is_cond")
        self.machine.add_transition("move", "condition_start", "condition_end", conditions="is_n_comp")

    def break_to_expressions(self, classes):
        for _class in classes:
            self.cur_class = _class
            self.cur_expression.append(_class)
            self.move()
        return self.expressions


wm = word_machine()
print(wm.break_to_classes(["F(1) = 1; F(2) = 1;", "F(n) = F(n - 2) * (n - 1), при n > 2."]))
em = expressions_machine()
print(em.break_to_expressions(wm.break_to_classes(["F(1) = 1; F(2) = 1;", "F(n) = F(n - 2) * (n - 1), при n > 2."])))
