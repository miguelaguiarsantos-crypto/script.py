print("=== Sistema de Notas Acadêmicas ===")
nota1 = 8.0
nota2 = 6.0
print(f"Primeira Nota cadastrada: {nota1}")
print(f"Segunda Nota cadastrada: {nota2}")
media = (nota1 + nota2) / 2
print(f"\nMédia Final calculada: {media:.1f}")
if media >= 7.0:
    print("Status: Aluno Aprovado! 🎉")
else:
    print("Status: Aluno em Recuperação/Reprovado. ⚠️")
