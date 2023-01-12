/*
 Завдання на SQL до лекції 03.
 */


/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/
SELECT
    c."name" AS category, count(*) AS cnt
FROM
    public.film_category AS fc
        INNER JOIN
    public.category AS c ON fc.category_id = c.category_id
GROUP BY
    fc.category_id, c."name"
ORDER BY
	cnt DESC;



/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
SELECT
    a.first_name AS fname, a.last_name AS lname, SUM(fr.cnt) AS sum_rent
FROM
    public.film_actor AS fa
        INNER JOIN
    public.actor AS a ON fa.actor_id = a.actor_id
        INNER JOIN
--	= Визначення кількості прокатів за кожним фільмом
	(SELECT
	    i.film_id AS film_id, count(*) AS cnt
	FROM
	    public.inventory AS i
	        INNER JOIN
	    public.film AS f ON i.film_id = f.film_id
	        INNER JOIN
	    public.rental AS r ON i.inventory_id = r.inventory_id
	GROUP BY
	    i.film_id) AS fr ON fa.film_id = fr.film_id
GROUP BY
    fa.actor_id, a.first_name, a.last_name
ORDER BY
	sum_rent DESC
LIMIT 10;



/*
3.
Вивести категорію фільмів, на яку було витрачено найбільше грошей 
в прокаті
*/
SELECT
	c."name" AS category, SUM(p.amount) AS rental_payment
FROM
	public.inventory AS i
	    INNER JOIN
	public.film AS f ON i.film_id = f.film_id
	    INNER JOIN
	public.rental AS r ON i.inventory_id = r.inventory_id
	    INNER JOIN
	public.payment AS p ON r.rental_id = p.rental_id
	    INNER JOIN
	public.film_category AS fc ON f.film_id = fc.film_id
        INNER JOIN
    public.category AS c ON c.category_id = fc.category_id
GROUP BY
	fc.category_id, c."name"
ORDER BY
	rental_payment DESC
LIMIT 1;



/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/
SELECT
    f.title AS film
FROM
    public.film AS f
WHERE
	NOT EXISTS(	SELECT
					1
				FROM
					public.inventory AS i
				WHERE
					f.film_id = i.film_id);



/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
SELECT
    a.first_name AS fname, a.last_name AS lname, count(*) AS cnt
FROM
    public.film_actor AS fa
        INNER JOIN
    public.actor AS a ON fa.actor_id = a.actor_id
	    INNER JOIN
	(SELECT
	    f.film_id AS film_id
	FROM
	    public.category AS c
	        INNER JOIN
	    public.film_category AS fc ON c.category_id = fc.category_id
	        INNER JOIN
	    public.film AS f ON fc.film_id = f.film_id
	WHERE
		c."name" = 'Children') AS fi ON fa.film_id = fi.film_id
GROUP BY
    fa.actor_id, a.first_name, a.last_name
ORDER BY
	cnt DESC
LIMIT 3;
