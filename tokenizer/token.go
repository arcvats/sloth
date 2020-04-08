package tokenizer

import "fmt"

// Token struct
type Token struct {
	typeOfToken TokenType
	lexeme      string
	literal     string
	line        int
}

// NewToken creates new token
func NewToken(typeOfToken TokenType, lexeme string, literal string, line int) *Token {
	token := Token{typeOfToken: typeOfToken, lexeme: lexeme, literal: literal, line: line}
	return &token
}

// ToString string representation of token
func (t *Token) ToString() string {
	return fmt.Sprintf("%d %s %s", t.typeOfToken, t.lexeme, t.literal)
}
