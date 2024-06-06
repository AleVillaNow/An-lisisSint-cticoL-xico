import tkinter as tk
from tkinter import filedialog, messagebox

class AnalizadorLexico:
     # Se definen los tokens como atributos de clase para representar los distintos tipos de elementos del lenguaje.
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
        VAR = "VAR" # Añadido el token VAR
        EOF = "EOF"

    def __init__(self, entrada):
        # Se inicializan los atributos de la clase AnalizadorLexico.
        self.entrada = entrada
        self.posicion = -1

    def obtener_siguiente_token(self):
        # Este método analiza la entrada carácter por carácter y devuelve el siguiente token encontrado.
        if self.posicion == len(self.entrada) - 1:
            return self.TOKEN.EOF
        while True:
            self.posicion += 1
            if self.posicion >= len(self.entrada):
                return self.TOKEN.EOF

            car = self.entrada[self.posicion]

            if car == ' ' or car =='\n':
                continue
            elif car == ';':
                return self.TOKEN.SEMICOLON
            elif car == '.':
                return self.TOKEN.DOT
            elif car == ':':
                if self.posicion < len(self.entrada) - 1 and self.entrada[self.posicion + 1] == '=':
                    self.posicion += 1
                    return self.TOKEN.EQUALS
                else:
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
                while self.posicion + 1 < len(self.entrada) and (self.entrada[self.posicion + 1].isalpha() or self.entrada[self.posicion + 1].isdigit()):
                    self.posicion += 1
                    identifier += self.entrada[self.posicion]
                if identifier == 'WRITELN':
                    return self.TOKEN.WRITE
                elif identifier == 'PROGRAM':
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
                elif identifier == 'VAR':
                    return self.TOKEN.VAR
                else:
                    return self.TOKEN.IDENTIFIER
            else:
                return self.TOKEN.EOF

    def reiniciar_posicion(self):
        self.posicion = -1

class AnalizadorSintactico:
    # Se inicializan los atributos de la clase AnalizadorSintactico
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_actual = None
        self.posicion_actual = -1
        self.avanzar()

    def avanzar(self):
        # Este método avanza al siguiente token en la secuencia de tokens
        self.posicion_actual += 1
        if self.posicion_actual < len(self.tokens):
            self.token_actual = self.tokens[self.posicion_actual]
        else:
            self.token_actual = None

    def emparejar(self, tipo_esperado):
         # Este método compara el tipo del token actual con el tipo esperado y avanza si son iguales.
        if self.token_actual == tipo_esperado:
            self.avanzar()
        else:
            raise SyntaxError(f"Error sintáctico: se esperaba {tipo_esperado} pero se encontró {self.token_actual}")

    def analizar(self):
     # Este método inicia el análisis sintáctico llamando al método programa() y verifica si hay tokens inesperados.
        self.programa()
        if self.token_actual is not None:
            raise SyntaxError(f"Error sintáctico: token inesperado '{self.token_actual}'")
        print("Entrada válida.")

    def programa(self):
        # Este método representa la regla de la gramática para un programa.
        self.emparejar(AnalizadorLexico.TOKEN.PROGRAM)
        self.emparejar(AnalizadorLexico.TOKEN.IDENTIFIER)
        self.emparejar(AnalizadorLexico.TOKEN.SEMICOLON)
        self.bloque()
        self.emparejar(AnalizadorLexico.TOKEN.DOT)

    def bloque(self):
         # Este método representa la regla de la gramática para un bloque de código.
        self.declaracion_parte()
        self.sentencia_parte()

    def declaracion_parte(self):
        # Este método representa la regla de la gramática para la parte de declaración de variables.
        if self.token_actual == AnalizadorLexico.TOKEN.VAR:
            self.emparejar(AnalizadorLexico.TOKEN.VAR)
            self.declaracion_variable()
            while self.token_actual == AnalizadorLexico.TOKEN.IDENTIFIER:
                self.declaracion_variable()
            self.emparejar(AnalizadorLexico.TOKEN.SEMICOLON)

    def declaracion_variable(self):
        # Este método representa la regla de la gramática para la declaración de una variable.
        self.emparejar(AnalizadorLexico.TOKEN.IDENTIFIER)
        while self.token_actual == AnalizadorLexico.TOKEN.COMMA:
            self.emparejar(AnalizadorLexico.TOKEN.COMMA)
            self.emparejar(AnalizadorLexico.TOKEN.IDENTIFIER)
        self.emparejar(AnalizadorLexico.TOKEN.COLON)

    def sentencia_parte(self):
        # Este método representa la regla de la gramática para la parte de sentencias.
        self.sentencia_compuesta()

    def sentencia_compuesta(self):
        # Este método representa la regla de la gramática para una sentencia compuesta.
        self.emparejar(AnalizadorLexico.TOKEN.BEGIN)
        self.sentencia()
        while self.token_actual == AnalizadorLexico.TOKEN.SEMICOLON:
            self.emparejar(AnalizadorLexico.TOKEN.SEMICOLON)
            self.sentencia()
        self.emparejar(AnalizadorLexico.TOKEN.END)

    def sentencia(self):
        # Este método representa la regla de la gramática para una sentencia.
        if self.token_actual == AnalizadorLexico.TOKEN.IDENTIFIER:
            self.emparejar(AnalizadorLexico.TOKEN.IDENTIFIER)
            self.emparejar(AnalizadorLexico.TOKEN.ASSIGN)
            self.expresion()
        elif self.token_actual == AnalizadorLexico.TOKEN.BEGIN:
            self.sentencia_compuesta()
        elif self.token_actual == AnalizadorLexico.TOKEN.IF:
            self.sentencia_condicional()

    def sentencia_condicional(self):
        # Este método representa la regla de la gramática para una sentencia condicional.
        self.emparejar(AnalizadorLexico.TOKEN.IF)
        self.expresion()
        self.emparejar(AnalizadorLexico.TOKEN.THEN)
        self.sentencia()
        if self.token_actual == AnalizadorLexico.TOKEN.ELSE:
            self.emparejar(AnalizadorLexico.TOKEN.ELSE)
            self.sentencia()

    def expresion(self):
         # Este método representa la regla de la gramática para una expresión.
        self.term()
        while self.token_actual in {AnalizadorLexico.TOKEN.PLUS, AnalizadorLexico.TOKEN.MINUS}:
            self.emparejar(self.token_actual)
            self.term()

    def term(self):
         # Este método representa la regla de la gramática para un término
        self.factor()
        while self.token_actual in {AnalizadorLexico.TOKEN.MULTIPLY, AnalizadorLexico.TOKEN.DIVIDE}:
            self.emparejar(self.token_actual)
            self.factor()

    def factor(self):
        # Este método representa la regla de la gramática para un factor
        if self.token_actual == AnalizadorLexico.TOKEN.IDENTIFIER:
            self.emparejar(AnalizadorLexico.TOKEN.IDENTIFIER)
        elif self.token_actual in {AnalizadorLexico.TOKEN.INTEGER_CONST, AnalizadorLexico.TOKEN.REAL_CONST}:
            self.emparejar(self.token_actual)
        elif self.token_actual == AnalizadorLexico.TOKEN.LEFT_PAREN:
            self.emparejar(AnalizadorLexico.TOKEN.LEFT_PAREN)
            self.expresion()
            self.emparejar(AnalizadorLexico.TOKEN.RIGHT_PAREN)
        else:
            raise SyntaxError("Error sintáctico: factor inesperado.")

