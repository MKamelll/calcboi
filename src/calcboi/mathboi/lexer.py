from enum import Enum


class TokenType(Enum):
    PLUS = "PLUS"
    PLUS_PLUS = "PLUS_PLUS"
    MINUS_MINUS = "MINUS_MINUS"
    PLUS_EQUAL = "PLUS_EQUAL"
    MINUS_EQUAL = "MINUS_EQUAL"
    MINUS = "MINUS"
    STAR = "STAR"
    STAR_EQUAL = "STAR_EQUAL"
    SLASH = "SLASH"
    SLASH_EQUAL = "SLASH_EQUAL"
    EQUAL = "EQUAL"
    EQUAL_EQUAL = "EQUAL_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN_EQUAL = "GREATER_THAN_EQUAL"
    LESS_THAN_EQUAL = "LESS_THAN_EQUAL"
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"
    CONST = "CONST"
    LET = "LET"
    FUNCTION = "FUNCTION"
    LEFT_BRACKET = "LEFT_BRACKET"
    RIGHT_BRACKET = "RIGHT_BRACKET"
    LEFT_BRACE = "LEFT_BRACE"
    RIGHT_BRACE = "RIGHT_BRACE"
    RETURN = "RETURN"
    IDENTIFIER = "IDENTIFIER"
    INT = "INT"
    STRING = "STRING"
    FLOAT = "FLOAT"
    UNKNOWN_TOKEN = "UNKNOWN_TOKEN"
    EOF = "EOF"


class Token:
    def __init__(self, token_type: TokenType, lexeme: str):
        self.token_type = token_type
        self.lexeme = lexeme

    def __repr__(self) -> str:
        return f"Token(type: {self.token_type}, lexeme: {self.lexeme})"


class Lexer:
    def __init__(self, src: str):
        self.src = src
        self.curr = 0

    def advance(self):
        self.curr += 1

    def curr_char(self) -> str:
        return self.src[self.curr]

    def is_at_end(self) -> bool:
        return self.curr >= len(self.src)

    def next(self) -> Token:
        if self.is_at_end():
            return Token(TokenType.EOF, "EOF")
        match self.curr_char():
            case "+":
                self.advance()
                if self.curr_char() == "+":
                    self.advance()
                    return Token(TokenType.PLUS_PLUS, "++")
                elif self.curr_char() == "=":
                    self.advance()
                    return Token(TokenType.PLUS_EQUAL, "+=")
                return Token(TokenType.PLUS, "+")
            case "-":
                self.advance()
                if self.curr_char() == "-":
                    self.advance()
                    return Token(TokenType.MINUS_MINUS, "--")
                elif self.curr_char() == "=":
                    self.advance()
                    return Token(TokenType.MINUS_EQUAL, "-=")
                return Token(TokenType.MINUS, "-")
            case "*":
                self.advance()
                if self.curr_char() == "=":
                    self.advance()
                    return Token(TokenType.STAR_EQUAL, "*=")
                return Token(TokenType.STAR, "*")
            case "/":
                self.advance()
                if self.curr_char() == "=":
                    self.advance()
                    return Token(TokenType.SLASH_EQUAL, "/=")
                return Token(TokenType.SLASH, "/")
            case "=":
                self.advance()
                if self.curr_char() == "=":
                    self.advance()
                    return Token(TokenType.EQUAL_EQUAL, "==")
                return Token(TokenType.EQUAL, "=")
            case ">":
                self.advance()
                if self.curr_char() == "=":
                    self.advance()
                    return Token(TokenType.GREATER_THAN_EQUAL, ">=")
                return Token(TokenType.GREATER_THAN, ">")
            case "<":
                self.advance()
                if self.advance() == "=":
                    self.advance()
                    return Token(TokenType.LESS_THAN_EQUAL, "<=")
                return Token(TokenType.LESS_THAN, "<")
            case "(":
                self.advance()
                return Token(TokenType.LEFT_PAREN, "(")
            case ")":
                self.advance()
                return Token(TokenType.RIGHT_PAREN, ")")
            case "{":
                self.advance()
                return Token(TokenType.LEFT_BRACKET, "{")
            case "}":
                self.advance()
                return Token(TokenType.RIGHT_BRACKET, "}")
            case "[":
                self.advance()
                return Token(TokenType.LEFT_BRACE, "[")
            case "]":
                self.advance()
                return Token(TokenType.RIGHT_BRACE, "]")
            case '"':
                result = self.parse_string()
                return Token(TokenType.STRING, result)
            case " ":
                self.advance()
                return self.next()
            case _:
                lex = self.curr_char()
                self.advance()
                return Token(TokenType.UNKNOWN_TOKEN, lex)

    def parse_string(self) -> str:
        self.advance()
        result = ""
        while not self.is_at_end():
            if self.curr_char() == '"':
                self.advance()
                break
            result += self.curr_char()
            self.advance()
        return result


lexer = Lexer('+ - / * += *= /= 25 2.5 "test test" () {} []')
while True:
    token = lexer.next()
    if token.token_type == TokenType.EOF:
        break
    print(token)
