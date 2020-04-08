package tokenizer

// TokenType type
type TokenType int

// Token types
const (
	// Single Character Tokens
	LEFTPAREN TokenType = iota + 1
	RIGHTPAREN
	LEFTBRACE
	RIGHTBRACE
	COMMA
	DOT
	MINUS
	PLUS
	SEMICOLON
	SLASH
	STAR

	// One or two character tokens
	BANG
	BANGEQUAL
	EQUAL
	EQUALEQUAL
	GREATER
	GREATEREQUAL
	LESS
	LESSEQUAL

	// Literals
	IDENTIFIER
	STRING
	NUMBER

	// Keywords
	AND
	CLASS
	ELSE
	FALSE
	FUN
	FOR
	IF
	NIL
	OR
	PRINT
	RETURN
	SUPER
	THIS
	TRUE
	VAR
	WHILE

	// End of File
	EOF
)
