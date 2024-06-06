
class AnalizadorLexico:
    class TOKEN:
        PROGRAM = "PROGRAM"
        IDENTIFIER = "IDENTIFIER"
        SEMICOLON = "SEMICOLON"
        DOT = "DOT"
        COLON = "COLON"
        COMMA = "COMMA"
        EQUALS = "EQUALS"
        INTEGER_CONST = "INTEGER_CONST"
        REAL_CONST = "REAL_CONST"
        STRING = "STRING"
        LEFT_PAREN = "LEFT_PAREN"
        RIGHT_PAREN = "RIGHT_PAREN"
        PLUS = "PLUS"
        MINUS = "MINUS"
        MULTIPLY = "MULTIPLY"
        DIVIDE = "DIVIDE"
        ASSIGN = "ASSIGN"
        LESS_THAN = "LESS_THAN"
        LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"
        GREATER_THAN = "GREATER_THAN"
        GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
        NOT_EQUAL = "NOT_EQUAL"
        AND = "AND"
        OR = "OR"
        NOT = "NOT"
        IF = "IF"
        THEN = "THEN"
        ELSE = "ELSE"
        WHILE = "WHILE"
        DO = "DO"
        BEGIN = "BEGIN"
        END = "END"
        READLN = "READLN"
        WRITE = "WRITE"
        EOF = "EOF"
        

    def __init__(self, entrada):
        self.entrada = entrada
        self.posicion = -1

    def obtener_siguiente_token(self):
        if self.posicion == len(self.entrada) - 1:
            return self.TOKEN.EOF
        while True:
            self.posicion += 1
            if self.posicion >= len(self.entrada):
                return self.TOKEN.EOF

            car = self.entrada[self.posicion]

            if car == ' ':
                continue
            elif car == ';':
                return self.TOKEN.SEMICOLON
            elif car == '.':
                return self.TOKEN.DOT
            elif car == ':':
                return self.TOKEN.COLON
            elif car == ',':
                return self.TOKEN.COMMA
            elif car == '=':
                return self.TOKEN.EQUALS
            elif car == '(':
                return self.TOKEN.LEFT_PAREN
            elif car == ')':
                return self.TOKEN.RIGHT_PAREN
            elif car == '+':
                return self.TOKEN.PLUS
            elif car == '-':
                return self.TOKEN.MINUS
            elif car == '*':
                return self.TOKEN.MULTIPLY
            elif car == '/':
                return self.TOKEN.DIVIDE
            elif car == '<':
                if self.posicion < len(self.entrada) - 1 and self.entrada[self.posicion + 1] == '=':
                    self.posicion += 1
                    return self.TOKEN.LESS_THAN_OR_EQUAL
                else:
                    return self.TOKEN.LESS_THAN
            elif car == '>':
                if self.posicion < len(self.entrada) - 1 and self.entrada[self.posicion + 1] == '=':
                    self.posicion += 1
                    return self.TOKEN.GREATER_THAN_OR_EQUAL
                else:
                    return self.TOKEN.GREATER_THAN
            elif car == '<':
                if self.posicion < len(self.entrada) - 1 and self.entrada[self.posicion + 1] == '>':
                    self.posicion += 1
                    return self.TOKEN.NOT_EQUAL
                else:
                    return self.TOKEN.LESS_THAN
            elif car == '&':
                return self.TOKEN.AND
            elif car == '|':
                return self.TOKEN.OR
            elif car == 'n':
                if self.posicion < len(self.entrada) - 2 and self.entrada[self.posicion + 1] == 'o' and \
                        self.entrada[self.posicion + 2] == 't':
                    self.posicion += 2
                    return self.TOKEN.NOT
                else:
                    return self.TOKEN.IDENTIFIER
            elif car.isdigit():
                const = car
                while self.posicion + 1 < len(self.entrada) and self.entrada[self.posicion + 1].isdigit():
                    self.posicion += 1
                    const += self.entrada[self.posicion]
                if self.posicion + 1 < len(self.entrada) and self.entrada[self.posicion + 1] == '.':
                    self.posicion += 1
                    const += self.entrada[self.posicion]
                    while self.posicion + 1 < len(self.entrada) and self.entrada[self.posicion + 1].isdigit():
                        self.posicion += 1
                        const += self.entrada[self.posicion]
                    return self.TOKEN.REAL_CONST
                return self.TOKEN.INTEGER_CONST
            elif car == '\'':
                string = ''
                while self.posicion + 1 < len(self.entrada) and self.entrada[self.posicion + 1] != '\'':
                    self.posicion += 1
                    string += self.entrada[self.posicion]
                if self.posicion + 1 < len(self.entrada):
                    self.posicion += 1  # Moverse al último '
                    return self.TOKEN.STRING
                else:
                    return self.TOKEN.EOF
            elif car.isalpha():
                identifier = car
                while self.posicion + 1 < len(self.entrada) and (self.entrada[self.posicion + 1].isalpha() or
                                                                 self.entrada[self.posicion + 1].isdigit()):
                    self.posicion += 1
                    identifier += self.entrada[self.posicion]
                if identifier == 'PROGRAM':
                    return self.TOKEN.PROGRAM
                elif identifier == 'IF':
                    return self.TOKEN.IF
                elif identifier == 'THEN':
                    return self.TOKEN.THEN
                elif identifier == 'ELSE':
                    return self.TOKEN.ELSE
                elif identifier == 'WHILE':
                    return self.TOKEN.WHILE
                elif identifier == 'DO':
                    return self.TOKEN.DO
                elif identifier == 'BEGIN':
                    return self.TOKEN.BEGIN
                elif identifier == 'END':
                    return self.TOKEN.END
                elif identifier == 'READLN':
                    return self.TOKEN.READLN
                elif identifier == 'WRITE':
                    return self.TOKEN.WRITE
                else:
                    return self.TOKEN.IDENTIFIER
            else:
                return self.TOKEN.EOF

    def reiniciar_posicion(self):
        self.posicion = -1
