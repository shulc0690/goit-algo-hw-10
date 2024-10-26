## Висновки

1. **Метод Монте-Карло**:
   - Значення інтеграла: приблизно 2.6667 (залежить від кількості точок N; чим більше N, тим точніший результат).
   - **Переваги**: простий у реалізації, може бути застосований для багатовимірних інтегралів.
   - **Недоліки**: потребує великої кількості випадкових точок для високої точності.

2. **Аналітичний метод**:
   - Значення інтеграла: точно 2.6667.
   - **Переваги**: точний, швидкий.
   - **Недоліки**: не завжди можливий для складних функцій.

3. **Функція `quad`**:
   - Значення інтеграла: точно 2.6667.
   - **Переваги**: точний, зручний для чисельного інтегрування.
   - **Недоліки**: може бути складний для багатовимірних інтегралів.

Метод Монте-Карло підтверджує свою точність, проте для високої точності краще використовувати аналітичні методи або чисельні методи, такі як `quad`.
