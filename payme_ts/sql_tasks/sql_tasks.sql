/*
    Task 1:
    Calculate the total sales amount and the total number of transactions for each month.
 */
select
    to_char(transaction_date, 'YYYY-MM')                        as month -- Вытаскиваем месяц из даты
,   count(transaction_id)                                       as count_of_transactions -- считаем кол-во транзакций
,   round(cast(sum(s.quantity * p.unit_price) as numeric),2)    as total_amount -- считаем сумму транзакций
from sales_transactions as s
    join products as p on s.product_id = p.product_id
group by 1
order by 1;


/*
    Task 2:
    Calculate the 3-month moving average of sales amount for each month.
    The moving average should be calculated based on the sales data from the previous 3 months (including the current month).
 */
with tab_1 as (
        select
            date_trunc('month', transaction_date)::date                                         as month -- Вытаскиваем месяц из даты
        ,   round(cast(sum(s.quantity * p.unit_price) as numeric),2)                            as total_amount -- считаем сумму транзакций
        from sales_transactions as s
            join products as p on s.product_id = p.product_id
        where 1=1
            and transaction_date between '2024-11-01' and '2025-01-31' -- фильтруем данные за последние 3 мясяца
        group by 1
    )
select
    to_char(month, 'YYYY-MM')                                                                   as month
,   round(avg(total_amount) over (order by month rows between 2 preceding and current row),2)   as moving_avg -- считаем скользящее среднее за 3 месяца включая текущий
from tab_1
order by 1;