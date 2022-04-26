# Тестовая документация для проверки расчета сервиса по выдаче кредитов
 + [Замечания к документации/заданию](#notes)
 + [Критерии приемки](#criteria)
 + [Чек-лист](#checklist)
 + [Тест-кейсы](#tests)

## <a name="notes"></a> Замечания к документации/заданию

- Единица измерения финансов. Предлагаю рассмотреть возможность замены миллионов на тысячи. Исходя
- Возраст. Несовершеннолетние тоже могут брать кредит? Рекомендую рассмотреть вопрос об ограничении возраста с 16 (18) до 99
- Доход и запрашиваемая сумма указана в миллионах. Рекомендую рассмотреть вопрос об измнении на тысячи. При тестировании буду исходить, что шаг 0.1
- Срок погашения указан в годах. Рекомендую рассмотреть возможность изменения на месяцы. При тестировании буду исходить из того, что кредит можно взять на опредленное количество полных лет
- Нет информации об изменении/сохранении модифкатора при цели "Автокредит"

## <a name="criteria"></a> Критерии приемки
- ### [01] Допустимые значения входных параметров
    - [01.1] Возраст [not negative int], лет
    - [01.2] Пол [F, M] [female,male]
    - [01.3] Источник дохода [пассивный доход, наёмный работник, собственный бизнес, безработный] [passive income, employee, own business, unemployed]
    - [01.4] Доход за последний год [int], млн
    - [01.5] Кредитный рейтинг [-2, -1, 0, 1, 2]
    - [01.6] Запрошенная сумма [0.1 .. 10], млн
    - [01.7] Срок погашения [1..20], лет
    - [01.8] Цель [ипотека, развитие бизнеса, автокредит, потребительский] [mortgage, business development, car loan, personal loan]
    
- ### [02]Условия выдачи кредита
    - [02.1] Если возраст превышает пенсионный возраст на момент возврата кредита, кредит не выдаётся
    - [02.2] Если результат деления запрошенной суммы на срок погашения в годах более трети годового дохода, кредит не выдаётся
    - [02.3] Если кредитный рейтинг -2, кредит не выдаётся
    - [02.4] Если в источнике дохода указано "безработный", кредит не выдаётся
    - [02.5] Если годовой платёж (включая проценты) больше половины дохода, кредит не выдаётся
    
- ### [03] Рассчет суммы кредита
    - [03.1] Если работают несколько условий по сумме кредита - выбирается наименьшая
    - [03.2] При пассивном доходе выдаётся кредит на сумму до 1 млн, наёмным работникам - до 5 млн, собственное дело - до 10 млн
    - [03.3] При кредитном рейтинге -1 выдаётся кредит на сумму до 1 млн, при 0 - до 5 млн, при 1 или 2 - до 10 млн
    
- ### [04]Условия изменения базовой ставки
  - [04.1] Все модификаторы процентной ставки суммируются, применяется итоговый модификатор
  - #### по параметру "Цель"
    - [04.2.1] ипотека (-2%)
    - [04.2.2] развития бизнеса (-0.5%)
    - [04.2.3] потребительский кредит (+1.5%)
    
  - #### по параметру "Кредитный рейтинг"
    - [04.3.1] +1.5% для кредитного рейтинга  -1
    - [04.3.2] 0% для кредитного рейтинга 0
    - [04.3.3] -0.25% для кредитного рейтинга 1
    - [04.3.4] -0.75% для кредитного рейтинга 2

  - #### по параметру "Источник дохода"
    - [04.4.1] Для пассивного дохода ставка повышается на 0.5%
    - [04.4.2] для наемных работников ставка снижается на 0.25% 
    - [04.4.3] с собственным бизнесом ставка повышается на 0.25%
    
  - #### по параметру "Запрашиваемая сумма"
    - [04.5.1] Модификатор в зависимости от запрошенной суммы рассчитывается по формуле `[-log(sum)]
    
- ### [05] Способ расчета годового платежа
    - [05.1] Базовая ставка - 10%
    
    - [05.2] Годовой платеж по кредиту определяется по следующей формуле:

`(<сумма кредита> * (1 + <срок погашения> * (<базовая ставка> + <модификаторы>))) / <срок погашения>`
- ### [06] Выходные данные
    - [06.1] Кредит выдаётся/не выдаётся
    - [06.2] Годовой платеж по кредиту
    
- ### Уточнения к критериям приемки
    - Проверяем именно бизнес-логику
    - Корректен ли расчет
    - Одобрен/ Не одобрен кредит
    - Не проводим специфичные для API тесты с изменением методов запроса, дублированием/отстутствием параметров итд

## <a name="checklist"></a> Чек-лист
- ### валидация по значениям входных параметров
    - [01.1] возраст [-20, -1, 0, 1, 40, 100]
    - [01.2] пол (невалидное значение)
    - [01.3] источник дохода (невалидное значение)
    - [01.4] Доход за последний год [-1, 0, 1, 0.3, 5.6, 9.9, 10, 11.1]
    - [01.5] Кредитный рейтинг 
    - [01.6] Запрошенная сумма [-0.5 -0.1, 0, 0.1, 1, 9.9 10, 10.1], млн
    - [01.7] Срок погашения [-1, 0, 1, 10, 19,20,21, 50], лет
    - [01.8] Цель [mortgage, business development, car loan, personal loan, party]
    
- ### валидация по условиям выдачи кредита
    - [02.1] Если возраст превышает пенсионный возраст на момент возврата кредита, кредит не выдаётся 
      [мужчина, возраст + срок погашения = 59,60,61, 64, 65, 66; женщина, возраст + срок погашения 50, 59, 60, 61, 70]
    - [02.2] Если результат деления запрошенной суммы на срок погашения в годах более трети годового дохода, кредит не выдаётся
      [(запрошенная сумма + срок) >,>=, < (доход/3)]
    - [02.3] Если кредитный рейтинг -2, кредит не выдаётся
    - [02.4] Если в источнике дохода указано "безработный", кредит не выдаётся
    - [02.5] Если годовой платёж (включая проценты) больше половины дохода, кредит не выдаётся
    
- ### проверка рассчета суммы кредита
    - [03.1] Если работают несколько условий по сумме кредита - выбирается наименьшая
    - [03.2] [пассивный доход, сумма - 0.1, 0.9 ,1, 1.1], [наемный работник, сумма - 0.8, 4.9,5, 5.1], 
    - [03.3] [рейтинг -1, сумма - 0.1, 0.9 ,1, 1.1], [рейтинг 0, сумма - 0.8, 4.9,5, 5.1], [рейтинг 1, рейтинг 2, сумма - 5.5, 9.9,10, 10.1],

- ### [04]Условия изменения базовой ставки
  - [04.1] Проверка, что все модификаторы суммируются
  - #### по параметру "Цель"
    - [04.2.1] ипотека (-2%)
    - [04.2.2] развития бизнеса (-0.5%)
    - [04.2.3] потребительский кредит (+1.5%)
    
  - #### по параметру "Кредитный рейтинг"
    - [04.3.1] +1.5% для кредитного рейтинга  -1
    - [04.3.2] 0% для кредитного рейтинга 0
    - [04.3.3] -0.25% для кредитного рейтинга 1
    - [04.3.4] -0.75% для кредитного рейтинга 2

  - #### по параметру "Источник дохода"
    - [04.4.1] Для пассивного дохода ставка повышается на 0.5%
    - [04.4.2] для наемных работников ставка снижается на 0.25% 
    - [04.4.3] с собственным бизнесом ставка повышается на 0.25%
    
  - #### по параметру "Запрашиваемая сумма"
    - [04.5.1] Модификатор в зависимости от запрошенной суммы рассчитывается по формуле `[-log(sum)]
    
- ### [05] Способ расчета годового платежа
    - [05.1] Узнать, где отображается в коде или в переменных окружения базовая ставка
    - [05.2] Проверить расчет по формуле:
`(<сумма кредита> * (1 + <срок погашения> * (<базовая ставка> + <модификаторы>))) / <срок погашения>`

## <a name="tests"></a> Тест-кейсы
- ### [TC01.1.1] Возраст - 40 лет, кредит одобрен
    - #### Шаги 
    1. Отправить запрос на получение информации о кредите, указав параметр возраст - 40
    - #### OP 
    - Кредит одобрен, информация о годовом платеже присутствует
    
- ### [TC01.1.2] Отрицательный возраст и возраст 0 
    - #### Шаги 
    1. Отправить запрос на получение информации о кредите, 
    - #### OP 
    - Узнать ожидаемый результат у аналитиков
    
- ### [TC01.1.3] Невалидное значение возраста  
    - #### Шаги 
    1. Отправить запрос на получение информации о кредите
    - #### OP 
    - Узнать ожидаемый результат у аналитиков
    
- ### [TC01.2.1] Пол - женский,мужской - кредит одобрен
    - #### Шаги 
    1. Отправить запрос на получение информации о кредите, указав женский пол
    - #### OP 
        Кредит одобрен, информация о годовом платеже присутствует
    2. Отправить запрос на получение информации о кредите, указав мужской пол
    - #### OP 
        Кредит одобрен, информация о годовом платеже присутствует
      
- ### [TC01.2.2] Пол - невалидный 
    - #### Шаги 
    1. Отправить запрос на получение информации о кредите, указав невалидный пол
    - #### OP 
        Узнать ожидаемый результат у аналитиков
      
- ### [TC01.3.1] Валидный источник дохода - кредит одобрен 
    - #### Шаги 
    1. Отправить запрос на получение информации о кредите, указав валидный источник дохода
    - #### OP 
        Кредит одобрен, информация о годовом платеже присутствует
    

- ### [TC02.1.1] Мужчина, Возраст + срок погашения не превышают пенсионный
    - #### Шаги
    1. Отправить запрос на получение информации о кредите, указав мужской пол, возраст + сумма погашения = 40
    #### OP 
        OP Кредит одобрен, информация о годовом платеже присутствует
    2. Отправить запрос на получение информации о кредите, указав мужской пол, возраст + сумма погашения = 61
    #### OP 
        Кредит одобрен, информация о годовом платеже присутствует
    3. Отправить запрос на получение информации о кредите, указав мужской пол, возраст + сумма погашения = 64
    #### OP 

- ### [TC02.1.2] Мужчина, Возраст + срок погашения превышают пенсионный
    - #### Шаги
   1.Отправить запрос на получение информации о кредите, указав мужской пол, возраст + сумма погашения = 65
    #### OP 
        Кредит не одобрен
    1. Отправить запрос на получение информации о кредите, указав мужской пол, возраст + сумма погашения = 66
    #### OP 
        Кредит не одобрен
    2. Отправить запрос на получение информации о кредите, указав мужской пол, возраст + сумма погашения = 80
    #### OP 
        Кредит одобрен

- ### [TC02.1.3] Женщина, Возраст + срок погашения не превышают пенсионный
    - #### Шаги
    1. Отправить запрос на получение информации о кредите, указав мужской пол, возраст + сумма погашения = 30
    #### OP 
        OP Кредит одобрен, информация о годовом платеже присутствует
    2. Отправить запрос на получение информации о кредите, указав мужской пол, возраст + сумма погашения = 59
    #### OP 
        Кредит одобрен, информация о годовом платеже присутствует

- ### [TC02.1.4] Женщина, Возраст + срок погашения превышают пенсионный
    - #### Шаги
    1. Отправить запрос на получение информации о кредите, указав женский пол, возраст + сумма погашения = 60
    #### OP 
        Кредит не одобрен
    2. Отправить запрос на получение информации о кредите, указав женский пол, возраст + сумма погашения = 61
    #### OP 
        Кредит не одобрен
    3. Отправить запрос на получение информации о кредите, указав мужской пол, возраст + сумма погашения = 70
    #### OP 
        Кредит не одобрен

- ### [TC02.2.1] Результат деления запрошенной суммы на срок погашения в годах <= трети годового дохода
    - #### Шаги
    1. Отправить запрос на получение информации о кредите, указав, результат, равный трети годового дохода
    #### OP 
        Кредит одобрен, информация о годовом платеже присутствует
    2. Отправить запрос на получение информации о кредите, если результат меньше трети годового дохода
    #### OP 
        Кредит одобрен, информация о годовом платеже присутствует


- ### [TC02.2.2] Результат деления запрошенной суммы на срок погашения в годах > трети годового дохода
    - #### Шаги
    1. Отправить запрос на получение информации о кредите, указав мужской пол, возраст + сумма погашения = 70
    #### OP 
        Кредит не одобрен

- ### [TC02.3.1] Если кредитный рейтинг -2, кредит не выдаётся
    - #### Шаги
    1. Отправить запрос на получение информации о кредите, указав кредитный рейтинг -2
    #### OP 
        Кредит не одобрен

- ### [TC02.4.1] Если в источнике дохода указано "безработный", кредит не выдаётся
    - #### Шаги
    1. Отправить запрос на получение информации о кредите, указав в источнике дохода "безработный"
    #### OP 
        Кредит не одобрен

- ### [TC02.5.1] Годовой платёж (включая проценты) больше половины дохода
    - #### Шаги
    1. Отправить запрос на получение информации о кредите, подобрав данные таким образом, чтобы годовой платеж был меньше половины дохода
    #### OP 
        Кредит не одобрен

- ### [TC02.5.2] Годовой платёж (включая проценты) больше половины дохода <= половине дохода
    - #### Шаги
    1. Отправить запрос на получение информации о кредите, подобрав данные таким образом, чтобы годовой платеж был меньше половины дохода
    #### OP 
        Кредит не одобрен