def abrir_archivo():
    # Este método se ejecuta cuando se hace clic en el botón "Abrir Archivo" y abre un cuadro de diálogo para seleccionar un archivo.
    filepath = filedialog.askopenfilename()
    if not filepath:
        return

    try:
        with open(filepath, 'r') as file:
            contenido = file.read()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo: {str(e)}")
        return

    tokens = analizar_contenido(contenido)
    analizar_sintaxis(tokens)

def analizar_contenido(contenido):
    # Este método toma el contenido del archivo abierto, lo convierte en una lista de caracteres y pasa esta lista al analizador léxico.
    entrada = list(contenido)
    analizador = AnalizadorLexico(entrada)
    tokens = []

    while True:
        token = analizador.obtener_siguiente_token()
        if token == AnalizadorLexico.TOKEN.EOF:
            break
        tokens.append(token)

    return tokens

def analizar_sintaxis(tokens):
    # Este método llama al analizador sintáctico con los tokens obtenidos del analizador léxico y maneja los errores sintácticos.
    try:
        print("Tokens encontrados:", tokens)  # Agregar esta línea para imprimir los tokens
        analizador_sintactico = AnalizadorSintactico(tokens)
        analizador_sintactico.analizar()
        print("Análisis sintáctico sin errores.")
        mostrar_exito()  # Mostrar mensaje de éxito después de un análisis exitoso
        actualizar_resultado(tokens)  # Mostrar los tokens encontrados en la interfaz
    except SyntaxError as e:
        print("Error en el análisis sintáctico:", str(e))
        messagebox.showerror("Error", str(e))

def actualizar_resultado(tokens):
    # Este método actualiza el contenido del recuadro de resultados con los tokens encontrados.
    resultado_text.delete(1.0, tk.END)  # Limpiar el contenido actual
    resultado_text.insert(tk.END, "Tokens encontrados:\n")
    for token in tokens:
        resultado_text.insert(tk.END, f"{token}\n")  # Mostrar cada token en una nueva línea



def mostrar_exito():
    # Este método muestra un mensaje de éxito cuando el análisis sintáctico se completa sin errores.
    messagebox.showinfo("Análisis Sintáctico", "El análisis sintáctico fue exitoso.")

        
# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Analizador Sintáctico")

# Crear un Frame para contener el botón y el recuadro de resultados
frame_contenedor = tk.Frame(ventana)
frame_contenedor.pack(padx=10, pady=10)

# Botón para abrir el archivo
boton_abrir = tk.Button(frame_contenedor, text="Abrir Archivo", command=abrir_archivo)
boton_abrir.pack(side=tk.LEFT)

# Crear un Frame para mostrar los tokens encontrados
frame_tokens = tk.Frame(ventana)
frame_tokens.pack(padx=10, pady=10)

# Recuadro para mostrar los tokens
resultado_text = tk.Text(frame_tokens, wrap=tk.WORD, width=50, height=15)
resultado_text.pack(pady=10)

ventana.mainloop()



