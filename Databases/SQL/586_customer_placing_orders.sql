select customer_number as customer_number from Orders group by customer_number having count(customer_number)>=ALL (
    select count(customer_number) from Orders GROUP by customer_number
)