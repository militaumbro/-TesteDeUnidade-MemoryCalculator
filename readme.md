# Teste de Unidade: MemoryCalculator
Prof. Andre Hora

Objetivo: Exercitar testes de unidade. Iremos utilizar o framework de teste [unittest](https://docs.python.org/3/library/unittest.html).

Explore a classe `MemoryCalculator` em `calculator.py`. 
Veja que ela é muito simples: apenas soma os números passados para o método `add` e retorna o valor da soma através do método `sum`.
Veja um exemplo de uso abaixo:

```python
calculator = MemoryCalculator()
calculator.add(5)
calculator.add(5)
print(calculator.sum()) # resultado: 10
print(calculator.sum()) # resultado: 0

calculator.add(5)
print(calculator.sum()) # resultado: 5
```

- Quando o método `sum` é chamado, o valor em memória da soma é zerado. Por isso a última soma acima é 5 (e não 15).

- Se `save_last_sum` é True, o valor da última soma é armazenado em `last_sum`.

O arquivo `test_calculator.py` contém os testes de unidade.
Para executar os testes, clique no botão **run**.
Note que apenas o método de teste `test_sum_is_zero_on_initialization` foi implementado.

Implemente os 4 métodos de testes faltantes em `test_calculator.py`:

- test_sum_one_number
- test_sum_two_numbers
- test_sum_is_zero_after_calling_sum
- test_sum_numbers_and_save_last_sum